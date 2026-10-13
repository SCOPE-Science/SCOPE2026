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
# Verification

The included `verify.py` performs an exact finite reconstruction of the source example.

It realizes \(\mathbb F_{64}\) as \(\mathbb F_2[\theta]/(\theta^6+\theta^4+\theta^3+\theta+1)\), checks that all points in the Example 3.5 orbit table satisfy \(y^2+y=x^9\), and rebuilds the \(128\) affine rational points in the source order.  It then forms the information set
\[
O_1\cup\cdots\cup O_6\cup\{O_7(1),\ldots,O_7(7)\}\cup\{O_8(1),O_8(2),O_8(3)\}
\]
and verifies that both information and check sets have size \(64\).

For each \(a\in\mathbb F_{64}\), the script finds the two constants \(c\) for which \(c+\omega_a(a)\) solves \(z^2+z=a^9\), constructs \(\Phi_{a,c}\), and verifies that the \(128\) maps are distinct permutations of the source point set.  It checks that the full source family covers every one of the \(8128\) unordered coordinate pairs.

For the lower bound it groups coordinates into the \(64\) two-point vertical fibers and verifies that exactly three of those fibers are wholly contained in the check set, indexed by \(0\), \(1\), and \(\theta^{56}\).  With \(W=\operatorname{span}_{\mathbb F_2}\{1,\theta^{56}\}\), the script verifies the \(16\) affine \(W\)-cosets and the resulting lower bound \(2\cdot16=32\).

Finally it reconstructs the stated \(32\) maps, verifies that each belongs to the source family, and exhaustively checks that their minimum pair-coverage multiplicity is \(1\), so no coordinate pair is missed.  A successful replay ends with `VERIFY_OK`.

Unproved limits: the finite check does not minimize over automorphisms outside the source's Theorem 4.5 family, does not optimize over different information sets, and does not establish absolute bibliographic novelty.
