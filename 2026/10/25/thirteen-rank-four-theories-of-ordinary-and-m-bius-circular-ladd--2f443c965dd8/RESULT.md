# Thirteen rank-four theories of ordinary and Möbius circular ladders

## Finding
For every integer \(n\ge3\) and twist bit \(\epsilon\in\{0,1\}\), let \(L_n^\epsilon\) be the ordinary circular ladder when \(\epsilon=0\) and the Möbius ladder when \(\epsilon=1\), as defined precisely below. In first-order logic with adjacency and equality, and without named vertices or coordinates,
\[
L_n^\epsilon\equiv_4 L_m^\eta
\quad\Longleftrightarrow\quad
\bigl(n,m\ge9\bigr)\ \lor\
\bigl(3\le n=m\le8\ \land\ \epsilon=\eta\bigr).
\]
Thus the two infinite ladder families together have exactly **thirteen** distinct quantifier-rank-four theories: the twelve individual graphs at rung lengths three through eight, and one common class of all ordinary and twisted ladders with at least nine rungs. Every class has a representative on at most eighteen vertices; eighteen is optimal within this union of families.

## Assumptions and scope
All graphs are finite, simple, undirected, and loopless. Define \(L_n^\epsilon\) on \(\{0,\ldots,n-1\}\times\{0,1\}\). There is a rung between \((i,0)\) and \((i,1)\) for each column. For \(0\le i<n-1\), each \((i,s)\) is adjacent to \((i+1,s)\). The closing edge from column \(n-1\) joins \((n-1,s)\) to \((0,s\oplus\epsilon)\). These are cubic graphs on \(2n\) vertices. The case \(\epsilon=0\) is \(C_n\square K_2\); the case \(\epsilon=1\) is the \(2n\)-vertex Möbius ladder, equivalently a cycle on \(2n\) vertices with antipodal chords. Our rank notion is maximum quantifier nesting depth, not the number of variables in a formula or the counting-logic rank.

## Proof
**Exact logical types.** For a tuple \(\bar a\), let \(A(\bar a)\) be its complete equality-and-adjacency diagram. Define recursively
\[
T_0(\bar a)=A(\bar a),\qquad
T_{r+1}(\bar a)=\bigl(A(\bar a),\{T_r(\bar a,x):x\in V\}\bigr).
\]
The standard induction on formulas shows that two tuples have identical \(T_r\) precisely when they satisfy the same first-order formulas of quantifier rank at most \(r\), with the tuple as parameters. In particular \(T_4(())\) is a complete invariant of the rank-four theory. Equality and repeated vertex choices are retained at every extension step.

**Uniform locality lemma.** For all \(n,m\ge16\) and all twist bits, \(L_n^\epsilon\equiv_4L_m^\eta\). To see this, classify \(T_2(a,b)\) by the cyclic distance \(\delta\) of the columns containing \(a,b\), together with their relative layer positions when \(\delta\le4\). The possible states are \(\delta=0,1,2,3,4\) and a single remote state \(\delta\ge5\). For \(\delta=0\), also distinguish \(a=b\) from the two distinct vertices on the same rung.

Here is why this is exhaustive. For any triple of chosen vertices, its one-step extension type \(T_1(a,b,c)\) is determined by its atomic diagram and which of the eight adjacency patterns of a fourth, *new* vertex are realizable. A fourth vertex equal to an old one is accounted for directly by equality and the atomic diagram. The all-nonadjacent new-vertex pattern always occurs: at most twelve vertices lie in the three closed neighborhoods, whereas \(2n\ge32\). Any other new-vertex pattern has a witness adjacent to at least one of the triple; two selected vertices can have a common neighbor only if their column distance is at most two.

For fixed \(a,b\), a third selected vertex \(c\) can consequently affect the extension diagram jointly with \(a\) or \(b\) only when its column is within cyclic distance two of the corresponding marked column. All other choices of \(c\) give a single remote extension pattern, and they exist because two radius-two column windows cover at most ten columns, fewer than \(n\). If the columns of \(a,b\) are within distance four, the relevant windows and their adjacent witnesses are contained in an arc of at most eleven consecutive columns. Since \(n\ge16\), this arc does not wind around the closing identification; a change of the layer coordinate within the arc removes the twist. Thus the set of \(T_1(a,b,c)\) depends only on the indicated short pair state. If the columns are at distance at least five, their radius-two windows are disjoint. A \(c\) near one of them has no common-neighbor interaction with the other, so every such remote pair has the same set of \(T_1(a,b,c)\), regardless of the twist or the long column separation.

Therefore these descriptions determine \(T_2(a,b)\) uniformly across all ordinary and twisted ladders with \(n\ge16\). Every vertex \(a\) realizes all the indicated short pair states and the remote state by suitable choices of \(b\). Hence the set of pair types, and thus \(T_3(a)\), is the same for every vertex in every such graph. Taking the set over all \(a\) gives identical \(T_4(())\), as claimed. This is an infinite statement, not an inference from numerical samples.

**Exact finite bridge and separation.** It remains to cover \(3\le n\le15\). The included program `verify.py` constructs \(T_4(())\) by the recurrence above for both twists and every rung number \(3\le n\le16\), using full sets of exact finite tuples, not hash equality or sampling. It finds twelve pairwise distinct types for the ordinary and twisted ladders at \(3\le n\le8\), none equal to the common type at \(n=9\); both twists at every \(9\le n\le16\) have exactly that common type. By the uniform locality lemma, the common type continues for all \(n\ge16\). This proves the displayed equivalence and the class count.

Finally every graph with \(n\le8\) has at most sixteen vertices and is in an isolated class; the common class has its first representative at \(n=9\), with eighteen vertices. Since all graphs in the stipulated family have even order, and the finite census excludes all twelve smaller candidates, eighteen is the sharp maximum minimum representative size.

## Verification
Run `python verify.py` with standard Python 3. The executable uses exact finite logical-type sets, including repeated selected vertices and quantifiers that alternate existential and universal (universal formulas are determined by complements of realized extension types). It checks all twenty-eight graphs with rung numbers three through sixteen, finds thirteen types, and performs supplementary checks for seventeen through twenty-four rungs in both families. Run `python direct_game.py` for a separate adversarial four-round game oracle, which confirms that the eight-rung ordinary and twisted graphs are distinguishable and the nine-rung graphs are not. Successful recorded outputs are in `verification_output.txt` and `direct_game_output.txt`. The infinite locality lemma is essential to the proof; neither finite computation by itself proves the claim for arbitrarily large rung counts.

## Relationship to prior work
Brown and Hoshino (2007, Section 4, Theorem 4.1) classify the four-round theories of the *individual cycle graphs*, obtaining the cycle stabilization threshold eleven. Their theorem does not apply to the cubic ladders or to the twist choice and does not imply the shared nine-rung threshold. Heinig (2011, arXiv:1112.5101v1, Sections 1 and 2) studies prisms and Möbius ladders in connection with Hamiltonian generation of cycle spaces, not bounded-rank first-order theories. Exact four-round classification for these two graph families, including their common eventual theory and sharp minimum representative, was not found in the examined sources. These comparisons concern logical implications, not merely differences in titles.

## Limitations
The classification concerns ordinary first-order logic with only adjacency and equality, **exactly quantifier rank four**, and precisely the two graph families defined here. It does not determine their higher-rank theories, distinguishability in counting logic, or a sharp representative bound among arbitrary graphs. The finite computation is exhaustive only for the stated finite range. The originality comparison is limited by publication indexing and access; independent scientific evaluation has not been performed.

## References
1. J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212, especially Section 4. Open full text: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf (publicly listed 2007-04-30).
2. P. C. Heinig, *On prisms, Möbius ladders and the cycle space of dense graphs*, arXiv:1112.5101v1 (first public version 2011-12-21), https://arxiv.org/html/1112.5101v1.
