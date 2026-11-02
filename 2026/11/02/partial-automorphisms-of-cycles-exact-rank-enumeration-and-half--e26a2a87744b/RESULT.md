# Partial automorphisms of cycles: exact rank enumeration and half-rank concentration

## Finding

For every integer \(n\ge3\), let \(C_n\) be the undirected simple cycle with vertex set \(\mathbb Z/n\mathbb Z\), and let \(M_n=\operatorname{PAut}(C_n)\) be the inverse monoid of all graph isomorphisms between vertex-induced subgraphs, including the empty map. Its *rank* statistic is the cardinality of the domain, not its minimum number of generators. Write \(a_{n,k}\) for the number of elements with rank \(k\), for \(0\le k\le n\).

For \(1\le k<n\), let \(\lambda\vdash k\) be a partition, with multiplicity \(m_j=m_j(\lambda)\) of part size \(j\), and put \(r=\sum_{j\ge1}m_j\). Define
\[
N_{n,\lambda}=\begin{cases}
\displaystyle\frac{n(r-1)!}{\prod_{j\ge1}m_j!}\binom{n-k-1}{r-1},&r\le n-k,\\
0,&r>n-k.
\end{cases}
\]
Then \(N_{n,\lambda}\) counts the vertex subsets whose induced subgraph has precisely \(m_j\) path components of size \(j\) for every \(j\). The complete rank enumerator is
\[
\boxed{a_{n,0}=1,\quad a_{n,n}=2n,\quad
 a_{n,k}=\sum_{\lambda\vdash k}N_{n,\lambda}^{\,2}
 \left(\prod_{j\ge1}m_j!\right)2^{\,r-m_1}\quad(1\le k<n).}
\]
In particular, the finite polynomial \(\sum_{k=0}^n a_{n,k}u^k\) is specified exactly for every \(n\), without a recurrence or unknown constants.

Two consequences establish the asymptotic shape. As \(n\to\infty\),
\[
\boxed{\log|M_n|=\tfrac n2\log n+O(n),}
\]
and if \(X_n\) is uniform on \(M_n\), with \(R_n=|\operatorname{dom}X_n|\), then, for every fixed real \(0<\epsilon<1/2\),
\[
\boxed{\Pr\bigl(|R_n/n-1/2|\ge\epsilon\bigr)
 \le\exp\bigl(-\epsilon n\log n+O_\epsilon(n)\bigr).}
\]
Thus \(R_n/n\) converges to \(1/2\) in probability, with superexponentially small macroscopic tails. For each fixed integer \(d\ge1\), there is also the high-rank asymptotic
\[
\boxed{a_{n,n-d}=\frac{2^d}{d}\,n^{d+1}+O_d(n^d).}
\]

Finally, let \(\operatorname{DPC}_n\) denote the *distance-preserving* partial-isometry monoid of the same cycle. For \(3\le n\le5\), \(M_n=\operatorname{DPC}_n\). For every \(n\ge6\), \(\operatorname{DPC}_n\subsetneq M_n\); in fact their cardinalities have logarithmically different scales,
\[
\log\frac{|\operatorname{DPC}_n|}{|M_n|}
 =-\tfrac n2\log n+O(n).
\]
The published enumeration of \(\operatorname{DPC}_n\) is used here as an established comparison, not as a new result.

## Assumptions and scope

Graphs are finite, undirected and loopless. The cycle has the usual edges between residues differing by one modulo \(n\), with \(n\ge3\) ensuring a simple graph. A partial graph automorphism is a bijection from a vertex subset \(S\) onto a vertex subset \(T\), such that for all \(x,y\in S\), adjacency of \(x,y\) is equivalent to adjacency of their images. Neither distance preservation nor extension to a global cycle automorphism is assumed. The empty map has rank zero. All asymptotic constants in \(O_d\) and \(O_\epsilon\) may depend on the indicated fixed parameter but not on \(n\).

The exceptional full-subset case \(k=n\) must be handled separately: \(C_n\) has dihedral automorphism group of order \(2n\) (including the triangular case). Every nonempty proper induced subgraph is a disjoint union of paths, including isolated vertices as one-vertex paths.

## Proof

**1. Cyclic run count.** Fix a proper nonempty vertex subset \(S\), of size \(k\). Its circular indicator word has \(r\) runs of ones and \(r\) runs of zeros. The lengths of the runs of ones form a cyclically ordered list with multiset \(\lambda\), and all lengths of runs of zeros are positive with total \(n-k\). Exactly \(r!/\prod_jm_j!\) linear arrangements of the one-run lengths are possible, and \(\binom{n-k-1}{r-1}\) compositions of the zero-run lengths are possible. Choosing a first run-start among \(n\) labeled vertices and dividing by the \(r\) possible choices of designated one-run counts each subset once. Therefore the number of subsets with these component sizes is precisely \(N_{n,\lambda}\). The construction also proves the vanishing condition \(r\le n-k\), and directly confirms that the displayed expression is an integer.

**2. Partial-isomorphism count.** Two induced path forests admit an isomorphism if and only if their component-size multisets agree. A one-vertex component has only one automorphism; a path of size at least two has exactly two (orientation-preserving or orientation-reversing) automorphisms. The components of each fixed size can be permuted arbitrarily, so the number of isomorphisms between two prescribed induced forests of type \(\lambda\) is
\[
H_\lambda=\Bigl(\prod_{j\ge1}m_j!\Bigr)2^{\,r-m_1}.
\]
There are \(N_{n,\lambda}\) choices for each domain and image, and a map belongs to exactly one such type. Sum \(N_{n,\lambda}^2H_\lambda\) over all partitions. The empty and full cases contribute one and \(2n\), respectively. This proves every coefficient of the enumerator.

**3. Total growth and rank concentration.** Put \(s=\lfloor n/2\rfloor\). Any proper rank-\(k\) forest has \(r\le\min(k,n-k)\le s\) components. Its automorphism group has size at most \(2^rr!\). There are at most \(4^n\) ordered pairs of vertex subsets, hence
\[
|M_n|\le 1+2n+4^n2^ss!.
\]
Conversely, fix one independent set of size \(s\), whose induced graph is edgeless: all \(s!\) permutations of this set are members of \(M_n\). Thus \(s!\le|M_n|\). Stirling's formula sandwiches \(\log|M_n|\) between \(\log(s!)\) and \(\log(s!)+O(n)\); both have leading term \(\tfrac n2\log n\).

On the event \(|k/n-1/2|\ge\epsilon\), every proper rank-\(k\) element has \(r\le(1/2-\epsilon)n\). With \(b=\lfloor(1/2-\epsilon)n\rfloor\), the number of such maps is at most \(4^n2^bb!+2n+1\). Divide by \(|M_n|\ge s!\) and use Stirling's formula for both factorials. For fixed \(\epsilon\), the logarithm of the ratio is at most \(-\epsilon n\log n+O_\epsilon(n)\); the full-rank maps and empty map are absorbed in this bound. This proves the concentration law. No finite simulation is used as a substitute for these inequalities.

**4. Fixed deficiency.** Fix \(d\ge1\), let \(k=n-d\) and take \(n\to\infty\). The component count satisfies \(r\le d\). Contributions from \(r<d\) are \(O_d(n^d)\): there are \(O_d(n^{r-1})\) partitions of \(n-d\) into \(r\) parts, each contributes at most \(O_d(n^2)\), because its factorial factors, zero-run composition count, and orientation count are bounded in \(d\). With \(r=d\), all zero-runs have length one, and the partitions into \(d\) distinct parts each at least two number
\[
\frac{n^{d-1}}{d!(d-1)!}+O_d(n^{d-2})
\]
for \(d\ge2\), by counting ordered positive compositions and excluding repeated or unit parts (each excluded equality lowers the dimension of this fixed-length composition count). Each generic distinct-part partition contributes \(n^2((d-1)!)^2 2^d\). Partitions having repeated or unit parts contribute only \(O_d(n^d)\) altogether. The leading coefficient simplifies to \(2^d/d\). For \(d=1\), the direct formula gives \(a_{n,n-1}=2n^2\) exactly. Hence the fixed-deficiency formula holds for every \(d\ge1\).

**5. Distance preservation is different.** A graph isomorphism of induced vertex subsets preserves adjacency, whereas an element of \(\operatorname{DPC}_n\) also preserves *shortest-path distance in the entire cycle*. If \(n\le5\), all distances between distinct vertices of the cycle are one or two, so preserving adjacency and nonadjacency is equivalent to preserving distance. For \(n\ge6\), the bijection between the two-vertex sets \(\{0,2\}\) and \(\{0,3\}\), sending \(0\mapsto0\) and \(2\mapsto3\), preserves the two edgeless induced graphs but changes ambient distance from two to three. Thus the inclusion is strict. Fernandes and Paulista's independent published count \(|\operatorname{DPC}_n|=n2^{n+1}-(((-1)^n+5)n^2)/4-2n+1\) implies \(\log|\operatorname{DPC}_n|=O(n)\), whereas the monoid \(M_n\) has \(\tfrac n2\log n+O(n)\) logarithmic size, establishing the displayed separation.

## Verification

The accompanying standalone `verify.py` computes the partition formula using exact integers and, independently, enumerates all domain subsets, image subsets and bijections, testing preservation *and reflection* of graph adjacency for every pair of vertices. It compares every coefficient for \(3\le n\le9\). For example, the rank coefficients at \(n=6\) are \((1,36,234,384,216,72,12)\), totaling \(955\); at \(n=9\) they are \((1,81,1620,9612,18954,14256,4806,972,162,18)\), totaling \(50{,}482\). These computations test finite instances only; the complete and asymptotic statements are established by the preceding proofs.

To reproduce: `python3 verify.py` with Python standard library only. The script prints `VERIFY_OK` after all its assertions pass. The formulas are exact over the integers and require no numerical tolerances.

## Relationship to prior work

Jajcay, Jajcayová, Szakács and Szendrei (first public September 12, 2018) defined and studied the general inverse monoid \(\operatorname{PAut}(\Gamma)\) through Green relations, the natural order and realizability. Their structural general theory is not claimed as new here. The present theorem calculates a cycle-specific complete rank profile and two asymptotic laws not supplied by their inspected results.

Dimitrova, Fernandes, Koppitz and Quinteiro (first public January 29, 2021) determine cardinalities and other invariants for \(\operatorname{PAut}(P_n)\) of a *linear path*, not the cycle. Their interval-block enumeration is a useful conceptual precedent; closing the endpoints of the path changes the run constraints, includes the dihedral full-domain stratum, and requires the circular formula proved here. The path theorem alone does not imply the stated cycle coefficients or concentration estimate.

Fernandes and Paulista (first public May 4, 2022) count \(\operatorname{DPC}_n\), the strictly smaller monoid of ambient-distance-preserving partial bijections of the cycle. Their cardinality formula is quoted as known, and the precise distinction of the two monoids is proved above. Dimitrova and Koppitz (first public April 29, 2022) study partial automorphisms of an alternating *crown poset* and its generating rank, rather than graph-induced partial automorphisms of an undirected cycle.

## Limitations

The result concerns undirected simple cycles with at least three vertices, not digraphs, arbitrary regular graphs, or maps preserving full ambient graph distance. It does not determine the constant factor or a local central limit theorem for the dominant ranks. The fixed-deficiency estimate holds for fixed deficiency and is not uniform when the deficiency grows with the cycle. Although inspected literature and semantic research-record searches did not identify an equivalent cycle enumerator, a hidden implication of a broader graph-monoid enumeration remains possible; global publication priority is not established. No independent mathematical audit has been performed.

## References

1. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (first public 2018-09-12), https://arxiv.org/abs/1809.04422 . Full text inspected: introductory definitions, sections on Green relations, natural order, characterization and conclusions.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468 (first public 2021-01-29), https://arxiv.org/abs/2101.12468 . Full HTML inspected, especially Section 2, Theorem 2.1 and its proof.
3. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (first public 2022-05-04), https://arxiv.org/abs/2205.02196 . Full text inspected, including definition and cardinality theorem.
4. I. Dimitrova and J. Koppitz, *The rank of the inverse semigroup of all partial automorphisms on a finite crown*, arXiv:2204.13961 (first public 2022-04-29), https://arxiv.org/abs/2204.13961 . Full HTML inspected, including definitions and main rank results.
