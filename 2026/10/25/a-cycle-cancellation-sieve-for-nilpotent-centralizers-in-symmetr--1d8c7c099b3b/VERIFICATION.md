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

The two included programs use Python's standard library and require no data files. Run `python3 general_verify.py` and `python3 verify.py` in a directory containing those scripts.

`general_verify.py` creates actual partial injective maps and compares all rank coefficients for all nilpotent chain types of total vertex-count at most six. It also compares an independently enumerated decorated-chain matching count with the signed cycle sieve for chain types of total vertex-count seven through eleven with at most five chains. Its expected success message is `VERIFY_OK_NILPOTENT_CENTRALIZER_SIEVE`.

`verify.py` checks the equal-length exponential generating function using exact rational polynomial arithmetic, compares it with independent decorated-matching enumeration, and exhaustively enumerates actual partial bijections in eight small cases. Its expected success message is `VERIFY_OK_UNIFORM_CHAIN_CENTRALIZER_RANK_PROFILES`.

These checks establish exact agreement in their stated finite ranges only. The general proof is the chain-prefix/terminal-suffix bijection followed by signed cycle cancellation; no independent mathematical audit has been performed.
