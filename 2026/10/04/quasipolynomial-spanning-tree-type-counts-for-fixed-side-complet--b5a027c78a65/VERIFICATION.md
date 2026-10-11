---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Deleting all leaves on the large side of a spanning tree of \(K_{d,m}\) leaves a finite core with at most \(d-1\) retained large-side vertices because \(\sum(\deg(v)-1)=d-1\). Re-expanding a fixed core is exactly a weak composition of \(m-k_F\) among the \(d\) small-side vertices, modulo the core automorphism action. The action on that side is faithful because two distinct retained large-side vertices with the same neighborhood would create a 4-cycle. Burnside therefore gives the displayed root-of-unity rational generating function, hence a quasipolynomial of degree \(d-1\) and period dividing \(\operatorname{lcm}(1,\ldots,d)\). The reciprocal-automorphism sum combined with the labeled-core count yields the stated leading coefficient. The assigned verifier independently reconstructs all cores for \(d\le4\), compares literal orbits with Burnside counts, and matches the known small-\(d\) formulas and tables.

## originality

PASS

Yan and Zhang state only the fixed-\(d\) asymptotic \(A_dn^{d-1}+O_d(n^{d-2})\), while the audited theorem upgrades the bounded-core decomposition to exact orbit enumeration for every \(m>d\). Current Resultary and web searches did not locate a general fixed-\(d\) quasipolynomial or Burnside formula. Exact formulas for small sides are acknowledged as prior special cases. The Yan--Zhang full text was not accessible through the web route used in this run, so the originality judgment is best-of-knowledge with that explicit residual risk rather than a whole-document noncoverage claim.

## value

PASS

The exact fixed-side count is the natural refinement of a current asymptotic spanning-tree-type theorem. Turning the bounded-core method into an explicit finite Burnside sum and proving quasipolynomiality for every \(m>d\) gives reusable exact structure rather than a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
