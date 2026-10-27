# Involutive path partial automorphisms: exact rank series and a half-domain law

## Finding
For the partial-automorphism inverse monoid of an undirected finite path, the rank enumerator of the elements whose square is the identity on their domain is given by a finite, explicit interval-run sum. This enumeration has a superexponential asymptotic consequence: for \(n\) vertices the logarithm of the number of these self-inverse elements has leading term \(\frac14 n\log n\), while the logarithm of the entire monoid's cardinality has leading term \(\frac12 n\log n\). Uniformly sampled self-inverse elements therefore have domain density tending to \(1/2\), and their induced domains have asymptotically \(n/2\) connected components.

Precisely, write \(V_n(z)=\sum_{k=0}^n v_{n,k}z^k\), where \(v_{n,k}\) is the number of partial graph automorphisms \(\alpha\) with \(|\operatorname{Dom}\alpha|=k\) and \(\alpha^2=\operatorname{id}_{\operatorname{Dom}\alpha}\). Define the formal power series
\[
A(x)=x+\frac{2x^2}{1-x},\qquad
B(x)=x^2+\frac{2x^4}{1-x^2},
\]
and for every \(r\ge0\),
\[
J_r(x)=\sum_{j=0}^{\lfloor r/2\rfloor}
\frac{r!}{(r-2j)!\,j!\,2^j}
A(x)^{r-2j}B(x)^j.
\]
Then, for every \(n\ge1\),
\[
\boxed{V_n(z)=1+\sum_{r=1}^{\lfloor(n+1)/2\rfloor}
\sum_{k=r}^{n-r+1}
\binom{n-k+1}{r}[x^k]J_r(x)z^k.}
\]
In particular, \(V_1(z)=1+z\), \(V_2(z)=1+2z+2z^2\), \(V_3(z)=1+3z+6z^2+2z^3\), and \(V_4(z)=1+4z+12z^2+8z^3+2z^4\).

Putting \(U_n=V_n(1)\) and \(T_n=|\operatorname{PAut}(P_n)|\),
\[
\boxed{\log U_n=\tfrac14 n\log n+O(n),\qquad
\log T_n=\tfrac12 n\log n+O(n),\qquad
\log\frac{U_n}{T_n}=-\tfrac14 n\log n+O(n).}
\]
For fixed \(0<\varepsilon<1/2\), when \(\alpha\) is uniform among the \(U_n\) self-inverse elements,
\[
\Pr\left(\left|\frac{|\operatorname{Dom}\alpha|}{n}-\frac12\right|>\varepsilon\right)
\le\exp\left(-\frac\varepsilon2 n\log n+O_\varepsilon(n)\right).
\]
If \(r(\alpha)\) counts connected components of the domain-induced graph, then \(r(\alpha)/n\to1/2\) in probability, with the same stretched superexponential upper bound for \(r(\alpha)/n<1/2-\varepsilon\).

## Assumptions and scope
The graph \(P_n\) has vertex set \([n]=\{1,\ldots,n\}\), with edges exactly between consecutive integers; \(n\ge1\). A partial graph automorphism is a bijection between two subsets that preserves adjacency in both directions **within the induced subgraphs**, not necessarily the graph metric in the whole path. This distinction separates \(\operatorname{PAut}(P_n)\) from the more restrictive monoid of partial isometries. The empty partial map is counted; it has rank zero and its square is the empty identity. The logarithm is natural. All generating-function equalities are identities of formal power series, so no analytic convergence assumption enters the exact count. The asymptotic statements concern integer \(n\to\infty\).

## Proof
**1. Self-inverse elements preserve their domains.** For a partial bijection \(\alpha:S\to T\), if \(\alpha^2=\operatorname{id}_S\), then \(\alpha\) maps every element of \(S\) into \(S\). Since \(|S|=|T|\), necessarily \(T=S\). Thus such elements are precisely the involutions (including the identity) of the ordinary automorphism group of the induced graph \(P_n[S]\), counted once for each subset \(S\subseteq[n]\).

**2. Component involutions and their weights.** A nonempty subset \(S\) of size \(k\) is uniquely the union of \(r\) maximal nonempty intervals (induced paths), with ordered lengths \(\ell_1,\ldots,\ell_r\ge1\) and total \(k\). Any automorphism of \(P_n[S]\) permutes components of the same length. If its square is the identity, the induced permutation of the \(r\) component positions is an involution. A fixed component of length one admits one internal automorphism, while a fixed component of length at least two admits two (identity and reflection). A transposed pair of components of common length one admits one reciprocal pair of isomorphisms; a transposed pair of length at least two admits two, according to orientation of one map (the other must be its inverse). Consequently a fixed component has length-generating weight \(A(x)\) and a transposed component-pair has weight \(B(x)\). An involution of the \(r\) component positions with \(j\) swapped pairs can be selected in \(r!/((r-2j)!j!2^j)\) ways. This proves that \([x^k]J_r(x)\) counts the involutive component automorphisms, summed over all ordered \(r\)-tuples of component lengths totaling \(k\). Length-mismatched transpositions contribute zero by construction.

**3. Embedding the intervals in the path.** Given ordered lengths summing to \(k\), the \(r\) components must be separated by at least one omitted vertex. Distributing the remaining \(n-k-(r-1)\) omitted vertices among the \(r+1\) exterior and inter-component gaps has exactly \(\binom{n-k+1}{r}\) solutions. This is independent of the length tuple. The possible number of components is \(1\le r\le\lfloor(n+1)/2\rfloor\), and for fixed \(r\) the support size satisfies \(r\le k\le n-r+1\). Combining the preceding two paragraphs, and adding the empty partial map, proves the displayed coefficient formula.

**4. An elementary involution-count estimate.** Let \(i_m\) denote the number of involutions in the symmetric group on \(m\) letters. Its decomposition into \(j\) transpositions and \(m-2j\) fixed points gives
\[
i_m=\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{m!}{(m-2j)!\,j!\,2^j},
\qquad
\log i_m=\frac m2\log m+O(m).
\]
For the upper bound of the estimate, the summand is at most \(m^{2j}(e/(2j))^j\) when \(j\ge1\), using \(j!\ge(j/e)^j\); and \(j\log(m/j)=O(m)\) uniformly in \(1\le j\le m/2\). Each summand has logarithm at most \(\frac m2\log m+O(m)\) and there are at most \(m+1\) summands. The lower bound comes from \(j=\lfloor m/2\rfloor\) and the elementary factorial estimates \(\log m!=m\log m-m+O(\log m)\).

**5. Total asymptotic sizes.** For any subset with \(r\) components, the number of involutions of its induced graph is at most \(2^ri_r\): each permissible involutive component permutation admits at most two local choices per fixed or paired component. A subset of \([n]\) has at most \(m_n=\lceil n/2\rceil\) components. Hence \(U_n\le 2^n2^{m_n}i_{m_n}\). Conversely, choose one independent set of cardinality \(m_n\), such as alternating vertices. Its induced graph consists of \(m_n\) isolated vertices and admits all \(i_{m_n}\) involutions; thus \(U_n\ge i_{m_n}\). The involution-count estimate gives \(\log U_n=\frac14 n\log n+O(n)\).

Every partial graph automorphism is an isomorphism between two induced subgraphs. There are at most \(4^n\) ordered domain/image-subset pairs, and for any pair with \(r\) components on each side there are at most \(2^rr!\le2^{m_n}m_n!\) component-preserving isomorphisms. Therefore \(T_n\le4^n2^{m_n}m_n!\). On the fixed alternating independent set there are \(m_n!\) full permutations, all partial automorphisms; hence \(T_n\ge m_n!\). These bounds prove \(\log T_n=\frac12 n\log n+O(n)\) and the stated logarithmic ratio.

**6. Concentration of the domain and component count.** If the domain has size \(k\) and \(r\) components, then \(r\le\min(k,n-k+1)\). On the event \(|k/n-1/2|>\varepsilon\), this forces \(r\le(1/2-\varepsilon)n+1\). Summing the upper bound \(2^ri_r\) over at most \(2^n\) subsets yields an event count with logarithm at most \((1/4-\varepsilon/2)n\log n+O_\varepsilon(n)\). Dividing by \(U_n\ge i_{m_n}\) proves the concentration inequality. Since \(r\le(n+1)/2\) always, exactly the same argument proves the stated lower-tail bound for component count. Therefore both normalized quantities converge in probability to \(1/2\).

## Verification
A standalone Python checker (`check_path_involutions.py`) computes each \(V_n\) in two distinct ways: by polynomial coefficient extraction from the claimed formula and by directly enumerating partial permutations of all vertex subsets, testing both the induced-graph adjacency condition and the involution equation. It exhaustively compared all rank coefficients for \(1\le n\le9\), traversing \(1{,}112{,}082\) raw candidate permutations (across all subsets and these nine path lengths). Each comparison passed. These finite tests are not evidence for the all-size asymptotic claims; those follow from the bounds in the proof.

## Relationship to prior work
Dimitrova, Fernandes, Koppitz, and Quinteiro (2021), arXiv:2101.12468, study exactly the path partial-automorphism monoid and prove its total cardinality formula (their Theorem 2.1), describe Green relations, and determine generator ranks. Their formula counts all partial graph automorphisms, without imposing \(\alpha^2=\operatorname{id}_{\operatorname{Dom}\alpha}\). The new restriction requires an involution on interval components and reciprocal orientations on paired components. The present rank-wise enumerator and the concentration/asymptotic statements are not consequences of the cited cardinal formula without that additional enumeration and analysis.

The finite symmetric inverse monoid contains \(\operatorname{PAut}(P_n)\), but ordinary partial-injection involution counts impose no induced-graph adjacency constraint. Work on partial isometries of wheel, cycle, and star graphs concerns related but different monoids and graph families. The term *involution matching* in the paper by Higgins (2019) denotes a different semigroup-level operation and should not be conflated with an element that is its own inverse.

## Limitations
The theorem gives the exact rank distribution and its first-order logarithmic scale; it does not compute a full equivalent for \(U_n\), the finer fluctuations of rank about \(n/2\), or a limiting law at the smaller fluctuation scale. Formal and finite checks cannot establish historical uniqueness; an earlier general graph-automorphism cycle-index theorem might encode the exact formula implicitly. No assertion is made that the classical permutation-involution formula or the established path-component decomposition is new.

## References
1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468 (first public version 2021-01-29), https://arxiv.org/abs/2101.12468; Semigroup Forum 103 (2021), 87–105, https://doi.org/10.1007/s00233-021-10193-y.
2. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, Communications in Algebra 51 (2023), 1028–1048, https://doi.org/10.1080/00927872.2022.2121404. Related but distinct partial-isometry monoid.
3. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, Turkish Journal of Mathematics 47 (2023), 1746–1760, https://doi.org/10.55730/1300-0098.3460. Related but distinct graph family and restriction.
4. P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum 98 (2019), 669–689, https://doi.org/10.1007/s00233-019-10018-z. Different use of “involution”.
