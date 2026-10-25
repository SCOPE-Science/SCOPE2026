# An eight-state Young-graph family resolving the \(Y(8,5)\) isomorphism conjecture

## Finding
For every integer \(n\ge3\), put \(g=n^2-1\) and \(k=n^2-n-1\). The Young graph for base \(g\) and multiplier \(k\), including its distinguished initial vertex and its even- and odd-pivot structure, is isomorphic to \(Y(8,5)\):
\[
Y(n^2-1,n^2-n-1)\cong Y(8,5)\qquad(n\ge3).
\]
This proves Conjecture 3 in Section 6.1 of Kendrick, *Young Graphs: 1089 et Al.*. Each graph has eight carry-state vertices and sixteen carry-state edges, in addition to the initial vertex and initial edge. Hence, by the previously known enumeration for \(Y(8,5)\), the number \(R_{g,k}(d)\) of positive base-\(g\) integers with exactly \(d\) digits whose product by \(k\) has reversed digits satisfies
\[
\sum_{d\ge0}R_{g,k}(d)z^d=\frac{z^4(1+z)}{1-2z^2}.
\]
In particular, for every \(t\ge2\), \(R_{g,k}(2t)=R_{g,k}(2t+1)=2^{t-2}\); the counts are zero at shorter lengths.

## Assumptions and scope
A base-\(g\), multiplier-\(k\) reverse multiple is a positive integer whose base-\(g\) digits reverse when multiplied by \(k\). The Young graph is the trimmed directed carry-pair graph: its noninitial vertices are the reachable carry pairs lying on a path to an even or odd pivot. An even pivot is a carry pair with equal coordinates. An odd pivot is a carry pair with an outgoing edge to the pair with coordinates interchanged. An initial edge requires both outer digits to be nonzero. The isomorphism asserted here preserves the initial node, directed adjacency, and which vertices are even and odd pivots; it does not identify the numeric digit labels at different bases.

Write
\[
a=n-2,\quad b=n(n-2),\quad c=(n+1)(n-2)=k-1,\quad g=k+n.
\]
The eight named carry states are
\[
O=(0,0),\ B=(0,b),\ A=(a,a),\ D=(a,c),\ E=(b,0),\ F=(b,b),\ G=(c,a),\ H=(c,c).
\]
They are pairwise distinct for every \(n\ge3\), including the boundary case \(n=3\).

## Proof
**Carry equations.** An edge from \((L,R)\) to \((L',R')\), reading its outer left digit \(v\) and outer right digit \(u\), is permitted exactly when
\[
ku+R=v+gR',\qquad kv+L'=u+gL,
\]
with \(0\le u,v<g\) and \(0\le L',R'<k\). Consequently, on setting \(v=L+h\),
\[
L'=u+nL-kh,\qquad u\equiv n(R-L-h)\pmod g,
\]
since \(k=g-n\) and \(n^2\equiv1\pmod g\). For every \(0\le u<g\) and \(0\le R<k\), the quotient \(R'=\lfloor(ku+R)/g\rfloor\) automatically lies between \(0\) and \(k-1\). Thus the interval on \(L'\) is the only remaining carry bound. The bounds on \(u,L,L'\) force \(0\le h\le n\): negative \(h\) forces \(L'\ge k\), and \(h\ge n+1\) forces \(L'<0\).

**Exclusion of all unwanted edges.** At each of the eight proposed states, \(n(R-L)\) is congruent modulo \(g\) to a representative \(t\in\{0,a,-a\}\). The respective unique digits \(u\in\{0,\ldots,g-1\}\) are, for \(0\le h\le n\),
\[
\begin{array}{c|ccc}
t & h=0 & 1\le h\le n-1 & h=n\\\hline
0 & 0 & g-nh & g-1\\
a & a & g+a-nh & a-1\\
-a & g-a & g-a-nh & g-n+1
\end{array}
\]
For states with \(L=0\) or \(L=a\), the corresponding \(t\) is \(0\) or \(a\), and the inequality \(0\le L'<k\) allows precisely \(h=0,1\). Indeed, for \(2\le h\le n-1\), \(L'=nL+t+g(1-h)<0\), while at \(h=n\) it is again negative; at \(h=0,1\) it equals \(nL+t\), which lies between \(0\) and \(k-1\). (For \(n=3\), the possibly empty intermediate range causes no exception.)

For states with \(L=b\) or \(L=c\), the corresponding \(t\) is \(0\) or \(-a\). Here \(nL=ga+e\), with \(e=a\) if \(L=b\) and \(e=c\) if \(L=c\). Substitution gives \(L'\ge k\) at \(h=0\) and at \(1\le h\le n-2\), while exactly \(h=n-1,n\) yield \(L'=e+t\in\{0,a,b,c\}\). All admitted digits satisfy \(0\le v=L+h<g\). Thus each proposed state has exactly two permitted outgoing edges.

**The entire labeled transition table.** The entries list the destination, followed by the ordered digits \((v,u)\). The letters are state identifiers only.

| Source | First outgoing edge | Second outgoing edge |
|---|---|---|
| O | O: \((0,0)\) | B: \((1,k)\) |
| B | A: \((0,a)\) | D: \((1,g-2)\) |
| A | E: \((a,0)\) | F: \((a+1,k)\) |
| D | G: \((a,a)\) | H: \((a+1,g-2)\) |
| E | O: \((k,1)\) | B: \((k+1,k+1)\) |
| F | A: \((k,n-1)\) | D: \((k+1,g-1)\) |
| G | E: \((k+a,1)\) | F: \((g-1,k+1)\) |
| H | G: \((k+a,n-1)\) | H: \((g-1,g-1)\) |

The initial carry pair \((0,0)\) has only one transition with both outer digits nonzero: the initial edge to B, with digits \((1,k)\). Every proposed state is reachable from this edge (for example, B reaches A,D, and the table supplies paths onward to all six others). Every state reaches a pivot, so none is discarded in trimming; conversely no other state can be reached because the transition table is complete. Therefore this is the entire Young graph.

**Pivot structure and isomorphism.** The even pivots are exactly O, A, F, H. The odd pivots are exactly O, D, E, H: the required edges are respectively the loops at O and H, the edge D to its reversed state G, and the edge E to its reversed state B. The directed state-adjacency list and both pivot subsets are independent of \(n\). At \(n=3\), one has \((g,k)=(8,5)\), so the names identify an explicit initial- and pivot-preserving directed-graph isomorphism to \(Y(8,5)\) for every \(n\ge3\).

**Enumeration consequence.** For a \(d\)-digit reverse multiple, a path from the initial node to an even pivot has \(d/2\) edges when \(d\) is even, while a path to an odd pivot has \((d-1)/2\) edges when \(d\) is odd. The established \(Y(8,5)\) path count therefore applies verbatim and gives the displayed generating function. Equivalently, the same table yields \(2^{t-2}\) even-pivot and odd-pivot paths at each respective allowed length \(t\ge2\).

## Verification
The bundled `verify.py` uses only standard-library exact integers. It independently enumerates every admissible outer digit \(u\) at each named carry state for all integers \(3\le n\le60\), checks the complete two-edge adjacency lists (including digit labels), reachability, pivot classes, and both parity-specific path counts up to lengths \(24\) and \(25\). It returned `VERIFY_OK`. These finitely many cases corroborate the symbolic argument; only the symbolic carry inequalities establish the theorem for all \(n\).

## Relationship to prior work
Kendrick's 2014 preprint (revised 2015) explicitly states the isomorphism as Conjecture 3 in Section 6.1 but proves different characterizations for 1089 graphs, complete Young graphs, and certain cyclic families. The present family is not in the 1089 class: \(k+1=n(n-1)\) does not divide \(g=(n-1)(n+1)\). The graph is not complete, because it has asymmetric carry-state vertices. Holt's work on symmetric and shifted-symmetric palintiples does not itself give this eight-state transition theorem. His separate paper on derived palintiple families discusses further Young-graph isomorphism classes and examples, including the reference class, but poses their general structural classification as questions rather than proving this quadratic-parameter family. Sloane's 2013 paper already enumerates reverse multiples for \(Y(8,5)\); the rational generating function above is a prior result carried over through the new isomorphism, not separately claimed to be new.

## Limitations
The result establishes the specified one-parameter isomorphism class, not a characterization of every pair \((g,k)\) whose graph is isomorphic to \(Y(8,5)\), not Kendrick's other proposed families, and not digit-label-preserving equivalence. Literature searches cannot establish global uniqueness; equivalent formulations in unlocated research remain possible. Independent validation has not been performed.

## References
1. L. H. Kendrick, *Young Graphs: 1089 et Al.*, arXiv:1410.0106, first posted 2014-10-01; Section 6.1, Conjecture 3; equations and Young graph definitions in Section 2. https://arxiv.org/abs/1410.0106
2. N. J. A. Sloane, *2178 And All That*, arXiv:1307.0453, first posted 2013-07-01; Young graph construction and enumeration for \(Y(8,5)\). https://arxiv.org/abs/1307.0453
3. B. Holt, *Some Thoughts on Determining Symmetric Palintiples*, arXiv:1410.2356, 2014; classification context for symmetric and shifted-symmetric carry structures. https://arxiv.org/abs/1410.2356
4. B. Holt, *Derived Palintiple Families and Their Palinomials*, arXiv:1412.0231, first posted 2014-11-30; Section 7.1 on Young-graph isomorphism questions. https://arxiv.org/abs/1412.0231
