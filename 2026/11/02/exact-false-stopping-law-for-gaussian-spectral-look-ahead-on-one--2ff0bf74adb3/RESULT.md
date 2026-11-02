# Exact false-stopping law for Gaussian spectral look-ahead on one-spike residuals

## Finding

Consider the Gaussian spectral look-ahead statistic used in matrix-free randomized low-rank approximation. For a matrix with one singular value above a flat but highly populated tail, the statistic has an exact finite-dimensional beta distribution. This produces an explicit failure probability and a sharp sketch-size/power-iteration detection transition, even when the singular-value gap diverges.

For integers \(N\ge1\), \(1\le b\le N\), \(q\ge0\), and \(0<d<1\), set
\[
E=\operatorname{diag}(1,dI_N),\qquad
Y_q=(EE^{\mathsf T})^qE\Omega,\qquad
Q_q=\operatorname{orth}(Y_q),\qquad
L_q=\|Q_q^{\mathsf T}E\|_2,
\]
where \(\Omega\in\mathbb R^{(N+1)\times b}\) has independent standard real Gaussian entries. Let \(S\sim\operatorname{Beta}(b/2,(N+1-b)/2)\). Then, exactly,
\[
\boxed{L_q^2\ \overset{\mathrm d}=\ d^2+(1-d^2)\frac{S}{S+d^{4q+2}(1-S)}.}
\]
In particular, for every \(d<\tau<1\),
\[
\boxed{
\mathbb P(L_q\le\tau)
=I_{\xi}(b/2,(N+1-b)/2),\qquad
\xi=\frac{d^{4q+2}(\tau^2-d^2)}{1-\tau^2+d^{4q+2}(\tau^2-d^2)}.
}
\]
Here \(I_x(a,b)\) is the regularized incomplete beta function. The probability is zero for \(\tau\le d\) and one for \(\tau\ge1\). For a full \((N+1)\)-column Gaussian block, \(L_q=1\) almost surely.

For each fixed sketch width \(b\), fixed number \(q\) of power iterations, and \(d_N=N^{-\alpha}\) with \(\alpha>0\), the following phase diagram holds as \(N\to\infty\):
\[
\boxed{
L_q^2\ \xrightarrow{\mathbb P}\
\begin{cases}
0,&\alpha<1/(4q+2),\\
1,&\alpha>1/(4q+2),
\end{cases}
\quad\text{and}\quad
L_q^2\ \xrightarrow{\mathrm d}\ \frac{Z}{Z+1}
\quad\text{at }\alpha=1/(4q+2),\ Z\sim\chi_b^2.
}
\]
Thus, for any fixed \(\tau\in(0,1)\), a look-ahead test reporting \(L_q\le\tau\) passes with probability tending to one below this critical exponent and with probability tending to zero above it. In all cases, the true norm is \(\|E\|_2=1\) while the optimal rank-one approximation error is \(d_N\to0\). The fixed-block test can therefore almost surely misclassify an increasingly well-separated leading singular mode.

There is also a sharp growing-block boundary. If \(b_N\to\infty\), \(b_N=o(N)\), \(d_N\to0\), \(q\) is fixed, and
\[
\beta_N=\frac{b_N}{N d_N^{4q+2}}\longrightarrow\beta\in[0,\infty],
\]
then \(L_q^2\to\beta/(1+\beta)\) in probability (with the natural values at \(0\) and \(\infty\)). Consequently a fixed \(0<\tau<1\) gives asymptotic false-stop probability one if \(\beta<\tau^2/(1-\tau^2)\) and zero if \(\beta>\tau^2/(1-\tau^2)\). No universal assertion is made at equality.

As a finite example, \(N=10000\), \(b=16\), \(d=0.1\), \(q=0\), and \(\tau=0.5\) give
\[
\mathbb P(L_0\le0.5)=0.9897679877478459\ldots
\]
despite \(\|E\|_2=1\) and optimal rank-one spectral error \(0.1\). The exact beta formula permits direct calibration of the block width to a prescribed false-stop probability on this family.

## Assumptions and scope

Everything is over the real field and in exact arithmetic. All matrix norms denoted by \(\|\cdot\|_2\) are spectral norms. The singular values of \(E\) are one value equal to \(1\) and exactly \(N\) values equal to \(d\); the matrix is a possible current residual, not necessarily the original matrix in a multi-block implementation. Every Gaussian test column is independent of the residual. The exponent \(q=0\) corresponds to the unpowered spectral look-ahead block; \(q\ge1\) describes an optional power-filtered block, not an assertion about an implementation that omits power iteration. A common scalar normalization of \(\Omega\) does not alter \(Q_q\).

The event \(L_q\le\tau\) is called a *false stop* only when \(d<\tau<1\): it passes a spectral look-ahead comparison although the true residual norm is larger than the tolerance. This is a statement about the indicator, not a universal statement about the final error of any entire adaptive algorithm.

## Proof

**Step 1: reducing the spectral statistic to a single projection.** Since
\[
EE^{\mathsf T}=d^2I_{N+1}+(1-d^2)e_1e_1^{\mathsf T},
\]
and \(Q_q^{\mathsf T}Q_q=I_b\),
\[
(Q_q^{\mathsf T}E)(Q_q^{\mathsf T}E)^{\mathsf T}
= d^2I_b+(1-d^2)(Q_q^{\mathsf T}e_1)(Q_q^{\mathsf T}e_1)^{\mathsf T}.
\]
The rank-one summand has largest eigenvalue \(\|Q_q^{\mathsf T}e_1\|^2\), so
\[
L_q^2=d^2+(1-d^2)\|P_{\operatorname{range}(Y_q)}e_1\|^2.
\]

**Step 2: a deterministic one-axis subspace-scaling identity.** Let \(R\) be any \(b\)-dimensional subspace of \(\mathbb R^{N+1}\) and write \(S=\|P_Re_1\|^2\). For \(h>0\), let \(D_h=\operatorname{diag}(1,hI_N)\). Then
\[
\boxed{\|P_{D_hR}e_1\|^2=\frac{S}{S+h^2(1-S)}.}
\]
To see this when \(0<S<1\), take the unit vector \(v=P_Re_1/\sqrt S\in R\), so its first coordinate is \(\sqrt S\), and complete it to an orthonormal basis of \(R\) with vectors whose first coordinate is zero. Applying \(D_h\) preserves the orthogonality between \(D_hv\) and the remaining scaled basis vectors, because their first coordinates vanish and \(v\) is perpendicular to them. The projection of \(e_1\) onto \(D_hR\) is therefore just its projection onto \(D_hv\); its squared length is \(S/[S+h^2(1-S)]\). The endpoint cases follow directly. In our setting, \(Y_q=D_h\Omega\) with \(h=d^{2q+1}\).

**Step 3: the exact Haar beta law.** Standard Gaussian rotational invariance makes \(R=\operatorname{range}(\Omega)\) a Haar-uniform \(b\)-plane. If \(U\) is Haar orthogonal of order \(N+1\), then \(S\) is distributed as the sum of the first \(b\) squared entries of a uniform unit vector. Consequently
\[
S\ \overset{\mathrm d}=\frac{Z}{Z+V},\qquad
Z\sim\chi_b^2,\quad V\sim\chi_{N+1-b}^2,\quad Z\perp V,
\]
and hence \(S\sim\operatorname{Beta}(b/2,(N+1-b)/2)\). Combining the first two steps proves the claimed exact law and also the representation
\[
L_q^2\ \overset{\mathrm d}=d^2+(1-d^2)\frac{Z}{Z+d^{4q+2}V}.
\]
For \(d<\tau<1\), the event \(L_q^2\le\tau^2\) is equivalent to
\[
S\le\frac{d^{4q+2}(\tau^2-d^2)}{1-\tau^2+d^{4q+2}(\tau^2-d^2)},
\]
which proves the finite-dimensional CDF, including the limiting endpoint cases. If \(b=N+1\), the Gaussian square matrix is invertible almost surely, and its image is the full space, giving \(L_q=1\). Since adding columns enlarges the filtered subspace, the false-stop probability is nonincreasing in the sketch width, and its exact value at each integer width follows from the CDF.

**Step 4: sharp fixed-width phase diagram.** Keep \(b\) and \(q\) fixed, choose \(d_N=N^{-\alpha}\), and use the chi-square representation above with \(V_N\sim\chi_{N+1-b}^2\). We have \(V_N/N\to1\) in probability; hence the transformed projection converges to zero, \(Z/(Z+1)\), or one according as \(N d_N^{4q+2}\to\infty\), \(1\), or \(0\). Because \(d_N^2\to0\), the same three limits hold for \(L_q^2\). For fixed \(\tau\in(0,1)\), convergence in probability or continuity of the critical chi-square law determines the stated false-stop probabilities, with the critical probability explicitly
\[
\lim_{N\to\infty}\mathbb P(L_q\le\tau)
=\mathbb P\left(Z\le\frac{\tau^2}{1-\tau^2}\right)
\quad\text{at }\alpha=1/(4q+2).
\]

**Step 5: sharp growing-width phase diagram.** Let \(b_N\to\infty\), \(b_N=o(N)\), and \(d_N\to0\). In the chi-square representation, \(Z_N/b_N\to1\) and \(V_N/N\to1\) in probability by the chi-square variance formula. Therefore
\[
\frac{Z_N}{Z_N+d_N^{4q+2}V_N}
=\frac{Z_N/b_N}{Z_N/b_N+(d_N^{4q+2}N/b_N)(V_N/N)}
\xrightarrow{\mathbb P}\frac{\beta}{1+\beta},
\]
with the endpoint interpretations. Since \(d_N\to0\), this is also the limit of \(L_q^2\). Comparing the limiting value with \(\tau^2\) proves the two strict threshold regimes. At equality, the leading limit alone cannot determine the boundary probability, so no classification is claimed there.

## Verification

Run `python verify.py` with NumPy and SciPy. The checker independently compares the spectral norm of an explicitly QR-orthonormalized Gaussian block with both the rank-one projector identity and the transformed unfiltered Haar projector. It tests several dimensions and power counts, checks block-width monotonicity of the beta-CDF, and compares independent seeded chi-square experiments with the exact CDF. It also checks the displayed finite numerical example and the expected signs of finite-size phase trends.

These computations test implementation and signs only. No finite Monte Carlo sample proves an infinite-dimensional asymptotic. The proof rests on the deterministic subspace-scaling identity, the exact Haar projection law, and chi-square concentration.

## Relationship to prior work

Smith, Do and Chen introduced the spectral look-ahead block in their adaptive matrix-free QB method: its norm is used as a proxy for the previous residual's spectral norm (their Algorithm 5 and Theorem 4.3). Their theorem uses a high-probability factor depending on sketch parameters and does not assert the exact one-spike probability here. For \(q=0\), the present statistic matches that block-level estimator on the stated residual.

Halko, Martinsson and Tropp developed Gaussian range finding, probabilistic approximation-error estimates, and power schemes. Saibaba derived canonical-angle and singular-value bounds for randomized subspace iteration. Liu and Yu analyzed adaptive fixed-threshold rank revelation and explicitly highlighted the effects of heavy singular-value tails. Those works anticipate the qualitative dependence on the tail and the singular-value gap; none of the inspected statements supplies the present beta-CDF for the *spectral look-ahead decision* or its exact fixed-width and growing-width classification.

An exact random-section-radius law for one-spike ellipsoids, available in published mathematical research records, also uses a Haar beta projection. Its random functional is an ellipsoid section radius in a Haar subspace, rather than the norm of a two-sided filtered-and-projected matrix. The shared beta ingredient is acknowledged; the present claim concerns the additional nonlinear transfer to a specific adaptive spectral stopping test and its false-decision phase transition, not discovery of the Haar beta law itself.

## Limitations

The formula relies on one distinguished singular direction and exactly flat remaining singular values. It does not give the false-stop law for arbitrary spectra, non-Gaussian sketches, adaptively chosen sketches dependent on the current residual, finite-precision orthogonalization, or the output of an entire multi-block algorithm. The optional powered variant is a mathematical diagnostic and is not claimed to be part of the source's unpowered implementation. Previous canonical-angle analyses can predict qualitative sample/power scaling, and equivalent special-case probability formulas may exist under other terminology; exact scholarly priority needs independent checking.

## References

1. A. I. Smith, E. Do and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1, first posted 7 July 2026, Sections 4.1–4.2.
2. N. Halko, P.-G. Martinsson and J. A. Tropp, *Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions*, SIAM Review 53 (2011), 217–288; arXiv:0909.4061v2, Sections 4 and 10.
3. A. K. Saibaba, *Randomized Subspace Iteration: Analysis of Canonical Angles and Unitarily Invariant Norms*, arXiv:1804.02614, Sections 3 and 4.
4. Q. Liu and Y. Yu, *Efficient Adaptive Randomized Algorithms for Fixed-Threshold Low-Rank Matrix Approximation*, arXiv:2508.07553v1, 11 August 2025, Sections 1–3.
5. *Exact Random-Radius Law for One-Spike Ellipsoids in Every Codimension*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-random-radius-law-for-one-spike-ellipsoids-in-every-codime--e99f37d3b7ae, especially the rank-one compression proof.
