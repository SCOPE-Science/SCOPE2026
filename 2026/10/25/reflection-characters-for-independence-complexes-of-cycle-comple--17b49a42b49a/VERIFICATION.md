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

# Verification record

The proof's critical exact identity is \(M^3=(n-1)I_3\); it follows by multiplying the explicit matrices in the result. The three reflected path forms evaluate respectively to \(u^\mathsf T N M^{3h+1}e=0\), \(u^\mathsf T M^{3h+1}e=0\), and \(u^\mathsf T N M^{3h-2}Ne=n(n-1)^h\). The homology-concentration premise is Theorem 22 of arXiv:2307.12401.

A second, independent finite implementation constructs the original categorical-product graph, its reflection vertex orbits and their forbidden internal edges, then recursively computes the exact integer signed independence count of the orbit graph. A separate implementation applies the transfer matrices. Exact agreement holds for all \(1\le r\le5\), \(2\le n\le5\), and both reflection-axis types where applicable. A third method enumerates every original independent set and its signed orbit cycles for \((m,n)=(3,3),(6,3),(6,4),(9,3)\), agreeing with the preceding two checks. Run `python3 cycle_reflections_checker.py`.

Limits: the finite checker is not a proof for unbounded \(r,n\); the matrix identity and folding argument supply that proof. No statement about joint nontrivial color permutations, integral representations or independent external validation is made.
