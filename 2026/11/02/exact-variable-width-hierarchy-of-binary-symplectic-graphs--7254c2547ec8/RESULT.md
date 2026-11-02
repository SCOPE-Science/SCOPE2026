# Exact variable-width hierarchy of binary symplectic graphs

## Finding
For each integer \(d\ge1\), let \(S_d\) be the simple graph on the nonzero vectors of a \(2d\)-dimensional vector space \(V_d\) over \(\mathbb F_2\), equipped with a nondegenerate alternating bilinear form \(B_d\); distinct vertices are adjacent precisely when \(B_d(x,y)=1\). All choices of the form produce isomorphic graphs. In ordinary first-order graph logic with equality and adjacency, without counting quantifiers, the following is the **complete classification at unrestricted quantifier depth**.

For every integer \(k\ge3\) and every \(d,e\ge1\),
\[
S_d\equiv_{\mathrm{FO}^k}S_e
\quad\Longleftrightarrow\quad
\min(d,k-1)=\min(e,k-1).
\]
Thus \(\mathrm{FO}^k\) has exactly \(k-1\) theories across this family: the separate dimensions \(1,\dots,k-2\), and one stable class containing every dimension at least \(k-1\). The least graph in the stable class has \(2^{2(k-1)}-1\) vertices, the sharp uniform smallest-representative bound. For \(k=1\) there is one theory; for \(k=2\) there are exactly two, represented by \(d=1\) and by any \(d\ge2\).

Equivalently, for \(1\le d<e\), the **minimum number of variable names** needed to distinguish \(S_d\) and \(S_e\) at any quantifier depth is \(2\) if \(d=1\), and \(d+2\) if \(d\ge2\). In particular, the graphs on \(63\) and \(255\) vertices, \(S_3\) and \(S_4\), agree on all four-variable sentences, but a five-variable sentence distinguishes them.

## Assumptions and scope
The universe is exactly \(V_d\setminus\{0\}\), not a vector space with a named zero or addition function. The signature consists solely of equality and one irreflexive undirected adjacency predicate. A formula in \(\mathrm{FO}^k\) may reuse at most \(k\) variable symbols any number of times; there is **no quantifier-rank bound**. The theorem concerns ordinary Boolean first-order logic, not counting logic, fixed-point logic, a signature exposing the field operations, or graphs produced by switching.

Fix a standard symplectic basis \((e_1,f_1,\ldots,e_d,f_d)\) with \(B_d(e_i,f_i)=1\), all other basis pairings zero. Nondegeneracy implies that for a subspace \(W\le V_d\) of dimension \(r\), the map \(x\mapsto B_d(x,-)|_W\) onto \(W^*\) is surjective and each nonempty fiber has \(2^{2d-r}\) elements.

## Proof
**One-point extension lemma.** Fix \(k\ge3\), \(d,e\ge k-1\), and two tuples of at most \(k\) placed pebbles. Maintain the following invariant: (i) all pairings between corresponding placed vertices agree, and (ii) for every subfamily of at most \(k-1\) placed positions, the sum of its vectors vanishes on one side exactly when it vanishes on the other. Repeated positions are included. In particular, all two-point equality patterns are preserved, because all graph vertices are nonzero and two vectors over \(\mathbb F_2\) coincide exactly when their sum vanishes. Hence the invariant preserves every atomic formula.

Suppose one pebble is moved. At most \(k-1\) vectors \(a_1,\ldots,a_s\) remain fixed, with \(s\le k-1\). Their full linear relation spaces agree, because every relation on these \(s\) positions uses at most \(k-1\) positions. Put \(W=\langle a_1,\ldots,a_s\rangle\), of dimension \(r\le s\). Let \(F\) be the union of the spans of all subfamilies of at most \(k-2\) of the fixed vectors (including the empty subfamily, whose span is \(\{0\}\)). If \(r\le k-2\), an independent subfamily of size \(r\) shows that \(F=W\), so \(|F|=2^r\). If \(r=k-1\), the fixed vectors are independent and \(F=W\setminus\{a_1+\cdots+a_{k-1}\}\), so \(|F|=2^{k-1}-1\).

If the chosen new vertex \(x\) lies in \(F\), express \(x\) as the sum of at most \(k-2\) fixed vertices and choose the same combination on the other side. All its pairings and its relations with any at most \(k-2\) fixed positions are preserved, since these reduce to relations among the unchanged fixed positions. The corresponding sum cannot be zero because the existing relations of the fixed tuples agree.

If \(x\notin F\), it is not in the span of any \(k-2\) fixed positions. Prescribe the pairing vector \((B_d(x,a_i))_{i=1}^s\) on the other side. It obeys all linear relations among the stationary vectors; the preserved relation space and nondegeneracy guarantee a nonempty fiber in \(V_e\) of cardinality \(2^{2e-r}\). When \(r=k-1\),
\[
2^{2e-r}\ge2^{k-1}>2^{k-1}-1=|F|.
\]
When \(r\le k-2\),
\[
2^{2e-r}\ge2^{2(k-1)-r}>2^r=|F|.
\]
Hence a solution outside the corresponding forbidden set \(F\) exists; it is nonzero and has no vanishing relation with a subfamily of at most \(k-2\) stationary vectors. Choosing it maintains the invariant. The same argument works in both directions, for every move, and therefore gives a winning \(k\)-pebble back-and-forth strategy of arbitrary duration. This proves equivalence for all \(d,e\ge k-1\).

**Sharp distinction of dimensions.** For each \(t\ge1\), consider the condition on \(t+1\) vertices \(u_1,\ldots,u_{t+1}\) that they are pairwise distinct and pairwise nonadjacent, every \(t\)-subfamily is linearly independent, and some vertex \(z\) satisfies
\[
B(z,u_1)=1,\qquad B(z,u_i)=0\quad(2\le i\le t+1).
\]
Within a pairwise orthogonal family, independence of a named \(t\)-subfamily is definable using just one additional variable \(z\): require, in a finite conjunction over all \(2^t\) binary patterns, the existence of a vertex whose adjacencies to the named \(t\) points realize that pattern. If these points are independent, every pattern is realized by nondegeneracy, with nonzero witnesses even for the zero pattern; if dependent, a pattern violating their linear relation is impossible. The resulting sentence \(\Phi_t\) therefore uses at most \(t+2\) variable symbols.

In \(V_t\), a pairwise orthogonal set spans a totally isotropic subspace of dimension at most \(t\). If \(t+1\) points have every \(t\)-subfamily independent, their unique dependence is \(u_1+\cdots+u_{t+1}=0\); the prescribed pairing pattern has odd sum and is impossible. Hence \(S_t\not\models\Phi_t\). In every \(V_e\) with \(e\ge t+1\), take \(u_i=e_i\) for \(1\le i\le t+1\) and \(z=f_1\); then \(S_e\models\Phi_t\). Thus \(S_t\) and every \(S_e\) with \(e>t\) differ in \(\mathrm{FO}^{t+2}\).

If \(d<e\) and \(k\ge3\), the established back-and-forth makes them equivalent when \(d\ge k-1\); otherwise \(\Phi_d\) uses \(d+2\le k\) variables and distinguishes them. This completes the classification and shows the representative bound is attained.

For the small-width boundary, \(S_1\) is \(K_3\), whereas every \(S_d\) with \(d\ge2\) has both neighbors and distinct nonneighbors at every vertex. A two-pebble strategy preserving equality and adjacency therefore equates all \(d\ge2\); the two-variable sentence asserting a distinct nonadjacent pair separates \(d=1\). With one variable every graph in this family has only the same loopless unary atomic data and is nonempty.

## Verification
The standalone programs `checks/verify_fo4.py` and `checks/verify_width.py` use the Python standard library. Run them from a directory containing the files with `python3 checks/verify_fo4.py` and `python3 checks/verify_width.py`; compare output with `checks/fo4_output.txt` and `checks/width_output.txt` respectively. The first enumerates all \(17\) three-point pairing/dependence types in six-dimensional binary symplectic space and checks their four-point extension-signature sets against the eight-dimensional space. It also checks all \(15^3=3375\) ordered triples in dimension four and the four-variable separator in dimensions one through three. The second checks the precise finite forbidden-set/fiber inequalities for widths three through eleven and explicitly constructs a five-variable boundary witness. These computations corroborate, but do not replace, the universally quantified fiber-counting and pebble-strategy proof.

## Relationship to prior work
Grohe and Otto (2012) develop the plain, noncounting finite-variable pebble-game framework and its relation to algebraic relaxations, without giving the symplectic-graph dimension classification. Abiad and Haemers (2014/2015) give the binary symplectic graph construction and prove switching and binary-rank results, without addressing unrestricted-depth finite-variable equivalence. Brouwer describes the associated projective orthogonality graph, which in the binary case is the complement of the present nonorthogonality graph. Complementation does not change the variable-width equivalence problem. The result gives an explicit exact dimension hierarchy not established by the inspected portions of these sources. A stronger theorem under a different algebraic or logical formulation could still imply it; no exhaustive historical-priority claim is made.

## Limitations
All fields are binary and all forms nondegenerate alternating forms. The result concerns neither other field orders nor arbitrary strongly regular graphs with the same parameters. The proof does not apply to counting quantifiers or enriched signatures with field addition. It establishes no isomorphisms across different dimensions; the graphs in the stable class have different cardinalities. The finite checks are not a substitute for the infinite algebraic argument. Independent mathematical audit has not been performed.

## References
1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, original public submission 2012-04-09; CSL 2012, DOI: https://doi.org/10.4230/LIPIcs.CSL.2012.289.
2. A. Abiad and W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945, original public submission 2014-12-09; *Designs, Codes and Cryptography*, online 2015-08-14, DOI: https://doi.org/10.1007/s10623-015-0127-x.
3. A. E. Brouwer, *Symplectic graphs*, https://aeb.win.tue.nl/graphs/Sp.html (undated reference page; not used as date evidence).
