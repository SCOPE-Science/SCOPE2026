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
# Reproducible verification

Both commands were executed on the embedded source and the embedded certificate:

```sh
python3 verify.py certificate.json
python3 verify_independent.py certificate.json
```

The first program exhausts perfect matchings using the least-uncovered-vertex recurrence and then derives all 1-factorizations and single-cycle switch edges. It checks all certificate tables for equality with its newly generated data and verifies the explicit sixteen-vertex graph isomorphism edge by edge. Observed output:

```text
VERIFY_CERTIFICATE_OK 20_factorizations 27_switch_edges explicit_self_isomorphism=true
VERIFY_OK GP(8,3) vertices=16 edges=24 perfect_matchings=33
VERIFY_OK matchings_two_factor_types=6+10:24,16:6,8+8:3
VERIFY_OK unordered_one_factorizations=20 profiles=16+3+1
VERIFY_OK Kempe_graph_components=16+4 edges=24+3
VERIFY_OK component_4=K_1,3 component_16=GP(8,3) via_certificate
```

The independent program assigns three named colors edge by edge, rejecting local conflicts and fixing color names at the three edges incident to vertex zero. It thus traverses all colorings up to global color permutation without using the perfect-matching recursion. It separately reconstructs every bichromatic connected component and Kempe move. Observed output:

```text
VERIFY_INDEPENDENT_CERTIFICATE_OK exact_colorings_and_Kempe_edges
VERIFY_INDEPENDENT_OK assigned_edges=24 fixed_color_names_at_root=3 full_colorings=120 unordered=20
VERIFY_INDEPENDENT_OK Kempe_edges=27 components=4+16 claw_degrees=1,1,1,3
```

The certificate is a *finite, labeled, complete* enumeration. The code is the proof of exhaustiveness: recursion explicitly visits every permitted next choice. The graph isomorphism is established by a displayed full bijection checked against the exact edge set. Neither a timeout nor sampled computation is used to exclude alternatives. No claims of independent external review, generalization to other graphs, or machine-checked infinite proof are made.
