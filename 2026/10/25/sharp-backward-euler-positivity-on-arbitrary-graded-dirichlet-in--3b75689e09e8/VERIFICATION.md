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

The exact tridiagonal stiffness and consistent mass entries are correct. A=M+tau K is SPD and strictly diagonally dominant, so leading minors and right Schur pivots are positive. The 2x2 Schur elimination of Au=M e_j gives the explicitly positive nearest-neighbor numerator tau[1/2+a/(6b)+b/(3a)+(e/gamma)(a/(6b)-b/(6a))] with |e/gamma|<1. The tridiagonal inverse ratio forces negative P_{i,i+2} or P_{n,n-2} when any interior c_i=h_{i+1}/6-tau/h_{i+1}>0; Stieltjes inverse positivity and M>=0 prove sufficiency. The tau=0 and n=1,2 endpoints are explicit. A separate exact-rational solver checked 480 cases and 128 subthreshold witnesses. The unlimited quantifiers rest on the proof, not these cases.

## originality

PASS

Qualified best-of-knowledge original: the source theorem upgrades known time-step Stieltjes sufficiency to exact necessity for every individual arbitrary graded Dirichlet interval with at least three interior nodes and proves positive nearest-neighbor entries. A specifically relevant 2008 Thomée–Wahlbin article could not be read in full; its abstract does not decide the exact backward-Euler classification, which remains a priority risk. Yang–Gu 2006 explicitly analyzes minimum steps for accuracy rather than this positivity iff.

## value

PASS

A sharp easily computed one-step positivity phase boundary for the standard consistent-mass finite-element heat solver on every graded interval, with a minimal dimension, exceptional low dimensions, and the non-obvious irrelevance of boundary element lengths, is a structurally useful mesh-design and monotonicity fact. This is more than a generic sufficient M-matrix test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
