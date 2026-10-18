# A heavy-tail phase transition and two-sided scaling law for a rational planar map

## Finding

Consider the real rational map
\[
F(x,y)=\left(\frac{\tfrac32x-\tfrac54}{y},\frac{x-\tfrac32}{y}\right),\qquad y\ne0.
\]
Put \(\theta=\arccos(1/4)\), \(h=\sqrt{15}\), and, for every \(P\ge0\), define
\[
\begin{split}
D_P(t)&=P+2\cos t,\\
\Phi_P(t)&=\left(\frac{10P+5\cos t-h\sin t}{4D_P(t)},
\frac{2P+\cos t-h\sin t}{2D_P(t)}\right).
\end{split}
\]
Delete all initial angles whose forward or backward \(\theta\)-rotation orbit meets a zero of \(D_P\):
\[
\Omega_P=\{t\in\mathbb R/(2\pi\mathbb Z):D_P(t+n\theta)\ne0\ \text{for every }n\in\mathbb Z\}.
\]
Let \(\Gamma_P=\Phi_P(\Omega_P)\), and denote by \(\mu_P\) the pushforward to \(\Gamma_P\) of normalized circular Lebesgue measure. The map preserves \(\Gamma_P\), and \(\mu_P\) is its unique invariant Borel probability on that set. In particular it is ergodic. When \(P=0\), the parametrization identifies antipodal angles; for \(P>0\) it is injective.

Let \(R(x,y)=\sqrt{x^2+y^2}\). There is an exact sharp transition in the tails and moment integrability of this natural stationary observable:

**Two simple poles.** If \(0\le P<2\), put \(s_P=\sqrt{1-P^2/4}\) and
\[
V_\pm(P)=\left(\frac{15P}{8}\mp\frac{\sqrt{15}}4s_P,
\frac{3P}{4}\mp\frac{\sqrt{15}}2s_P\right),
\qquad
K(P)=\frac{\|V_+(P)\|+\|V_-(P)\|}{2\pi s_P}.
\]
Then \(K(P)>0\) and
\[
\lim_{r\to\infty}r\,\mu_P\{R>r\}=K(P).
\]
At \(P=0\) the invariant curve is the line \(y=2x-1\); its second-coordinate marginal is the exact Cauchy law with location \(1/4\) and scale \(\sqrt{15}/4\), and \(K(0)=5\sqrt3/(4\pi)\).

**Coalesced double pole.** At \(P=2\), put \(a=\sqrt{261}/4=3\sqrt{29}/4\). Then
\[
\lim_{r\to\infty}\sqrt r\,\mu_2\{R>r\}=\frac{\sqrt a}{\pi}.
\]
For \(P>2\), \(\Gamma_P\) is bounded. Consequently, for every real \(q>0\),
\[
\int R^q\,d\mu_P<\infty
\quad\Longleftrightarrow\quad
\begin{cases}
q<1,&0\le P<2,\\
q<\tfrac12,&P=2,\\
\text{always},&P>2.
\end{cases}
\]
For every complete initial orbit on \(\Gamma_P\) and every exponent \(q>0\) for which the moment diverges, the empirical average of \(R^q\) tends to \(+\infty\), not merely almost surely.

**Sharp two-sided crossover.** For every fixed \(\xi>0\), as \(\delta\downarrow0\),
\[
\begin{split}
\delta^{-1/2}\mu_{2-\delta}\{R>a\xi/\delta\}
&\longrightarrow\frac1\pi\left(\sqrt{1+\xi^{-1}}-\sqrt{(1-\xi^{-1})_+}\right),\\
\delta^{-1/2}\mu_{2+\delta}\{R>a\xi/\delta\}
&\longrightarrow\frac1\pi\sqrt{(\xi^{-1}-1)_+},
\end{split}
\]
where \((u)_+=\max(u,0)\). The two different boundary profiles quantify how an unbounded heavy-tailed stationary state passes into a bounded stationary state.

## Assumptions and scope

All parameters and coordinates are real. The rational map is defined only when \(y\ne0\); the set \(\Omega_P\) deletes the countable forbidden angle orbit, ensuring every forward and backward rational iterate is defined. Angle is measured modulo \(2\pi\). Invariant probabilities and unique ergodicity are asserted on the explicitly specified invariant carrier \(\Gamma_P\), not on the whole plane. At \(P=0\), the carrier is a line with a countable subset removed; at \(P>0\), it is an explicitly parametrized conic-type carrier (with possible forbidden points deleted). Tail and moment statements refer to the Euclidean norm \(R\) and the particular measure \(\mu_P\). The exponent \(q\) is strictly positive.

## Proof

**1. Exact conjugacy and uniqueness of the stationary law.** Write
\[
W_P(t)=P+2\cos t,\qquad
X_P(t)=\tfrac32+\frac{W_P(t+2\theta)}{W_P(t)},\qquad
Y_P(t)=\frac{W_P(t+\theta)}{W_P(t)}.
\]
The identities \(\cos\theta=1/4\), \(\sin\theta=\sqrt{15}/4\), and \(\cos(2\theta)=-7/8\) simplify these to the displayed formula for \(\Phi_P\). The Fourier modes \(1,e^{it},e^{-it}\) have characteristic polynomial
\[
(z-1)(z^2-\tfrac12z+1)=z^3-\tfrac32z^2+\tfrac32z-1.
\]
Hence
\[
W_P(t+3\theta)=\tfrac32W_P(t+2\theta)-\tfrac32W_P(t+\theta)+W_P(t).
\]
Substitution shows \(F(\Phi_P(t))=\Phi_P(t+\theta)\) for all \(t\in\Omega_P\). The rational map's denominators do not vanish there because \(Y_P(t)=W_P(t+\theta)/W_P(t)\ne0\). The linear map from \((P,\cos t,\sin t)\) to \((W_P(t+2\theta),W_P(t+\theta),W_P(t))\) is nonsingular: its matrix has determinant \(3\sqrt{15}/2\). Equality of the rational images therefore forces the two triples \((P,\cos t,\sin t)\) to be proportional. For \(P>0\), their first coordinates fix the proportionality factor at one and thus the angles agree. For \(P=0\), equality holds exactly for equal or antipodal angles.

The number \(2\cos\theta=1/2\) is rational but not an integer. If \(\theta/\pi\) were rational it would be a sum of roots of unity, hence an algebraic integer, contradicting the fact that the only rational algebraic integers are integers. Thus rotation by \(\theta\), as well as its quotient rotation modulo \(\pi\), is irrational and uniquely ergodic. The excluded angles form a countable invariant set, with zero circular Lebesgue measure; every invariant probability on its complement extends by zero to the circle and must be Haar. By the injectivity just proved (or the antipodal quotient when \(P=0\)), \(\mu_P\) is the unique invariant probability on \(\Gamma_P\).

**2. Simple poles and the order-one tail.** For \(0\le P<2\), \(D_P(t)\) has precisely two simple roots satisfying \(\cos t=-P/2\) and \(\sin t=\pm s_P\). At either root the numerator vector \((D_PX_P,D_PY_P)\) is exactly \(V_\pm(P)\), and the absolute derivative of the denominator is \(2s_P\). Neither numerator vector vanishes: simultaneous vanishing of both components would force \(P=0\) and \(s_P=0\), which is impossible. Therefore near that pole,
\[
R(\Phi_P(t))\sim\frac{\|V_\pm(P)\|}{2s_P|t-t_\pm|}.
\]
The length of its exceedance neighborhood at radius \(r\), multiplied by \(r\), tends to \(\|V_\pm(P)\|/s_P\). The two disjoint neighborhoods supply all large-radius exceedances, and division by \(2\pi\) yields the asserted constant \(K(P)\). When \(P=0\), direct simplification gives \(Y_0(t)=1/4-(\sqrt{15}/4)\tan t\) and \(Y_0=2X_0-1\), proving the Cauchy and norm-tail statements.

**3. Double pole and the sharp moment transition.** When \(P=2\), the sole zero of \(D_2(t)=2+2\cos t\) is \(t=\pi\), where \(D_2(\pi+u)=u^2+O(u^4)\). The numerator vector there equals \((15/4,3/2)\) and has norm \(a=\sqrt{261}/4\). Thus \(R(\Phi_2(\pi+u))\sim a/u^2\), so the exceedance interval has length asymptotic to \(2\sqrt{a/r}\). For \(P>2\), the denominator is bounded below by \(P-2>0\), giving bounded image. The layer-cake identity
\[
\int R^q\,d\mu_P=q\int_0^\infty r^{q-1}\mu_P\{R>r\}\,dr
\]
establishes all integrability thresholds, including divergence at equality. For a divergent exponent choose \(M>0\) and set \(g_M(t)=\min(R(\Phi_P(t))^q,M)\) on \(\Omega_P\). This extends continuously over each deleted pole by the value \(M\). By irrational-rotation unique ergodicity, the averages of \(g_M(t+n\theta)\) converge, for every admissible initial angle, to its Haar integral. Since \(R^q\ge g_M\), the lower limit of its orbit averages is at least that integral. Monotone convergence sends the integrals to infinity as \(M\to\infty\), proving all-orbit divergence.

**4. The two boundary scaling functions.** Fix \(\xi>0\) and put \(t=\pi+\sqrt\delta z\). Uniformly on bounded \(z\)-intervals,
\[
D_{2\pm\delta}(t)=\delta(z^2\pm1)+O(\delta^2z^4),
\quad
\big\|(D_{2\pm\delta}X_{2\pm\delta},D_{2\pm\delta}Y_{2\pm\delta})\big\|=a+o(1).
\]
If \(R>a\xi/\delta\), then \(|D_{2\pm\delta}(t)|\) is bounded by a fixed multiple of \(\delta\). This forces \(t-\pi=O(\sqrt\delta)\), so no exceedance region is omitted by this local scaling. The limiting condition is exactly \(|z^2\pm1|<\xi^{-1}\); its boundary consists of finitely many points and contributes zero limiting measure. In the minus case, its total one-dimensional length equals
\[
2\left(\sqrt{1+\xi^{-1}}-\sqrt{(1-\xi^{-1})_+}\right),
\]
while the plus case has length \(2\sqrt{(\xi^{-1}-1)_+}\). Multiplication by \(\sqrt\delta/(2\pi)\) proves the two formulas. This completes the theorem.

## Verification

The accompanying standalone `verify.py` reconstructs the conjugacy with exact SymPy simplification, checks the nonsingular projective-coordinate matrix, derives both numerator vectors, and confirms the critical-pole squared norm \(261/16\). It also checks the local denominator limits symbolically and compares six numerical exceedance probabilities (two sides, three threshold ratios) with the limiting profiles using deterministic root isolation and bisection. Running the packaged checker yielded `VERIFY_OK`. These finite numerical comparisons are diagnostics; the proof of all-parameter and infinite-time statements is the analysis above.

## Relationship to prior work

Bajo, Franco, and Perán (arXiv:1011.2050, publicly posted November 9, 2010), especially their Theorem 11 and explicit projective solution formulas, established the conic orbit structure of the ambient rational-map family. The present rational map, its linear-projective conjugacy, and the conic parametrization are specializations of that framework, not independent discoveries. Bajo (arXiv:1311.3199) further studies invariant quadrics and orbit geometry. The novelty claimed here is the **specific stationary-law calculation**, the complete simple-pole/double-pole/bounded **moment trichotomy**, the every-complete-orbit divergent-moment statement, and the **two different double-scaling exceedance profiles** at the conic transition. None of those claims was found in the inspected primary manuscripts. Their relation to generic projective and Cauchy-distribution theory is discussed under limitations.

## Limitations

Only the stated explicit rational map and the listed invariant carriers are classified, not all parameters of the general rational-system family. The probability measure is supported on a one-dimensional invariant curve (not two-dimensional Lebesgue measure). Unique invariance is relative to \(\Gamma_P\) and does not exclude other invariant sets or invariant probabilities elsewhere in the plane. Finite moments below the cutoff imply convergence of orbit averages for almost every initial angle by Birkhoff's theorem, not necessarily every angle. The proof of all-orbit divergence is restricted to nonnegative powers whose invariant means diverge. The source and database searches support but cannot certify absolute historical originality: implicit instances may exist within broader projective or singular-observable ergodic theory. No independent audit has been performed.

## References

1. I. Bajo, D. Franco and J. Perán, *Dynamics of a Rational System of Difference Equations in the Plane*, arXiv:1011.2050v1 (public 2010-11-09), https://arxiv.org/abs/1011.2050 . Full original text includes Theorem 11 and equations (14)–(18).
2. I. Bajo, *Invariant quadrics and orbits for a family of rational systems of difference equations*, arXiv:1311.3199 (2013), https://arxiv.org/abs/1311.3199 .
3. I. Bajo and E. Liz, *Periodicity on discrete dynamical systems generated by a class of rational mappings*, Journal of Difference Equations and Applications 12 (2006), 1201–1212, DOI:10.1080/10236190600949782.
