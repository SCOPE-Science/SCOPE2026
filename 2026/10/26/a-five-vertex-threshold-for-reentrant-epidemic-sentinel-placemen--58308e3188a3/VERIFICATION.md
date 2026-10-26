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
# Verification instructions

Run \(\texttt{python verify.py}\) using Python 3 from the folder containing the embedded files. Compare the resulting JSON (whitespace-insensitively) with \(\texttt{certificate.json}\). No third-party packages or network are required.

The verifier checks four five-vertex polynomial gaps and six four-vertex polynomial gaps by exact integer coefficient arithmetic. It independently computes infection reachability over all \(16\) edge configurations and all five possible sources for each of \(p=1/5\), \(p=1/2\), and \(p=4/5\), yielding \(240\) weighted source-and-edge configurations and \(1{,}200\) monitor contributions. The result matches exact closed-form distances and verifies that sites \(2\), \(1\), \(2\) are the unique optimizers at those respective probabilities.

The universal impossibility for at most four vertices follows from a sign-change analysis of the six symbolic pairwise gap factors in RESULT.md, not from these finite checks. The extension to all larger paths follows by a fixed finite strict-margin perturbation argument and is likewise not a finite experiment. Independent scientific audit has not been performed.
