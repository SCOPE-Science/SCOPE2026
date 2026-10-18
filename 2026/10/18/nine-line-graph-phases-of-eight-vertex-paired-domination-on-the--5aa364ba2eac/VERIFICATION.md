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

The exact claim concerns the incidence graph defined by `y == m*x+b (mod 3)` on nine point and nine line vertices. No external numerical data files or third-party Python packages are required.

Run `python verification/verify_incidence.py` to construct and exhaustively scan all balanced two-, four-, six- and eight-vertex selections and their induced perfect matchings. It checks exactly 9 feasible six-vertex states, 216 eight-vertex states, nine eight-vertex components each of size 24, 648 exchange edges overall, uniform degree 6 and component diameter 3. It also verifies the minimum layer is edgeless.

Run `python verification/verify_geometry.py` for a separate coordinate-based exhaustive enumeration. It tests perfect matchings by enumerating all bijections, checks all possible four-point/four-line selections against the explicit nine-core/24-extension construction, verifies the forbidden twelve-cycle and identifies each exchange component as a line graph with 72 edges and diameter 3. It rules out all between-core jumps.

Run `python verification/verify_orbits.py` to check the stated action of 108 affine transformations on four-point selections. Its four orbits have sizes 18, 27, 54, 27 and compatible four-line choice counts 12, 0, 0, 0, respectively. This proves the finite classification lemma with a second, symmetry-reduced coverage check.

The three recorded output files are included under `verification/`; they are observational records, not substitutes for the supplied proofs or scripts. These finite checks exhaust the stated 18-vertex object. No claim is made for larger biaffine planes. The literature comparison is not a machine-verifiable certificate of global priority. Independent scientific evaluation has not been performed.
