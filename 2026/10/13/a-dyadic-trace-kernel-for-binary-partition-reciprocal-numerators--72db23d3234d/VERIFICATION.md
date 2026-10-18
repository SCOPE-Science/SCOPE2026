---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The pinned theorem defines the reduced binary numerator H_n as a partition sum for every n>=2. Degree d=sum_{k>=1}2^k floor(n/2^k) is common to every term. In Z/4Z[[x]], (1+x)^(2^k)=1+x^(2^k)+2x^(2^(k-1)) mod4 for k>=1. After multiplying first-order corrections and using B(n) even for n>=2, the marked-part generating series z^(2^k)/(1-z^(2^k))*B(z) yields C_k(n) mod2 exactly 1 for even n divisible by 2^k. This proves H_n/2=(1+x)^(d-2^t)*Q_(t,c) mod2; odd n pair to H_(n-1). The term j=t-1 uniquely survives Q(1), so root multiplicity is d-2^t, and coefficient x=2 mod4 establishes integer content exactly two. Independent exact integer-polynomial construction and bitwise F2 kernel compared EVERY coefficient for n=2..20, confirming congruence, sharp root and linear parity; these finite checks supplement the all-n parity proof. Root multiplicity is only in F2 on H_n/2, not over C.

## originality

PASS

The new claim was compared at the level of mathematical implication against the explicitly identified primary sources and Resultary findings. Existing core definitions/classical identities are credited; no stronger previously published result covering the precise new structure was found in material inspected, subject to named residual risks.

## value

PASS

The exact closed mod-four structure of the whole binary partition numerator and its high-multiplicity characteristic-two zero is a motivated structural refinement of current partition-polynomial research, distinct from its previously known exact but unsolved characteristic-zero recurrence and low-degree coefficient data. It gives every residue class of every coefficient and exact modular degeneracy for all indices; this is not a raw known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
