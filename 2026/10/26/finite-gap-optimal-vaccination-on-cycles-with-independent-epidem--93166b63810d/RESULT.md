# Finite-gap optimal vaccination on cycles with independent epidemic seeds

## Finding
Let \(C_n\) be the simple undirected cycle with \(n\ge4\). Vaccinate exactly two vertices perfectly before an outbreak. Each remaining vertex independently starts infected with probability \(q\in(0,1)\), and each edge between remaining vertices is independently transmissible with probability \(p\in(0,1)\). Infection reaches precisely the union of transmissible connected components containing at least one initial seed. Let \(N=n-2\) and let \(a,b\ge0\), \(a+b=N\), be the numbers of unvaccinated vertices on the two arcs separating the vaccinees.

Put
\[
 r=p(1-q),\quad A=\frac{1-p}{1-r},\quad B=\frac{pq}{1-r},\quad
 c=1-(1-q)A^2,\quad K=\frac{2(1-q)AB}{1-r},
\]
and define \(f(0)=K\) and, for integers \(s\ge1\),
\[
 f(s)=Kr^s-(1-q)B^2s r^{s-1}.
\]
The expected final number of infected vertices is **exactly**
\[
 E_n(a,b)=cN-2K+f(a)+f(b).
\]
In particular the exact optimal placement for every finite \(n\ge4\) is obtained by minimizing the explicit one-dimensional quantity \(f(a)+f(N-a)\) over integers \(1\le a\le \lfloor N/2\rfloor\); adjacent vaccinees (a zero-length arc) never minimize this expectation.

More strikingly, for each fixed \(0<p,q<1\), write
\[
 \theta(p,q)=\frac{(1-q)\,[pq+2(1-p)]}{q(1-p+pq)},\qquad
 m(p,q)=\lfloor\theta(p,q)\rfloor+1.
\]
There exists \(n_0(p,q)\) such that for **every** \(n\ge n_0(p,q)\), the unique optimal pair of arc lengths, up to exchanging the arcs, is
\[
 \boxed{(a,b)=(m(p,q),\ n-2-m(p,q)).}
\]
Thus the short arc of the optimal two-vaccine placement stabilizes at a finite length as network size diverges, rather than approaching half the cycle length. At fixed \(p\in(0,1)\), \(q\,m(p,q)\to2\) as \(q\downarrow0\).

For the concrete symmetric parameters \(p=q=1/2\), every \(n\ge6\) has optimal shorter arc length \(2\); the sole extra optimum is \((3,3)\) when \(n=8\), tied with \((2,4)\). For \(n=4,5\), the optimal shorter arc length is \(1\). For example, on \(C_{10}\) the optimal lengths \((2,6)\) give expectation \(5755/1024\), strictly below the balanced \((4,4)\) expectation \(45/8\).

## Assumptions and scope
Vaccinated vertices cannot be seeded, infected, or transmit. The graph is a labeled, undirected simple cycle, not a metapopulation mixing matrix. Every surviving edge is an independent one-shot undirected transmission bond; no arbitrary continuous-time SIR recovery distribution or directed infectivity correlation is presumed. The initially infected indicator at each unvaccinated vertex is an independent Bernoulli \(q\), independent of the bonds. The objective is the unconditional expected total number ever infected, including initial seeds. The theorem does not impose an individual-seed constraint: multiple initial seeds may coexist. Both \(p\) and \(q\) are strictly between zero and one and held fixed as \(n\to\infty\). Rotating or reflecting the cycle yields equivalent length pairs.

## Proof
**1. Exact expected epidemic size on a surviving path.** Write \(H_s\) for the expected final infected count on a path of \(s\ge0\) vertices, with \(H_0=0\). Fix a vertex \(i\in\{1,\ldots,s\}\) and let \(X_d\) be the number of consecutively reachable vertices along one side before the first closed bond or the boundary, when \(d\) vertices lie in that direction. A direct geometric-series calculation gives
\[
 \mathbb E[(1-q)^{X_d}]
 =(1-p)\sum_{j=0}^{d-1}[p(1-q)]^j+[p(1-q)]^d=A+Br^d.
\]
The left and right bonds are independent. The vertex \(i\) escapes infection exactly when its entire open cluster contains no initial seed. Therefore
\[
 \Pr(i\text{ escapes})=(1-q)(A+Br^{i-1})(A+Br^{s-i}).
\]
Summing over \(i\), using \(\sum_{i=1}^s r^{i-1}=(1-r^s)/(1-r)\), yields
\[
 H_s=s-(1-q)\left[sA^2+\frac{2AB(1-r^s)}{1-r}+sB^2r^{s-1}\right]
 =cs-K+f(s)
\]
for \(s\ge1\). The definition \(f(0)=K\) makes the final equality hold at \(s=0\) as well. Two vaccinated vertices disconnect \(C_n\) into paths of lengths \(a,b\), so additivity gives \(E_n(a,b)=H_a+H_b\) and the displayed exact formula.

**2. Adjacent vaccinees cannot minimize for \(n\ge4\).** Joining two nonempty paths by one edge cannot decrease the infected set under the natural coupling that shares all their seeds and old edge states. The increase has strictly positive expectation: the new edge opens, at least one seed occurs on one side, and no seed occurs on the other side. Consequently \(H_{a+b}>H_a+H_b\) for \(a,b\ge1\). In particular \(H_N>H_1+H_{N-1}\) for \(N\ge2\), excluding an empty arc and reducing finite optimization to \(1\le a\le\lfloor N/2\rfloor\).

**3. A one-turn defect function and its unique finite minimizer.** Direct subtraction gives, for every integer \(s\ge1\),
\[
 f(s+1)-f(s)=(1-q)B^2(1-r)r^{s-1}\,[s-\theta(p,q)].
\]
The prefactor is positive. Thus \(f\) strictly decreases until it crosses \(\theta\), then strictly increases; at an integer threshold \(\theta=t\) exactly \(f(t)=f(t+1)\). The minimum over positive integers is attained at \(m=\lfloor\theta\rfloor+1\), possibly tied with \(m-1\) if \(\theta\) is a positive integer. Moreover \(f(s)\to0\) exponentially as \(s\to\infty\), and \(f(s)<0\) for all sufficiently large \(s\). Hence \(f(m)<0\).

Let \(a_N\le N/2\) be any minimizing short arc. Choosing the fixed competitor \(a=m\) gives \(f(a_N)+f(N-a_N)\le f(m)+f(N-m)\to f(m)<0\). If \(a_N\to\infty\) along any subsequence, both terms on the left tend to zero, a contradiction. Therefore the minimizing short arc lengths stay bounded. Since \(f(N-a)\to0\) uniformly for bounded \(a\), eventual minimizers must minimize \(f\) on positive integers. If \(\theta\notin\mathbb Z\), that minimizer is uniquely \(m\). If \(\theta=t\in\mathbb Z_{\ge1}\), its only possible competitors are \(t\) and \(t+1=m\). On the eventual increasing tail of \(f\), one has \(f(N-m)<f(N-t)\), so the shorter remaining long path corresponding to \(m\) strictly breaks the tie. This proves eventual uniqueness for all fixed \(0<p,q<1\). The expression for \(\theta\) immediately gives \(q\,m(p,q)\to2\) for fixed \(p<1\) as \(q\downarrow0\).

**4. Exact finite classification at \(p=q=1/2\).** Here \(r=1/4\), \(c=7/9\), \(K=8/27\), \(\theta=5/3\), and
\[
 f(s)=\frac{8-6s}{27\,4^s}\quad(s\ge0),\qquad H_s=\frac{7s}{9}-\frac8{27}+f(s).
\]
Let \(g(s)=4^{1-s}(s-5/3)\) for integers \(s\ge1\). We have \(g(1)<0\), \(g(2)=g(3)>0\), and \(g(s)>g(s+1)\) for \(s\ge3\). For any \(1\le a<\lfloor N/2\rfloor\), the successive difference in the objective \(H_a+H_{N-a}\) has the sign of \(g(a)-g(N-a-1)\). It is strictly negative at \(a=1\) when \(N\ge4\), and nonnegative for all \(a\ge2\). Equality in the latter range occurs only for \(N=6,a=2\). Hence \(a=2\) is optimal for every \(N\ge4\), with one additional optimum \(a=3\) at \(N=6\); at \(N=2,3\), the optimum is \(a=1\). Direct substitution for \(N=8\) gives the stated \(C_{10}\) expectations.

## Verification
The standalone `verify.py` independently enumerates every transmissible-edge configuration for 385 choices of a two-vertex vaccinated subset and cycle size between 3 and 11, at three exact-rational pairs \((p,q)\), comparing the resulting component-based expectation to \(H_a+H_b\) without relying on the path formula to calculate the enumerated result. It also checks the curvature identity
\[
 H_{s+1}-2H_s+H_{s-1}=p^s q(1-q)^{s-1}[2-(s+1)q]
\]
and the exact \(f\)-difference formula at 74 positive path lengths per parameter pair; verifies the \(p=q=1/2\) optimum through \(n=71\); and tests four further large-cycle parameter settings by exact fractions. All checks completed successfully. The proofs above, rather than finite testing, establish the unbounded-size conclusions. Run: `python3 verify.py` with Python 3.8 or newer.

## Relationship to prior work
Li, Zhao, and Zhang (2022) formulate site-bond percolation with vaccination and derive epidemic thresholds and expected outbreak sizes for random network classes. Their published metadata explicitly gives primary MSC 92D30. The current result uses the finite, spatially optimized two-site intervention and independent multi-seed outbreak objective instead; the restricted publisher preview does not permit a whole-paper novelty exclusion. Sartori et al. (2022) analyze structural node-vaccination heuristics and SIR outcomes on empirical networks, rather than the exact two-site cycle model. Delmas, Dronnier, and Zitt (2021/2023) examine optimal vaccination on directed and undirected circles, but optimize the **spectral effective reproduction number** of a metapopulation next-generation matrix, not expected final infections in a seeded bond-percolation process. Holme (2017) gives symbolic SIR-vaccination results for graphs of at most seven vertices, not a general all-cycle classification. Keeling and Shattock (2012) document heterogeneous optimal prophylactic allocation in spatial populations, under a different metapopulation epidemic objective. Thus concentration of vaccines or separation effects in general are not claimed as new; the precise finite-gap optimization theorem under independent multiple seeding is the asserted contribution.

## Limitations
The result does not extend automatically to vaccination of more than two vertices, heterogeneous seeding, directed or dependent transmission, nonperfect vaccines, differing vertex risks, or objectives such as maximum component size, total discounted harm, the dominant eigenvalue, or outbreak probabilities conditional on at least one seed. The existence threshold \(n_0(p,q)\) is proved but not claimed to be supplied by a universal explicit bound. The difference from earlier literature is supported by inspected source portions and searches; equivalent results elsewhere cannot be ruled out. No independent audit has been performed.

## References
1. S. Li, X. Zhao, R. Zhang, *Site-bond percolation model of epidemic spreading with vaccination in complex networks*, Journal of Mathematical Biology 85, 49 (first public online 2022-10-12), DOI 10.1007/s00285-022-01816-1.
2. F. Sartori et al., *A comparison of node vaccination strategies to halt SIR epidemic spreading in real-world complex networks*, Scientific Reports 12, 21355 (2022-12-09), DOI 10.1038/s41598-022-24652-1.
3. J.-F. Delmas, D. Dronnier, P.-A. Zitt, *Optimal vaccination: various (counter) intuitive examples*, first preprint 2021-12-16, arXiv:2112.08756; Journal of Mathematical Biology 86, 26 (2023), DOI 10.1007/s00285-022-01858-5.
4. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (2017); Physical Review E 96, 062305.
5. M. J. Keeling, A. Shattock, *Optimal but unequitable prophylactic distribution of vaccine*, Epidemics 4, 78–85 (2012), DOI 10.1016/j.epidem.2012.03.001.
