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

Run `python3 verifier.py` with Python 3 (standard library only) in the directory containing that file. Its exact output is captured in `verification_output.txt`.

The executable independently constructs all graph vertices, shortest-path distances and scale-one/scale-two flag complexes for \(3\le m\le6\) and \(2\le\ell\le5\), computes all binary boundary ranks, and checks that the reduced Betti groups match the theorem in each of the \(32\) tested scale/parameter combinations. For each length-three case it checks the full suspension face-set identity and the diameter-three terminal contractibility; for each longer case it independently checks every proposed elementary collapse pair, down to the original graph. Oriented one-chain identities check that endpoint reversal flips each interior cycle, while suspension reverses that sign a second time. The general proof does not depend on this finite sampling.

These tests do not establish originality or represent independent audit. The integral homology-module assertions follow from the explicitly written generators, integral boundary equations and exact symmetry actions, not from mod-two matrix ranks. Every parameter statement beyond the bounded verifier range is supported by the symbolic proof in `RESULT.md`.
