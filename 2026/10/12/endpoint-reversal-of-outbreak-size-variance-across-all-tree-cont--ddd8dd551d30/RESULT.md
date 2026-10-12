# Endpoint reversal of outbreak-size variance across all tree contact networks

## Finding
Let \(n\ge4\) be an integer and let \(T\) be any finite simple tree on \(n\) vertices. Retain every contact edge independently with transmissibility \(p\in(0,1)\). Choose one index case uniformly from the vertices, independently of the retained edges. Let \(S_T(p)\) be the number of vertices in its retained-edge connected component, including the index case, and let \(V_T(p)=\operatorname{Var}(S_T(p))\).

Define the *wedge count* and *Wiener distance sum*, respectively, by
\[
B(T)=\sum_{v\in V(T)}\binom{\deg_T(v)}2,\qquad
W(T)=\sum_{\{u,v\}\subseteq V(T)}d_T(u,v).
\]
Then, uniformly over every \(n\)-vertex tree,
\[
V_T(p)=\frac{2(n-1)}n p+
\left(\frac{8B(T)}n-\frac{4(n-1)^2}{n^2}\right)p^2+O_n(p^3)
\quad(p\downarrow0),
\]
and
\[
V_T(1-q)=W(T)q+O_n(q^2)\quad(q\downarrow0).
\]
In fact, set \(\delta_n=1/(100n^6)\). For any two \(n\)-vertex trees \(T,U\), **every strict wedge-count ordering controls outbreak variance** when \(0<p<\delta_n\):
\[
B(T)>B(U)\implies V_T(p)>V_U(p).
\]
**Every strict Wiener-index ordering controls outbreak variance** when \(1-\delta_n<p<1\):
\[
W(T)>W(U)\implies V_T(p)>V_U(p).
\]
Consequently, for sufficiently weak transmission the \(n\)-vertex star uniquely maximizes variance and the \(n\)-vertex path uniquely minimizes it, whereas for sufficiently strong transmission the path uniquely maximizes and the star uniquely minimizes. The explicit intervals above work simultaneously for *all* trees of each order. These are strict extremizers up to graph isomorphism.

For the smallest nontrivial order \(n=4\), the only two tree shapes satisfy the additional exact identity
\[
V_{K_{1,3}}(p)-V_{P_4}(p)=
\frac{p^2(1-p)}4(8-6p-5p^2-p^3).
\]
Thus their variance ranking crosses exactly once in \((0,1)\), at the unique positive root of \(8-6p-5p^2-p^3=0\), approximately \(0.7673457409\). The all-order theorem **does not claim** a unique crossover at larger orders or characterize intermediate-transmissibility optimizers.

## Assumptions and scope
All contact graphs are connected, simple, undirected, and acyclic, with exactly \(n\ge4\) vertices and \(n-1\) edges. Edge states are independent Bernoulli variables of common parameter \(p\); the initial infection is a single uniformly random index vertex. The final outbreak is defined to be the full connected cluster reachable by retained edges; this corresponds to the standard bond-percolation version of a single-seed SIR outbreak. No infection times or recovery-time correlations are modeled. The variance includes both random seed placement and independent contact-transmission outcomes. Strict comparisons are asserted only when the named invariant is strictly ordered; equality of those invariants does not imply equal variances at arbitrary transmissibilities.

## Proof
Write \(m=n-1\). For a vertex \(v\), \(S_v=\sum_u I_{v\leftrightarrow u}\), where \(I_{v\leftrightarrow u}\) indicates that every edge in the unique tree path from \(v\) to \(u\) is retained. Hence \(\mathbb E I_{v\leftrightarrow u}=p^{d_T(v,u)}\), and uniform averaging over the seed gives
\[
\mathbb E S_T(p)=1+\frac{2m}{n}p+\frac{2B(T)}n p^2+O_n(p^3),
\]
because there are \(m\) pairs at distance one and \(B(T)\) unordered pairs at distance two. For its square, use the exact identity
\[
\mathbb E S_T(p)^2=\frac1n\sum_{v,u,w}p^{|P(v,u)\cup P(v,w)|},
\]
where \(P(v,u)\) is the edge set of the unique tree path. The union has zero edges only for \(v=u=w\). Each one-edge path contributes six ordered \((v,u,w)\) triples with union that edge. Each length-two path contributes twelve: five with the seed at each endpoint, and two with the seed at the middle. Therefore
\[
\mathbb E S_T(p)^2=1+\frac{6m}{n}p+\frac{12B(T)}n p^2+O_n(p^3).
\]
Subtracting the square of the mean yields the first asserted expansion.

For the second, write \(q=1-p\) and \(D=n-S_T(p)\). With probability \(1-O_n(q)\) every edge survives and \(D=0\). At first order only configurations with exactly one deleted edge contribute. Deletion of an edge whose two components have orders \(s\) and \(n-s\) gives a uniform-seed squared deficit expectation
\[
\frac{s}{n}(n-s)^2+\frac{n-s}{n}s^2=s(n-s).
\]
The contribution from at least two deleted edges is \(O_n(q^2)\). Because \((\mathbb ED)^2=O_n(q^2)\), the variance equals \(q\sum_e s_e(n-s_e)+O_n(q^2)\). Each unordered pair of vertices is separated by precisely as many edges as its graph distance, so \(\sum_e s_e(n-s_e)=W(T)\), proving the second expansion.

For a quantitative uniform remainder, take two independent copies \(X,Y\) of the uniformly seeded open cluster. The variance is the expectation of \(h(X,Y)=S_X^2-S_XS_Y\), with \(|h|\le n^2\), over \(2m\) independent Bernoulli edge variables and two independent seed choices. The \(k\)-th derivative of such a multiaffine Bernoulli expectation is a sum over ordered distinct coordinates of expected \(k\)-fold discrete differences. Each difference has absolute value at most \(2^k n^2\). Therefore
\[
|V_T^{(k)}(p)|\le (4m)^k n^2\qquad (k=2,3;\ 0\le p\le1).
\]
Taylor's theorem applied to the difference for two trees gives, at small \(p\),
\[
\left|V_T(p)-V_U(p)-\frac8n(B(T)-B(U))p^2\right|
\le\frac{64}{3}m^3n^2p^3,
\]
and, at \(q=1-p\),
\[
\left|V_T(1-q)-V_U(1-q)-(W(T)-W(U))q\right|
\le16m^2n^2q^2.
\]
Both invariants are integers. If their difference is nonzero its magnitude is at least one, while \(m<n\). Substitution of \(0<p<1/(100n^6)\), respectively \(0<q<1/(100n^6)\), makes the displayed error strictly smaller than the leading term. This proves the two all-pairs order implications with a common, conservative explicit interval.

It remains to establish the extremizers, independently of probabilistic arguments. Set \(z_v=\deg_T(v)-1\ge0\), so \(\sum_vz_v=n-2\). Then
\[
B(T)=\sum_v\frac{z_v(z_v+1)}2\ge n-2,
\]
with equality only if every degree is at most two, hence exactly for the path; convex concentration yields
\[
B(T)\le\binom{n-1}{2},
\]
with equality only if a single vertex has all excess degree, hence exactly for the star. For the Wiener sum, the edge-cut formula gives \(W(T)=\sum_e s_e(n-s_e)\ge(n-1)^2\), with equality only if every edge is pendant, hence precisely for the star. For the upper bound, remove any leaf \(v\) adjacent to \(x\):
\[
W(T)=W(T-v)+(n-1)+\sum_{u\in V(T-v)}d_{T-v}(x,u).
\]
In a connected graph on \(n-1\) vertices, the sum of distances from one vertex is at most \((n-2)(n-1)/2\), with equality only for a path with \(x\) at an endpoint: order the vertices by nondecreasing distance and note that the \(j\)-th distance is at most \(j\). Induction yields
\[
W(T)\le\frac{n^3-n}{6}=W(P_n),
\]
with equality only for a path. The reversed unique extrema follow.

For \(n=4\), direct enumeration of the three edge states for each graph shape gives the stated factored polynomial. Its cubic factor decreases strictly on \((0,1)\), is positive at zero, and negative at one, proving the unique crossing.

## Verification
The standalone, standard-library-only program `verify.py` independently enumerates every labeled tree with \(4\le n\le6\) using Prüfer sequences, every edge-retention state, and every possible index case. It builds exact-rational outbreak-variance polynomials, checks both expansion coefficients and their extremal implications on the explicit intervals, and verifies the four-vertex factored identity and inequalities at two additional transmission values. Its actual output is:

```text
VERIFY_OK labeled_trees=1437 sizes=4..6 endpoint_order_and_both_taylor_coefficients=exact quartic_difference=exact
```

Run with `python3 verify.py`. The finite enumeration is a reproducibility check, not a substitute for the all-order proof or the uniform analytic derivative estimate.

## Relationship to prior work
Moore and Newman (1999 preprint; 2000 journal publication) relate epidemic transmissibility to bond percolation on small-world contact networks; their setting is not an extremal comparison over all finite trees. Jevtić, Lanchier and La Salle (2020) explicitly study exact first and second cluster-size moments on paths, rings and stars. Their computations cover the object and the special shapes used in the four-vertex example; these moment formulas and that example alone are not asserted to be new. The present structural statement instead compares **every fixed-order tree**, derives the two distinct controlling invariants, and proves explicit uniform transmission neighborhoods with *opposite unique global optimizers*. Lanchier and La Salle's 2021 paper derives bounds for finite regular graphs; nontrivial finite trees are not regular and its theorem does not yield the fixed-order tree ordering. Classical Wiener-index extrema on trees are used and reproved, not claimed as new. Prior full-text access for the 2020 path/star paper was unavailable, so possible broader statements hidden in that source remain a documented originality risk.

## Limitations
The explicit neighborhoods \(1/(100n^6)\) are deliberately conservative, not optimal switching thresholds. The theorem is silent on the extremal tree at intermediate transmissibility, on equality when two nonextremal trees have the same wedge or Wiener index, on directed or cyclic graphs, on heterogeneous transmissibilities, on multiple introductions, and on dependent edge transmission. It concerns outbreak-size variance under the specified stochastic network proxy rather than empirically measured epidemic risk. An accessible full-text comparison against the 2020 path/star study was not completed; originality is assessed with that residual risk, and no independent scientific audit is claimed.

## References
1. C. Moore and M. E. J. Newman, *Epidemics and percolation in small-world networks*, arXiv:cond-mat/9911492 (first public version 1999-11-30); *Physical Review E* 61 (2000), 5678–5682, DOI:10.1103/PhysRevE.61.5678.
2. P. Jevtić, N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on rings, paths and stars*, *Statistics & Probability Letters* 161 (2020), 108714, DOI:10.1016/j.spl.2020.108714.
3. N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on regular graphs*, arXiv:2111.01982 (2021).
4. H. Wang, *The extremal values of the Wiener index of a tree with given degree sequence*, arXiv:0709.1679 (2007).
