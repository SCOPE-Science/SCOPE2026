---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For finite Blaschke B degree N, b=B(0), 0<r<1, T=S_B, v=(B-b)/z, backward shift invariance gives I-T*T=v⊗v and telescoping defect I-(T^k)*T^k=sum_{ell=0}^{k-1}(T^{*ell}v)⊗(T^{*ell}v). Its rank <=k forces >=N-k singular values exactly 1. Trace telescoping and Taylor-coefficient tails yield Tr|T^k|²=N-k+kr²+sum_{j=1}^{k-1}(k-j)|b_j|². With det modulus |det T^k|=r^k, the remaining k singular values have product r^k, so AMGM for all p>0 yields Tr|T^k|^p>=N-k+kr^p, equality iff all k remaining singular values r, equivalently b1..b_{k-1}=0 by exact p2 excess. Frostman disk automorphism factorizes all equality products B=(b+z^k C)/(1+conj(b)z^k C) with C finite Blaschke degree N-k. For k=N zeros form a regular N-gon of radius r^(1/N). Independent NumPy Szego-kernel Gram construction for a degree-three regular-zero example with r=1/8 gives exact singular profiles (1,1,1/8), (1,1/8,1/8), (1/8,1/8,1/8) for k1,2,3; confirms finite instance only.

## originality

PASS

General finite TTO Schatten membership is automatic and known; exact jet-weighted Hilbert-Schmidt excess, simultaneous all-positive-power fixed-value minimization and complete Frostman equality classification were not identified in inspected primary prior work.

## value

PASS

Classifying simultaneous Schatten-power minimizers and the complete initial Taylor-jet equality condition of finite Hardy compressed shifts supplies a natural exact structural theorem in operator theory. The weighted Hilbert–Schmidt defect and Frostman parameterization extend beyond a bare textbook AMGM lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
