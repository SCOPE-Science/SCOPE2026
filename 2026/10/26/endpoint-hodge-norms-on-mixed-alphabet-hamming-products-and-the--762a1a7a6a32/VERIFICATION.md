---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An i-edge divergence has its i-factor in the q_i eigenspace; on this sector L is strictly positive. The product heat resolvent on the other coordinates has mass 1/q_i and distinguished-minus-other differences of fixed sign. Summing absolute gradients in direction i gives 2(q_i-1)/q_i; in direction j the other factors have mass one and the distinguished-minus-other marginal integrates to 1/(q_i+q_j), counted in two layers with q_j-1 neighbors each. Expanding the resolvent at the distinguished vertex gives Q_ee=2alpha_i, so the complementary column sum is 1+A_i-4alpha_i. Symmetry identifies row and column norms. For a<b the cut difference is positive by ab>a+b. Conditioning the resistance difference on the remaining factors gives (b-a) E[1/((a+Z)(b+Z)(a+b+Z))]. At Z=0 the resulting difference bound plus the positive remaining-factor contribution works unless (a,b)=(2,3); there the bound from any third factor c is strictly positive since 1/30-1/(15c) >= 0 and c-1-2/(c+5)>0. Equal-size factors tie by permutation. An independent rational grounded-Laplacian computation (python3 /workspace/branches/reproduce_45.py 5) tested 31 representative columns across nine products, including (2,3,4) with exact binary-direction values 14/5 and 28/9. This corroborates rather than replaces the proof.

## originality

PASS

Verified equal-alphabet, binary, and broad product precedents do not supply the mixed finite pair of formulas with the strict cycle maximizing-direction law. The later weighted-product record does cover the cut formula at unit conductance; that overlap is explicit, but it neither predates the frozen result by its catalog date nor supplies the cycle theorem. Pass is limited to the stated mixed canonical projection result, not the known equal-alphabet formulas, product resistance methods, or the general weighted cut theory.

## value

PASS

The exact direction scores remove a graph-sized projection computation for a natural heterogeneous family and identify all worst directions for both endpoint norms. In particular, the cycle ordering is not a restatement of the cut ordering: diagonal resistance competes with it, and adding a third factor restores a strict ordering that can fail for two factors. This is an exact canonical-projection invariant, not a minimal-projection theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
