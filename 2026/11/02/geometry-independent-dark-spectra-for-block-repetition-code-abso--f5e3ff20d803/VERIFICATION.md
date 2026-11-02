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

The reproducible checker is `verify.py`, requiring Python 3.8 or newer and no third-party packages. Run `python3 verify.py`. Successful replay prints `VERIFY_OK spectral_partitions=134 krylov_partitions=30`. The computation uses exact finite-field elimination on Walsh restrictions and independently on Krylov spans for small graphs. It is a finite consistency check, not an exhaustive proof for all dimensions. The analytic proof in `RESULT.md` handles all allowed integers and all strictly positive absorber rates. No independent audit has been performed.
