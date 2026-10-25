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
Run the following from a clean copy of the embedded files with Python 3, SymPy, and a C++17 compiler:

```
python3 build_restrictions.py > setup_log.txt
g++ -O3 -std=c++17 enumerate.cpp -o enumerate
./enumerate > census_log.txt
python3 orbit_check.py > orbit_log.txt
python3 group_check.py > group_log.txt
python3 verify.py > verification_log.txt
```

All 7,174,453 normalized quartics are visited in the C++ loop; `high_forms.tsv` contains all 2,782 having at least eight rational bitangents, not a sample. The coefficient-action orbits of the complete set sum to 2,782, and `group_check.py` verifies the five generators produce all 5,616 projective matrices. The independently coded `verify.py` calculates the seven representative line restrictions symbolically, evaluates singularity for all six excluded orbit representatives and proves smoothness of the unique surviving representative by unit Jacobian ideals in three affine charts. The main text also gives a hand-checkable derivative proof. It verifies the unique rational curve point and three concurrent nonbitangent lines.

The reference outputs and coefficient certificates are attached; they are not substitutes for rerunning the exhaustive check. Computation and proof concern rational bitangents over \(\mathbf F_3\), not all geometric bitangents over an algebraic closure or curves over another base field.
