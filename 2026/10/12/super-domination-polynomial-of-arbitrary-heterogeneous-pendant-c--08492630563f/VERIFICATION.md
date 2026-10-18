---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a super dominating set S, its omitted roots U cannot have omitted private leaves because an omitted leaf would lack a selected neighbor. Any selected root may support at most one omitted private leaf, and if it does, no adjacent base root may be omitted or the root would have two omitted neighbors. Conversely selecting all other vertices witnesses each omitted root by any own selected leaf (r_v>=1), and each allowable omitted leaf by its selected root. This gives a bijection with U and zero/one leaf choices at v outside N[U]. Counting selected vertices gives R+|N(U)\U| plus factors x+r_v. Constant term requires U a component union, yielding the component product. With two omissions, disallowed pairs are two leaves of one bundle, root/own leaf, and neighbor root/leaf, yielding the coefficient formula. Independent direct defining-predicate brute force agreed with the polynomial on all 74 base/multiplicity instances n<=3, including isolated/disconnected roots. No claim that finite checks prove arbitrary n.

## originality

PASS

The scalar gamma_sp(G o N_r)=nr and a full one-leaf minimum-set count 2^{c(G)} are already published, as are polynomial definition and formulas for other graph families. The claimed new part is the entire heterogeneous all-subset boundary polynomial with its weighted edge coefficient and component product for arbitrary positive r_v. No inspected primary statement implies these distributions automatically; Kaidash 2024 chapter remains inaccessible after lawful OA and authorized access attempts.

## value

PASS

An exact all-cardinality enumerator on arbitrary base graphs with heterogeneous leaf bundles is a natural graph polynomial that refines the known scalar super-domination number and captures both component structure and a weighted edge statistic. The closed bijection is useful for extracting further coefficient identities; this is not mere recomputation of known minimum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
