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

# Reproducibility and proof checks

The attached `VERIFY.py` is a standalone Python 3 standard-library checker. Run `python3 VERIFY.py` from the extracted file directory. An actual replay of the packaged source reported:

`CHECK_OK 180380 exact integer/rational assertions for distances, cuts, equality cases, and embeddings, n<=13`

The checker reconstructs the entire crown graph and its shortest-path matrix in the domain \(3\le n\le12\). It enumerates every one of the \(2^{2n}\) cut vectors for each \(3\le n\le8\), evaluating the sharp inequality and exact equality criterion using integers. It enumerates every balanced subset for each \(3\le n\le13\) and compares every graph distance to the rational distance of the explicit cut embedding. These are complete checks within their *finite* indicated ranges only, not a brute-force proof of the infinite theorem.

For all larger integers, the proof uses the symbolic identity for arbitrary \(k,\ell,t\), its even/odd nonnegativity argument, and the exact binomial subset-separation probability. The old Matoušek paper presents a residual bibliographic comparison risk because only an abstract was accessible. The source evaluation and proof review were self-review; independent audit remains not performed.
