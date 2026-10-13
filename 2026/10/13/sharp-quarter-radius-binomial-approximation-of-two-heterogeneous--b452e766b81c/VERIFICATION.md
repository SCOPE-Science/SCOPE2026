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

# Reproduction and verification

Run `python3 verify.py` using only Python's standard library. The expected and observed output is:

```
VERIFY_OK low_rational=655 high_square_rational=174 extremal_tests=3250
```

The script checks the identity \(d_{\mathrm{TV}}(P,\operatorname{Bin}(1,p+q-pq))=pq\) on 655 rational pairs satisfying \(pq\le1/4\). It checks \(d_{\mathrm{TV}}(P,\operatorname{Bin}(2,\sqrt{pq}))=(\sqrt p-\sqrt q)^2\) on 174 square-rational pairs with \(pq\ge1/4\); the square-rational representation makes all arithmetic exact. It also checks all 3,250 indicated exact-rational combinations of 50 positive trial counts and 65 approximating probabilities against the extremal input law, together with the analytic maximal-singleton inequality for each tested trial count.

The universal theorem does not follow from the verifier's finite samples. Its infinite-step proof is elementary: exact mass matching for the upper bound; the constraints \(pq\ge1/4\), \(p\le1\) for its sharp constant and uniqueness; and the binomial point-mass inequality \(mr(1-r)^{m-1}\le(1-1/m)^{m-1}\le1/2\) for all integers \(m\ge2\) for the lower bound. No computer algebra, random numerical tolerance, or external downloaded data is required.

The manuscript does not determine the best approximation at each input pair and does not prove a multi-summand analogue. The bibliographic originality assessment retains explicit uncertainty about older inaccessible literature. Independent validation or audit has not been performed.
