---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For each u the determinant-one companion matrix has trace u; its characteristic polynomial splits with distinct roots or stays irreducible exactly according to the nonzero discriminant sign. The sign proof in RESULT.md lines 25–59 concerns one common starting trace t. For p>8 the union of roots is the nine distinct values −6 through 2, with only f_0 and f_4 sharing a root (−2). Off those roots the indicator product is either 32 or 0; on the roots it is at most 16. In the product expansion the nonempty subsets are nonsquares: eight containing {0,4} have precisely one repeated root, whose removal lowers the number of distinct simple roots in the squarefree kernel by two relative to nominal degree and adds at most one to the sum error. The others are squarefree. Summing the Weil coefficients gives 129−16=113 and summing both errors gives 144+8=152. Thus 32N≥p−113sqrt(p)−152, strictly positive at 14000 and increasing thereafter. Independent Python 3 replay at /workspace/branches/5aa5a643-178d-4769-bfe7-a3c43841a834/independent_check.py (output run.log) used Euler character values and the two translated linear factors, and exhausted all t for all 1651 odd primes below 14000, including 3, 5 and 7 where the analytic distinct-root assumption does not apply. It reproduced the complete forty-prime exception list, the sole all-minus gap at 233, and full support at 229 and 239. The next prime after 233 is 239. The replay verifies the bounded range, and the analytic inequality is needed for the infinite range. VERIFICATION.md and the supplied verify.py were inspected without executing author code.

## originality

PASS

The supported distinct claim is the simultaneous sharp prime cutoff, exceptional set and boundary obstruction for the five consecutive trace discriminants with their shared root. Nonzero discriminant classification and Weil expansion are established ingredients. The closest inspected indexed character-universality results use different polynomials or ordinary shifted linear arguments. No inspected statement supplies this exact five-product classification; this is not a proof of historical priority.

## value

PASS

Five is the first short consecutive window with an actual branch-root collision when p>8, giving a natural scope rather than an arbitrary slice. The exact prime cutoff and exception set determine when every five-coordinate sequence of regular split and nonsplit types is available at consecutive traces, which a generic asymptotic character bound does not decide. The unique last obstruction is a useful precise boundary witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
