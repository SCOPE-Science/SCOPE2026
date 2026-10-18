# Poisson extreme-edge gaps and the sharp mean-width deficit of random symmetric edge polytopes

## Finding

Let \(0<p<1\) be fixed, let \(G_n\sim G(n,p)\) be the binomial random graph, and let
\[
P_G=\operatorname{conv}\left(\{0\}\cup\{\pm(e_i-e_j):\{i,j\}\in E(G)\}\right)
\subset H_n=\left\{x\in\mathbb R^n:\sum_i x_i=0\right\}.
\]
The origin in this definition only makes the empty-graph case well-defined. Write \(w_n\) for Euclidean mean width computed using the unit sphere of the \((n-1)\)-dimensional ambient space \(H_n\).

Take independent Gaussian scores \(Z_1,\ldots,Z_n\), independent of \(G_n\), and put
\[
R_n=\max_i Z_i-\min_i Z_i,\qquad
M_n=\max\left(\{0\}\cup\{|Z_i-Z_j|:\{i,j\}\in E(G_n)\}\right),
\qquad L_n=R_n-M_n.
\]
Let \(\mathcal U=(U_1>U_2>\cdots)\) and \(\mathcal V=(V_1>V_2>\cdots)\) be independent Poisson point processes on \(\mathbb R\), both of intensity \(e^{-x}\,dx\), written in decreasing order. Independently let \(B_{ij}\), \(i,j\ge1\), be independent Bernoulli-\(p\) indicators. Define the finite, nonnegative random variable
\[
D_p=\min_{i,j\ge1:\,B_{ij}=1}
\left[(U_1-U_i)+(V_1-V_j)\right].
\]
Then the scaled Gaussian support loss obeys
\[
\boxed{\sqrt{2\log n}\,L_n\ \Longrightarrow\ D_p,\qquad
\mathbb E[\sqrt{2\log n}\,L_n]\longrightarrow c(p):=\mathbb ED_p.}
\]
For each \(t\ge0\), the almost surely finite count
\[
N_t=\#\{(i,j)\in\mathbb N^2:(U_1-U_i)+(V_1-V_j)\le t\}
\]
gives the complete limiting distribution and its mean:
\[
\boxed{\mathbb P(D_p>t)=\mathbb E(1-p)^{N_t},\quad
\mathbb EN_t=(1+t)e^t,\quad
\mathbb P(D_p=0)=p,\quad
c(p)=\int_0^\infty\mathbb E(1-p)^{N_t}\,dt.}
\]
In particular, the expected *intrinsic Euclidean mean-width deficit* has the sharp asymptotic
\[
\boxed{\lim_{n\to\infty}\sqrt{n\log n}\,
\left[w_n(P_{K_n})-\mathbb E_{G_n}w_n(P_{G_n})\right]
=\sqrt2\,c(p).}
\]
The positive function \(c\) is continuous and strictly decreasing on \((0,1)\), and
\[
\boxed{c(p)\sim\log(1/p)\quad(p\downarrow0),\qquad
c(p)\sim(1-p)/2\quad(p\uparrow1).}
\]
The limit is **annealed** over the random graph. The distributional statement concerns both graph and Gaussian direction randomness, and does not assert a quenched or uniform-in-\(p\) limit.

## Assumptions and scope

All graphs are simple, labeled, and generated with independent edge indicators of common, fixed probability \(p\in(0,1)\). Gaussian coordinates are independent \(N(0,1)\). The normalization \(\sqrt{2\log n}\) applies to the support-value deficit \(L_n\), while \(w_n\) is full directional width \(h_P(u)+h_P(-u)\) averaged over the ambient unit sphere. The theorem takes \(n\to\infty\) with \(p\) fixed, then takes endpoint limits in the resulting coefficient \(c(p)\); it does not interchange these limits.

## Proof

**1. Conditional edge-deletion identity.** For a deterministic vector \(z\) with distinct coordinates, let \(r=\max_i z_i-\min_i z_i\) and, for \(0\le s<r\), let
\[
N_n(s;z)=\#\left\{\{i,j\}:\ |z_i-z_j|\ge r-s\right\}.
\]
The event that all graph edges fail to reach the level \(r-s\) is precisely the absence of all \(N_n(s;z)\) possible extreme-span edges. Consequently
\[
\mathbb P(L_n>s\mid Z=z)=(1-p)^{N_n(s;z)}\qquad(0\le s<r),
\]
with no atom at the boundaries when the Gaussian scores are continuous. In particular, the unique pair joining the maximum and minimum scores is the only pair with deficit zero; thus \(\mathbb P(L_n=0)=p\) for every \(n\ge2\).

**2. Joint extremal point processes and distributional convergence.** Put
\[
a_n=\sqrt{2\log n},\qquad
b_n=a_n-\frac{\log\log n+\log(4\pi)}{2a_n}.
\]
The Gaussian tail asymptotic yields \(n\mathbb P(Z_1>b_n+x/a_n)\to e^{-x}\) for every fixed \(x\). The point processes of upper and reflected lower Gaussian scores, respectively
\[
\sum_i\delta_{a_n(Z_i-b_n)},\qquad
\sum_i\delta_{a_n(-Z_i-b_n)},
\]
converge jointly to independent processes of intensity \(e^{-x}\,dx\). Joint independence follows from the multinomial rare-event limit: a single Gaussian coordinate cannot occupy both disjoint upper and lower extreme tails. For any fixed \(t\), only finitely many extreme upper/lower score pairs can have span within \(t/a_n\) of the full Gaussian range. With probability tending to one these pairs consist of an upper extreme and a lower extreme, not two scores from the same tail. Therefore the point-process convergence and continuity away from equality boundaries imply
\[
N_n(t/a_n;Z)\ \Longrightarrow\ N_t.
\]
There are almost surely no coincident positive pair gaps or exact ties at any prescribed \(t>0\). Apply the conditional identity of step 1, bounded convergence for the integer-valued count, and the fact \(a_nR_n\to\infty\), to obtain
\[
\mathbb P(a_nL_n>t)\longrightarrow \mathbb E(1-p)^{N_t}
\]
for \(t>0\), hence convergence to \(D_p\). At zero the exact atom is \(p\) on both sides; for positive \(t\), the minimum of finitely many locally relevant continuous random gaps has no atom.

**3. Computation of the limiting pair-count intensity.** Condition on the largest point \(U_1=u\). The positive gaps \(U_1-U_i\), \(i\ge2\), form a Poisson process on \((0,\infty)\) with conditional intensity \(e^{-u}e^a\,da\). The variable \(e^{-U_1}\) has exponential distribution of mean one. Thus the expected contribution from the first row and first column of candidate pairs is \(1+2(e^t-1)\). The expected contribution from pairs with both indices at least two is
\[
\int_{\substack{a,b>0\\a+b\le t}}e^{a+b}\,da\,db
=\int_0^t s e^s\,ds=(t-1)e^t+1.
\]
Adding yields \(\mathbb E N_t=(t+1)e^t\). Finiteness of its expectation proves almost-sure local finiteness.

**4. Integrability and convergence of means.** Arrange Gaussian scores as \(Z_{(1)}<\cdots<Z_{(n)}\). From the maximizing vertex \(Z_{(n)}\), inspect its potential edges to \(Z_{(1)},Z_{(2)},\ldots,Z_{(n-1)}\) in this order. Let \(J_n\) be the first present edge's position; put \(J_n=n\) if no edge occurs. Then \(J_n\) is independent of the order statistics, is stochastically bounded by a geometric-\(p\) variable, and
\[
0\le L_n\le Z_{(J_n)}-Z_{(1)}.
\]
We use the uniform Gaussian spacing bound: for an absolute finite constant \(C\), all \(n\ge3\) and \(1\le j\le n\) obey
\[
\mathbb E\big[a_n^2(Z_{(j)}-Z_{(1)})^2\big]\le Cj^2.
\]
To verify it, set \(Y_i=-\log\Phi(Z_i)\), which are independent unit exponentials, and \(g(y)=\Phi^{-1}(1-e^{-y})\). The increasing function \(g\) has derivative the decreasing Gaussian Mills ratio, so \(g'(y)\le C/a_n\) on \(y\ge(\log n)/4\). For \(j\le\sqrt n\), the failure of \(Y_{(n-j+1)}\ge(\log n)/4\) has probability at most \(e^{-c n^{3/4}}\), by a binomial Chernoff bound. On the complementary event, the required difference is controlled by \(C/a_n\) times the sum of the last \(j-1\) independent exponential order-statistic spacings, with rates \(1,\ldots,j-1\), whose second moment is at most \(Cj^2\). The exceptional event is negligible by Cauchy–Schwarz and the fourth-moment Gaussian maximum bound. For \(j>\sqrt n\), use \(\mathbb E(Z_{(n)}-Z_{(1)})^2=O(\log n)\), hence \(a_n^2\mathbb E(\text{range})^2=O((\log n)^2)\le Cj^2\). Adjust \(C\) for finitely many small \(n\). Conditioning on \(J_n\) now gives
\[
\sup_n\mathbb E(a_nL_n)^2\le C\sup_n\mathbb E J_n^2<\infty.
\]
The scaled losses are uniformly integrable, so distributional convergence yields convergence of their expectations. The limiting mean is finite and positive.

**5. Euclidean radial conversion.** Projection of the standard Gaussian vector onto \(H_n\) has independent uniform direction and Euclidean norm, the latter having mean
\[
\rho_n=\mathbb E\|\Pi_{H_n}Z\|=\sqrt2\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}\sim\sqrt n.
\]
Both edge polytopes are centrally symmetric, so the full spherical mean width is \(2\mathbb E M_n/\rho_n\), and for the complete graph it is \(2\mathbb E R_n/\rho_n\). Consequently the expected mean-width deficit equals \(2\mathbb EL_n/\rho_n\), and the asserted \(\sqrt2c(p)\) coefficient follows from \(a_n\sim\sqrt{2\log n}\).

**6. Monotonicity and endpoint behavior.** The first row of the limiting Bernoulli array supplies the upper bound \(D_p\le V_1-V_J\) where \(J\) is geometric with parameter \(p\). The successive descending gaps of the Poisson extreme process are independent exponentials of rates \(1,2,\ldots\); hence
\[
0<c(p)\le\mathbb E H_{J-1}=-\log p.
\]
Monotone coupling of Bernoulli marks with the same uniforms proves strict decrease (the top-top edge is added with positive probability), and dominated convergence on every compact probability interval proves continuity. Write \(q=1-p\). Since \(N_t\ge1\),
\[
\frac{c(p)}q=\int_0^\infty \mathbb E q^{N_t-1}\,dt.
\]
For \(q\le1/2\), the integrand is dominated by \(2\mathbb E(1/2)^{N_t}\), an integrable function by the preceding upper bound. As \(q\downarrow0\), the integrand tends to \(\mathbb P(N_t=1)\). Exactly one pair qualifies if both first positive Poisson gaps exceed \(t\); these gaps are independent exponentials of rate one, so \(\mathbb P(N_t=1)=e^{-2t}\). Thus \(c(p)/(1-p)\to1/2\). Finally, \(1-(1-p)^{N_t}\le pN_t\) and the first-moment formula imply
\[
\mathbb P(D_p\le t)\le p(t+1)e^t.
\]
For each fixed \(\varepsilon>0\), taking \(t=(1-\varepsilon)\log(1/p)\) proves \(\mathbb P(D_p>t)\to1\) as \(p\downarrow0\). Therefore \(c(p)\ge(1-o(1))(1-\varepsilon)\log(1/p)\), while the geometric upper bound is \(\log(1/p)\); let \(\varepsilon\downarrow0\).

## Verification

A standalone standard-library Python checker is provided as `checker.py`. It exhaustively enumerates 1,096 labeled graphs over three distinct rational-score vectors, with dimensions three, four, and five. Using exact rational arithmetic, it checks the conditional distribution identity, the probability of zero support loss, and the conditional expectation identity obtained by integrating the tail. Independent simulations of a finite truncation of the Poisson/Bernoulli limiting model provide nonproof diagnostics at four edge probabilities; run `python checker.py`.

The infinite-dimensional Poisson convergence, the uniform integrability estimate, and the limiting mean-width and endpoint formulas are mathematical consequences of the displayed proof, not inferences from simulation. The checker intentionally does not claim certification of an infinite theorem.

## Relationship to prior work

Braun, Bruegge and Kahle studied facets, degree sequences, and clustering for precisely the random symmetric edge polytope model, including an edge-density facet transition. Their 2022 work motivates studying a different, metric invariant of the same random polytopes. Higashitani, Jochemko and Michałek developed arithmetic invariants of symmetric edge polytopes; Chen, Davis and Korchevskaia studied facets and facet subgraphs. Standard Gaussian extreme-value point-process convergence is used as a proof input, not claimed as new. The finding here concerns the **random support deficit, its full extreme-pair limit law, and the sharp intrinsic mean-width deficit**, not the known descriptions of the polytopes or their face structure.

## Limitations

The graph-edge probability is fixed in \((0,1)\) as the number of vertices tends to infinity. The coefficient endpoint limits do not treat simultaneous sparse or near-complete regimes. Mean width is averaged over graphs, not proved concentrated for a typical graph. The Poisson coupling specifies the limiting law implicitly through an infinite but locally finite random structure; no elementary closed form for \(c(p)\) is asserted. Asymptotic extreme-value arguments require the usual Gaussian tail and Poisson-convergence facts. Bibliographic novelty is based on material inspected and can remain subject to equivalent formulations elsewhere. No independent mathematical validation has been performed.

## References

1. B. Braun, K. Bruegge and M. Kahle, *Facets of Random Symmetric Edge Polytopes, Degree Sequences, and Clustering*, arXiv:2204.07239v1 (initial public version 2022-04-14); published version DOI: 10.46298/dmtcs.9925.
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (2018).
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (2021).
4. S. I. Resnick, *Extreme Values, Regular Variation, and Point Processes*, Springer (1987), for standard point-process methods of extreme-value theory.
