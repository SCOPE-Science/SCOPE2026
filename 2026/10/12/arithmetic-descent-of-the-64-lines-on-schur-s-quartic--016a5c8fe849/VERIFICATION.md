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

# Reproducibility

Run `python verify_schur_arithmetic.py` with Python 3.10+ and SymPy 1.12+, or first install `requirements.txt`. The program performs exact symbolic algebra in characteristic zero, never floating-point sampling. It regenerates the 64 published line equations, verifies 64 distinct normalized Plücker vectors, checks that their spanning-point parametrizations vanish identically on the quartic, constructs the three Galois permutations on the set of lines, and checks fixed-point totals \(8,8,40\). It recovers the five field counts \((6,2,2,34,20)\) and the orbit profile \((6,19,5)\) of sizes \(1,2,4\), respectively. It also exhaustively enumerates all subsets of the six rational lines and computes the sharp skew size four.

The actual successful run returned:

`VERIFY_OK lines=64 fields=Q:6,Qi:2,Qsqrt3:2,Qsqrtminus3:34,K:20 Galois_orbits=1^6,2^19,4^5 real=8 rational=6 maximal_rational_skew=4`

These checks establish exact arithmetic consequences *conditional on* the published complete classification of all 64 lines; they do not independently rederive its exhaustiveness or establish the absence of all unindexed earlier literary overlap. The cited 2019 paper supplies the exhaustive classification. No independent audit is claimed.
