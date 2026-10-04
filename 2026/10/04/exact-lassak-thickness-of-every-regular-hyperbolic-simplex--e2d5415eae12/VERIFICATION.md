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

For vertices \(v_0,\ldots,v_d\) of a regular hyperbolic simplex with \(q=\cosh\ell\), the Lorentz Gram matrix is
\[
G=(q-1)I-qJ.
\]
Direct multiplication gives
\[
G^{-1}
=
\frac1{q-1}I
-
\frac q{(q-1)(dq+1)}J.
\]

If \(s_i=\langle v_i,n\rangle\) are the nonnegative pairings with a unit spacelike normal of a supporting hyperplane and \(M=\max_i s_i\), then
\[
1=s^TG^{-1}s.
\]
After writing \(t_i=s_i/M\), this becomes
\[
M^2
=
\frac{q-1}{\sum_i t_i^2-\frac q{dq+1}(\sum_i t_i)^2}.
\]
At least one \(t_i\) is zero.

On each coordinate face the denominator has Hessian
\[
2(I-cJ),
\qquad
c=\frac q{dq+1},
\]
whose exceptional eigenvalue is
\[
2(1-dc)=\frac2{dq+1}>0.
\]
Hence the denominator is strictly convex there, so a maximum has a zero-one pattern. With \(k\) ones its value is
\[
F_k=\frac{k((d-k)q+1)}{dq+1},
\]
and
\[
F_{k+1}-F_k
=
\frac{(d-2k-1)q+1}{dq+1}.
\]
For \(q>1\), this changes sign exactly around
\[
k=\left\lceil\frac d2\right\rceil,
\]
proving the unique cardinality of the minimizing support pattern.

The embedded `verify.py` symbolically replays these identities, checks the exact discrete maximizer for several rational values of \(q>1\) and dimensions through \(12\), and verifies the algebraic equivalence of the \(d=3\) specialization with Lassak's edge-supported tetrahedral expression after \(\ell=2x\).

The replay output is:

`VERIFY_OK regular hyperbolic simplex Lassak thickness`

The finite range in the checker is not used as an all-dimensional proof; it only guards the symbolic reductions and special-case algebra. The proof in `RESULT.md` supplies the quantifiers and sign argument for every \(d\ge2\) and every \(\ell>0\).
