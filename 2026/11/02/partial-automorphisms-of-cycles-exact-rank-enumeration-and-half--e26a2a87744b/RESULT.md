# Partial automorphisms of cycles at fixed deficiency

## Finding

Let \(M_n=\operatorname{PAut}(C_n)\) count the isomorphisms between labelled vertex-induced subgraphs of the undirected simple cycle \(C_n\), including the empty map. The rank of a map is its domain cardinality; write \(a_{n,k}\) for the number of maps of rank \(k\). Then for each fixed integer \(d\ge1\), as \(n\to\infty\),
\[
 a_{n,n-d}=\frac{2^d}{d}\,n^{d+1}+O_d(n^d).
\]
At that rank the leading term counts exactly the maps whose domains omit \(d\) isolated vertices and whose induced path components have pairwise distinct sizes, all at least two. Their images have the same property. For \(d=1\), \(a_{n,n-1}=2n^2\) exactly for every \(n\ge3\).

## Assumptions and scope

Vertices are distinguished; there is no quotient by cyclic symmetries. A partial isomorphism must preserve and reflect adjacency of domain vertices but need not preserve ambient graph distances or extend to a full automorphism. The deficiency \(d\) is fixed independently of \(n\); no uniformity in growing \(d\) is asserted.

## Proof

For a nonfull, nonempty domain of size \(n-d\), the run lengths of its cyclic indicator word describe a forest of \(r\le d\) paths. A *shape* is the multiset of the \(r\) positive path sizes. Each shape admits at most \(O_d(n)\) labelled placements: mark a run start, choose an ordering of the run lengths and a composition of \(d\) into positive gap lengths. Only the choice of the start has order \(n\), since \(r\le d\). Once the domain and image are fixed and have the same shape, an isomorphism permutes paths of matching sizes and chooses their orientations; there are at most \(2^d d!\) choices. Thus any one shape contributes \(O_d(n^2)\) maps.

For \(r<d\), there are at most \(\binom{n-d-1}{r-1}=O_d(n^{r-1})\) shapes. It follows that the types with fewer than \(d\) paths contribute \(O_d(n^d)\) in total. When \(r=d\), every gap has length one. Among the ordered compositions into \(d\) parts, one specified part equal to one or two specified parts equal to each other leaves at most \(O_d(n^{d-2})\) choices for fixed \(d\ge2\): solve the total-sum equation after imposing the extra independent constraint. The union of these exceptions has the same order because \(d\) is fixed. Hence the number of shapes with \(d\) distinct lengths, all at least two, is
\[
 \frac{1}{d!}\binom{n-d-1}{d-1}+O_d(n^{d-2})
 =\frac{n^{d-1}}{d!(d-1)!}+O_d(n^{d-2}).
\]
The exceptional shapes contribute \(O_d(n^d)\) by the per-shape bound.

For each remaining shape, there are exactly \(n(d-1)!\) labelled subsets: order the distinct runs in \(d!\) ways and choose the first run's start in \(n\) ways, then divide by \(d\) because each resulting subset has \(d\) marked run starts. A given domain and image of this shape have exactly \(2^d\) isomorphisms: distinct lengths fix the component correspondence and each path of size at least two can be traversed in either order. Thus each of these shapes contributes \(2^d n^2((d-1)!)^2\). Multiplying gives the stated leading coefficient and error. For \(d=1\), both the domain and image are \(n-1\)-vertex paths with \(n\) placements and two orientation choices, proving the exact count.

## Relationship to known enumeration and other rank asymptotics

The complete cycle rank polynomial for \(n\ge5\) is already given by the formula for \(Q_n(z)\) in [1]. It uses the same cyclic run count and the automorphism factors of induced path forests. The fixed-deficiency contribution here is the asymptotic extraction at the moving index \(k=n-d\): identifying the dominant class and accounting for equal or singleton sizes and fewer runs at strictly lower order. The polynomial itself is not claimed as distinct, and the catalog date does not establish the order of the two records. The general induced-subgraph type stratification is classical [2]; path cardinality enumeration is studied in [3].

The macroscopic estimates are also useful context. Put \(s=\lfloor n/2\rfloor\). A rank \(k\) proper domain has at most \(\min(k,n-k)\) components, so for ranks with at most \(b\) components there are at most \(4^n2^b b!\) proper maps. A fixed independent set of size \(s\) supplies at least \(s!\) maps. Include the empty and full cases (one and \(2n\) maps) and apply Stirling with \(b=s\) or \(b=\lfloor(1/2-\epsilon)n\rfloor\). This gives \(\log|M_n|=\tfrac12 n\log n+O(n)\) and the bound \(\exp(-\epsilon n\log n+O_\epsilon(n))\) for the uniform rank probability of \(|k/n-1/2|\ge\epsilon\), for fixed \(0<\epsilon<1/2\). These scales can also be transferred from the path estimates in [4]: at each proper rank, the cycle count lies between the count for \(P_{n-1}\) and \(n^2\) times that count, by choosing a missing vertex in each of the domain and image and mapping the remaining induced paths to a fixed reference path. This comparison does not determine the fixed-deficiency leading constant.

The ambient-distance partial isometry monoid in [5] is a simpler invariant. Its size is exponential in \(n\), rather than factorial in scale. It agrees with \(M_n\) for \(3\le n\le5\) since the cycle then has diameter at most two. It differs for \(n\ge6\) since the map sending \(0\mapsto0,2\mapsto3\) is an induced isomorphism of two edgeless pairs but changes distance.

## Verification and limitations

The accompanying `verify.py` compares the full labelled rank vectors for \(3\le n\le9\) by enumerating adjacency-preserving and reflecting bijections independently of the known partition formula. It includes exact rank \(n-1\) and \(n-2\) checks at \(n=20\). The finite computations illustrate the relevant counts but do not establish the fixed-deficiency asymptotic, which follows from the proof. No uniform estimate in the deficiency, local limit theorem near half rank, or historical-priority guarantee is made.

## References

1. *A finite-rank hub correction for wheel partial-isometry monoids*, Resultary record dated 2026-11-02, Finding and proof of the rim polynomial \(Q_n\), https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-finite-rank-hub-correction-for-wheel-partial-isometry-monoids--d147c97c6256/RESULT.md.
2. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, Proposition 3.1.
3. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468, Theorem 2.1.
4. *Sharp lower-tail exponents for random partial automorphisms of a finite path*, Resultary record dated 2026-11-22, Finding, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-lower-tail-exponents-for-random-partial-automorphisms-of-a--b3dc8a9f5e5d/RESULT.md.
5. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196, Theorem 1.4.
