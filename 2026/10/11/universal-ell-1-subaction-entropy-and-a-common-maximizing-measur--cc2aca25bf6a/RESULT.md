# Universal \(\ell^1\) subaction entropy and a common maximizing measure for planar regular subshifts

## Finding

**Theorem (exact entropy for every integer direction).** Let \(d\ge 1\) and let \(X\) be a nonempty, finite-alphabet, \(d\)-regular, extendable \(\mathbb Z^2\)-subshift of finite type in the sense of Bondarenko--Grigorchuk--Vdovina [1]. Equivalently for the proof, work in its conjugate nearest-neighbour matrix presentation, where every admissible three-corner pattern of a unit square has a unique fourth-corner completion and every occurring rectangular pattern has exactly \(d\) extensions on each of its four sides. Let \(\sigma^v\) denote translation by \(v\in\mathbb Z^2\), and let \(\mu\) be the canonical, fully supported, shift-invariant measure assigning equal mass to all occurring patterns of any fixed rectangle. Then, **simultaneously for all** \(v=(a,b)\in\mathbb Z^2\),

\[
h_{\mathrm{top}}(\sigma^v\vert_X)
=h_\mu(\sigma^v)
=(|a|+|b|)\log d.
\]

Thus a single canonical measure maximizes the entropy of every rank-one lattice subaction; its entropy function on integer vectors is the restriction of the \(\ell^1\) norm multiplied by \(\log d\). This is the entropy of the full transformation \(\sigma^v\) on \(X\), **not** the entropy obtained by observing symbols on only one lattice line. In the example of the binary additive square shift, these latter two quantities differ for diagonal directions.

For each nonzero \(v\), the proof gives one explicit finite clopen partition that already realizes both equalities. There is no mixing, primitivity, or Ramanujan hypothesis.

## Assumptions and scope

Write \(X_R\) for the set of rectangular restrictions of globally occurring configurations. A \(d\)-regular system has \(|X_{[0,m-1]\times[0,n-1]}|=s d^{m+n-2}\) for positive integers \(m,n\), with \(s\) the number of occurring symbols; this count and the unique-completion property for the extendable matrix presentation are established in [1, Section 3, Definition 4 and Proposition 6]. The canonical measure \(\mu\) has rectangular cylinder masses \(1/(s d^{m+n-2})\) [1, Section 3, after Proposition 7]. All logarithms are natural. Both entropies in the theorem refer to the ordinary single-homeomorphism action of \(\sigma^v\), including a negative-coordinate vector; for \(v=(0,0)\), they are zero.

For a finite shape \(F\subset\mathbb Z^2\), denote by \(\mathcal P_F\) the clopen partition according to the configuration restricted to \(F\). Denote the number of occurring patterns on a finite set \(S\) by \(N_X(S)\). The result is invariant under rectangular higher-block recoding, so the matrix presentation used in the proof does not restrict the stated systems.

## Proof

**Step 1: a staircase restriction lemma.** Consider an axis-aligned rectangle of lattice vertices \(R\), with \(m+1\) columns and \(n+1\) rows, and any unit-step monotone path \(P\) joining opposite corners, with \(m\) horizontal and \(n\) vertical unit steps. A path may use either sign in each coordinate, but never reverses either sign. Restriction from occurring rectangular patterns to occurring path patterns is a bijection.

To prove it, first take the boundary L-shaped path consisting of the bottom row followed by the right column (or its sign-reflected equivalent). Values along this path uniquely determine all of \(R\): complete the square adjacent to the boundary corner from its three known corners, then move across the next row, and iterate row-by-row. Existence of each completion is inherited from the globally occurring rectangle pattern, and uniqueness is the four-corner rule. Any two monotone lattice paths with the same endpoints are connected by adjacent interchanges of one horizontal and one vertical step: the word of steps is transformed by swaps \(HV\leftrightarrow VH\). Such a swap replaces a path's intermediate corner of one unit square by the opposite intermediate corner. The unchanged endpoints and old intermediate vertex are three corners of that unit square, so unique completion determines the replacement; the same rule reverses the move. Therefore every corner swap induces a bijection of globally occurring path patterns. Chaining these bijections yields the claimed restriction bijection for arbitrary \(P\).

Consequently, since \(|R|\) has \((m+1)\times(n+1)\) vertices,

\[
N_X(P)=N_X(R)=s d^{m+n}.
\]

Further, because the rectangle restrictions are equiprobable under \(\mu\) and the restriction map is bijective, the \(s d^{m+n}\) path restrictions are also equiprobable. Hence

\[
H_\mu(\mathcal P_P)=\log s+(m+n)\log d.
\]

This lemma includes horizontal or vertical paths (a rectangle of width or height one); when both step counts vanish, the count is \(s\).

**Step 2: lower bounds and a finite entropy-realizing partition.** Fix \(v=(a,b)\ne(0,0)\), and choose one monotone lattice path \(P_v\) from the origin to \(v\), with exactly \(L=|a|+|b|\) unit steps. Let \(\mathcal Q=\mathcal P_{P_v}\). For every positive integer \(N\),

\[
S_N=\bigcup_{j=0}^{N-1}(P_v+jv)
\]

is precisely the concatenated monotone path from the origin to \(Nv\), with \(LN\) unit steps. The join \(\bigvee_{j=0}^{N-1}(\sigma^v)^{-j}\mathcal Q\) is the partition by restrictions to \(S_N\). Step 1, applied to \(S_N\), gives the **finite exact identities**

\[
N_X(S_N)=s d^{LN},\qquad
H_\mu\!\left(\bigvee_{j=0}^{N-1}(\sigma^v)^{-j}\mathcal Q\right)
=\log s+LN\log d.
\]

Taking \(N^{-1}\log\) of the first, and \(N^{-1}\) times the second, proves

\[
h_{\mathrm{top}}(\sigma^v,\mathcal Q)
=h_\mu(\sigma^v,\mathcal Q)=L\log d.
\]

This is a lower bound for the full topological and measure-theoretic entropies. The negative-coordinate cases use exactly the same argument with reflected monotone paths; all four corner orientations are uniquely completable.

**Step 3: matching upper bounds.** Let \(F\subset\mathbb Z^2\) be an arbitrary fixed finite rectangle containing the support of any desired clopen partition. The union \(\bigcup_{j=0}^{N-1}(F+jv)\) is contained in an axis-aligned rectangle with \(|a|N+O_F(1)\) columns and \(|b|N+O_F(1)\) rows (with constant side lengths in any vanishing coordinate). By the exact rectangle count,

\[
\log N_X\!\left(\bigcup_{j=0}^{N-1}(F+jv)\right)
\le LN\log d+O_F(1).
\]

This bounds both the logarithm of the number of atoms in the joined partition and its Shannon entropy under \(\mu\). After division by \(N\), the upper entropy bound is \(L\log d\). Every open cover of compact, zero-dimensional \(X\) is refined by a finite cylinder partition, and these partitions also generate the measure sigma algebra; taking the supremum establishes both upper bounds. For \(v=(0,0)\), the transformation is the identity and both entropies are zero. Combined with Step 2 this proves the theorem for every \(v\) and establishes that \(\mu\) is a common maximal-entropy measure. \(\square\)

## Verification

The proof is exact and does not rely on computational enumeration. The self-contained accompanying `verify_staircase_entropy.py` checks **325 exact finite counting and staircase-bijection identities** on additive square shifts over \(\mathbb F_2\) and \(\mathbb F_3\), including a finite diagnostic distinguishing diagonal line projection from a full diagonal subaction. Run it with `python verify_staircase_entropy.py`. The finite checks are illustrations only: arbitrary alphabet sizes, all integer vectors, and infinite time are covered by Steps 1--3.

An explicit non-product-form illustration is the binary SFT satisfying \(x_{i,j}+x_{i+1,j}+x_{i,j+1}+x_{i+1,j+1}=0\) in \(\mathbb F_2\). Every configuration has the form \(x_{i,j}=r_i+c_j\). It has \(s=d=2\), so its full diagonal shift \(\sigma^{(1,1)}\) has entropy \(2\log2\) by the theorem, whereas its restriction to the single diagonal line is the full binary one-dimensional shift, of entropy \(\log2\). This distinction explains why results about line-projection entropy alone do not provide the full subaction statement.

## Relationship to prior work

Bondarenko, Grigorchuk and Vdovina [1] introduce \(d\)-regular multidimensional subshifts, prove exact rectangular pattern counts and four-way unique extendability in their planar matrix models (Proposition 6), construct the canonical uniform-rectangle measure, and give Ramanujan examples for odd prime-power \(d\). Their results concern zero entropy of the full planar group action and quantitative mixing. These structural ingredients are acknowledged, not claimed as new. The added result is the exact entropy of **every** individual full-space lattice shift and the fact that the same prescribed measure achieves all these maximal entropies. The decisive extra argument is the finite staircase restriction bijection, not simply the rectangle asymptotic.

Johnson, Kass and Madden [2] investigate the entropy of projecting a subshift to one lattice-line subspace, varying it under conjugacy, and its relation to full-dimensional entropy (in particular their Theorem 4.1). Projectional entropy can be strictly smaller than the entropy of the original single shift homeomorphism; the binary additive-square illustration above provides an exact separation. Jung, Lee and Park [3] discuss directional entropy dimensions and the positive directional entropy of the classical three-dot system, but do not furnish the present exact \(\ell^1\) formula or common measure theorem for four-way regular subshifts. The three-dot local rule is triangular and is not itself the four-corner hypothesis used here.

## Limitations

This is not a statement about irrational Milnor directions or a claim that the subaction is Bernoulli, expansive or uniquely ergodic. It does not establish uniqueness of the maximizing measure for any direction, nor apply without the four-way unique-completion hypothesis. The full \(\mathbb Z^2\)-action has zero area-normalized entropy, as already known from the rectangle count. Possible equivalent formulations in older textile/commuting-square or cellular-automaton literature remain a priority risk; published mathematical records and the primary works cited below were compared, but no independent audit has taken place.

## References

1. I. Bondarenko, R. Grigorchuk and A. Vdovina, *Ramanujan subshifts*, arXiv:2602.22356v1 (first public 25 February 2026), especially Section 3, Definition 4, Proposition 6 and the canonical measure after Proposition 7. https://arxiv.org/html/2602.22356v1
2. A. Johnson, S. Kass and K. Madden, *Projectional Entropy in Higher Dimensional Shifts of Finite Type*, Complex Systems 17 (2007), 243--257. DOI: 10.25088/ComplexSystems.17.3.243. https://content.wolfram.com/sites/13/2018/02/17-3-3.pdf
3. U. Jung, J. Lee and K. K. Park, *Topological Entropy Dimension and Directional Entropy Dimension for \(\mathbb Z^2\)-Subshifts*, Entropy 19 (2017), article 46. https://www.mdpi.com/1099-4300/19/2/46
