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

The verification separates the source-backed structural step from the finite combinatorics.

1. **Metric hierarchy.** For an injective tuple with all distances at least \(2^{-h}\), agreement through the first \(j\) Baire coordinates gives a refinement chain of partitions from one block to singletons. Conversely such a chain determines the first-separation level of every pair and hence a dyadic ultrametric using exactly the visible scales.

2. **Orbit identification.** The principal source proves strict metric homogeneity. Its graph example starts from the class of all finite looped graphs, so arbitrary off-diagonal edge choices are compatible with each finite metric hierarchy. Hence labeled finite metric graphs are exactly ordered-tuple orbits and contribute the factor \(2^{\binom n2}\).

3. **Resolution recurrence.** If \(H_h(n)\) counts the partition chains, conditioning on the first exposed partition gives
   \[
   H_{h+1}(n)=\sum_{\pi\in\Pi_n}\prod_{B\in\pi}H_h(|B|).
   \]
   This matches the standard higher-order Bell iteration.

4. **Polynomial structure.** Compress a weak refinement chain to a strict chain with \(k\) transitions. Its transition positions can be chosen in \(\binom{h+1}{k}\) ways, so
   \[
   H_h(n)=\sum_{k=0}^{n-1}c_{n,k}\binom{h+1}{k}.
   \]
   The maximal-chain coefficient is
   \[
   c_{n,n-1}=\prod_{k=2}^n\binom k2=\frac{n!(n-1)!}{2^{n-1}},
   \]
   yielding leading coefficient \(n!/2^{n-1}\).

5. **Computational replay.** The bundled script independently generates set partitions, directly enumerates refinement multichains for \(n\le5\) and \(h\le3\), checks the recurrence, verifies the strict-chain binomial expansion and maximal-chain coefficient, interpolates leading coefficients, and checks the graph factor and binary special case. It reports:

`VERIFY_OK 180 exact assertions`

It reproduces the first four hierarchy rows

`h=0: [1, 1, 1, 1, 1, 1, 1]`

`h=1: [1, 2, 5, 15, 52, 203, 877]`

`h=2: [1, 3, 12, 60, 358, 2471, 19302]`

`h=3: [1, 4, 22, 154, 1304, 12915, 146115]`

for \(n=1,\ldots,7\).

No independent audit has been performed.
