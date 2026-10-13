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

The proof is self-contained in `RESULT.md`. Run `python3 checker.py` using Python 3.8 or later, with no additional dependencies. The checker enumerates precisely all \(2^{15}=32768\) labeled simple graphs on six vertices and independently establishes the required upper bound on triangles as a function of edge count. It evaluates the three polynomial positivity certificates with exact rational Bernstein coefficients on the full closed parameter intervals \([1/6,1/5]\), \([1/5,1/4]\), and \([1/4,1/3]\). On successful completion the script prints `EXACT_CHECK_OK`.

The analytical proof—not finite sampling—establishes the inequality for every real normalized weight vector and every real \(p\in(0,1/3]\). The only computationally finite assertion is the graph lemma, whose complete space is enumerated. Verification does not cover different Bernoulli parameters, seven or more nonzero weights, or the strictly greater-than-mean event. Independent scientific audit is not performed.
