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
# Verification

The focal source was checked at the exact definition of \(F_t\), \(H\), and \(\|\cdot\|_\theta\), and at equations (5.1)–(5.2) and Proposition 5.2. The source verifies the lower-bound vectors and homogeneity used by the proof.

For the new upper bound, let \(y\) have support size at most \(k\) and normalize \(\|y\|_1=1\). For \(0<t<1\), the coordinate part of \(F_t(y)\) is at most the entropy \(\sum r_j\log(1/r_j)\le\log k\), while the correction term has modulus at most \(1/e\). For \(t\ge1\), \(F_t(y)=0\). Scaling back yields \(H(y)\le\|y\|_1(\log k+1/e)\), and hence the claimed coordinate-projection bound.

No finite enumeration, numerical optimization, or external certificate is used. The unresolved scientific limit is the exact leading coefficient of \(k_m(\theta)\), which is not claimed.
