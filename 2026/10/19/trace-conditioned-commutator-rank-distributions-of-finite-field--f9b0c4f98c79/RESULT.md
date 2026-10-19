# Trace-conditioned commutator rank distributions of finite-field idempotents

## Finding

Fix a prime power \(q\), an integer \(n\ge2\), a rank-one idempotent \(E\in M_n(\mathbf F_q)\), and an integer \(1\le s<n\). Count rank-\(s\) idempotents \(F\) by the two natural invariants
\[
a=\operatorname{tr}(EF)\in\mathbf F_q,\qquad c=\operatorname{rank}(EF-FE)\in\{0,1,2\}.
\]
Define the Gaussian binomial and rank-fixed idempotent count
\[
G_q(m,k)={m\brack k}_q=\prod_{j=0}^{k-1}\frac{q^{m-j}-1}{q^{k-j}-1},\qquad I_q(m,k)=G_q(m,k)q^{k(m-k)},
\]
with \(I_q(m,k)=0\) for \(k<0\) or \(k>m\). For every \(a\in\mathbf F_q\), put
\[
T(a)=\frac{I_q(n,s)}{(q^n-1)q^{n-1}}\left[(q^s-1)(q^{n-s}-1)q^{n-2}+q^{n-1}\bigl((q^s-1){\mathbf{1}}_{a=1}+(q^{n-s}-1){\mathbf{1}}_{a=0}\bigr)\right].
\]
For \(i=0,1\), define \(J_0=I_q(n-1,s)\), \(J_1=I_q(n-1,s-1)\), \(w_0=q^s\), and \(w_1=q^{n-s}\). The exact number \(N(a,c)\) of such \(F\) is
\[
\boxed{\begin{aligned}
N(i,0)&=J_i,\\
N(i,1)&=2(w_i-1)J_i,\\
N(i,2)&=T(i)-(2w_i-1)J_i\qquad(i=0,1),\\
N(a,2)&=T(a),\quad N(a,0)=N(a,1)=0\qquad(a\notin\{0,1\}).
\end{aligned}}
\]
All these numbers are nonnegative integers. They sum to \(I_q(n,s)\).

The full similarity class of the commutator \(C=EF-FE\) follows: \(C=0\) if \(c=0\); if \(c=1\), it has one nilpotent Jordan block of size two and the remaining blocks of size one; if \(c=2\) and \(a=0\) or \(1\), it has one nilpotent Jordan block of size three and remaining singleton zero blocks. If \(a\notin\{0,1\}\), it is similar to the companion matrix of \(t^2+a(1-a)\) direct-summed with \(n-2\) zero dimensions. Its characteristic polynomial is always
\[
\chi_C(t)=t^{n-2}\bigl(t^2+a(1-a)\bigr).
\]
In particular, over \(\mathbf F_2\) every such commutator is nilpotent of index at most three, whereas for every \(q>2\) there are nonnilpotent examples. The formulas determine precisely how often each nilpotency index occurs.

For example, in dimension \(4\), with \(q=2\) and \(s=2\), there are \(560\) idempotents \(F\); for either value of \(a\), the commutator rank multiplicities for \(c=0,1,2\) are \(28,168,84\), respectively. Hence exactly \(168\) produce nilpotency index three.

## Assumptions and scope

All matrices are over a field \(\mathbf F_q\), including fields of characteristic two. A rank-one idempotent is a nonzero matrix satisfying \(E^2=E\) with one-dimensional image. Both ranks are ordinary vector-space ranks over \(\mathbf F_q\). The scalar \(a\) is an element of the field, not the integer rank of \(EF\). The theorem counts each labeled matrix \(F\) once, with the rank-one matrix \(E\) fixed, and makes no claim about unrestricted pairs of idempotents of arbitrary ranks.

For completeness, the excluded extreme ranks have one element apiece: \(s=0\) gives \(F=0\), \(a=c=0\); \(s=n\) gives \(F=I_n\), \(a=1\), \(c=0\).

## Proof

**1. Reduction and commutator spectrum.** Conjugation transports the counting problem bijectively, so fix
\[
E=\begin{pmatrix}1&0\\0&0_{n-1}\end{pmatrix},\qquad
F=\begin{pmatrix}a&b\\d&D\end{pmatrix},
\]
with a row \(b\), a column \(d\), and a square block \(D\) of size \(n-1\). Then \(a=\operatorname{tr}(EF)\) and
\[
C=\begin{pmatrix}0&b\\-d&0\end{pmatrix},\quad
c={\mathbf{1}}_{b\ne0}+{\mathbf{1}}_{d\ne0}.
\]
The upper-left equation in \(F^2=F\) gives \(bd=a(1-a)\). Thus \(c=2\) whenever \(a\notin\{0,1\}\). The Schur-complement polynomial identity, valid first for formal invertible \(t\) and hence polynomially, yields \(\chi_C(t)=t^{n-2}(t^2+bd)\). Direct multiplication gives \(C^3=-bd\,C\). When \(a\in\{0,1\}\) and \(c=2\), the outer product \(db\) is nonzero, so \(C^2\ne0\), and therefore \(C\) has one length-three nilpotent Jordan chain. When \(c=1\), \(C^2=0\) and \(C\) has exactly one length-two chain. If \(bd\ne0\), the two-space spanned by the first coordinate vector and \(d\) is invariant, cyclic, and has characteristic polynomial \(t^2+bd\), with an invariant complementary zero-space of dimension \(n-2\).

**2. The trace-conditioned total.** It is classical that \(I_q(n,s)\) counts rank-\(s\) idempotents: choose their image subspace, then one of \(q^{s(n-s)}\) complementary kernels. Likewise, the number of rank-one idempotents is \(I_q(n,1)=(q^n-1)q^{n-1}/(q-1)\). Double-count ordered pairs \((E,F)\) with \(a=\operatorname{tr}(EF)\) by fixing \(F\) to be the diagonal projection on \(\mathbf F_q^s\oplus\mathbf F_q^{n-s}\). Write \(E=uv^{\mathsf T}\), where \(u=(x,y)\), \(v=(\alpha,\beta)\), and \(\alpha(x)+\beta(y)=1\). Two such pairs determine the same \(E\) precisely up to \((u,v)\mapsto(\lambda u,\lambda^{-1}v)\) with \(\lambda\ne0\). The additional condition is \(\alpha(x)=a\). When \(x,y\ne0\), the number of choices is \((q^s-1)(q^{n-s}-1)q^{n-2}\) for each \(a\). When \(y=0\), only \(a=1\) is possible and there are \((q^s-1)q^{n-1}\) choices; when \(x=0\), only \(a=0\) is possible and there are \((q^{n-s}-1)q^{n-1}\) choices. Dividing the resulting number of pairs by \(I_q(n,1)\) yields the stated \(T(a)\). This argument works in every characteristic and for both one-dimensional boundary blocks.

**3. Exact commutator ranks at the exceptional scalar values.** If \(c=0\), then \(b=d=0\), and idempotence forces \(D^2=D\). For \(a=0\), its rank is \(s\), giving exactly \(J_0\) choices. For \(a=1\), its rank is \(s-1\), giving exactly \(J_1\) choices. If \(a=0\), \(d=0\), \(b\ne0\), then \(bD=b\); a rank-\(s\) idempotent \(D\) has exactly \(q^s-1\) such rows. The transposed case \(b=0\), \(d\ne0\) contributes equally. Hence \(N(0,1)=2(q^s-1)J_0\). If \(a=1\), \(d=0\), \(b\ne0\), then \(bD=0\) with \(D\) of rank \(s-1\), giving \(q^{n-s}-1\) options per \(D\), and the transposed case contributes equally. Hence \(N(1,1)=2(q^{n-s}-1)J_1\). All remaining matrices at either scalar value have \(b,d\ne0\), so subtract the two known strata from \(T(0)\) or \(T(1)\) to obtain \(N(i,2)\). For all other \(a\), the relation \(bd=a(1-a)\ne0\) already forces \(c=2\). These cases are exhaustive and disjoint.

**4. Existence of nonnilpotent instances.** If \(q>2\), fix \(a\notin\{0,1\}\), and take a rank-one idempotent on a two-dimensional summand with diagonal entry \(a\) and off-diagonal product \(a(1-a)\), extended by a rank-\(s-1\) projection on the remaining \(n-2\) coordinates. Its commutator with \(E\) is nonnilpotent. If \(q=2\), all scalar values are \(0\) or \(1\), so \(C^3=0\) for every \(F\).

## Verification

The standalone file `check.py` enumerates every matrix over prime fields in six test cases: \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\). It tests idempotence, computes rank, and checks every cell of the scalar/rank distribution rather than only the total. All cells agree. A second set of exact integer arithmetic checks verifies nonnegativity and that the formulas sum to \(I_q(n,s)\) for all \(2\le n\le8\), \(1\le s<n\), and the field orders \(q=2,3,4,5,7,8,9\). These finite checks are not an infinite proof; the proof above is algebraic and valid for every prime power.

## Relationship to prior work

Ferraz, Polcino Milies, and Taufer (2017), *Left ideals in matrix rings over finite fields*, prove the rank-fixed idempotent count \(I_q(n,s)\) and parameterize idempotents generating a given left ideal. That classical total is used here and is not claimed as new. Their rank-by-rank and left-ideal enumerations do not determine the additional invariant \(\operatorname{tr}(EF)\), the commutator rank, or the joint similarity-type multiplicities for a fixed rank-one \(E\).

Drnovšek (2023), *On commutators of idempotents*, characterizes the existence of commutator representations over rings with two invertible and in operator settings. Its Theorems 2.1 and 2.2 do not prescribe the rank of one idempotent, enumerate finite-field idempotents by the trace of their product, or determine exact multiplicities of commutator ranks and nilpotency indices; moreover, the theorem requiring two invertible does not cover characteristic two. The contribution here is the all-characteristic, all-dimension, finite-field joint distribution, not the underlying block identity or the known total number of idempotents.

## Limitations

Only one idempotent has rank one, and the other has prescribed rank. The formulas count labeled matrices, not conjugacy classes of pairs. The exact spectrum is determined in this setting but does not characterize commutators of arbitrary-rank idempotents. Exhaustive computations cover finite small cases only. Related unpublished or differently indexed enumerations could imply some or all of the formula; the originality assessment is relative to literature inspected and is not a universal priority claim.

## References

- R. A. Ferraz, C. Polcino Milies, and E. Taufer, *Left ideals in matrix rings over finite fields*, arXiv:1711.09289v1 (public 2017-11-25), https://arxiv.org/abs/1711.09289.
- R. Drnovšek, *On commutators of idempotents*, arXiv:2311.16724v1 (public 2023-11-28), https://arxiv.org/abs/2311.16724.
- T. Özdin and E. Gümüşel, *Characterizations of commutators involving idempotents in certain subrings of \(M_2(\mathbb Z)\)*, Turkish Journal of Mathematics (2023). Available journal metadata reviewed; full text not retrieved.
