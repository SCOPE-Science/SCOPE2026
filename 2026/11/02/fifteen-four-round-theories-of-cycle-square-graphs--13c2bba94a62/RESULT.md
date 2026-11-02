# Fifteen four-round theories of cycle-square graphs

## Finding
For each integer \(n\ge5\), define the finite simple graph \(S_n\) on \(\mathbb Z/n\mathbb Z\) by joining distinct residues precisely when their cyclic distance is one or two. Equivalently, \(S_n=C_n^2\), the square of the undirected cycle. In ordinary first-order logic with equality and the single undirected adjacency predicate, the complete quantifier-rank-four classification is

\[
S_m\equiv_4 S_n\quad\Longleftrightarrow\quad
(m=n<19)\ \lor\ (m,n\ge19)
\qquad(m,n\ge5).
\]

Thus this infinite family has exactly fifteen rank-four theories: fourteen singleton parameter classes for \(n=5,\ldots,18\), and one class containing every \(n\ge19\). Its sharp within-family smallest-representative bound is nineteen vertices.

## Assumptions and scope
The language has no vertex names, orientation, order, distance predicate, counting quantifiers or parameters. Quantifier rank means the greatest nesting depth of first-order quantifiers. For all \(n\ge5\), \(S_n\) is a simple four-regular graph on \(n\) vertices. The claim compares different members of this family, not arbitrary graphs having the same degree.

## Proof
**Infinite tail from a one-quantifier interpretation.** Write \(E_C\) for cycle adjacency and \(E_S\) for square-graph adjacency on a common domain. For every \(n\ge5\), the latter relation is interpreted in the original cycle by

\[
E_S(x,y)\quad\longleftrightarrow\quad x\ne y\ \land\ \bigl(E_C(x,y)\lor\exists z\,(E_C(x,z)\land E_C(z,y))\bigr).
\]

The inequality is necessary because the two-step condition alone would admit loops. Replace every square-graph adjacency atom in a first-order formula \(\varphi\) by the right side, choosing each bound variable \(z\) fresh. A structural induction on \(\varphi\) shows that the translated formula \(\varphi^*\) has the same truth value on the original cycle and satisfies \(\operatorname{qr}(\varphi^*)\le\operatorname{qr}(\varphi)+1\). Boolean operations preserve the bound; each original quantifier adds one to the inductive depth. Brown and Hoshino's cycle theorem (Theorem 4.9, 2007) says that all undirected cycles of lengths at least \(2^{q-1}+3\) agree at quantifier rank \(q\), for \(q\ge3\). At \(q=5\), the threshold is nineteen. Consequently all \(S_n\) with \(n\ge19\) agree at rank four.

**Finite separation via exact types.** For any graph \(G\), ordered tuple \(\mathbf a\) (allowing repeated vertices) and integer \(r\ge0\), define its atomic diagram \(A_G(\mathbf a)\) to list, in a fixed order, the equality and adjacency status of every coordinate pair. Define inductively

\[
\tau_0^G(\mathbf a)=A_G(\mathbf a),\qquad
\tau_{r+1}^G(\mathbf a)=\left(A_G(\mathbf a),\ \{\tau_r^G(\mathbf a,b):b\in V(G)\}\right).
\]

For tuples of the same length, equality of these recursively formed finite objects is equivalent to agreement on all first-order formulas of rank at most \(r\) with the corresponding free variables. This follows by induction: atomic formulas determine \(\tau_0\), and a formula with one leading existential quantifier tests membership of an extension type; a universal quantifier is its Boolean dual. Hence two finite structures agree on all rank-four sentences exactly when their empty-tuple \(\tau_4\) objects agree.

Applying this exact recursion to all ordered tuples of up to four vertices in \(S_n\), for each \(5\le n\le19\), gives fifteen pairwise distinct empty-tuple types. The accompanying direct finite enumerator implements the recurrence on all ordered tuples, and a second enumerator uses only dihedral orbit representatives. Both independently intern atomic diagrams and finite extension-type sets, with identical pairwise equality results through \(n=32\). Full output and compilation commands are supplied in the verification files. Thus every \(S_n\) for \(5\le n\le18\) differs at rank four from every other such graph and from \(S_{19}\). The infinite-tail argument completes the classification.

Since each exceptional theory has only one family member and the common tail starts at nineteen, the maximum of the smallest orders of family representatives is exactly nineteen.

## Verification
Run \(\texttt{sh verify.sh}\) in the directory containing the two C++ files. It compiles them using a C++17 compiler and checks the stated partition independently by complete ordered-tuple enumeration through \(n=32\) and symmetry-reduced enumeration through \(n=72\). The script also checks a secondary structural observation: the induced adjacency patterns of four distinct selected vertices stabilize already at \(n=12\). An elementary proof of this observation increases or decreases a cyclic gap of length at least three among four selected points; doing so cannot change adjacency, which is determined by cyclic distances at most two. For \(n\ge12\), such a gap exists, and for \(n>12\) some gap has length at least four, allowing reduction to twelve. Thus short existential witnesses stabilize earlier than the full rank-four theories.

The executable recurrence is an exhaustive finite computation, not by itself a proof about unbounded cycle lengths. The published cycle theorem plus the displayed interpretation supply that missing infinite argument.

## Relationship to prior work
Brown and Hoshino (2007), Theorem 4.9, completely classify first-order bounded-rank equivalence of ordinary undirected cycles. In particular, their rank-five bound supplies the present infinite-tail implication after one additional adjacency-definition quantifier; it does not state the finite rank-four partition of the square graphs. Macêdo Filho, Dantas, Machado and de Figueiredo (2012) investigate powers of paths and cycles, including an explicit structural description of their bicliques; their objectives and conclusions concern biclique colourings, not equality of first-order rank-four theories. The present finite separation supplies the sharpness and the fifteen-class count beyond the earlier upper-bound implication.

## Limitations
The proof concerns only the natural nondegenerate four-regular cycle-square family \(n\ge5\) and ordinary first-order graph logic at rank four. It makes no claim about arbitrary cycle powers, higher ranks, counting logic, or arbitrary four-regular graphs. The arithmetic cutoff follows from the cited undirected-cycle theorem. The distinctness of the fourteen finite exceptional cases has exact computational proof via the supplied short general recurrence and source code; no compact human-readable list of fifteen separating sentences is supplied. Literature searches and inspections cannot guarantee historical priority.

## References
1. Jason Brown and Richard Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212, Theorem 4.9, published April 30, 2007. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. H. B. Macêdo Filho, S. Dantas, R. C. S. Machado and C. M. H. de Figueiredo, *Biclique-colouring verification complexity and biclique-colouring power graphs*, first public arXiv version March 12, 2012, https://arxiv.org/abs/1203.2543
