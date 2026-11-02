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

# Reproducibility

Run `python3 verify.py` from the directory containing `certificates.json`. The program requires only the Python standard library and checks finite constraints using exact rational arithmetic. The complete certificate consists of six codebooks, six rational received-word weight vectors, and six rational source-word slack vectors.

For each profile, the verifier enumerates all \(128\) length-seven binary words and all \(32\) length-five received words, checks two independently defined deletion-shadow procedures, checks all codebooks against the list-size condition, and proves each rational objective falls below the next integer. The observed output is attached as `check_output.txt`. No randomized tests, timeouts, numerical solver certificates, or unverified external processes are used for the reported proof.

The proof establishes only the claimed finite profile. It does not establish publication priority conclusively, nor does it replace an independent mathematical audit.
