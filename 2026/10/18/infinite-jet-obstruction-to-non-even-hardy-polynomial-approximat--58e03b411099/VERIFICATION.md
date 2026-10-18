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

# Verification notes
The proof is an exact analytic coefficient argument for arbitrary \(M\), \(a\), and non-even \(p\). The included standalone Python checker uses exact rational generalized-binomial coefficients and Taylor coefficient convolution; it checks \(72\) triples from \(p/2\in\{1/2,3/2,5/2,7/4\}\), \(a\in\{1/2,1/3\}\), and \(M=1,\ldots,9\). It confirms that the objective difference vanishes through order \(2M\) and that the order-\(2M+1\) coefficient equals \(-2(1-a^2)\beta_M\beta_{M+1}\).

**Run command:** `python verify_nonlocal.py` from the artifact directory. No third-party packages are required.

**Observed output:**
```
PASS: exact rational coefficient test for 72 parameter triples; each onset is order 2m+1
Example p=3, a=1/2, m=3: Taylor coefficient [lambda^7] difference = -9/4096
```

**Verification boundary:** The checker tests finitely many rational inputs, while the proof covers real \(p>0\) outside positive even integers, every integer \(M\ge1\), and real \(a\in(0,1)\). There is no independent mathematical audit or claim about optimizers.
