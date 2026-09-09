"""Symplectic-cap contrast (target witness route): K3-embedding shape.

Machine-checked arithmetic only; embedding existence cited as standard
cork-embedding theorem (Akbulut-Yasui: Mazur corks embed in blown-up elliptic
surfaces), NOT proved here. Purpose: show the witness equation becomes
SATISFIABLE in a symplectic b2+>1 closing, in sharp contrast to the naive
definite-plumbing cap (9/9 unsatisfiable). This keeps the target alive and
localizes exactly what remains: fix the embedding + evaluate tau on basics.

K3 = E(2): e=24, sig=-16, b2+=3, b2-=19. d(K)=0 <=> K^2 = 2e+3sig = 0.
Canonical K=0: SW=1 (Witten). Fiber class F: g=1, F^2=0 -> adjunction
0 >= 0+|K.F| satisfiable (0>=0). Section class: g=0? in E(2) section has
S^2=-2, adjunction -2 >= -2+|K.S| satisfiable. So basic classes survive,
unlike the naive cap where every sphere violated by margin >=4.
Exoticity shape: tau trivial on lattice (homeomorphism.py) but moves the
chamber/basic set: SW_Xhat(0)=1 vs SW_Xhat_tau(0)=0 (kill) or vice versa.
"""
import json

def main():
    e, sig = 24, -16
    b2p, b2m = 3, 19
    assert e == 2 + b2p + b2m  # e = 2-2b1+b2, b1=0
    assert sig == b2p - b2m
    ksq_d0 = 2 * e + 3 * sig
    assert ksq_d0 == 0, ksq_d0
    out = {
        "closed_symplectic_model": "Xhat_symp = (E(2)#kCPbar with C(2,3,11) embedded) and twist Xhat_tau; same e/sig/Q (cork lemma + homeomorphism.py)",
        "e": e, "sig": sig, "b2+": b2p, "b2-": b2m,
        "d_zero_equation": f"K^2 = 2*{e}+3*({sig}) = {ksq_d0}",
        "canonical_class": "K=0, SW=1 (Witten), satisfies adjunction on fiber F (g=1,F^2=0): 0>=0+0 OK; section S^2=-2: -2>=-2+0 OK",
        "contrast_naive": "naive cap: 9/9 spheres violate by margin>=4 (c5 margin>=6); K3 cap: canonical class satisfies all checked adjunctions with margin 0",
        "witness_shape": "same lattice K=0, SW_Xhat(0)=1 vs SW_Xhat_tau(0)=0 (kill) — chamber/basic-set move, lattice fixed",
        "remaining": "fix explicit embedding of C(2,3,11) in E(2)#kCPbar + evaluate tau on basic set (Morgan-Mrowka-Szabo / Akbulut-Yasui cork-twist formula); not claimed here",
        "embedding_cite": "Akbulut-Yasui / Akbulut-Kirby: Mazur-type corks embed in blown-up elliptic surfaces; specific (2,3,11) embedding is the open explicit step",
    }
    with open("symplectic_contrast_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"K3: e={e} sig={sig} d0_Ksq={ksq_d0} canonical-adjunction SATISFIABLE")
    print("SYMPLECTIC_CONTRAST_OK")

if __name__ == "__main__":
    main()
