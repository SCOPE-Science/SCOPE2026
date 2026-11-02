# Fixed-count isolation on a circle has a unique spatial sign switch absent under Poissonization

## Finding
For fixed-count random connection graphs on a circle, two specified vertices can have **negatively correlated isolation events even after it is known that they are not directly connected**. In the corresponding Poisson point-process model, that conditioned covariance is always nonnegative. For continuous strictly decreasing radial connection probabilities, the fixed-count covariance switches sign exactly once as tagged-vertex separation increases. For hard-radius geometric graphs this switch, and the fraction of nonadjacent pairs on its positive side, are explicit and sharp.

**Exact conditioned covariance.** For every integer \(n\ge3\) and tagged separation \(d\in(0,1/2]\) with a nonzero probability of no direct tagged edge, let \(m=\int_0^1h(x)\,dx\) and \(C(d)=\int_0^1h(x)h(x-d)\,dx\). Then
\[
\operatorname{Cov}(I_1,I_2\mid X_1=0,X_2=d,E_{12}=0)
=(1-2m+C(d))^{n-2}-(1-m)^{2(n-2)}.
\]
Here \(I_i\) is the indicator that tagged vertex \(i\) is isolated. The sign is exactly that of \(C(d)-m^2\). For continuous strictly decreasing \(H\), there is a unique \(d_*\in(0,1/2)\) with \(C(d_*)=m^2\); the sign is positive at \(d<d_*\), zero at \(d=d_*\), and negative at \(d>d_*\), wherever the no-edge conditioning is defined.

**Poissonization contrast.** With a Poisson(\(\lambda\)) number of additional independent uniform vertices, \(\lambda>0\), the same conditional covariance becomes
\[
e^{-2\lambda m}\bigl(e^{\lambda C(d)}-1\bigr)\ge0.
\]
Thus fixing the total number of additional points can reverse the dependence sign, rather than merely change its magnitude. As a concrete example, set \(H(t)=1-2t\) for \(0\le t\le1/2\), let \(d=1/2\), and compare one fixed background vertex with a Poisson(1) background. The conditioned covariances are respectively \(-1/12\) and \(e^{-5/6}-e^{-1}>0\). The direct tagged edge is absent automatically in this example.

**Hard-radius transition and optimal prevalence.** For \(H(t)=\mathbf 1_{\{t\le r\}}\), \(0<r<1/2\), write \(d_*(r)=2r(1-2r)\). Among two uniformly selected labeled vertices, **conditional on their not being directly connected**, their separation is uniform on \((r,1/2)\); hence the fraction of such separations having positive conditional covariance is
\[
F(r)=\begin{cases} \dfrac{2r(1-4r)}{1-2r},&0<r<1/4,\\0,&1/4\le r<1/2.\end{cases}
\]
The exact maximum, over all hard connection radii, is
\[
\max_{0<r<1/2}F(r)=3-2\sqrt2
\quad\text{at the unique }r=(2-\sqrt2)/4.
\]
For \(r\ge1/4\), every possible nonadjacent tagged pair has **strictly negative** conditioned isolation covariance in the fixed-count model.

## Assumptions and scope
The base space is the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), with circular distance \(\operatorname{dist}_{\mathbb T}(x,y)=\min\{|x-y|,1-|x-y|\}\). There are \(n\ge3\) labeled vertices at iid uniform positions; a regular conditional distribution fixes the positions of vertices 1 and 2 at \(0\) and \(d\) without modifying the iid uniform law of the remaining \(n-2\) positions. Conditional on all positions, distinct possible edges are independent and each is present with probability \(h(x-y)=H(\operatorname{dist}_{\mathbb T}(x,y))\), for measurable \(H:[0,1/2]\to[0,1]\). The additional conditioning \(E_{12}=0\) is imposed only where \(H(d)<1\). No assertion is made about conditioning on this null event when \(H(d)=1\).

The uniqueness theorem additionally assumes \(H\) continuous and strictly decreasing on the entire interval \([0,1/2]\). The hard-kernel theorem is separate and permits a discontinuity. The Poisson comparison uses two deterministically inserted tagged vertices, with an independent Poisson point process of mean \(\lambda\) background points. Isolation includes both the tagged-tagged edge and every tagged-background edge.

## Proof
**1. Exact binomial joint law.** Write \(a=1-m\) and \(b(d)=\int_0^1(1-h(x))(1-h(x-d))\,dx=1-2m+C(d)\). Conditioning on the absence of the tagged-tagged edge does not affect any other edge or position. For each background point, the probability of having no edge to vertex 1 is \(a\), and the probability of having no edge to either tagged vertex is \(b(d)\). Different background points contribute independent factors. Therefore
\[
\Pr(I_1=1\mid E_{12}=0,0,d)=a^{n-2},\qquad
\Pr(I_1=I_2=1\mid E_{12}=0,0,d)=b(d)^{n-2}.
\]
The same marginal applies to \(I_2\). Taking the difference yields the stated covariance. Since \(n-2\ge1\), the map \(u\mapsto u^{n-2}\) is strictly increasing on \([0,1]\). Thus the sign equals that of \(b(d)-a^2=C(d)-m^2\), including equality.

**2. Exactly one switch for strictly decreasing kernels.** Because \(h\) is even on the circle, its periodic autocorrelation \(C(d)\) is continuous and symmetric around \(1/2\). Represent \(h\) by its layer-cake decomposition into centered circular arcs \(\{x:\operatorname{dist}_{\mathbb T}(x,0)<R_s\}\), plus any constant full-circle levels. The length of intersection of any two centered arcs after separating their centers by \(d\in[0,1/2]\) is nonincreasing in \(d\). Consequently \(C\) is nonincreasing. It is in fact **strictly** decreasing for the assumed \(H\): for any \(0\le d_1<d_2\le1/2\), choose equal level-set radii \(R_s=R_t=a\) with \(d_1<2a<d_2\) (possible for \(a<1/4\)). Such arcs intersect at distance \(d_1\) but not at \(d_2\). Strict continuity and decrease of \(H\) give a positive-measure neighborhood of level pairs with this strict difference, proving \(C(d_1)>C(d_2)\).

Fubini gives \(\int_0^1C(d)\,dd=m^2\). Since \(C\) is strictly decreasing on \([0,1/2]\), symmetric on the circle, and continuous, \(C(0)>m^2>C(1/2)\). It therefore crosses \(m^2\) exactly once in \((0,1/2)\). Step 1 gives the covariance sign classification.

**3. Poissonized joint law.** A background point at \(x\) has probability \(h(x)+h(x-d)-h(x)h(x-d)\) of connecting to at least one tagged vertex. Poisson thinning gives probability \(e^{-\lambda(2m-C(d))}\) that no background point connects to either; a single tag is untouched with probability \(e^{-\lambda m}\). Conditioning on the tagged-tagged edge being absent is independent of background edges. Subtraction produces the nonnegative stated expression because \(C(d)\ge0\).

**4. Hard kernels.** The neighborhood of each tag is a circular arc of length \(2r\). For \(0\le d\le1/2\), intersection geometry gives
\[
C_r(d)=\max\{2r-d,0\}+\max\{2r+d-1,0\},\qquad m=2r.
\]
Put \(d_*=2r-4r^2=2r(1-2r)\). This satisfies \(0<d_*\le1-2r\) and \(d_*<2r\). Thus \(C_r(d_*)=2r-d_*=4r^2=m^2\). The arc-overlap function is nonincreasing; on a neighborhood of \(d_*\) its slope is \(-1\), so the sign is strictly positive below \(d_*\), strictly negative above. A hard tagged-tagged edge is absent precisely when \(d>r\), up to a zero-probability equality boundary. The positive-sign interval \((r,d_*)\) is nonempty exactly when \(r<1/4\).

A tagged separation of two independent uniform points on the circle has density \(2\) on \((0,1/2)\). Conditioning on nonadjacency makes it uniform on \((r,1/2)\). Therefore \(F(r)=(d_*-r)_+/(1/2-r)\), giving the displayed piecewise formula. On \((0,1/4)\) its derivative has the sign of \(8r^2-8r+1\), whose only zero in that interval is \(r=(2-\sqrt2)/4\). The endpoints of the interval have fraction zero. Substitution gives the unique global maximum \(3-2\sqrt2\).

**5. Explicit soft example.** For \(H(t)=1-2t\), direct integration gives \(m=1/2\) and
\[
C(d)=\frac{1-6d^2+8d^3}{3},\qquad 0\le d\le1/2.
\]
Its sole crossing of \(m^2=1/4\) is \(d=1/4\). At antipodal distance \(1/2\), \(C=1/6\), and for \(n=3\) the fixed-count covariance is \(1/6-1/4=-1/12\). For a Poisson(1) background it is \(e^{-5/6}-e^{-1}>0\).

## Verification
The standalone script `verify.py` uses only Python's standard library and reports 8,732 successful exact/numerical assertions. It independently computes intersections of lifted arcs and checks the closed arc-overlap formula over rational radius/separation grids; checks exact finite-count covariance sign formulas; enumerates all background-position configurations on a finite circular grid with replacement; uses discrete convolution for strictly decreasing soft profiles; verifies the triangular soft-kernel convolution by exact piecewise Simpson integration; and checks the sharp maximizing radius. The discrete-grid enumeration is a **different finite model** used only as a formula cross-check; it is not a proof of the continuous case. All infinite and all-real-parameter assertions follow from the analytic proof above, not from numerical tests.

Reproduce: `python3 verify.py` (Python 3 standard library, no arguments, no network).

## Relationship to prior work
Wilsher, Dettmann and Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs* (first public preprint July 13, 2020), develop the one-dimensional random connection model and derive an exact **Poisson point-process** two-point isolation probability (their Section 4, Eq. (5)). Their 2022 preprint studies a Poisson limit for the global count of isolated nodes. The Poissonized half of Step 3 is a direct conditional consequence of this established Poisson pair law and is acknowledged as prior mathematical input, not as an independently novel formula. Penrose, *Connectivity of soft random geometric graphs* (first public preprint 2013), treats fixed-count models and general connection kernels in dimensions at least two, with global asymptotic connectivity/isolated-count conclusions; it does not state the one-dimensional finite-size conditioned pair-covariance sign classification.

The contribution claimed here is the fixed-count conditional sign formula together with its **one-switch theorem for strictly decreasing circle kernels**, the exact hard-radius quarter-circle boundary, the sharp spatial prevalence extremum, and the resulting explicit difference from Poissonized spatial dependence. These conclusions concern spatially conditioned *joint* laws, not the previously studied marginal or global isolated-node counts.

## Limitations
This is a finite-size statement for fixed-count iid uniform points on the unit circle, supplemented by a Poissonized comparison with deterministically inserted tags. It does not assert unconditional pair-covariance signs after integrating out separation; does not cover a pair sampled uniformly from the *realized graph's* random set of nonedges; does not assert uniqueness for arbitrary nonmonotone or discontinuous soft kernels; and does not yield connectivity thresholds or higher-dimensional sign-phase classifications. Exact historical priority is not proved. The uninspected portions of wider stochastic-geometry literature could contain an equivalent fixed-count statement. Independent mathematical audit has not been performed.

## References
- M. Wilsher, C. P. Dettmann, A. Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs*, arXiv:2007.06301, initial submission 2020-07-13, Section 4 and Eq. (5).
- M. Wilsher, C. P. Dettmann, A. J. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph*, arXiv:2202.08044, initial submission 2022-02-16, Theorem 1 and Lemma 6.
- M. D. Penrose, *Connectivity of soft random geometric graphs*, arXiv:1311.3897, initial submission 2013-11-15, Annals of Applied Probability 26 (2016), Theorems 2.1–2.3.
