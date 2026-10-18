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
The polynomial equalities and the uniqueness proof in `RESULT.md` cover all integers \(a\ge2\), \(b\ge2\), \(d\ge1\) with \(\gcd(a,d)=1\). No external formal certificate is claimed.

Run `python verify.py` using Python 3 and no nonstandard dependencies. The script independently checks weights of every relation, compares reduced normal forms for all monomials up to weighted degree \(500\), and tests each relation's necessity using breadth-first connectivity of its finite weighted factorization fiber after removal of that relation. Tested ranges: \(2\le a\le23\), \(2\le b\le9\), \(1\le d\le12\) with the stated gcd condition; completed result: 1,320 settings and 2,294,527 factorization vectors, all passing.

Finite computations do not establish infinite correctness. The proof instead relies on a strictly descending reduction measure and uniqueness of the representatives with \(0\le y+(b+1)z<a\), which remains valid outside the tested range.
