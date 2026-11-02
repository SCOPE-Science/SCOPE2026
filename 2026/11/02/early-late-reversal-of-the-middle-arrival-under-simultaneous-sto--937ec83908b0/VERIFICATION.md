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

# Verification scope

The mathematical claim, its hypotheses, and complete proof are in `RESULT.md`. All numerical experiments are illustrative finite checks, not infinite-time proof or independent certification.

## Reproduction

Install the packages listed in `requirements.txt`, then execute `OPENBLAS_NUM_THREADS=1 python verify.py` from this directory. The check program evaluates the reset-free survival-transform identity via numerical quadrature; verifies finite binomial counting, strict convex comparisons and the one-reset short-time bound; solves two scalar renewal-pole equations at three distance values; checks the strict exponent gap; and discretizes the three joint-survival Volterra equations to compare short- and long-horizon median-arrival probabilities at \(D=d=r=1\).

The executed local run returned `PASS: 154 numerical and finite-algebra checks`, with renewal poles \(0.489409173023\) and \(0.874957794252\), and strict separation \(0.103860551795\). Numerical renewal discretization has a finite grid step and is not an exact identity. Analytical renewal and Jensen arguments prove the general conclusions for all strictly positive parameters.

## Unproved or unchecked limits

No exact crossing time or uniqueness claim is made. No finite-size empirical validation, random-parameter coverage, or global survey of every earlier article is claimed. The numerical program does not certify the key renewal theorem, the absence of a stronger unpublished result, or full independent priority.
