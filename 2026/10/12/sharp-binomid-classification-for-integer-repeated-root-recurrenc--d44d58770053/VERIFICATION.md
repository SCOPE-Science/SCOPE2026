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

# Verification

The complete proof in `RESULT.md` derives the recurrence closed form and exact generalized coefficient identity, checks the constant/geometric and zero-initial branches, and constructs infinitely many denominator-prime witnesses using Dirichlet's theorem. The proof includes a separate direct witness for the failure of index divisibility.

Run `python3 verify.py` in a directory containing that file; only the Python standard library is used. The captured output is in `verify_output.txt`. Tests enumerate 800 parameter triples, check 17,632 positive-case coefficients, and verify 684 prime-witness instances using exact fractions, including the central valuation obstruction. The checks do not establish Dirichlet's theorem, the unbounded prime argument, or a complete infinite classification by enumeration; those follow from the mathematical proof.

Scientific comparison includes the open-access 2023 principal paper, original preprint publication date, relevant 2022 divisible-recurrence classification, and searches for exact or equivalent affine and repeated-root statements. The comparison cannot exclude all unindexed equivalent prior literature.
