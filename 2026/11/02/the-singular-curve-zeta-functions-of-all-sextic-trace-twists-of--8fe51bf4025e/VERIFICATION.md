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

Run `python3 verify.py` in a directory containing that standalone script. Only the standard library is required. The attached `verify_output.txt` is the captured output from the exact execution; it is not a substitute for checking the proof.

The script constructs the fifteen two-subsets, fifteen perfect matchings, and forty-five incident flags of a six-element set. It exhausts all \(720\) permutations, verifies their precise cycle histograms against the eleven-case table, and independently counts fixed objects under powers \(1\) through \(12\). It also verifies the common splitting-field degree and performs separate direct-coordinate projective singularity enumerations for the split defining equation over \(\mathbb F_7\) and \(\mathbb F_{11}\), comparing the outcome with the union of the fifteen explicit lines. The observed totals are \(90\) and \(150\), respectively, and execution ends with `VERIFY_OK`.

The proof for every finite field and every permitted sextic étale algebra is not inferred from the two numerical point counts. It follows from the complete geometric singular-locus argument, finite exhaustive \(S_6\)-orbit enumeration, and the normalization point-count identity. No characteristic below seven and no ambient-threefold zeta function is verified or claimed.
