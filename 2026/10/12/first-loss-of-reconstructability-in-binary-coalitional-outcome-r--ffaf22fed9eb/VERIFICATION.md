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
# Reproduction and limitations

Place the standalone `verify.py` alongside the other files and execute `python3 verify.py`. This uses no third-party modules, databases or hidden files. It checks all \(4\), \(16\), and \(256\) binary truth tables for one, two, and three binary-action agents, generates the exact outcome-range family of every coalition, computes action-relabeling representatives, and asserts the signature census, ambiguous signature sizes, explicit witness, and Burnside orbit counts. The expected final output is `PASS: first nonfaithfulness at three players; witness and exact census verified`.

The witness's two tables and the two-agent case also have direct mathematical proofs in `RESULT.md`. The Burnside formula independently certifies the number of action-flip orbits. The 41/46 finite census is exhaustive because the complete universe has exactly 256 members, each visited once; no randomized sampling or timeout is involved. No claim about four agents, arbitrary action-set sizes, infinitely many agents, or global publication novelty is verified by this finite computation. An external independent audit has not been performed.
