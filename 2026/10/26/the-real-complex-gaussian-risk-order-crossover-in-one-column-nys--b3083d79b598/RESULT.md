# The real-complex Gaussian risk-order crossover in one-column Nyström

## Finding
For every real symmetric positive-definite \(2\times2\) matrix \(A\) with eigenvalues \(a>b>0\), form a rank-one exact-arithmetic Nyström approximation
\[
N(A,w)=\frac{Aww^*A}{w^*Aw},\qquad Z(w)=\|A-N(A,w)\|_*.
\]
Let \(w_{\mathbb R}\) have independent standard real-normal coordinates and let \(w_{\mathbb C}\) have independent standard circular complex-normal coordinates (each complex entry has unit squared-modulus expectation). Then, for every nondecreasing convex \(\varphi:[b,a]\to\mathbb R\),
\[
\mathbb E\varphi(Z(w_{\mathbb C}))\le\mathbb E\varphi(Z(w_{\mathbb R})).
\]
The inequality is strict for every strictly increasing convex \(\varphi\). Despite this increasing-convex risk ordering, there is no first-order stochastic dominance: the two continuous error laws have exactly the same median \(2ab/(a+b)\), and their quantile functions cross there. Their means are
\[
\mathbb E Z(w_{\mathbb R})=\sqrt{ab},\quad
\mathbb E Z(w_{\mathbb C})=\frac{ab\log(a/b)}{a-b},
\]
so the real-to-complex mean-error ratio diverges like \(\sqrt{a/b}/\log(a/b)\) as the spectral contrast grows. This is a distributional risk comparison at one vector over two different scalar fields, not an equal-arithmetic-cost algorithm comparison.

## Assumptions and scope
Let \(A\in\mathbb R^{2\times2}\) be positive definite, with distinct eigenvalues \(a>b>0\), considered either as a real symmetric or complex Hermitian matrix. The rank-one Nyström map is defined above for \(w\ne0\). In the real experiment, \(w_{\mathbb R}\in\mathbb R^2\) has independent \(N(0,1)\) entries. In the complex experiment, \(w_{\mathbb C}\in\mathbb C^2\) has coordinates \((X_j+iY_j)/\sqrt2\), where all four real-normal variables are independent. Both zero-vector events have probability zero. All norms are complex nuclear/Schatten-1 norms as appropriate. Eigenvalue-basis coordinates can be used because both probe laws are invariant under real orthogonal transformations.

For \(0<p<1\), the error quantiles (left-continuous inverses of their distribution functions) are exactly
\[
Q_{\mathbb R}(p)=\frac{ab}{b+(a-b)\cos^2(\pi p/2)},\qquad
Q_{\mathbb C}(p)=\frac{ab}{a-(a-b)p}.
\]
Therefore \(Q_{\mathbb R}(p)<Q_{\mathbb C}(p)\) for \(0<p<1/2\), equality holds at \(p=1/2\), and the ordering reverses for \(1/2<p<1\). Additionally,
\[
\mathbb E Z(w_{\mathbb R})^2=\frac{a+b}{2}\sqrt{ab},\qquad
\mathbb E Z(w_{\mathbb C})^2=ab.
\]
When \(a=b\), both residual laws instead degenerate at \(a\), by continuous extension.

## Proof
Diagonalize \(A=U\operatorname{diag}(a,b)U^T\). Since \(N=A^{1/2}P_{A^{1/2}w}A^{1/2}\), its residual is positive semidefinite of rank one. Hence its nuclear norm equals its trace. With \(u=U^Tw\), direct expansion yields
\[
Z= a+b-\frac{a^2|u_1|^2+b^2|u_2|^2}{a|u_1|^2+b|u_2|^2}
=\frac{ab(|u_1|^2+|u_2|^2)}{a|u_1|^2+b|u_2|^2}
=\frac{ab}{b+(a-b)T},\quad
T=\frac{|u_1|^2}{|u_1|^2+|u_2|^2}.
\]
For real Gaussian coordinates, independent squared-normal variables have gamma shape \(1/2\), and \(T_{\mathbb R}\sim\operatorname{Beta}(1/2,1/2)\) with \(F_{\mathbb R}(t)=(2/\pi)\arcsin\sqrt t\). For circular complex Gaussian coordinates, independent squared moduli are exponential, so \(T_{\mathbb C}\sim\operatorname{Beta}(1,1)\), uniform on \([0,1]\). Invert the strictly decreasing rational map from \(T\) to \(Z\) to obtain both stated quantiles. Its median is attained at \(T=1/2\).

We now prove a comparison stronger than the mean inequality. The arcsine CDF satisfies \(F_{\mathbb R}(t)>t\) for \(0<t<1/2\) and \(F_{\mathbb R}(t)<t\) for \(1/2<t<1\). One verification uses the density difference \(1/(\pi\sqrt{t(1-t)})-1\): it has exactly two symmetric roots in \((0,1)\), is positive near either endpoint, and is negative near the midpoint; symmetry and \(F_{\mathbb R}(1/2)=1/2\) establish the signs. Set \(H(s)=\mathbb E(T_{\mathbb R}-s)_+-\mathbb E(T_{\mathbb C}-s)_+\). Then \(H'(s)=F_{\mathbb R}(s)-s\), \(H(0)=H(1)=0\), and so \(H(s)>0\) for \(0<s<1\). Equal means \(\mathbb ET_{\mathbb R}=\mathbb ET_{\mathbb C}=1/2\) and the hinge-function representation of convex functions imply that \(T_{\mathbb R}\) dominates \(T_{\mathbb C}\) in convex order.

For every nondecreasing convex \(\varphi\), the function \(g(t)=\varphi(ab/[b+(a-b)t])\) is convex on \([0,1]\): the inner rational function is strictly convex and \(\varphi\) is convex nondecreasing. Convex ordering gives the desired inequality. If \(\varphi\) is strictly increasing, the strict convexity of the inner function forces strictness. The CDF crossing follows from the same explicit angular CDF signs, while \(Q_{\mathbb R}\) and \(Q_{\mathbb C}\) cross once at their common median.

Finally the real moments follow from \(T=\cos^2\theta\) with uniform \(\theta\) on \([0,\pi/2]\), using
\[
\frac2\pi\int_0^{\pi/2}\frac{d\theta}{a\cos^2\theta+b\sin^2\theta}=\frac1{\sqrt{ab}},\quad
\frac2\pi\int_0^{\pi/2}\frac{d\theta}{(a\cos^2\theta+b\sin^2\theta)^2}=\frac{a+b}{2(ab)^{3/2}}.
\]
The complex moments follow by integrating \((b+(a-b)t)^{-1}\) and \((b+(a-b)t)^{-2}\) over uniform \(t\in[0,1]\). Divide the means and let \(a/b\to\infty\), with \(b>0\) arbitrary, to obtain the stated asymptotic.

## Verification
Run `python3 verify.py` from this package. The standard-library-only verifier performs composite-trapezoid checks of the four moment formulas over four positive-eigenvalue pairs; checks 2,000 rotated complex-probe trace identities; compares both quantile functions; and verifies representative convex stop-loss and polynomial-risk inequalities. Observed run output: `VERIFY_OK: 4 quadrature pairs, 2000 matrix trace identities, convex-risk tests`. These computations test formulas and numerical code but do not establish the universal convex ordering; the proof does.

## Relationship to prior work
Balabanov, Beaupere, Grigori, and Lederer (arXiv:2210.11295v1, 20 October 2022; later PMLR 2023) give the standard Nyström map and compare practical structured and Gaussian sketches, without the present planar real-versus-complex residual-distribution and increasing-convex-order formulas. Tropp, Yurtsever, Udell, and Cevher (2017) explicitly formulate Gaussian Nyström sketches over both real and complex fields and establish larger-sketch expected approximation guarantees; their main relative-error theorem requires more sketch columns than the one-column case examined here. The beta/angular identities used in the proof are classical. The contribution claimed here is the field-dependent *complete scalar trace-error law and risk ordering* for the Nyström construction, not the underlying Nyström formula or the gamma-to-beta transformation.

## Limitations
Only a one-column exact-arithmetic rank-one approximation of a real symmetric positive-definite \(2\times2\) input is analyzed. The complex approximation may contain nonreal off-diagonal entries although its residual remains positive semidefinite Hermitian. One complex matrix-vector product is not generally equal in arithmetic cost to one real product; two independent real vectors already span a generic real two-dimensional problem. No practical cost superiority, finite-precision stability, larger-rank conclusion, or full stochastic dominance is claimed. An equivalent exact statistical field comparison outside the inspected numerical literature remains possible; novelty is best-knowledge, not independently certified.

## References
1. O. Balabanov, M. Beaupere, L. Grigori, V. Lederer, *Block subsampled randomized Hadamard transform for low-rank approximation on distributed architectures*, arXiv:2210.11295v1 (public 2022-10-20), https://arxiv.org/abs/2210.11295 ; ICML/PMLR 2023, https://proceedings.mlr.press/v202/balabanov23a/balabanov23a.pdf .
2. J. A. Tropp, A. Yurtsever, M. Udell, V. Cevher, *Fixed-Rank Approximation of a Positive-Semidefinite Matrix from Streaming Data*, NeurIPS 2017, https://proceedings.neurips.cc/paper_files/paper/2017/file/4558dbb6f6f8bb2e16d03b85bde76e2c-Paper.pdf .
