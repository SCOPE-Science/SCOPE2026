# Sharp moment thresholds for Gaussian-noisy, norm-weighted Kaczmarz projections

## Finding

Consider a row-action method whose coefficient rows are freshly observed with independent additive Gaussian errors at each iteration. Fix integers \(m,d\ge1\), variance \(\sigma^2>0\), deterministic means \(\mu_1,\ldots,\mu_m\in\mathbb R^d\), a nonzero right-hand side \(b\in\mathbb R^m\), and a sampling exponent \(\beta\ge0\). At every iteration independently draw \(a_i\sim N(\mu_i,\sigma^2 I_d)\), choose a row \(I\) with probability \(\|a_i\|^\beta/\sum_j\|a_j\|^\beta\), and project the current iterate \(x\) onto \(a_I^{\mathsf T}z=b_I\):

\[
x^+=x+\frac{b_I-a_I^{\mathsf T}x}{\|a_I\|^2}a_I.
\]

Define the critical moment exponent

\[
q_\star=\min\{md,\ d+\beta\}.
\]

**Exact finite-time and equilibrium classification.** For every deterministic initial \(x_0\in\mathbb R^d\), every integer \(k\ge1\), and every \(q>0\),

\[
\mathbb E\|x_k\|^q<\infty\quad\Longleftrightarrow\quad q<q_\star.
\]

The Markov chain has a **unique invariant probability law** \(\pi\). It satisfies

\[
\int\|x\|^q\,\pi(dx)<\infty\quad\Longleftrightarrow\quad q<q_\star.
\]

The critical endpoint \(q=q_\star\) always diverges. Thus the classical squared-row-norm choice \(\beta=2\) restores finite expected squared error exactly when \(md>2\), whereas uniform row choice \(\beta=0\) requires \(d>2\), irrespective of how many rows are offered. Nevertheless no choice of \(\beta\) can restore moments of order \(q\ge md\): all candidate rows can be simultaneously almost zero.

For centered Gaussian rows \(\mu_i=0\) and the classical choice \(\beta=2\), the **entire one-step moment spectrum** is explicit. For \(0<q<\min\{md,d+2\}\), starting at zero,

\[
\mathbb E\|x_1\|^q=
\frac{\sum_{i=1}^m|b_i|^q}{(2\sigma^2)^{q/2}}
\frac{\Gamma((md-q)/2)\,\Gamma((d+2-q)/2)}{\Gamma(d/2)\,\Gamma((md+2-q)/2)}.
\]

When \(md>2\), for **every** deterministic \(x_0\) and integer \(k\ge0\), the expected squared norm has the exact evolution

\[
\mathbb E\|x_k\|^2=\left(1-\frac1d\right)^k\|x_0\|^2+
\frac{d\|b\|^2}{\sigma^2(md-2)}
\left[1-\left(1-\frac1d\right)^k\right].
\]

In particular, the invariant squared-norm floor is \(d\|b\|^2/[\sigma^2(md-2)]\). For example, \(d=1,m=3,\beta=2\) gives finite second moments but infinite third moments, while uniform sampling has infinite second moments for every \(m\) when \(d=1\).

## Assumptions and scope

The rows are independently redrawn **at each iteration**, including all nonselected candidate rows. This online coefficient-noise regime is distinct from drawing one noisy matrix and reusing it throughout a conventional Kaczmarz solve. The right-hand side is fixed and nonzero; there is no coupling between \(b\) and the refreshed coefficient noise. Each \(a_i\) has a full-dimensional Gaussian distribution with strictly positive variance. The sampling distribution is computed from the same freshly observed rows and is normalized jointly over all \(m\) candidates. For \(\beta=0\), sampling is uniform. Zero-length sampled rows have probability zero and may be ignored.

The result classifies moments of the numerical iterates, **not** their convergence to a prescribed deterministic solution. In the centered illustration, the row observations do not encode a fixed nonzero ground-truth coefficient matrix; their value is to expose the exact stochastic error floor.

## Proof

**1. The affine projection and the singular innovation.** Put \(u=a_I/\|a_I\|\), \(B=I_d-uu^{\mathsf T}\), and \(V=b_Iu/\|a_I\|\). Then \(x^+=Bx+V\), \(\|B\|\le1\), and \(BV=0\). Conditional on all sampled candidate rows,

\[
\mathbb E(\|V\|^q\mid a_1,\ldots,a_m)
=\frac{\sum_i |b_i|^q\|a_i\|^{\beta-q}}{\sum_j\|a_j\|^\beta}.
\]

Since some \(b_i\ne0\), positivity shows that integrability is equivalent to integrability of one summand indexed by such an \(i\).

**2. Exact integrability of the innovation.** Write \(r_j=\|a_j\|\). The independent radius densities have the form \(f_j(r)=r^{d-1}h_j(r)\), where \(h_j\) is positive and bounded above and below on each compact radius interval including zero; the Gaussian tails control the large-radius region. For \(m=1\), the denominator cancels and \(\mathbb E\|V\|^q<\infty\) exactly for \(q<d\), equal to \(q<q_\star\).

Let \(m\ge2\). To study the simultaneous-origin singularity, set \(s=\max_jr_j\), and on each of the \(m\) sectors where one particular radius is maximal, write \(r_j=st_j\), with one \(t_j=1\) and every other \(t_j\in[0,1]\). The change of variables, including radial densities, contributes \(s^{md-1}\) times factors \(t_j^{d-1}\). The summand for selected row \(i\) becomes

\[
s^{-q}\frac{t_i^{\beta-q}}{\sum_j t_j^\beta}.
\]

Because at least one \(t_j=1\), its denominator lies between \(1\) and \(m\). The radial integral near zero is finite exactly when \(q<md\), while its angular integral near a vanishing nonmaximal chosen radius is finite exactly when \(q<d+\beta\). If the selected radius is maximal, its angular numerator equals one and creates no additional singularity. The remaining Gaussian-tail region is integrable subject to the same selected-row local condition. Thus both strict inequalities suffice.

Necessity of \(q<d+\beta\) follows by holding all other radii in \([1,2]\) and sending the chosen \(r_i\) to zero: the integral has a positive multiple of \(\int_0^\epsilon r^{d+\beta-q-1}\,dr\). Necessity of \(q<md\) follows by restricting all radii to comparable values in \([s,2s]\) as \(s\downarrow0\): each dyadic shell contributes a positive multiple of \(s^{md-q}\). This also proves divergence at both equality boundaries. Consequently

\[
\mathbb E\|V\|^q<\infty\quad\Longleftrightarrow\quad 0<q<q_\star.
\]

**3. Every positive finite time.** If \(q<q_\star\), the inequality \(\|Bx+V\|\le\|x\|+\|V\|\), with the standard \(L^q\) triangle inequality for \(q\ge1\) and subadditivity of \(t^q\) for \(q\in(0,1)\), gives finite \(q\)-moment by induction from deterministic \(x_0\). Conversely, for any almost surely finite preceding state \(x\), independent of the refreshed rows, choose \(M<\infty\) with \(\Pr(\|x\|\le M)>0\). On this event \(\|Bx+V\|\ge(\|V\|-M)_+\). The innovation has infinite \(q\)-moment for \(q\ge q_\star\), even after subtracting a fixed constant. Independence therefore forces the updated \(q\)-moment to be infinite for every positive iteration.

**4. Unique invariant law.** If \(d=1\), \(B=0\) almost surely; each step completely refreshes the iterate to \(V\). Its law is the unique invariant law and has the stated moment spectrum. For \(d\ge2\), the selected unit direction has full support on the sphere because each Gaussian row density is strictly positive and its weight is positive away from zero. For every \(q>0\), the continuous function

\[
F_q(v)=\mathbb E\bigl\|(I_d-uu^{\mathsf T})v\bigr\|^q,
\qquad\|v\|=1,
\]

is strictly less than one: with positive probability the chosen direction is not orthogonal to \(v\). Compactness of the sphere yields \(\rho_q=\max_{\|v\|=1}F_q(v)<1\). In particular, since \(q_\star\ge2\) for \(d\ge2\), \(\mathbb E\|V\|<\infty\). Coupling two chains by the same fresh rows and index contracts their expected distance by \(\rho_1\). The transition kernel is therefore a strict contraction in the complete Wasserstein-one space of laws with finite first moment, giving one invariant law there. Any invariant probability law is the same: take its coupling with the finite-first-moment invariant law using identical innovations; the difference follows products of independent projections and tends to zero in probability by the \(\rho_1\)-contraction for fixed initial displacement, even when that displacement has no first moment (truncate it first). This also yields weak convergence from every starting state.

For \(q<q_\star\), \(\mathbb E\|Bx\|^q\le\rho_q\|x\|^q\). When \(q\ge1\), Minkowski bounds \(\|x_{k+1}\|_{L^q}\le\rho_q^{1/q}\|x_k\|_{L^q}+\|V\|_{L^q}\); when \(q<1\), the corresponding subadditive moment bound applies. Thus the chain started from zero has uniformly bounded \(q\)-moments. Weak convergence and lower semicontinuity imply that the invariant law has finite \(q\)-moment. If an invariant random state \(X\) had finite \(q\)-moment for \(q\ge q_\star\), independently drawing a new innovation and setting \(X^+=BX+V\) would also give a finite-\(q\)-moment \(X^+\), contradicting \(\|V\|\le\|X^+\|+\|X\|\). This proves the claimed equivalence.

**5. Exact centered Gaussian formulas for \(\beta=2\).** Now \(\mu_i=0\). Put \(Y_i=\|a_i\|^2/(2\sigma^2)\), which are independent \(\operatorname{Gamma}(d/2,1)\). Then \(Y=\sum_jY_j\sim\operatorname{Gamma}(md/2,1)\), and \(W_i=Y_i/Y\) is independent of \(Y\), with marginal \(\operatorname{Beta}(d/2,(m-1)d/2)\) for \(m\ge2\); when \(m=1\), \(W_1=1\). The exact \(q\)-moment factorizes as

\[
\mathbb E\|x_1\|^q=(2\sigma^2)^{-q/2}\sum_i|b_i|^q\mathbb E[Y^{-q/2}]\mathbb E[W_i^{1-q/2}],
\]

which gives the stated gamma-function expression. The factors require \(q<md\) and, for \(m\ge2\), \(q<d+2\); for \(m=1\), cancellation gives the correct \(q<d\) condition. With \(q=2\), \(\mathbb E\|V\|^2=\|b\|^2/[\sigma^2(md-2)]\). Rotational symmetry makes \(u\) uniform on the sphere, hence \(\mathbb E[B]= (1-1/d)I_d\). The exact pathwise orthogonality \(Bx\perp V\) gives

\[
\mathbb E(\|x^+\|^2\mid x)=\left(1-\frac1d\right)\|x\|^2+\frac{\|b\|^2}{\sigma^2(md-2)}.
\]

Solving this scalar recurrence proves the announced finite-time identity and stationary floor.

## Verification

The standalone program `verify.py` checks the gamma-ratio reduction at \(q=2\), the moment-boundary classifications in multiple dimensions, and independently simulates the centered Gaussian process to compare the analytic one-step and invariant second moments. All divergence, all-dimension and invariant-law conclusions above are proved analytically, not inferred from finite simulations. Run with `python verify.py` after installing the dependency in `requirements.txt`.

## Relationship to prior work

Bergou, Boucherouite, Dutta, Li, and Ma (arXiv:2308.16904, first version 31 August 2023) analyze randomized Kaczmarz with noise in both the coefficient matrix and the right-hand side. Their central bounds condition on a perturbed coefficient matrix and concern error convergence and noise horizons; the present result treats **fresh independent Gaussian coefficient observations and unconditional moment existence at every order**, a different question and noise protocol. The recurrence is the same projection primitive, not a claim about failure of their fixed-data theorem.

Needell, Srebro, and Ward (arXiv:1310.5715) study importance sampling and convergence of Kaczmarz/SGD on fixed row systems. Classical norm-squared sampling is prior work. Their convergence-rate and residual tradeoffs do not imply the sharp singular-integrability cutoff for Gaussian-resampled rows. Anderson, Collins, Haddock, Lok, and Rebrova (arXiv:2511.20877) study higher moments and concentration for random iterative methods, particularly fixed consistent linear systems with homogeneous error recurrences. Their moment bounds do not cover the affine innovations with denominator singularities classified here. The gamma/Dirichlet distributions and contraction-coupling arguments are classical ingredients, not claimed as inventions.

## Limitations

The sharp exponent assumes full-dimensional, nondegenerate Gaussian coefficient noise, fresh rows at every iteration, and nonzero fixed \(b\). If \(b=0\), the singular innovation disappears and all moments are finite for deterministic starting states. Bounded or lower-truncated row norms also eliminate the claimed singularities. We do not claim optimality of norm-power sampling for statistical accuracy, convergence to a true noiseless solution, corresponding statements for reusing one frozen noisy matrix, or a universal tail constant. The mathematical priority assessment remains provisional pending independent literature audit.

## References

1. E. H. Bergou, S. Boucherouite, A. Dutta, X. Li, and A. Ma, *A Note on Randomized Kaczmarz Algorithm for Solving Doubly-Noisy Linear Systems*, arXiv:2308.16904 (first submitted 2023-08-31), https://arxiv.org/abs/2308.16904 .
2. D. Needell, N. Srebro, and R. Ward, *Stochastic Gradient Descent, Weighted Sampling, and the Randomized Kaczmarz Algorithm*, arXiv:1310.5715 (2013), https://arxiv.org/abs/1310.5715 .
3. T. Anderson, M. Collins, J. Haddock, J. Lok, and E. Rebrova, *Beyond Expectation: Concentration Inequalities for Randomized Iterative Methods*, arXiv:2511.20877 (2025), https://arxiv.org/abs/2511.20877 .
4. J. Lok and E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889 (2023), https://arxiv.org/abs/2309.04889 .
