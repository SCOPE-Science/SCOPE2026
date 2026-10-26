# An exact loop–cycle covariance spectrum in the configuration model

## Finding

In the uniform labeled-half-edge pairing model with nonnegative degree sequence \(d_1,\ldots,d_n\), let \(L\) denote the total number of loops, and let \(C_r\) denote the number of simple-vertex \(r\)-cycles with multiplicity, for \(3\le r\le n\). Put \(Q=\sum_i d_i\), \(A=\sum_i\binom{d_i}{2}\), and, with \(\Gamma_r\) the undirected simple \(r\)-cycles on \(\{1,\ldots,n\}\), define

\[
 w_\gamma=\prod_{v\in\gamma}d_v(d_v-1),\quad
 B_r=\sum_{\gamma\in\Gamma_r} w_\gamma,\quad
 S_r=\sum_{\gamma\in\Gamma_r}w_\gamma\sum_{v\in\gamma}(2d_v-3),\quad
 P_s(Q)=\prod_{j=0}^{s-1}(Q-2j-1).
\]

Whenever \(Q\) is even and \(Q\ge 2r+2\), the exact covariance is

\[
 \boxed{\operatorname{Cov}(L,C_r)=
 \frac{2rAB_r/(Q-1)-S_r}{P_{r+1}(Q)}.}
\]

For \(Q=2r\), the covariance is \(-AB_r/((Q-1)P_r(Q))\): any full-length cycle consumes every half-edge and excludes loops. There are no claims about \(Q<2r\), when \(C_r=0\).

For \(d_i=d\ge2\), \(Q=nd\) even, and \(n\ge r\ge3\), if \(nd\ge2r+2\), this becomes

\[
\boxed{\operatorname{Cov}(L,C_r)=
\frac{(n)_{\underline r}[d(d-1)]^r\bigl(nd(2-d)+2d-3\bigr)}
{2(nd-1)^2\prod_{j=1}^r(nd-2j-1)}.}
\]

Consequently it is strictly **positive** at degree \(d=2\) for every \(3\le r<n\), strictly **negative** for \(d\ge3\), and strictly **negative** at the boundary \(d=2\), \(r=n\). The transition is uniform across all nonspanning lengths. With \(d,r\) fixed and \(n\to\infty\), along admissible parities,

\[
\operatorname{Cov}(L,C_r)=\begin{cases}
\frac{1}{8n^2}+O_r(n^{-3}),&d=2,\\[2pt]
-\frac{(d-2)(d-1)^r}{2dn}+O_{d,r}(n^{-2}),&d\ge3.
\end{cases}
\]

## Assumptions and scope

The experiment chooses a uniformly random perfect matching of \(Q\) **distinguishable half-edges**, grouped into vertices of sizes \(d_i\). A loop pairs two half-edges from the same vertex. Write \(M_{uv}\) for the number of cross-vertex edges joining distinct vertices \(u,v\). Each undirected simple vertex-cycle \(\gamma=(v_1,\ldots,v_r)\) contributes \(\prod_{j=1}^r M_{v_jv_{j+1}}\), with cyclic indexing, to \(C_r\). Thus a parallel-edge choice gives a separate cycle, but cyclic shifts and reversal do not. The model is not uniform over unlabeled multigraphs, and it is not conditioned to be simple. The nonnegative-degree result allows isolated vertices and zero \(B_r\); sign assertions require the positive regular degrees and listed ranges.

## Proof

For a specified distinct-stub \(r\)-cycle \(\gamma\), each of its \(r\) prescribed matching pairs occurs with probability \(P_r(Q)^{-1}\). At each vertex of \(\gamma\), the two incident oriented edges choose an ordered pair of distinct half-edges. Summing over undirected cycles gives

\[
\mathbb E[C_r]=\frac{B_r}{P_r(Q)},\qquad
\mathbb E[L]=\frac{A}{Q-1}.
\]

Fix a particular realized stub-cycle \(\gamma\). It occupies two half-edges at each of its vertices. The number of possible loop pairs among the remaining half-edges is exactly

\[
 A-\sum_{v\in\gamma}\left[\binom{d_v}{2}-\binom{d_v-2}{2}\right]
 =A-\sum_{v\in\gamma}(2d_v-3).
\]

Provided \(Q\ge2r+2\), the conditional probability for each such remaining loop pair is \((Q-2r-1)^{-1}\). Therefore the exact mixed moment is

\[
\mathbb E[LC_r]=\frac{AB_r-S_r}{P_{r+1}(Q)}.
\]

Subtracting \(\mathbb E[L]\mathbb E[C_r]\), and observing \(P_{r+1}(Q)=P_r(Q)(Q-2r-1)\), yields the first boxed formula. If \(Q=2r\), a realized \(r\)-cycle uses all available half-edges; hence \(LC_r=0\) identically, giving the asserted boundary.

For degree \(d\) the number of undirected simple vertex-cycles is \((n)_{\underline r}/(2r)\). Each has weight \([d(d-1)]^r\) and deletion toll \(r(2d-3)\). Thus \(B_r=(n)_{\underline r}[d(d-1)]^r/(2r)\), \(S_r=r(2d-3)B_r\), and \(A=nd(d-1)/2\). Inserting these into the general formula and simplifying proves the regular-degree identity. All denominator factors are strictly positive in its stated domain. The remaining sign factor is \(nd(2-d)+2d-3\): at \(d=2\) it equals \(1\); for \(d\ge3\), \(n\ge3\) it is strictly negative. The excluded spanning degree-two case is the already proved full-half-edge boundary. Fixed-\(d,r\) expansions of numerator and factors \(nd-O_{d,r}(1)\) give the two limits. No asymptotic step is needed for the finite formula or sign classification.

As illustrative exact values, \(\operatorname{Cov}(L,C_3)=32/245\) for \((n,d)=(4,2)\), whereas it equals \(-2592/4235\) for \((n,d)=(4,3)\). At \((n,d,r)=(5,2,5)\) the boundary covariance is \(-128/567\).

## Verification

The self-contained file `verify.py` enumerates perfect matchings of labeled half-edges, constructs loop and cycle multiplicities directly, and compares their exact rational moments with the analytic identities. Executing `python verify.py` passes 549 exact comparisons over degree lists with at most 12 half-edges, involving 148,080 enumerated matching-cases, as well as regular sign tests for \(3\le n\le13\), \(2\le d\le8\). Its two-cycle tests are auxiliary regression checks, not part of the claimed new \(r\ge3\) theorem. Exhaustive small instances do not prove the infinite family; that follows from the counting argument above.

## Relationship to prior work

McKay, Wormald and Wysocka (2004) prove short-cycle asymptotic laws in uniformly random **simple** regular graphs. Their theorems cannot determine a covariance with loops because simple graphs have no loops. Janson (2006) develops pairing-model joint moment and Poisson techniques for **loops and parallel-edge pairs** in degree-specified random multigraphs. Those statements do not directly supply the displayed mixed moment with vertex-distinct cycles of length at least three. The finite loop–parallel-edge-pair covariance (length two) and its degree transition are known; that case is excluded from the present contribution. The new assertion is the complete \(r\ge3\) exact length spectrum, its arbitrary-degree form, and its spanning-length sign exception, not invention of the stub-conditioning technique.

## Limitations

The result concerns unconditioned labeled-stub pairings, not uniform simple graphs, unlabeled multigraphs, or cycles with repeated vertices. The strict regular-case signs require \(d\ge2\), \(3\le r\le n\), and even \(nd\). For irregular degrees the formula gives the sign but no universal sign is asserted. Infinite families are proved analytically; the attached exhaustive checks cover only small configurations. Published-literature comparisons support a differentiated result but cannot certify historical priority, particularly against unexamined obscure pairing-model sources and an inaccessible 1981 short-cycle paper. No independent audit has occurred.

## References

1. B. D. McKay, N. C. Wormald and B. Wysocka, *Short cycles in random regular graphs*, Electronic Journal of Combinatorics **11** (2004), #R66, published September 20, 2004. DOI: 10.37236/1819.
2. S. Janson, *The probability that a random multigraph is simple*, arXiv:math/0609802v1, first posted September 28, 2006, especially Sections 4, 5 and 7.
3. N. C. Wormald, *The asymptotic distribution of short cycles in random regular graphs*, Journal of Combinatorial Theory, Series B (1981), DOI: 10.1016/S0095-8956(81)80022-6 (full text not inspected).
