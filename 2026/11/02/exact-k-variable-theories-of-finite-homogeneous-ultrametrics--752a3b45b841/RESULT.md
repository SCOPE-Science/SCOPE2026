# Exact \(k\)-variable theories of finite homogeneous ultrametrics

## Finding
Fix an integer \(h\ge1\), positive real distance levels \(r_1>\cdots>r_h\), and integer branching vectors \(\mathbf b=(b_1,\ldots,b_h)\) with \(b_i\ge2\). Let \(U(\mathbf b)\) be the finite leaf set \(\prod_{i=1}^h\{0,\ldots,b_i-1\}\). Distinct leaves have distance \(r_i\) if their first differing coordinates occur at position \(i\). Regard the space as a relational structure with equality and one binary distance-level predicate \(R_i\) for each \(i\), so \(R_i(x,y)\) holds exactly when \(d(x,y)=r_i\).

**Theorem (exact classification).** For every integer \(k\ge2\), every fixed height \(h\), and all such vectors \(\mathbf b,\mathbf c\), the following are equivalent:

\[
U(\mathbf b)\equiv_{\mathrm{FO}^{k}}U(\mathbf c)
\quad\Longleftrightarrow\quad
\min(b_i,k)=\min(c_i,k)\quad(1\le i\le h).
\]

The logic permits arbitrarily deep formulas using at most \(k\) distinct variable symbols and no counting quantifiers. For fixed \(h,k\), there are exactly \((k-1)^h\) theories in the family, with a smallest representative obtained by replacing each branching number by \(\min(b_i,k)\). Every theory has a representative with at most \(k^h\) leaves; this uniform bound is sharp. For two distinct branching vectors, the minimum number of variable symbols in an ordinary first-order sentence separating the structures is

\[
\min_{1\le i\le h:\, b_i\ne c_i}\bigl(\min(b_i,c_i)+1\bigr).
\]

By contrast, the two-variable language **with counting quantifiers** distinguishes every two different branching vectors: \(U(\mathbf b)\equiv_{C^2}U(\mathbf c)\) exactly when \(\mathbf b=\mathbf c\).

## Assumptions and scope
The height, ordered level names \(R_1,\ldots,R_h\), and the strictly decreasing distance values are fixed and common to all compared structures. The underlying domain consists of leaves only: internal balls or tree nodes are **not** named as elements. A predicate \(R_i\) is false on the diagonal. The theorem does not claim equivalence when heights or relational signatures differ. Branch numbers are arbitrary integers at least two, and \(k\) is any fixed integer at least two, with no bound on quantifier rank.

## Proof
**1. A definable obstruction when one truncated degree differs.** Suppose \(\min(b_i,k)\ne\min(c_i,k)\). By interchanging the spaces if necessary, take \(b_i<c_i\) with \(b_i<k\). Put \(t=b_i+1\le k\). The sentence

\[
\exists x_1\cdots\exists x_t\;
\bigwedge_{1\le a<b\le t}R_i(x_a,x_b)
\]

holds in \(U(\mathbf c)\) and fails in \(U(\mathbf b)\). Indeed, any set of leaves pairwise at distance \(r_i\) must share their initial \(i-1\) coordinates and have pairwise distinct \(i\)-th coordinates; conversely any \(t\) distinct children at a common level-\(i\) parent yield such a set. Hence the maximum such set size is exactly \(b_i\) or \(c_i\).

**2. The extension lemma.** Let \(A=U(\mathbf b)\) and \(B=U(\mathbf c)\) have identical truncated degree vectors. Suppose \(m<k\) pebbled positions in \(A,B\) have the same equality and distance-level relations. These relations encode the shared rooted prefix tree on the at most \(m\) distinct occupied leaves. For any new source leaf \(x\), construct a target leaf \(y\) one coordinate at a time. At a parent prefix visited by some occupied leaves, if \(x\) enters a child already containing an occupied leaf, take the corresponding child in the target. Otherwise, take a child unoccupied by the retained pebbles. The latter always exists: at most \(m\le k-1\) children are occupied, and, when an unused source child exists, the number of occupied children is strictly smaller than \(b_i\). If \(b_i<k\), truncation equality gives \(b_i=c_i\) and the same unused capacity; if \(b_i\ge k\), then \(c_i\ge k\), so the target has at least one unused child. At a parent prefix not occupied by retained leaves, choose any continuation. Thus \(y\) has precisely the same distances to all retained pebbled leaves as \(x\) does. The construction also matches equality: if \(x\) is an occupied leaf, the corresponding target leaf is chosen; if not, the first separating child remains separate. It works symmetrically with \(A,B\) exchanged.

**3. Unlimited play.** In each round of the \(k\)-pebble back-and-forth game, remove the selected pebble, leaving at most \(k-1\) pebble positions. Apply the extension lemma on the side where Spoiler moves. Equality and all named distance relations remain preserved. The strategy is independent of the number of rounds; therefore Duplicator wins every finite \(k\)-pebble game. The standard pebble-game characterization yields equality of all \(\mathrm{FO}^{k}\) sentences, without a quantifier-rank bound.

**4. Exact number of theories and representatives.** Each \(\min(b_i,k)\) takes precisely one of \(2,3,\ldots,k\). By part 1, every pair of different truncated vectors is separated, while parts 2–3 identify precisely the matching ones. Hence the number of theories is \((k-1)^h\). In each class the unique coordinatewise-smallest branching vector is \((\min(b_i,k))_i\), and cardinality is the product of its coordinates. The maximal minimum is \(k^h\), attained by the class with all coordinates at least \(k\). The minimum separating variable width formula follows by taking the least \(k\) for which a truncated coordinate differs.

**5. Counting-logic contrast.** Fix a leaf \(x\). The number of leaves \(y\) satisfying \(R_i(x,y)\) is

\[
N_i=(b_i-1)\prod_{j=i+1}^{h}b_j.
\]

These cardinalities are expressible by two-variable counting sentences \(\forall x\,\exists^{=N_i}y\,R_i(x,y)\). They recover the vector recursively from the bottom: \(b_h=N_h+1\) and \(b_i=1+N_i/\prod_{j>i}b_j\) for \(i=h-1,\ldots,1\). Thus two distinct vectors have distinct \(C^2\) theories; identical vectors give isomorphic structures.

## Verification
The standalone standard-library script `verify.py` exhaustively checks all distinct-tuple distance types at widths two through four for 21 small structures, performing 210 pair/width comparisons with the proposed truncated vector rule. It checks bottom-up reconstruction of each degree vector from counting annuli. It also exhaustively tests the required two-way extension property on 120,068 compatible partial isometries across four representative parameter pairs. Run `python verify.py` from the directory containing this result; expected output is recorded verbatim in `verification_output.txt`. These finite computations corroborate, and do not substitute for, the proof applying to all heights and degrees.

## Relationship to prior work
Delhomme–Laflamme–Pouzet–Sauer study homogeneous ultrametric spaces and tree-of-balls representations; their full article gives homogeneity and degree information but does not state the present precise unrestricted \(\mathrm{FO}^{k}\)-classification or the sharp representative and counting-logic contrast. Immerman–Kozen's finite-variable work treats bounded-variable theory and trees, but not this exact family of leaf-only level-labelled metric structures. Grohe–Otto give the general logical and game-theoretic machinery but not the numerical levelwise classification. The exact claim has been compared with relevant accessible research records and searches for nested equivalence, homogeneous ultrametric, and truncated branching formulations. This is a qualified best-knowledge priority assessment, not proof of novelty; a broader published tree/finite-variable result could still imply the theorem.

## Limitations
The result requires uniform branching at each distance level and names every exact distance level. It does not classify arbitrary nonhomogeneous ultrametrics, variable-length distance spectra, metric languages lacking level predicates, or games with counting. The counting observation explicitly changes the logic; it is not an extension of the noncounting equivalence. Small-scale checks are finite only. Historical novelty and correctness have not undergone an independent audit.

## References
1. C. Delhomme, C. Laflamme, M. Pouzet, and N. Sauer, *On homogeneous ultrametric spaces*, arXiv:1509.04346, first public version 2015-09-14. https://arxiv.org/abs/1509.04346
2. N. Immerman and D. Kozen, *Definability with Bounded Number of Bound Variables*, *Information and Computation* 83 (1989), 121–139. https://www.cs.cornell.edu/~kozen/Papers/bbv.pdf
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, LIPIcs 16, 289–304. https://drops.dagstuhl.de/storage/00lipics/lipics-vol016-csl2012/LIPIcs.CSL.2012.289/LIPIcs.CSL.2012.289.pdf
