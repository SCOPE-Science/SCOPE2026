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

The exact standalone program `verify.py` needs only Python 3 and was run from its actual package source. Its full checks are finite-field multiplication in \(\mathbb F_4\), complete row-reduced enumeration of all \(357\) rank-two subspaces of \(\mathbb F_4^4\), exact cubic-containment testing, Frobenius orbit counts, and exhaustive projective counts over \(\mathbb F_2\) and \(\mathbb F_4\).

Expected terminal lines:
```
GEOMETRIC_PLANES=27, F2_PLANES=15, F4_NEW_PLANES=12, FROBENIUS_PAIRS=6
CLEBSCH_F2_POINTS=15, CLEBSCH_F4_POINTS=45
DIRECT_SEGRE_F2_AND_F4_COUNTS_AND_CONE_TRANSLATION_OK
SEGRE_CONE_F2_POINTS=31, F4_POINTS=181
PICARD_FROBENIUS_EIGEN_MULTIPLICITIES=+1:6,-1:1
ZETA_S=1/((1-T)(1-2T)(1-4T)^6(1+4T)(1-8T))
VERIFY_OK
```
The script checks the enumerated finite geometry. The infinite-field geometric-line count, reducedness of the Fano scheme, and formulas for all extension degrees are justified separately by the proof in `RESULT.md`. A finite experiment is not being substituted for these geometric arguments. Independent validation has not been performed.
