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

For a compact interval [0,K], the required multiplicities lie at indices at most floor(K a_N)+r=o(sqrt(N)), so DeSalvo–Menz gives joint total-variation transfer, with c=pi/sqrt(6). In the geometric model the zero probabilities are 1-exp(-cj/sqrt(N)). Writing epsilon=a_N/sqrt(N) gives a_N epsilon^r=1, and Taylor expansion uniformly on this window gives the stated Riemann-sum intensity. For a fixed tuple of distinct starts, a connected cluster of t overlapping windows has at least r+t-1 distinct absent sizes and O(a_N) placements, hence contributes O(epsilon^(t-1)); different clusters are independent. Removing nearby tuples from the independent product of intensity sums costs O(1/a_N). Mixed factorial moments therefore give independent Poisson interval counts; first moments give tightness on compacts, and the diffuse intensity gives vague convergence and count convergence on [0,x]. At x=0 the count is zero. The k-th start tail is exactly the event of at most k-1 starts through floor(x a_N); overlapping starts are counted as stipulated. The source's finite coefficient/enumeration tests were inspected as bounded corroboration, not rerun or used as a limit proof.

## originality

PASS

The supported contribution is the fixed-r point-process limit and its successive-start laws relative to the inspected predecessors. There is a distinct, mathematically equivalent Resultary record carrying a later publication date, which is disclosed, not treated as a different theorem or evidence of reverse priority. No inspected source established the same limiting law before the frozen result. This is not a priority certification.

## value

PASS

The statistic is the established chain mex and its canonically ordered successors. Its intensity, scaling exponent and fixed-rank laws characterize a natural emergence process and require controlling overlapping runs, rather than replacing r in a one-gap limit. The result is useful as a distributional description; it does not by itself give an asymptotic of the summed mex or any unbounded moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
