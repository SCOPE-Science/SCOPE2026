---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Use φ(ψ(n))/n=[φ(ψ(n))/ψ(n)]∏_{p|n}(1+1/p). If n even but not 2, 6|ψ(n), so first factor≤1/3, and five-prime product≤(3/2)(4/3)(6/5)(8/7)(12/11)=1152/385<3. If n odd, 2|ψ(n); if 5∤n the product≤(4/3)(8/7)(12/11)(14/13)(18/17)=4608/2431<2. If 5|n, 6|ψ(n) and product≤(4/3)(6/5)(8/7)(12/11)(14/13)=1536/715<3. These exhaustive cases yield strictness except n=2; n=2 gives equality. Independently factored n=39270=2·3·5·7·11·17, ψ=124416 and φ(ψ)=41472>39270. Bounds apply to arbitrary prime exponents; source finite sieve through 200000 is not the proof.

## originality

PASS

Sándor 2005 exact primary full text Theorem 3.23 proves reduction to squarefree kernel and Remark 3.26 records counterexample 39270; this does not imply that no infinitely large five-prime-support n can fail. The new five-prime uniform bound closes that gap, not discovery of 39270. OEIS A196200 tabulates numerical counterexamples only, and asymptotic density results do not imply minimal support.

## value

PASS

The least prime-support number of a counterexample to a historically conjectured multiplicative-function inequality is a natural structural invariant. Establishing exactly six by ruling out infinitely many lower-support inputs has mathematical significance beyond verifying a first numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
