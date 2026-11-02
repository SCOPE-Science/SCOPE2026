# Degree-resolved random-greedy jamming and residual blocked edges in uniform labeled trees

## Finding

Let \(\mathcal T_n\) be a uniform labeled tree on \(n\ge2\) vertices. Give its vertices independent uniform arrival times in \([0,1]\). In increasing arrival-time order, accept a vertex precisely when none of its neighbors has previously been accepted. Let \(I_n\) be the final accepted independent set, \(D_v\) the degree of vertex \(v\), and \(B_n\) the number of edges with neither endpoint in \(I_n\). The latter is the **residual blocked-edge count**, not the number of unoccupied vertices.

The following *single bivariate exact identity* determines the joint degree and acceptance probability of a distinguished vertex, for all finite orders. Write
\[
T(z)=\sum_{n\ge1}\frac{n^{n-1}}{n!}z^n,\qquad T(z)=ze^{T(z)}.
\]
Define the formal exponential generating function
\[
\mathcal A(z,q)=\sum_{n\ge1}\frac{z^n}{n!}
 \sum_{(\tau,r)}\Pr(r\in I(\tau))\,q^{\deg_\tau(r)},
\]
where the inner sum runs over all labeled trees \(\tau\) of order \(n\), with a distinguished root \(r\), and the probability is over their independent arrival times. Then
\[
\boxed{\mathcal A(z,q)=ze^{qT(z)}\int_0^1(1+sT(z))^{-q}\,ds.}
\]
The coefficient of \(z^nq^d\), divided by \(n^{n-1}/n!\), is exactly \(\Pr(D_V=d, V\in I_n)\) for an independent uniformly chosen vertex \(V\). The identity also covers \(n=1\), if the isolated root has degree zero.

In particular, the degree-weighted accepted-root series is
\[
\boxed{H(z):=\left.\partial_q\mathcal A(z,q)\right|_{q=1}
=T(z)\log(1+T(z))-\tfrac12\log^2(1+T(z)).}
\]
Consequently, for every \(n\ge2\),
\[
\boxed{\mathbb E B_n=n-1-
 n\frac{n!}{n^{n-1}}[z^n]H(z).}
\]
Its first two asymptotic terms are
\[
\boxed{\mathbb E B_n=\frac{1-\log2}{2}\,n
 -\frac9{16}+\frac{\log2}{8}+O(n^{-1}).}
\]
In particular \(B_n/n\to(1-\log2)/2\) in probability. Unlike the known \(1/2\) limiting accepted-vertex density, this limit measures the geometry of *edges between two rejected vertices*.

For every fixed integer \(d\ge1\), the joint empirical frequency of accepted degree-\(d\) vertices converges in probability to
\[
\boxed{\frac{e^{-1}}{(d-1)!}\,
 \frac{1-(1-\log2)^d}{d}.}
\]
Equivalently, the limiting probability of acceptance conditional on degree \(d\) is \(\big(1-(1-\log2)^d\big)/d\), strictly decreasing in \(d\). The limiting mean degree of a uniformly sampled accepted vertex is \(1+\log2\), while that of a uniformly sampled rejected vertex is \(3-\log2\).

## Assumptions and scope

Trees are sampled uniformly from the \(n^{n-2}\) labeled unrooted Cayley trees; no distribution is imposed on their shapes beyond uniformity. Arrival times are independent, absolutely continuous, and exchangeable; uniform times provide a convenient parametrization. The greedy rule forbids two accepted adjacent vertices. Expectations average over both the random tree and arrivals. The variables \(z,q\) in the enumerators are formal, and \(\log(1+x)\) denotes its formal power series. For asymptotics, \(n\to\infty\) through all positive integers.

## Proof

**1. Root-recursion generating function.** A rooted labeled tree is a root attached to an unordered set of independently rooted labeled child trees, which gives \(T=ze^T\). Define \(F(z,t)\) by replacing the indicator in the rooted-tree EGF with the probability that its root is accepted by time \(t\). The root has arrival time in \([t,t+dt]\) with density \(dt\); before this time its child subtrees evolve independently and the root will be accepted precisely if no child root has previously been accepted. The corresponding child-class EGF is \(T-F(z,t)\). Therefore
\[
\partial_tF(z,t)=z\exp(T(z)-F(z,t)),\qquad F(z,0)=0.
\]
Since \(ze^{T(z)}=T(z)\), integration yields \(F(z,t)=\log(1+tT(z))\). When a formal weight \(q\) is attached to *each edge incident to the distinguished root only*, the same conditioning gives
\[
\mathcal A(z,q)=z\int_0^1 \exp\big(q[T(z)-F(z,t)]\big)\,dt,
\]
which proves the bivariate identity. In particular its degree-\(d\) slice is
\[
[z^nq^d]\mathcal A(z,q)=\frac1{d!}[z^{n-1}]
\int_0^1\big(T(z)-\log(1+tT(z))\big)^d\,dt.
\]
All integrals here integrate polynomials in arrival-time variables coefficientwise, and thus yield rational coefficients.

**2. Edge identity and all-order coefficients.** Differentiation with respect to \(q\) at \(q=1\), followed by \(x=1+tT\), gives
\[
H(z)=T\int_0^1\frac{T-\log(1+tT)}{1+tT}\,dt
=T\log(1+T)-\tfrac12\log^2(1+T).
\]
Because \(I_n\) is independent, every edge incident to an accepted vertex is counted *exactly once* in \(\sum_{v\in I_n}D_v\). Thus, pathwise,
\[
B_n=(n-1)-\sum_{v\in I_n}D_v.
\]
The uniform rooted-tree count is \(n^{n-1}\); coefficient extraction from \(H\), averaging a random distinguished root and multiplying by \(n\), proves the exact finite-order formula for \(\mathbb E B_n\).

**3. Finite-size constant.** Let \(h(u)=u\log(1+u)-\tfrac12\log^2(1+u)\). The standard square-root expansion of \(T(z)\) at its unique dominant singularity \(z=e^{-1}\), followed by singularity transfer, gives for functions \(g\) analytic on a complex neighborhood of the image of the dominant dented domain (as \(h\) is):
\[
\frac{[z^n]g(T(z))}{[z^n]T(z)}
=g'(1)-\frac{g''(1)+g'''(1)/2}{n}+O(n^{-2}).
\]
The relation follows by subtracting \(g'(1)T(z)\), noting that the first remaining *nonanalytic* term is the cube of \(\sqrt{2(1-ez)}\), and comparing its coefficient with that of the square-root term of \(T\). For \(g=h\), direct differentiation gives
\[
h'(1)=\frac{1+\log2}{2},\quad
h''(1)=\frac12+\frac{\log2}{4},\quad
h'''(1)=-\frac18-\frac{\log2}{4}.
\]
Hence the ratio is \((1+\log2)/2-(7/16+\log2/8)/n+O(n^{-2})\); substituting it in the exact expression for \(\mathbb E B_n\) proves the announced finite-size correction. The error term comes from the next odd singular powers and is not inferred from numerical data.

**4. Degree profile and concentration.** For fixed \(d\ge1\), write the degree-\(d\) generating series from step 1 as a function of \(u=T(z)\) using \(z=ue^{-u}\). Since \(\partial_u(ue^{-u})=0\) at \(u=1\), its leading singular coefficient ratio to \(T\) equals
\[
\frac{e^{-1}}{(d-1)!}\int_0^1
\frac{(1-\log(1+t))^{d-1}}{1+t}\,dt
=\frac{e^{-1}}{(d-1)!}\frac{1-(1-\log2)^d}{d}.
\]
The ordinary degree distribution of a random distinguished Cayley vertex is exactly \(1+\operatorname{Bin}(n-2,1/n)\), converging to \(1+\operatorname{Pois}(1)\). Dividing joint by marginal probabilities yields the conditional expression. The integral representation makes strict decrease with degree immediate.

For empirical convergence, the marked uniform Cayley trees converge locally, in probability, to the size-biased critical Poisson Galton--Watson tree. Root greedy acceptance is approximable by a radius-\(R\) marked neighborhood: a discrepancy requires a strictly decreasing arrival-time path of length \(R\). The limiting tree has expected generation size \(R+1\), making this event at most \((R+1)/(R+1)!=1/R!\). Local-pattern counts concentrate by the two-root local limit, so every fixed-degree accepted-vertex fraction concentrates around the coefficient limit above. The degree tails are uniformly integrable because \(D_V=1+\operatorname{Bin}(n-2,1/n)\), allowing passage to the degree-weighted sum and hence to \(B_n/n\). Finally summing the degree-weighted joint profile gives \(\mathbb E[D_V\mathbf 1_{V\in I_n}]\to(1+\log2)/2\) and \(\Pr(V\in I_n)\to1/2\), yielding the two conditional mean degrees.

## Verification

The standard-library checker `checker.py` derives formal bivariate coefficients, independently enumerates every labeled Cayley tree of orders \(2\) through \(7\) using Prüfer sequences, and solves random-greedy root acceptance by a first-pick recursion on vertex subsets. It also directly enumerates all priority permutations for every tree of orders \(2\) through \(6\) to count residual blocked edges, independently of the root recursion. All 38 rational-exact equalities passed. For instance, \(\mathbb EB_4=3/16\), \(\mathbb EB_5=8/25\), \(\mathbb EB_6=305/648\), and \(\mathbb EB_7=1488/2401\) (the last is from the all-tree coefficient/root calculation). These finite checks verify the formulas in their tested ranges but do not replace the all-size generating-function and asymptotic proofs.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli, and Shikhelman establish local-limit/branching-process methods for random greedy independent sets; their size-biased Poisson calculation gives the already-known limiting accepted-vertex fraction \(1/2\). Contat proves a much stronger exact scalar law and Gaussian fluctuations for the *number* of accepted vertices of uniform Cayley trees. The present exact bivariate root-degree enumerator and residual blocked-edge finite-size expectation concern different statistics and do not follow from the scalar cardinality law. The degree-only limiting expression is compatible with the known two-type branching-process ODE and is not asserted as an independent general ODE theory. Penrose--Sudbury provide general graph forward equations and Bethe-lattice pair correlations; they are conceptual antecedents but do not provide the finite labeled-Cayley-tree bivariate enumerator or its edge-count coefficient. This distinction is the essential priority comparison, rather than mere differences in paper titles.

## Limitations

The result concerns Cayley-uniform labeled trees and iid exchangeable arrival times. It does not extend the same coefficients to conditioned degree sequences, recursive trees, configuration-model trees, or arbitrary finite graphs. The analytical formula is proven, but independent mathematical review and a definitive global historical-priority determination have not been performed. Framework-level equations in earlier work could potentially permit a separate derivation of some displayed asymptotic corollaries; the distinctive exact finite-order bivariate enumerator and edge correction are the claimed contribution.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216, first posted 2019-07-16, especially Sections 5 and 6.3. https://arxiv.org/abs/1907.07216
2. A. Contat, *Surprising identities for the greedy independent set on Cayley trees*, arXiv:2103.03800, first posted 2021-03-05, especially Sections 3 and 4. https://arxiv.org/abs/2103.03800
3. M. D. Penrose, A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Ann. Appl. Probab. 15 (2005), 853--889. https://arxiv.org/abs/math/0503519
4. H. G. Dehling, S. R. Fleurke, C. Külske, *Parking on a Random Tree*, J. Stat. Phys. 133 (2008), 151--157. https://arxiv.org/abs/0711.4061
5. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393--401. https://doi.org/10.1137/0402034
