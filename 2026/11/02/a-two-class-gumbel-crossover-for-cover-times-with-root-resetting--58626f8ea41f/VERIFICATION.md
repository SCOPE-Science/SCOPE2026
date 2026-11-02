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

# Verification and reproducibility

The proof in `RESULT.md` is analytic. Its key steps are (1) separate genuine uniform moves from root resets; (2) prove conditional independence of the two coupon streams; (3) show the two move-count processes have linear means and variance \(O(t)\); (4) apply the coupon-collector missing-count factorial-moment limit after normalization; and (5) use joint convergence to evaluate the last-covered-side event. The valid range is all fixed \(0<r<1\) and fixed real \(\lambda\), with the bipartite part sizes specified there.

The self-contained Python script `check_reset_biclique.py` compares an exact labelled-walk Markov-chain recursion with a structurally different exact part-chain/coupon-stream recursion. It runs for three rational reset probabilities, 16 pairs of small part sizes, and all nine horizons from 0 through 8. The test compares three completed-coverage probabilities per case, giving 1296 exact Fraction assertions; it also performs 12 rational stationary-rate checks and six floating-point normalization checks, totalling 1314 asserted comparisons. Run `python3 check_reset_biclique.py`; the expected final line is `PASS 1314 exact/evaluated assertions; finite-state checks rational-exact`.

Limitations: the script does not check arbitrary graph sizes, infinite asymptotics, optimality, or historical novelty. Those depend on the written mathematical arguments and independent literature review. Independent mathematical audit has not been performed.
