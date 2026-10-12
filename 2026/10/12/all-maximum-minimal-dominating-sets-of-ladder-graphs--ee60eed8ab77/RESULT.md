# All maximum minimal dominating sets of ladder graphs

## Finding
Let \(L_n=P_2\square P_n\) be the ordinary (Cartesian, **not strong-product**) ladder on two labeled rows and \(n\ge2\) columns. A set is *minimal dominating* if it dominates all vertices and none of its proper subsets dominates. Its upper domination number \(\Gamma(L_n)\) is the maximum size of such a set.

**Theorem.** For every integer \(n\ge2\), one has \(\Gamma(L_n)=n\). Every minimal dominating set of cardinality \(n\) is represented by exactly one of the following column-mask words (mask \(1\) selects the upper vertex, mask \(2\) the lower vertex, mask \(3\) both, and mask \(0\) neither):

1. The four words obtained by truncating one of the infinite periodic words \(1111\cdots\), \(2222\cdots\), \(1212\cdots\), and \(2121\cdots\) after \(n\) columns.
2. **Only if \(n\) is even**, the two words obtained by truncating \(30033003\cdots\) and \(03300330\cdots\) after \(n\) columns.

All listed words are distinct for \(n\ge2\). Hence the number \(U_n\) of maximum minimal dominating sets is exactly
\[
U_n=\begin{cases}4,&n\ge3\text{ odd},\\6,&n\ge2\text{ even}.\end{cases}
\]
For completeness, \(L_1=K_2\) has exactly two maximum minimal dominating sets, each of size \(1\). Thus the coefficient of \(z^n\) in the *minimal-domination polynomial* \(\sum_{D\text{ minimal dominating}}z^{|D|}\) is \(U_n\). This is an **upper** extremal-set count, not the number of minimum dominating sets.

## Assumptions and scope
The graph is finite, simple, and consists of two copies of the path with edges between corresponding vertices. Vertices are individually labeled by row and column. A selected vertex \(v\) has a *private closed neighbor* if some \(w\in N[v]\) satisfies \(N[w]\cap D=\{v\}\). It is elementary that a dominating set is inclusion-minimal exactly when every selected vertex has a private closed neighbor. No conjecture on larger-width grids is asserted.

## Proof
We give a finite-state proof with a complete, independently replayable certificate rather than an unchecked extrapolation from small examples. A finite verification of an automaton **identity** is a proof for all word lengths, unlike checking only finitely many graphs.

**Local characterization.** Encode each column by a mask in \(\{0,1,2,3\}\) and pad the word with two nonexistent columns on each end, denoted by the distinct symbol \(\bot\). To decide both domination and the private-neighbor condition for the two vertices in column \(i\), it is sufficient to inspect columns \(i-2,\ldots,i+2\): any possible private neighbor lies in column \(i-1\), \(i\), or \(i+1\), and that neighbor's closed neighborhood lies inside this five-column window. Treating \(\bot\) as *absent vertices*, and not as empty existing columns, handles the endpoints exactly. Let \(Q(a,b,c,d,e)\) denote the Boolean predicate that every real vertex in central column \(c\) is dominated and each selected central vertex has a private closed neighbor. The accompanying verifier implements this definition literally from grid adjacencies; it does not use the claimed pattern formula.

**Weighted finite automaton.** States are the \(5^4=625\) four-symbol windows \(s=(a,b,c,d)\). A transition labeled \(e\in\{0,1,2,3\}\) goes to \(t=(b,c,d,e)\) precisely if \(Q(a,b,c,d,e)\) holds. Its integer gain is \(g=\operatorname{popcount}(e)-1\). The initial state is \((\bot,\bot,\bot,\bot)\). A state is terminal if appending two padding symbols passes both remaining central-column tests. Therefore accepting paths with exactly \(n\) real transitions are in bijection with minimal dominating sets of \(L_n\), and the sum of their gains is \(|D|-n\).

**Upper bound and equality witness.** The supplied certificate constructs an integer potential \(R\) on all \(625\) states by two rounds of the finite Bellman maxima, initialized to \(0\) at terminal states and to a fixed sufficiently negative integer elsewhere. It then **checks all** inequalities
\[
R(s)\ge g(s,t)+R(t),\qquad R(s)\ge0\quad\text{for terminal }s,
\qquad R(s_0)=0.
\]
These inequalities alone are sufficient for the proof and are exactly tested in the executable, so no assumption about approximate convergence is needed. Telescoping along an accepted word gives \(|D|-n\le R(s_0)-R(s_f)\le0\). The four single-vertex-per-column words are directly accepted and have \(n\) selected vertices. Consequently \(\Gamma(L_n)=n\).

Every accepted word of size \(n\) must have equality in every potential inequality on its path and must end at a terminal state with \(R=0\). Call such transitions *tight*. This necessity is a direct consequence of summing nonnegative integer slacks, not a numerical heuristic. Conversely every tight accepting word reaches size \(n\).

**Complete classification.** Construct a second finite automaton recognizing the six periodic families stated in the theorem: it tracks which of the six prescribed periodic words still agree with the prefix, the length modulo four, and whether the length is zero, one, or at least two. Taking the synchronous product with the tight-transition automaton, a breadth-first traversal visits exactly \(41\) reachable product states and checks equality of the two accepting predicates at **every** one; it also traverses all \(46\) reachable product transitions. Exhaustive product-state closure proves equality of the languages for *every* finite length by induction on word length. In particular, the two full/empty-column words are admissible exactly at even positive lengths, while the four singleton-column words are admissible for all \(n\ge2\). Their distinctness gives the stated counts.

The verifier supplies the literal local graph predicate, the potential computation and inequality checks, and the product-language equivalence check. These finite certificates establish the theorem unconditionally when run under exact integer and Boolean arithmetic; they are not reliance on an unproved pattern observed in a finite census.

## Verification
Run `python3 ladder_upper_certificate.py` from the directory containing this file. It requires Python 3 standard library only. The program tests \(625\) exact potential inequalities and terminal conditions, compares the entire reachable tight automaton against the periodic-language recognizer, and separately enumerates all \(n\)-vertex subsets of the actual \(2n\)-vertex graph for \(1\le n\le10\). The independent graph-level test uses closed neighborhoods and deletion-minimality and does not call the local-window predicate. The actual output appears in `certificate_output.txt`.

The infinite conclusion comes from the verified **finite-state language equivalence** and potential inequalities; the small exhaustive census is a separate consistency check, not the basis for the infinite claim.

## Relationship to prior work
Su, Allagan, Gao, Malomo, Gao, and Eyob (2024) analyzed *minimum* dominating sets of rectangular grids, including ladder minimum-set counts. The quantity here is fundamentally different: it counts *maximum-cardinality inclusion-minimal* dominating sets. Sahbi (2026) determines the upper-domination **cardinality** of rectangular grids, including ladders, by the bipartite identity \(\Gamma=\alpha\). This scalar conclusion is already known and is not a novelty claim here. OEIS A290379 tabulates the **total** number of minimal dominating sets of ladders; knowing the evaluation of their generating polynomial at \(1\) does not determine the coefficient of highest degree. The new object is the entire equality-case classification and the corresponding top-coefficient count.

## Limitations
The classification is specific to two-row Cartesian grid graphs and to maximum-cardinality minimal dominating sets. It does not enumerate all minimal dominating sets of each smaller size, nor extend to cylindrical or higher-width grids. The proof is computer-assisted but finite and exact, with source code included; no independent external audit has been conducted. Exact equivalent descriptions could have escaped the literature search, especially in generalized upper-domination polynomial terminology or in inaccessible later portions of the 2026 preprint.

## References
1. J. Su, J. Allagan, S. Gao, O. Malomo, W. Gao, and E. Eyob, *Dominion on Grids*, Mathematics **12** (2024), 3408, DOI: 10.3390/math12213408. First publicly dated 2024-10-31; primary MSC 05C69.
2. R. Sahbi, *Upper Domination in Rectangular Grid Graphs and Its Relation to Sub-Quorum Colorings*, arXiv:2610.03785 (first posted 2026-09-30). Scalar upper domination of grids.
3. OEIS A290379, *Number of minimal dominating sets in the n-ladder graph*; known total-set sequence and recurrence.
4. E. W. Weisstein, *Upper Domination Number*, MathWorld, for the classical parameter definition.
