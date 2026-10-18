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

Normalize A to contain zero. The convolution identity at a∈A and nonnegativity force h(t)=0 on (A-A)\{0}. For every remaining x∉A the unknown values on allowed shifts solve integer incidence M_A h=ones. The standalone exact checker constructs each of the five group tables and iterates every one of the 2^15 normalized nonempty subsets; for every case, either allowed shifts fail coverage, an explicit compatible complement exists, or integer elimination finds rank_Q[M|1]>rank_Q M. Rational inconsistency excludes all real, hence nonnegative, solutions. Direct converse takes h=1_B for a tiling complement containing zero. I independently read and reran the complete deterministic Python checker, which terminated successfully with 163840 subsets and exact tile counts 1,15,95,139,1;1,15,183,371,1;1,15,311,387,1;1,15,359,787,1;1,15,455,1395,1. Exhaustiveness depends on transparent loop and exact group construction, not a sampled finite experiment.

## originality

PASS

The primary Kiss--Matolcsi--Matolcsi--Somlai theorem defines normalized positive-definite weak tiling and proves low-dimensional elementary p-group results, not the five order-16 types without Fourier positivity. An earlier complete F2^4 census establishes one of the five cases exactly (counts 1,15,455,1395,1) and is acknowledged as known. Spectral/Fuglede censuses for Z4² and Z4×Z2² concern spectral sets rather than arbitrary nonnegative normalized weak complements. The other four group types and all-order-16 classification survive direct implication checks.

## value

PASS

A complete cutoff over the natural five isomorphism classes at order 16 addresses whether normalized weak tiling rigidifies to an actual translational factorization. It is an exact full finite classification with nontrivial rational-infeasibility certificates; dropping positive definiteness is a substantive strengthening, and the known F2^4 component is explicitly not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
