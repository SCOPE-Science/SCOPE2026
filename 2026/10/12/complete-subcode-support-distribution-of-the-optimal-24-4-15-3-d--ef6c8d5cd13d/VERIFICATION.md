---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The exact defining-set code C_D1 is evaluation of Tr_27/3(ax)+b on F27\F3, with F27=F3[X]/(X³+2X+1). Verified modulus has no F3 root, the trace realization, 24 coordinates and rank-four linear message map. An independently written RREF generator enumerated exactly 40+130+40+1=211 nonzero message subspaces (one per linear subcode), computed each union of codeword supports from basis vectors and recovered N1={15:8,16:27,18:4,24:1}; N2={21:80,22:36,24:14}; N3={23:24,24:16}; N4={24:1}. These all add to the Gaussian binomial counts and have minima (15,21,23,24), matching the primary article Examples 3.4/3.8. This is exhaustive over this finite-dimensional code; no uniform family generalization inferred.

## originality

PASS

The inspected primary paper explicitly states the exact codeword enumerator and generalized Hamming hierarchy but does not enumerate subcode-support multiplicities or nonminimal support layers. Other published defining-set and Solomon–Stiffler/subcode-distribution papers may count different families; no direct implication giving these 211-subspace multiplicities for this exact F27\F3 affine slice was found.

## value

PASS

The exact multiplicity of each generalized-support weight, not just the minima, is a natural invariant of this highlighted optimal self-orthogonal [24,4,15] code. The 80 two-dimensional minimizers and 24 three-dimensional minimizers and all non-minimal layers are concrete inputs for code incidence, secret-sharing and equivalence questions; a complete natural 211-subcode census can be independently useful without a family-wide theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
