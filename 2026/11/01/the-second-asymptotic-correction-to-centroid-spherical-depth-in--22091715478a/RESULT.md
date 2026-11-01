# The second asymptotic correction to centroid spherical depth in regular simplices

## Finding

Let \(S_d\) be a nondegenerate regular Euclidean \(d\)-simplex, \(d\ge2\), with centroid \(c\). Let \(X,Y\) be independent uniform-volume points in \(S_d\); let \(B[X,Y]\) denote the closed ball with diameter \(XY\). Set \(m=d+1\), and write
\[
p_d=\mathbb P\big(c\in B[X,Y]\big).
\]
Then, as \(d\to\infty\),
\[
\boxed{\displaystyle
p_d=\frac12+\frac1{\sqrt{2\pi}}\left(\frac2{3\sqrt m}-\frac{4883}{270m^{3/2}}\right)+o(m^{-3/2}).}
\]
In particular the deviation from one half has a strictly positive leading coefficient, whereas its next nonzero coefficient is negative. The full coefficient is specific to the simplex-volume law; it is not an approximation inferred from a finite-dimensional numerical experiment.

## Assumptions and scope

All probabilities use independent uniform **volume** sampling, including the interior, and the ambient metric is Euclidean. A regular simplex means all \(\binom{d+1}{2}\) edge lengths are equal and positive. The asymptotic is along all integers \(d\ge2\); the theorem asserts a limiting expansion, not monotonicity or a strict sign for every finite \(d\). The event includes the boundary of the diameter ball, which has probability zero for this continuous law. Because of similarity invariance, edge length and location play no role.

## Proof

**1. Geometric reduction.** Place the simplex vertices at \(v_i=e_i-m^{-1}\mathbf1\) in the \((m-1)\)-dimensional hyperplane \(\sum z_i=0\). The centroid is the origin. For barycentric coordinate vectors \(P,Q\), the point pair is \(X=P-m^{-1}\mathbf1\), \(Y=Q-m^{-1}\mathbf1\). The angle-in-a-diameter-ball identity gives
\[
0\in B[X,Y]\quad\Longleftrightarrow\quad
\langle X,Y\rangle\le0
\quad\Longleftrightarrow\quad
\sum_{i=1}^m P_iQ_i\le\frac1m.
\]
For uniform volume sampling, \(P,Q\) are independent \(\operatorname{Dirichlet}(1,\ldots,1)\). Let \(E_i,F_i\) be independent unit-rate exponential variables. Their normalized vectors give \(P_i=E_i/\sum E_j\), \(Q_i=F_i/\sum F_j\). Multiplication by the positive denominators shows the event is exactly
\[
T_m:=\sum_{i=1}^m(E_i-\bar E)(F_i-\bar F)\le0,
\qquad \bar E=m^{-1}\sum E_i,\quad \bar F=m^{-1}\sum F_i.
\]
This is the negative-sign event for the empirical covariance of two independent exponential samples, with no approximation in the reduction.

**2. Conditional Fourier inversion.** Condition on \(E=(E_i)\), and put
\[
s^2=\sum_i(E_i-\bar E)^2,\quad
b_i=(E_i-\bar E)/s,\quad
M_j=\sum_i b_i^j.
\]
Almost surely \(s>0\), \(\sum b_i=0\), and \(M_2=1\). Conditional on \(E\), the sign of \(T_m\) is that of \(Z=\sum_i b_i(F_i-1)\), whose characteristic function is
\[
\varphi(t)=\prod_{i=1}^m\frac{e^{-itb_i}}{1-itb_i},\qquad
\log\varphi(t)=\sum_{j=2}^\infty\frac{(it)^j}{j}M_j
\]
for \(|t|\max_i|b_i|<1\). The centered conditional law is continuous. The inversion formula is
\[
\mathbb P(Z\le0\mid E)
=\frac12-\frac1\pi\int_0^\infty\frac{\operatorname{Im}\varphi(t)}t\,dt.
\]
On any event where empirical centered moments through order eight are bounded, \(s^2\) is between two positive multiples of \(m\), and a positive fraction of the centered observations have absolute value bounded away from zero, one has \(M_j=O(m^{1-j/2})\), for \(3\le j\le8\). If also \(\max_i E_i\le C\log m\), then Taylor expansion for \(t\le m^{1/30}\) followed by Gaussian integration yields
\[
\begin{aligned}
\mathbb P(Z\le0\mid E)=\frac12+\frac1{\sqrt{2\pi}}\bigg[&
\frac{M_3}{3}-\frac{3M_5}{5}
+\frac{5M_3M_4}{4}-\frac{35M_3^3}{54}\bigg]+R_m(E),\\
&\mathbb E\big[|R_m(E)|\,;\text{good event}\big]=O(m^{-2}).
\end{aligned}
\]
To verify the displayed coefficients directly, the imaginary part of the characteristic-function expansion is, to the required order,
\[
e^{-t^2/2}\left(-\frac{t^3M_3}3+\frac{t^5M_5}5-
\frac{t^7M_3M_4}{12}+\frac{t^9M_3^3}{162}\right).
\]
Integration uses \(\int_0^\infty t^{2r}e^{-t^2/2}\,dt=(2r-1)!!\sqrt{\pi/2}\). The remaining real logarithmic term of order \(M_6=O(m^{-2})\), and all higher-order terms, contribute at most \(O(m^{-2})\) to the integrated error.

For clarity, the Fourier tail is controlled separately, rather than extending a Taylor series outside its domain. A positive fraction of the \(|b_i|\) lie between positive constant multiples of \(m^{-1/2}\); hence
\[
|\varphi(t)|\le(1+ct^2/m)^{-c'm/2}
\]
for fixed positive \(c,c'\). This makes the integral above \(m^{1/30}\) negligible faster than any inverse power of \(m\). All the required good-event conditions have complement probability \(O(m^{-K})\) for any prescribed fixed \(K\): exponential maximum tails and high-moment bounds for empirical moments provide this. On the complement, the true probability and the polynomial in the normalized \(M_j\) are bounded, because \(\sum b_i^2=1\). Thus the displayed conditional expansion may be averaged with unconditional remainder \(O(m^{-2})\).

**3. Explicit moment contractions.** Define \(U_j=m^{-1}\sum_i(E_i-\bar E)^j\). For \(E_i-1\), the centered moments needed here are
\[
\mu_2=1,\qquad\mu_3=2,\qquad\mu_4=9,\qquad\mu_5=44.
\]
The exact mean formulas and first-order covariance limits are
\[
\begin{aligned}
\mathbb E U_2&=1-m^{-1},\\
\mathbb E U_3&=2-6m^{-1}+O(m^{-2}),\\
m\operatorname{Var}(U_2)&\longrightarrow8,\\
m\operatorname{Cov}(U_2,U_3)&\longrightarrow36.
\end{aligned}
\]
Indeed the first-order influence functions of \(U_2,U_3\), respectively, are \((E-1)^2-1\) and \((E-1)^3-2-3(E-1)\). Applying second-order Taylor expansion to \(f(u_3,u_2)=u_3u_2^{-3/2}\) at \((2,1)\) gives
\[
\mathbb E\left[\frac{U_3}{U_2^{3/2}}\right]
=2-\frac{27}{m}+o(m^{-1}).
\]
The correction is
\[
-6+3+\tfrac12(15/2)(8)-(3/2)(36)=-27.
\]
Since \(M_j=m^{1-j/2}U_j/U_2^{j/2}\), the law of large numbers and uniform integrability also give
\[
\begin{aligned}
\mathbb EM_3&=2m^{-1/2}-27m^{-3/2}+o(m^{-3/2}),\\
\mathbb EM_5&=44m^{-3/2}+o(m^{-3/2}),\\
\mathbb E(M_3M_4)&=18m^{-3/2}+o(m^{-3/2}),\\
\mathbb EM_3^3&=8m^{-3/2}+o(m^{-3/2}).
\end{aligned}
\]
Substituting into the averaged conditional expansion, the coefficient of \(m^{-3/2}\) inside the square brackets is exactly
\[
-\frac{27}{3}-\frac{3\cdot44}{5}
+\frac{5\cdot18}{4}-\frac{35\cdot8}{54}
=-\frac{4883}{270}.
\]
This completes the proof.

## Verification

The standalone Python program `verify.py` reconstructs the rational coefficient from the four independent moment-contraction terms, checks 3,000 independent sign equivalences in the simplex/exponential representations, and compares Monte Carlo estimates with the known planar exact case \(p_2=1/3+(\log3)/6\) and the derived asymptotic at three higher dimensions. It uses fixed seeds and checks its Monte Carlo comparisons against five standard errors. The Monte Carlo checks are *not* proofs of the asymptotic expansion, which is established by the conditional Fourier argument above. Invoke `python verify.py` using Python with NumPy installed.

## Relationship to prior work

Rabinowitz (2026) computes the exact triangle-incenter spherical depth and its extremal equilateral value, which motivates the dimensional question here. The present result treats regular simplices of arbitrary dimension and extracts their first **two nonzero high-dimensional coefficients**. Bardsley (2014) documents a tendency toward negative sample correlation for independent positively skewed variables but gives neither these exact simplex coefficients nor this two-term asymptotic. Ogasawara (2006) provides a general nonnormal sample-correlation Edgeworth expansion **through order \(m^{-1}\)**, whereas the explicit \(m^{-3/2}\) coefficient and its geometric interpretation are the contribution here. The general Edgeworth formalism is relevant machinery; historical priority for this particular evaluated coefficient is not asserted conclusively.

## Limitations

The statement does not prove a finite-dimensional monotonicity law, does not cover nonregular simplices, and does not extend directly to nonuniform volume distributions. Only an asymptotic expansion is established. General higher-order sample-correlation expansion machinery could in principle recover the coefficient after specialized moment algebra; that is a priority risk, not an independent validation of the present derivation. A closely related 2006 sample-correlation article was only accessible through an abstract; a complete historical full-text comparison was unavailable. No independent mathematical audit has been performed.

## References

1. S. Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, arXiv:2608.27491, first posted 2026-08-26. https://arxiv.org/abs/2608.27491
2. E. Bardsley, *Tendency toward negative correlations for positively-skewed independent random variables*, 2014; full-text article available at https://www.researchgate.net/publication/288978882_Tendency_toward_negative_correlations_for_positively-skewed_independent_random_variables
3. H. Ogasawara, *Asymptotic expansion of the sample correlation coefficient under nonnormality*, Computational Statistics & Data Analysis 50 (2006), 891–910. https://doi.org/10.1016/j.csda.2004.11.001
4. C. S. Withers, *Asymptotic Expansions for Distributions and Quantiles with Power Series Cumulants*, JRSS B 46 (1984), 389–396. https://doi.org/10.1111/j.2517-6161.1984.tb01310.x
