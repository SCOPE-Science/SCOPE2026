# A Lambert-W two-population cover-time crossover on complete split graphs

## Finding
For each integer \(a\ge 2\), form the complete split graph \(G_{a,b}=K_a\vee\overline{K_b}\): \(a\) clique vertices form class \(A\), and \(b\) mutually nonadjacent vertices form class \(B\); every vertex of \(B\) is adjacent to every vertex of \(A\). Run discrete-time simple random walk without holding, from any deterministic initial vertex. Let \(U_A(t)\) and \(U_B(t)\) be the numbers of vertices in the two classes unvisited at times \(0,\ldots,t\), and let \(T\) be the first time when all vertices have been visited.

Suppose \(a\to\infty\), \(b=b(a)\to\infty\), \(b/a\to0\), and
\[
\eta_a=\log a-\left(1+\frac ba\right)\log b\longrightarrow\eta\in\mathbb R.
\]
For fixed real \(x\), put
\[
t_a(x)=\left\lfloor(a+2b-1)(\log b+x)\right\rfloor.
\]
Then the joint law has the **total-variation limit**
\[
\big(U_A(t_a(x)),U_B(t_a(x))\big)
\xrightarrow{\mathrm{TV}}
\operatorname{Pois}(e^{\eta-x})\otimes\operatorname{Pois}(e^{-x}).
\]
In particular,
\[
\Pr\{T\le t_a(x)\}\longrightarrow
\exp\!\left[-(1+e^\eta)e^{-x}\right].
\]
The limit is uniform over the choice of deterministic starting vertex, in the sense that any sequence of starting vertices gives the same limit. A canonical exactly balanced crossover is
\[
b=\left\lfloor\frac{a\,W(\log a)}{\log a}\right\rfloor,
\]
where \(W\) is the positive Lambert function: in this case \(\eta=0\), the two unvisited classes have independent limiting \(\operatorname{Pois}(e^{-x})\) counts, and the cover-time distribution tends to \(\exp(-2e^{-x})\).

## Assumptions and scope
The walk moves at every time step to a uniformly chosen neighboring vertex; samples at successive steps are determined by this Markov transition, not treated as independent coupons. The graph has no loops. The convergence is for fixed \(x\in\mathbb R\) and any integer sequence \(b(a)\) satisfying the three stated conditions. We do not claim an explicit convergence rate, uniformity over growing \(x\), or a result when \(b/a\) tends to a positive constant. The positive Lambert function satisfies \(W(y)e^{W(y)}=y\) for \(y>0\).

## Proof
**Step 1 (exact avoidance reduction).** Fix integers \(k,\ell\ge0\). Mark as forbidden any \(k\) distinct clique vertices and any \(\ell\) distinct independent-set vertices, excluding the starting vertex. Until a forbidden vertex is hit, symmetry reduces the random walk to the substochastic matrix on the remaining classes
\[
Q_{k,\ell}=\begin{pmatrix}
\dfrac{a-k-1}{a+b-1}&\dfrac{b-\ell}{a+b-1}\\[3pt]
\dfrac{a-k}{a}&0
\end{pmatrix}.
\]
If the starting vertex belongs to class \(s\in\{A,B\}\), the exact probability of no forbidden visit by time \(t\) is \(h_s(k,\ell,t)=e_s^\mathsf TQ_{k,\ell}^{t}\boldsymbol1\). The initial visit at time zero is accounted for by excluding the starting vertex. This identity is exact for every admissible finite \(a,b,k,\ell,t\).

**Step 2 (dominant eigenvalue).** Write \(u=(a-k-1)/(a+b-1)\), \(v=(b-\ell)/(a+b-1)\), and \(w=(a-k)/a\). The two eigenvalues of \(Q\) solve \(z^2-uz-vw=0\). At \(k=\ell=0\), they are \(1\) and \(-b/(a+b-1)\). Direct substitution gives
\[
1-u-vw=\frac{ak+a\ell+bk-k\ell}{a(a+b-1)}.
\]
Implicit differentiation of \(z^2-uz-vw=0\) at \((z,k,\ell)=(1,0,0)\) gives
\[
\left.\frac{\partial\lambda_+}{\partial k}\right|_0
=-\frac{1+b/a}{a+2b-1},\qquad
\left.\frac{\partial\lambda_+}{\partial\ell}\right|_0
=-\frac{1}{a+2b-1}.
\]
For fixed \(k,\ell\), the eigenvalue gap is bounded below for all large \(a\) because \(b/a\to0\). Entries and their first derivatives have size \(O(1)\) and \(O(a^{-1})\), respectively, so the implicit second derivatives of \(\lambda_+\) are \(O_{k,\ell}(a^{-2})\). Taylor's formula therefore yields
\[
\lambda_+(k,\ell)=1-\frac{k(1+b/a)+\ell}{a+2b-1}+O_{k,\ell}(a^{-2}).
\]
The other eigenvalue has magnitude \(O(b/a)\). The exact spectral-projector formula \(Q^t=\lambda_+^t(Q-\lambda_-I)/(\lambda_+-\lambda_-)+\lambda_-^t(\lambda_+I-Q)/(\lambda_+-\lambda_-)\) shows, for either initial class, that the dominant-term coefficient in \(h_s\) tends to one. Indeed \(Q\to\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)\) and the positive projector maps \(\boldsymbol1\) to \(\boldsymbol1\). The negative-eigenvalue term is negligible at the times under consideration.

**Step 3 (all mixed factorial moments).** The hypothesis implies \(\log b\sim\log a\), hence \(t_a(x)=O(a\log a)\). For fixed \(k,\ell\), the eigenvalue expansion has negligible accumulated error: \(t_a(x)O(a^{-2})=o(1)\). Consequently,
\[
h_s(k,\ell,t_a(x))=
\exp\left[-\big(k(1+b/a)+\ell\big)(\log b+x)+o(1)\right].
\]
Let \((m)_{\underline{k}}=m(m-1)\cdots(m-k+1)\). If the initial vertex belongs to \(A\), symmetry gives the *exact* mixed factorial-moment identity
\[
\mathbb E\big[(U_A)_{\underline{k}}(U_B)_{\underline\ell}\big]
=(a-1)_{\underline{k}}(b)_{\underline\ell}\,h_A(k,\ell,t_a(x)).
\]
For an initial vertex of \(B\), replace the prefactors by \((a)_{\underline{k}}(b-1)_{\underline\ell}\) and use \(h_B\). In either case, substitution gives
\[
\mathbb E\big[(U_A)_{\underline{k}}(U_B)_{\underline\ell}\big]
\longrightarrow e^{k(\eta-x)}e^{-\ell x}.
\]
These are exactly the mixed factorial moments of two independent Poisson variables with means \(e^{\eta-x}\) and \(e^{-x}\). Convergence of all ordinary mixed moments follows because ordinary powers are finite linear combinations of falling factorials. The limiting independent Poisson law is moment-determinate (its joint moment-generating function exists everywhere), so the multivariate method of moments yields weak convergence. Since all variables take values in \(\mathbb N_0^2\) and the limit is a probability distribution on that lattice, convergence of point probabilities plus tightness upgrades this to total-variation convergence.

**Step 4 (cover time and balanced scaling).** The event \(T\le t\) is precisely \(\{U_A(t)=U_B(t)=0\}\), proving the claimed CDF. Put \(L=\log a\) and \(w=W(L)\). Then \(w e^w=L\), \(w/L\to0\), and for \(b=\lfloor aw/L\rfloor\) one has \(b/a=w/L+O(a^{-1})\) and \(\log b=L-w+o(1)\). Thus \(\eta_a=w^2/L+o(1)\to0\), which proves the balanced crossover.

## Verification
The standalone script `verify_cover_crossover.py` uses exact rational transition propagation on the full graphs for \(3\le a\le6\) and \(2\le b\le5\) and compares it against the two-state reduction for multiple forbidden sets and times. It also symbolically verifies the key eigenvalue identity and first derivatives, and checks numerically that finite-size mixed factorial moments approach the claimed Poisson quantities along the canonical Lambert scaling. Run `python verify_cover_crossover.py` from the directory containing this file; the observed output was `VERIFY_OK 1087 assertions`. Only the analytic argument proves the infinite-family theorem; numerical checks do not establish any asymptotic limit by themselves.

## Relationship to prior work
Cooper, Frieze and Pegden (2018, arXiv:1810.04772), *On the cover time of dense graphs*, give first-order asymptotic estimates for expected cover times of dense graphs in terms of stationary degrees. That result motivates studying a nonregular dense family but does not determine the centered fluctuation law or two-class unvisited counts. Maier and Brockmann (2017, arXiv:1706.02356) and Dong et al. (2022, arXiv:2210.05122) give heterogeneous cover-time approximations or rescaling heuristics from first-passage data; these identify related Gumbel behavior, but assume approximate independence rather than proving the two-class total-variation theorem here. Zlatanov and Kocarev (2009, arXiv:0910.3545) derive a general finite-graph inclusion-exclusion formula for cover times, not the class-resolved asymptotic. Doumas and Papanicolaou (2017, arXiv:1709.04500) analyze two uniform coupon groups with independent draws and fixed asymptotic group-size ratios and per-coupon probability ratio; their model is not this graph walk, and their fixed-parameter asymptotics do not cover the regime \(b/a\to0\) with relative rate tending to one. The proof here instead uses an exact killed-chain reduction for the dependent walk, yielding a joint Poisson law in a sharp triangular critical window.

## Limitations
The result establishes a limit, not a uniform finite-size error bound. The canonical Lambert scaling converges slowly; finite numerical examples need not resemble the limiting balanced values closely. The provided numerical tests are finite checks, while the theorem's full generality depends on the stated spectral perturbation and factorial-moment argument. Search-based historical priority is not definitive; related work on generalized coupon collectors or graph cover-time extremes may contain equivalent formulations. An independent mathematical audit has not been performed.

## References
1. C. Cooper, A. Frieze, W. Pegden, *On the cover time of dense graphs* (first posted 2018-10-10), https://arxiv.org/abs/1810.04772.
2. B. F. Maier, D. Brockmann, *Cover time for random walks on arbitrary complex networks* (2017), https://arxiv.org/abs/1706.02356.
3. J.-Q. Dong, W.-H. Han, Y. Wang, X.-S. Chen, L. Huang, *Universal cover-time distribution of heterogeneous random walks* (first posted 2022-10-11), https://arxiv.org/abs/2210.05122.
4. N. Zlatanov, L. Kocarev, *Random walks on networks: cumulative distribution of cover time* (2009), https://arxiv.org/abs/0910.3545.
5. A. V. Doumas, V. G. Papanicolaou, *Sampling from a mixture of different groups of coupons* (2017), https://arxiv.org/abs/1709.04500.
