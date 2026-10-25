# Hidden dihedral symmetry and universal equivariant Euler characters of bidirected bipartite multipath complexes

## Finding

For every integer \(n\geq1\), form the digraph \(D_n\) by replacing each edge of the complete bipartite graph \(K_{2,n}\) with its two opposite directed arcs. Write \(X_n\) for the multipath complex: its vertices are the arcs, and its simplices are the arc subsets whose directed subgraphs are disjoint unions of directed simple paths and isolated vertices.

There is a simplicial action of \(S_n\times D_8\) on \(X_n\), where \(S_n\) permutes the \(n\) leaves and the dihedral group of order eight permutes the four arc types while preserving the two pairs \(\{\alpha,\delta\}\) and \(\{\beta,\gamma\}\). The latter action is generally larger than the group induced by relabelings or reversals of the original digraph.

For \(\sigma\in S_n\), let \(c_j=c_j(\sigma)\) denote the number of cycles of length \(j\). Define the *negative reduced equivariant Lefschetz character* by

\[
L_n(\sigma,t)=-\sum_{j\geq0}(-1)^j\operatorname{tr}\!\left((\sigma,t)\mid\widetilde H_j(X_n;\mathbb Q)\right).
\]

The following formulas determine \(L_n\) for every element of \(S_n\times D_8\). Let \(a=(\alpha\ \delta)\), \(b=(\beta\ \gamma)\), and \(s=(\alpha\ \beta)(\gamma\ \delta)\). The five conjugacy classes of \(D_8\) are represented by \(1,ab,a,s,as\); then

\[
\begin{aligned}
L_n(\sigma,1)&=1-2c_1+4\binom{c_1}{2}-12\binom{c_1}{3}+24\binom{c_1}{4},\\
L_n(\sigma,ab)&=1-2c_1-4c_2+4c_1c_2+8\binom{c_2}{2},\\
L_n(\sigma,a)&=1-2c_1-2c_2+6\binom{c_1}{2}+2c_1c_2
                   -6\binom{c_1}{3}-4c_2\binom{c_1}{2},\\
L_n(\sigma,s)&=1-4c_2+8\binom{c_2}{2},\\
L_n(\sigma,as)&=1-4c_4.
\end{aligned}
\]

In particular, no cycle length other than \(1,2,4\) affects the character; a leaf permutation without cycles of these lengths gives value \(1\) in all five classes. At \(n=6\) and \(\sigma=1\), the five values are \((169,-11,-41,1,1)\). They refine ordinary Euler-characteristic information, but these formulas concern the *alternating* homology representation; they do not assert concentration of homology in any particular degree for general \(n\).

## Assumptions and scope

The two distinguished hubs are \(u,v\); the leaf set is \([n]\). For each leaf \(i\), label the four arcs

\[
\alpha_i:u\to i,\qquad \beta_i:v\to i,\qquad
\gamma_i:i\to u,\qquad \delta_i:i\to v.
\]

A subset of arcs is a simplex precisely when every hub and every leaf has indegree and outdegree at most one, and there are no directed cycles. A valid simplex can use at most one arc of each of the four displayed types, hence has at most four arcs. A dihedral type permutation applies uniformly at every leaf and is independent of leaf relabeling. No assumption is made about additional automorphisms of the resulting complex.

## Proof

**1. Exact local description of faces.** Because each hub may have only one incoming and one outgoing arc, a face includes at most one arc of each of the four types. If it includes two arcs incident with a given leaf, the two must be one incoming and one outgoing, and cannot form a directed two-cycle. Exactly two pairs are therefore allowed at a leaf: \(\{\alpha_i,\delta_i\}\) or \(\{\beta_i,\gamma_i\}\). Finally, a directed cycle avoiding multiple uses of hub directions must alternate hubs and leaves; the only remaining possible cycle is a four-cycle formed by a pair of the first kind at one leaf and a pair of the second kind at a *different* leaf. Excluding their coexistence is necessary and sufficient. Thus the three conditions—distinct global types, permitted same-leaf pairs, and no opposite-kind double pairs on different leaves—describe the entire face set for all \(n\).

**2. The dihedral action.** The permutations of four types that preserve the unordered partition \(\{\{\alpha,\delta\},\{\beta,\gamma\}\}\) form the wreath product \(S_2\wr S_2\), a dihedral group of order eight. They preserve each condition in Step 1, including the four-cycle exclusion. Hence they act simplicially, and commute with arbitrary permutations of the leaves. The displayed generators satisfy \(a^2=b^2=s^2=1\), \(ab=ba\), and \(sas=b\), giving the five listed conjugacy classes.

**3. Signed orbit count.** For a simplicial automorphism \(g\), let \(\varepsilon_g(F)\) be the sign of its induced permutation on the vertices of a setwise invariant face \(F\). The augmented simplicial Lefschetz identity gives

\[
L_n(g)=\sum_{F\in X_n\, :\,gF=F}(-1)^{|F|}\varepsilon_g(F),
\]

where the empty face contributes \(+1\). If \(F\) decomposes into \(r\) vertex orbits under \(g\), the contribution is \((-1)^r\): an orbit of length \(\ell\) contributes \((-1)^\ell(-1)^{\ell-1}=-1\). This also fixes the overall sign convention of the theorem.

**4. Bounded cycle-support expansion.** If an invariant face uses any leaf in a \(\sigma\)-cycle, invariance under \((\sigma,t)\) forces it to use *every* leaf in that cycle. A face involves at most four leaves, so only cycles of lengths at most four can occur, and the sum of their lengths is at most four. Group the signed orbit count by the exact collection of leaf cycles used. Permuting those cycles of equal lengths preserves the count, so it has the unique form

\[
L_n(\sigma,t)=\sum_{k_1+2k_2+3k_3+4k_4\leq4}
A_t(k_1,k_2,k_3,k_4)\prod_{j=1}^4\binom{c_j}{k_j}.
\]

The coefficient \(A_t(k)\) is the signed sum over invariant faces using every cycle in a *fixed* template with exactly \(k_j\) leaf cycles of length \(j\). These are finite computations on at most four leaves. Equivalently, if \(L_t(k)\) is the augmented signed fixed-face sum for that template, inclusion-exclusion gives the exact integer

\[
A_t(k)=\sum_{0\leq h_j\leq k_j}
(-1)^{\sum_j(k_j-h_j)}
\left(\prod_{j=1}^4\binom{k_j}{h_j}\right)L_t(h).
\]

There are exactly twelve admissible support templates, including the empty one. The nonzero coefficients from complete enumeration of those twelve templates, in the tuple order \((k_1,k_2,k_3,k_4)\), are:

| Type action | Template and coefficient |
| --- | --- |
| \(1\) | \((0,0,0,0):1\), \((1,0,0,0):-2\), \((2,0,0,0):4\), \((3,0,0,0):-12\), \((4,0,0,0):24\) |
| \(ab\) | \((0,0,0,0):1\), \((1,0,0,0):-2\), \((0,1,0,0):-4\), \((1,1,0,0):4\), \((0,2,0,0):8\) |
| \(a\) | \((0,0,0,0):1\), \((1,0,0,0):-2\), \((0,1,0,0):-2\), \((2,0,0,0):6\), \((1,1,0,0):2\), \((3,0,0,0):-6\), \((2,1,0,0):-4\) |
| \(s\) | \((0,0,0,0):1\), \((0,1,0,0):-4\), \((0,2,0,0):8\) |
| \(as\) | \((0,0,0,0):1\), \((0,0,0,1):-4\) |

All other coefficients are zero, including every coefficient involving \(k_3>0\). The independent enumerating program `verify_character.py` contains all twelve integer certificate calculations, without relying on a table of homology groups or a homotopy classification. Substitution gives the five claimed polynomials for every \(n\geq1\).

## Verification

Run `python3 verify_character.py` with standard-library Python. It compares the local face criterion against an independent directed-graph indegree/outdegree/cycle test for all 9,686 arc subsets of cardinality at most four at \(1\leq n\leq5\), checks 9,432 transformations under all eight type symmetries, exhaustively evaluates all twelve cycle-support templates and their binomial finite differences, and checks 220 further fixed-face character evaluations against the formulas for every leaf-permutation cycle partition at \(1\leq n\leq7\). The run prints `ALL_CHECKS_PASS` and reproduces the listed nonzero coefficient table. The general conclusion comes from the exact support bound and finite coefficient exhaustion in the proof, not from finite tests at large \(n\).

## Relationship to prior work

Caputi, Collari and Smith introduced and studied bidirectional polygonal multipath complexes, including path and cycle families, in their January 2026 preprint. The present graph is a completely bidirected bipartite graph, not a path or polygon, and the result concerns its new four-arc-type dihedral action and full alternating homology character. The earlier paper of Caputi, Collari, Di Trani and Smith computes an Euler characteristic for a complete bipartite digraph with only arrows *from one part to the other*; its matching-complex formula does not handle the present bidirected cycles or the enlarged symmetry. An earlier finite nonequivariant classification of the six-leaf member supplies no symmetry-character formula. These distinctions identify the part not covered by the inspected comparisons; they do not prove the absence of every possible equivalent formulation in the literature.

## Limitations

The formulas determine a virtual graded rational homology character, not each degree's representation for general \(n\), not integral torsion, and not the complete homotopy type. The order-eight action is exhibited and proved, but it is not asserted to be the entire complex automorphism group. The calculations and bibliographic comparison have not undergone independent scientific review; an unindexed equivalent character calculation remains a residual originality risk.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 2026-01-09, https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, first posted 2022-08-09, https://arxiv.org/abs/2208.04656, especially Section 3.2.
