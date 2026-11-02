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

# Mathematical and computational verification

The analytic argument verifies the exact domain \(m,n\ge3\), \(\gcd(m,n)=1\), \(a,b>0\), and independent coordinate controls. The crucial steps are the root-of-unity chord identity, the coprime congruence that forces both frequency sums to equal their cycle lengths, the unique-pair and at-most-double spectral collision conclusion, and the two-row PBH determinant equivalence to simultaneous modular divisibility. The proof is not based on sampled spectra.

The included `check_directed_tori.py` is a standalone Python 3 test requiring `mpmath` and executes with `python check_directed_tori.py` from the directory holding the file. The test was executed in its delivered form before acceptance and returned:

```
PASS 4248701 deterministic checks across 89 resonant parameter samples and all coprime pairs through 25
```

The tests include a complete integer check of the chord-direction modular implication for coprime orders from three through twenty-five, direct Fourier eigenvalue collision enumeration for 89 parameter settings, and all cyclic two-site displacements on those examples. The comparison tolerance is \(10^{-65}\) at 82-digit precision. The checks do not exhaust infinitely many lengths or positive real rate ratios. The finite script uses the analytic formulas and is an independent consistency calculation, not a formal proof certificate.

Scientific limitations and the unresolved accessible-literature overlap risk are documented in the result and review. Self-review was completed; no independent audit was performed.
