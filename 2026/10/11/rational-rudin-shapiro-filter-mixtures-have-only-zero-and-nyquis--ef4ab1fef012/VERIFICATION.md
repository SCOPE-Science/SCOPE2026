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

The certificate below is a finite computational corroboration only. The unrestricted proof is in `RESULT.md`.

Run `python3 verify.py` with Python 3 and the standard library. The checker generates the two classical Rudin–Shapiro coefficient arrays for \(1\le m\le12\). It tests every nonzero integer mixing pair \((a,b)\in\{-3,-2,-1,0,1,2,3\}^2\), evaluating the two endpoint modes exactly and reducing every mixed symbol modulo each \(\Phi_{2^r}(z)=z^{2^{r-1}}+1\) for \(2\le r\le m\). It separately builds 24 full cyclic convolution matrices for \(1\le m\le4\) and checks exact ranks by rational Gaussian elimination.

Observed output when the packaged checker was run:

`VERIFY_OK levels=12 rational_pairs=576 primitive_cyclotomic_checks=3168 exact_circulant_ranks=24 real_extension_counterexample=proved_symbolically`

There is no exhaustive verification over all rational pairs or all depths, nor does the checker establish independent scientific validation. The real irrational counterexample is proved algebraically in `RESULT.md` rather than by an approximate floating-point root test.
