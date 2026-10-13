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

The symbolic proof in `RESULT.md` establishes the universal theorem. The executable artifact `verify.py` checks representative instances of each logical branch:

- a case with \(p(0)\ne0\) and \(p\mid q\), where domination must hold;
- a case with \(p(0)=0\) and \(tp\mid q\), where domination follows from a two-sided factorization;
- a case with \(p(0)=0\), \(p\mid q\), but \(tp\nmid q\), where the explicit nilpotent witness violates domination;
- a case where \(p\nmid q\), where a Jordan block violates domination;
- the matrix identity underlying \(q(yx)=y\,p(xy)\,x\,r(yx)\).

The finite checks do not certify the universal quantifiers; they only replay algebraic consequences on small exact test spaces. The nonmembership argument is the explicit infinite-dimensional shift representation given in `RESULT.md`.

Expected final verifier line: `CHECK_OK`.
