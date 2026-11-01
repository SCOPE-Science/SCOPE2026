# A complete two-variable arithmetic phase diagram for cyclic addition relations without constants

## Finding
For every integer \(n\ge 1\), let \(\mathcal C_n=(\mathbb Z/n\mathbb Z;R)\), where \(R(a,b,c)\) holds precisely when \(a+b=c\pmod n\). The vocabulary contains only the ternary relation \(R\), with no constant symbols and no function symbols. Let \(a(n)=\nu_2(n)\), let \(m(n)=n/2^{a(n)}\), and define the odd-part phase \(P(m)\) by the four mutually exclusive possibilities:

* \(F\): \(m=1\);
* \(FT\): \(m=3\);
* \(FL\): \(m>1\) and \(3\nmid m\);
* \(FTL\): \(m>3\) and \(3\mid m\).

**Theorem.** For all positive integers \(n,n'\), the following are equivalent:
\[
\mathcal C_n\equiv_{\mathrm{FO}^{2}}\mathcal C_{n'}
\quad\Longleftrightarrow\quad
\bigl(a(n),P(m(n))\bigr)=\bigl(a(n'),P(m(n'))\bigr).
\]
Here \(\mathrm{FO}^{2}\) is counting-free first-order logic with only two reusable variable symbols, allowing arbitrary quantifier depth. Consequently there are exactly four theories for each fixed nonnegative \(2\)-adic valuation. Within each of the four classes, the least possible cardinalities are respectively \(2^a\), \(3\cdot2^a\), \(5\cdot2^a\), and \(9\cdot2^a\). In particular, the nonisomorphic cyclic addition relations of sizes \(5\) and \(7\), and of sizes \(9\) and \(15\), satisfy the same \(\mathrm{FO}^{2}\) sentences.

## Assumptions and scope
The domain is the full finite cyclic group \(\mathbb Z/n\mathbb Z\), including \(n=1\), but addition is represented **only** by its ternary graph. The symbols \(0\), \(+\), negation and numerical parameters are not available in the syntax. The notation \(\nu_2(n)\) denotes the largest \(a\ge0\) such that \(2^a\mid n\). The four phases are structural, recording the presence of the unique doubling fixed point, nonzero doubling two-cycles, and doubling cycles of length at least three. The phase letters are notation, not predicates in the original vocabulary. No quantifier-rank restriction is imposed.

## Proof
**1. Reduction of all two-variable atoms.** Let \(D(x,y)\) abbreviate \(R(x,x,y)\), so \(D(x,y)\iff y=2x\pmod n\). Let \(Z(x)\) abbreviate \(R(x,x,x)\), so \(Z(x)\iff x=0\). Every atomic formula formed using at most the variables \(x,y\) is logically determined by the five bits
\[
x=y,\quad Z(x),\quad Z(y),\quad D(x,y),\quad D(y,x).
\]
Indeed the other substitutions of \(x,y\) into \(R\) reduce to \(Z(x)\) or \(Z(y)\). Equality supplies no other binary atoms. Thus it suffices to study two-pebble equivalence of the relational doubling digraph with its definable zero mark. This does **not** replace \(D\) by a unary function symbol: iterated function terms would change the variable-width fragment.

**2. Doubling components and colors.** Write \(n=2^a m\) with \(m\) odd. By the Chinese remainder theorem, doubling has a cyclic/permutation part of size \(m\) and a nilpotent part on the \(2\)-primary factor. Each orbit enters its periodic part after at most \(a\) steps. Periodic vertices consist of the single fixed point \(0\) (type \(F\)), exactly two points forming a mutual two-cycle when \(3\mid m\) (type \(T\)), and all remaining periodic points (type \(L\)), whose doubling cycles have length at least three. Hence the number of \(L\) roots is \(m-1-2\mathbf1_{3\mid m}\). When type \(L\) is present this number is at least four, and each \(L\) root has a distinct successor, a distinct predecessor, and at least one other \(L\) root that is neither. For \(m=7\), for example, the six \(L\) roots form two three-cycles, so the last property also holds in the shortest-cycle case.

Give each vertex its *color* \((c,t)\), where \(c\in\{F,T,L\}\) is the periodic type reached under doubling and \(t\in\{0,\dots,a\}\) is its exact distance to the periodic part. For each periodic root, the off-cycle incoming tree has exactly one vertex at distance one and \(2^{t-1}\) vertices at distance \(t\ge1\), for \(t\le a\). If \(r_c\) is the number of periodic roots of type \(c\), the total number of vertices of color \((c,t)\) is \(r_c\) at height zero and \(r_c2^{t-1}\) at positive height. The possible root counts are exactly \(r_F=1\), \(r_T=2\) when present, and \(r_L\ge4\) when present. More precisely, a periodic root has one off-cycle predecessor when \(a\ge1\); each off-cycle vertex below height \(a\) has exactly two off-cycle predecessors; vertices at height \(a\) have none. This follows from multiplication by two on \(\mathbb Z/2^a\mathbb Z\), independently of the odd part.

**3. Uniform two-pebble extension lemma.** Consider any two structures having the same \(a\) and the same phase. For every color \(u\) of a selected vertex and every color \(v\) of its possible replacement, the set of realizable five-bit atomic diagrams from step 1 is identical across the structures, independently of which vertex of color \(u\) was selected. To verify this directly, split the target vertices into the selected vertex itself; its forward doubling neighbor; its backward doubling neighbors; and the remaining vertices. Same-level edges are possible only on the periodic cycle; the only mutual edges between distinct points are the \(T\) two-cycle. Off-cycle edges always join consecutive heights in the same root type. The numbers of available off-cycle neighbors are determined solely by \(a,t\), including the exceptional one-child periodic root. For unrelated vertices, the only small cardinalities requiring care are the unique \(F\) root, its unique height-one child, and the two \(T\) roots: all are determined by the color data. Every \(L\) color has at least four vertices; in particular the three possibilities (forward neighbor, backward neighbor, neither) all occur at \(L\) height zero. At positive heights there are the prescribed binary-tree neighbors and other vertices of the same color; the existence of an unrelated witness again depends only on the height and the number of roots \(1,2,\ge4\), not on that number beyond the threshold. To see explicitly that the residual cases cannot depend on hidden cycle data, for a fixed source and target color subtract the possible equal vertex, forward neighbor, and incoming neighbors from the displayed color cardinality; the remaining targets all realize the unique diagram with neither directed adjacency nor equality. For \(L\) at height zero, at least one such target survives since there are at least four roots and precisely two distinct cycle neighbors. At positive \(L\) heights, at most two neighbors lie in any one target color and the target color has at least four members. The \(F\) and \(T\) colors have exact known cardinalities, so these subtractions give identical answers throughout each class. Thus the five-bit support is a function only of \((a,P,u,v)\).

Duplicator now maintains the color of each pebble as well as the five-bit atomic diagram between the two pebbles. On a move that lifts one pebble, the other selected vertex serves as the anchor. The extension lemma gives an element of the same desired color with the same five-bit diagram in the opposing structure. If the two pebbles coincide, the equality bit is handled in the same way. This produces a legal response for *every round*, proving \(\mathrm{FO}^{2}\)-equivalence of structures with the same invariant by the two-pebble characterization.

**4. Formulas separating the invariants.** Define \(\lambda_0(x)\) to mean that \(x\) has no incoming \(D\)-edge, and recursively let \(\lambda_{j+1}(x)\) assert that some incoming \(D\)-neighbor satisfies \(\lambda_j\). Explicitly,
\[
\lambda_0(x)=\neg\exists y\,D(y,x),\qquad
\lambda_{j+1}(x)=\exists y\bigl(D(y,x)\land \lambda_j(y)\bigr),
\]
where the bound inner variables are alpha-renamed alternately so that only \(x,y\) occur. For \(a=0\), \(\lambda_0\) holds nowhere, because doubling is a bijection. For \(a\ge1\), leaf vertices are exactly at off-cycle height \(a\); since the zero vertex loops to itself,
\[
\mathcal C_n\models\exists x\bigl(Z(x)\land\lambda_j(x)\bigr)
\quad\Longleftrightarrow\quad j\ge a.
\]
Therefore the sentences determine \(a\), including whether it is zero. A two-cycle is detected by the two-variable sentence
\[
\exists x\exists y\bigl(x\ne y\land D(x,y)\land D(y,x)\bigr),
\]
which holds exactly when \(3\mid m\). For a fixed recovered \(a\), let \(C_a(x)\) be the tautology if \(a=0\), and \(\lambda_a(x)\) if \(a\ge1\). The predicate \(C_a\) selects exactly the periodic vertices. Consequently
\[
\exists x\bigl(C_a(x)\land\neg Z(x)\land
\neg\exists y\,(x\ne y\land D(x,y)\land D(y,x))\bigr)
\]
holds exactly when some periodic cycle has length at least three, i.e. when type \(L\) is present. The \(T\)-test and the \(L\)-test determine the four possible phases, completing necessity.

**5. Representatives.** Among positive odd \(m\) in the respective phases, the minima are \(1,3,5,9\). Multiplying by the required fixed \(2^a\) gives the stated exact smallest models within the family.

## Verification
Two independent standalone Python 3 programs implement exact finite checks. `verification/verify_types.py` computes the noncounting two-variable unary-type refinement directly from all ternary atomic substitutions, and compares all \(12{,}720\) unordered pairs of moduli from \(1\) to \(160\). Every pair agrees with the claimed invariant; the sampled structures separate by quantifier rank three. This rank-three statement applies **only to the tested finite sample**, not uniformly to arbitrary \(a\). `verification/verify_palette.py` independently enumerates complete one-step atomic support palettes for all \(12{,}880\) anchors and \(1{,}378{,}160\) ordered pairs in the same range. All predicted equivalences and inequivalences agree, and colors have uniform support. Both programs are accompanied by their recorded output. The infinite result rests on the proof above, not the computations.

## Relationship to prior work
Gomaa's 2007 thesis develops Ehrenfeucht–Fraïssé bounds and definability for finite cyclic groups using an addition relation **with an identity constant** (Chapter 3); it does not yield the present constant-free, two-variable, unrestricted-depth classification as stated. Bova and Martin (2015) study first-order query evaluation on finite abelian groups in a **functional** group signature, rather than this two-variable fragment of the relational graph of addition. Although the zero vertex is unary-definable as \(Z(x)\), a *named* zero can occur as the third argument in \(R(x,y,0)\), which exposes the inverse-pair relation using two variables; such atomic expressive power is absent here. Therefore neither a match in group terminology nor an upper bound obtained with more variables entails this exact two-variable equivalence. Related results on short finite-variable games, if any, also would not automatically imply equivalence at arbitrary depth. The result is advanced with historical-priority uncertainty because a stronger general theorem about binary functional digraphs could conceivably imply it.

## Limitations
The vocabulary restriction is essential: named group identity, binary addition as a function symbol, iterated doubling terms, or counting quantifiers may distinguish groups equivalent here. The smallest representatives are within the family of cyclic addition relations and are not claimed to be smallest among all arbitrary relational structures. Exhaustive numerical checks end at modulus \(160\); only the proof supplies the universal quantifiers. The literature comparison is not exhaustive, and independent mathematical validation has not been performed.

## References
1. Walid Gomaa, *Model Theory and Complexity Theory*, University of Maryland doctoral thesis (publicly available 2007-07-06), Chapter 3, especially Sections 3.1, 3.5–3.6. Permanent repository: https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 ; PDF: https://drum.lib.umd.edu/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/download .
2. Simone Bova and Barnaby Martin, *First-Order Queries on Finite Abelian Groups*, LIPIcs CSL 2015, DOI 10.4230/LIPIcs.CSL.2015.41 (2015-09-07). https://doi.org/10.4230/LIPIcs.CSL.2015.41 .
