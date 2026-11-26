# Size-biased deletion and ordered covariance thresholds for isolated vertices and components in uniform random hypergraphs

## Finding and scope

Let $H$ be the independent-edge $r$-uniform hypergraph on $[n]$, where $r\ge2$, $n\ge r+1$, and each potential edge is present with probability $0<p<1$. Use ordinary vertex connectivity via intersecting edges. Fix $r\le s\le n-1$. Let $Z_s$ be a weighted count of components on exactly $s$ vertices, with finite nonnegative weights depending only on the marked component's labels and internal edges and with $\mathbb E Z_s>0$. Write $I_m$ for the isolate count of the same model on $m$ vertices (edgeless for $m<r$), $q=1-p$, $M_m=\binom{m-1}{r-1}$ for $m\ge1$, and $\Delta_s=M_n-M_{n-s}$. Use the usual zero convention for binomial coefficients with insufficient upper index.

For every real function $g$ on $\{0,\ldots,n\}$,
\[
\frac{\mathbb E[Z_s g(I_n)]}{\mathbb E Z_s}=\mathbb E[g(I_{n-s})].
\]
For $0\le j\le n-s$, the corresponding mixed falling factorial moment divided by $\mathbb E Z_s$ is $(n-s)_{\underline j}q^{\binom{n-s}{r}-\binom{n-s-j}{r}}$, where $(m)_{\underline 0}=1$. In particular,
\[
\frac{\operatorname{Cov}(I_n,Z_s)}{\mathbb E Z_s}=(n-s)q^{M_{n-s}}-nq^{M_n}.
\]
The covariance switches sign once, from negative to positive, at $p_*(n,r,s)=1-((n-s)/n)^{1/\Delta_s}$, and $p_*$ is strictly increasing in $s$ for fixed $n,r$. For fixed $r,s$ and $n\to\infty$,
\[
p_*\sim (r-2)!n^{1-r},\qquad
\left.\frac{\operatorname{Cov}(I_n,Z_s)}{\mathbb E Z_s}\right|_{p=c/n^{r-1}}
\longrightarrow s e^{-c/(r-1)!}\left(\frac{c}{(r-2)!}-1\right)\quad(c>0).
\]
For $s=n-1$ and fixed $r$, $p_*=1-n^{-1/M_n}\sim(r-1)! n^{1-r}\log n$. The two endpoints of the size hierarchy thus recover the scales of the giant-component branching threshold and isolated-vertex disappearance, respectively. These are scale comparisons, not exact phase-transition thresholds.

## Proof

Expand $Z_s$ by marked vertex sets $S$ and connected internal configurations on $S$. On such a marked event, only edges meeting $S$ have been conditioned on: no edge crosses its boundary, and the internal configuration is specified. The completely outside edges remain independent Bernoulli variables with parameter $p$. Each vertex in the connected marked component has positive degree, so $I_n$ on that event is exactly the isolate count on the complement. This conditional law depends on neither $S$ nor its internal shape, which gives the first identity by weighting and summing. For $j$ fixed distinct ordered vertices of the complement to be isolated, all $\binom{n-s}{r}-\binom{n-s-j}{r}$ edges meeting them must be absent. Summation gives the factorial moment. Taking $j=1$ and subtracting the original mean times $\mathbb E Z_s$ proves the covariance identity.

The sign is the sign of $((n-s)/n)q^{-\Delta_s}-1$, since the omitted factor is positive. As $p$ increases from 0 to 1 this expression increases from $-s/n$ to infinity, yielding the unique root. Write $a_s=\log(n/(n-s))$. Then $a_s/s$ strictly increases in $s$ because $-\log(1-x)/x$ strictly increases for $0<x<1$. Pascal's identity gives $\Delta_s=\sum_{j=n-s}^{n-1}\binom{j-1}{r-2}>0$. Thus $\Delta_s/s$ is a mean of nondecreasing summands, with each successive increase in $s$ appending the next smaller or equal term. The ratio $a_s/\Delta_s$ strictly increases, as does $p_*=1-e^{-a_s/\Delta_s}$.

For fixed $r,s$, $a_s\sim s/n$, $\Delta_s\sim s n^{r-2}/(r-2)!$, and $M_n\sim n^{r-1}/(r-1)!$. These imply the first threshold asymptotic. When $p=c/n^{r-1}$, $q^{M_n}\to e^{-c/(r-1)!}$ and $q^{-\Delta_s}=1+cs/((r-2)!n)+o(1/n)$. Substitute into $q^{M_n}[(n-s)q^{-\Delta_s}-n]$ to get the normalized covariance limit. For $s=n-1$, $a_s=\log n$ and $\Delta_s=M_n$, giving the stated near-spanning threshold.

## Verification and limitations

The accompanying `verify.py` from the original source package enumerates small labeled graphs and uniform hypergraphs, compares first and second mixed factorial moments in component-size and edge-count strata, and checks the ordering on a finite parameter grid. The recorded run is supplemental; the proof applies to unrestricted finite parameters and to all allowed weights. The result does not give the magnitude of Pearson correlation without second moments of the weighted count. Its sign, however, is the covariance sign: $I_n$ is nonconstant (empty versus one-edge graph), and $Z_s$ is nonconstant because it vanishes on the empty hypergraph and is positive with positive probability. The proof uses independent edges and ordinary vertex components and does not assert an analogue for fixed-edge-count models, nonuniform probabilities, or higher-order connectivity.

## Relationship to prior work

The ordinary graph covariance formula and ordering follow by setting the first component size to one in *Shape-universal covariance sign reversals for random graph components*, Resultary record `2026/10/18/...--00c844d9af13` (equations (1)–(2)); summing marked events also allows label-dependent weights in that case. No independent novelty is asserted for those graph-case covariance results or the fixed-size sparse graph/tree asymptotic. Pittel, *On tree census and the giant component in sparse random graphs* (1990), DOI `10.1002/rsa.3240010306`, is a classical asymptotic precedent. Last, Nestmann and Schulte, arXiv:1808.01203, §3, give component-count Palm moment formulas for a Poisson spatial graph, not this fixed-vertex uniform model. Cooley, Fang, Del Giudice and Kang, arXiv:1810.08107, study the size and structure of components in sparse uniform hypergraphs. The distinct scope here is the full isolate deletion law under locally weighted component marks and the finite ordered threshold law for $r\ge3$ connecting the two scales. The comparison does not establish historical priority.
