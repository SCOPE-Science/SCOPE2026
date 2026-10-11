---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fresh endpoint-reduced integer enumeration independently gives unique reduced optima (1,6,6,0,36,0,216,0,1296,0), (1,7,7,0,49,0,343,0,2401,0), and (2,7,12,2,88,0,640,0,4656,0) with values 7776, 16807 and 33872. The affine x5 coefficient is strictly positive at all three winning prefixes, and the x4 coefficient is also strictly positive there, so no omitted interior split ties the optimum. Proposition 11 of the primary paper applies because q>2 and gives counts 14, 16 and 6552; for q=9 one orientation has C(9,2)C(14,12)=3276 choices and reversal doubles it. The primary paper explicitly states that under its Proposition-11 hypotheses no code is double counted.

## originality

PASS

The 2024 source supplies the exact SQN framework, counting formula and computations only through q=6 in the published nonbinary table. The audited q=7,8,9 cells are the next three alphabet sizes; fresh search found no external source stating the values, complete counts or optimal profiles. A later same-repository record repeats only the three S-values, but repository history shows the present stronger record was imported first and is its ancestor, so that later duplicate does not negate priority.

## value

PASS

These are the first three alphabet sizes immediately beyond the published length-six nonbinary table. The q=9 cell marks a genuine transition away from the simple Blackburn k=5 extremal form, and the complete maximum-code counts/profiles make that transition structurally informative rather than a bare numerical extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
