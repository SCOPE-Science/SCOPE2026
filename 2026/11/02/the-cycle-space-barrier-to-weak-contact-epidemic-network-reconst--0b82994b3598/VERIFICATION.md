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

The exact proof uses the reversible, independent Bernoulli stationary law at zero contact intensity, a centered-product eigenbasis of the uncoupled finite generator, the differentiated stationarity equations, and signed graph incidence rank. These steps establish an all-finite-graph theorem without extrapolation from a finite search.

The accompanying `verify.py` is a standalone Python 3 standard-library checker. From the same directory run:

```text
python verify.py
```

Observed result from the supplied program: `EXACT_CHECKS_OK 2505`. The script checks the exact rational residual of the full first-order stationary generator equation, the one-site and pairwise moment identities, contact-support signs, incidence-rank/nullity identities, explicit leaf-peeling reconstruction of positive directional rates on forests, and distinct-rate triangle aliases.

The finite checks verify implementations and illustrative instances. They do not establish all-graph correctness by enumeration. The proof does not address higher-order response identifiability, statistical estimation of derivatives, or imperfectly known local baseline rates. Independent examination has not been performed.
