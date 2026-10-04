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

The theorem was checked in four ways.

1. **Pigeonhole inequality.** If the witness tuple uses only \(u\le k\) distinct vertices and the model has more than \(k+2^k\) vertices, then the outside set has more than \(2^u\) vertices. Hence two outside vertices have the same adjacency vector to the witness set.
2. **Induced-subgraph preservation.** Restricting to the witness values and those two outside vertices preserves every atomic formula on retained vertices, so a universal quantifier-free matrix remains true.
3. **Clone-type preservation.** In the expansion, a diagonal clone pair has the same atomic type as \((b,b)\), a distinct clone pair has the same atomic type as \((b,c)\), and a clone paired with a witness has the same atomic type as \(b\) paired with that witness. This exhausts assignments to the two universal variables.
4. **Sharpness replay.** `verify.py` checks for \(0\le k\le12\) that choosing any number up to \(2^k\) of distinct binary witness-neighborhood profiles realizes every order through \(k+2^k\), and it checks the equality/adjacency type table used by the cloning argument.

The finite replay is corroborative only; it does not prove the theorem beyond the tested range. The symbolic proof is uniform in \(k\). The archived survey and the two-variable-universal paper were inspected for prior coverage. No independent audit has been performed.
