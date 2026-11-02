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

# Verification of the exact theorem

Run `python3 verify.py` using Python 3 and only the standard library. It constructs two different coefficient-ring structures of the same cardinality, checks normalized projective-point reductions and their \(q^2\)-fold branching, and explicitly matches all vectors by valuation, compatible projective ancestor and unit-scalar fiber. Every pair of vectors is tested for preservation of its wedge-zero relation in these finite cases:

- \((q,\ell)=(2,1)\): \(16\) full-matrix graph vertices, \(88\) ordered commuting pairs.
- \((q,\ell)=(2,2)\): \(256\) graph vertices, \(6400\) ordered commuting pairs; direct exhaustive multiplication independently checks all \(65,536\) ordered matrix pairs over \(\mathbb Z/4\mathbb Z\).
- \((q,\ell)=(2,3)\): \(4096\) vertices, \(434176\) ordered commuting pairs.
- \((q,\ell)=(3,2)\): \(6561\) vertices, \(741393\) ordered commuting pairs.

The enumerated centralizer-size spectra and ordered-pair sums agree exactly with the theorem for each case, and direct multiplication spot checks identify the same commutation condition as the wedge-zero test. The script prints `VERIFY_OK` only after all assertions pass. It does not enumerate every finite chain ring or constitute a proof in arbitrarily large length; those quantifiers are discharged by the general projective-reduction argument.
