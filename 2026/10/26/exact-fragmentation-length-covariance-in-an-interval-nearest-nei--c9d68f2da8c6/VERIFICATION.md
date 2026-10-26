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

## Reproducible computations

Run `python3 verify_nearest_neighbor.py` with Python 3. No additional packages or nonlocal datasets are required. The output written during verification is `verification_output.txt`.

The program exhaustively checks rank permutations of the internal gap lengths for sample sizes from 2 through 9, computing the expected exponential order statistic for each gap rank with exact `Fraction` arithmetic. It separately checks the weighted joint event of two local maxima a distance of two indices apart by enumerating all 120 relative rank patterns of five exponential variables. It directly constructs the undirected nearest-neighbor graph on sorted points for all permutations of distinct integer gaps of lengths 2 through 6, confirming the local-maximum deletion characterization.

The finite computations do not establish the theorem for untested values of \(n\); the infinite-family proof rests on the independence of normalized exponential spacings and their sum, a five-variable exact rank count, and the finite-range local covariance expansion.
