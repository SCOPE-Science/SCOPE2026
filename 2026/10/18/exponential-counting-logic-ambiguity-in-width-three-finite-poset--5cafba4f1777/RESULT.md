# Exponential counting-logic ambiguity in width-three finite posets

## Finding
For every integer \(t\ge 2\), there are exactly \(2^{t-1}\) pairwise nonisomorphic finite **strict partial orders** in the explicitly defined cyclic three-chain family below. Each has \(6t+3\) elements, width exactly three, height \(2t+1\), and all members for a fixed \(t\) satisfy precisely the same sentences of two-variable first-order logic with counting, \(C^2\), in the pure binary strict-order signature. In each member, ordinary directed counting colour refinement gives exactly the \(2t+1\) automorphism orbits, each of size three, after one refinement round. Thus recovering all automorphism orbits by counting refinement need not identify a width-three partial order.

In particular, two different fifteen-element width-three strict partial orders are \(C^2\)-equivalent. The factor \(2^{t-1}\) is an **exact isomorphism-type count within this construction**, not an asserted optimum over all width-three posets.

## Assumptions and scope
Fix an integer \(t\ge 2\) and a sign sequence \(s=(s_0,\ldots,s_{t-1})\in\{-1,1\}^t\). The underlying set of \(P_s\) is
\[
V_t=\{(a,z):0\le a\le 2t,\quad z\in\mathbb Z/3\mathbb Z\}.
\]
Give it the **transitive closure** of the following directed generating edges:
\[
(a,z)\longrightarrow(a+1,z)\quad(0\le a<2t),
\]
\[
(2j,z)\longrightarrow(2j+2,z+s_j)\quad(0\le j<t).
\]
All coordinate arithmetic in the second slot is modulo three. The relation is denoted \(<_s\); it is the full strict order, **not** merely the displayed generating-edge relation. The logic uses this one binary relation with equality; the levels are **not** named by predicates in the logical signature.

Define \(X_a=\{(a,z):z\in\mathbb Z/3\mathbb Z\}\). For \(0\le a<b\le 2t\), define the set of completely contained shortcut indices
\[
J(a,b)=\{j: a\le2j\text{ and }2j+2\le b\},\qquad m(a,b)=|J(a,b)|.
\]

## Proof
**1. A complete relation formula.** Every increasing path from level \(a\) to level \(b\) uses ordinary adjacent-level edges and may use any subset of shortcuts whose two endpoints lie in this interval. The possible shortcuts are ordered along the level axis and do not overlap in their interiors, so every such subset is realizable by filling the gaps with adjacent-level edges. A shortcut contributes its sign to the second coordinate, whereas an adjacent-level edge contributes zero. Consequently, for \(a<b\),
\[
(a,z)<_s(b,w)\quad\Longleftrightarrow\quad
w-z\in\left\{\sum_{j\in H}s_j\pmod3:H\subseteq J(a,b)\right\}.
\tag{1}
\]
If \(m(a,b)=0\), the set on the right is \(\{0\}\). If \(m(a,b)=1\), it is \(\{0,s_j\}\), with two distinct residues. If \(m(a,b)\ge2\), already two shortcuts yield every element of \(\mathbb Z/3\mathbb Z\), since \(\{0,u,v,u+v\}=\mathbb Z/3\mathbb Z\) whenever \(u,v\in\{-1,1\}\). Thus the number of elements of \(X_b\) above any fixed point of \(X_a\) is
\[
q(a,b)=\begin{cases}1,&m(a,b)=0,\\2,&m(a,b)=1,\\3,&m(a,b)\ge2.\end{cases}
\tag{2}
\]
It depends on \(a,b,t\), **not** on the signs. Translation of every second coordinate by the same residue is an automorphism, so counts in the reverse direction are also uniform and equal to \(q(a,b)\).

**2. Order and width.** Every generator strictly increases the first coordinate. The closure is therefore irreflexive, asymmetric and transitive. At a fixed level, all three points are incomparable. The three subsets \(\{(a,z):0\le a\le2t\}\), for fixed \(z\), are chains because adjacent-level edges join consecutive elements with that coordinate. Hence the width is at most three and, by each three-point level, is exactly three. The largest chain has \(2t+1\) points, one per level, and such a chain exists. The cardinality is \(3(2t+1)=6t+3\).

**3. Counting-logic equivalence.** Give the elements temporary level labels only for this proof. Every level has three elements; within each level all distinct ordered pairs are incomparable; between levels \(a<b\), each point has exactly \(q(a,b)\) upper neighbours and each upper point has exactly \(q(a,b)\) lower neighbours. By (2), every member of the family has the same complete table of numbers for the binary atomic pair types (equal, below, above, incomparable) between level labels. A structural induction on two-variable formulas now proves that a formula with at most two free variables depends only on the levels of those variables and their atomic pair type, in the same manner for every member: this is immediate for atomic formulas and Boolean combinations, and a counting quantifier eliminates one variable by summing the prescribed per-level counts of each atomic type. In particular, all sentences of \(C^2\) have the same truth value in all \(P_s\). Equivalently, this is the standard directed colour-refinement/equitable-partition criterion, applied to the binary relation including both incoming and outgoing incidences.

**4. Exact isomorphism classification.** For every level \(a\), all three points have the same number \(p_a\) of strict predecessors. These numbers are strictly increasing: \((a,z)<_s(a+1,z)\) and every predecessor of the first point precedes the second, which additionally has \((a,z)\) below it. Thus every isomorphism between two of the posets preserves each \(X_a\). By (1), the relation from \(X_a\) to \(X_{a+1}\) is exactly the identity matching in the second coordinate. Preserving all these matchings forces an isomorphism to have the form
\[
(a,z)\longmapsto(a,\sigma(z))
\]
with one common permutation \(\sigma\) of the three residues. Every permutation of \(\mathbb Z/3\mathbb Z\) is affine, \(\sigma(z)=uz+v\) with \(u\in\{-1,1\}\), \(v\in\mathbb Z/3\mathbb Z\). For each \(j\), the comparison from \(X_{2j}\) to \(X_{2j+2}\) consists precisely of the identity matching and the matching of offset \(s_j\). Therefore an isomorphism \(P_s\to P_r\) must satisfy \(r_j=us_j\) for every \(j\). Conversely, if \(r=us\), this affine map preserves the generating edges and their transitive closures. Hence
\[
P_s\cong P_r\quad\Longleftrightarrow\quad r=s\text{ or }r=-s.
\tag{3}
\]
For nonempty sign sequences, global sign reversal has no fixed sign sequence. The \(2^t\) sign choices therefore form exactly \(2^{t-1}\) isomorphism classes.

**5. Orbit-exact refinement.** The global translations \((a,z)\mapsto(a,z+v)\) act transitively within each level. Thus no automorphism-invariant refinement can split any \(X_a\). Conversely, the strictly increasing predecessor counts \(p_a\) distinguish the levels already after the first directed counting-refinement step from the uniform initial colour. Its stable classes, and precisely the automorphism orbits, are therefore the levels \(X_0,\ldots,X_{2t}\). In fact, (3) shows that the automorphism group of every member is the translation group of order three.

For \(t=2\), take \(s=(1,1)\) and \(r=(1,-1)\). Equation (3) proves that these fifteen-point orders are nonisomorphic, while (2) proves that their entire counting-refinement and \(C^2\) invariants coincide. Their per-vertex upper-comparison counts from level \(a\) to a later level \(b\), in upper-triangular row order, are \((1,2,2,3)\), \((1,1,2)\), \((1,2)\), and \((1)\).

## Verification
The accompanying standalone standard-library Python programs generate the transitive closures and test the direct subset-sum formula separately. The first checks every sign choice for \(1\le t\le7\), giving 254 finite constructions; it checks the predicted width chains, the common comparison-count table, the stable colour partition, and exhaustively checks level-preserving isomorphisms for \(t\le4\). The second checks 407,646 individual ordered-pair relations by a separately implemented subset-sum calculation against transitive closure. Both pass. These finite tests **corroborate** the argument; they do not replace the proof for arbitrary \(t\).

To reproduce from the embedded files with Python 3, run `python checker.py` and `python formula_check.py` in the same directory. The stored text outputs are `checker_output.txt` and `formula_output.txt`; these contain the recorded results of the two checks.

## Relationship to prior work
Kopczyński and Tan's study of two-variable counting logic (arXiv:1304.0829, first posted 2013-04-03) develops regular/biregular descriptions of finite models and thereby supplies the general mechanism behind counting logic's insensitivity to certain incidence patterns. It does **not**, in the examined full-text sections and model classification, state a width-three strict-poset construction with the exact \(2^{t-1}\) isomorphism spectrum and orbit-exact refinement.

Gajarský, Hliněný, Obdržálek and Ordyniak (arXiv:1409.4433, first posted 2014-09-15) prove fixed-parameter algorithms for existential first-order model checking on bounded-width posets. Their full-text results concern algorithmic model checking and embeddings, not equivalence under unrestricted-rank \(C^2\) or this explicit family. Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255, first posted 2015-02-04) analyze amenability and refinability of undirected graphs and the correspondence with counting logic; the present objects are transitive directed orders, and the isomorphism-fiber count here is not a specialization of the reported graph characterizations. No priority or independence conclusion follows merely from these searches; specific earlier examples might exist under another terminology.

## Limitations
This result does not classify all width-three partial orders or prove that fifteen is the smallest size of a nonisomorphic \(C^2\)-equivalent width-three pair. The exponent counts isomorphism types **inside the defined family** only. All counting-logic statements use ordinary two-variable first-order counting quantifiers and one *strict, transitively closed* binary order; they do not concern the cover graph alone, logics with three variables, or any claimed complexity lower bound. Full-text priority coverage is necessarily finite, and independent scientific review has not been performed.

## References
1. E. Kopczyński and T. Tan, *Regular graphs and the spectra of two-variable logic with counting*, arXiv:1304.0829 (2013), https://arxiv.org/abs/1304.0829.
2. J. Gajarský, P. Hliněný, J. Obdržálek and S. Ordyniak, *Faster existential FO model checking on posets*, arXiv:1409.4433 (2014), https://arxiv.org/abs/1409.4433.
3. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph isomorphism, color refinement, and compactness*, arXiv:1502.01255 (2015), https://arxiv.org/abs/1502.01255.
4. S. Bova, R. Ganian and S. Szeider, *Model checking existential logic on partially ordered sets*, CSL-LICS (2014), https://arxiv.org/abs/1405.2891.
