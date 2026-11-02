# Cycle–leaf dependence in uniform connected unicyclic graphs

## Finding

Let \(G_n\) be uniform over all **simple connected labeled graphs** on \([n]=\{1,\ldots,n\}\) with exactly \(n\) edges, for \(n\ge3\). Write \(C_n\) for the length of its unique cycle and \(L_n\) for its number of degree-one vertices. Put \(m=n-c\) and \(q_n=1-1/n\).

**Exact conditional occupancy law.** For every \(3\le c\le n-1\), conditionally on \(C_n=c\), the variable \(L_n\) has the distribution of the number of empty boxes among \(m\) specified boxes when \(m-1\) independent balls are thrown uniformly into \(n\) boxes. Equivalently, for every \(0\le j\le m\),
\[
\mathbb E\!\left[\binom{L_n}{j}\middle|C_n=c\right]
=\binom mj\left(1-\frac jn\right)^{m-1}.
\]
For \(c=n\), \(L_n=0\) almost surely. The cycle-length law is exactly
\[
\mathbb P(C_n=c)=\frac{n^{n-c}/(n-c)!}{\displaystyle\sum_{r=0}^{n-3}n^r/r!},\qquad 3\le c\le n.
\]

**Strict negative conditional regression.** The conditional mean is
\[
\mu_n(c):=\mathbb E[L_n\mid C_n=c]
=\begin{cases}(n-c)q_n^{n-c-1},&3\le c<n,\\0,&c=n.\end{cases}
\]
It decreases strictly with \(c\) throughout the support. Consequently, for every \(n\ge4\) and every strictly increasing real function \(f\) on \(\{3,\ldots,n\}\),
\[
\operatorname{Cov}(f(C_n),L_n)<0.
\]
For \(n=3\), both statistics are constant and the covariance is zero.

**Independent first-order fluctuations, dependent second-order response.** Let \(H=|Z_1|\), where \(Z_1\sim N(0,1)\), and let \(Z_2\sim N(0,(e-2)/e^2)\) be independent of \(Z_1\). Then
\[
\left(\frac{C_n}{\sqrt n},\frac{L_n-n/e}{\sqrt n}\right)
\xrightarrow{d}(H,Z_2).
\]
Nevertheless the raw covariance does not vanish: 
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,L_n)}{\sqrt n}
=-\frac1{e\sqrt{2\pi}}.}
\]
More precisely, if \(3\le c_n\le n\) and \(c_n/\sqrt n\to x\ge0\), then
\[
\mu_n(c_n)-\frac ne\longrightarrow\frac{1-x^2}{2e}.
\]
This quadratic response produces the negative covariance at order \(\sqrt n\), despite independence of the leading Gaussian and half-normal fluctuations.

## Assumptions and scope

Graphs are undirected, loop-free, without multiple edges, connected, and distinguishably labeled. Exactly \(n\) edges on \(n\) vertices means that there is exactly one simple cycle, of length at least three. A leaf has ordinary graph degree one; vertices on the cycle cannot be leaves. No assertions concern nonuniform graph laws, multigraphs, or disconnected pseudoforests. The finite exact laws include \(n=3\); strict covariance statements require \(n\ge4\). The asymptotics let the total number of vertices tend to infinity.

## Proof

**1. Rooted-forest enumeration.** For a prescribed set \(R\subseteq[n]\) of \(c\) roots, where \(m=n-c\), the number of forests on \([n]\) with exactly \(c\) components, each containing exactly one root, is
\[
F_{n,c}=c\,n^{m-1}.
\]
For \(m=0\) interpret the expression as \(1\). Indeed, the rooted-forest form of the matrix-tree theorem gives the determinant of the principal submatrix of the complete-graph Laplacian indexed by the \(m\) nonroots. That matrix is \(nI_m-J_m\), with eigenvalues \(c\) once and \(n\) with multiplicity \(m-1\). This proves the count for \(m\ge1\); for \(m=0\) the empty forest is unique.

Every unicyclic graph is uniquely a simple cycle together with such a rooted forest attached to its cycle vertices. The cycle can be selected in \(\binom nc(c-1)!/2\) ways. Hence the number with cycle length \(c\) is
\[
\binom nc\frac{(c-1)!}{2}F_{n,c}
=\frac{n!}{2(n-c)!}\,n^{n-c-1}.
\]
Dividing by the sum over \(c\) gives the asserted truncated-Poisson cycle law. In particular, \(M_n=n-C_n\) has a \(\operatorname{Poisson}(n)\) distribution conditioned on \(M_n\le n-3\).

**2. Exact leaf law.** Fix the cycle-root set and suppose \(m\ge1\). For any specified set \(S\) of \(j\le m\) noncycle vertices to be leaves, remove all vertices in \(S\). Every removed vertex must have exactly one edge to a vertex outside \(S\), and no two removed leaves can be adjacent. Conversely, choosing an arbitrary rooted forest on the remaining \(n-j\) vertices, and independently one parent outside \(S\) for each removed vertex, reconstructs exactly the original rooted forests in which all \(S\) are leaves. Their number is
\[
c(n-j)^{m-j-1}(n-j)^j=c(n-j)^{m-1}.
\]
At \(j=m\), the remaining rooted forest has only roots and the same expression still counts the \(c^m\) possible attachments. After division by \(F_{n,c}\),
\[
\mathbb P(\text{every vertex in }S\text{ is a leaf}\mid C_n=c)
=\left(1-\frac jn\right)^{m-1}.
\]
These are precisely the probabilities that \(j\) specified boxes are empty after \(m-1\) independent uniform allocations to \(n\) boxes. By inclusion-exclusion, the full joint law of the leaf indicators (and hence the factorial moments and the law of \(L_n\)) agrees with those vacancy indicators. For completeness the exact point probabilities are
\[
\mathbb P(L_n=\ell\mid C_n=c)
=\frac{\binom m\ell}{n^{m-1}}
\sum_{h=0}^{m-\ell}(-1)^h\binom{m-\ell}{h}(n-\ell-h)^{m-1},
\quad 0\le\ell\le m.
\]
In particular \(\mu_n(c)=m q_n^{m-1}\).

**3. Strict negative regression.** Put \(a_m=mq_n^{m-1}\) for \(m\ge1\), and \(a_0=0\). For \(2\le m\le n-3\),
\[
a_m-a_{m-1}=q_n^{m-2}\left(1-\frac mn\right)>0,
\]
and \(a_1>a_0\). Thus \(c\mapsto\mu_n(c)=a_{n-c}\) is strictly decreasing. For an independent copy \(C_n'\) of \(C_n\),
\[
2\operatorname{Cov}(f(C_n),L_n)
=\mathbb E[(f(C_n)-f(C_n'))(\mu_n(C_n)-\mu_n(C_n'))].
\]
Every integrand is nonpositive, and when \(n\ge4\) two different cycle lengths occur with positive probability, giving a strict inequality.

For an exact mixed-moment identity set \(S_r(z)=\sum_{j=0}^rz^j/j!\) for \(r\ge0\). Directly summing the cycle weights yields, for \(n\ge4\),
\[
\begin{aligned}
\mathbb EC_n&=\frac{n^{n-2}}{(n-3)!S_{n-3}(n)},\\
\mathbb EL_n&=\frac{nS_{n-4}(n-1)}{S_{n-3}(n)},\\
\mathbb E(C_nL_n)&=\frac{n(n-1)^{n-3}}{(n-4)!S_{n-3}(n)}.
\end{aligned}
\]
The last sum telescopes after the change of variable \(j=m-1\). Consequently,
\[
\operatorname{Cov}(C_n,L_n)
=\mathbb EC_n\left[(n-3)q_n^{n-3}-\mathbb EL_n\right]<0.
\]
The strict sign also follows without asymptotics from the conditional regression argument.

**4. Half-normal cycle limit and the quadratic leaf response.** The truncated-Poisson representation and the ordinary Poisson central limit theorem give
\[
\frac{C_n}{\sqrt n}\xrightarrow d H=|N(0,1)|.
\]
All fixed positive moments also converge: after conditioning on an event whose probability tends to \(1/2\), the corresponding centered Poisson moments remain uniformly bounded at the proper powers of \(n\).

Writing \(c=x\sqrt n+o(\sqrt n)\) and expanding \(\log(1-1/n)\), uniformly for \(x\) in compact subsets of \([0,\infty)\), gives
\[
(n-c)q_n^{n-c-1}
=\frac ne+\frac{1-x^2}{2e}+o(1).
\]
There is also a uniform bound \(\left|\mu_n(c)-n/e\right|\le K(1+c^2/n)\) for all supported \(c\) and a numerical constant \(K\): use \(q_n^{n-c-1}=e^{-1+c/n}(1+O(1/n))\) uniformly and \(1-(1-u)e^u=O(u^2)\) on \([0,1]\). Together with the Poisson moment bounds, this proves uniform integrability of the quadratic response. Since \(\mathbb EH^2=1\),
\[
\mathbb EL_n-\frac ne\to0,
\qquad
\frac{\operatorname{Cov}(C_n,L_n)}{\sqrt n}
\to\operatorname{Cov}\left(H,\frac{1-H^2}{2e}\right)
=-\frac1{e\sqrt{2\pi}},
\]
using \(\mathbb EH=\sqrt{2/\pi}\) and \(\mathbb EH^3=2\sqrt{2/\pi}\).

**5. Joint asymptotic independence.** Conditional on \(C_n=c\), couple the leaf count to vacancies among the first \(m=n-c\) boxes after \(b=m-1\) independent uniform draws to \([n]\). Let \(E_b\) be the total number of empty boxes after \(b\) draws and let \(R_b\) be the empty-box count among the remaining \(c\) boxes. Then \(L_n=E_b-R_b\) in this conditional coupling. Since distinct box-vacancy indicators have nonpositive covariance,
\[
\operatorname{Var}(R_b\mid C_n=c)\le c.
\]

For a fixed \(n\), define \(E_j\) using one common sequence of independent draws, set \(q_n=1-1/n\), and write \(E_j^*=E_j-nq_n^j\). If \(B_j\) records whether the \(j\)-th draw hits a previously empty box, then
\[
E_j^*=q_n E_{j-1}^*-\xi_j,
\quad \xi_j=B_j-E_{j-1}/n,
\]
where \((\xi_j)\) is a bounded martingale-difference sequence. Thus, for any \(b=n-O(\sqrt n)\),
\[
E_n^*-E_b^*=(q_n^{n-b}-1)E_b^*
-\sum_{j=b+1}^nq_n^{n-j}\xi_j.
\]
The first term divided by \(\sqrt n\) tends to zero in \(L^2\), because \(\operatorname{Var}(E_b)=O(n)\); the second does likewise, because its variance is at most \(n-b=O(\sqrt n)\). The centered variable \(R_b\) is negligible on the \(\sqrt n\) scale by the previous variance bound. These estimates are uniform for \(c\le K\sqrt n\), for each fixed \(K\).

Finally,
\[
\frac{E_n-nq_n^n}{\sqrt n}
=-\frac1{\sqrt n}\sum_{j=1}^nq_n^{n-j}\xi_j
\xrightarrow d N(0,v),
\quad
v=\int_0^1e^{-2(1-t)}e^{-t}(1-e^{-t})\,dt
=\frac{e-2}{e^2}.
\]
The martingale central limit theorem applies: the increments are bounded and the predictable quadratic variation converges to this integral, since \(E_{\lfloor nt\rfloor}/n\to e^{-t}\) uniformly in probability. Draws in the coupling are independent of \(C_n\). Combining the uniform estimates for \(c\le K\sqrt n\), tightness of \(C_n/\sqrt n\), and the conditional mean expansion proves that the joint limiting pair consists of independent \(H\) and \(Z_2\).

## Verification

The standalone file `check_unicyclic.py` enumerates all simple graphs with \(n\) vertices and \(n\) edges for \(3\le n\le7\), retains connected graphs, identifies the unique cycle and all degree-one vertices, and compares their exact joint counts against the closed inclusion-exclusion formula. It also checks the finite conditional means and their strict monotonicity, the known totals of labeled unicyclic graphs, and illustrative numerical convergence of the covariance coefficient. Running `python3 check_unicyclic.py` from the extracted directory passes all assertions. Exhaustion is only for these finite sizes; the general statements follow from the proof above.

## Relationship to prior work

Ben-Naim and Krapivsky (2004) analyze numbers and size distributions of unicyclic components in an evolving random **multigraph**, allowing self-loops, with a large ambient vertex population. Their full text does not give the exact conditional leaf-vacancy law or the mixed cycle–leaf limits for one uniform **simple connected** unicyclic graph with specified order. Zhang and Zhang (2013) study unicyclic graphs with prescribed numbers of leaves and girth, but their full-text theorems optimize Laplacian coefficients in deterministic graph families; they do not count the conditional random law or establish its dependence properties. The total unicyclic counts agree with OEIS A057500, which is not a joint \((C_n,L_n)\) table. The rooted-forest matrix-tree enumeration and ordinary occupancy central limit theorem are standard ingredients, not asserted to be new. The assessed contribution is the paired exact conditional regression and asymptotic independence with a nonzero second-order covariance coefficient.

## Limitations

The graph model is restricted to uniform labeled simple connected unicyclic graphs. The argument does not prove a full stochastic-order comparison of \(L_n\) at different values of \(C_n\); only strict ordering of conditional means and its consequences for increasing functions of \(C_n\) are established. The joint limit is first order, while the explicit mixed covariance detects a smaller dependence not visible in that limit. A specialized prior bivariate enumeration or a sufficiently general conditioned-graph theorem could imply parts of the statement; independent historical-priority review remains warranted.

## References

1. E. Ben-Naim and P. L. Krapivsky, *Unicyclic Components in Random Graphs*, arXiv:cond-mat/0403453v1, first submitted March 18, 2004. https://arxiv.org/html/cond-mat/0403453v1
2. J. Zhang and X.-D. Zhang, *Laplacian coefficients of unicyclic graphs with the number of leaves and girth*, arXiv:1311.1987v1, first submitted November 8, 2013. https://arxiv.org/html/1311.1987v1
3. OEIS A057500, *Number of connected labeled graphs with \(n\) edges and \(n\) nodes*. https://oeis.org/A057500
4. OEIS A098909, *Triangle of counts of connected unicyclic labeled graphs by unique-cycle length*. https://oeis.org/A098909
