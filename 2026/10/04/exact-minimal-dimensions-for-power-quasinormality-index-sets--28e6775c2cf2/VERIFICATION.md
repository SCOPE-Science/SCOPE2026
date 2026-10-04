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

The claim is proved symbolically over complex matrices. No external certificate or finite enumeration is needed.

The source-side checks used the exact finite-dimensional statements in Zhou–Yang, arXiv:2609.09775v1: Proposition 2.4 for the injective/nilpotent block form, Theorem 2.10 for normality of the relevant power in finite dimension, Proposition 3.1 for direct sums and additive/difference closure, Theorem 3.3 for the arithmetic-tail form, and Example 3.9 for the explicit periodic and nilpotent blocks.

The lower-bound replay is as follows. At the first admissible exponent \(m=dq\), the finite-dimensional block form diagonalizes because its injective block is invertible and annihilates the cross term through \(A^*X=0\). The nilpotent block satisfies \(B^m=0\). Consequently the large-exponent tail is controlled entirely by the injective block, forcing its period to be exactly \(d\). If \(q\ge2\), the exponent \((q-1)d\) belongs to the injective block's index set but not the target set, so it must fail for the nilpotent block. Hence \(B^{{(q-1)d}}\ne0\), forcing nilpotent dimension at least \((q-1)d+1\). For \(d\ge2\), the injective periodic block needs dimension at least \(2\). The separate boundary cases \(d=1\) and \(q=1\) then give the remaining exact values.

For the upper bound with \(d,q\ge2\), set \(r=(q-1)d+1\). The explicit direct sum \(S_d\oplus J_r\) has index set \(d\mathbb N\cap\{k:k\ge r\}\), whose first element is \(dq\); therefore it realizes exactly the required arithmetic tail in dimension \((q-1)d+3\).

Limit: this verification establishes the stated minimum dimension, not a classification of all minimizers. The literature comparison retains the residual risk stated in the review concerning older equivalent terminology.
