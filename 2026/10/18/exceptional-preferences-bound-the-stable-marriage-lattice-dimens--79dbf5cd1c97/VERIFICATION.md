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
# Reproduction and limits

The source file `verify.py` requires Python 3 standard library only. Execute `python3 verify.py` from the directory containing the embedded files; its standard output is exact JSON that must byte-match `certificate.json`. It computes all stable matchings by brute-force permutation enumeration independently of the projection/greedy completion method. For \(n=2,3\) with one exceptional woman, it checks every exceptional preference permutation and every set of men's preference permutations with fixed common master order. It also checks the sharp one-exception family for \(n=1,\ldots,6\), the Boolean family for \(k=1,2,3\), and all asserted exceptional-partner order embeddings within these finite tests.

The finite checks cannot establish the universally quantified statements; the written proof supplies those arguments. The certificate describes exact counts, not a probabilistic test and not an independent audit. No external theorem prover was used. Scientific assumptions and unverified extensions are documented in `RESULT.md`.
