# A sharp two-point tail-depth covariance phase diagram near random permutations

## Finding

Let \(f:[n]\to[n]\) be a uniformly sampled mapping, and let \(C\) be the set of cyclic vertices. Fix two distinct labels \(x,y\). For each vertex \(v\notin C\), let \(H_v\) be its first-entry distance to \(C\), equivalently the number of directed edges along the orbit of \(v\) before first reaching a cyclic vertex. Condition on \(|C|=k\), \(x,y\notin C\), and put \(m=n-k\), where \(k\ge1\) and \(2\le m\le5\).

**Theorem.** The conditional covariance is
\[
\operatorname{Cov}(H_x,H_y\mid |C|=k,\ x,y\notin C)
=\frac{P_m(k)}{(k+m)^{2m-2}},
\]
where
\[
\begin{aligned}
P_2(k)&=-1,\\
P_3(k)&=k^2-2k-19,\\
P_4(k)&=3k^4+46k^3+192k^2+24k-836,\\
P_5(k)&=5k^6+168k^5+2217k^4+14072k^3
       +40503k^2+25728k-64261.
\end{aligned}
\]
The entire sign phase diagram on this natural near-permutation domain is:

| Noncyclic vertices | Negative covariance | Positive covariance |
|---|---|---|
| \(m=2\) | All \(k\ge1\) | Never |
| \(m=3\) | \(1\le k\le5\) | \(k\ge6\) |
| \(m=4\) | \(k=1\) | \(k\ge2\) |
| \(m=5\) | Never | All \(k\ge1\) |

There are no zero cases. In particular, among all uniform random mappings conditioned on two specified labels being noncyclic, **six vertices is the smallest size permitting positive covariance**: at \(n=6\) the cases \((m,k)=(5,1),(4,2)\) have covariances \(8/729\) and \(11/1296\), whereas \((m,k)=(3,3),(2,4)\) have negative covariance. At \(m=3\), the first positive case is \(k=6\) (hence \(n=9\)), with covariance \(5/6561\).

## Assumptions and scope

The mapping is uniform among all \(n^n\) functions, including self-loops. A cyclic vertex is a member of any directed cycle, including a fixed point; \(H_v\) counts directed steps from a noncyclic vertex to the first cyclic vertex. Conditioning is on both distinct marked labels being **noncyclic**, so \(m\ge2\). The number \(k\) of cyclic vertices is positive. The theorem classifies all \(k\ge1\) for each \(m\in\{2,3,4,5\}\); it does **not** claim an all-\(m\) covariance formula or a corresponding sign pattern when conditioning only on the number of cyclic vertices and not on the two marked vertices being noncyclic.

## Proof

Fix any specific cyclic set \(R\subset[n]\setminus\{x,y\}\) of cardinality \(k\). On \(R\), a mapping restricts to an arbitrary permutation, giving \(k!\) choices. On the remaining \(m=n-k\) labels, each noncyclic vertex has one outgoing arrow, and those arrows must eventually reach \(R\), without cycles outside \(R\). Thus the induced arrows form a directed forest oriented toward the \(k\) designated roots. For every such forest, the number of compatible permutations on \(R\) is the same. Hence conditional on \(R\), and consequently on \(|C|=k\) and \(x,y\notin C\), the forest is uniformly distributed among all directed forests with roots \(R\).

Relabel the \(m\) noncyclic vertices so that \(x=1\), \(y=2\). Collapse the \(k\) roots into a formal symbol \(0\). For every vector \(p=(p_1,\ldots,p_m)\) with \(p_i\in\{0,1,\ldots,m\}\), discard self-arrows or any directed cycle on \(\{1,\ldots,m\}\). For each remaining vector let \(r(p)=|\{i:p_i=0\}|\). Its multiplicity in the original forest model is precisely \(k^{r(p)}\), because every arrow to symbol \(0\) independently selects one of \(k\) distinct cyclic roots. Let \(h_i(p)\) be the number of parent steps until reaching \(0\).

Define the integer polynomials
\[
\begin{aligned}
W_m(k)&=\sum_{p\text{ admissible}} k^{r(p)},\\
A_m(k)&=\sum_{p\text{ admissible}} k^{r(p)}h_1(p),\\
B_m(k)&=\sum_{p\text{ admissible}} k^{r(p)}h_1(p)h_2(p).
\end{aligned}
\]
A finite enumeration of the parent choices, using precisely the rejection and depth recursion specified above, gives the following **symbolic polynomial identities**, valid for every positive integer \(k\), not merely sampled numerical values. Write \(A_m(k)=k a_m(k)\) and \(B_m(k)=k b_m(k)\):

| \(m\) | \(a_m(k)\) | \(b_m(k)\) |
|---|---|---|
| 2 | \(k+3\) | \(k+4\) |
| 3 | \(k^2+8k+17\) | \(k^2+10k+30\) |
| 4 | \(k^3+15k^2+78k+142\) | \(k^3+18k^2+120k+302\) |
| 5 | \(k^4+24k^3+222k^2+944k+1569\) | \(k^4+28k^3+315k^2+1712k+3836\) |

For the denominator, the same enumeration (or the classical fixed-root forest enumeration) yields
\[
W_m(k)=k(k+m)^{m-1}.
\]
By symmetry of the two marked labels,
\[
\mathbb E H_x=\mathbb E H_y=\frac{A_m(k)}{W_m(k)},\qquad
\mathbb E[H_xH_y]=\frac{B_m(k)}{W_m(k)}.
\]
Therefore
\[
\operatorname{Cov}(H_x,H_y)
=\frac{b_m(k)(k+m)^{m-1}-a_m(k)^2}{(k+m)^{2m-2}},
\]
and polynomial multiplication of the displayed finite identities yields exactly \(P_m(k)\) in the theorem. In particular, this proves the formulas for **all** integer \(k\ge1\) despite the bounded number of transient vertices.

To determine signs, \(P_2=-1\). The quadratic \(P_3\) is strictly increasing for integer \(k\ge2\), with \(P_3(5)=-4\), \(P_3(6)=5\), and it is negative also at \(k=1\). The polynomial \(P_4\) has strictly positive derivative for positive \(k\), and \(P_4(1)=-571\), \(P_4(2)=396\). All nonconstant coefficients of \(P_5\) are positive, while \(P_5(1)=18432>0\); it is therefore positive throughout \(k\ge1\). The cases at \(n\le5\) necessarily have \(2\le m\le4\) and fall in the negative ranges above, while the two \(n=6\) positive examples prove the sharp first-size statement.

## Verification

The standalone `verify.py` uses only Python's standard library. Its first implementation enumerates all \((m+1)^m\) potential parent vectors for each \(2\le m\le5\), discards cyclic cases and exactly computes the integer coefficient vectors of \(W_m,A_m,B_m\). It checks every displayed coefficient, the count identity, the covariance identities and sign thresholds. A separate implementation enumerates **actual complete functions** on \([n]\) for \(3\le n\le6\), detects cyclic vertices by orbit tracing, conditions on the two specified transient labels and recomputes the three moments. These independent computations agree exactly. To reproduce: run `python3 verify.py` in a directory containing the delivered script.

## Relationship to prior work

Classical Cayley rooted-forest enumeration is not claimed as new. Pitman's *Coalescent Random Forests* (public technical report September 1, 1996), especially Section 2.1, establishes the fixed-root forest count; it does not state the present two-marked-depth covariance phase diagram. Chuprunov–Fazekas (2009) study block-size counts and strong laws in the same uniform rooted-forest model, not marked depth covariance. Berlinkov's 2015 open preprint explicitly reduces uniform random mappings conditional on cyclic vertices to a rooted-forest model, but focuses on highest-tree asymptotics rather than finite two-vertex depth signs. Hansen–Jaworski (2008) study local mapping properties including one-vertex predecessors and successors; their broader local statistics are an important historical-priority comparison, not a verified statement of this pairwise phase diagram.

The additional step here is the exact joint-depth moment enumeration and the complete positive/negative phase boundary for the first four nontrivial transient populations, including the sharp first positive population size.

## Limitations

No statement is made for \(m\ge6\), for weighted mapping models, or for unconditional pairwise depth covariance. The proof is an exact symbolic finite-parent-type census for \(m\le5\), not a general recurrence for arbitrary \(m\). Earlier general multivariate forest or random-mapping generating functions might imply these identities after specialization; such implicit historical coverage has not been ruled out. The reproduction script is a finite exact check of algebraic coefficient identities and direct small-size maps; it is not evidence for an unproved all-\(m\) extrapolation. No independent audit is claimed.

## References

1. J. Pitman, *Coalescent Random Forests*, Berkeley Technical Report 457 (public September 1, 1996), https://statistics.berkeley.edu/tech-reports/457 ; especially Section 2.1 and equation (6).
2. A. Chuprunov and I. Fazekas, *Strong laws of large numbers for random forests*, Acta Math. Hungar. 124 (2009), 59–71, https://doi.org/10.1007/s10474-009-8150-x .
3. M. V. Berlinkov, *Highest Trees of Random Mappings*, arXiv:1504.04532v1 (public April 17, 2015), https://arxiv.org/abs/1504.04532 .
4. J. C. Hansen and J. Jaworski, *Local Properties of Random Mappings with Exchangeable In-Degrees*, Adv. Appl. Probab. 40 (2008), 183–205, https://doi.org/10.1239/aap/1208358892 .
