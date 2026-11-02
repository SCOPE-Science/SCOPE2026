---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Summing LG(:,y)=delta_y-1/N over descendant subtrees gives edge increment 1_{y in subtree}-q_l; telescoping along root-to-x and zero row sums yield G(x,y)=t(x,y)+H-F(|x|)-F(|y|). Exact LCA expectation and centering show |R_h(k)-2(1-q1)F(k)|<=2delta_h, where delta_h<=h*b^(h+1)/(b^(h+1)-1)^2. Uniformly in k this yields ||G||_infty/N->2/b with O_b(h) unscaled error; fixed-depth limit is (2/b)(1-b^-k). Separately the leaf sign partition gives exact absolute row formula. Independent rational matrix identity LG=I-11^T/N and leaf response checked b=2,3,h=1..3, and actual check.py read; finite tests only corroborate.

## originality

PASS

General weighted-tree Green/inverse formulas are old, but evaluating a sharp global endpoint row-sum asymptotic 2/b and the full b-ary depth profile requires explicit LCA absolute-value analysis not present in inspected primary sources.

## value

PASS

A natural canonical hierarchy has highly nonuniform Green response: exact sharp linear amplification coefficient and every fixed-depth normalized row limit, with bounded quantitative remainder and exact leaf formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
