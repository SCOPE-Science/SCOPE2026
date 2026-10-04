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

The proof was checked in the exact Bernoulli state space. For \(P_{t+1}=(tP_t+S_t/m)/(t+1)\) with \(S_t\mid P_t\sim\operatorname{Binomial}(m,P_t)\), direct conditional expectation gives the martingale identity and direct conditional second-moment calculation gives
\[
\mathbb E[P_{t+1}(1-P_{t+1})\mid P_t]
=P_t(1-P_t)\left(1-\frac{1}{m(t+1)^2}\right).
\]
Iterating this identity yields the finite product exactly. Euler's sine product supplies the infinite-round limit. The Taylor expansion of \(\sin x/x\) supplies the large-\(m\) correction.

`verify.py` independently propagates the exact rational distribution of accumulated success counts for several small values of \(m\) and \(t\). It checks the unconditional mean and variance formula, a conditional variance formula after fixing the first-round count, and numerical agreement between long finite products and the Euler sine product. It also checks the strict \(\pi^2/6\) inequality on a representative range of batch sizes.

The computation is finite and is used only as a cross-check of identities proved symbolically above. It does not certify any claim for unequal batches, sparse random comparison graphs, more than two items, or log-odds risk near the boundary.
