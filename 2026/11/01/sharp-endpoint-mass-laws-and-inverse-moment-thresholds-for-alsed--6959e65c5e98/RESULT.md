# Sharp endpoint mass laws and inverse-moment thresholds for Alsedà–Misiurewicz stationary measures

## Finding

For every two-map Alsedà–Misiurewicz (AM) system with strictly positive Lyapunov exponents at both endpoints, the unique non-atomic stationary law has **exactly determined boundary mass powers**. Let the maps and parameters be as specified below. There are unique strictly positive exponents \(\kappa_0\) and \(\kappa_1\) satisfying
\[
p_-a_-^{-\kappa_0}+p_+b_+^{-\kappa_0}=1,
\qquad p_-b_-^{-\kappa_1}+p_+a_+^{-\kappa_1}=1.
\]
For some strictly positive \(c_0,C_0,c_1,C_1,r_*\) depending on the system, and all \(0<r<r_*\),
\[
c_0r^{\kappa_0}\le\mu([0,r])\le C_0r^{\kappa_0},
\qquad c_1r^{\kappa_1}\le\mu([1-r,1])\le C_1r^{\kappa_1}.
\]
Consequently the local dimensions at the endpoints exist and equal \(\kappa_0\) and \(\kappa_1\), respectively, and for any real \(s\ge0\)
\[
\int_{(0,1)}x^{-s}\,d\mu(x)<\infty\ \Longleftrightarrow\ s<\kappa_0,
\qquad
\int_{(0,1)}(1-x)^{-s}\,d\mu(x)<\infty\ \Longleftrightarrow\ s<\kappa_1.
\]
In particular the reciprocal moments at \(s=\kappa_i\) diverge. These are **two-sided bounds at the sharp exponent**, not an assertion that normalized endpoint masses converge: multiplicative-lattice slopes can produce oscillation.

The exponent relative to one has an exact rational-slope phase criterion:
\[
\begin{aligned}
\kappa_0<1&\iff p_-/a_-+p_+/b_+>1,\\
\kappa_0=1&\iff p_-/a_-+p_+/b_+=1,\\
\kappa_0>1&\iff p_-/a_-+p_+/b_+<1,
\end{aligned}
\]
and similarly for \(\kappa_1\) with \((a_-,b_+)\) replaced by \((b_-,a_+)\).

**An asymmetric simultaneous example.** For \(p_-=p_+=1/2\), \(a_-=1/4\), \(b_-=2\), \(a_+=3/4\), \(b_+=16\), both endpoint Lyapunov exponents are positive, yet
\[
\kappa_0=\frac{\log((1+\sqrt5)/2)}{\log4}\approx0.3471209568<1,
\qquad \kappa_1\approx1.9149842712>1.
\]
Thus this one stationary law has an **infinite** left reciprocal-distance moment and a **finite** right reciprocal-distance moment. The contrasting regimes concern endpoint local dimensions, not the global Hausdorff dimension of the measure.

## Assumptions and scope

Choose \(0<a_-<1<b_-\), \(0<a_+<1<b_+\) and \(p_-,p_+>0\) with \(p_-+p_+=1\). Write
\[
x_-=(b_--1)/(b_--a_-),\qquad x_+=(1-a_+)/(b_+-a_+).
\]
On \([0,1]\) consider the increasing homeomorphisms
\[
f_-(x)=\begin{cases}a_-x&0\le x\le x_-,\\ 1-b_-(1-x)&x_-<x\le1,\end{cases}
\quad
f_+(x)=\begin{cases}b_+x&0\le x\le x_+,\\1-a_+(1-x)&x_+<x\le1.\end{cases}
\]
At each discrete step select \(f_-\) with probability \(p_-\) and \(f_+\) with probability \(p_+\), independently of all preceding choices. Assume both
\[
\Lambda_0=p_-\log a_-+p_+\log b_+>0,
\quad \Lambda_1=p_-\log b_-+p_+\log a_+>0.
\]
By the established existence and uniqueness theorem [1, Theorem 3.6], there is one stationary Borel probability \(\mu\) with \(\mu(\{0,1\})=0\), and it has no atoms [1, Proposition 3.11]. We refer **only** to this non-atomic stationary measure; the endpoint atomic measures are distinct stationary measures and are excluded. No disjoint-type, symmetry, resonance, density, or full-support assumption is imposed. Local endpoint dimension means \(\lim_{r\downarrow0}\log\mu([0,r])/\log r\), and likewise at the right endpoint.

## Proof

**1. The positive Cramér roots.** Consider either boundary with its two positive affine slopes \(D_-\) and \(D_+\), one below one and the other above one. For the left endpoint these are \((a_-,b_+)\), and for the right they are \((b_-,a_+)\). Their weighted mean log is the relevant \(\Lambda>0\). Define \(\Phi(t)=p_-D_-^{-t}+p_+D_+^{-t}\). We have \(\Phi(0)=1\), \(\Phi'(0)=-\Lambda<0\), \(\Phi''(t)=\sum_i p_i(\log D_i)^2D_i^{-t}>0\), and \(\Phi(t)\to\infty\) as \(t\to\infty\) because one slope is below one. Strict convexity therefore gives a unique second root \(\kappa>0\), with \(\Phi'(\kappa)>0\).

**2. A local CDF renewal equation.** Set \(F(r)=\mu([0,r])\). Since the maps are increasing, their initial affine pieces imply
\[
F(r)=p_-F(r/a_-)+p_+F(r/b_+),\qquad 0<r<\delta_0,
\]
where \(\delta_0=\min\{a_-x_-,b_+x_+\}>0\). Similarly \(G(r)=\mu([1-r,1])\) satisfies
\[
G(r)=p_-G(r/b_-)+p_+G(r/a_+),\qquad 0<r<\delta_1,
\]
where \(\delta_1=\min\{b_-(1-x_-),a_+(1-x_+)\}>0\). Equalities at a branch point are harmless because \(\mu\) has no atoms.

Both \(F(r)\) and \(G(r)\) are strictly positive for every \(r>0\). Indeed, any interior point of \(\operatorname{supp}\mu\) has its whole forward semigroup orbit in that support because stationarity has strictly positive probabilities. As \(f_-^n(x)\downarrow0\) and \(f_+^n(x)\uparrow1\) for every interior \(x\), the support meets every endpoint neighbourhood with positive \(\mu\)-measure. Also \(F(r),G(r)\to0\) as \(r\downarrow0\), from the absence of endpoint atoms.

**3. A stopped multiplicative walk.** We prove a general lemma for either renewal equation. Suppose a nondecreasing bounded CDF \(H\) obeys \(H(r)=\sum_{i\in\{-,+\}}p_iH(r/D_i)\) for \(0<r<\delta\), is continuous at zero with \(H(0)=0\), and has \(H(\delta)>0\). Let \(Z_0=r\in(0,\delta)\), let independent symbols have law \((p_-,p_+)\), set \(Z_n=r/\prod_{j=1}^nD_{i_j}\), and stop at \(\tau=\inf\{n\ge0:Z_n\ge\delta\}\). Until exit, the process \(H(Z_{n\wedge\tau})\) is a bounded martingale. On \(\{\tau=\infty\}\), the strong law gives \(Z_n\to0\) because \(\sum_i p_i\log D_i>0\). Bounded convergence and optional stopping yield
\[
H(r)=\mathbb E_p[H(Z_\tau)\mathbf1_{\{\tau<\infty\}}].
\]
Define new symbol probabilities \(q_i=p_iD_i^{-\kappa}\); by the root equation they are strictly positive and sum to one. At any stopped path of length \(n\), the likelihood ratio is
\[
\frac{\mathbb P_p(i_1,\ldots,i_n)}{\mathbb P_q(i_1,\ldots,i_n)}
=\prod_{j=1}^n D_{i_j}^{\kappa}
=(r/Z_n)^{\kappa}.
\]
Summing over the disjoint finite hitting paths gives
\[
H(r)=r^{\kappa}\mathbb E_q\!
\left[\frac{H(Z_\tau)}{Z_\tau^{\kappa}}\,\mathbf1_{\{\tau<\infty\}}\right].
\]
Under the tilted law, \(\mathbb E_q\log(1/D_i)=\Phi'(\kappa)>0\), so \(Z_n\to\infty\) under \(q\) and \(\mathbb P_q(\tau<\infty)=1\). Write \(d=\min_iD_i<1\). An exit can only occur through division by such a \(d\), because other slopes exceed one. Hence at first exit \(\delta\le Z_\tau<\delta/d\). When applied to the two AM boundaries, \(\delta/d\le1\), so all terms are legitimate CDF values. Monotonicity yields the uniform positive bounds
\[
H(\delta)(\delta/d)^{-\kappa}\,r^{\kappa}
\le H(r)\le \delta^{-\kappa}r^{\kappa}.
\]
This establishes the claimed comparison at both endpoints, without non-lattice assumptions or the existence of a limiting leading coefficient.

**4. Dimensions, inverse moments and phases.** The logarithms of the two power bounds, divided by \(\log r\to-\infty\), prove both exact endpoint dimensions. For \(s>0\), the layer-cake formula applied near zero gives
\[
\int_{(0,1)}x^{-s}\,d\mu(x)
=1+s\int_0^1r^{-s-1}\mu((0,r))\,dr,
\]
with possible value \(+\infty\); the right counterpart is identical. Replacing the inner endpoint mass by its sharp two-sided powers reduces convergence to \(\int_0^{r_*}r^{\kappa_i-s-1}\,dr\), which is finite exactly for \(s<\kappa_i\). For \(s=0\) the integrals equal one. Strict convexity gives \(\Phi(t)<1\) for \(0<t<\kappa\) and \(\Phi(t)>1\) for \(t>\kappa\); setting \(t=1\) proves the phase criteria.

**5. Exact two-regime example.** With the displayed four rational slopes and equal probabilities, \(x_-=4/7\), \(x_+=1/61\), \(\Lambda_0=\log2>0\), and \(\Lambda_1=(\log(3/2))/2>0\). The left root equation is \(4^\kappa+16^{-\kappa}=2\). Substituting \(z=4^\kappa\) reduces it to \((z-1)(z^2-z-1)=0\), whose positive nontrivial solution is the golden ratio. For the right root the equation is \(2^{-\kappa}+(4/3)^\kappa=2\); its unique positive root lies between one and two because at one the left side is \(11/6<2\) whereas at two it is \(1/4+16/9>2\) (strictly true since \(1/4+16/9=73/36>2\)). Thus the left first inverse moment diverges and the right converges. This completes the proof.

## Verification

The accompanying `CHECK.py` independently checks branch continuity, exact rational breakpoint and terminal-value identities, the local inverse formulas at many rational radii, the positivity of both endpoint Lyapunov products, the rational phase inequalities, the polynomial golden-ratio identity, and a numerical bracket for the unique right exponent. The proof of the infinite-parameter claims rests on the stopped-walk change-of-measure argument above, **not** on the checker or on a finite sampling of radii.

## Relationship to prior work

Barański and Śpiewak [1] define these AM systems, prove existence/uniqueness of their interior stationary measure (Theorem 3.6), establish non-atomicity (Proposition 3.11), and give a weaker, unspecified small-Hölder-exponent upper boundary estimate. Their Theorem 2.4 characterizes when the **entire** stationary law is Lebesgue. The new claim is different: it identifies **both sharp local endpoint exponents for every positive-Lyapunov AM system**, including singular measures, proves matching lower bounds, and gives complete negative-moment thresholds. In [2] the same authors study the global Hausdorff dimension of these stationary laws, not these two local endpoint mass rates. Bradík and Roth [3] address generic full-support singularity in a broader smoothness class rather than the explicit slopes/thresholds proved here. Generic exponential change-of-measure and Cramér-root techniques are established methods; the claim of originality is only their exact two-endpoint dynamical consequence in this AM family, not the probabilistic method itself.

## Limitations

The constants in the sharp two-sided comparison depend on the system and are not claimed optimal. A limit of the normalized quotient \(\mu([0,r])/r^{\kappa_0}\) or its right analogue is **not** asserted (lattice resonance may prevent it). The endpoint dimensions are **not** the global Hausdorff dimension of \(\mu\); no claims concern mixing, smoothness of \(\mu\), or place-dependent branch probabilities. The stationary endpoint atoms are excluded. Literature priority beyond the inspected primary texts and mathematical indexes remains to be independently evaluated.

## References

[1] K. Barański and A. Śpiewak, *Singular stationary measures for random piecewise affine interval homeomorphisms*, arXiv:1905.11048v1 (first public 2019-05-27), Journal of Dynamics and Differential Equations 33 (2021), 345–393, DOI:10.1007/s10884-019-09807-5. Full accessible primary text: https://link.springer.com/article/10.1007/s10884-019-09807-5.

[2] K. Barański and A. Śpiewak, *On the dimension of stationary measures for random piecewise affine interval homeomorphisms*, arXiv:2208.06394v2 (first public 2022-08-12), Ergodic Theory and Dynamical Systems 44 (2024), 1473–1488.

[3] J. Bradík and S. Roth, *Typical behaviour of random interval homeomorphisms*, arXiv:2102.02023v1 (first public 2021-02-03).
