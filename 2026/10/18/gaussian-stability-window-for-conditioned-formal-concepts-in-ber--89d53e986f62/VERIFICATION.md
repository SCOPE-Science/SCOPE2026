---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

On conditioning E=(A,B) formal concept, A×B all-one, every outside-B column not all-one on A, and every outside-A row not all-one on B constrain disjoint iid blocks. The N outside columns on A are independent Bernoulli-p vectors truncated at the all-ones vector. For |S|=t, Pr(S′=B|E)=((1-p^t)/(1-p^a))^N, and for S,T use 1-p^|S|-p^|T|+p^|S∪T|; summing indicators yields both moments. With independent U~uniform P(A), |U|~Bin(a,1/2), compare the indicator U′=B to |U|≥h. Outside width w=2 log a/(-log p), conditional mismatch is O(a^-2) or exp(-a²+o(1)); binomial anti-concentration in the width O(log a/√a) plus Berry–Esseen yields uniform bound. Independent exhaustive enumeration of all truncated column words confirmed exact first and second moments and variance for (a,N,p)=(2,1,1/2),(3,2,2/3),(4,2,1/3); at (2,1,1/2) mean7/12 variance1/72.

## originality

PASS

Strongest relevant published earlier SCOPE theorem studies *unconditional top-concept* Bernoulli stability and proves an almost-sure Gaussian crossover with the same leading threshold. In this critical window the event that no attribute is common to all a rows has probability tending to 1, so the earlier theorem implies the *qualitative* conditional Gaussian limit via conditioning on empty top intent. Thus neither Gaussian location nor limit shape alone is original. The reviewed claim additionally proves exact conditioned first/second moments for prescribed (A,B), all finite parameters, and an explicit uniform O(log a/√a) L1 approximation not implied by the prior qualitative theorem; these are the surviving original statements.

## value

PASS

Stability is a central formal-concept robustness invariant. Exact conditional second moments quantify fluctuations for an explicitly prescribed concept, and a uniform nonasymptotic Gaussian error bound addresses a different sampling scheme than top-concept unconditional stability. The quantitative estimate and finite law are potentially reusable even though a qualitative limit follows from the prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
