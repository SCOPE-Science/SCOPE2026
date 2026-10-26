# Exact \(k\)-limited domination of every classical Sierpiński graph

## Finding

For every integer \(n\geq1\), \(m\geq2\), and \(1\leq k\leq m-1\), the \(k\)-limited domination number of the classical Sierpiński graph is
\[
\boxed{\gamma_k^{\mathrm L}(S(n,m))=(m-k)m^{n-1}.}
\]
Thus the formula proposed in Conjecture 12 of Božović (2026) holds for the full stated range, not only for \(k=1\) or \(m=3\). In addition, if \(n\geq2\) and \(k\geq2\), every minimum \(k\)-limited dominating set contains exactly \(m-k\) vertices in every base clique.

## Assumptions and scope

The vertex set of \(S(n,m)\) is \(\{0,\ldots,m-1\}^{n}\). Two distinct words \(u,v\) are adjacent when some index \(h\) satisfies: their entries before \(h\) agree; \(u_h\ne v_h\); and all later entries of \(u\) equal \(v_h\), while all later entries of \(v\) equal \(u_h\). These are the classical (complete-base) Sierpiński graphs, not arbitrary generalized Sierpiński graphs.

A set \(D\) dominates a graph if every vertex outside \(D\) has a neighbor in \(D\). It is \(k\)-limited if each vertex in \(D\) has at most \(k\) neighbors outside \(D\). The number \(\gamma_k^{\mathrm L}\) minimizes \(|D|\) over these sets. The proof addresses every integer in the stated range without asymptotic conditions.

For \(n\geq2\), a **base clique** consists of the \(m\) words with any prescribed first \(n-1\) coordinates. A **superblock** consists of the \(m\) base cliques with the same first \(n-2\) coordinates. For \(n=2\), there is exactly one superblock, with empty prefix. A linking edge joins vertices in distinct base cliques; each vertex has at most one such edge.

## Proof

Put \(r=m-k\), so \(1\leq r\leq m-1\).

**Lower bound.** First suppose \(n\geq2\), and fix a superblock determined by a prefix \(p\) of length \(n-2\). Write \(C_a=\{pab:b\in\{0,\ldots,m-1\}\}\) for its \(m\) base cliques. Let \(D\) be any \(k\)-limited dominating set.

If \(C_a\cap D\ne\varnothing\), a selected vertex in that clique is adjacent to all omitted vertices of the same clique. Consequently \(|C_a\setminus D|\leq k\), hence \(|C_a\cap D|\geq r\).

If \(C_a\cap D=\varnothing\), then for every \(b\ne a\), the omitted vertex \(pab\) has precisely one neighbor outside \(C_a\), namely \(pba\). Indeed, its last two symbols differ, excluding a linking edge at any earlier coordinate; its edge to \(pba\) is the linking edge at coordinate \(n-1\). Since \(pab\) must be dominated, \(pba\in D\). This vertex lies in \(C_b\) and already has one outside neighbor in \(C_a\). Its \(k\)-limited constraint therefore allows at most \(k-1\) omitted vertices inside \(C_b\). Thus \(|C_b\cap D|\geq r+1\) for every \(b\ne a\). In particular, two base cliques in one superblock cannot both be empty.

If no base clique of the superblock is empty, the superblock contributes at least \(mr\) selected vertices. If one is empty, it contributes at least
\[
(m-1)(r+1)=mr+(k-1)\geq mr.
\]
There are exactly \(m^{n-2}\) disjoint superblocks, so \(|D|\geq m^{n-2}mr=rm^{n-1}\). For \(n=1\), the graph is \(K_m\); every nonempty \(k\)-limited dominating set contains at least \(m-k=r\) vertices. This proves the lower bound in every dimension.

**Upper bound.** Regard the symbols as the cyclic group \(\mathbb Z/m\mathbb Z\). Choose an additive-inversion-invariant set \(T\) of exactly \(r\) residues. One explicit choice is
\[
T=\bigcup_{j=1}^{\lfloor r/2\rfloor}\{j,-j\}\;\cup
\begin{cases}\{0\},&r\text{ odd},\\\varnothing,&r\text{ even}.\end{cases}
\]
All the listed nonzero residues are distinct because \(r\leq m-1\); hence \(|T|=r\) and \(T=-T\).

For \(n\geq2\), select a word if and only if the difference between its last and penultimate symbols belongs to \(T\):
\[
D_T=\{x_1\cdots x_n:x_n-x_{n-1}\in T\pmod m\}.
\]
Each base clique contains precisely \(r\) chosen vertices and hence exactly \(k\) omitted vertices. Therefore every omitted vertex is dominated within its base clique. We check that no linking edge crosses between \(D_T\) and its complement. For a linking edge indexed by \(h=n-1\), the two terminal pairs are \((a,b)\) and \((b,a)\), with differences that are negatives of one another; membership is identical because \(T=-T\). For any linking edge indexed by \(h\leq n-2\), both terminal pairs have equal entries, so both differences are zero. Thus both endpoints have the same membership. Each selected vertex consequently has precisely its \(k\) omitted base-clique neighbors outside \(D_T\), proving the \(k\)-limited condition. As there are \(m^{n-1}\) base cliques, \(|D_T|=rm^{n-1}\). For \(n=1\), any \(r\) vertices of \(K_m\) form an admissible set. This proves equality.

**Minimum-set consequence.** For \(n\geq2\) and \(k\geq2\), a superblock with an empty clique contributes at least \(mr+k-1>mr\); hence no minimum set has an empty base clique. All nonempty base cliques contribute at least \(r\), and the total attains that lower bound, so each contributes exactly \(r\). This establishes the stated additional property. \(\square\)

## Verification

The standalone standard-library program `verify.py` reconstructs adjacency independently from the coordinate definition, checks the explicit modular-residue construction and its exact size for 31 parameter triples, and exhaustively rules out smaller feasible sets in six small graphs (263,568 candidate masks counted across their \(k\)-values). It also checks the block-cost identity for 1,225 parameter pairs. The program prints `VERIFY_OK` upon success. Run `python3 verify.py` from this directory. The mathematical proof above, not finite testing, establishes the theorem for unbounded parameters.

## Relationship to prior work

Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs* (arXiv:2610.01584v1, publicly submitted 2026-10-01), proves the formula for \(k=1\) with arbitrary \(m\) (Theorem 10) and for \(m=3\), \(k\in\{1,2\}\) (Theorem 11), and formulates the complete formula as Conjecture 12. The present proof establishes precisely the conjectured general statement and supplies the extra minimum-set consequence. Its lower bound uses grouped base cliques and does not assume that every individual base clique contains a selected vertex. Its explicit upper construction uses inversion-symmetric residues to respect every linking edge.

Božović, Kovijanić Vukićević, Radić, and Tepeh, *On \(k\)-limited domination in graphs* (arXiv:2606.22422), introduced the parameter and general bounds. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products* (arXiv:2606.22428), studies product graphs; its graph products do not directly identify the classical Sierpiński family. Relevant literature comparisons and their limitations are detailed in `AUDIT.json` and `REVIEW.md`.

## Limitations

The formula concerns finite, simple classical Sierpiński graphs with a complete graph as their recursive base and \(1\leq k\leq m-1\). No result is asserted for generalized Sierpiński graphs built over arbitrary base graphs, or for counting every minimum set. The minimum-set consequence specifies base-clique cardinalities, not a complete classification. Finite computational checks are supplementary, and external independent mathematical assessment has not been performed.

## References

1. D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1 (2026), https://arxiv.org/html/2610.01584 .
2. D. Božović, Ž. Kovijanić Vukićević, G. Radić, and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422 (2026), https://arxiv.org/abs/2606.22422 .
3. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (2026), https://arxiv.org/abs/2606.22428 .
4. S. Klavžar and U. Milutinović, *Graphs \(S(n,k)\) and a variant of the Tower of Hanoi problem*, Czechoslovak Mathematical Journal **47** (1997), 95–104.
