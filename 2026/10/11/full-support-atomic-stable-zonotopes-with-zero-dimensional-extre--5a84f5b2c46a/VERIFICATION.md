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

# Verification and proof obligations

The argument is self-contained and analytic. The following assertions have been checked symbolically from the stated definitions:

1. The marked Poisson mapping produces an intensity of \(\alpha r^{-1-\alpha}\mathrm{d}r\,\sigma(\mathrm{d}v)\), giving the exact positive-stable Laplace transform for the sums along any subset of atoms.
2. For \(0<q<\alpha\), the fractional moment is finite and scales with the directional mass tail to power \(q/\alpha\); the geometric-tail assumption and Markov's inequality give summable probabilities, so Borel–Cantelli applies.
3. Support-maximizing signs produce at most \(2\sum_{i=0}^{d-1}\binom{n-1}{i}\) truncated vertices; the Euclidean distance to a corresponding exposed point is at most the sum of the omitted segment lengths.
4. The finite union of closed covering balls contains **the closure of the exposed set** and therefore every extreme point; the usual false shortcut from a Hausdorff cover of a dense subset is not used.
5. An explicit dense-direction sign separation gives an injective exposed-point map on the complement of countably many great subspheres, while positive segments in \(d\) independent directions give interior.

No numerical experiments, floating-point output, or external computed certificates are needed for the theorem. Independent audit has not been performed. The literature check does not prove global novelty and cannot rule out unindexed equivalent constructions.
