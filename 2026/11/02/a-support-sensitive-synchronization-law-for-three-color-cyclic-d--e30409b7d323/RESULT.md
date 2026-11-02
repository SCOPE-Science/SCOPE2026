# A support-sensitive synchronization law for three-color cyclic dynamics on paths

## Finding
For every integer \(n\ge2\), consider the labelled path \(P_n\) with vertex set \(\{0,\ldots,n-1\}\). Under synchronous three-color cyclic cellular automaton (CCA), a vertex of color \(a\in\mathbb Z/3\mathbb Z\) advances to \(a+1\) precisely when one of its path neighbors has color \(a+1\); otherwise it retains \(a\). Let \(T_n\) be the first iteration at which all vertices have the same color, with initially constant configurations assigned \(T_n=0\).

**Deterministic identity.** Lift the initial coloring into integer heights \(S_0=0\) and \(S_{i+1}-S_i\in\{-1,0,1\}\), where the increment represents \(X_0(i+1)-X_0(i)\pmod3\). Let \(A=\{j:S_j=\max_{0\le k<n}S_k\}\). Then
\[
T_n=\max_{0\le i<n}\min_{j\in A}|i-j|.
\]
In particular \(0\le T_n\le n-1\), sharply.

**I.i.d. full-support regime.** If initial colors are independent with probabilities \(p_0,p_1,p_2>0\), summing to one, then as \(n\to\infty\),
\[
\frac{T_n}{n-1}\ \Longrightarrow\ R=\max(U,1-U),\qquad U\sim\operatorname{Beta}(1/2,1/2).
\]
For \(1/2\le r\le1\), \(\Pr(R\le r)=\frac4\pi\arcsin\sqrt r-1\), with CDF zero below \(1/2\) and one above \(1\). Moreover,
\[
\lim_{n\to\infty}\frac{\mathbb ET_n}{n-1}=\frac12+\frac1\pi.
\]
The associated stationary height increments have long-run variance exactly \(18p_0p_1p_2\).

**Two-color regime.** If exactly two colors occur with positive probabilities, write them \(a\) and its cyclic successor \(b=a+1\pmod3\), with \(\Pr(X_0(i)=b)=\theta\in(0,1)\). Then
\[
\frac{T_n}{\log n}\ \xrightarrow{\Pr}\ \frac1{2|\log(1-\theta)|}.
\]
For a one-color distribution \(T_n=0\) identically. Thus an arbitrarily small but fixed probability of the third color changes the synchronization scale from logarithmic to linear.

**Exact sharp-end count.** Under the uniform three-color law, the number of labelled initial colorings having \(T_n=n-1\) is
\[
E_n=6\left([z^0]+[z^1]\right)(z^{-1}+1+z)^{n-2},
\]
where \([z^h]\) extracts the coefficient of \(z^h\). In particular
\[
\Pr(T_n=n-1)\sim\frac{2\sqrt3}{3\sqrt{\pi n}}.
\]

## Assumptions and scope
All updates are simultaneous; path endpoints have only one neighbor, without self-neighbors or wraparound. The deterministic identity holds for every initial coloring and every \(n\ge2\). The distributional limits take \(n\to\infty\) with the indicated fixed product law; the two-color limit does not cover \(\theta\) changing with \(n\). No statement concerns cyclic rings, graph trees with branching, more than three colors, or asynchronous updating.

## Proof
**1. Integer maximum evolution.** Define \(H_i(t)=\max\{S_j:0\le j<n,\ |j-i|\le t\}\). Each \(S_j\) has adjacent increments of magnitude at most one; consequently \(|H_i(t)-H_{i+1}(t)|\le1\). One may see this by projecting every index of one radius-\(t\) window onto the neighboring window, moving it by at most one position and changing its \(S\)-value by at most one. The same holds with the windows exchanged. Also \(H_i(t+1)\) equals the maximum of \(H_i(t)\) and its neighbors' values. Inductively, the color at vertex \(i\) and iteration \(t\) is \(X_t(i)\equiv X_0(0)+H_i(t)\pmod3\): it holds at \(t=0\); because neighboring heights differ by at most one, a vertex has a neighbor of successor color if and only if a neighbor's height is exactly one larger, precisely the condition for the local maximum to increase. Thus the modulo-three update coincides with integer maximum evolution.

If all colors agree at time \(t\), adjacent heights \(H_i(t)\) are congruent modulo three and differ by at most one, so all heights are equal as integers. At any index \(j\in A\), \(H_j(t)=\max S\), and hence all heights agree exactly when each radius-\(t\) window intersects \(A\). This is equivalent to \(t\ge\max_i\min_{j\in A}|i-j|\). An equal-color configuration stays equal, so this proves the deterministic formula and its sharp diameter bound.

**2. Full support gives a Brownian height profile.** Put \(D_i=S_{i+1}-S_i\), and let \(p=(p_0,p_1,p_2)\). The process \((D_i)\) is bounded, stationary, one-dependent, and centered: ordered adjacent colors giving increment \(+1\) and \(-1\) each have probability \(p_0p_1+p_1p_2+p_2p_0\). Its variance is twice this sum; its only nonzero lag covariance is
\[
\operatorname{Cov}(D_0,D_1)=-\sum_{a=0}^2p_a(p_{a-1}-p_{a+1})^2,
\]
with subscripts cyclic. Direct expansion using \(p_0+p_1+p_2=1\) gives the long-run variance
\[
\sigma^2=\operatorname{Var}(D_0)+2\operatorname{Cov}(D_0,D_1)=18p_0p_1p_2>0.
\]
The functional central limit theorem for stationary bounded one-dependent sequences therefore gives convergence of the linearly interpolated process \(S_{\lfloor(n-1)t\rfloor}/(\sigma\sqrt{n-1})\) to standard Brownian motion on \([0,1]\). Brownian motion has almost surely a unique global maximizer \(U\) with the classical arcsine (\(\operatorname{Beta}(1/2,1/2)\)) distribution. At every continuous function with a unique maximum, uniform convergence forces every discrete maximizing site into a vanishing neighborhood of the maximizing time. Consequently the normalized maximizing set converges in Hausdorff distance to \(\{U\}\), and the covering radius from part 1 converges in law to \(\max(U,1-U)\). The explicit CDF follows from the arcsine CDF and symmetry. Since \(0\le T_n/(n-1)\le1\), bounded convergence of expectations in distribution gives the stated mean.

**3. Loss of one color produces a longest-run problem.** With only \(a\) and \(b=a+1\), any \(b\)-site never advances, and every \(a\)-site becomes \(b\) as soon as the infection wave reaches it. Thus if at least one \(b\) occurs, \(T_n\) is the largest graph distance to the set of initial \(b\)-sites; if no \(b\) occurs the state is already constant. Write \(q=1-\theta\). Let \(K_n\) be the length of the longest run of \(a\)-sites. For fixed \(\varepsilon\in(0,1)\), a union bound yields
\[
\Pr\left(K_n\ge(1+\varepsilon)\frac{\log n}{|\log q|}\right)\le n q^{\lceil(1+\varepsilon)\log n/|\log q|\rceil}\longrightarrow0.
\]
Splitting the path into disjoint blocks of length \(\lfloor(1-\varepsilon)\log n/|\log q|\rfloor\) shows that at least one block is entirely \(a\) with probability tending to one: the number of blocks times the probability that a block is all \(a\) diverges. Therefore \(K_n/\log n\to1/|\log q|\) in probability. The two boundary runs have geometrically decaying tails and hence are \(O_{\Pr}(1)\). On each interior run of \(k\) non-\(b\) sites, the maximum distance to a \(b\)-site is \(\lceil k/2\rceil\). The longest run is interior with probability tending to one up to an additive \(O_{\Pr}(1)\) boundary correction. Hence \(T_n=K_n/2+o_{\Pr}(\log n)\), proving the logarithmic law.

**4. Exact endpoint-delay census.** Set \(L=n-1\). The covering radius equals \(L\) if and only if the global maximum of the \(L\)-step height walk occurs uniquely at one of its two endpoints. Under uniform coloring the increments are independent uniform steps in \(\{-1,0,1\}\), and there are three choices of initial color for each gradient word. The number of walks having the left endpoint as unique maximum is the number of length-\(L\) walks with every noninitial partial sum strictly negative. Their first step must be \(-1\); after reflection about height \(-1\), the remaining \(L-1\) steps form an arbitrary nonnegative Motzkin prefix. By the reflection principle for these three-step walks, the number of such prefixes of length \(k\) is \(([z^0]+[z^1])(z^{-1}+1+z)^k\): at each nonnegative endpoint height the bad paths reflect to walks ending two levels lower, and summing over endpoints telescopes to the central two coefficients. The symmetric right-endpoint case gives the same count, and the cases are disjoint. This proves the exact formula. A local central limit estimate for the lazy symmetric walk gives \(([z^0]+[z^1])(z^{-1}+1+z)^k\sim3^k\sqrt{3/(\pi k)}\), yielding the stated probability.

## Verification
Run `python3 verify.py` from the package containing this result. It compares independent direct synchronous simulations against the height-covering-radius formula for every initial gradient word at sizes \(2\le n\le11\), representing all three choices of starting color, and verifies the exact extreme count. Additional two-color deterministic checks test the infection-distance identity, and finite arithmetic tests corroborate the variance expansion. The recorded checks are finite corroboration, not a substitute for the infinite-family and weak-limit arguments above.

## Relationship to prior work
Gravner, Lyu and Sivakoff (arXiv:1610.07320, first public 2016-10-24; later *Annals of Applied Probability* 2018), Lemma 1 and Theorem 3, established a maximum-over-walks excitation representation and synchronization by graph diameter on finite trees. The maximum principle and diameter bound are therefore **prior work**, not new parts of this claim. The distinct quantitative contributions here are the initial-support dichotomy, the exact variance controlling its full-support phase, the explicit arcsine synchronization-time limit, the two-color logarithmic constant, and the extremal finite enumeration. Hellouin de Menibus and Le Borgne (arXiv:1903.12622; later revisions) analyze nonuniform Bernoulli initial states for the one-dimensional infinite cyclic cellular automaton and random-walk encoding, but their inspected results concern infinite-lattice clustering and the limiting local-color distribution, not finite-path synchronization-time laws. Classical Donsker invariance, Lévy's arcsine law, the reflection principle, and longest-run estimates are used as established tools.

## Limitations
This is a deterministic path formula plus two asymptotic regimes for fixed i.i.d. initial laws, not a full closed finite-size distribution at every intermediate time. The crossover when the third color probability depends on path length is unresolved. The results are mathematical deductions using known maximum principles and probability theory; originality is restricted to the quantitative path-specific synthesis, and historical or unindexed equivalent formulations cannot be ruled out by finite search. Independent validation has not been performed.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, "Limiting behavior of 3-color excitable media on arbitrary graphs," arXiv:1610.07320 (first publicly submitted 2016-10-24); *Annals of Applied Probability* 28 (2018), 3324–3357, DOI:10.1214/17-AAP1350. Open full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
2. B. Hellouin de Menibus and Y. Le Borgne, "Asymptotic behaviour of the one-dimensional 'rock-paper-scissors' cyclic cellular automaton," arXiv:1903.12622 (first publicly submitted 2019-03-29); https://arxiv.org/pdf/1903.12622 .
3. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. 1, 3rd ed., Wiley, 1968, chapters on fluctuation theory and walks; classical reflection principle.
4. P. Billingsley, *Convergence of Probability Measures*, 2nd ed., Wiley, 1999; functional central limit theorem and continuous mapping.
