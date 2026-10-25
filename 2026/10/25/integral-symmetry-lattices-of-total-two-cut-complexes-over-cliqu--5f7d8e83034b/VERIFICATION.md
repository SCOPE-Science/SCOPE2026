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

# Reproduction of the stated checks

Run `python3 tree_cut_verify.py` with Python 3 and no third-party packages. It reconstructs each graph \(K_m\square T\), enumerates faces of its total two-cut complex using the complementary nonedge criterion, enumerates all elements of \(S_m\times\operatorname{Aut}(T)\), and calculates their **signed reduced simplicial Lefschetz numbers**. It compares these numbers to \((-1)^{mt-4}\) times the predicted trace on the unique nonzero reduced rational homology. There are \(192\) exact permutation/sign comparisons over ten examples, including a four-vertex star and a four-vertex path. All completed successfully.

For cases with at most nine graph vertices it additionally computes actual simplicial boundary-map ranks over \(\mathbb F_2\), including the augmented degree-zero correction, and checks the predicted reduced Betti rank \((m-1)(t-1)\). These matrices confirm finite cases only; the general integral assertion, the absence of torsion, the full representation and the exact equivariant extension order follow from the proof in `RESULT.md`.

For a human proof check, independently verify that the tree incidence matrix has an integral right inverse after rooting; that \(H^1\) of the quotient multigraph is \(\bigoplus_{e} \mathbb Z^{[m]}/\mathbb Z\mathbf1\); that tree automorphisms multiply every bipartition-oriented edge by the same sign; and that Alexander duality contributes the ambient vertex-permutation sign. Finally verify that the invariant homomorphism restriction \(\operatorname{Hom}_{S_m}(\mathbb Z^{[m]},\mathbb Z)\to\operatorname{Hom}_{S_m}(\mathbb Z,\mathbb Z)\) is multiplication by \(m\). None of these verification suggestions implies that an external audit occurred.
