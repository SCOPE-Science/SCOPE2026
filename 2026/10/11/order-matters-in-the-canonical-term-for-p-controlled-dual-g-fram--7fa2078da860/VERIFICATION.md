---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For A=P T_Λ, the frame operator is AA*=P S_Λ P and the minimal-norm right inverse is A*(AA*)^{-1}=T_Λ* P (P S_Λ P)^{-1}. All bounded right inverses differ by an operator with image in ker A. Coordinates therefore give Γ_j=Λ_j P S_{PΛP}^{-1}+T_j, A T=0. The published term Λ_j S_{PΛP}^{-1}P reconstructs P S_Λ P^{-1}S_Λ^{-1}, equal to I iff [P,S_Λ]=0. In the exact two-dimensional witness S_Λ=diag(1,2), P=[[2,1],[1,2]], this reconstruction is [[2/3,1/3],[-2/3,7/6]], not I. P has eigenvalues 1 and 3. This proves general equivalence and a valid counterexample, not merely numerics.

## originality

PASS

The 2019 equal-control g-frame literature already has the correctly ordered canonical term; therefore that isolated operator expression is not novel. The genuinely separate claim identifies the 2023 Theorem 4.3 reversed-order error, determines the exact commutation iff for its formula, and provides a concrete admissible noncommuting counterexample. Resultary returned the target item and adjacent controlled-frame corrections, but not a distinct prior correction to this theorem. An unindexed erratum remains possible.

## value

PASS

A published characterization of all controlled dual g-frames would be mathematically false under its printed general hypotheses. Isolating the exact commutation condition and an admissible 2x2 obstruction repairs a substantive statement used for frame reconstruction; this is more than an arbitrary type check, although the general right-inverse algebra is familiar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
