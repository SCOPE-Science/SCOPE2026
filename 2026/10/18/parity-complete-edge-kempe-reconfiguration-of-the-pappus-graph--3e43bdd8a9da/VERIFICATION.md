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

# Reproduction of the finite classification

The graph is defined from nine points and nine nonvertical affine lines over \(\mathbb F_3\), with incidence \(y=mx+b\). The two verifiers do not require any graph datasets or private files. An explicit mapping to the standard Pappus LCF presentation is checked.

Execute from the directory containing the three files:

```sh
python3 verify_factorizations.py --check-certificate kempe_certificate.json
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_colorings.cpp -o verify_colorings
./verify_colorings
```

The Python verifier enumerates all matching bijections through a branch for each admissible point-to-line assignment. It constructs all factorization triples and all nontrivial single-bichromatic-cycle switch edges. The supplied JSON certificate is recomputed rather than trusted. The independent C++ verifier colors the 27 edges directly and canonically identifies each complete coloring modulo global color permutations. Both test parity separation, component sizes and windmill adjacency, rather than relying on logged counts.

Actual successful output:

```text
VERIFY_MATCHINGS_OK vertices=18 edges=27 matchings=42 one_factorizations=20 named_edge_colorings=120
VERIFY_KEMPE_OK switch_edges=36 components=10+10 each_component=K1_join_3K3
VERIFY_BICHROM_OK central=2_profile_6+6+6_three_pairs peripheral=18_profile_18+18+6+6+6
VERIFY_PARITY_OK signs=10+10 each_parity_sector_is_one_component diameter_each=2
VERIFY_CERTIFICATE_OK factorization_masks=20 adjacency_rows=36 parity_and_profiles=true
VERIFY_DIRECT_OK vertices=18 edges=27 proper_named_3_edge_colorings=120 unlabeled_factorizations=20
VERIFY_DIRECT_OK bichromatic_hubs=2 leaves=18 Kempe_switch_edges=36
VERIFY_DIRECT_OK components=2x10 both_K1_join_3K3=true sign_classes=10+10
```

The mathematical parity-invariance argument is independent of all finite enumeration. The exact 18-vertex state-space classification is finite and exhaustive; the methods do not establish an infinite-family result. The certificate and sources are provided for transparent inspection; independent mathematical review has not been performed.
