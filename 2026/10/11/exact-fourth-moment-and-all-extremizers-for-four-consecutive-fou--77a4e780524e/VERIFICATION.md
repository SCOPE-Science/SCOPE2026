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

# Verification evidence

Running `python3 check.py` from the same directory outputs `VERIFY_OK`. The checker uses Python standard-library rational arithmetic to verify the derivative polynomial and isolate its unique positive critical root, tests the complete convolution/autocorrelation identity on 624 nonzero integer vectors, tests each nonnegative scalar comparison, and checks the cyclic fourth moment for five grid sizes by independent complex quadrature. The exact root of the cubic and analytic inequalities establish the unrestricted theorem; no finite test is presented as proof of the infinite parameter range. An independent audit has not been performed.
