---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Fresh enumeration checked the defining separation condition on all 296010 six-subsets of the 27 possible columns and all 888030 seven-subsets. Exactly 36 six-subsets are valid and no seven-subset is valid, so heredity gives the sharp maximum six. Applying all 1296 standard row/symbol transformations to the 36 maxima gives one orbit of size 36, hence stabilizer 36. This independently reconstructs the package's certificate without relying on its stored classification file.

## originality

PASS

Existence of a six-column \(\operatorname{PHF}(3;6,3,3)\) is old and appears in Kim's thesis and Walker–Colbourn's construction tables. Walker–Colbourn explicitly describe their tables as best-known construction/upper-bound data for the row number rather than exact extremal classifications in general. No inspected source proves that seven columns are impossible, counts the 36 labeled six-column families, or proves they are one equivalence orbit. Those are the audited contributions.

## value

PASS

The three-row ternary case is the smallest genuinely nontrivial perfect-hash parameter where a six-column construction has long been known but an exact all-family census is not supplied by the standard tables. Closing the upper bound and proving one-orbit rigidity is a natural finite classification with clear reference value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
