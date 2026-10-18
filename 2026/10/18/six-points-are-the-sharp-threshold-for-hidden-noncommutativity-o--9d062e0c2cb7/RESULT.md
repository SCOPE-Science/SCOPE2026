# Six points are the sharp threshold for hidden noncommutativity of two relational bijections

## Finding
Let \(X\) be a finite nonempty set, and let \(f,g:X\to X\) be bijections. Regard them as a structure with **two binary relation symbols** \(F,G\), interpreted by \(F(x,y)\iff f(x)=y\) and \(G(x,y)\iff g(x)=y\). The functions are not symbols in the logical language.

**Sharp threshold theorem.** When \(|X|\le5\), commutativity of \(f\) and \(g\) is preserved by equivalence in two-variable first-order logic with counting quantifiers, \(C^2\). At \(|X|=6\), there is a commuting pair and a noncommuting pair whose relational structures satisfy exactly the same \(C^2\) sentences. Thus six is the least domain size at which \(C^2\) equivalence can hide noncommutativity.

**Complete minimal-layer classification.** Among all ordered pairs of permutations of six points, precisely **three** \(C^2\)-equivalence classes contain both commuting and noncommuting structures. Within these three classes the numbers of isomorphism types of commuting versus noncommuting ordered pairs are, respectively, \((4,3)\), \((2,2)\), and \((2,2)\). Each of the three mixed classes has a one-cell stable vertex partition of size six. The enumeration contains 901 simultaneous-conjugacy types of ordered pairs and 860 distinct stable \(C^2\) signatures altogether.

In contrast, three first-order variables suffice to express commutativity in the relational language, by the sentence
\[
\forall x\,\forall y\,\bigl[(\exists z\,[F(x,z)\wedge G(z,y)])\leftrightarrow(\exists z\,[G(x,z)\wedge F(z,y)])\bigr].
\]

## Assumptions and scope
All universes are finite and nonempty. Every interpretation of \(F\) and \(G\) is the graph of a permutation, with no extra symbols or individual constants. Isomorphisms simultaneously conjugate the ordered pair \((f,g)\); they do not exchange the names \(F\) and \(G\). The logical equivalence is full \(C^2\) equivalence (all quantifier ranks, with exact counting). The theorem is a minimum-size and minimal-layer classification, **not** a claim to enumerate all larger indistinguishable pairs.

For \(a,b\in X\), define their **atomic two-type** as the five-bit tuple
\[
\tau(a,b)=(a=b,\ F(a,b),\ F(b,a),\ G(a,b),\ G(b,a)).
\]
The **first-round local counting profile** of \(a\) records, for each of the at most \(32\) atomic two-types \(\tau\), the number of \(b\) with \(\tau(a,b)=\tau\). The first-round profile of the entire structure records the multiplicities of these local profiles.

## Proof
**1. The finite lower bound is exhaustive and logically sound.** For every \(n\in\{1,2,3,4,5\}\), enumerate all \((n!)^2\) ordered pairs of permutations of \(\{0,\ldots,n-1\}\). Compute the atomic two-type count profile at each point and the resulting multiset of point profiles. Separately test \(f(g(x))=g(f(x))\) at every point. The standalone exhaustive enumerator `lower_bound.py` yields the following number of ordered permutation pairs / distinct first-round profiles:
\[
(1,1),\quad(4,4),\quad(36,11),\quad(576,43),\quad(14400,154).
\]
In each size, every first-round structure profile has a unique commutativity truth value. The enumeration is exhaustive because the program iterates over the full permutation list twice, without pruning or random sampling. Every assertion is checked before the PASS line.

To justify the logical implication: for each atomic two-type \(\tau\) and nonnegative integer \(k\), the statement that a point has exactly \(k\) neighbours of type \(\tau\) can be expressed in \(C^2\) as \(\exists^{=k}y\,\tau(x,y)\). Finite conjunctions determine a point profile, and a counting quantifier over \(x\) determines how many points have that profile. Hence \(C^2\)-equivalent structures necessarily have the same first-round structure profile. The computed absence of a mixed profile at sizes at most five proves the lower-bound assertion. `full_pairs.cpp` independently re-enumerates all pairs up to size six, including the same lower-bound checks.

**2. Explicit six-point obstruction.** Take \(X=\{0,1,2,3,4,5\}\) and set
\[
\begin{aligned}
 f&=(1,0,3,2,5,4),\\
 g_{\mathrm c}&=(2,3,4,5,0,1),\\
 g_{\mathrm n}&=(2,4,1,5,3,0),
\end{aligned}
\]
where the entries are images of \(0,1,2,3,4,5\). The pair \((f,g_{\mathrm c})\) commutes. The pair \((f,g_{\mathrm n})\) does not, since \(f(g_{\mathrm n}(0))=3\) and \(g_{\mathrm n}(f(0))=4\).

In **both** six-point structures, **every** point has precisely this atomic two-type distribution: one diagonal point; one point joined in both directions by \(F\) and not by \(G\); one outgoing-only \(G\) point; one incoming-only \(G\) point; and two points with no \(F\) or \(G\) edge in either direction. All listed categories are disjoint. Thus the initial uniform point colour has the same one-class equitable refinement in the two structures and their disjoint union. The standard counting two-pebble-game / colour-refinement equivalence for binary relational structures therefore gives \(C^2\) equivalence. A direct replay in `witness.py` checks every atomic two-type count and the composition inequality.

**3. Exhaustion and classification of the six-point ambiguity.** To avoid counting label changes as new models, fix one standard permutation \(f\) for each of the eleven integer partitions of six (its cycle type), enumerate all \(6!=720\) choices of \(g\), and identify two such choices under conjugation by the centralizer \(C_{S_6}(f)\). This is complete for ordered pairs up to simultaneous conjugation: conjugate the first permutation to standard form and then act by its centralizer. Exactly \(11\cdot720=7920\) presentations reduce to 901 isomorphism types.

For each ordered pair, refine vertex colours by the vector of counts of **atomic two-types into each current colour class**, until stable. Record the sizes of the stable cells and the atomic-two-type transition counts between cells. Sorting the canonically numbered stable cells gives a comparison key for the stable \(C^2\) quotient. The script `six_point_census.py` implements this algorithm, checks explicit simultaneous-conjugacy orbit minima, and verifies by a **joint refinement on disjoint unions** that every commuting/noncommuting representative pair assigned a mixed key really is \(C^2\)-equivalent. It finds 860 keys, exactly three mixed, with commuting/noncommuting isomorphism-type multiplicities \((4,3),(2,2),(2,2)\). Every mixed quotient has a single cell of size six. The independent C++ program `full_pairs.cpp` performs the classification directly on all \(518400=(6!)^2\) labelled ordered pairs, confirming 860 stable signatures and exactly three mixed signatures.

To see that the quotient criterion is complete for this calculation, the counting-two-pebble characterization says that stable colour matching under joint refinement is equivalent to \(C^2\) equivalence for finite binary-relational structures. The three mixed classes have also been directly cross-checked by this joint test, so their existence and multiplicities do not rest on an untested quotient-key converse.

**4. Three-variable expressibility.** The displayed sentence tests, for each \(x,y\), whether some \(z\) witnesses the \(f\)-then-\(g\) composition, exactly when some \(z\) witnesses \(g\)-then-\(f\). Because the relations are graphs of functions, its truth is precisely \(f\circ g=g\circ f\). The six-point pair proves that no \(C^2\) sentence does the same job over all finite relational permutation pairs.

## Verification
The package contains four independent or complementary standalone program sources, together with the actual stdout records generated from those sources:

- `lower_bound.py` / `lower_bound.out`: all \((n!)^2\) ordered permutation pairs for each \(1\le n\le5\), no mixed first-round profile; `LOWER_BOUND_PASS`.
- `witness.py` / `witness.out`: explicit six-point permutation and atomic-type checks; `WITNESS_PASS`.
- `six_point_census.py` / `six_point_census.out`: 7920 reduced presentations, 901 simultaneous-conjugacy types, 860 stable quotient signatures, three mixed classes, plus joint C2 comparisons; `SIX_POINT_CENSUS_PASS`.
- `full_pairs.cpp` / `full_pairs.out`: independent enumeration of all 518400 ordered pairs at six points, independently confirming three mixed stable signatures; `FULL_PAIRS_PASS`. Compile with `c++ -O2 -std=c++17 full_pairs.cpp -o full_pairs` and run `./full_pairs`. The Python programs require only Python 3 standard library.

The decisive size-lower-bound claim is an **exhaustive finite computation**, not an inference from random tests. The lower bound is also independently verified by an implementation using different data representations and a different language. Runtime or successful logging alone is not a proof: correctness additionally rests on the transparent loop coverage, atomic profile definitions, centralizer reduction and logical invariance argument above.

## Relationship to prior work
Kiefer, Schweitzer and Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, develop the relationship between counting logic and graph/relational colour refinement. Their general framework permits the comparison used here but does not itself state the six-point commutativity threshold or the three minimal mixed equivalence classes.

Moreno and Rivera, *Blocks in cycles and k-commuting permutations*, arXiv:1306.5708, study permutations that commute or nearly commute in a counting/Hamming-distance sense, not logical indistinguishability of ordered pairs of relational permutation graphs.

Albert, Bouvel and Féray, *Two first-order logics of permutations*, arXiv:1808.05459, consider different permutation-logical encodings; their examined formulation does not provide this two-named-binary-relation, two-variable-counting threshold. Mathematical implication rather than paper-title similarity is the basis of these comparisons.

## Limitations
The precise scope is pairs of named **binary relation graphs of bijections**. If \(f,g\) are available as *function symbols*, nested terms can already compare \(f(g(x))\) and \(g(f(x))\) with one variable, so this theorem is not about that different syntax. The minimal-layer census is restricted to six points; it does not enumerate larger models or establish asymptotic prevalence. Although no equivalent assertion was identified in the inspected primary material and research records, specialized prior coverage may exist. No independent scientific audit or publication-priority certification has been performed.

## References
1. S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, first publicly submitted 2015-03-30. https://arxiv.org/abs/1503.08792
2. L. Moreno and A. Rivera, *Blocks in cycles and k-commuting permutations*, arXiv:1306.5708v1, first publicly submitted 2013-06-24. https://arxiv.org/abs/1306.5708
3. M. Albert, M. Bouvel, and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459v1. https://arxiv.org/abs/1808.05459
