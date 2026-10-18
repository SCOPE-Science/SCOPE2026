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
# Verification record

The independently implemented `verify_rank_one.py` program creates all rank-one square-zero matrices by outer products over finite fields (including \(\mathbb F_4\)), directly multiplies every pair, checks the equivalence between commuting and pairwise annihilation, then counts ordered tuples using exact bitset recursion. It independently evaluates the closed Gaussian-binomial formula using integer arithmetic.

The checks completed for thirteen \((n,r,q)\) configurations, including \((4,2,2)\) with count \(2836\), \((4,3,2)\) with count \(38536\), and \((3,2,4)\) with count \(9136\). The script also tested the component-index and dimension formulas on the parameter grid \(2\le n\le15\) and \(1\le r\le15\).

Reproduce by running `python3 verify_rank_one.py` in the directory containing the file. Success prints `VERIFY_OK_MINIMAL_NILPOTENT_TUPLES`. The output is only corroboration in finite cases: the general irreducibility and exact count rest on the accompanying proof, and the scheme structure remains unverified.
