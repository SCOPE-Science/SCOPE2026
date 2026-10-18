# Pathwise multifractal spectrum of rotation displacement for two degree-one circle maps

## Finding
Let \(\omega\in\{+,-\}^{\mathbb N}\) be **any** (not necessarily generic or stationary) forcing sequence for which the asymptotic fraction of \(+\) symbols is \(p\in[0,1]\). The degree-one lifts specified below have, for each \(c\in[p-1,p]\), a level set \(E_\omega(c)\) of initial circle points with asymptotic lift displacement \(c\), and
\[
\dim_{\mathrm H}E_\omega(c)=\frac1{\log3}\inf_{t\in\mathbb R}\left\{p\log(1+2e^t)+(1-p)\log(1+2e^{-t})-tc\right\}.
\]
The infimum is also interpreted as its limit at an infinite optimizer at the endpoints. Explicitly,
\[
\dim_{\mathrm H}E_\omega(p)=\frac{p\log2}{\log3},\qquad
\dim_{\mathrm H}E_\omega(p-1)=\frac{(1-p)\log2}{\log3}.
\]
The spectrum is strictly concave and real analytic on \((p-1,p)\), with its unique dimension-one peak at \(c=(4p-2)/3\). No orbit has a limiting displacement outside \([p-1,p]\). Thus the entire rotation-level spectrum depends only on symbol frequency, not on forcing correlations or the lengths of its blocks; in particular the conclusion includes deterministic forcing sequences that are not generic for any specified Bernoulli measure.

## Assumptions and scope
Write \(\mathbb T=\mathbb R/\mathbb Z\). On \([0,1)\) set
\[
F_+(x)=\begin{cases}3x,&0\le x<2/3,\\4-3x,&2/3\le x<1,\end{cases}\quad
F_-(x)=\begin{cases}-3x,&0\le x<1/3,\\3x-2,&1/3\le x<1.\end{cases}
\]
Extend by \(F_s(x+m)=F_s(x)+m\) for integers \(m\), and let \(f_s=F_s\pmod1\). For the prescribed forward forcing \(\omega=(\omega_1,\omega_2,\ldots)\), put \(F_\omega^{(n)}=F_{\omega_n}\circ\cdots\circ F_{\omega_1}\). Assume only
\[
\lim_{n\to\infty}n^{-1}\#\{1\le k\le n:\omega_k=+\}=p.
\]
Define \(E_\omega(c)=\{x\in[0,1):\lim_{n\to\infty}(F_\omega^{(n)}(x)-x)/n=c\}\). Hausdorff dimension uses Euclidean distance on \([0,1)\), equivalently circle distance. The lift (rather than a mod-one orbit distance) is essential to the definition of displacement.

## Proof
**Full-branch coding and integer cocycle.** Each map \(f_s\) has three affine monotone full branches over the intervals \(I_j=(j/3,(j+1)/3)\), with slopes of absolute value \(3\). Their lift-integer values are, in branch order,
\[
k_+(0),k_+(1),k_+(2)=(0,1,1),\quad
k_-(0),k_-(1),k_-(2)=(-1,-1,0).
\]
The inverse branches (with target coordinate \(u\in(0,1)\)) are
\[
\begin{array}{c|ccc}
&j=0&j=1&j=2\\\hline
+&u/3&(1+u)/3&(3-u)/3\\
-&(1-u)/3&(1+u)/3&(2+u)/3.
\end{array}
\]
Therefore every length-\(n\) branch word defines an interval of length \(3^{-n}\) (up to endpoints), and these intervals partition the unit interval. For any orbit avoiding the countable set of branch preimages, its branch word \(j_1,j_2,\ldots\) satisfies the **exact telescoping identity**
\[
F_\omega^{(n)}(x)-x=\sum_{k=1}^{n}k_{\omega_k}(j_k)+u_n-u_0,
\]
where \(u_k=f_{\omega_k}\circ\cdots\circ f_{\omega_1}(x)\in[0,1)\). The terminal error is bounded by one. Preimages of branch boundaries form a countable set; once a boundary is hit, a subsequent integer lift remains an integer, and its limiting displacement is zero, so these exceptional points cannot add any dimension or a value outside the interval below.

**Pressure and upper bound.** For every real \(t\), the cylinder partition sum of the exponential integer displacement is exactly
\[
Z_n(t)=\sum_{j_1,\ldots,j_n}\exp\Big(t\sum_{k=1}^{n}k_{\omega_k}(j_k)\Big)
=(1+2e^t)^{N_+(n)}(1+2e^{-t})^{n-N_+(n)}.
\]
Consequently \(n^{-1}\log Z_n(t)\to P_p(t)=p\log(1+2e^t)+(1-p)\log(1+2e^{-t})\). An orbit in \(E_\omega(c)\) has every sufficiently long branch sum between \(n(c-\varepsilon)\) and \(n(c+\varepsilon)\). For \(t\ge0\), the number of such words is bounded by \(\exp[-tn(c-\varepsilon)]Z_n(t)\); for \(t<0\) use \(c+\varepsilon\). Covering by length-\(3^{-n}\) cylinders, and then taking \(\varepsilon\downarrow0\), proves
\[
\dim_{\mathrm H} E_\omega(c)\le \frac{P_p(t)-tc}{\log3}
\]
for every \(t\), hence the infimum. The deterministic integer increments lie between \(-1\) and \(1\), and the frequency limit more sharply forces all convergent averages into \([p-1,p]\).

**Lower bound inside the interval.** Since \(P_p''(t)>0\) for every finite \(t\), the derivative \(P_p'(t)\) increases continuously from \(p-1\) to \(p\). For every interior \(c\), select its unique \(t\) with \(P_p'(t)=c\). On the branch-word space construct the independent (not identically distributed) digit law assigning at step \(k\) the probability
\[
q_{k,t}(j)=\frac{e^{t k_{\omega_k}(j)}}{\sum_{i=0}^{2}e^{t k_{\omega_k}(i)}}.
\]
All logarithms of these probabilities and all increments are uniformly bounded for fixed \(t\). Kolmogorov's strong law for independent bounded variables yields, almost surely, convergence of the average increment to \(P_p'(t)=c\) and of minus-log cylinder masses per symbol to \(h_p(c)=P_p(t)-tc\). The inverse-branch coding projects this law onto \(E_\omega(c)\). Its almost-sure Euclidean local dimension is \(h_p(c)/\log3\): in addition to the cylinder-mass limit, uniform positivity of the three step probabilities implies by Borel–Cantelli that the number of consecutive branch choices keeping a coded point within \(3^{-(n+r)}\) of an order-\(n\) cylinder boundary is \(o(n)\). Thus Euclidean balls and cylinders agree on the logarithmic scale; the mass-distribution principle gives the matching lower bound. (Equivalently, one may use the standard triadic Billingsley dimension lemma.)

**Boundary levels.** For \(c=p\), at each plus step choose uniformly between the two maximizing branches \(j\in\{1,2\}\), and at each minus step choose only \(j=2\). Every sample sequence has limiting increment \(p\); the cylinder information rate is \(p\log2\), giving dimension \(p\log2/\log3\) by the same interval-coding argument. For \(c=p-1\), choose only \(j=0\) at plus steps, and choose uniformly between \(j\in\{0,1\}\) at minus steps. This gives dimension \((1-p)\log2/\log3\). The pressure upper bound as \(t\to\pm\infty\) matches both constructions, including \(p=0\) and \(p=1\). Exceptional endpoint codings do not affect dimension.

**Shape and maximizer.** The Legendre transform satisfies \(h_p'(c)=-t\) and \(h_p''(c)=-1/P_p''(t)<0\), proving strict concavity and analyticity in the interior. At \(t=0\), \(P_p(0)=\log3\) and \(P_p'(0)=(4p-2)/3\); strict concavity makes this the unique peak, of dimension \(1\).

## Verification
The included standard-library `check.py` replays the exact affine full-branch/winding identities at rational target values, checks 55,986 finite inverse-coded orbit words and 64 independent length-six partition polynomials, and tests the pressure and entropy formulas for boundary and interior frequencies. Execute `python check.py`; its output begins `FINITE_IDENTITIES_OK`. Finite checks do not replace the infinite proof, the strong law, or the dimension argument. The only asymptotic input about forcing is the existence of its plus-symbol frequency.

## Relationship to prior work
Li, Lloyd and Romaña's 2026 arXiv preprint determines \([p-1,p]\) as the Bernoulli model's rotation interval (Example 3.1) and \(\log3\) as its total entropy (Example 4.1); neither quantity determines the dimension of each rotation level. The published *Simultaneous ordered invariant graphs for the full Bernoulli rotation interval* constructs a single equivariant point for each rotation and proves zero entropy on each such singleton. The present claim instead quantifies **all** initial points of a specified rotation, and applies pathwise to every forcing with convergent symbol frequency, without Bernoulli typicality or stationarity. Feng and Shu (2009) developed general conditional random Birkhoff multifractal methods, and Rempe-Gillen and Urbański (2016) developed nonautonomous conformal dimension methods. These provide important general frameworks, but their consulted abstracts do not settle whether the present deterministic-path, explicit closed-form spectrum is covered. This bibliographic residual risk is not a claim that the general methods are inapplicable.

## Limitations
The exact formula uses the three equal-ratio full branches of this particular pair of piecewise-linear lifts. It does not establish an analogous closed formula for general random circle endomorphisms, forcing without a limiting symbol frequency, or variable-slope branches. A deterministic-path formula can be a consequence of more general established thermodynamic formalism; complete priority requires comparison with additional nonautonomous multifractal full texts. No independent audit is claimed.

## References
1. Z. Li, S. Lloyd, S. Romaña, *Rotation Sets and Topological Entropy for Random Circle Endomorphisms*, arXiv:2606.16498v1, first posted 15 June 2026, Examples 3.1 and 4.1. https://arxiv.org/abs/2606.16498
2. *Simultaneous ordered invariant graphs for the full Bernoulli rotation interval*, public research record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-simultaneous-ordered-invariant-graphs-for-the-full-bernoulli-rot--12bec35e4a8d
3. D.-J. Feng, L. Shu, *Multifractal analysis for disintegrations of Gibbs measures and conditional Birkhoff averages*, Ergodic Theory Dynam. Systems 29 (2009), 885–918, doi:10.1017/S0143385708000655.
4. L. Rempe-Gillen, M. Urbański, *Non-autonomous conformal iterated function systems and Moran-set constructions*, Trans. Amer. Math. Soc. 368 (2016), 1979–2017, arXiv:1210.7469.
