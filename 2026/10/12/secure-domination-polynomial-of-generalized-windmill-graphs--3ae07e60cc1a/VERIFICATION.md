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

A secure-dominating set without the universal center must meet every clique blade, and same-blade replacement secures every outside blade vertex; moving one selected vertex to the center defends the center. With the center selected, at most one empty blade is sufficient; two empty blades defeat the only available defender of a vertex in one empty blade. These exhaustive cases yield D_s=A_m^r+x(A_m^r+r A_m^{r-1}), A_m=(1+x)^m-1, valid r,m>=2. Least exponent r, coefficient m^{r-1}(m+r), and top degree rm+1 recover minimum counts/parameters. Independently re-implemented graph adjacency and direct defender-swap checks for (r,m)=(2,2),(2,3),(3,2),(3,3), yielding minimum counts 8,15,20,54 and exact full coefficients; proof, not bounded experiments, handles all r,m.

## originality

PASS

No inspected prior result proved the exact submitted mathematical conclusion; comparisons evaluate statements and implications rather than titles, with bounded source-access and bibliographic uncertainties retained.

## value

PASS

The exact defender-swap threshold is a substantive structural characteristic of a natural clique-blade block-graph family. The closed cardinality polynomial enumerates all feasible sets rather than only solving the known minimum optimization problem; parameter reconstruction and minimum-set multiplicities are useful invariant data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
