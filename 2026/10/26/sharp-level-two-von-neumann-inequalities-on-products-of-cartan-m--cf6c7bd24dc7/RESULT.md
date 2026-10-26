# Sharp level-two von Neumann inequalities on products of Cartan matrix balls

## Finding

For every integer \(s\geq1\) and positive integers \(p_j,q_j\), consider the product of type-I Cartan matrix balls
\[
\Omega=\prod_{j=1}^{s}R_{p_j,q_j},\qquad
R_{p,q}=\{Z\in M_{p,q}(\mathbb C):\|Z\|_{\mathrm{op}}<1\}.
\]
Suppose the \(2\times2\) matrices \(T_{j,ab}\) commute jointly and, for every factor, their rectangular operator block \(Q_j(T)=[T_{j,ab}]_{a=1,\ldots,p_j;\,b=1,\ldots,q_j}\) satisfies \(\|Q_j(T)\|<1\). Then for **every scalar bounded holomorphic** \(f\in H^\infty(\Omega)\),
\[
\boxed{\|f(T)\|\leq\|f\|_{\infty,\Omega}.}
\]
The constant \(1\) is optimal and requires no bounded \(H^\infty\)-Gleason property for any factor. There is no bound on the number or rank of factors.

The ambient matrix size is sharp in the following universal sense: for every **single** type-I Cartan ball with \(pq\geq2\), there exist jointly commuting \(3\times3\) matrices in its strict block operator ball and a scalar polynomial \(P\) with \(\|P(T)\|>\sup_{Z\in R_{p,q}}|P(Z)|\). Thus size \(2\) is the largest universal contractive matrix size for each non-disc type-I Cartan ball. The size-\(3\) counterexample follows from the already published row-ball construction of Hartz–Richter–Shalit; it is not asserted to be new.

## Assumptions and scope

The operator norm in \(Q_j(T)\) acts from \(\mathbb C^{q_j}\otimes\mathbb C^2\) to \(\mathbb C^{p_j}\otimes\mathbb C^2\). Every coordinate matrix in every factor is assumed to commute with all other coordinates. The tuple has Taylor joint spectrum in \(\Omega\), by simultaneous triangularization and compression of strict block contractions, so its ordinary commuting holomorphic functional calculus is defined. All inequalities concern scalar-valued holomorphic functions and strict block contractions; the result does not assert complete spectral-set contractivity for matrix-valued test functions or estimates for arbitrary matrix sizes.

For \(B\in R_{p,q}\), write \(D_{B^*}=(I_p-BB^*)^{1/2}\) and \(D_B=(I_q-B^*B)^{1/2}\). The matrix-ball automorphism
\[
\Phi_B(Z)=D_{B^*}^{-1}(Z-B)(I_q-B^*Z)^{-1}D_B
\]
sends \(B\) to \(0\), maps \(R_{p,q}\) biholomorphically onto itself, and preserves strict contraction at every block-matrix level (with each scalar entry of \(B\) amplified by \(I_2\)). Indeed direct multiplication gives the exact defect identity
\[
I_p-\Phi_B(Z)\Phi_B(Z)^*=D_{B^*}(I_p-ZB^*)^{-1}(I_p-ZZ^*)(I_p-BZ^*)^{-1}D_{B^*}.
\]
The same identity holds after amplification, without a commutativity assumption on \(Z\). Its inverse is the corresponding matrix-ball automorphism carrying \(0\) to \(B\). This is also the standard liftable automorphism from the type-I Cartan-domain literature.

## Proof

**1. Simultaneous triangularization and functional calculus.** Choose one common orthonormal triangularizing basis for all commuting \(2\times2\) coordinates:
\[
T_\nu=\begin{pmatrix}\lambda_\nu&v_\nu\\0&\mu_\nu\end{pmatrix},
\]
where \(\nu\) ranges over all scalar coordinates. Compression of each block contraction gives \(\lambda,\mu\in\Omega\). If \(\lambda\ne\mu\), commutativity implies \((\lambda_\nu-\mu_\nu)v_\kappa=(\lambda_\kappa-\mu_\kappa)v_\nu\), so there is a single \(c\in\mathbb C\) with \(v_\nu=c(\lambda_\nu-\mu_\nu)\) for all \(\nu\). Consequently
\[
f(T)=\begin{pmatrix}a&c(a-b)\\0&b\end{pmatrix},\qquad a=f(\lambda),\quad b=f(\mu),
\]
for every \(f\) holomorphic near the joint spectrum. This follows first for polynomials and then from holomorphic functional calculus. If \(\lambda=\mu\), the same calculus instead gives \(f(T)=\begin{psmallmatrix}a&df_\lambda(v)\\0&a\end{psmallmatrix}\).

**2. Two distinct joint diagonal points.** Apply the amplified lift of \(\Phi_{\mu_j}\) to the \(j\)-th factor. Under the tensor-factor permutation exchanging the two \(\mathbb C^2\) basis components, the transformed rectangular block is
\[
\begin{pmatrix}U_j&cU_j\\0&0\end{pmatrix},\qquad U_j=\Phi_{\mu_j}(\lambda_j).
\]
Its norm is \(\sqrt{1+|c|^2}\,\|U_j\|\). The strict contraction assumption and the defect identity therefore give
\[
\rho:=\max_{1\leq j\leq s}\|U_j\|>0,
\qquad (1+|c|^2)\rho^2<1.
\]
The analytic disk \(h:\mathbb D\to\Omega\), defined componentwise by
\[
h(w)_j=\Phi_{\mu_j}^{-1}(wU_j/\rho),
\]
satisfies \(h(0)=\mu\) and \(h(\rho)=\lambda\). After normalizing \(\|f\|_\infty\leq1\), scalar Schwarz–Pick applied to \(f\circ h\) gives
\[
\delta(a,b):=\left|\frac{a-b}{1-\bar b a}\right|\leq\rho.
\]
For \(|a|,|b|<1\), a direct positivity test on the \(2\times2\) defect matrix shows that \(\begin{psmallmatrix}a&c(a-b)\\0&b\end{psmallmatrix}\) is a contraction precisely when
\[
|c|^2|a-b|^2\leq(1-|a|^2)(1-|b|^2).
\]
But \(|a-b|^2/[(1-|a|^2)(1-|b|^2)]=\delta(a,b)^2/[1-\delta(a,b)^2]\), and \((1+|c|^2)\rho^2<1\) implies \(|c|^2\rho^2/(1-\rho^2)<1\). Thus the contractivity criterion holds. If \(|a|=1\) or \(|b|=1\), the maximum-modulus principle makes \(f\) constant, and the conclusion is immediate.

**3. Repeated joint diagonal point.** Suppose \(\lambda=\mu\). Writing \(V_j=(v_{j,ab})\), the amplified automorphism transforms the \(j\)-th factor into the square-zero block \(\begin{psmallmatrix}0&W_j\\0&0\end{psmallmatrix}\) with \(W_j=(d\Phi_{\lambda_j})_{\lambda_j}(V_j)\). Hence \(\sigma:=\max_j\|W_j\|<1\). If \(\sigma=0\), the automorphism derivatives are invertible and every \(v_\nu=0\), so the claim is trivial. If \(\sigma>0\), the disk
\[
h(w)_j=\Phi_{\lambda_j}^{-1}(wW_j/\sigma)
\]
satisfies \(h(0)=\lambda\) and \(h'(0)=v/\sigma\). The scalar Schwarz–Pick derivative bound yields
\[
|df_\lambda(v)|\leq\sigma(1-|f(\lambda)|^2)\leq1-|f(\lambda)|^2.
\]
The rightmost inequality is exactly the contractivity condition for \(\begin{psmallmatrix}f(\lambda)&df_\lambda(v)\\0&f(\lambda)\end{psmallmatrix}\). Scaling removes the normalization \(\|f\|_\infty\leq1\). Constants give equality, proving sharpness.

**4. Size-three boundary.** Hartz–Richter–Shalit, Proposition 3.5, provide a commuting \(3\times3\) strict-or-nonstrict row-contractive pair \((A_1,A_2)\) and the polynomial \(P(z_1,z_2)=z_1^2+z_2^2\), with supremum \(1\) on the Euclidean two-ball and \(\|P(A_1,A_2)\|>1\). By continuity, multiplying both \(A_i\) by a scalar sufficiently close to \(1\) makes the row norm strictly below \(1\), retaining strict violation. If \(q\geq2\), put these two matrices in the first row of the \(p\times q\) block and zero elsewhere. If \(p\geq2\), put \(A_1^*,A_2^*\) in the first column and zero elsewhere; their column contraction condition is the adjoint of the row condition, and the real-coefficient polynomial has the same operator norm after adjunction. Its scalar supremum on the full Cartan ball remains \(1\). This proves the claimed sharp obstruction whenever \(pq\geq2\).

## Verification

The matrix-ball defect identity was checked directly by matrix multiplication and tested numerically on complex rectangular samples in dimensions \(2\times2\), \(2\times3\), and \(3\times2\). The accompanying `checks/cartans_two_level.py` repeats those tests with fixed seeds and additionally checks the triangular contraction identities. These are finite diagnostics; the general proof is the analytic argument above. The size-three boundary uses a specifically cited, published theorem and does not depend on numerical searches.

## Relationship to prior work

Kiri (2026, arXiv:2610.20355v1) establishes finite-dimensional estimates under an additional bounded Gleason hypothesis; for higher-rank type-I Cartan factors, its results are expressly conditional. Its unconditional product theorem applies only to row and column balls and yields a nonsharp factor depending on the number of coordinates. The theorem above is unconditional for all type-I products at matrix size two, with the exact constant one. Kiri's Proposition 1.13 establishes the relevant liftable automorphisms, but does not state or prove this sharp level-two conclusion.

Hartz–Richter–Shalit (2022, arXiv:2109.08550, Corollary 3.4) already prove the constant-one inequality for **single Euclidean row balls** at size two. Their Proposition 3.5 gives the size-three violation reused in step 4; neither result covers the present arbitrary products of genuine matrix balls. The one-dimensional disk case is classical. The proof uses the usual two-point Schwarz–Pick mechanism; possible earlier equivalent formulations in operator-domain interpolation remain an explicit historical-priority risk.

## Limitations

No claim is made for matrix-valued holomorphic functions, complete spectral sets, unrestricted higher operator dimensions, the optimal inequality above dimension two, or any particular Gleason division property. The three-dimensional obstruction is imported from earlier work. The two-dimensional inequality is proved for finite products and strict block contractions; nonstrict boundary tuples require further functional-calculus hypotheses. Independent scholarly priority review has not been performed, and older two-point interpolation theorems could cover part of the result.

## References

1. Ran Kiri, *Von Neumann Type Inequalities for NC Operator Balls*, arXiv:2610.20355v1, first public 2026-10-14, https://arxiv.org/html/2610.20355v1; especially Theorems A–C, Proposition 1.13 and Section 5.
2. Michael Hartz, Stefan Richter and Orr Moshe Shalit, *von Neumann's inequality for row contractive matrix tuples*, arXiv:2109.08550v3, https://arxiv.org/pdf/2109.08550; particularly Corollary 3.4 and Proposition 3.5; published in *Mathematische Zeitschrift* 301 (2022), 3877–3894.
3. Classical Schwarz–Pick lemma on the unit disk; used only in its two-point and derivative forms.
