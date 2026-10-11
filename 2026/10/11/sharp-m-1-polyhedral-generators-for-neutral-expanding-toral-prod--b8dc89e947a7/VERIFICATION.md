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
# Verification of the minimal generating alphabet

The proof requires no program, numerical table, or finite enumeration. Each step is independently checkable for a symbolic positive integer parameter \(m\ge2\).

1. The intervals \([0,\theta/m)\), \([\theta/m,1/m)\), and \([j/m,(j+1)/m)\) for \(1\le j<m\) form a disjoint cover of the second coordinate for each \(\theta\), with half-open boundary convention.
2. Under \(T_m\), merging the first two labels reads \(d_n=\lfloor m(m^ny\bmod1)\rfloor\); the convergent digit series reconstructs \(y\) exactly on canonical representatives.
3. For every \(y\) in the standard common full-measure set uniformly distributed under multiplication by \(m\), the \(a\)-frequency is precisely the interval length \(\theta/m\), for every \(\theta\) simultaneously. The same common full-measure set handles an uncountable collection of thresholds by rational squeeze.
4. Haar entropy is \(\log m\), since multiplying by \(m\) is uniform Bernoulli in its base digits and the neutral coordinate has zero entropy. For a finite \(m\)-letter process, each block entropy is at most \(n\log m\); if the stationary entropy rate equals \(\log m\), subadditivity forces equality at every block size. Hence its process must be i.i.d. uniform and ergodic, contrary to the invariant neutral coordinate if the name map were generating.

These exact arguments establish the upper and lower bounds for all \(m\ge2\). No claim is made about partitions required to be Markov or independent, pointwise generation on all exceptional orbits, higher-dimensional neutral factors, or arbitrary non-diagonal matrices. Literature incompleteness is the remaining novelty risk; independent audit was not performed.
