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

# Verification of exact tree vaccination crossover

Run the standard-library-only program:

`python3 verification/tree_vaccine_verifier.py`

Expected program checks: all \(18,248\) labelled trees of sizes \(2\) through \(7\) reconstructed by Prüfer sequences; for each vertex removal, integer pair-distance histograms and an optimal certificate vertex with nonnegative coefficient-prefix gaps; eight-vertex witness coefficient vectors and exact rational evaluations. The program is an exhaustive finite checker for the lower bound, with proof of coverage supplied by the Prüfer correspondence. It does not imply anything beyond the checked tree orders.

A separate, independently implemented graph-isomorphism-based enumeration found \(1,1,2,3,6,11\) unlabelled trees at sizes \(2,3,4,5,6,7\), and checked the same prefix-dominance conclusion for all \(24\). A separate exact edge-state enumeration of the witness at \(p=1/2\) and \(p=9/10\) reproduced the rational expected outbreak sizes in the result. These independent checks were performed directly, but only the standard-library finite certificate is embedded as executable source; no claim of independent scientific audit is made.

The general \(p\)-dependence is a mathematical identity, derived from path uniqueness and summation by parts. Sampling points cannot establish uniqueness; the unique threshold follows instead from the strict increase of \(p^2+p^3\). All evidence required to replay the finite checks is present in the accompanying executable file.
