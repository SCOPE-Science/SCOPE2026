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
# Reproduction and scope

With standard Python 3, run `python3 VERIFY.py`. It has no nonstandard dependencies. The checker constructs the Pauli matrices and rank-one eigenprojector numerators, confirms five mutually unbiased bases, enumerates fifteen maximal commuting triples, verifies forty non-basis rays with support multiset \(\{2,2,2,4,4\}\) and twenty basis rays with \(\{1,4,4,4,4\}\), and tests all \(\binom{20}{3}=1140\) independent triples and all \(\binom{20}{4}=4845\) four-ray determinants. Exactly \(600\) four-subsets are dependent and they are precisely the four-subsets of the forty certified six-orthogonality sets.

No tolerance tests, random trials, external files or incomplete enumeration are used. Matrix entries throughout the projector and determinant computations are Gaussian integers of bounded magnitude and their integer components are exactly representable in Python's complex numbers. The final step from rank incidence to **all** complex vectors is proved analytically in RESULT.md; the executable by itself does not verify the literature-based uniqueness of all complete five-basis systems. The motivating 2026 preprint was available only at the full-abstract/metadata level, and historical originality is subject to unindexed literature. This is a scientific reproducibility record, not a claim of independent certification.
