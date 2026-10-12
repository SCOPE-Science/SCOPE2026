# Pareto-tail copy activation for randomly sampled passive qutrits

## Finding
For a uniformly sampled diagonal passive three-level state with equally spaced levels, the number of copies first permitting positive work extraction is finite almost surely but has **infinite expectation**. The exact survival function, for every integer \(m\ge1\), is
\[
\Pr(A>2m+1)=6\int_0^1\left[\frac1{(1+u+u^{2+1/m})^2}-\frac1{(1+u+u^{2-1/(m+1)})^2}\right]du.
\]
Its sharp tail constant is
\[
C=24\int_0^1\frac{-u^2\log u}{(1+u+u^2)^3}\,du=0.5226368151659937\ldots,
\qquad\Pr(A>t)\sim\frac{2C}{t}.
\]
This exponent persists for every continuous ensemble density that is positive on a nontrivial section of the thermal-state curve. Consequently \(\mathbb E[A^q]\) is finite exactly for \(0<q<1\).

## Assumptions and scope
Let \(\varepsilon>0\), \(H=\varepsilon\operatorname{diag}(0,1,2)\), and \(\rho=\operatorname{diag}(p_0,p_1,p_2)\), with \(p_0\ge p_1\ge p_2>0\), \(p_0+p_1+p_2=1\). A tensor power is *passive* if no joint unitary lowers its mean energy. Let \(A\in\{3,5,7,\ldots\}\cup\{\infty\}\) be the smallest copy number permitting strictly positive work; the infinite value applies only to completely passive thermal states in this full-rank setting. The uniform law means normalized two-dimensional Lebesgue measure in \((p_1,p_2)\) on the ordered simplex, of area \(1/12\); its density is \(12\). For the generalized law, take a nonnegative bounded continuous density \(f(p_1,p_2)\), normalized on that triangle, that is strictly positive at least at one interior point of the thermal curve \(p_j\propto e^{-jt}\) for \(t>0\).

## Proof
**1. Reconstruct the copy criterion.** Put \(a=\log(p_0/p_1)\ge0\), \(b=\log(p_1/p_2)\ge0\). In a basis configuration of \(N\) copies with \(z\) occurrences of level 2 and energy index \(E\in\{0,\ldots,2N\}\), the population is proportional to \(e^{-aE-(b-a)z}\). At energy \(E\), the admissible integer interval is
\[
\max(0,E-N)\le z\le\lfloor E/2\rfloor.
\]
Passivity means that the smallest population at energy \(E\) is at least the largest population at energy \(E+1\), for every \(E=0,\ldots,2N-1\). For \(N=2m+1\), comparing the endpoints of these intervals gives exactly \(a\ge m(b-a)\) when \(b\ge a\), or \(a\ge(m+1)(a-b)\) when \(b\le a\). (Indeed the relevant extreme differences of the allowed \(z\)-ranges are respectively \(m\) and \(m+1\), attained by central adjacent energy shells.) Both inequalities are equivalent to
\[
 m/(m+1)\le b/a\le(m+1)/m,
 \quad\text{or}\quad a+b\ge(2m+1)|a-b|.
\]
At \(a=0\), interpret the condition without division; the boundary has zero sampling measure. The even-copy criterion agrees with that for the preceding odd number of copies: the same interval-endpoint argument applies to \(N=2m+2\). The elementary shell comparison independently reconstructs the required known deterministic finite-copy criterion; the new claim concerns its ensemble distribution and limiting law.

**2. Push forward the uniform measure.** Put \(u=p_1/p_0=e^{-a}\) and \(v=p_2/p_1=e^{-b}\). Then
\[
(p_0,p_1,p_2)=\frac{(1,u,uv)}{1+u+uv},\qquad
\left|\frac{\partial(p_1,p_2)}{\partial(u,v)}\right|=\frac{u}{(1+u+uv)^3}.
\]
For \(m\ge1\), passivity of the \((2m+1)\)-copy state is equivalent to
\[
0<u<1,\qquad u^{(m+1)/m}\le v\le u^{m/(m+1)}.
\]
The random variable \(A\) is greater than \(2m+1\) exactly on this region. Multiplying the Jacobian by the uniform density \(12\), integrating \(v\) explicitly, and then \(u\), gives the stated exact one-dimensional integral.

**3. Sharp asymptotics.** Equivalently, write \(a=-\log u\), \(b=-\log v\), and \(D(a,b)=1+e^{-a}+e^{-a-b}\). The exact integration region is
\[
a>0,\quad \frac{m}{m+1}a\le b\le\frac{m+1}{m}a.
\]
Its width is \(a(1/m+1/(m+1))\). In \((a,b)\) coordinates, the probability-element Jacobian is \(e^{-2a-b}/D(a,b)^3\). For a continuous probability density \(f\), dominated convergence, using \(b\ge a/2\) and the integrable bound proportional to \(a e^{-5a/2}\), yields
\[
\lim_{m\to\infty}m\Pr_f(A>2m+1)= C_f
=2\int_0^\infty\frac{a e^{-3a}\, f\!\left(\frac{e^{-a}}{1+e^{-a}+e^{-2a}},\frac{e^{-2a}}{1+e^{-a}+e^{-2a}}\right)}{(1+e^{-a}+e^{-2a})^3}\,da.
\]
If \(f\) is positive anywhere on the interior thermal curve, continuity makes \(C_f>0\). The uniform density \(f=12\) reduces this expression to the displayed constant \(C\). Since passivity for even tensor powers has the same threshold as for the previous odd power, monotonicity squeezes arbitrary integer and real \(t\) between successive odd thresholds and gives \(t\Pr_f(A>t)\to 2C_f\). The thermal curve has two-dimensional Lebesgue measure zero, so \(A<\infty\) almost surely. The tail-sum (or layer-cake) identity implies \(\mathbb E_f[A]=\infty\), and for \(q>0\), \(\mathbb E_f[A^q]<\infty\) iff \(q<1\).

## Verification
The companion standalone program `verify.py` enumerates all product-basis configurations for 384 small finite instances using exact rational populations and independently checks the adjacent-energy-shell criterion. It also evaluates the exact survival integral numerically for two finite copy numbers, and checks convergence of the scaled survival probability toward its independently integrated limit. Run `python verify.py` after installing the single declared numerical dependency (`scipy`). The reported run is `VERIFY_OK finite_tensor_cases=384 tail_at_3=0.3474185942900126 tail_at_5=0.20885085501991435 constant=0.5226368151659937 10000_scaled=0.5226106846009265`. These computations are consistency checks; the infinite-copy theorem follows analytically from the shell comparison and dominated convergence.

## Relationship to prior work
Classical complete-passivity theorems identify Gibbs states as exactly the full-rank states that are passive for all copy numbers (Pusz–Woronowicz; Lenard). Skrzypczyk, Silva and Brunner explain finite-copy activation using virtual-temperature inequalities and produce an explicit sufficient-copy construction. Salvia and Giovannetti derive quantitative energy bounds for structurally stable and general finite-copy passive states. Those results, and the exact elementary equal-gap finite-copy criterion obtainable from the shell comparison above, are antecedents; no novelty is asserted for the deterministic criterion itself. The present statement gives the exact probability law under a geometrically defined sampling measure and a universal nonintegrable first-activation tail across continuous ensembles. We did not identify these ensemble conclusions in the inspected primary papers. The possibility of an unlocated more general result remains.

## Limitations
The result concerns diagonal, full-rank, three-level passive states with equal energy spacing and unrestricted global unitaries. It does not address arbitrary energy gaps, coherent states, restricted controls, work-storage models, or other sampling measures lacking a continuous density positive along the Gibbs curve. The universal exponent has an ensemble-dependent constant, not a universal numerical coefficient. Numerical tests cover finitely many copies and cannot certify the asymptotic theorem. Publication-priority comparison is incomplete; independent audit has not been performed.

## References
1. P. Skrzypczyk, R. Silva, and N. Brunner, *A short note on passivity, complete passivity and virtual temperatures*, arXiv:1412.5485v1 (first public December 17, 2014), later *Physical Review E* **91**, 052133 (2015). https://arxiv.org/abs/1412.5485
2. R. Salvia and V. Giovannetti, *Energy upper bound for structurally-stable N-passive states*, arXiv:1912.02099 (2019), *Quantum* (2020). https://arxiv.org/abs/1912.02099
3. W. Pusz and S. L. Woronowicz, *Passive states and KMS states for general quantum systems*, *Communications in Mathematical Physics* **58**, 273–290 (1978). DOI 10.1007/BF01614224.
4. A. Lenard, *Thermodynamical proof of the Gibbs formula for elementary quantum systems*, *Journal of Statistical Physics* **19**, 575–586 (1978). DOI 10.1007/BF01011769.
