---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The number of distinct adjacent-two-deletion descendants is 1+∑_{i=1}^{n−2}1_{x_i≠x_{i+2}}, because outputs y_i=y_j imply period two of the intervening source substring and equal-output blocks are contiguous. The binary difference map δ_i=x_i⊕x_{i+1}, δ_n=x_n is invertible, and the last bit selects a unique lift from syndrome modulo n to modulo 2n. The weighted transition enumerator F_n(q,z) is expressed through the 2×2 transfer product J D_i(q). For a root q of order d|n/2, d even, nonconstant cyclic rotation orbits cancel and constant orbits give tr P_d=0; det P_d=−(1−z²)^d implies P_d²=(1−z²)^d I and F_n(q,z)=2K. For primitive order n, reversal/complement pairs contributions with opposite q^{n/2} signs, giving F_n(q,z)=0. q=1 gives F_n=2G. Fourier inversion yields the claimed four-exceptional versus remaining 2n−4 syndrome classes. Independent exact enumeration of all words n=4,8,16 and separate DP at n=32 matched every coefficient, covering examples but not replacing the all-powers-of-two Fourier proof.

## originality

PASS

Xie–Sun–Ge 2026 Theorem VI.1 proves binary differential VT codes correct and cover two-burst deletions, hence the total |image| per syndrome is 2^(n−2); it does not give the individual codeword burst-deletion-ball-size distribution polynomial in the materially read primary full text. Earlier DVT size results do not logically determine this coefficientwise refinement. The new finite-parameter classification is original on checked evidence, with risk of implicit old transfer-matrix enumerators.

## value

PASS

The precise number of distinct outputs per codeword is a canonical invariant of the perfect two-burst deletion code, relevant to variable sphere geometry and decoding/covering heterogeneity. It refines the recently established global count into a full sharp two-class syndrome-conditional distribution for every power of two, not an arbitrary finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
