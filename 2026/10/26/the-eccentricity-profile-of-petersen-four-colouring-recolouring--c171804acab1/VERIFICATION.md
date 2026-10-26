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

The attached `verify_kneser.py` and `verify_petersen.py` require only Python's standard library. Run them without arguments from the directory containing both scripts. Save stdout and compare it byte-for-byte to `verify_kneser.out` and `verify_petersen.out` respectively. Both source programs are complete standalone certificates and include assertions on their output counts.

The first uses the disjointness model of the Petersen graph on the ten two-element subsets of a five-element ground set. It recursively generates all proper colourings, constructs every one-coordinate recolouring edge and reduces the distance calculation to eleven symmetry orbits under the 120 permutations of the ground set and the 24 palette namings per normalized colour partition. It performs complete breadth-first search from a representative of every orbit and prints each complete distance histogram.

The second directly enumerates all \(4^{10}=1{,}048{,}576\) labelled vertex colourings of the standard outer-pentagon/inner-pentagram representation, filters every edge inequality, forms all recolouring edges, and independently computes the eleven symmetry-orbit representative distances. It asserts the explicit graph isomorphism used for orbit reduction.

Both programs return \(12{,}960\) legal colourings, \(53{,}280\) exchange edges, one connected component, eccentricities \(13\) (\(3{,}360\) states) and \(14\) (\(9{,}600\) states), eleven orbit classes, and the same full degree-count vector. Every claimed state is enumerated; no inaccessible third-party tables, randomness, or external checks are dependencies. The exact scripts embedded here were replayed after extraction from the proposed package, and their byte outputs matched the included records.

Independent external scientific auditing is not performed. No claims are made for other graphs, palette sizes or update moves. Literature novelty remains a best-knowledge assessment rather than a proof.
