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
`artifacts/verify.py` reconstructs finite instances from `artifacts/certificate.json` using only the Python standard library.

For the exact Proposition 5.5 source function over \(\mathbb F_{11}\),
\[
h(x)=\frac{x^3-3x+1}{x(x-1)},
\]
the verifier recovers the four full three-point fibers on \(\mathbb P^1(\mathbb F_{11})\), uses \(b=0\), and constructs the Theorem 3.2 generator with \(r=2\) and \(t=2\). It tests every one-, two-, and three-column subset. All one- and two-column sets are independent, and exactly the four source fibers are dependent triples. Thus the checked instance has dual minimum distance \(3\), four minimum supports, and \(40\) nonzero minimum dual words.

A second fiber-Vandermonde model over \(\mathbb F_{13}\) checks \(r=3\), \(t=2\), three four-point fibers, and the projective infinity column. Every subset of at most three columns is independent, and exactly the three designated fibers are dependent four-subsets, giving \(36\) nonzero minimum dual words.

The verifier then sets \(t=1\) in that second model and confirms that additional dependent four-subsets appear. This is a direct finite check that the theorem's \(t\ge2\) hypothesis is not cosmetic.

The finite cases validate the generator interpretation and implementation but do not establish the all-prime-power theorem. The infinite statement is proved symbolically in `RESULT.md` by extended Vandermonde independence, one-dimensional nullspaces, and comparison of the \(j=0\) and \(j=1\) blocks.

Successful replay prints `VERIFY_OK`.
