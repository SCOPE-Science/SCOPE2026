# Two-way single-crossing covariance of degree counts and noninduced motifs in independent random graphs

## Finding

Let \(H\) be any finite simple graph with \(k\ge2\) vertices, at least one edge and **no isolated vertices**. Write \(d_v\ge1\) for its vertex degrees, \(\delta=\min_vd_v\), and assume \(n\ge k\). Form \(G\sim G(n,p)\) for \(0<p<1\), independently retaining every edge with probability \(p\). Set \(N=n-1\) and let \(N_r\) count vertices of degree exactly \(r\), \(0\le r\le N\).

For each injection \(\phi:V(H)\hookrightarrow[n]\), fix a deterministic weight \(w_\phi\ge0\), not all zero, and define the (not necessarily induced) weighted copy count
\[
T_H=\sum_\phi w_\phi\prod_{uv\in E(H)}\mathbf 1_{\{\phi(u)\phi(v)\in E(G)\}}.
\]
Put \(e=|E(H)|\), \(\mu=p^e\sum_\phi w_\phi>0\), \(b_r=\binom Nr p^r(1-p)^{N-r}>0\), and \((x)_{\underline d}=x(x-1)\cdots(x-d+1)\). The exact finite-sample covariance law is
\[
\boxed{\ \frac{\operatorname{Cov}(N_r,T_H)}{b_r\mu}=F_{H,r,N}(p):=\sum_{v:d_v\le r}\frac{(r)_{\underline{d_v}}}{(N)_{\underline{d_v}}p^{d_v}}-k.\ }
\]
Here an empty sum means zero. All summands and boundary cases are defined because \(d_v\le k-1\le N\).

This identity yields a **two-way single-crossing classification**:

1. If \(r<\delta\), the covariance is strictly negative for every \(0<p<1\). If \(r=N\), it is strictly positive for every \(0<p<1\).
2. For every \(\delta\le r<N\), there is exactly one \(p_{H,N,r}\in(0,1)\) at which the covariance is zero; the covariance is strictly positive when \(p<p_{H,N,r}\) and strictly negative when \(p>p_{H,N,r}\).
3. Those thresholds strictly increase with the degree being counted: \(p_{H,N,r}<p_{H,N,r+1}\) for \(\delta\le r<N-1\). For each fixed \(p\), the covariance as a function of \(r\) has exactly one transition from negative to positive, possibly with a single zero between them. This is a statement about signs, not monotonicity of the unnormalized covariances.
4. The normalized law and thresholds depend on \(H\) **only through its degree multiset**, not its topology or the nonnegative deterministic embedding weights. If \(H\) is \(d\)-regular, the threshold is explicit:
\[
 p_{H,N,r}=\left(\frac{(r)_{\underline d}}{(N)_{\underline d}}\right)^{1/d},\qquad d\le r<N.
\]

In two regimes the threshold has a quantitative profile. If \(H\) and \(r\ge\delta\) are fixed and \(N\to\infty\), there is a unique positive \(q_{H,r}\) satisfying
\[
 \sum_{v:d_v\le r}\frac{(r)_{\underline{d_v}}}{q_{H,r}^{d_v}}=k,
 \qquad p_{H,N,r}=\frac{q_{H,r}}N+O_{H,r}(N^{-2}).
\]
If \(H\) is fixed, \(u=r/N\in[\varepsilon,1-\varepsilon]\), and \(\varepsilon>0\), then uniformly in the stated range,
\[
\boxed{\ p_{H,N,r}=u-\frac{1-u}{2N}\frac{\sum_vd_v(d_v-1)}{\sum_vd_v}+O_{H,\varepsilon}(N^{-2}).\ }
\]
For a three-vertex path with degree multiset \((1,2,1)\), the \(r=1\) crossing is exactly \(p_{H,N,1}=2/(3N)\). For a triangle, the \(r=1\) covariance is always negative, whereas the \(r=2<N\) crossing equals \(\sqrt{2/[N(N-1)]}\).

## Assumptions and scope

Every edge in \(G(n,p)\) is independent. The motif count is a sum over injective **noninduced** copies (all motif edges must be present; other edges may be present); weights are fixed, deterministic and nonnegative. They may be unequal and may vanish, but not all can vanish. Every vertex of \(H\) is incident to an edge. The conclusions concern integer \(0\le r\le n-1\), real \(0<p<1\), and finite \(n\ge|V(H)|\), without requiring asymptotics except in the two displayed expansions. Motif embedding multiplicities need not be divided by automorphism counts: scaling all weights cancels in the normalized identity.

## Proof

**1. One pinned motif.** Fix an injection \(\phi\), and let \(A_\phi\) be the event that all \(e\) edges of that copy are present. Then \(\Pr(A_\phi)=p^e\). Conditioned on \(A_\phi\), the other Bernoulli edges remain independent with retention probability \(p\). At an image vertex \(\phi(v)\), exactly \(d_v\) distinct incident edges are forced present, so its conditional degree is \(d_v+\operatorname{Bin}(N-d_v,p)\). Every vertex outside the image has degree \(\operatorname{Bin}(N,p)\), because no edge incident to it is among the forced edges. Consequently
\[
\mathbb E[N_r\mid A_\phi]-(n b_r)=\sum_{v\in V(H)}\left(\mathbf 1_{\{r\ge d_v\}}\binom{N-d_v}{r-d_v}p^{r-d_v}(1-p)^{N-r}-b_r\right).
\]
For \(r\ge d\), the ratio of the binomial factor to \(b_r\) is exactly
\[
\frac{\binom{N-d}{r-d}p^{r-d}(1-p)^{N-r}}{\binom Nr p^r(1-p)^{N-r}}=\frac{(r)_{\underline d}}{(N)_{\underline d}p^d}.
\]
Since \(\mathbb E[N_r\mathbf 1_{A_\phi}]=p^e\mathbb E[N_r\mid A_\phi]\), multiplying by \(w_\phi\), summing and subtracting \(\mathbb E[N_r]\mathbb E[T_H]=nb_r\mu\) proves the displayed normalized covariance identity. No independence between overlapping motif occurrences was assumed or used.

**2. Signs and crossings.** All \(d_v\ge1\). If \(r<\delta\), no term enters and \(F=-k<0\). At \(r=N\), \(F=\sum_vp^{-d_v}-k>0\). For \(\delta\le r<N\), at least one positive inverse power of \(p\) enters, so \(F\to+\infty\) as \(p\downarrow0\). Every appearing coefficient \((r)_{\underline d}/(N)_{\underline d}\) is strictly below one (as \(d\ge1\) and \(r<N\)); absent coefficients are zero. Hence \(F(1)<0\). Its derivative is strictly negative on \((0,1)\), since every appearing summand is a positive multiple of \(p^{-d}\). Continuity proves exactly one root and the claimed signs.

For each \(d\ge1\), \((r)_{\underline d}\) is zero for \(r<d\) and strictly increases thereafter. Thus \(F_{H,r,N}(p)\) is constant at \(-k\) for \(r<\delta\) and strictly increasing at each step once \(r\ge\delta-1\). In particular \(F_{H,r+1,N}(p_{H,N,r})>0\), and because the next function decreases strictly with \(p\), its zero satisfies \(p_{H,N,r+1}>p_{H,N,r}\). The endpoint signs ensure exactly one degree-index transition (possibly with a zero). The formula uses only the multiset \(\{d_v\}\) and cancels every weight, establishing universality. If all degrees equal \(d\), the zero equation is \((r)_{\underline d}/[(N)_{\underline d}p^d]=1\), proving the regular formula.

**3. Sparse threshold.** For fixed \(H,r\), the root equation after substituting \(p=q/N\) has the form \(\sum_{v:d_v\le r}(r)_{\underline{d_v}}q^{-d_v}[N^{d_v}/(N)_{\underline{d_v}}]=k\). Its left-hand side decreases strictly from infinity to zero in positive \(q\), and the bracket equals \(1+O_H(N^{-1})\). The limiting positive root is unique with a strictly nonzero derivative. The mean-value theorem (or local implicit-function argument) yields \(q_N=q_{H,r}+O_{H,r}(N^{-1})\), and hence \(p=q_{H,r}/N+O_{H,r}(N^{-2})\).

**4. Dense threshold.** Fix \(\varepsilon>0\), and put \(u=r/N\in[\varepsilon,1-\varepsilon]\). For any fixed integer \(d\ge1\), uniformly on this interval,
\[
 \frac{(r)_{\underline d}}{(N)_{\underline d}}=u^d\left[1-\frac{(1-u)d(d-1)}{2uN}+O_{d,\varepsilon}(N^{-2})\right].
\]
Seek a root \(p=u+\alpha/N+O(N^{-2})\). Expanding \(p^{-d}=u^{-d}[1-d\alpha/(uN)+O(N^{-2})]\), the coefficient of \(1/N\) in \(F\) is \(-u^{-1}[\alpha\sum_vd_v+(1-u)\sum_vd_v(d_v-1)/2]\). It vanishes precisely at \(\alpha=-(1-u)\sum_vd_v(d_v-1)/(2\sum_vd_v)\). The derivative \(\partial_pF\) is bounded above by a negative constant uniformly on this range for sufficiently large \(N\), making the remainder \(O_{H,\varepsilon}(N^{-2})\). This proves the dense formula.

## Verification

The standalone `verify.py` independently enumerates all labelled graphs on four and five vertices, compares exact rational mixed moments against the analytic formula for edges, paths, triangles and stars, and repeats checks with nonuniform deterministic embedding weights. Its additional numerical tests check ordering of degree thresholds, the explicit star crossing, and convergence of the dense expansion. Running `python3 verify.py` produced `PASS: 159 exact finite graph-case/threshold groups` and `PASS: 16 additional asymptotic/root checks`. These finite checks do not replace the unrestricted analytic proof.

## Relationship to prior work

Lin and Reinert (first publicly posted 2009-12-24) study joint degree-count distributions and multivariate approximations. Sah and Sawhney (first publicly posted 2020-06-19) study local limit theorems and graph-factor expansions for subgraph counts. The present object couples a fixed-degree census to noninduced weighted motif counts, establishing the exact signed covariance and two-directional phase diagram, not simply their separate marginal laws or joint normality. Classical random-graph orthogonal-decomposition methods, notably Janson (1994), could yield broader mixed-moment identities; its full monograph was not available for a decisive implication-level inspection. Claims of historical novelty are therefore provisional pending further literature access and independent scrutiny.

## Limitations

The theorem concerns only Erdős–Rényi **independent-edge** graphs, **noninduced** motifs without isolated vertices, and fixed deterministic **nonnegative** embedding weights. Signed weights would void the positive normalization. It does not imply that the unnormalized covariances increase with degree index, nor characterize covariances among different motif counts. The dense expansion is uniform only when the degree fraction stays in a fixed interior interval; the sparse expansion fixes the degree index and motif. A possible equivalent consequence of broader unpublished or inaccessible graph-factor results remains a historical-priority risk.

## References

- Y. Lin and G. Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, arXiv:0912.4812, initial public posting 2009-12-24, https://arxiv.org/abs/0912.4812.
- A. Sah and M. Sawhney, *Local limit theorems for subgraph counts*, arXiv:2006.11369, initial public posting 2020-06-19, https://arxiv.org/abs/2006.11369.
- S. Janson, *Orthogonal decompositions and functional limit theorems for random graph statistics*, Memoirs of the American Mathematical Society, 1994, https://doi.org/10.1090/memo/0534. Full text not inspected; bibliographic comparison only.
