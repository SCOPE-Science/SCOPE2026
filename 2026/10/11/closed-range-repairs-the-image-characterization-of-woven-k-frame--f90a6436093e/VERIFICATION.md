---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The explicit infinite-dimensional counterexample uses
\[
H=\ell^2(\mathbb N),\quad Ke_n=n^{-1}e_n,\quad f_n=g_n=ne_n,
\]
and yields \(Kf_n=Kg_n=e_n\). Every image weave has energy \(\|h\|^2\) and dominates \(\|K^*h\|^2\), so its \(K\)-frame bounds are \(1,1\). For \(x_N=N^{-1}e_N\), all original weaving energies equal \(1\) while \(\|x_N\|^2=N^{-2}\), forcing an unbounded upper-frame ratio. Each \(f_n\in R(K^*)\) and \(R(K)\) is nonclosed by the vector \((1/n)_{n\ge1}\) and its finite truncations.

For closed-range \(K\), the corrected ordinary frames are the projected families \(Pf_i,Pg_i\) in \(M=R(K^*)\). The identity \(\langle x,Pf_i\rangle=\langle x,f_i\rangle\) for \(x\in M\), the adjoint identity \(\langle h,Kf_i\rangle=\langle K^*h,f_i\rangle\), and the bounded preimage \(h=(K^*)^\dagger x\) prove the two implications with constants \((A,B\|K\|^2)\) and \((C,D\|K^\dagger\|^2)\) for \(K\ne0\). The zero operator is handled trivially. If \(f_i,g_i\in M\), no projections are needed.

The membership caveat is witnessed in \(\mathbb R^2\) by \(K=P_{\operatorname{span}(e_1)}\), \(f_1=g_1=e_1+e_2\): the image is a \(K\)-frame but the unprojected vectors are not vectors of \(R(K^*)\). This does not invalidate the weaker inequalities restricted to that subspace.

The full mathematical statements and proofs of the relevant arXiv source's Propositions 1.4, 2.5, 2.6 were read, including page-image verification of the disputed upper-bound step. No finite approximation is used to prove the infinite-dimensional counterexample.
