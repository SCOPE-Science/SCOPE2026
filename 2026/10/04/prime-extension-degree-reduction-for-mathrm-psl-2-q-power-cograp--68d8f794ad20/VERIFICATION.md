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
The final theorem was checked against the exact published \(\mathrm{PSL}_2(q)\) cograph criterion.

Critical proof checks:
- for \(p=2\), even composite extension degree is excluded by \(2^{2m}-1=(2^m-1)(2^m+1)\), with the exact exceptions \(f=2,4\);
- for odd \(f\), \(2^f+1\) admissible forces \((2^f+1)/3\) prime, and composite odd \(f\) is impossible;
- \(2^f-1\) has no proper prime-power form for odd \(f\ge3\);
- for odd \(p\) and even \(f\), divisibility by \(4\) and \(3\) excludes \(p\ne3\), while the \(p=3\) factorization leaves only \(f=2\);
- for odd composite \(f\), a proper composite factor of \((p^f+1)/2\), together with a primitive divisor of \(p^{2f}-1\), excludes both admissible possibilities;
- for odd prime \(f\), primitive divisors force \((p-1)/2\) and \((p+1)/2\) to be consecutive primes unless \(p=3\), hence \(p=5\);
- substituting \(p=3\) and \(p=5\) yields exactly the displayed cyclotomic primality conditions.

The Bang--Zsigmondy applications use exponents \(f\ge3\) and \(2f\ge6\) with odd base \(p\), so neither classical exception applies.

`artifacts/verify.py` independently factors the relevant integers and compares the published criterion with the reduced criterion for \(p=2\), \(2\le f\le31\), and for \(p\in\{3,5,7,11\}\), \(2\le f\le9\). It returns `VERIFY_OK`.

Finite computation is not used to establish the universal statement.
