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
The proof is symbolic for all \(n\ge4\) and all algebraically closed fields. Known binomial-edge radicality and prime decomposition are cited explicitly; their proof is not reproduced. The tangent-rank argument separates internal nonzero-run edges from the isolated-zero blocks, giving an exact rank equality rather than finite inference. For the generic adjacent-zero stratum the chart \(p_{35}\ne0\) eliminates every equation except \(st=0\).

Run `python3 verify_cycle.py` in the directory containing this file to perform independent finite-field corroboration. The code enumerates every rank-two row-space representative over \(\mathbb F_2\) for \(n=4,5,6,7\), and \(\mathbb F_3\) for \(n=4,5,6\), then compares exact ranks of the cyclic-minor Jacobian with the geometric pointwise criterion and confirms support on indexed components. The extracted file returned `VERIFY_OK` with counts written in the result. Finite fields and bounded sizes are not an exhaustive proof of the stated infinite-family theorem. The reviewer has not performed independent validation.
