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

Run `python verify_johnson_online.py johnson_adaptive_trees.json` from the directory containing both artifacts. The standard-library checker independently enumerates every \(k\)-subset, reconstructs open-neighborhood answers, and verifies all \(15+31=46\) internal query nodes and all \(16+32=48\) leaf-center witnesses in the depth-four and depth-five certificates. It separately computes the exact adaptive dimensions of those instances using memoized exhaustive query splitting.

It also enumerates the full query traces on the distance-one common-neighbor family in six parameter cases and checks exact recursive depths for \(20\) interior-rank parameter pairs up to \(n=13\). The reproduced stdout is `verification_output.txt`. These tests are finite: the all-order bound is independently justified by the structural trace lemma in `RESULT.md`, and lower bounds outside the certificate instances use exact induced embeddings.

The certificates are ordinary finite witness data, not independently validated or formally certified. Historical originality is not established by finite replay.
