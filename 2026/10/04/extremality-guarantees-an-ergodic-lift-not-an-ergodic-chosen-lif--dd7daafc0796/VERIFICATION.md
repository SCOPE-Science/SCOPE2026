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
The proof has two independent parts.

For the positive statement, write \(P(\nu)=\pi_*\nu\). If \(\mu\) is extreme in the affine image and \(P^{-1}(\mu)\) contains a nontrivial convex combination, pushing that combination forward forces both endpoint measures back into the same fibre. Hence the fibre is a face. Compactness gives an extreme point of the fibre; the face property makes that measure extreme in the full invariant-measure simplex, which is equivalent to ergodicity of the shift flow. This argument requires no injectivity of \(P\).

For the time-average consequence, Birkhoff is applied on trajectory space to \(f\circ\pi\). Because \(\pi(\sigma_t\phi)=\phi(t)\), its ergodic average is exactly the trajectory average. Disintegration of the full-measure Birkhoff set over \(\pi\) yields at least one such trajectory for \(\mu\)-almost every initial state.

For the counterexample, \(S_+\) and \(S_-\) are disjoint periodic shift orbits. Their unique invariant probabilities \(\nu_+\) and \(\nu_-\) both have one-time marginal equal to Haar measure \(m\). Any invariant probability on the disjoint union is \(\lambda\nu_++(1-\lambda)\nu_-\), so the base invariant-measure set is the singleton \(\{m\}\). The half-half mixture gives mass \(1/2\) to the invariant component \(S_+\), so it is not ergodic.

Limits: the argument does not establish extremality of every invariant measure that is ergodic in the strong-backward-invariance sense, and it does not characterize other possible trajectory averages. No computational experiment is used.
