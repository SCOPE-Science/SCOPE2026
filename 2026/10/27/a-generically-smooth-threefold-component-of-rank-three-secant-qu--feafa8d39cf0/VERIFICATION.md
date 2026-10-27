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

# Verification

The supporting `verify.py` uses rational Gaussian elimination only; there are no external Python dependencies. Run `python3 verify.py` from a directory containing the extracted files. For each integer \(m\) from \(3\) through \(14\), it uses the squarefree polynomial \(P(t)=t^m+1\) over \(\mathbb Q\), constructs the two multiplier containment conditions, and computes the exact nullity of their linearization. Expected output: the tangent dimension equals \(6\) at \(m=3\), equals \(3\) for \(m=4,\ldots,14\), and ends with `VERIFY_OK`.

The computation is a finite check and does not prove the theorem for arbitrary degree or arbitrary smooth plane curve; those assertions follow from the polynomial-degree argument and the geometric Quot tangent-space calculation in `RESULT.md`. In particular the existence of the three-dimensional family, injectivity of its parameterization, regularity of the local rings, and relation to the Hilbert secant locus are mathematical arguments, not tested by the linear-algebra script. Independent audit has not been performed.
