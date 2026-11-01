# The sharp quenched coverage threshold for random translates of a cube

## Finding

Let \(Q_d=[0,1]^d\). For every integer \(d\geq1\), take an infinite sequence \(U_{d,1},U_{d,2},\ldots\) of independent points uniformly distributed in \(Q_d\), and set
\[
C_{d,m}=2^{-d}\operatorname{vol}_d\left(\bigcup_{j=1}^{m}(Q_d+U_{d,j})\right),\qquad m\geq1.
\]
Thus \(C_{d,m}\) is the fraction of \([0,2]^d\) covered by the random union. Fix any \(\alpha\in(0,1)\), and define the random partial-coverage threshold
\[
T_{d,\alpha}=\min\{m\geq1:C_{d,m}\geq\alpha\}.
\]
Let \(\Phi\) and \(\phi\) denote the standard normal distribution function and density, let \(s_\alpha=\Phi^{-1}(\alpha)\), and write \(\gamma\) for Euler's constant. Then, under **any coupling** of the random sequences across dimensions,
\[
\boxed{\log T_{d,\alpha}=d+s_\alpha\sqrt d-\gamma-\frac{1-s_\alpha^2}{3}+o(1)\quad\text{almost surely as }d\to\infty.}
\]
The convergence also holds in probability. In particular, for the natural half-volume threshold,
\[
\boxed{T_{d,1/2}\,e^{-d}\longrightarrow\exp(-\gamma-1/3)\quad\text{almost surely}.}
\]
The constant is approximately \(0.402303\). The width of the threshold in logarithmic sample size is \(\sqrt d\), but its **multiplicative sample-size constant** depends jointly on the skewness of a gamma law and a Gumbel extreme-value shift.

The following auxiliary formulas and concentration estimate are included to make the result reproducible. For every \(d,m\geq1\),
\[
\mathbb E C_{d,m}=\sum_{k=1}^{m}(-1)^{k+1}\binom mk\frac1{(k+1)^d},
\qquad
\Pr\{|C_{d,m}-\mathbb EC_{d,m}|\geq t\}
\leq 2\exp\!\left(-\frac{2t^2 4^d}{m}\right).
\]
The exact mean identity is a specialization of earlier random cubical-coverage formulas and **is not asserted to be new**. The additional sharp sample-wise threshold and its constant-order shift are the claimed contribution. Uniformly for \(s\) in a fixed compact set, at \(m_d=\lceil e^{d+s\sqrt d}\rceil\) one has
\[
\mathbb E C_{d,m_d}=\Phi(s)+\frac{\phi(s)}{\sqrt d}
\left(\gamma+\frac{1-s^2}{3}\right)+O(d^{-1}).
\]
The concentration estimate upgrades this expansion to \(C_{d,m_d}\) almost surely, with an \(O(d^{-1})\) remainder under any coupling across dimensions.

## Assumptions and scope

The translations are coordinatewise uniform on the same cube, and are independent for each fixed dimension. Their joint law **between different dimensions is arbitrary**; no cross-dimensional independence is assumed. Volume is ordinary Lebesgue measure. Integer sample sizes satisfy \(m\geq1\); for the asymptotic theorem \(\alpha\in(0,1)\) is fixed before \(d\to\infty\). The geometric sets \(Q_d+U_{d,j}\) need not be disjoint, and their union is generally nonconvex. The result concerns **partial volume coverage**, not complete coverage of every point. The normalization cube \([0,2]^d\) is essential to the numerical threshold.

## Proof

### 1. An exact coverage-to-extremes identity

Choose an independent point \(X\) uniformly in \([0,2]^d\). Conditional on \(X=x\), the probability that a single random translate \(Q_d+U_{d,1}\) contains \(x\) equals
\[
p(x)=\prod_{i=1}^{d}\min\{x_i,2-x_i\}.
\]
If \(X_i\) is uniform on \([0,2]\), then \(\min\{X_i,2-X_i\}\) is uniform on \([0,1]\). Accordingly, the coordinates produce independent mean-one exponential variables
\[
E_i=-\log\min\{X_i,2-X_i\},
\qquad G_d=\sum_{i=1}^d E_i\sim\operatorname{Gamma}(d,1),
\qquad p(X)=e^{-G_d}.
\]
Fubini's theorem and conditional independence of the \(m\) translates give
\[
\mathbb E C_{d,m}=\mathbb E\{1-(1-e^{-G_d})^m\}.
\]
Introduce independent mean-one exponentials \(E'_1,\ldots,E'_m\), independent of \(G_d\), and put \(M_m=\max_{j\leq m}E'_j\). Since conditional on \(G_d=g\) each \(E'_j\) exceeds \(g\) with probability \(e^{-g}\),
\[
\boxed{\mathbb E C_{d,m}=\Pr(G_d\leq M_m).}
\]
Expanding the binomial and using \(\mathbb E e^{-kG_d}=(k+1)^{-d}\) gives the exact mean sum quoted above. It also yields the older known harmonic-polynomial representation
\[
1-\mathbb E C_{d,m}=\frac{h_{d-1}(1,1/2,\ldots,1/(m+1))}{m+1},
\]
where \(h_r\) denotes the complete homogeneous symmetric polynomial of degree \(r\). This last equality follows by differentiating \(B(1+t,m+1)=(m+1)^{-1}\prod_{j=1}^{m+1}(1+t/j)^{-1}\) \(d-1\) times at \(t=0\).

### 2. A uniform one-term expansion for the expectation

For \(m\geq2\), the maximum of \(m\) exponential random variables has
\[
\mathbb EM_m=H_m=\log m+\gamma+O(m^{-1}),
\qquad \operatorname{Var}(M_m)=\sum_{j=1}^{m}\frac1{j^2}\leq\frac{\pi^2}{6}.
\]
In particular, \(\sup_{m\geq2}\mathbb E(M_m-\log m)^2<\infty\). Let \(F_d\) be the \(\operatorname{Gamma}(d,1)\) distribution function and \(f_d\) its density. Direct differentiation, with Stirling's formula, gives the uniform bound
\[
\sup_{t>0}|f_d'(t)|=O(d^{-1})\qquad (d\to\infty).
\]
A Taylor expansion of \(F_d\) around \(a=\log m\) and the preceding bounded second moment therefore gives
\[
\mathbb E C_{d,m}=F_d(a)+\gamma f_d(a)+O(d^{-1}+m^{-1}d^{-1/2}),
\]
uniformly for \(a=d+O(\sqrt d)\). (The harmless \(m^{-1}\) correction follows from \(H_m-\log m=\gamma+O(m^{-1})\).)

For \(a=d+s\sqrt d\), Stirling expansion of the gamma density yields, locally uniformly in \(s\),
\[
\sqrt d\,f_d(d+s\sqrt d)
=\phi(s)\left[1+\frac{s^3-3s}{3\sqrt d}\right]+O_s(d^{-1}),
\]
where the error may be integrated over the left half-line using gamma Chernoff bounds. Consequently,
\[
F_d(d+s\sqrt d)
=\Phi(s)+\frac{1-s^2}{3\sqrt d}\phi(s)+O_s(d^{-1}).
\]
Combining these two estimates gives, for bounded \(s\),
\[
\boxed{\mathbb E C_{d,\lceil e^{d+s\sqrt d}\rceil}
=\Phi(s)+\frac{\phi(s)}{\sqrt d}\left(\gamma+\frac{1-s^2}{3}\right)+O_s(d^{-1}).}
\]
The ceiling changes \(\log m\) by only \(O(e^{-d-s\sqrt d})\), so does not affect the displayed error. The bounds are uniform in compact \(s\)-intervals. Equivalently, for every fixed real \(u\), taking \(m=\lceil\exp(d+s\sqrt d+u)\rceil\) gives
\[
\mathbb E C_{d,m}=\Phi(s)+\frac{\phi(s)}{\sqrt d}
\left(u+\gamma+\frac{1-s^2}{3}\right)+O_{s,u}(d^{-1}).
\]

### 3. Concentration of the random covered fraction

Hold all but one translation fixed. As its translated cube varies, the total union volume stays between the volume of the other cubes' union and that volume plus \(1\); hence the range of possible normalized covered fractions has length at most \(2^{-d}\). McDiarmid's bounded-differences inequality gives
\[
\Pr\{|C_{d,m}-\mathbb E C_{d,m}|\geq t\}
\leq2\exp(-2t^2 4^d/m),
\]
for every positive \(t\). In the critical regime \(m=\exp(d+O(\sqrt d))\), choosing \(t=d^{-1}\) makes the right-hand side summable in \(d\), since \(\log4>1\). The first Borel–Cantelli lemma proves
\[
C_{d,\lceil e^{d+s\sqrt d}\rceil}
=\mathbb E C_{d,\lceil e^{d+s\sqrt d}\rceil}+O_s(d^{-1})
\quad\text{almost surely},
\]
for each fixed \(s\), independently of the coupling across dimensions. This exhibits a random geometric quantity with an asymptotically deterministic second-order profile.

### 4. Inverting the critical profile to obtain the hitting time

Fix \(\alpha\in(0,1)\) and put \(s=s_\alpha\), \(b=-\gamma-(1-s^2)/3\). For any fixed \(\varepsilon>0\), set
\[
m_d^-=\left\lfloor\exp(d+s\sqrt d+b-\varepsilon)\right\rfloor,
\quad
m_d^+=\left\lceil\exp(d+s\sqrt d+b+\varepsilon)\right\rceil.
\]
The shifted expectation expansion gives
\[
\mathbb E C_{d,m_d^\pm}
=\alpha\pm\frac{\varepsilon\phi(s)}{\sqrt d}+O_{\alpha,\varepsilon}(d^{-1}).
\]
Because \(\phi(s)>0\), for sufficiently large \(d\), the two expectations differ from \(\alpha\) in the desired directions by at least \(\varepsilon\phi(s)/(2\sqrt d)\). Concentration at the two integer sample sizes shows that the events
\[
C_{d,m_d^-}\geq\alpha\quad\text{or}\quad C_{d,m_d^+}<\alpha
\]
have summable probabilities. By Borel–Cantelli, eventually almost surely \(C_{d,m_d^-}<\alpha\leq C_{d,m_d^+}\). The fraction is nondecreasing in \(m\); hence eventually \(m_d^-<T_{d,\alpha}\leq m_d^+\). Taking logarithms and then intersecting these probability-one events for all positive rational \(\varepsilon\) proves
\[
\log T_{d,\alpha}-d-s\sqrt d-b\longrightarrow0
\quad\text{almost surely}.
\]
For each fixed \(d\), \(T_{d,\alpha}\) is finite almost surely because \(\mathbb EC_{d,m}\uparrow1\) as \(m\to\infty\), and the random fractions themselves increase monotonically. The half-volume specialization follows by \(s_{1/2}=0\).

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It performs exact rational checks that the finite inclusion-exclusion mean equals the complete homogeneous harmonic-polynomial expression, and exact rational calculations of a concrete planar union of overlapping translates. Separate, seeded finite simulations calculate actual union volumes and compare them with the mean formula. Numerically stable integer-shape gamma CDF calculations and quadrature in the Gumbel limiting representation independently test the second-order \(d^{-1/2}\) correction and the half-volume constant-order shift. Run `python verify.py` from the extracted package directory. **Finite computations do not prove the almost-sure asymptotic or the absence of previously published results**; those claims rest on the displayed argument and the scoped literature comparison.

## Relationship to prior work

Shelley and Tartakovsky (first public October 19, 2026) investigate geometric/topological simplifications of inclusion-exclusion for deterministic unions of translates of strictly convex bodies, distinguishing the planar and higher-dimensional cases. This prompts an expectation-level and dimensional scaling question for **random box** translations, but their theorem neither treats independent uniform cube translations nor supplies a sharp sample-wise high-dimensional threshold.

**Important prior overlap:** Zhigljavsky and Noonan (2020, Section 4.2, especially equations (28)–(29)) give a general exact expected coverage formula for small axis-parallel cubes with independently uniform centers in a larger cube. Their parameters specialize to this model after translation and rescaling, so the finite expected-coverage identity above is **not** a new claim; neither is the mere observation that cube coverage is a sum of intersection volumes. The precise almost-sure sample-size threshold including the constant-order term \(-\gamma-(1-s_\alpha^2)/3\), obtained by combining the gamma–extreme-value comparison with concentration, is the claim evaluated here. The prior exact formula is a powerful starting point, not a proof in its source text of the new threshold statement.

Penrose (2023) studies complete coverage of a fixed-dimensional region by shrinking Euclidean balls sampled from within it. That is a different geometry, asymptotic regime, and coverage requirement. Random-polytope volume thresholds concern convex hulls of random points, not unions of congruent translated cubes. No directly covering published statement was identified in the targeted literature and mathematical-record searches; a priority risk remains because elementary probabilistic arguments might have appeared in other random-coverage sources.

## Limitations

This theorem is restricted to axis-parallel, equal-sized cubes, uniform translation points, and a fixed target fraction \(\alpha\in(0,1)\). It does not establish a complete-coverage threshold, rates uniform as \(\alpha\) approaches an endpoint, a central limit theorem for fluctuations of \(C_{d,m}\) below the concentration scale, or analogous constants for non-product convex bodies. Its historical priority is not independently certified. The all-dimensional finite expectation is explicitly acknowledged as covered by older work. Independent mathematical audit has not been performed.

## References

1. A. Shelley and D. Tartakovsky, *Union of Translates of a Convex Body*, arXiv:2610.25841, initial public posting October 19, 2026. https://arxiv.org/abs/2610.25841
2. A. Zhigljavsky and J. Noonan, *Covering of High-Dimensional Cubes and Quantization*, SN Operations Research Forum 1 (2020), article 18, Section 4.2, doi:10.1007/s43069-020-0015-8. Open-access text: https://orca.cardiff.ac.uk/id/eprint/134282/
3. M. D. Penrose, *Random Euclidean Coverage from Within*, Probability Theory and Related Fields 185 (2023), 747–814, doi:10.1007/s00440-022-01182-5.
4. C. McDiarmid, bounded-differences inequality; and the standard gamma Edgeworth expansion. Standard probabilistic tools are used with their hypotheses verified explicitly above.
