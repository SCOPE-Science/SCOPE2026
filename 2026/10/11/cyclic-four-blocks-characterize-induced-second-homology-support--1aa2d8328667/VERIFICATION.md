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

The accompanying `verify.py` performs only finite exact computations over \(\mathbf F_2\).

It reconstructs the \(30\) tetrahedra from the three cyclic difference cycles and verifies \(f=(10,40,60,30)\). It computes \(\operatorname{rank}\partial_2=30\) and \(\operatorname{rank}\partial_3=29\), hence \(\dim H_2(K;\mathbf F_2)=1\).

It then checks all \(\binom{10}{4}=210\) four-subsets and proves computationally that exactly ten are missing tetrahedra, namely the cyclic four-blocks. Finally it checks every one of the \(2^{10}=1024\) vertex subsets, computes the image rank of local second homology in global second homology, and verifies the complete if-and-only-if support criterion and all layer counts.

The seven-vertex set \(\{0,1,2,4,5,6,8\}\) is checked as a zero-image counterexample to any universal threshold below eight. The statement is finite and object-specific; no infinite-family conclusion is inferred from the computation.
