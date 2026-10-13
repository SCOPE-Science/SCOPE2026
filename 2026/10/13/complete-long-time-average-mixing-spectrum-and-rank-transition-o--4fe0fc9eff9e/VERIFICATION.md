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

The proof uses exact graph identities and a Laurent constant-term calculation. The accompanying `verify_hamming.py` is executable after installing NumPy and invokes no network resources. Run `python verify_hamming.py` in the same directory.

The exact branch enumerates ordered pairs of characters of matching Hamming weight for \(45\) triples with \(2\le q\le6\), \(1\le d\le3\), and \(0\le j\le d\). It checks equality to the rational closed formula and verifies the binary/nonbinary rank result in each tested dimension. The independent matrix branch builds spectral projectors from additive characters, checks the graph adjacency decomposition and stochasticity, then compares the full eigenvalues for ten specified parameter pairs, with numerical error below \(8\times10^{-16}\).

Expected program output:

`VERIFY_OK exact_pair_count_cases=45 matrix_projector_cases=10 max_eigen_error=7.772e-16`

Finite examples do not establish an unrestricted result. The infinite claim is proven by the tensor-factorization and constant-term arguments in `RESULT.md`. No external/independent audit was performed.
