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

If an initial set contains a spine vertex \(x\) or \(y\), the domination step observes that spine and one internal vertex on every page, after which each page forces through. With no spine vertex selected, any touched page becomes fully observed and can ensure both spine vertices are observed. If at most one page is untouched, a spine vertex then has a unique unobserved neighbor in that page and propagation finishes; if at least two pages are untouched, each spine vertex has at least two unobserved page neighbors and the process stalls. Thus the iff criterion is correct. Counting a nonempty spine choice gives \(q(x)(1+x)^{2r}\) with \(q(x)=x(x+2)\); touching all pages gives \(q(x)^r\); omitting exactly one page gives \(r q(x)^{r-1}\). The package verifier independently simulates power domination on every subset for \(2\le r\le8\), checks every coefficient, the total count, and the minimum-set count.

## originality

PASS

The complete 2018 primary article defines the power-domination polynomial, gives structural decompositions, and computes paths, cycles, wheels, stars, complete graphs, and selected coronas, but contains no book-graph treatment. Its concluding questions explicitly call for counting power-dominating sets of further nontrivial families. The 2025 graph-entropy paper defines the same \(C_4\)-book and computes domination entropy for it, while its power-domination section treats other named families; the inspected book section does not supply the audited power-domination polynomial. Resultary search likewise returned no prior book power-domination polynomial.

## value

PASS

Book graphs are a standard infinite family and the power-domination polynomial is an established refinement of the monitoring parameter. The theorem gives every feasible set by a simple page criterion, the complete polynomial, total count, and exact minimum-set classification. This supplies a reusable named-family benchmark rather than a tiny-instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
