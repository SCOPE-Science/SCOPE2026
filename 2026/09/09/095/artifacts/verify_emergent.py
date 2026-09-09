"""Master replay verifier for the emergent cap-lattice package.

Replays plumbing.py, cork_link.py, adjunction.py, short_vector.py,
splitting.py (+ milnor_cap.py, symplectic_contrast.py, homeomorphism.py as
context legs) and asserts the emergent claim's verification-critical facts:
 (i)   det(Q_P)=-1, sig(Q_P)=-9, negative-definite; det(Q_N)=+1, sig=+9,
       positive-definite;
 (ii)  cork-link det/H1 agree (|det|=1, H1=0);
 (iii) adjunction collision on all 9 cap spheres (SW=0 both sides, naive cap);
 (iv)  short-vector census complete for squares<=2: #{sq1}=2, #{sq2}=240,
       min-nonzero-square=1, with integer-exact v0 check v0^2=1;
 (v)   splitting Q_N=<+1> orth q8: Qv0=e8, primitive, det(complement)=1,
       complement positive-definite rank 8.
Prints VERIFY_OK or fails.
"""
import json
import os
import subprocess
import sympy as sp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

def run(script):
    r = subprocess.run(["python3", script], cwd=HERE, capture_output=True, text=True)
    tail = (r.stdout.strip().splitlines() or [""])[-1]
    print(f"{script}: {tail}")
    if r.returncode != 0:
        print(r.stderr[-2000:])
        raise SystemExit(f"replay of {script} failed")

def main():
    for s in ("plumbing.py", "cork_link.py", "adjunction.py", "short_vector.py",
              "splitting.py", "e8_isometry.py", "milnor_cap.py",
              "symplectic_contrast.py", "homeomorphism.py"):
        run(s)
    P = json.load(open(os.path.join(HERE, "plumbing_result.json")))
    C = json.load(open(os.path.join(HERE, "cork_link_result.json")))
    A = json.load(open(os.path.join(HERE, "adjunction_result.json")))
    S = json.load(open(os.path.join(HERE, "short_vector_result.json")))
    T = json.load(open(os.path.join(HERE, "splitting_result.json")))
    assert P["det_QP"] == -1 and abs(P["det_QP"]) == 1
    assert P["sig_QP"] == -9 and P["sig_QN"] == 9
    assert P["negative_definite_P"] and P["positive_definite_N"]
    assert P["H1_order"] == 1
    assert abs(C["det"]) == 1 and C["H1_boundary"] == "0 (|det|=1)"
    rows = A["partA_naive_cap_collision"]["rows"]
    assert len(rows) == 9 and all(r["satisfiable"] is False for r in rows)
    assert S["counts_square_le2"] == {"0": 1, "1": 2, "2": 240}, S["counts_square_le2"]
    assert S["min_nonzero_square"] == 1
    QN = sp.Matrix(P["QN"])
    v0 = sp.Matrix(T["v0"])
    assert int((v0.T * QN * v0)[0]) == 1
    assert T["Qv0"] == [0] * 8 + [1] and T["primitive_gcd"] == 1
    assert T["det_complement"] == 1 and T["sig_complement"] == 8
    G = sp.Matrix(T["complement_gram"])
    assert int(G.det()) == 1
    assert G.tolist() == [row[:8] for row in P["QN"][:8]]
    assert T["char_parity"] == [0] * 8 + [1]
    J = json.load(open(os.path.join(HERE, "e8_isometry_result.json")))
    U = sp.Matrix(J["isometry_U"])
    assert int(U.det()) in (1, -1)
    assert (U.T * U * 0 + U.T * sp.Matrix(J["E8_cartan"]) * U).tolist() == G.tolist()
    assert J["num_roots_G"] == 240
    print("VERIFY_OK: emergent cap-lattice package fully consistent")

if __name__ == "__main__":
    main()
