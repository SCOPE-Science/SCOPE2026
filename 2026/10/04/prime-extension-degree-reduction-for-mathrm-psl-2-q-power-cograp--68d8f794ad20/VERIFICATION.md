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

The proof correctly starts from the published admissibility criterion. For p=2, even f factors 2^f-1 into coprime nontrivial factors and modulo-three divisibility eliminates all but f=2,4; for odd composite f the proper divisor 2^a+1 and the 3-power analysis eliminate admissibility. For odd p, even f≠2 over p=3 creates incompatible 4- and 3-divisibility, while p=3 reduces to f=2. For odd composite f, the factor (p^a+1)/2 is already composite and Bang–Zsigmondy supplies an outside prime, excluding both prime-power and squarefree-semiprime forms. At odd prime f, primitive divisors force p>3 to have both consecutive integers (p-1)/2,(p+1)/2 prime, hence p=5; p=3 and 5 then reduce to the stated exact factors. An independent comparison of the source criterion and reduced criterion for all primes p≤19 and 2≤f≤12 found zero mismatches. The cited Zsigmondy applications avoid the classical exceptions.

## originality

PASS

Manna–Cameron–Mehatari already isolate the PSL₂(q) number-theoretic problem, including the characteristic-two even-degree exceptions q=4,16 and necessary conditions for odd degrees. Cameron–Manna–Mehatari subsequently prove the exact admissibility criterion for the two torus orders. The inspected literature does not carry this to the submitted global reduction: apart from q=16, composite extension degrees are eliminated, and in odd characteristic the base prime is forced to 3 or 5 with the stated exact residual primality conditions.

## value

PASS

The finite-simple-group classification explicitly leaves a number-theoretic search. Reducing every nonprime field, aside from one exception, to prime extension degree and forcing the odd-characteristic base to 3 or 5 removes a large infinite parameter region and replaces it by explicit residual primality conditions. This is a meaningful structural reduction of the stated open branch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
