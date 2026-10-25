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

# Reproduction and mathematical boundaries

Extract `check_derivations.py` with the other files and run `python3 check_derivations.py` using Python 3 without external dependencies. The source constructs \(D|_{V\oplus W}\) directly from its two-generator and four quadratic-basis coefficients and independently row-reduces matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\). Its \(\mathbb F_4\) arithmetic uses the irreducible polynomial \(t^2+t+1\).

An actual replay returned `DERIVATION_SPECTRUM_OK` and `LEIBNIZ_BASIS_OK`. The complete histograms from exhaustive \(q=2\) and \(q=3\) runs are
\[
(1,45,466,576,3008,0,0),
\quad(1,320,6240,5832,217242,104976,196830).
\]
Every \(2\times2\) leading matrix was checked for its tensor-square rank in all four tested fields; the full quadratic parameter is exhaustively traversed only for \(q=2\) and \(q=3\). The checker also samples 250 quadratic blocks per leading matrix in each tested field and separately tests the Leibniz identity on all pairs of basis words in 160 random derivations per field. Sampling does not certify an infinite family.

The mathematical proof in `RESULT.md` is an all-characteristic argument using the explicit tensor-square matrix, the exact block-rank identity, and closed counts of \(2\times2\) matrices. The claimed scope is all finite fields and exactly the two-generator length-three free associative quotient; nothing is asserted about arbitrary nonmonomial quotients or Jordan types.
