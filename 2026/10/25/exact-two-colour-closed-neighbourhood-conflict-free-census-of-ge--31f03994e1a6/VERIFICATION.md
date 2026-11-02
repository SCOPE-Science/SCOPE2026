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

For n>=3 and 1<=k<n/2 each generalized Petersen vertex has four distinct closed neighbors. Among two named colors, exactly one occurrence of a color iff the red indicator sum on that neighborhood is odd (1 or 3). Outer constraints determine each inner bit uniquely y_i=1+x_{i−1}+x_i+x_{i+1} in F2; inner constraints become the homogeneous cyclic linear equation [1+(T^-1+1+T)(T^-k+1+T^k)]x=0. Multiplication by t^(k+1) yields polynomial h_k, and the kernel of multiplication by h_k in F2[t]/(t^n+1) has size 2^deg gcd for repeated factors too. For k=1 h=(1+t)^4 and the t+1 multiplicity of t^n+1 yields 2/4/16 cases. For k=2 h=(1+t)(1+t^5), so cyclic differences of outer colors are 5-periodic; closure parity yields exactly the 2/4/32/64 cases and complete characterization. All-red and all-blue fail. Independent brute reconstruction for all admissible k at n=3..10 matched gcd; GP(5,2)=32, GP(10,2)=64.

## originality

PASS

PASS for the complete two-color odd-parity/unique-neighbor assignment census on the natural GP(n,k) family. Related balanced-closed-neighborhood Petersen results require exactly two red and two blue per closed neighborhood (even parity), mathematically disjoint from the present 1/3 split. Sedlar–Škrekovski study improper closed-neighborhood conflict-free coloring but focus on existence, planar bounds and gadgets, not the all-(n,k) gcd kernel count. The general linear-algebra kernel method is standard and not independently novel; the graph-specific reduction and exact phase diagram are the assessed results. A previously published binary-kernel census under odd-neighborhood coloring terminology remains a residual risk.

## value

PASS

Closed-neighborhood conflict-free coloring is natural, and a full count of all named assignments on the generalized Petersen family refines mere chromatic feasibility. The exact polynomial gcd formula measures dimension of a cyclic binary code attached to the graph, with a nontrivial five-periodicity transition at k=2. This is a complete infinite-family invariant, not an arbitrary small-case table or an unsupported generalization to proper coloring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
