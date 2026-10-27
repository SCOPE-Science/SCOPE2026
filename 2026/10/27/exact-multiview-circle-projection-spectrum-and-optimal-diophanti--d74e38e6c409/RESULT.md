# Exact multiview circle-projection spectrum and optimal Diophantine stability

## Finding

Let \(k\ge2\) be an integer and let \(\Phi=(\phi_1,\ldots,\phi_k)\) be arbitrary real viewing angles, interpreted modulo \(\pi\). From an \(L^2\)-density on the unit circle, observe its one-dimensional orthogonal projections along these directions, with each projected density measured relative to arcsine probability. The resulting observation operator \(M_\Phi\) has, on the two-dimensional Fourier-harmonic subspace of degree \(n\ge1\), **exact squared singular values**

\[
\lambda_\pm(n)=\frac{k\pm\left|\sum_{j=1}^k e^{2in\phi_j}\right|}{2}.
\]

Its constant block has squared singular value \(k\). Set

\[
\beta_j=\frac{\phi_j-\phi_1}{\pi}\quad(2\le j\le k),\qquad
\delta_n=\max_{2\le j\le k}\operatorname{dist}(n\beta_j,\mathbb Z).
\]

The least eigenvalue is quantitatively equivalent, with constants depending only on the number of views, to the simultaneous small divisor:

\[
\frac4k\,\delta_n^2\le\lambda_-(n)\le4\pi^2(k-1)\,\delta_n^2. \tag{1}
\]

In particular, the observations are injective on \(L^2\) if and only if at least one relative angle \(\beta_j\) is irrational. For any \(\tau\ge0\), the **exact equivalence**

\[
\exists c>0\ \forall f\in L^2(S^1):\quad
\|M_\Phi f\|_{\oplus L^2(\mathrm{arcsine})}\ge c\|f\|_{H^{-\tau}(S^1)}
\quad\Longleftrightarrow\quad
\inf_{n\ge1}n^\tau\delta_n>0 \tag{2}
\]

holds, with the Sobolev norm interpreted via Fourier coefficients. For injective finite-view configurations, no inequality (2) can hold with \(\tau<1/(k-1)\). The borderline loss \(\tau=1/(k-1)\) holds exactly for simultaneously badly approximable angular difference vectors. For every such configuration, every \(s>0\), and all \(f\in H^s(S^1)\),

\[
\|f\|_{L^2}\le C_{\Phi,s}
\|f\|_{H^s}^{1/(1+s(k-1))}
\|M_\Phi f\|^{s(k-1)/(1+s(k-1))}. \tag{3}
\]

The exponent \(s(k-1)/(1+s(k-1))\) on the observed data in (3) is optimal under a fixed positive \(H^s\)-bound: no larger uniform exponent is possible. Exact squared condition numbers for bandlimited data up to degree \(N\ge1\) are

\[
\operatorname{cond}(M_\Phi|_{\deg\le N})^2
=\frac{k}{\min_{1\le n\le N}\lambda_-(n)}
\]

when the denominator is positive (and infinity otherwise).

## Assumptions and scope

Identify \(S^1\) with \(\theta\in[0,2\pi)\) and equip it with \(d\theta/(2\pi)\). Complex-valued or real-valued \(L^2\)-densities are allowed. For a view at angle \(\phi\), push forward the measure \(f(\theta)d\theta/(2\pi)\) under \(\theta\mapsto x=\cos(\theta-\phi)\), obtaining a density \(q_\phi(x)\) with respect to

\[
\rho(dx)=\frac{dx}{\pi\sqrt{1-x^2}},\qquad -1<x<1.
\]

Define \(M_\Phi f=(q_{\phi_j})_{j=1}^k\), with the Hilbert direct-sum norm. On the circle use the orthonormal real trigonometric basis \(1,\sqrt2\cos(n\theta),\sqrt2\sin(n\theta)\); on the interval use \(1,\sqrt2 T_n(x)\), where \(T_n(\cos t)=\cos(nt)\). Both are orthonormal with the stated reference probabilities. Fourier-degree \(n\) receives Sobolev weight \((1+n^2)^{s/2}\). All assertions concern complete one-dimensional projected **measures**, equivalently restriction of the Fourier transform to the corresponding complete lines through the origin; they do not concern a finite number of Fourier samples, arbitrary off-circle measures, or projection noise in a different weighting.

## Proof

**1. Exact pushforward and block structure.** For \(0<t<\pi\), the two inverse images of \(x=\cos t\) are \(\phi+t\) and \(\phi-t\) modulo \(2\pi\). Changing variables on the two semicircles proves, first for bounded densities and then by \(L^2\)-approximation,

\[
q_\phi(\cos t)=\frac{f(\phi+t)+f(\phi-t)}2.
\]

For an arbitrary degree-\(n\) input \(f=a\sqrt2\cos(n\theta)+b\sqrt2\sin(n\theta)\), this becomes

\[
q_\phi(x)=\sqrt2\big(a\cos(n\phi)+b\sin(n\phi)\big)T_n(x).
\]

Consequently, orthogonal Fourier degrees do not mix under \(M_\Phi\), and the degree-\(n\) matrix is the \(k\times2\) real matrix whose \(j\)-th row is \((\cos(n\phi_j),\sin(n\phi_j))\). For constant input the image consists of \(k\) copies of the same constant.

**2. Exact spectrum.** The degree-\(n\) Gram matrix equals

\[
B_n^*B_n=\frac12
\begin{pmatrix}
k+\sum_j\cos(2n\phi_j)&\sum_j\sin(2n\phi_j)\\
\sum_j\sin(2n\phi_j)&k-\sum_j\cos(2n\phi_j)
\end{pmatrix}.
\]

Diagonalization yields the two stated eigenvalues. The identity

\[
k^2-\left|\sum_j e^{2in\phi_j}\right|^2
=4\sum_{i<j}\sin^2\big(n(\phi_i-\phi_j)\big)
\]

also gives the equivalent formulation

\[
\lambda_-(n)=
\frac{2\sum_{i<j}\sin^2(n(\phi_i-\phi_j))}
{k+\left|\sum_j e^{2in\phi_j}\right|}. \tag{4}
\]

This denominator always lies in \([k,2k]\). The inequalities \(2\operatorname{dist}(u,\mathbb Z)\le|\sin\pi u|\le\pi\operatorname{dist}(u,\mathbb Z)\) hold for all real \(u\). Keeping only pairs \((1,j)\) in (4) gives \(\lambda_-(n)\ge4\delta_n^2/k\). For any pair, the torus distance between \(n\beta_i\) and \(n\beta_j\) is at most \(2\delta_n\). Bounding all \(k(k-1)/2\) pairs in (4) from above proves the other half of (1).

**3. Injectivity and bandlimited conditioning.** The two degree-\(n\) columns become linearly dependent precisely when all \(e^{2in\phi_j}\) coincide, equivalently when \(n\beta_j\in\mathbb Z\) for every \(j\ge2\). Such an \(n\) exists if and only if every \(\beta_j\) is rational. If at least one is irrational, all \(\lambda_-(n)>0\), so Parseval forces a density with vanishing observations to be zero. The largest singular value on any degree-bounded space is exactly \(\sqrt k\) (already attained by constants); the smallest is the square root of the smallest \(\lambda_-\) among degrees one through \(N\), giving the condition-number formula.

**4. Exact Sobolev criterion.** On the degree-\(n\) subspace the optimal lower squared observation bound is \(\lambda_-(n)\). Thus a lower inequality with \(H^{-\tau}\) is equivalent to a positive uniform lower bound for \(\lambda_-(n)(1+n^2)^\tau\) for all \(n\ge1\) (the constant mode has eigenvalue \(k\)). By (1), and \(n^2\le1+n^2\le2n^2\) for \(n\ge1\), this is equivalent to the right side of (2). The equivalence includes a failure of injectivity, for which both sides fail.

**5. Optimal arithmetic loss.** Put \(d=k-1\). Dirichlet's simultaneous approximation theorem gives, for every integer \(Q\ge1\), a positive integer \(n\le Q^d\) with \(\delta_n\le1/Q\). If at least one \(\beta_j\) is irrational, such integers are unbounded as \(Q\to\infty\). Along an unbounded sequence, \(\delta_n\le n^{-1/d}\). Therefore \(n^\tau\delta_n\to0\) along a subsequence for every \(\tau<1/d\), ruling out (2). At \(\tau=1/d\), (2) is equivalent **by definition** to simultaneous bad approximability \(\inf_{n\ge1}n^{1/d}\delta_n>0\). This class is nonempty in every dimension by classical simultaneous Diophantine approximation; no special algebraic example in higher dimension is required for the claim.

**6. Optimal conditional Hölder stability.** Under bad approximability, (2) with \(\tau=1/d\) gives \(\|f\|_{H^{-\tau}}\le C\|M_\Phi f\|\). Fourier-sequence Hölder interpolation yields

\[
\|f\|_{L^2}
\le\|f\|_{H^{-\tau}}^{s/(s+\tau)}
\|f\|_{H^s}^{\tau/(s+\tau)},
\]

which is (3). For sharpness, take an unbounded Dirichlet subsequence \(n_\ell\) from step 5 and a unit eigenvector \(u_\ell\) corresponding to \(\lambda_-(n_\ell)\). Rescale the corresponding unit \(L^2\) harmonic to \(f_\ell=(1+n_\ell^2)^{-s/2}u_\ell\). Then \(\|f_\ell\|_{H^s}=1\), \(\|f_\ell\|_{L^2}\asymp n_\ell^{-s}\), and \(\|M_\Phi f_\ell\|\le C n_\ell^{-(s+1/d)}\). Any Hölder exponent strictly exceeding \(s/(s+1/d)\) contradicts these inequalities as \(\ell\to\infty\). All limits and inequalities are analytic; no finite-frequency experiment is used to prove them.

## Verification

A standalone numerical checker (`checker.py`, NumPy) directly assembled the projection matrices and verified their eigenvalues against the exact phasor formula on \(450\) frequency/view configurations; maximum absolute eigenvalue discrepancy was \(8.882\times10^{-16}\). It also verified the two bounds in (1), compared direct arcsine-coordinate integrals of finite trigonometric inputs against the blockwise energy identity (error \(2.220\times10^{-16}\)), checked five exact rational-angle rank failures, and inspected the record denominator sequence for a quadratic irrational. This is a finite sanity check, not a substitute for the infinite approximation or interpolation arguments. Run `python checker.py` with NumPy installed to reproduce its `CHECKER_OUTPUT.txt`.

## Relationship to prior work

Hedenmalm and Montes-Rodríguez introduced Heisenberg uniqueness pairs in the setting of Fourier transforms of singularly supported measures (2011). Lev and Sjölin analyzed the circle/two-line uniqueness problem (2011); the later treatment of Gröchenig and Jaming (2016) explicitly recalls the irrational-angle uniqueness criterion for the circle. Fernández-Bertolín, Gröchenig, and Jaming (2017 preprint, inspected in its full openly accessible version) study instability of recovering harmonic solutions from two lines: their Proposition 3.7 derives a two-direction determinant containing \(\sin(n(\phi_1-\phi_2))\), and their accompanying discussion invokes simultaneous approximation for arbitrarily many lines. That is closely related motivation and a qualitative two-view obstruction. The present claim is the **exact entire singular spectrum of arcsine-normalized circle pushforwards for any finite number of views**, together with the necessary-and-sufficient Sobolev loss criterion, the sharp all-\(k\) exponent \(1/(k-1)\), and sharp conditional Hölder exponent. These latter conclusions are not stated in the inspected portions of the cited works. They concern a different normed observation operator than the unweighted harmonic Dirichlet traces in the 2017 instability example. Existing general Fourier-frame or inverse-problem literature may contain an equivalent derivation despite different terminology; independent priority verification remains to be done.

## Limitations

The projective angular reference measure, angular Sobolev normalization, and complexification are fixed explicitly; different noise norms lead to different singular-value normalizations. The all-view formula does not extend unchanged to measures away from the circle or to incomplete Fourier-line sampling. The optimal \(1/(k-1)\) derivative loss is attained only for simultaneously badly approximable direction vectors; arbitrary irrational configurations may require greater loss or admit no finite-order Sobolev inequality. No closed-form optimal lower stability constant is asserted beyond the exact discrete eigenvalue sequence. This manuscript provides a self-review, not independent mathematical or publication-priority certification.

## References

1. H. Hedenmalm and A. Montes-Rodríguez, *Heisenberg uniqueness pairs and the Klein-Gordon equation*, Annals of Mathematics 173 (2011), 1507–1527. https://annals.math.princeton.edu/2011/173-3/p06. Published online 2011-05-01; MSC includes 42B10.
2. N. Lev, *Uniqueness theorems for Fourier transforms*, Bulletin des Sciences Mathématiques 135 (2011), 134–140. DOI: 10.1016/j.bulsci.2010.12.002. Circle HUP source; full text not independently inspected.
3. P. Sjölin, *Heisenberg uniqueness pairs and a theorem of Beurling and Malliavin*, Bulletin des Sciences Mathématiques 135 (2011), 125–133. DOI: 10.1016/j.bulsci.2010.12.004. Circle HUP source; full text not independently inspected.
4. K. Gröchenig and P. Jaming, *The Cramér–Wold theorem on quadratic surfaces and Heisenberg uniqueness pairs*, arXiv:1608.06738 (first posted 2016-08-24). https://arxiv.org/pdf/1608.06738.
5. A. Fernández-Bertolín, K. Gröchenig, and P. Jaming, *From Heisenberg uniqueness pairs to properties of the Helmholtz and Laplace equations*, arXiv:1711.05520 (first posted 2017-11-15); especially Proposition 3.7 and its subsequent discussion. https://arxiv.org/pdf/1711.05520.
6. Classical Dirichlet simultaneous approximation theorem; standard Fourier–Sobolev interpolation and classical existence of badly approximable vectors.
