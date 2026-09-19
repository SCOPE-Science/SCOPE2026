# Spectral-radius parity obstruction to ordered-product Lyapunov convergence

## Statement

Sornette, Saiprasad and Troude, *A New Route to Chaos through the Geometric Composition of Non-Normal Amplification* (arXiv:2609.18017v1), introduce for a smooth map with tangent Jacobians \(J_n\)
\[
h_L=\frac1L\Big\langle \log \rho(J_{n+L-1}\cdots J_n)\Big\rangle
\]
and state that \(h_L\) approaches the maximal Lyapunov exponent \(\lambda_1\) as \(L\) grows, with the leading eigenvector of the product aligning with the leading Oseledets direction.

That convergence statement is false without additional hypotheses, even for a smooth planar map and an exact period-two orbit. More strongly, there is a two-parameter family in which every one-step Jacobian is spectrally stable, the maximal Lyapunov exponent is positive, and \(h_L\) alternates forever between negative and positive values according to the parity of \(L\).

Let \(a>b\), \(s>0\), and define the smooth polynomial map
\[
F_{a,b,s}(x,y)=
\begin{pmatrix}
1-3x^2+2x^3+\left[-s+\left(s+\frac{e^{2a}}s\right)x\right]y\\[1mm]
sx+\left(-2s+\frac{e^{2b}}s\right)x^2+
\left(s-\frac{e^{2b}}s\right)x^3
\end{pmatrix}.
\]
Then
\[
p_0=(0,0),\qquad p_1=(1,0)
\]
form a period-two orbit. Writing
\[
A=DF(p_0)=s
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
B=DF(p_1)=
\begin{pmatrix}
0&e^{2a}/s\\
-e^{2b}/s&0
\end{pmatrix},
\]
the two-step monodromy is
\[
BA=\operatorname{diag}(e^{2a},e^{2b}).
\]
Hence the Lyapunov exponents per iterate on this orbit are exactly
\[
\lambda_1=a,\qquad \lambda_2=b.
\]

For the orbit average over the two phases, the source paper's statistic satisfies
\[
\boxed{h_{2k}=a\quad(k\ge1)}
\]
and
\[
\boxed{h_{2k+1}=\frac{a+b}{2}\quad(k\ge0).}
\]
Consequently, if
\[
a>0,\qquad a+b<0,\qquad e^{a+b}<s<1,
\]
then
\[
\rho(A)=s<1,\qquad
\rho(B)=\frac{e^{a+b}}s<1,
\]
while
\[
\lambda_1=a>0,
\]
and nevertheless
\[
h_{2k}>0,\qquad h_{2k+1}<0
\]
for every \(k\). There is no convergence of \(h_L\) to \(\lambda_1\), nor even an eventual stabilization of its sign.

## Exact proof of the parity law

The derivatives above give
\[
BA=M:=\operatorname{diag}(e^{2a},e^{2b}),
\qquad
AB=\operatorname{diag}(e^{2b},e^{2a}).
\]

For an even block \(L=2k\), the two phase-started products are \(M^k\) and \((AB)^k\). Since \(a>b\), both have spectral radius \(e^{2ak}\), so their phase average gives
\[
h_{2k}=\frac{1}{2k}\log(e^{2ak})=a.
\]

For an odd block \(L=2k+1\), the products are
\[
AM^k=
\begin{pmatrix}
0&-s e^{2bk}\\
s e^{2ak}&0
\end{pmatrix},
\]
and
\[
B(AB)^k=
\begin{pmatrix}
0&e^{2a(k+1)}/s\\
-e^{2b(k+1)}/s&0
\end{pmatrix}.
\]
Both have zero trace. Their spectral radii are therefore
\[
s\,e^{k(a+b)}
\quad\text{and}\quad
\frac{e^{(k+1)(a+b)}}s,
\]
respectively. Averaging the two logarithms cancels \(\log s\), leaving
\[
h_{2k+1}
=
\frac{1}{2k+1}\,
\frac{(2k+1)(a+b)}2
=
\frac{a+b}{2}.
\]

The same example also directly contradicts the stated eigenvector-alignment justification. Every odd product above has two eigenvalues of equal modulus (indeed a conjugate purely imaginary pair), although the Oseledets gap is \(a-b>0\). Thus an Oseledets singular-direction gap does not imply a leading-eigenvalue modulus gap for the finite product.

## A singular-value repair

Define instead
\[
g_L=
\frac1L\Big\langle
\log \sigma_{\max}(J_{n+L-1}\cdots J_n)
\Big\rangle.
\]
For the explicit period-two family above,
\[
\boxed{g_L=a=\lambda_1\quad\text{for every }L\ge1.}
\]
For even \(L\) this is immediate from the diagonal monodromy. For \(L=2k+1\), the largest singular values of the two phase-started products are
\[
s e^{2ak},
\qquad
\frac{e^{2a(k+1)}}s,
\]
whose averaged logarithm is exactly \(a(2k+1)\).

More generally, for an ergodic invariant measure satisfying the standard integrability condition on \(\log^+\|DF\|\), the integrated block quantity
\[
\frac1L\int \log \|DF^L(x)\|\,d\mu(x)
\]
converges to the top Lyapunov exponent by the subadditive ergodic theorem. This is the standard norm/singular-value route; there is no analogous unconditional convergence theorem obtained by simply replacing the norm by spectral radius.

## Periodic checkpoints can hide the problem

There is also an exact periodicity effect relevant to the numerical validation in arXiv:2609.18017v1. If an orbit has period \(p\) and the tangent maps are invertible, then for every \(m\ge1\),
\[
\boxed{h_{mp}=\lambda_1.}
\]
Indeed, each length-\(mp\) block is the \(m\)-th power of a \(p\)-step monodromy matrix based at the corresponding phase. The phase monodromies are conjugate, hence have the same spectral radius, and periodic-orbit Lyapunov growth is \((1/p)\log\rho(M_p)\).

The source paper reports a stable period-64 generalized-Hénon state and also reports agreement between \(h_{1024}\) and \(\lambda_1\) across its tested cases. For that period-64 state,
\[
1024=16\times64,
\]
so \(h_{1024}=\lambda_1\) is an exact periodic identity, not evidence by itself for convergence of the spectral-radius statistic at unrestricted horizons.

## Relation to known cocycle theory

The general distinction between norm growth and spectral-radius growth is established prior theory, not a novelty claim here. In particular, Nicolas Martinez Ramos, *Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles* (arXiv:2507.19624), summarizes the generalized Berger-Wang result that for a broad ergodic cocycle one has only
\[
\limsup_{n\to\infty}\frac1n\log\rho(A^{(n)}(x))=\lambda_1
\]
almost everywhere, and explicitly notes that the full limit can fail in general. That paper proves convergence only under additional structural hypotheses.

The contribution recorded here is therefore source-specific: it identifies that the unconditional convergence and eigenvector-alignment statements attached to the newly introduced \(h_L\) in arXiv:2609.18017v1 are not valid, gives an elementary smooth-map counterexample in the same non-normal dynamical setting with an exact parity law and sign reversal, and identifies a standard singular-value replacement with the correct Lyapunov-limit property.

## What remains valid

This correction does not invalidate the paper's finite-\(L\) numerical observations for its particular Hénon and Ikeda trajectories, nor its broader geometric point that ordering of non-normal tangent maps can strongly change asymptotic growth. The statistic \(h_L\) can still be useful empirically at selected finite horizons. What fails is the claim that increasing \(L\) generally makes this spectral-radius statistic converge to \(\lambda_1\), together with the proposed Oseledets-eigenvector justification.

## Reproducibility

`artifacts/verify_ordered_product.py` evaluates the explicit polynomial map and its Jacobians, checks the period-two monodromy, verifies that both one-step spectral radii are below one for the representative choice
\[
(a,b,s)=(0.2,-0.8,0.8),
\]
and confirms
\[
h_L=-0.3\ \text{for odd }L,\qquad
h_L=0.2\ \text{for even }L,\qquad
g_L=0.2\ \text{for every tested }L.
\]
The script was executed with Python 3.13.5 and NumPy 2.3.5; its clean numerical output is included in `artifacts/verification_output.txt`.

## References

1. D. Sornette, V. R. Saiprasad, V. Troude, *A New Route to Chaos through the Geometric Composition of Non-Normal Amplification*, arXiv:2609.18017v1 (2026). https://arxiv.org/abs/2609.18017
2. N. Martinez Ramos, *Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles*, arXiv:2507.19624 (2025; revised 2026). https://arxiv.org/abs/2507.19624
3. A. Avila, J. Bochi, *A formula with some applications to the theory of Lyapunov exponents*, Israel J. Math. 131 (2002), 125–137; arXiv:math/0104103. https://arxiv.org/abs/math/0104103
4. R. Aoun, C. Sert, *Law of large numbers for the spectral radius of random matrix products*, arXiv:1908.07469 (2019; published 2021). https://arxiv.org/abs/1908.07469
