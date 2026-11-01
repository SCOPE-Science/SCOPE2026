# The first two 3-cycle filtration stages of odd cyclic tournaments

## Finding

For each integer \(k\geq1\), let \(n=2k+1\). The cyclic tournament \(R_n\) has vertex set \(\mathbb Z/n\mathbb Z\) and arcs \(i\to i+j\) for \(1\leq j\leq k\) (all indices modulo \(n\)). For \(t\in\mathbb Z_{\geq0}\), let \(F_t(R_n)\) be the simplicial complex on these vertices whose nonempty faces \(A\) induce at most \(t\) directed three-cycles. Put
\[
C_n=\frac{n(n^2-1)}{24}.
\]
Then the complete homotopy types at the first two thresholds are
\[
F_0(R_n)\simeq S^1,\qquad
F_1(R_n)\simeq\bigvee^{C_n-1}S^2,
\]
where a wedge with zero summands is interpreted as a point (this occurs when \(n=3\)). Moreover \(H_1(F_t(R_n);\mathbb Z)=0\) for every \(t\geq1\), and \(H_2(F_t(R_n);\mathbb Z)=0\) for every \(t\geq2\). The **complete integral persistent homology in degrees one and two** therefore consists of one degree-one interval \([0,1)\) and \(C_n-1\) degree-two intervals \([1,2)\). These intervals use the integer filtration parameter; there are no other intervals in those degrees.

There is also a natural dihedral symmetry on the underlying filtered simplicial complexes: rotations preserve the tournament and reflections replace it by its converse while preserving the number of directed three-cycles. Let \(\mathcal T_n\) denote the set of cyclic three-element vertex subsets, let \(\mathbb Z[\mathcal T_n]\) be its permutation lattice, and let \(\varepsilon\) be the character that is \(+1\) on rotations and \(-1\) on reflections. Then
\[
\widetilde H_2(F_1(R_n);\mathbb Z)
\cong_{\mathbb Z[D_n]}
\varepsilon\otimes\ker\big(\mathbb Z[\mathcal T_n]\xrightarrow{\ \mathrm{sum}\ }\mathbb Z\big).
\]
The dihedral statement concerns the underlying vertex-set complexes, not a claim that a reflection is an orientation-preserving digraph automorphism.

## Assumptions and scope

The theorem holds for every odd \(n\geq3\), with no upper cutoff, and uses integral coefficients throughout. A directed three-cycle means a three-vertex induced subtournament in which each vertex has one incoming and one outgoing arc. Since \(R_n\) is a tournament, every subset induces one tournament, and the tournaplex filtration is an ordinary abstract simplicial-complex filtration with one simplex per subset. Its stage \(F_0\) is the transitive-subtournament (directed-flag) complex, whereas the full flag tournaplex is the simplex on all \(n\) vertices. The parameter \(t\) counts directed cyclic *triples*, not edges or longer directed circuits. There are no claims about higher-dimensional barcodes or filtrations on noncyclic regular tournaments.

## Proof

**1. The zero stage is a circle.** Within \(R_n\), an induced subtournament is transitive if and only if it has a vertex beating every other vertex: the forward direction is immediate, and the converse uses the transitive orientation of every out-neighborhood. The out-neighborhood of vertex \(i\) is the consecutive block \(\{i+1,\ldots,i+k\}\), and that block is transitively oriented. Consequently the maximal simplices of \(F_0\) are exactly the \(n\) consecutive \((k+1)\)-vertex blocks \(B_i=\{i,i+1,\ldots,i+k\}\). Put the vertex \(i\) at \(i/n\) on the circle \(S^1=\mathbb R/\mathbb Z\). Choose any real radius \(r\) with \(k/(2n)<r<1/4\). The open circular arcs of radius \(r\) centered at the vertices form a good cover of \(S^1\): they cover the circle, and each nonempty finite intersection is a contractible arc, since every arc has length less than half of the circumference. Their nerve consists exactly of those vertex sets lying in some consecutive block of \(k+1\) vertices. Indeed, a common intersection is equivalent to containment in some arc of length \(2r<1/2\); because the sampled points are evenly spaced, its longest needed clockwise span is then at most \(k/n<2r\). Thus their nerve is \(F_0\), and the nerve lemma gives \(F_0\simeq S^1\).

For an oriented edge \((u,v)\), let \(s(u,v)\) be the unique integer congruent to \(v-u\pmod n\) in \([-k,k]\). This is well defined because \(n=2k+1\). If a triangle belongs to \(F_0\), its vertices lift to an interval of length at most \(k\) in \(\mathbb Z\), and the sum of \(s\) on its oriented boundary is zero. For any integral simplicial one-cycle \(z\), cancellation of endpoints modulo \(n\) makes \(\sum_{(u,v)}z_{uv}s(u,v)\) divisible by \(n\). Thus
\[
\operatorname{wind}(z)=\frac{1}{n}\sum_{(u,v)}z_{uv}s(u,v)
\]
is an integer-valued homology homomorphism on \(F_0\). The consecutive cycle \(0\to1\to\cdots\to n-1\to0\) has winding one; combined with \(H_1(F_0;\mathbb Z)\cong\mathbb Z\), this proves that winding is an isomorphism.

**2. Only triangles enter at threshold one.** If a four-vertex tournament contains a directed triangle \(a\to b\to c\to a\), consider the fourth vertex \(d\). If \(d\) defeats all three or loses to all three, there is exactly one directed triangle. In every other case, exactly one of the three triples involving \(d\) is also cyclic, so there are exactly two. The first two possibilities cannot arise inside \(R_n\), because both the in-neighborhood and the out-neighborhood of every vertex are transitively oriented consecutive blocks. Therefore every four-vertex subset of \(R_n\) has either zero or two directed three-cycles. A simplex newly entering at threshold one cannot have four or more vertices; conversely every directed cyclic triple enters. Hence \(F_1\) is obtained from \(F_0\) by adjoining exactly one two-simplex for each directed cyclic triple and no additional higher-dimensional cells.

Count those triples: among all \(\binom n3\) triples, the transitive ones are counted exactly once by their unique source. Every vertex is the source of \(\binom k2\) transitive triples. Therefore
\[
|\mathcal T_n|=\binom n3-n\binom k2=\frac{n(n^2-1)}{24}=C_n.
\]
If a triple \(a,b,c\) is in clockwise order and cyclic, its three clockwise gaps are all at most \(k\) and sum to \(n\). Its boundary (clockwise orientation) therefore has winding one by the preceding formula. All of the new attaching maps \(S^1\to F_0\simeq S^1\) have degree \(+1\) after this orientation choice. Attaching the first two-cell makes a contractible complex, because it kills the primitive generator of \(\pi_1(S^1)\). Every remaining attaching loop is nullhomotopic in that complex and contributes a wedge-summand \(S^2\). This proves the claimed homotopy type and torsion-free integral homology of \(F_1\).

**3. The symmetry lattice.** The relative cellular group \(H_2(F_1,F_0;\mathbb Z)\) is freely generated by clockwise oriented directed cyclic triples. Rotations permute these generators without sign, while reflections reverse cyclic order and hence multiply by \(-1\). By the exact sequence of the pair, since \(H_2(F_0;\mathbb Z)=0\),
\[
0\longrightarrow H_2(F_1;\mathbb Z)\longrightarrow
H_2(F_1,F_0;\mathbb Z)\xrightarrow{\partial}
H_1(F_0;\mathbb Z)\longrightarrow0.
\]
The winding calculation shows that \(\partial\) takes every clockwise oriented triangle generator to the same positive generator. This makes its kernel precisely the signed augmentation lattice as stated.

**4. Death of low-dimensional classes.** The four-vertex calculation also implies that every four-element subset belongs to \(F_2\), and every triple belongs to \(F_1\). Thus \(F_2\) contains the full three-skeleton of the simplex on \(n\) vertices. This skeleton has vanishing reduced integral homology in degrees one and two, as does any complex obtained from it by attaching only cells of dimension four and above. No new two-simplices enter after threshold one, and no new three-simplices after threshold two. Consequently \(H_1(F_t;\mathbb Z)=0\) for all \(t\geq1\) and \(H_2(F_t;\mathbb Z)=0\) for all \(t\geq2\). Since the stage-one group is free of rank \(C_n-1\), the indicated integral persistence intervals follow. At \(n=3\), the full simplex already enters at stage one and the same formulas hold with \(C_n-1=0\).

## Verification

Run `python3 check.py` with Python 3 and no third-party packages. It reconstructs every simplex at thresholds zero, one and two for \(n=3,5,7,9,11\); verifies the triple count, the absence of higher-dimensional new simplices at threshold one, the exact winding of every cyclic triple, the entire three-skeleton at threshold two and all corresponding mod-two Betti numbers. The expected terminal marker is `CYCLIC_TOURNAMENT_FIRST_TWO_DIRECTIONALITY_STAGES_OK`. These tests are finite corroboration; Steps 1–4 are the proofs for every permitted odd order.

## Relationship to prior work

Govc, Levi and Smith introduced the flag tournaplex and the filtration by the number of cyclic three-vertex subtournaments. Their article supplies the construction and studies examples and data, but its inspected statements do not give the stage-one homotopy type or integral two-stage barcodes of the entire cyclic tournament family. Govc's directed-flag homotopy census concerns chiefly threshold zero and a separate local-directionality filtration. Adamaszek and Adams classify circle Čech complexes, a result consistent with (and substantially broader than) the identification of \(F_0\) as a circle. The new statement is about adding all cyclic triangles to that circle, their integral attaching degrees, their symmetry module and their deaths at threshold two; none follows solely from the Čech classification. An indexed result about reversing a single edge of a cyclic tournament addresses a different operation, not the full cycle-count filtration. Unindexed equivalent work remains a bibliographic risk.

## Limitations

The homotopy type of \(F_2\) and the persistence in degrees at least three are not determined. The dihedral symmetry is a symmetry of the abstract subset filtration and does not claim that reflections preserve arc directions. The finite checker does not certify an infinite theorem by enumeration. No independent audit has been conducted.

## References

1. D. Govc, R. Levi, J. P. Smith, *Complexes of Tournaments, Directionality Filtrations and Persistent Homology*, arXiv:2003.00324, first posted 2020-02-29; open-access journal version in *Journal of Applied and Computational Topology* 5 (2021), 313–337. https://arxiv.org/abs/2003.00324 ; https://doi.org/10.1007/s41468-021-00068-0
2. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333, first posted 2020-06-09. https://arxiv.org/abs/2006.05333
3. M. Adamaszek, H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, 2015; especially its discussion of circle Čech complexes and nerve methods. https://arxiv.org/abs/1503.03669
