"""Milnor-fiber symplectic cap data for Y=Sigma(2,3,11) (target witness route).

Machine-checked: mu=(2-1)(3-1)(11-1)=20; Stein fiber M has chi=1+mu=21,
simply connected, bounds +Y (Brieskorn link theorem). Unimodularity
consequence: since Y is an integer homology sphere, H2-closed gluing keeps
unimodular Q. Parametric witness equation d(K)=0, i.e. K^2=2e+3sig, is
tabulated as a function (no invented closed-cap lattice claimed).
Cites standard theorems; only arithmetic is machine-checked.
"""
import json

def main():
    p, q, r = 2, 3, 11
    mu = (p - 1) * (q - 1) * (r - 1)
    assert mu == 20
    chi_M = 1 + mu
    out = {
        "singularity": "x^2+y^3+z^11=0, link Sigma(2,3,11)",
        "mu": mu,
        "chi_Milnor_fiber": chi_M,
        "topology_M": "simply connected Stein domain, b2=20, bounds +Y=Sigma(2,3,11) (Brieskorn; Gompf-Stein)",
        "boundary_H1": "0 (Y integer homology sphere; verified det=+-1 in plumbing_result.json)",
        "unimodularity_note": "any closed cap Xhat=C U Z with H1(Z)=lattice glue keeps det(Q)=+-1; Q shared by twist pair (Freedman/cork lemma)",
        "witness_equation_parametric": {
            "d(K)": "(K^2-2e-3sig)/4",
            "d_zero": "K^2 = 2e+3sig",
            "adjunction": "2g(S)-2 >= S^2+|K.S| for every embedded symplectic surface S in cap",
            "tau_action": "exoticity iff tau^*(basic set of X) != basic set of X_tau as labeled by homeomorphism identification",
        },
        "why_naive_failed": "definite plumbing cap N=-P has only g=0, S^2>0 spheres (adjunction kills all K); Milnor/Stein cap supplies higher-genus symplectic surfaces where (d=0 + adjunction) is satisfiable",
        "status": "cap existence + equation shape standard; finite K-enumeration awaits fixing the closed b2+>1 lattice (positive concave extension / blowups of M); not claimed here",
    }
    with open("milnor_cap_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"mu={mu} chiM={chi_M}")
    print("MILNOR_CAP_OK")

if __name__ == "__main__":
    main()
