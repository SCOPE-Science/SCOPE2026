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
# Reproducibility

The standalone standard-library checker `verify_regular_gsets.py` builds all coset actions from finite abelian groups, constructs every equivariant map from its source-orbit representative images, and independently searches every candidate equivariant map for a witness to the semigroup regularity equation. It compares complete image-orbit histograms to the proposed inclusion–exclusion formula and also checks the unrestricted normalizer. Cases: \(C_2\) with two fixed orbits and one/two free orbits; \(C_4\) with one orbit of each stabilizer order; \(C_2\times C_2\) with two fixed orbits and one orbit of each remaining subgroup type. The output file records four passed cases, 3253 maps and 1793 regular maps. Run `python3 verify_regular_gsets.py`; no external modules or network services are needed.

The arbitrary-parameter result rests on the orbit-map classification and counting proof; finite checks alone do not prove that result. No independent audit has been performed.
