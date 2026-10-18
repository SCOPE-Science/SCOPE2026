# Sharp quantifier-free expressivity staircase and symmetry gap on finite cycles

## Finding

**Theorem (exact open-type profile, sharp finite-length cutoff, and invariant-relation gap).** For each integer \(n\ge3\), view the undirected cycle \(C_n\) as a finite relational structure with equality and one symmetric irreflexive adjacency predicate. All formulas and relations below are *parameter-free*. For \(k\ge1\), let \(T_{n,k}\) be the number of realized complete quantifier-free types of ordered \(k\)-tuples; equivalently, the number of equivalence classes of tuples under agreement on all atomic and negated atomic formulas. Exactly \(2^{T_{n,k}}\) subsets of \(V(C_n)^k\) are quantifier-free definable.

For integers \(j\ge1\) and \(1\le r\le j\), let \(f_{j,r}\) be the number of simple labeled graphs on \([j]\) that are unions of precisely \(r\) vertex-disjoint paths (isolated vertices count as paths). Then
\[
 f_{j,r}=\frac{j!}{r!}[z^j]\left(z+\frac{z^2}{2(1-z)}\right)^r,
\]
where \([z^j]\) extracts a formal-power-series coefficient. Set
\[
 a_{n,j}=\begin{cases}
 (n-1)!/2,&j=n,\\
 \displaystyle\sum_{r=1}^{\min(j,n-j)}f_{j,r},&1\le j<n.
 \end{cases}
\]
Writing \(\left\{\begin{smallmatrix}k\\j\end{smallmatrix}\right\}\) for a Stirling number of the second kind, the exact profile is
\[
 \boxed{T_{n,k}=\sum_{j=1}^{\min(k,n)}\left\{\begin{smallmatrix}k\\j\end{smallmatrix}\right\}a_{n,j}.}
\]

For each fixed \(k\ge2\), \(T_{n,k}\) is **strictly increasing** as \(n\) runs through \(3,4,\ldots,2k\), and is constant for all \(n\ge2k\). Its stable value is
\[
 \boxed{T_{\infty,k}=\sum_{j=1}^k\left\{\begin{smallmatrix}k\\j\end{smallmatrix}\right\}f_j,\qquad
 f_j=j![z^j]\exp\left(z+\frac{z^2}{2(1-z)}\right).}
\]
In particular, for any \(3\le n<m\), the **least positive arity** for which the two cycles have different numbers of quantifier-free definable relations is exactly
\[
 \boxed{\left\lfloor\frac n2\right\rfloor+1.}
\]
(The unary profiles all equal one.)

Moreover, let \(O_{n,k}\) count orbits of ordered \(k\)-tuples under the full graph-automorphism group of \(C_n\). Then
\[
 \boxed{O_{n,k}=1+\left\{\begin{smallmatrix}k\\2\end{smallmatrix}\right\}\left\lfloor\frac n2\right\rfloor
 +\sum_{j=3}^{\min(k,n)}\left\{\begin{smallmatrix}k\\j\end{smallmatrix}\right\}\frac{n!}{2n(n-j)!}.}
\]
Exactly \(2^{O_{n,k}}\) relations are automorphism-invariant. Consequently, for every fixed \(k\ge2\), the fraction of automorphism-invariant \(k\)-ary relations that are quantifier-free definable is
\[
 \boxed{2^{T_{n,k}-O_{n,k}}=2^{-(1/2+o(1))n^{k-1}}\longrightarrow0\qquad(n\to\infty).}
\]
The classical enumeration of labeled linear forests used in the coefficients \(f_j\) is not claimed as new; the result concerns the exact logical profiles, their sharp parameter cutoff and inverse separation, and comparison with all invariant relations.

## Assumptions and scope

The cycle is simple and undirected and has at least three vertices. Tuples may repeat vertices. The logical language has **only** equality and the adjacency predicate: no vertex names, no constants, no graph-distance predicates, no quantified formulas and no external parameters. An automorphism-invariant relation is any subset of the indicated tuple universe stable under the simultaneous action of every graph automorphism. Formal-series coefficients are taken over the rationals but yield integers by the combinatorial interpretation. For \(k=1\), \(T_{n,1}=O_{n,1}=1\); the strict-rise and asymptotic comparison are expressly for \(k\ge2\).

## Proof

**Step 1: atomic types.** An ordered \(k\)-tuple has a unique equality partition of its coordinate positions into \(j\) nonempty blocks. For a fixed equality partition, label its blocks canonically (for example by their first coordinate). The complete atomic diagram records precisely the adjacency graph induced by the \(j\) distinct vertices attached to those blocks. There are \(\left\{\begin{smallmatrix}k\\j\end{smallmatrix}\right\}\) choices for the partition, and each realizable induced labeled adjacency graph supplies one type. Distinct atomic diagrams can be separated by conjunctions of literals. A Boolean combination of atomic formulas is constant on every realized atomic type, and every union of these types is definable. Thus the count of definable relations is \(2^{T_{n,k}}\).

**Step 2: proper induced subsets of a cycle.** If \(1\le j<n\), deleting at least one cycle vertex turns the selected induced graph into a disjoint union of paths. Its \(r\) path components are maximal runs of selected consecutive vertices separated cyclically by nonempty runs of omitted vertices, so \(n-j\ge r\). Conversely take any labeled forest of \(r\) paths on \([j]\); place its components consecutively around the ambient cycle, with at least one omitted vertex between each pair of successive components. This is possible whenever \(n-j\ge r\), realizes every edge and nonedge of the forest, and yields no other induced edges. For \(j=n\) all vertices are present, so the only induced graph is a spanning cycle; the number of different labeled cycles on \([n]\) is \((n-1)!/2\). This establishes \(a_{n,j}\) and, using Step 1, the formula for \(T_{n,k}\).

**Step 3: path-forest enumeration.** A labeled undirected path component on one vertex has one structure; on \(s\ge2\) labeled vertices there are \(s!/2\) structures (the two linear orientations describe the same path). Hence its exponential generating function is \(P(z)=z+z^2/(2(1-z))\). Taking an unordered set of exactly \(r\) such labeled components gives \(P(z)^r/r!\). Multiplication by \(j!\) yields \(f_{j,r}\); summing over the component count yields \(f_j=j![z^j]\exp(P(z))\).

**Step 4: a strict staircase and its inverse cutoff.** Extend \(a_{n,j}\) by zero for \(j>n\). For fixed \(j\), the sequence in \(n\) is nondecreasing. At \(n=j\) it equals \((j-1)!/2\), strictly below the \(j!/2\) spanning-path graphs that occur at \(n=j+1\) (for \(j\ge3\)). For \(n>j\), it accumulates nonnegative new component layers \(f_{j,n-j}\) until \(n=2j\), after which every path forest is realizable. At \(n=j\) a positive cycle layer first appears; for \(j=1,2\), the proper-subset formula still gives monotonicity on the allowed \(n\ge3\). Now fix \(k\ge2\). If \(n<k\), moving to \(n+1\) creates a positive \((n+1)\)-distinct-coordinate type (since \(n+1\le k\)). If \(n=k\), the \(k\)-distinct-coordinate contribution increases strictly from the cycle layer to spanning paths. If \(k<n<2k\), a new layer of \(k\)-vertex path forests having \(n+1-k\) components appears, and such a forest exists because \(1\le n+1-k\le k\). In all cases \(T_{n+1,k}>T_{n,k}\). When \(n\ge2k\), for every \(j\le k\) we have \(n-j\ge j\), so all forest types are already present and the profile is constant. Given \(n<m\), every arity \(k\le\lfloor n/2\rfloor\) is on the common plateau; at \(k=\lfloor n/2\rfloor+1\), strict rise from \(n\) to \(m\) (possibly followed by the plateau) distinguishes them. This proves the sharp inverse cutoff.

**Step 5: automorphism orbits.** The full automorphism group of a simple cycle is dihedral of order \(2n\). If a tuple contains one distinct vertex there is a single orbit. If it contains exactly two, its orbit is determined by the unordered cyclic distance between their two vertex values, giving \(\lfloor n/2\rfloor\) orbits for each equality partition. A nonidentity dihedral symmetry fixes at most two individual vertices; therefore its action on ordered tuples with \(j\ge3\) distinct vertices is free. Such tuples have \(n!/(n-j)!\) assignments per equality partition, each orbit having size \(2n\). Applying the Stirling partition count gives \(O_{n,k}\). Automorphism-invariant relations are precisely unions of these orbits. For fixed \(k\ge2\), the \(j=k\) summand gives \(O_{n,k}\sim n^{k-1}/2\), while Step 4 makes \(T_{n,k}\) independent of \(n\) for \(n\ge2k\). Their ratio has the stated exponent. \(\square\)

## Verification

The included standalone `check_cycle_types.py` computes \(f_{j,r}\) by a recurrence that isolates the path component containing the least label; it does **not** use the generating function. Independently, it enumerates injective assignments to concrete cycles and records adjacency-bit patterns, then checks the exact formula. It enumerates explicit dihedral images of tuples with repetitions, and checks the independent orbit formula. It also tests strict increase and exact stabilization for several arities. Execute with `python check_cycle_types.py` in the same directory. The actual package extraction produced:

`VERIFY_OK injective_cases=37 injective_assignments=68888 dihedral_cases=24 orbit_tuples=10274 sharp_cutoff_k2..6=YES cycle3_k3= 5 cycle5_k3= 13 cycle6_k3= 14`

These finite enumerations are evidence for the implementation and boundary cases; all-size correctness rests on Steps 1--5.

## Relationship to prior work

Areces, Campercholi, Penazzi and Ventura [1] develop open (quantifier-free) first-order definability on finite relational structures and characterize it using induced-substructure isomorphisms. Their full accessible paper discusses induced paths in a complexity reduction, not the exact two-parameter quantifier-free type count, the \(2k\) plateau or the dihedral separation on undirected cycles. Campercholi, Tellechea and Ventura [2] give general algorithms in functional rather than purely relational signatures and do not enumerate this cycle family. The labeled linear-forest numbers \(f_j\) and their generating function are **already recorded** in OEIS A011800 [3] and standard enumerative combinatorics; they are input to, not originality of, this result. The finite-cycle specific deductions in the Finding require combining the induced-subgraph realization criterion with the precise missing-vertex component bound and the orbit comparison. An earlier identical synthesis under the terminology of graph ages, open definability or finite-model profiles is possible; exhaustive bibliographic priority is not claimed.

## Limitations

The theorem does not address full first-order logic, quantified formulas, distance-enriched cycle signatures, directed cycles, or arbitrary graph families. A cardinality count of definable relations need not classify individual relations across structures with different domains. The standard forest-count sequence and generic semantic characterization are known. The computational checks cover only finite low-order instances. Novelty is supported by the inspected literature and search comparisons, not by an external independent audit or a proof that no unindexed equivalent theorem exists.

## References

1. C. Areces, M. Campercholi, D. Penazzi, P. Ventura, *The Complexity of Definability by Open First-Order Formulas*, arXiv:1904.04637v1, first posted 2019-04-09, https://arxiv.org/html/1904.04637v1 .
2. M. Campercholi, M. Tellechea, P. Ventura, *Two algorithms to decide Quantifier-free Definability in Finite Algebraic Structures*, arXiv:2303.17017v1, first posted 2023-03-29, https://arxiv.org/html/2303.17017v1 .
3. OEIS Foundation, *A011800: Number of labeled forests of n nodes each component of which is a path*, https://oeis.org/A011800 .
