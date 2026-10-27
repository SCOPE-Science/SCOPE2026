# Wheel geodesic transversals: minimal-set polynomial and linear spectral gaps

## Finding

For every integer \(n\ge6\), let \(J_n=K_1\vee C_n\). The vertices of its rim are \(v_0,\ldots,v_{n-1}\) in cyclic order and the central vertex is \(h\). A geodesic transversal meets every maximal shortest path; it is *inclusion-minimal* when no proper subset remains a geodesic transversal. Let \(\mathcal T_n(z)\) count all geodesic transversals by cardinality and let \(\mathcal M_n(z)\) count exactly the inclusion-minimal ones.

Put
\[
A(u)=\begin{pmatrix}
0&0&u^2\\
0&u&u^2\\
1&u&u^2
\end{pmatrix},
\qquad k_0=\lceil n/3\rceil,\qquad k_1=\lfloor n/2\rfloor.
\]
Then the complete enumerators are
\[
\boxed{\mathcal T_n(z)=z\sum_{k=k_0}^{n}\frac{n}{k}[u^{n-k}](1+u+u^2)^k z^k+z^n+n z^{n-1}+n z^{n-2}}
\]
and
\[
\boxed{\mathcal M_n(z)=n z^{n-2}+z\sum_{k=k_0}^{k_1}\frac{n}{k}[u^{n-k}]\operatorname{tr}(A(u)^k)z^k.}
\]
Here \([u^j]\) means coefficient extraction from an ordinary polynomial in \(u\), and all fractions shown are integers after extraction.

The exact cardinality spectrum of inclusion-minimal transversals is
\[
\boxed{\{k_0+1,k_0+2,\ldots,k_1+1\}\cup\{n-2\}.}
\]
For \(n\ge9\), the integer interval between \(k_1+1\) and \(n-2\) has exactly \(\lceil n/2\rceil-4\) absent cardinalities. The maximum inclusion-minimal cardinality is \(n-2\), while the known geodesic-transversal number is \(k_0+1\).

The number of *minimum-cardinality* geodesic transversals is, exactly,
\[
\boxed{
N_n=\begin{cases}
3,&n\equiv0\pmod3,\\
\dfrac{n(k_0+1)}2,&n\equiv1\pmod3,\\
n,&n\equiv2\pmod3.
\end{cases}}
\]
These results count actual labeled vertex sets, not symmetry classes.

## Assumptions and scope

All graphs are finite, simple, and undirected. The integer \(n\) counts rim vertices, so \(J_n\) has \(n+1\) vertices; no conventional ambiguity about whether the wheel index counts the hub is used. A geodesic is a shortest path, and a maximal geodesic cannot occur as a proper subpath of a longer shortest path. The first published problem definition and the known scalar wheel formula are credited in the references. Every theorem and coefficient identity here is asserted for **all** integers \(n\ge6\); smaller wheels are outside this statement.

## Proof

**Step 1: All maximal geodesics.** The wheel has diameter two. For \(n\ge6\), every edge belongs to a two-edge geodesic: a spoke belongs to \(v_i-h-v_j\) when \(v_i,v_j\) are nonadjacent rim vertices; a rim edge belongs to the geodesic \(v_i-v_{i+1}-v_{i+2}\). Therefore the maximal geodesics are exactly the two-edge paths, namely \(v_i-h-v_j\) for each nonadjacent rim pair and \(v_i-v_{i+1}-v_{i+2}\) for each cyclic starting index (including distinct paths with the same endpoints).

**Step 2: The hub-free branch.** Suppose a transversal \(S\) does not contain \(h\). Every path \(v_i-h-v_j\) is hit exactly when the omitted rim set \(T=V(C_n)\setminus S\) contains no nonadjacent pair. Thus \(T\) is a clique of \(C_n\). Since \(C_n\) has no triangle, \(T\) is empty, a singleton, or an adjacent pair. Conversely any such omission also hits every consecutive rim triple, because the first and last vertices of each triple are nonadjacent. This contributes \(z^n+n z^{n-1}+n z^{n-2}\) to \(\mathcal T_n(z)\). Such a transversal is inclusion-minimal precisely when its omitted set is a maximal rim clique, necessarily an edge. This branch contributes exactly \(n z^{n-2}\) to \(\mathcal M_n(z)\).

**Step 3: The hub-containing branch and all-set polynomial.** Suppose \(h\in S\). Let \(R=S\cap V(C_n)\), with \(k=|R|\). The hub automatically hits paths through itself; the remaining condition is that every three consecutive rim vertices meet \(R\). Since the rim is cyclic, the numbers of unselected vertices between successive members of \(R\) form a cyclic gap vector \((g_1,\ldots,g_k)\), where every \(g_i\in\{0,1,2\}\) and \(\sum_i g_i=n-k\). Conversely any such vector plus a distinguished starting selected vertex yields such a set. Each labeled set has exactly \(k\) choices of distinguished selected vertex and each vector has \(n\) possible starting positions, so its count is \((n/k)[u^{n-k}](1+u+u^2)^k\). This establishes the first displayed polynomial.

**Step 4: Inclusion minimality and the matrix.** Each selected rim vertex must be uniquely responsible for a consecutive rim triple, otherwise it can be removed. At any selected rim vertex, let \(a,b\) be its preceding and following gap lengths. It is indispensable exactly when \(a=2\), or \(b=2\), or both \(a\ge1\) and \(b\ge1\). Therefore the consecutive ordered gap pairs must belong to
\[
\{(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)\}.
\]
The displayed transfer matrix has row index \(a\), column index \(b\), and entry \(u^b\) for each allowed pair, zero otherwise. Hence \(\operatorname{tr}(A(u)^k)\) counts precisely the permissible cyclic gap words, weighted by total omitted rim vertices. The same \(n/k\) rooting argument gives the hub-containing summand of \(\mathcal M_n(z)\).

The local pair rule also forces each gap zero to be followed by a gap two. Distinct zero positions have distinct following positions, so there are at least as many two-gaps as zero-gaps. Accordingly, \(\sum_i g_i\ge k\) and also \(\sum_i g_i\le2k\), forcing \(k_0\le k\le k_1\). Conversely, for every integer \(k\) in this range, gaps chosen only from \(\{1,2\}\) with sum \(n-k\) satisfy the local pair rule and exist. Finally, for such a minimal rim set the hub is itself indispensable: there are \(n-k\ge\lceil n/2\rceil\ge3\) omitted rim vertices, which cannot form a clique of \(C_n\), so removing the hub leaves some path \(v_i-h-v_j\) unhit. This completes the full inclusion-minimal classification and the second polynomial.

**Step 5: Spectra and minimum multiplicity.** The hub branch realizes every cardinality \(k+1\) for \(k_0\le k\le k_1\), while the hub-free branch realizes only \(n-2\). The gap in between has length \(n-k_1-4=\lceil n/2\rceil-4\), positive for \(n\ge9\). The minimum \(k_0+1\) is strictly less than \(n-2\) for \(n\ge6\). At \(k=k_0\), count gap words. If \(n\equiv0\pmod3\), all gaps equal two and there are \(n/k_0=3\) placements. If \(n\equiv1\pmod3\), their total deficit from two is exactly two: either one zero-gap or two one-gaps. These yield \(k_0+\binom{k_0}{2}\) indexed cyclic gap words and therefore \(n(k_0+1)/2\) labeled sets. If \(n\equiv2\pmod3\), exactly one gap equals one and all others equal two, yielding \(n\) sets. Every listed minimum pattern meets the essentiality condition, completing the proof.

## Verification

A standalone source file `verify.py` constructs the actual wheel graph, independently enumerates shortest paths and checks which of them are maximal, and exhaustively tests all vertex subsets. Its inclusion-minimal counts agree with the transfer formula for every \(6\le n\le12\). Its all-transversal polynomial counts agree independently for every \(6\le n\le10\). The minimum multiplicity congruence formulas were also checked through \(n=13\). The checker prints `VERIFY_OK` on success. These are finite consistency checks; the infinite-domain claims rest on the five proof steps above.

## Relationship to prior work

Manuel, Brešar and Klavžar introduced geodesic transversals and their complexity and foundational theory [1]. Independently, Peterin and Semanišin studied maximal shortest path covers and established the **scalar** wheel number (using a convention in which the wheel index includes its hub) [2]. Their subsequent work on joins obtains a general minimization formula and uses the dichotomy between omitting a full factor and omitting a clique, a structural antecedent of Steps 2–3 [3]. Thus neither the concept, the known scalar minimum, nor the general join split is claimed as new. The claim here is the complete wheel all-set and inclusion-minimal enumerators, the exact census of minimum sets, and the gap structure of inclusion-minimal cardinalities. The cyclic gap representation specializes familiar path-vertex-cover techniques; it is the full intersection with the wheel hub branch and maximality constraints that yields the stated census and spectrum.

## Limitations

The result is restricted to \(n\ge6\) and does not describe general joins, arbitrary cycles without a hub, or weighted transversal costs. Finite checks cannot establish the infinite theorem. An earlier unindexed cycle-hypergraph enumeration may contain an equivalent specialization; the relevant historical mathematical literature has been compared but exhaustiveness of priority cannot be guaranteed. Full-page content of one relevant 2021 publication was not retrieved in this investigation; the published accessible sections explicitly provide the scalar wheel result and related definitions, which are fully credited.

## References

[1] P. Manuel, B. Brešar, and S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042, first publicly submitted 20 January 2021; *Applied Mathematics and Computation* **413** (2022), 126621. https://arxiv.org/abs/2101.08042.

[2] I. Peterin and G. Semanišin, *On the Maximal Shortest Paths Cover Number*, *Mathematics* **9** (2021), 1592, published 7 July 2021. https://doi.org/10.3390/math9141592.

[3] I. Peterin and G. Semanišin, *Geodesic transversal problem for join and lexicographic product of graphs*, preprint dated 26 October 2021; *Computational and Applied Mathematics* **41** (2022), article 128. https://doi.org/10.1007/s40314-022-01834-1.
