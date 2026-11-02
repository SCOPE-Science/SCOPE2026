---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

With any rational origin on the genus-one curve, write G=C(F_q) and T=[H-3O] in Pic^0(F_q). A line through three distinct rational points has group sum T; pairs of distinct points admit a rational tangent line when 2a+b=T or a+2b=T. Four covering lines must partition the twelve points into four distinct collinear triples, so sum(G)=4T. In cyclic C_12, sum(G)=6, which is not in 4G; four lines are impossible. For C_2 x C_6, sum(G)=0 and 4T=0 exactly when T lies in 3G, equivalent to a rational flex. Six explicitly inspected finite line certificates cover G with four lines only in this latter case and with five otherwise; the geometric group-to-line argument lifts them to any characteristic. An independent hypergraph generator constructed all tangent/secant rational line-point subsets and independently optimized exact set cover by dynamic programming over 2^12 subsets: minimum counts for C12 T=0,1,2 were 5,5,5; for C2xC6 T=0,1,2 were 4,5,5. The two F11 examples were independently checked to have 12 points and the predicted 2-torsion counts.

## originality

PASS

Zero-sum partition results, including group 3-ZSP theorems for noncyclic order-12 groups, can explain the zero-sum four-triple partition in the rational-flex case; that component is not claimed independent from group-partition literature. The assessed contribution is the whole geometric twelve-point covering dichotomy, including the hyperplane class T without a flex, the sharp five-line upper bounds for all remaining cases, and explicit realization. Asgarli et al. primarily address asymptotic plane-curve covering in the inspected public abstract. Their full manuscript was inaccessible, leaving possible exact low-point examples as priority risk.

## value

PASS

Exact minimal line-cover numbers of rational points are natural incidence invariants. The classification finds the first nontrivial group/embedding obstruction at cardinality twelve, including nonflex models, and provides sharp universal upper certificates and examples attaining both values. This complete finite classification is mathematically meaningful without a general all-cardinalities theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
