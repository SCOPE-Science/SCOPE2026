---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

The weighted-tree transport cut formula yields κ(xy)=2(p_x(y)+p_y(x))−2; summing over m edges gives total 2 and excludes k>2/m. For arbitrary nonsymmetric weights normalized by min=1, central t and leaf totals X≥a, Y≥b max(1,kt/(2−kb)) imply a strictly increasing scalar necessary condition Φ_{a,b,k}(t)≥k, whose unique sharp root is the two-branch T_{a,b}(k). At k*=4/[2b+1+sqrt(1+4a(b+1))] the active inequality changes. Explicit leaf weights 1 and B=max(1,kT/(2−kb)) attain the bound; equality and strict monotonicity force the unique normalized profile. Endpoint checks T(0)=sqrt(ab), T(2/m)=b+1 and boundary k*=2/m iff a=b. Independent numerical curvature checks support but do not replace this proof.

## originality

PASS

Best-of-knowledge originality after mathematical implication comparison; specific prior deductions and source-access limitations are recorded in the four named checks.

## value

PASS

The entire real-k sharp tradeoff and interior leaf-class activation threshold for a natural two-branch tree are explicit, enabling precise weighted-curvature comparisons; it refines an earlier nontrivial general **implicit** theorem rather than claiming a wholly new theory. Natural boundary and cusp questions make the exact formulas meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
