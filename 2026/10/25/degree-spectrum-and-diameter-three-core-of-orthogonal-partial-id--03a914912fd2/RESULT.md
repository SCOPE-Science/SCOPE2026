# Degree spectrum and diameter-three core of orthogonal partial idempotents

## Finding
For every integer \(n\ge2\), form the simple **orthogonality graph** \(\Omega_n\) of nonzero idempotents in the semigroup \(P_n\) of all partial transformations of a labeled \(n\)-point set. Distinct \(e,f\) are adjacent exactly when \(ef=fe=0\), the empty transformation. If \(r=|\operatorname{im}e|\) and \(d=|\operatorname{dom}e|\), then
\[
\deg_{\Omega_n}(e)=\sum_{s=1}^{n-d}\binom{n-d}{s}(s+1)^{n-r-s}.
\]
Exactly \(\binom nr\binom{n-r}{d-r}r^{d-r}\) vertices have \((r,d)\), for \(1\le r\le d\le n\). Consequently their weighted sum over \((r,d)\) gives the entire degree polynomial, with coincident exponents combined:
\[
\mathcal D_n(z)=\sum_{r=1}^n\sum_{d=r}^n\binom nr\binom{n-r}{d-r}r^{d-r}z^{\sum_{s=1}^{n-d}\binom{n-d}{s}(s+1)^{n-r-s}}.
\]
The isolated vertices are exactly the full-domain idempotents, numbering \(\sum_{r=1}^n\binom nr r^{n-r}\). For \(n\ge3\), the graph induced on nonisolated vertices is connected with diameter exactly \(3\); for \(n=2\), that graph is \(K_2\). The graph has clique number \(n\). For all \(n\ge2\), exactly \(n\) vertices have minimum positive degree \(1\) (the partial identities on complements of singletons), and exactly \(n\) have maximum degree
\[
\Delta_n=\sum_{s=1}^{n-1}\binom{n-1}{s}(s+1)^{n-1-s}
\]
(the singleton partial identities). These two families agree when \(n=2\).

## Assumptions and scope
For \(X=[n]\), a partial transformation \(e:D\to X\) may have any domain \(D\subseteq X\) and need not be injective. Multiplication is usual composition whenever the intermediate image belongs to the next domain; both composition conventions give the same symmetric adjacency relation. The zero transformation has empty domain. An idempotent satisfies \(e^2=e\). Its image \(R\) is exactly its fixed-point set and is contained in \(D\); conversely any choice of nonempty \(R\subseteq D\subseteq X\), with the identity on \(R\) and an arbitrary map \(D\setminus R\to R\), gives an idempotent. The zero map is excluded from graph vertices. The graph is simple and undirected; a vertex never counts as adjacent to itself.

## Proof
**Idempotents and rank/domain multiplicity.** If \(e^2=e\), then for each image value \(y=e(x)\), \(e(y)=y\), so \(R=\operatorname{im}e\subseteq D\) and \(e|_R=\operatorname{id}_R\). Conversely these conditions imply idempotency. To obtain rank \(r\) and domain size \(d\), choose the fixed set \(R\) in \(\binom nr\) ways, choose \(D\setminus R\) in \(\binom{n-r}{d-r}\) ways, and send each of its \(d-r\) points to one of \(r\) fixed points. Hence the asserted multiplicity.

**Orthogonality and local degrees.** For any partial transformations \(e,f\), both compositions vanish exactly when
\[
\operatorname{im}e\cap\operatorname{dom}f=\varnothing,
\qquad\operatorname{im}f\cap\operatorname{dom}e=\varnothing.
\]
Fix an idempotent \(e\) with fixed set \(R\) of size \(r\) and domain \(D\) of size \(d\). To construct a rank-\(s\) idempotent \(f\) orthogonal to \(e\), its fixed set \(S=\operatorname{im}f\) must be a subset of \(X\setminus D\), hence can be chosen in \(\binom{n-d}{s}\) ways. The map \(f\) is the identity on \(S\), undefined at each point of \(R\), and at each of the remaining \(n-r-s\) points it is independently either undefined or takes one of the \(s\) fixed values in \(S\). This is \(\binom{n-d}{s}(s+1)^{n-r-s}\) maps. For \(s=0\) the unique possibility is the zero map, which is not a vertex; summing over \(1\le s\le n-d\) proves the degree formula. Nonzero idempotents cannot annihilate themselves because \(e^2=e\ne0\), so no loop correction is needed.

**Isolates and connected core.** If \(d=n\), there is no nonempty possible \(S\) and \(e\) is isolated. If \(d<n\), choose \(x\in X\setminus D\); the singleton partial identity \(p_x\) is orthogonal to \(e\), proving non-isolation. Thus precisely the full-domain idempotents are isolated; their multiplicities sum to the formula. For any two nonisolated vertices \(e,f\), select \(x\notin\operatorname{dom}e\) and \(y\notin\operatorname{dom}f\). If \(x\ne y\), the singleton identities \(p_x,p_y\) are adjacent, giving a path \(e-p_x-p_y-f\) after removing any coincident consecutive vertices; if \(x=y\), there is a path of length at most two. Therefore the core diameter is at most three. For \(n\ge3\), let \(e\) be the partial identity on \(X\setminus\{x\}\) and \(f\) on \(X\setminus\{y\}\), where \(x\ne y\). Their domains intersect, so they are not adjacent. Any common neighbor \(h\) would have nonempty image contained in the complement of both their domains, which is empty because the two domains cover \(X\). Hence they are at distance at least three, proving equality. At \(n=2\), the only two nonisolated vertices are \(p_1,p_2\), which are adjacent.

**Extremal degrees.** When \(d=n-1\), only \(s=1\) contributes, and \(\deg(e)=2^{n-r-1}\), equal to one precisely when \(r=n-1\). If \(d\le n-2\), even the \(s=1\) contribution is \((n-d)2^{n-r-1}\ge2\). Thus the minimum positive degree and all its extremizers follow. For maximum degree, choose any \(x\) fixed by \(e\). Every neighbor of \(e\) is also a neighbor of \(p_x\), since the image and domain of \(p_x\) are both contained in those of \(e\). If \(e\ne p_x\), the domain of \(e\) contains some \(y\ne x\); then \(p_y\) is a neighbor of \(p_x\) but not a neighbor of \(e\), so the containment is strict. Therefore precisely the singleton partial identities attain the maximum; substituting \((r,d)=(1,1)\) gives \(\Delta_n\).

**Clique number.** In a clique, any two distinct nonzero idempotents have disjoint nonempty fixed sets, so at most \(n\) vertices can occur. The \(n\) singleton partial identities are pairwise orthogonal and realize this bound.

## Verification
The included standalone `verify.py` generates every partial map on \([n]\) for \(1\le n\le6\), filters idempotents directly, and tests both zero compositions either by explicit pointwise composition or by independently computed image/domain bit masks. It checks every rank/domain stratum, every conditional neighbor-rank count, and the global ordered-pair totals. For \(2\le n\le4\) it constructs the entire adjacency graph and checks each degree, its isolates, connectivity of the nonisolated core and the claimed exact diameter using breadth-first search. Symbolic integer summation crosschecks aggregate formulas through \(n=19\). The two terminal success markers are `VERIFY_OK_ORTHOGONAL_PARTIAL_IDEMPOTENT_RANK_DEGREES` and `VERIFY_OK_ORTHOGONAL_IDEMPOTENT_GRAPH_METRIC`. This finite verification supports but does not substitute for the uniform proof above.

## Relationship to prior work
Garba's 1990 study (day-precise online record dated 14 November 2011) treats idempotents in partial transformation semigroups, their projection characteristic and idempotent generation. Fernandes, Gomes and Jesus (2011) enumerate idempotents in chain-restricted transformation monoids. Pookpienlert, Nupo and Chaiya (2024) define an **annihilator graph on all nonzero zero divisors** where \(a,b\) are adjacent when they have a **common nonzero mutual annihilator**. Their 2026 co-annihilating graph is its complement. Neither graph is the orthogonality graph here, whose vertices are only nonzero idempotents and whose adjacency is the direct equation \(ef=fe=0\). A preexisting joint-rank enumeration for pairs of *commuting full idempotent transformations* can, after adjoining an absorbing fixed point, imply global counts of pairs of orthogonal partial idempotents; no novelty is asserted here for those global counts. They do not determine the present **vertexwise domain-sensitive degree multiset, isolate classification and sharp core diameter**. The new contribution is local graph geometry, not the known characterization of idempotents or the global joint-rank incidence.

## Limitations
Only the full partial transformation monoid on a finite labeled set is treated, and only the nonzero idempotent-induced mutual zero-product graph. Claims do not concern the 2024 graph based on shared annihilators, the whole zero-divisor graph, or semigroups of partial injective maps. A complete full text of Garba's 1990 primary paper could not be inspected, so possible unstated overlap there is a historical-priority risk. No independent mathematical audit has been performed.

## References
1. G. U. Garba, *Idempotents in partial transformation semigroups*, Proc. Roy. Soc. Edinburgh Sect. A 116 (1990), 359–366, DOI: 10.1017/S0308210500031553. Online record dated 2011-11-14.
2. V. H. Fernandes, G. M. S. Gomes and M. M. Jesus, *The cardinal and the idempotent number of various monoids of transformations on a finite chain*, Bull. Malaysian Math. Sci. Soc. 34 (2011), 79–85, https://hdl.handle.net/10362/5528.
3. C. Pookpienlert, N. Nupo and Y. Chaiya, *On the annihilator graphs of partial transformation semigroups*, Arab J. Basic Appl. Sci. 31 (2024), 580–590, DOI: 10.1080/25765299.2024.2423464.
4. C. Pookpienlert, N. Nupo and Y. Chaiya, *Co-annihilating graphs of partial transformation semigroups: structure and basic invariants* (2026), DOI: 10.1080/25765299.2025.2611606.
