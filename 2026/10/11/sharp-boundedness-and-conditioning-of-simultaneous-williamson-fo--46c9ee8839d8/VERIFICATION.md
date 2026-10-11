---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the sharp boundedness criterion

The analytical check is the exact identity \(T=JC=S^{-1}J(D\oplus D)S\) for every proposed bounded symplectic congruence and the contraction bound for the regularized polar factor \(K_\varepsilon=T(-T^2+\varepsilon I)^{-1/2}\). Direct multiplication gives \(-T^2=M_{c^2pq}\oplus M_{c^2pq}\) and the norm of \(K_\varepsilon\). Its monotone limit is \(\sqrt R\) without requiring any bounded inverse of \(C=A+B\). The explicit diagonal squeezing map meets the bound when \(R<\infty\).

Execute `python3 verify.py` with Python 3 standard library to check the two-coordinate symplectic identities, both congruences, and condition number on a finite nonuniform coefficient family. That finite check is illustrative and cannot certify the infinite result. No external formal proof or independent audit has been performed. Critical logical assumptions are strict positivity almost everywhere of \(p,q,a+b\), essential boundedness of all four weighted coefficients, and bounded invertibility of each normalizer being optimized.
