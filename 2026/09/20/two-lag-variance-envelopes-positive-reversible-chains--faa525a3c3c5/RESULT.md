# Sharp two-lag variance envelopes for positive reversible Markov chains

## Setup

Let \((X_t)_{t\in\mathbb Z}\) be a stationary reversible Markov chain with invariant law \(\pi\), and let its Markov operator \(P\) be positive semidefinite on \(L^2(\pi)\). Thus the spectrum relevant to centered observables is contained in \([0,1]\); lazy reversible chains are an important subclass.

For a centered nonzero observable \(g\in L^2_0(\pi)\), write
\[
\sigma^2=\langle g,g\rangle_\pi,
\qquad
r_k=\frac{\langle g,P^k g\rangle_\pi}{\sigma^2}\quad(k\ge0).
\]
By the spectral theorem there is a probability measure \(\nu\) on \([0,1]\) such that
\[
r_k=\int_0^1 \lambda^k\,\nu(d\lambda).
\]
Set
\[
\rho=r_1,\qquad q=r_2.
\]
Then necessarily
\[
0\le \rho\le1,\qquad \rho^2\le q\le\rho.
\]
The statements below concern the information contained in the exact pair \((r_1,r_2)\), not sampling error in empirical autocorrelations.

## 1. A sharp two-moment envelope

Assume \(0<\rho<1\), and define
\[
b=\frac q\rho,
\qquad
w_- = \frac{\rho^2}{q},
\]
\[
a=\frac{\rho-q}{1-\rho},
\qquad
d=1-2\rho+q,
\qquad
w_+=\frac{q-\rho^2}{d}.
\]
For every \(\phi\in C^3[0,1]\) with \(\phi'''\ge0\),
\[
(1-w_-)\phi(0)+w_-\phi(b)
\le \int\phi(\lambda)\,\nu(d\lambda)
\le (1-w_+)\phi(a)+w_+\phi(1).
\tag{1}
\]
Both bounds are sharp among probability measures on \([0,1]\) with first two moments \((\rho,q)\).

This is a two-moment specialization of classical truncated Hausdorff/Markov--Krein extremal theory; the general moment principle is not claimed as new here. A short direct proof is useful. For the lower bound, let \(Q_-\) be the quadratic Hermite interpolant to \(\phi\) at nodes \(0,b,b\). The interpolation remainder is
\[
\phi(x)-Q_-(x)=\frac{\phi'''(\xi_x)}6x(x-b)^2\ge0.
\]
For the upper bound, let \(Q_+\) interpolate at \(a,a,1\). Then
\[
\phi(x)-Q_+(x)=\frac{\phi'''(\eta_x)}6(x-a)^2(x-1)\le0.
\]
Expectations of the two quadratics depend only on \(1,\rho,q\), and evaluating them on the matching two-point measures gives (1).

When \(\phi'''>0\) in the interior, the equality supports are forced, apart from degenerate moment cases:
\[
\nu_-=(1-w_-)\delta_0+w_-\delta_b,
\qquad
\nu_+=(1-w_+)\delta_a+w_+\delta_1.
\tag{2}
\]

## 2. Every later autocorrelation has an explicit sharp interval

For every integer \(k\ge3\), apply (1) to \(\phi(x)=x^k\). Then
\[
\boxed{
\frac{q^{k-1}}{\rho^{k-2}}
\le r_k\le
\frac{(1-\rho)^2}{d}\left(\frac{\rho-q}{1-\rho}\right)^k
+\frac{q-\rho^2}{d}
}.
\tag{3}
\]
Both endpoints are sharp in the class of stationary positive reversible chains. In particular,
\[
\frac{q^2}{\rho}\le r_3\le q-\frac{(\rho-q)^2}{1-\rho}.
\]

A notable identification boundary occurs at \(q=\rho^2\). Then the spectral variance is zero, so \(\nu=\delta_\rho\) and
\[
\boxed{r_k=\rho^k\quad\text{for every }k\ge0.}
\tag{4}
\]
Thus equality in the elementary log-convexity constraint \(r_2\ge r_1^2\) determines the entire autocorrelation sequence for the observable.

## 3. Sharp finite-horizon sample-mean variance from two lags

For \(N\ge1\), define the normalized variance of the stationary sample mean
\[
V_N=
\frac{\operatorname{Var}\!\left(N^{-1}\sum_{t=0}^{N-1}g(X_t)\right)}{\sigma^2}.
\]
It has the spectral representation
\[
V_N=\int_0^1 H_N(\lambda)\,\nu(d\lambda),
\]
where
\[
H_N(x)=\frac1{N^2}\left[N+2\sum_{k=1}^{N-1}(N-k)x^k\right].
\tag{5}
\]
For \(x\ne1\), equivalently,
\[
H_N(x)=\frac1{N^2}\left[
N+\frac{2x\big((N-1)-Nx+x^N\big)}{(1-x)^2}
\right],
\qquad H_N(1)=1.
\]
For \(N\ge4\), \(H_N'''(x)>0\) on \([0,1]\), so (1) yields the sharp bounds
\[
\boxed{
L_N=(1-w_-)\frac1N+w_-H_N(b)
\le V_N\le
U_N=(1-w_+)H_N(a)+w_+.
}
\tag{6}
\]
For \(N\le3\), \(H_N\) has degree at most two, hence \(V_N\) is already determined exactly by \((\rho,q)\), and the two expressions in (6) coincide.

Consequently, if finite-horizon effective sample size is defined by \(\operatorname{ESS}_N=1/V_N\) after normalizing iid variance to \(1/N\), then the exact two lags give the reversed sharp interval \([1/U_N,1/L_N]\) for that normalization.

## 4. Long-run variance: a sharp lower bound but no finite upper bound

The normalized long-run variance, or integrated autocorrelation time in the extended sense, is
\[
\tau
=1+2\sum_{k\ge1}r_k
=\int_0^1\frac{1+\lambda}{1-\lambda}\,\nu(d\lambda)
\in[1,\infty].
\tag{7}
\]
For \(0<\rho<1\) and \(q<\rho\), applying the lower half of (1) to \(\phi(x)=(1+x)/(1-x)\), by monotone truncation if necessary, gives
\[
\boxed{
\tau\ge 1+\frac{2\rho^2}{\rho-q}.
}
\tag{8}
\]
The lower bound is attained by \(\nu_-\) in (2).

There is a sharp dichotomy.

- If \(q=\rho^2\), then (4) gives
  \[
  \tau=\frac{1+\rho}{1-\rho}.
  \]
- If \(q>\rho^2\), there is **no finite upper bound on \(\tau\)** determined by \((\rho,q)\), even after restricting to finite-state, irreducible, aperiodic, positive reversible chains.

For the second claim put \(v=q-\rho^2>0\). For any \(c<1\) sufficiently close to one, define
\[
u_c=\rho-\frac{v}{c-\rho},
\qquad
\omega_c=\frac{v}{(c-\rho)^2+v}.
\]
The two-point measure
\[
(1-\omega_c)\delta_{u_c}+\omega_c\delta_c
\tag{9}
\]
has first moment exactly \(\rho\) and second moment exactly \(q\). As \(c\uparrow1\), \(\omega_c\) tends to a positive limit while \((1+c)/(1-c)\to\infty\); hence \(\tau\to\infty\).

Thus exact knowledge of the first two positive-reversible autocorrelations can sharply certify a minimum long-run variance, but unless \(r_2=r_1^2\) it cannot rule out arbitrarily poor long-run effective sample size.

## 5. Finite-state realizability of the extremal spectral measures

The spectral measures above are not merely abstract moment constructions. For \(0\le\lambda<1\), consider the symmetric two-state transition kernel
\[
P_\lambda=\frac12
\begin{pmatrix}
1+\lambda&1-\lambda\\
1-\lambda&1+\lambda
\end{pmatrix}.
\]
It is finite-state, irreducible, aperiodic, reversible, and positive, with centered coordinate eigenfunction of eigenvalue \(\lambda\). The product of two such chains has orthogonal coordinate eigenfunctions. A normalized linear combination with squared coefficients \(w\) and \(1-w\) therefore has spectral measure \(w\delta_{\lambda_1}+(1-w)\delta_{\lambda_2}\).

This realizes the lower extremizer in (2) whenever \(q<\rho\). The upper measure in (2) is realized if nonergodic chains are allowed, using an eigenvalue at one. In the irreducible class, the exact-moment family (9) realizes the same \((\rho,q)\) and approaches the upper finite-horizon bound as \(c\uparrow1\). Hence for \(q>\rho^2\), \(U_N\) is the sharp irreducible supremum although the endpoint itself is not attained.

## 6. Worked example

Take
\[
\rho=\frac25,\qquad q=\frac15.
\]
Then the sharp lag-three interval is
\[
\frac1{10}\le r_3\le\frac2{15}.
\]
For \(N=10\),
\[
\frac{7297}{32000}
\le V_{10}\le
\frac{145709}{546750},
\]
i.e.
\[
0.22803125\le V_{10}\le0.2665002286\ldots.
\]
The corresponding reciprocal finite-horizon efficiencies lie between approximately \(3.75234\) and \(4.38536\). Yet the long-run quantity satisfies only
\[
\tau\ge\frac{13}{5},
\]
and has no finite upper bound at these same exact values of \(r_1,r_2\).

## Verification

`artifacts/verify_two_lag_envelopes.py` uses exact rational arithmetic to check the two canonical measures, their first two moments, the higher-lag endpoint formulas for several rational parameter pairs, the worked example, and exact-moment finite-state approximants whose long-run variance grows as their upper spectral atom approaches one. `artifacts/VERIFICATION.txt` records the verified outputs.

## Relation to prior work and originality

The spectral representation of reversible-chain autocovariances is classical. Kipnis--Varadhan developed the spectral framework for additive functionals of reversible Markov processes. Geyer's initial-sequence methodology exploits positivity, monotonicity and convexity properties of reversible-chain covariance combinations. Roberts--Rosenthal characterize variance-bounding reversible chains through spectral behavior. Berg--Song explicitly formulate reversible autocovariance sequences as compactly supported moment sequences and use that structure for shape-constrained estimation and asymptotic-variance estimation.

Classical Hausdorff and Markov--Krein moment theory already supplies general machinery for extremizing expectations under finitely many moment constraints. Accordingly, the generic two-moment interpolation lemma above is not claimed as a new moment theorem.

**To the best of our knowledge, the contribution here is the explicit positive-reversible-chain specialization:** the sharp closed-form envelope (3) for every later autocorrelation from exactly \((r_1,r_2)\); the sharp finite-horizon sample-mean variance interval (6); the identification boundary \(r_2=r_1^2\); and the dichotomy (8)--(9), showing that positive spectral variance permits arbitrarily large long-run variance at fixed first two autocorrelations even in finite-state irreducible chains. Searches across reversible-chain variance estimation, autocorrelation moment representations, effective sample size, truncated Hausdorff moments, and synonymous spectral formulations did not locate these explicit consequences. Because they are a concrete specialization of classical truncated moment machinery, an equivalent derivation in older moment or MCMC diagnostic literature remains the main originality risk.

## Limitations

The positivity assumption on \(P\) is essential for the support restriction \([0,1]\). General reversible chains may have negative spectrum, and the stated envelopes do not apply unchanged. The results concern one fixed observable \(g\), not a chain-wide worst case over all observables. They condition on exact population autocorrelations \((r_1,r_2)\), not noisy estimates. The absence of a finite upper bound concerns asymptotic variance when \(q>\rho^2\); every fixed finite horizon still has the sharp finite bound (6).

## References

1. F. Hausdorff, “Summationsmethoden und Momentfolgen. I,” *Mathematische Zeitschrift* 9 (1921), 74–109.
2. C. Kipnis and S. R. S. Varadhan, “Central limit theorem for additive functionals of reversible Markov processes and applications to simple exclusions,” *Communications in Mathematical Physics* 104 (1986), 1–19. https://doi.org/10.1007/BF01210789
3. C. J. Geyer, “Practical Markov Chain Monte Carlo,” *Statistical Science* 7 (1992), 473–483. https://doi.org/10.1214/ss/1177011137
4. G. O. Roberts and J. S. Rosenthal, “Variance bounding Markov chains,” *Annals of Applied Probability* 18 (2008), 1201–1214. https://doi.org/10.1214/07-AAP486
5. S. Berg and H. Song, “Efficient shape-constrained inference for the autocovariance sequence from a reversible Markov chain,” *Annals of Statistics* 51 (2023), 2440–2470. https://doi.org/10.1214/23-AOS2335
