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

The operator is defined in `RESULT.md`. The proof is analytical and applies to every real or complex Hilbert space of dimension at least two. Its essential steps are the rank-two reducing-subspace identity, exact two-dimensional trace and determinant, and the sharp Kantorovich bound with endpoint spectral-projection approximants. This record is not an independent audit.

## Executed supplementary checks

Run `python verify.py` using Python 3 and NumPy. The supplied deterministic checker constructs positive diagonal matrices in dimensions two through eight, uses randomized normalized complex spike directions, evaluates the endpoint by matrix multiplication, and compares its complete eigenvalue multiset with the analytic two-root formula. It also checks the outlier product, the rank-two support and the sharp scalar inequalities, and includes exact-endpoint witness configurations. The executed run returned:

`PASS: 8076 deterministic finite assertions, maximum absolute residual 4e-13`

Numerical ranks were evaluated with a specified floating-point threshold. Such finite checks are supplemental, do not certify equality for arbitrary matrices or infinite-dimensional operators, and are not used to justify originality or mathematical value.

## Proof boundaries and access limits

The infinite-dimensional sharpness assertion uses spectral projections near the spectral endpoints, including cases where no eigenvector realizes an extremum. The conclusion is restricted to rank-one spiked positive inputs. A related 2025 primary article could not be inspected in full; no comparison with its unseen results is asserted. A separate independent audit has not been conducted.
