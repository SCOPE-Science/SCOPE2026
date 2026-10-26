# Universal size-biased deletion and covariance thresholds for random hypergraph components

## Finding

Let \(H\) be the independent-edge, \(r\)-uniform random hypergraph on \([n]\), with \(n\ge r+1\), \(r\ge2\), and edge probability \(0<p<1\). Write \(I_n\) for its number of isolated vertices. Fix \(r\le s\le n-1\), and let \(Z_s\) be any nonnegative, nonzero-in-expectation weighted count of connected components on exactly \(s\) vertices, where each weight depends only on the component's vertices and internal hyperedges (not on the remainder of \(H\)). All components use ordinary vertex connectedness via intersecting hyperedges.

**Size-biased deletion.** For every real function \(g\) on \(\{0,\ldots,n\}\),
\[
\frac{\mathbb E[Z_s g(I_n)]}{\mathbb E Z_s}=\mathbb E[g(I_{n-s})],
\]
where on the right \(I_{n-s}\) counts isolated vertices in an independent copy of the same \(r\)-uniform binomial model on \(n-s\) vertices (with no edges when fewer than \(r\) vertices remain). Thus, for \(0\le j\le n-s\),
\[
\frac{\mathbb E[Z_s(I_n)_{\underline j}]}{\mathbb E Z_s}
=(n-s)_{\underline j}(1-p)^{\binom{n-s}{r}-\binom{n-s-j}{r}}.
\]
In particular, put
\[
M_n=\binom{n-1}{r-1},\quad
M_{n-s}=\binom{n-s-1}{r-1},\quad
\Delta_s=M_n-M_{n-s}>0.
\]
Then
\[
\boxed{\operatorname{Cov}(I_n,Z_s)=\mathbb E Z_s\bigl[(n-s)(1-p)^{M_{n-s}}-n(1-p)^{M_n}\bigr].}
\]
The sign depends on \(n,r,s,p\), **not** on the connected component shape, edge count, or allowed nonnegative component weights. It changes exactly once, from negative to positive, at
\[
\boxed{p_*(n,r,s)=1-\left(\frac{n-s}{n}\right)^{1/\Delta_s}.}
\]
For fixed \(n,r\), the sequence \(p_*(n,r,s)\) is strictly increasing over \(s=r,\ldots,n-1\). For each fixed \(r,s\), as \(n\to\infty\),
\[
p_*(n,r,s)\sim\frac{(r-2)!}{n^{r-1}},
\qquad
\frac{\operatorname{Cov}(I_n,Z_s)}{\mathbb E Z_s}
\longrightarrow s\exp\left(-\frac{c}{(r-1)!}\right)
\left(\frac{c}{(r-2)!}-1\right)
\]
whenever \(p=c/n^{r-1}\) for fixed \(c>0\). At the other end,
\[
p_*(n,r,n-1)=1-n^{-1/M_n}\sim\frac{(r-1)!\log n}{n^{r-1}}.
\]
The small-component threshold aligns asymptotically with the ordinary giant-component branching threshold; the largest-possible proper component threshold aligns with the isolated-vertex disappearance/connectivity scale. These are **scale comparisons**, not claims of exact finite-size critical probabilities for giant components or connectivity.

## Assumptions and scope

A hyperedge is an unordered set of \(r\) distinct vertices; every potential hyperedge is included independently with probability \(p\). A connected component on \(s\ge r\) vertices has no isolated vertex internally. The count \(Z_s\) can select specific connected isomorphism types, fix the component edge count, count all size-\(s\) components, or give each such component a nonnegative weight. Its weights must not depend on hyperedges outside the component or between the component and its complement. \(\mathbb E Z_s>0\) is assumed for the strict sign assertions. The standard unweighted size-\(s\) count satisfies this for all stated \(n,r,s,p\). Binomial coefficients with nonnegative upper argument smaller than the lower are zero; \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\), with \((a)_{\underline0}=1\).

## Proof

**1. Deletion under a marked component.** Expand \(Z_s\) over vertex sets \(S\subset[n]\) of size \(s\) and connected internal hyperedge configurations \(F\) supported on \(S\). The event that \(S\) is exactly one component with internal configuration \(F\) is the intersection of: (i) the prescribed edges/nonedges entirely within \(S\); and (ii) the absence of every hyperedge meeting both \(S\) and its complement. Both restrictions depend only on hyperedges that intersect \(S\). Hyperedges entirely within \([n]\setminus S\) remain independent Bernoulli-\(p\) variables, regardless of which \(S,F\) occurred. Since \(F\) is connected with \(s\ge r\), all vertices of \(S\) have positive degree. Therefore \(I_n\), on the marked-component event, is exactly the isolate count in the outside induced hypergraph \(H[[n]\setminus S]\), whose law is \(H^r(n-s,p)\). Multiplying by the internal weight, summing over \(F\) and \(S\), and dividing by \(\mathbb E Z_s\) proves the distributional size-bias identity for arbitrary \(g\).

**2. Factorial moments.** In \(H^r(m,p)\), prescribe an ordered \(j\)-tuple of distinct vertices. All of them are isolated precisely when none of the \(\binom{m}{r}-\binom{m-j}{r}\) possible hyperedges meeting that tuple occurs. Summing over the \((m)_{\underline j}\) tuples gives
\[
\mathbb E[(I_m)_{\underline j}]
=(m)_{\underline j}(1-p)^{\binom m r-\binom{m-j}r}.
\]
Apply step 1 with \(m=n-s\). In particular, \(\mathbb E I_m=m(1-p)^{\binom{m-1}{r-1}}\). Subtract \(\mathbb E I_n\,\mathbb E Z_s\) from \(\mathbb E[I_nZ_s]\) to obtain the displayed covariance.

**3. Unique sign crossover.** With \(q=1-p\) and \(\Delta_s>0\), divide the covariance by the strictly positive quantity \(nq^{M_n}\mathbb E Z_s\). The remainder is
\[
\frac{n-s}{n}q^{-\Delta_s}-1,
\]
which is strictly increasing in \(p\in(0,1)\), starting negative and ending positive. Its unique zero is the stated \(p_*\).

**4. Strict ordering in component size.** Define \(a_s=\log(n/(n-s))\). Since \(-\log(1-t)/t\) is strictly increasing on \((0,1)\), \(a_s/s\) strictly increases with \(s\). Pascal's identity yields
\[
\Delta_s=\sum_{j=n-s}^{n-1}\binom{j-1}{r-2}.
\]
These summands are nondecreasing in \(j\), so adding the next smaller term when \(s\) increases makes \(\Delta_s/s\) nonincreasing. Because \(\Delta_s>0\), the ratio \(a_s/\Delta_s\) strictly increases, and hence \(p_*=1-\exp(-a_s/\Delta_s)\) strictly increases.

**5. Endpoint and sparse asymptotics.** For fixed \(r,s\), \(\Delta_s\sim s n^{r-2}/(r-2)!\), \(a_s\sim s/n\), and \(M_n\sim n^{r-1}/(r-1)!\). These give the first threshold expansion. For \(p=c/n^{r-1}\), use \(q^{M_n}\to e^{-c/(r-1)!}\) and \(q^{-\Delta_s}=1+cs/((r-2)!n)+o(1/n)\) in the exact covariance ratio. For \(s=n-1\), \(\Delta_s=M_n\) and \(a_s=\log n\), yielding the other expansion directly.

## Verification

The standalone `verify.py` independently enumerates all labeled hypergraphs for \((n,r)=(3,2),(4,2),(5,2),(4,3),(5,3),(5,4),(6,4)\) at \(p=1/4\) and \(p=2/3\). It computes connected components, their vertex counts and internal hyperedge counts, and compares exact-rational first and second mixed factorial moments against the deletion formula for every present \((s,\text{edge count})\) stratum. It also checks strict ordering of the thresholds at high precision for \(5\le n\le50\) and \(2\le r\le\min(7,n-1)\). Output: `VERIFY_OK 44 component-shape strata 69872 hypergraph states`. The unrestricted claims are proved above; exhaustive finite samples are supplemental checks, not substitutes for proof.

## Relationship to prior work

De Ambroggio and Roberts (2021 preprint) study near-critical component-size tail probabilities in the ordinary independent-edge random graph, with primary MSC 60C05; the present claim instead gives exact mixed moments against **arbitrary component-type weights** at every finite \(n\), and extends to uniform hyperedges. Cooley, Fang, Del Giudice and Kang (2018 preprint) analyze large higher-order components and hypertree structure, but not the displayed isolate/component size-biased law. Last, Nestmann and Schulte (2018 preprint) derive covariance formulas for component counts in a Poisson-vertex random connection model; their model is not a fixed-vertex binomial hypergraph. Pittel (1990) gives limiting Gaussian covariance functions for tree-component counts in sparse ordinary random graphs: the fixed-size graph/tree asymptotic here should **not** be presented as independently novel, and may be a specialization of his results. The distinct candidate contribution here is the finite-\(n\), all-\(r\), all-connected-type deletion identity and its strictly ordered covariance-zero hierarchy, including the interpolation to the near-spanning component endpoint.

## Limitations

The theorem does not apply unchanged to sampling a fixed number of hyperedges, to nonuniform edge probabilities, or to \(j\)-connected components with \(j>1\) without checking a corresponding deletion independence property. It is a moment/size-bias identity and **not** a central limit theorem, giant-component theorem, connectivity theorem, or a claim that an actual phase transition happens exactly at \(p_*\). It does not establish correlation signs, whose normalization can depend on the weighted count. Classical component-count and Palm identities may already imply portions of the result; full text of Pittel's 1990 article was not available in the source inspection, so historical-priority assessment remains provisional. Independent scientific verification has not been performed.

## References

1. U. De Ambroggio and M. I. Roberts, *Unusually large components in near-critical Erdős–Rényi graphs via ballot theorems*, arXiv:2101.05358, first public version 2021-01-13; DOI: 10.1017/S0963548321000584. Primary MSC2020 60C05 in the published record.
2. O. Cooley, W. Fang, N. Del Giudice and M. Kang, *Subcritical random hypergraphs, high-order components, and hypertrees*, arXiv:1810.08107, first public version 2018-10-18; DOI: 10.1137/18M1221527.
3. G. Last, F. Nestmann and M. Schulte, *The random connection model and functions of edge-marked Poisson processes: second order properties and normal approximation*, arXiv:1808.01203, first public version 2018-08-03; DOI: 10.1214/20-AAP1585.
4. B. Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms 1 (1990), 311–342; DOI: 10.1002/rsa.3240010306.
