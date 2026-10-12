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
# Reproducibility and limits

Run `python3 checker.py` with standard Python 3; compare the output with `checker_output.txt`. The checker evaluates the explicit polynomial and all partial derivatives at every vector of \(\{0,1\}^{2m+1}\) for \(m=3,4,5,6\), and \(\{-1,0,1\}^{2m+1}\) for \(m=3,4\). That is 32,750 exact test vectors. It verifies the predicted rank/component criterion at each vector and gives generic component-isolation witnesses and reduced-support degree/count checks for \(3\le m\le8\).

The proof of the result for arbitrary \(m\) is symbolic. In particular, enumeration at bounded integer points neither establishes global irreducibility nor exhausts the complex points. Irreducibility is proved via Gauss's lemma, singular decomposition via the adjugate criterion and rank elimination, and the two generic transverse local normal forms via explicit elimination and nondegenerate Hessians. The full Jacobian scheme and singularities where components intersect are not determined. The historical-priority comparison has residual access risk for the 1982 coordinate-plane determinantal-section literature. Independent mathematical audit is not performed.
