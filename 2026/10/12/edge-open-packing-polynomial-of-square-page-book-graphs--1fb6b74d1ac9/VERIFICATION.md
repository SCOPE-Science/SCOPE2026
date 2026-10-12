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
# Verification

The checker constructs each square-page book \(B_m\) from the spine and page triples
\[
L_i=xu_i,\qquad M_i=u_iv_i,\qquad R_i=v_i y.
\]

For each edge subset it tests the original definition directly: every selected pair \(e_1,e_2\) is rejected exactly when some third graph edge joins an endpoint of \(e_1\) to an endpoint of \(e_2\).

Independently, the checker tests the theorem's structural classification. It then compares the full cardinality distribution against
\[
3(1+z)^m-2+2mz^2+z\bigl(2(1+z)^m-1\bigr),
\]
and verifies \(\rho_e^o(B_m)=m+1\) together with the maximum-set count.

Recorded output:

```text
VERIFY_OK
m=1: rho_e^o=2, edge_open_packings=9, maximum_sets=4
m=2: rho_e^o=3, edge_open_packings=21, maximum_sets=2
m=3: rho_e^o=4, edge_open_packings=43, maximum_sets=2
m=4: rho_e^o=5, edge_open_packings=85, maximum_sets=2
m=5: rho_e^o=6, edge_open_packings=167, maximum_sets=2
m=6: rho_e^o=7, edge_open_packings=329, maximum_sets=2
edge_subsets_checked = 599184
all sets matched the structural classification and polynomial
```

The computation exhausts every edge subset for \(1\le m\le6\), a total of \(599{,}184\) subsets. It is exhaustive for those instances and corroborative only for the arbitrary-page theorem, whose proof is symbolic.
