# A sharp near-certain-transmission transition for two epidemic sentinels on a path

## Finding
Let \(P_n\) be a path on \(n\ge4\) vertices, with independently open contacts of probability \(p\in(0,1)\), one uniformly selected initial infection, and two distinct sentinel vertices. Detection means that at least one sentinel lies in the infected component. Define
\[
g_n(p)=p^{n-3}\bigl[1+(n-2)(1-p)\bigr].
\]
There is exactly one \(p_n\in(0,1)\) satisfying \(g_n(p_n)=1\). The pair of endpoints is the unique placement maximizing eventual detection probability when \(p_n<p<1\); when \(p=p_n\), precisely the endpoint pair and its two one-step inward perturbations attain the maximum. For \(0<p<p_n\), the endpoint pair is suboptimal. Moreover,
\[
\lim_{n\to\infty}(n-2)^2(1-p_n)=2.
\]
Thus the endpoint-versus-interior transition is real at every path order, with a high-transmissibility window of width asymptotic to \(2/(n-2)^2\). For \(n=4\), the exact threshold is \(p_4=1/2\).

## Assumptions and scope
The vertices are \(0,1,\ldots,n-1\), in that order. Each of the \(n-1\) edges is independently open with common probability \(p\); a single source is chosen independently and uniformly from all \(n\) vertices. The epidemic infects exactly the source's open-edge connected component (the standard independent-bond final-outbreak representation). Before the source and edges are revealed, choose \(i<j\) as sentinels. The objective \(D_n(p;i,j)\) is the unconditional probability that the outbreak ever infects either sentinel; it is **not** the time to discovery, conditional discovery probability given a large outbreak, or prevention by removing vertices. Even a sentinel that is selected as the source counts as detected.

## Proof
Write \(a=i\), \(b=j-i\), \(c=n-1-j\), with \(a,c\ge0\), \(b\ge1\) and \(a+b+c=n-1\). Conditioning on the uniform source and on the unique path to the sentinels gives the exact quantity
\[
S(a,b,c):=nD_n(p;i,j)
=2+\sum_{r=1}^{a}p^r+\sum_{r=1}^{c}p^r
+\sum_{r=1}^{b-1}\bigl(p^r+p^{b-r}-p^b\bigr).
\tag{1}
\]
The first two geometric sums correspond to sources outside the sentinel interval. For a source strictly between the sentinels, the two possible open paths have probabilities \(p^r\) and \(p^{b-r}\), and their intersection has probability \(p^b\). Formula (1) uses inclusion-exclusion; no independence between these two overlapping detection events is assumed.

When \(a\ge1\), moving the left sentinel one step outward, keeping the right sentinel fixed, changes \(S\) by exactly
\[
S(a-1,b+1,c)-S(a,b,c)=p^b[1+b(1-p)]-p^a.
\tag{2}
\]
When \(c\ge1\), moving the right sentinel one step outward changes \(S\) by \(p^b[1+b(1-p)]-p^c\). Both identities follow by subtracting the finite sums in (1).

For \(0<p<1\), set \(H(a,b)=p^{b-a}[1+b(1-p)]\). For integers \(a\ge1,b\ge1\), it strictly increases with \(a\) and strictly decreases with \(b\). The first assertion is immediate from division by \(p\); for the second, writing \(t=1-p\),
\[
\frac{H(a,b+1)}{H(a,b)}=p\frac{1+(b+1)t}{1+bt}<1,
\]
since the denominator minus its numerator equals \((b+1)t^2>0\). At every permissible outward move \(b\le n-2\) and \(a\ge1\), so
\[
H(a,b)\ge H(1,n-2)=g_n(p),
\tag{3}
\]
with equality only when \((a,b)=(1,n-2)\). The same bound holds with \(c\) replacing \(a\). Equation (2) therefore shows: if \(g_n>1\), all outward moves strictly improve detection; if \(g_n=1\), they improve it except for the last outward step immediately adjacent to an endpoint pair. Moving both sentinels outward successively reaches the endpoints. This proves their uniqueness in the first case and the exact three-way tie in the equality case. If \(g_n<1\), (2) applied to \((a,b,c)=(1,n-2,0)\) shows that the near-end pair \((1,n-1)\) strictly beats \((0,n-1)\). Thus the endpoint pair is not optimal.

For \(n\ge4\), \(g_n(0)=0\), \(g_n(1)=1\), and differentiation gives its unique interior maximum at
\[
p_{\rm peak}=1-\frac1{(n-2)^2}.
\]
The derivative is positive below that point and negative above it. In particular the interior maximum exceeds \(1\), so continuity and strict monotonicity yield precisely one interior root \(p_n\) of \(g_n(p)=1\), with \(g_n(p)<1\) below \(p_n\) and \(g_n(p)>1\) between \(p_n\) and \(1\).

For the limit put \(m=n-2\) and \(p=1-y/m^2\), with fixed \(y>0\). Taylor expansion gives
\[
\log g_n(1-y/m^2)
=(m-1)\log(1-y/m^2)+\log(1+y/m)
=\frac{y-y^2/2}{m^2}+O_y(m^{-3}).
\]
For every fixed \(0<y<2<z\), the displayed expansion makes \(g_n(1-y/m^2)>1>g_n(1-z/m^2)\) for all sufficiently large \(n\). The uniqueness of the interior root traps \(m^2(1-p_n)\) between \(y\) and \(z\), proving the limit \(2\).

For the smallest switching case \(n=4\), \(g_4(p)=p(3-2p)\), so \(p_4=1/2\). The endpoints have
\[
D_4(p;0,3)=\frac{2+2p+2p^2-2p^3}{4},
\]
whereas the near-end pair \((0,2)\) has
\[
D_4(p;0,2)=\frac{2+3p-p^2}{4}.
\]
Their difference equals \(p(1-p)(2p-1)/4\). At \(p=1/4\), the probabilities are \(83/128\) and \(43/64\), respectively; at \(p=3/4\), they are \(121/128\) and \(59/64\), respectively.

## Verification
The accompanying self-contained Python 3 program `verification/verify.py` directly enumerates all \(2^{n-1}\) edge configurations and every source for each sensor pair at \(n=2,\ldots,9\). It makes **360 exact-rational direct comparisons** with (1), tests the optimal endpoint criterion at three rational probabilities, and checks every allowable outward-exchange identity for all \(3\le n\le19\) at four rational probabilities. The reported output is: `PASS: 360 exact percolation enumerations, all threshold comparisons, exchange identities.` The unrestricted statements are consequences of the foregoing analytical proof, not numerical extrapolations.

## Relationship to prior work
Newman (2002) establishes the bond-percolation representation of epidemic final outbreak size, supplying the basic transmission model here. Christakis and Fowler (2010) study empirical friend-based early detection, with lead time rather than this unconditional probability criterion. Holme (2017) computes exact SIR-based surveillance and other node-importance measures on small graphs, with an **expected time to discovery or extinction** objective, not probability of eventual detection, and does not give the all-path-size endpoint threshold and scaling stated here. These differences are substantive objective and parameter differences, not merely vocabulary. No all-size statement of (2)–(3) or the threshold root was identified in the primary material inspected; a possible equivalent from probabilistic coverage or network reliability remains a bibliographic limitation.

## Limitations
Only undirected paths, two perfect sentinels, one uniform source, a common independent bond-transmission probability, and **ever**-detected outcomes are covered. When \(p<p_n\), the theorem proves only that the endpoint pair is not optimal; it does not classify all optimal interior placements. No assertions are made about detection speed, imperfect tests, heterogeneity, competing observation costs, generic trees, or general social and epidemiological networks.

## References
- M. E. J. Newman, *The spread of epidemic disease on networks*, arXiv:cond-mat/0205009 (first submitted 30 April 2002), https://arxiv.org/abs/cond-mat/0205009.
- N. A. Christakis and J. H. Fowler, *Social Network Sensors for Early Detection of Contagious Outbreaks*, arXiv:1004.4792 (first submitted 27 April 2010), https://arxiv.org/abs/1004.4792.
- P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (first submitted 22 August 2017); *Physical Review E* **96**, 062305, https://doi.org/10.1103/PhysRevE.96.062305.
