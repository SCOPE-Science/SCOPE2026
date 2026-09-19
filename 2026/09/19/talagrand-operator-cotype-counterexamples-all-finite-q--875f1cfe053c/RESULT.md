# Talagrand operator-cotype counterexamples at every finite exponent

## Result

For every sufficiently large integer \(n\), there are an \(n\)-dimensional real Banach space \(X_n\) and a contraction
\[
U_n:X_n\to \ell_\infty^n
\]
for which the same pair \((X_n,U_n)\) simultaneously separates Rademacher cotype from Gaussian cotype plus the \((q,1)\)-summing norm at every finite exponent \(2\le q<\infty\). More precisely, there are universal constants \(c,C>0\) such that
\[
 C_q^r(U_n)\ge c\,n^{1/q},
\]
and
\[
 \max\{C_q^g(U_n),\|U_n\|_{q,1}\}
 \le C\left(\frac{n}{\log(n+1)}\right)^{1/q}
\]
for every \(2\le q<\infty\). Hence
\[
\boxed{
\frac{C_q^r(U_n)}{\max\{C_q^g(U_n),\|U_n\|_{q,1}\}}
\ge c\,(\log(n+1))^{1/q}.}
\]
In particular, for every fixed finite \(q\ge2\), no constant depending only on \(q\) can bound \(C_q^r(U)\) by \(\max\{C_q^g(U),\|U\|_{q,1}\}\) for all operators \(U\).

This strengthens the current version of Wu's counterexample, which establishes the separation for \(q=2\) and dimensions \(n=2^k\). The argument below also removes the power-of-two restriction.

## Construction

Let \(H_n\) be the orthogonal discrete cosine transform matrix
\[
(H_n)_{0j}=n^{-1/2},\qquad
(H_n)_{rj}=\sqrt{\frac2n}\cos\frac{\pi r(j+1/2)}n
\quad(1\le r\le n-1,\ 0\le j\le n-1).
\]
Thus
\[
H_n^TH_n=I_n,
\qquad
\max_{r,j}|(H_n)_{rj}|\le \sqrt{\frac2n}.
\]
The orthogonality follows from the standard finite cosine orthogonality identities. Put
\[
s_n=\sqrt{2\log(2n)}
\]
and equip \(\mathbb R^n\) with
\[
\|x\|_{X_n}
 =\max\left\{\|x\|_\infty,\frac{\|H_nx\|_\infty}{s_n}\right\}.
\]
Let \(U_nx=x\) as a map from \(X_n\) to \(\ell_\infty^n\). This is a contraction.

The same construction may be viewed isometrically as the graph subspace
\[
J_nX_n=\{(x,H_nx/s_n):x\in\mathbb R^n\}\subset
\ell_\infty^n\oplus_\infty\ell_\infty^n=\ell_\infty^{2n}.
\]
Thus the failure occurs on explicit \(n\)-dimensional subspaces of a \(2n\)-dimensional \(\ell_\infty\) space, despite Talagrand's positive theorem for operators whose whole domain is \(\ell_\infty^N\).

## Rademacher lower bound

Apply the definition of \(C_q^r(U_n)\) to the standard basis \(e_1,\dots,e_n\). Since \(\|U_ne_i\|_\infty=1\), the numerator is \(n^{1/q}\). If \(\varepsilon\in\{\pm1\}^n\), then
\[
\|\varepsilon\|_{X_n}
=\max\left\{1,\frac{\|H_n\varepsilon\|_\infty}{s_n}\right\}.
\]
Every row of \(H_n\) has Euclidean norm one, so each coordinate of \(H_n\varepsilon\) is 1-subgaussian. The usual exponential-moment bound gives
\[
\mathbb E\|H_n\varepsilon\|_\infty\le \sqrt{2\log(2n)}=s_n.
\]
Consequently
\[
\mathbb E\|\varepsilon\|_{X_n}\le2,
\qquad
C_q^r(U_n)\ge \frac12 n^{1/q}.
\]

## Gaussian interpolation lemma

A reusable observation is the following. If \(U:X\to Y\) is a contraction and \(2\le q<\infty\), then
\[
C_q^g(U)
\le
\bigl(C_2^g(U)\bigr)^{2/q}
\left(\sqrt{\frac\pi2}\right)^{1-2/q}.
\]
Indeed, for a finite family \((x_i)\subset X\), write
\[
a_i=\|Ux_i\|,
\qquad
G=\mathbb E\left\|\sum_i g_ix_i\right\|.
\]
By definition,
\[
\|a\|_2\le C_2^g(U)G.
\]
For every fixed \(i\), conditional Jensen gives
\[
G\ge \mathbb E|g_i|\,\|x_i\|
\ge \sqrt{\frac2\pi}\,a_i,
\]
so \(\|a\|_\infty\le\sqrt{\pi/2}\,G\). Interpolating the sequence norms,
\[
\|a\|_q\le \|a\|_2^{2/q}\|a\|_\infty^{1-2/q},
\]
which proves the claim.

Wu uses the classical estimate
\[
C_2^g(I_{\ell_\infty^n})
\le C_0\sqrt{\frac{n}{\log(n+1)}}.
\]
Because \(\|x\|_\infty\le\|x\|_{X_n}\), the same upper bound holds for \(C_2^g(U_n)\). The interpolation lemma therefore yields, uniformly for all \(q\ge2\),
\[
C_q^g(U_n)
\le C\left(\frac{n}{\log(n+1)}\right)^{1/q},
\]
with a universal \(C\).

## The \((q,1)\)-summing estimate

Take finitely many \(x_i\in X_n\), write the vectors as the columns of
\[
A=(a_{ji}),\qquad C=H_nA=(c_{ri}),
\]
and define
\[
\alpha=\max_j\sum_i|a_{ji}|,
\qquad
\beta=\max_r\sum_i|c_{ri}|.
\]
Then
\[
D:=\max_{\eta_i=\pm1}
\left\|\sum_i\eta_ix_i\right\|_{X_n}
=\max\left\{\alpha,\frac\beta{s_n}\right\}.
\]
Let \(u_i=\|x_i\|_\infty\). We have \(u_i\le\alpha\). Since \(A=H_n^TC\) and \(|(H_n)_{rj}|\le\sqrt{2/n}\),
\[
u_i\le \sqrt{\frac2n}\sum_r|c_{ri}|.
\]
Therefore, for every \(q\ge2\),
\[
\sum_i u_i^q
\le \alpha^{q-1}\sum_i u_i
\le \sqrt{2n}\,\alpha^{q-1}\beta,
\]
and hence
\[
\left(\sum_i\|U_nx_i\|_\infty^q\right)^{1/q}
\le
2^{1/(2q)}n^{1/(2q)}s_n^{1/q}D.
\]
Thus
\[
\|U_n\|_{q,1}
\le
2^{1/(2q)}n^{1/(2q)}(2\log(2n))^{1/(2q)}.
\]
Since
\[
\frac{\sqrt{2n}\,s_n\,\log(n+1)}{n}
=O\left(\frac{(\log n)^{3/2}}{\sqrt n}\right)\to0,
\]
there is a universal \(N_0\) such that, for all \(n\ge N_0\) and all \(q\ge2\),
\[
\|U_n\|_{q,1}
\le C\left(\frac{n}{\log(n+1)}\right)^{1/q}
\]
with universal \(C\).

Combining the three estimates proves the stated simultaneous separation.

## Consequences and boundary

For every fixed \(2\le q<\infty\), the separation factor \((\log n)^{1/q}\) diverges. Hence the failure of Talagrand's proposed operator inequality is not confined to the endpoint \(q=2\): it occurs at every finite cotype exponent.

The construction also makes clear that Talagrand's positive estimate for operators defined on all of \(\ell_\infty^N\) is not uniformly inherited by subspaces. Here \(X_n\) is an explicit graph subspace of \(\ell_\infty^{2n}\), yet operators on \(X_n\) violate the proposed bound by an unbounded factor for each fixed finite \(q\).

The result does not address \(q=\infty\), where \((\log n)^{1/q}\) no longer diverges. It does not determine the optimal separation rate for \(q>2\); sharper estimates for \(C_q^g(I_{\ell_\infty^n})\) may improve the logarithmic exponent. It also does not claim that the interpolation lemma, DCT orthogonality, or the classical Gaussian-cotype estimate are new.

## Literature context and originality boundary

Talagrand's Research Problem 19.1.2 asks, for \(q\ge2\), whether a universal bound controls Rademacher cotype by the maximum of Gaussian cotype and the \((q,1)\)-summing norm. His Theorem 19.1.5 gives such a bound when the domain itself is \(\ell_\infty^N\). Wu's arXiv:2609.19731v1 gives a negative answer for \(q=2\) using a Walsh--Hadamard renorming in dimensions \(2^k\).

The contribution here is the simultaneous extension of that counterexample mechanism to every finite \(q\ge2\), with an explicit quantitative factor \((\log n)^{1/q}\), together with removal of the power-of-two restriction via a uniformly flat real orthogonal DCT matrix. To the best of our knowledge, these statements are not present in the current Wu preprint or in the older operator-cotype sources inspected.

## References

1. Xinglong Wu, *A Counterexample to Talagrand's Operator Cotype Problem*, arXiv:2609.19731v1 (2026). https://arxiv.org/abs/2609.19731
2. Michel Talagrand, *Upper and Lower Bounds for Stochastic Processes: Decomposition Theorems*, 2nd ed., Springer, 2021, Section 19.1, Research Problem 19.1.2 and Theorem 19.1.5. https://doi.org/10.1007/978-3-030-82595-9
3. S. Geiss and M. Junge, *Type and cotype with respect to arbitrary orthonormal systems*, J. Approx. Theory 82 (1995), 399--433. https://doi.org/10.1006/jath.1995.1088
4. M. Junge, *Comparing gaussian and Rademacher cotype for operators on the space of continuous functions*, Studia Math. 118 (1996), 101--115. https://doi.org/10.4064/sm-118-2-101-115
