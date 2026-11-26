---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For n≥3, a set on one shore alone is not dominating (in particular, a singleton does not dominate its own shore); a selected shore of size one with both shores represented leaves its deleted-match partner either isolated or undominated. With both shores of size at least two every vertex is dominated and every selected vertex has an induced neighbor. In a disconnected induced subgraph each component therefore meets both shores, and no vertex can have more than one opposite-shore vertex outside its component. This forces two components of one vertex per shore and identical paired index sets. Thus D_c=x⁴(R_n²−C_n), with C_n=binom(n,2) and R_n(0)=C_n>sqrt(C_n). In the integral for R_n, differentiating once for odd n gives an even exponent and a strictly positive integral; for even n both R_n and its second derivative are strictly positive. The leading degree and 0<R_n(−2)<sqrt(C_n)<R_n(−1) give exactly the two level crossings, with nonzero derivative even for n=3 or 4. On [1,2], R_n(−y)/n=1/y+O(1/n) uniformly, giving the right-root limit. For the left root, at any fixed y=2+δ the exponential term outgrows n, giving y_n→2 by the unique crossings; at y_n the exact equations for (y_n−1)^n/n have limits 2sqrt(2)−2 (even) and 2sqrt(2)+2 (odd). Taking logs first gives ε_n=O(log n/n), so replacing n log(1+ε_n) by nε_n incurs o(1). The proof is for all n≥3 and concerns only real roots. No numerical replay was needed to establish these conclusions; the frozen verifier's finite checks are supporting evidence only. Its int.bit_count would require Python 3.10+, notwithstanding the Python 3.8 note.

## originality

PASS

The supported distinct claim is the all-order nonzero real-root classification and the two asymptotics, including the parity-specific constants. The polynomial and zero multiplicity are already covered; they are background, not original results. No inspected comparator supplies or gives this full root theorem by a direct specialization.

## value

PASS

The crown is a standard graph family. For its known enumerator, an all-order exact count and separation of simple real zeros is useful root geometry, not an extra coefficient computation. The interior limit and parity-dependent boundary scale distinguish two mathematical mechanisms and give researchers quantitative benchmarks for this graph-polynomial family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
