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

# Reproducibility and limits

The package contains source and exact output of two independently implemented exhaustive group enumerators, a finite-field line-enumeration and coefficient verifier, and a consistency check. From the containing directory, run:

```sh
python3 verify_f29.py
c++ -O2 -std=c++17 verify_theta_permutations.cpp -o verify_theta
c++ -O2 -std=c++17 verify_symplectic_matrices.cpp -o verify_matrices
./verify_theta > result_theta.txt
./verify_matrices > result_matrices.txt
python3 verify_consistency.py
```

The expected output is `VERIFY_F29_OK`, group size 1,451,520 in each independent enumeration, 25 distinct common cycle spectra, the minimum-orbit histogram \(\{1:984852,2:71820,3:96768,4:90720,7:207360\}\), and `VERIFY_GROUP_OK`. The reconstructed `group_cycle_spectra.csv` and `bitangents_F29.csv` should reproduce the embedded CSV files byte-for-byte.

The explicit coefficient tests cover all \(29^2+29+1=871\) projective lines defined over \(\mathbb F_{29}\); the 28 distinct bitangent identities and the classical count of 28 geometric bitangents prove exhaustiveness. The group test reaches the complete finite group by generating its known order with symplectic transvections. These finite exact checks certify the necessary calculations. The universal inference additionally uses the standard theta-characteristic correspondence, and sharpness uses the written Kummer twist argument; merely replaying logs without these arguments does not establish the theorem.

The computation does not classify the fields of definition of bitangent contact points, does not cover characteristic two, and does not establish that all 25 abstract cycle types arise geometrically over each finite field.
