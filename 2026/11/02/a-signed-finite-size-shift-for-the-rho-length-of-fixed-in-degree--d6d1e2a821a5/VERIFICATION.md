---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a uniform map with n divisible by fixed d>=2 and exactly n/d indegree-d targets, prescribing k distinct image targets has probability product b_vi/(n)_k. A uniform starting point not among those targets contributes (n-k)/n. Summing ordered k-subsets gives survival S_n(k)=(1-k/n) d^k binom(n/d,k)/binom(n,k), zero above n/d. With a=d-1, logarithmic expansion for k<=sqrt(n)log n gives -a k^2/(2n)+(a/2-1)k/n-(d^2-1)k^3/(6n^2) plus a summably O(n^-1/2) error; the inequality S_n(k)<=exp[-a k(k-1)/(2n)] handles the upper tail. Half-line Euler–Maclaurin gives E[R]=sqrt(pi n/(2a))+1/2+(a/2-1)/a-(d^2-1)/(3a^2)+O_d(n^-1/2) = sqrt(pi n/(2(d-1)))+(2d-7)/(3(d-1))+O_d(n^-1/2). Independently enumerated every admissible map and start at (n,d)=(4,2),(6,2),(6,3), and independently evaluated means through n=40000. This verifies but does not prove uniform infinite bounds.

## originality

PASS

Leckey–Wormald supplied the general exact path enumeration and leading Rayleigh distribution/moment limit, which are expressly prior art. Only the explicit subleading constant and d-dependent sign are assessed as possibly new. Martins–Panario earlier studied polynomial-vs-restricted-map expected rho lengths and is particularly relevant, but full paper remained unavailable after OA/arXiv and authorized Oxford attempts; its abstract is insufficient for a whole-paper exclusion and is a real priority risk.

## value

PASS

The order-one first-repeat bias is a natural next-order invariant of restricted-indegree random mappings, benchmarks for polynomial iteration and birthday/Pollard heuristics. It changes sign between d=3 and d=4 even when all classes have the leading Rayleigh square-root scale; an explicit O(n^-1/2) error and complete degree classification are informative for finite-size comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
