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

The checker reconstructs the nine-point poset from the cover relations stated in `RESULT.md`. It computes transitive closure and first verifies that no point is a beat point.

It enumerates every order-preserving self-map by assigning source points in lower-to-upper order. At each assignment, a target value is admitted exactly when it lies above the images of every already assigned lower cover. Because preservation of all covers is equivalent to preservation of the finite transitive order, this backtracking is exhaustive. Every completed map is then independently rechecked against all ordered pairs of the transitive closure.

For the resulting \(12{,}575\) maps, the checker constructs exact bit sets for the pointwise relation \(f\leq g\) and unions every comparable pair. It verifies component sizes \(12{,}573\), \(1\), and \(1\), checks that all nine constant maps are in the large component, and confirms that the two singleton maps are exactly the only two bijective isotone maps: the identity and the stated involution.

The final output is:

`VERIFY_OK maps=12575 components=12573,1,1 automorphisms=2 comparable_pairs=1235007 constants_large=9`

The computation proves only the exact finite census for this nine-point poset. The passage from components to homotopy classes uses the finite-space fence criterion in Barmak, Corollary 1.2.6, based on Stong's theory. No independent audit has been performed.
