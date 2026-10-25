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

# Verification details

The finite checker is `verify.py`. Run `python3 verify.py` using Python 3 with no third-party dependencies. It builds every \(W=(01)^a0(01)^b0(01)^c\) for \(1\le a,b,c\le9\) and compares distinct actual length-\(\ell\) substring sets against the diagonal-rectangle formula for every valid \(\ell\). It also checks the total number of distinct factors from a separate all-length set. Expected output: `VERIFY_OK 729 triples`.

**Limits:** These tests establish the enumerated finite cases, not an infinite theorem; the unrestricted formula follows from the explicit zero/one/two-defect partition and bijections in `RESULT.md`. No external or independent audit has been carried out.
