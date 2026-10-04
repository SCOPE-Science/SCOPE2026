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

The general theorem was checked by reconstructing the proof from the stated finite-poset definitions. The critical steps are:

1. For the image \(I=f(W)\), if every occupied target level contains at least two image points, distinct points in one target antichain cannot have preimages in different source levels. This forces a surjective order-preserving assignment from occupied target levels to source levels, hence all \(h\) levels are occupied and matched identically.
2. Every other image has an occupied singleton level (or is itself a singleton), making its order complex a cone. Thus the corresponding map is null-homotopic.
3. A level-preserving nonconstant self-map induces a tensor product of nonzero maps on the reduced degree-zero homology of the discrete levels, so its top rational homology action is nonzero.
4. Any pointwise-comparable map is homotopic and hence has the same nonzero top-homology action. The image lemma then forces both maps to be level-preserving, and comparability inside each antichain forces pointwise equality.
5. The number of nonconstant self-functions on a level of size \(r_i\) is \(r_i^{r_i}-r_i\); multiplying these independent choices gives the isolated-class count.

`verify.py` gives supplementary finite replay. It exhaustively enumerates all monotone self-maps for \((2,2,2)\) and \((2,2,3)\). For \((2,2,2)\), it constructs the pointwise-comparability graph of all \(446\) maps and finds exactly \(9\) components with sizes \(438,1,1,1,1,1,1,1,1\). For \((2,2,3)\), it enumerates \(2507\) monotone maps and finds exactly \(96\) level-preserving levelwise-nonconstant maps, as predicted. In both cases every remaining map has a contractible image of the type used in the proof. The replay terminates with `VERIFY_OK`.

These finite checks do not prove the unrestricted theorem; the symbolic argument above does.
