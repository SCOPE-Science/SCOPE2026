---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Read and checked the exact spectral premises in Golla–Osaka–Sequeira Theorem 2.2 and Corollary 2.17: complete orthogonal pure-point eigenbasis with no infinite strictly increasing distinct eigenvalues characterizes the norm-attaining-every-reducing-subspace positive class, and no infinite strictly decreasing sequence characterizes the minimum-attaining class. A nondecreasing scalar map preserves both sequence exclusions; nonincreasing swaps them. Strict monotonicity has a continuous inverse on f([0,R]), so functional calculus reflects each class. Necessity: every violation of oriented monotonicity yields strictly monotone bounded diagonal eigenvalue sequences with unattained extremal f-level by a continuity crossing construction; flat nondegenerate intervals yield f(A) scalar while A fails reflection. Counterexamples live on l2, never finite truncations. No external computation or mere samples are taken as proof.

## originality

PASS

The primary 2026 spectral classification and its special affine duality A->delta I-A are correctly prior. The complete universal continuous scalar map classification and all strict reflection converses are not an immediate restatement of affine duality; explicit crossing/flat-map witnesses establish sharp necessity. Prior paper on functional calculus of the smaller absolutely norm-attaining class may overlap in methods, but does not establish coverage of this operator class in accessible material.

## value

PASS

Sharp functional-calculus stability and rigidity classification for two natural complementary reducing-subspace attainment classes, including all continuous nonsmooth functions and necessary direction/exchange. This is a reusable structural theorem rather than a known spectral equivalence relabeled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
