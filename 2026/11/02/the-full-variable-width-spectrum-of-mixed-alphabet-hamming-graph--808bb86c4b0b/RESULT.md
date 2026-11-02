# The full variable-width spectrum of mixed-alphabet Hamming graphs

## Finding

For a finite nonempty sequence \(\mathbf q=(q_1,\ldots,q_d)\), where \(d\ge1\) and every integer \(q_i\ge2\), let
\[
G(\mathbf q)=K_{q_1}\square\cdots\square K_{q_d}
\]
be the Cartesian product of complete graphs, in the pure first-order language of equality and irreflexive adjacency. Its vertices are coordinate tuples; two are adjacent exactly when they differ in one coordinate. All formulas below are **counting-free** and may have **unbounded quantifier rank**.

For an integer \(k\ge3\) and each \(j\in\{2,\ldots,k\}\), define the truncated alphabet spectrum
\[
c_j^{(k)}(\mathbf q)=\#\{i\in\{1,\ldots,d\}:\min(q_i,k)=j\}.
\]
The complete classification is
\[
G(\mathbf q)\equiv_{\mathrm{FO}^k}G(\mathbf r)
\quad\Longleftrightarrow\quad
c_j^{(k)}(\mathbf q)=c_j^{(k)}(\mathbf r)
\ \text{for every }2\le j\le k.
\]
Here \(\mathrm{FO}^k\) permits at most \(k\) reusable variable symbols, not counting quantifiers. For \(k=1\), all graphs in this nonempty family are equivalent. For \(k=2\), precisely two theories occur: the complete graphs (one Cartesian factor) and the noncomplete products (at least two factors).

For fixed \(d\ge1\) and \(k\ge3\), there are exactly
\[
\binom{d+k-2}{k-2}
\]
distinct theories. A theory with spectrum \((c_2^{(k)},\ldots,c_k^{(k)})\) has one smallest representative up to graph isomorphism, namely
\[
\square_{j=2}^{k} K_j^{\square c_j^{(k)}},
\]
with precisely \(\prod_{j=2}^{k}j^{c_j^{(k)}}\) vertices; zero exponents indicate omitted factors.

The minimum distinguishing variable width for nonisomorphic products is also exact. If one has one factor and the other has at least two, the minimum is two. If both have at least two factors but different factor counts, the minimum is three. Otherwise their factor counts agree; if their multisets of alphabet sizes differ, let \(t\ge2\) be the least integer at which their multiplicities of size-\(t\) factors differ. The minimum distinguishing width is then \(t+1\). This last formula also applies to two nonisomorphic complete graphs.

## Assumptions and scope

The class comprises finite Cartesian products of at least one complete graph, each factor of order at least two. There are no named coordinate positions or colors, no counting quantifiers, and no uniform alphabet assumption. All graphs are nonempty, finite, connected, and loopless. No assertion concerns arbitrary induced subgraphs, merged Hamming graphs, or enriched signatures.

## Proof

**1. Intrinsic edge capacity.** Fix an edge \(xy\) changing the \(i\)-th coordinate. Any vertex adjacent to both \(x\) and \(y\) agrees with both endpoints outside coordinate \(i\); otherwise it would be at distance at least two from one endpoint. Consequently every clique containing \(xy\) is contained in that one-coordinate fiber, and the maximum clique containing \(xy\) has precisely \(q_i\) vertices. This holds also for \(q_i=2\).

**2. Each truncated edge color is definable with \(k\) variables.** For \(2\le a\le k\), write \(Q_a(x,y)\) for the formula that \(xy\) is an edge belonging to a clique on at least \(a\) vertices. The formula uses \(x,y\) and \(a-2\) further pairwise distinct witnesses, so at most \(a\) variable symbols. Put
\[
E_j(x,y)=Q_j(x,y)\wedge\neg Q_{j+1}(x,y)
\qquad(2\le j<k),
\]
and \(E_k(x,y)=Q_k(x,y)\). The formulas use at most \(k\) variables. By Step 1, \(E_j\) holds precisely on edges changing a coordinate \(i\) for which \(\min(q_i,k)=j\).

**3. Colored distance is definable with the same \(k\) symbols.** Fix a color \(j\). For each nonnegative integer \(h\), a binary formula \(P_{j,h}(x,y)\) says that there is an \(E_j\)-path of length at most \(h\). Define \(P_{j,0}(x,y)\) by \(x=y\), and inductively define
\[
P_{j,h+1}(x,y):=P_{j,h}(x,y)\vee
\exists z\big(P_{j,h}(x,z)\wedge E_j(z,y)\big).
\]
The three outer roles \(x,y,z\) require only three symbols. Because the inner binary formulas have exactly two free variables, bound variables in each occurrence can be renamed locally among the remaining \(k-2\) symbols. Thus every formula \(P_{j,h}\) belongs to \(\mathrm{FO}^k\), even though its quantifier rank increases with \(h\). For \(h\ge1\), the formula
\[
D_{j,h}(x,y):=P_{j,h}(x,y)\wedge\neg P_{j,h-1}(x,y)
\]
says that the finite shortest \(E_j\)-path distance equals \(h\).

**4. The maximum finite colored distance recovers the spectrum.** An \(E_j\)-path changes only coordinates having truncated alphabet size \(j\). Its connected components consist of all tuples obtained by varying those coordinates while fixing every other coordinate. Within each component the colored graph is a Cartesian product of \(c_j^{(k)}\) complete graphs. Its graph distance is the number of the relevant coordinates in which two tuples differ. Thus the maximum finite \(E_j\)-path distance equals exactly \(c_j^{(k)}\), and it is attained by a pair of vertices when that count is positive. When the count is zero, there are no \(E_j\)-edges. The existence of \(D_{j,h}\)-pairs for successive positive integers \(h\) therefore recovers every \(c_j^{(k)}\) using only \(k\) variables. This proves the necessity direction.

**5. Persistent pebble strategy.** Suppose the truncated spectra agree. Pair the factors so that corresponding factor sizes are equal whenever below \(k\), and both factor sizes are at least \(k\) otherwise. In the ordinary \(k\)-pebble game, maintain the equality pattern of all presently pebbled coordinate values, separately for each paired factor. This implies agreement of vertex equality and adjacency: two tuples agree (respectively, are adjacent) precisely when their coordinate equalities agree everywhere (respectively, fail in exactly one coordinate). When a pebble moves, erase its old values. At most \(k-1\) coordinate values remain mentioned in any coordinate. The new value is either equal to an already mentioned value, which can be copied, or new. The latter is available in the other structure because the paired alphabets have the same size below \(k\), or both have size at least \(k\). This works in either direction and at every round, hence proves equivalence at unrestricted quantifier depth.

**6. Widths one and two.** With one variable and no loops, every atomic formula reduces to truth or falsity in the same manner on all nonempty members. For two variables, the complete products \(K_q\) are equivalent to each other, since every vertex has another distinct neighbor; every noncomplete product has at least one distinct neighbor and at least one distinct nonneighbor of every vertex and hence admits the same indefinite two-pebble responses. The sentence \(\exists x\exists y\,(x\ne y\wedge\neg E(x,y))\) distinguishes these two classes.

**7. Consequences.** For fixed \(d\), the spectrum is a weak composition of \(d\) into \(k-1\) bins, giving the stated binomial count. Replacing every factor of size at least \(k\) by \(K_k\) produces the unique minimum-order graph in its class: each replacement weakly decreases the vertex count, strictly if its original size exceeds \(k\); any other member has the same factor counts in all smaller bins. A different exact alphabet size multiplicity first appearing at \(t\) becomes visible precisely when width reaches \(t+1\); if the factor counts differ, Step 4 detects that at width three. Together with Step 6 this proves all minimum-width assertions.

For example, \(K_2\square K_4\square K_6\) and \(K_2\square K_5\square K_7\) agree at width four (both have one size-two coordinate and two size-at-least-four coordinates) but are distinguished at width five, since one has a size-four coordinate and the other does not.

## Verification

The proof above is valid for all finite factor sequences and all widths in scope. The included independent programs test complementary finite consequences, and neither is used to extrapolate an infinite claim. `check/finite_types.py` implements exact noncounting variable-tuple type refinement until stabilization on ten selected graph pairs, including widths three, four and five. `check/edge_spectrum.py` independently enumerates maximal cliques and colored connected-component diameters for thirteen factor sequences at each of the widths three, four and five (39 checks), without reading the coordinate labels when assigning edge colors. The scripts are self-contained Python 3 programs using only the standard library; their reproducible terminal outputs are embedded beside them.

Run with `python3 check/finite_types.py` and `python3 check/edge_spectrum.py`. All comparisons passed against the exact outputs in `check/finite_types.out` and `check/edge_spectrum.out`.

## Relationship to prior work

The previous three-variable classification is the \(k=3\) specialization and is not claimed as new. The present assertion is a **uniform all-variable-width classification**, not a fixed-depth statement and not an inference from the three-variable case. For example, the width-four and width-five separation above requires more refined edge colors than the binary/nonbinary split available with three variables.

Klavžar and Peterin (2005) characterize Hamming-graph induced and isometric embeddings using edge labels; their theorems concern graph embeddings, not equivalence under arbitrary first-order formulas of bounded variable width. Grohe and Otto (2012) prove general connections between pebble games and finite-variable logical equivalence; their framework is used but their results do not state the present product-specific alphabet-spectrum classification. Pikhurko and Verbitsky (2010/2013) survey graph logical depth and width, but do not give this product-specific theorem. Adler, Benediktsson, and Macpherson (2020) study VC-dimension and VC-density of Hamming graph adjacency, which do not recover the full unrestricted-depth variable-width spectrum. The possibility of an implicit reduction from another general theorem has not been eliminated.

## Limitations

No counting quantifiers are allowed; with counting, degrees and neighborhood sizes yield different distinctions. The result is relative to the indicated Hamming-product family. It makes no claim about identifying its members among all finite graphs, nor about arbitrary Cartesian products, the case of a single-vertex \(K_1\) factor, directed or colored signatures, induced subgraphs, or infinite products. The mathematical proof and computational checks have not received independent external validation. Historical priority cannot be guaranteed solely by the inspected sources.

## References

1. S. Klavžar and I. Peterin, *Characterizing Subgraphs of Hamming Graphs*, Journal of Graph Theory 49 (2005), 302–312. First public online appearance 2005-04-08. DOI: https://doi.org/10.1002/jgt.20084 ; full text: https://users.fmf.uni-lj.si/klavzar/preprints/20084-scan.pdf .
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, 289–304. arXiv:1204.1990, https://arxiv.org/abs/1204.1990 ; DOI: https://doi.org/10.4230/LIPIcs.CSL.2012.289 .
3. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, https://arxiv.org/abs/1003.4865 .
4. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, https://arxiv.org/abs/2007.16042 .
