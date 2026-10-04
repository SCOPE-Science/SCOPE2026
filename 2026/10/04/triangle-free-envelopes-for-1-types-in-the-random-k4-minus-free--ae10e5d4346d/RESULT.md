# Triangle-free envelopes for 1-types in the random K4-minus-free 3-hypergraph

## Finding
Let \(M=F^3_{4,1}\) be the Fraïssé limit of the finite 3-uniform hypergraphs in which every four vertices span at most two hyperedges. Equivalently, \(M\) is the generic \(K_4^-\)-free 3-hypergraph, where \(K_4^-\) is the four-vertex 3-graph with three edges.

For a finite induced parameter substructure \(A\), define a conflict hypergraph \(C(A)\) with vertex set \(\binom{A}{2}\). For every triple \(\{a,b,c}\):

- if \(abc\) is a hyperedge of \(A\), put the three 2-edges \(\{ab,ac}\), \(\{ab,bc}\), and \(\{ac,bc}\) into \(C(A)\);
- if \(abc\) is a nonedge of \(A\), put the 3-edge \(\{ab,ac,bc}\) into \(C(A)\).

If \(P_A(z)\) weights a nonalgebraic complete 1-type by the number of pairs \(ab\) for which \(R(x,a,b)\) holds, then
\[
P_A(z)=I_{C(A)}(z),
\]
the independence polynomial of this mixed-rank conflict hypergraph.

Writing \(T_n(z)\) for the edge enumerator of labelled triangle-free graphs on \([n]\), one has, for every \(|A|=n\),
\[
P_A(z)\le_{\mathrm{coeff}}T_n(z),
\]
with equality exactly when \(A\) has no hyperedges. Thus the sharp maximum number of nonalgebraic 1-types over an \(n\)-element parameter set is the number \(t_n\) of labelled triangle-free graphs. In particular,
\[
\log_2 t_n=\frac{n^2}{4}+o(n^2).
\]

## Assumptions and scope
The language has one symmetric irreflexive ternary relation \(R\). The parameter set is a finite induced substructure \(A\subseteq M\). The result counts complete 1-types over \(A\); types realized by elements of \(A\) are algebraic and are not included in \(P_A\). Every type represented by a new point is nonalgebraic.

The source class \(\mathcal H^m_{l,s}\) consists of finite \(m\)-hypergraphs in which every \(l\)-set has more than \(s\) nonedges. Kikyo and Tsuboi record that this class has free amalgamation when \(s<\binom{l-2}{m-2}\), and that its Fraïssé limit is countably categorical with quantifier elimination. At \((m,l,s)=(3,4,1)\), the condition becomes exactly “every four vertices span at most two hyperedges.”

## Proof
Fix a new point \(x\). Its quantifier-free relation to \(A\) is determined by the graph \(L_x\) on vertex set \(A\) defined by
\[
ab\in E(L_x)\quad\Longleftrightarrow\quad R(x,a,b).
\]
Consider a triple \(a,b,c\) from \(A\). The four-set \(\{x,a,b,c}\) contains the old triple \(abc\), together with the three possible new triples \(xab,xac,xbc\). Since every four-set may contain at most two hyperedges, the legal-link condition is:
\[
|E(L_x[\{a,b,c}])|\le 1\quad\text{if }R(a,b,c),
\]
and
\[
|E(L_x[\{a,b,c}])|\le 2\quad\text{if }
eg R(a,b,c).
\]
The first condition is equivalent to forbidding every pair among \(ab,ac,bc\); the second is equivalent to forbidding their simultaneous selection. These are exactly the independent-set constraints defining \(C(A)\). Hence legal one-point diagrams are in weight-preserving bijection with independent sets of \(C(A)\), proving \(P_A(z)=I_{C(A)}(z)\).

Quantifier elimination implies that two such legal one-point diagrams give the same complete type exactly when they have the same link graph. The Fraïssé extension property realizes every legal diagram. Free amalgamation allows arbitrarily many copies of the same new-point diagram over \(A\), so every such outside type is nonalgebraic.

Every legal link graph is triangle-free: on each old triple its three link edges cannot all occur. If \(A\) has no hyperedges, this is the only restriction, so \(P_A(z)=T_n(z)\). For arbitrary \(A\), legal links form a subset of all triangle-free graphs, giving coefficientwise domination. If \(A\) has a hyperedge \(abc\), the graph with exactly the two edges \(ab,ac\) is triangle-free but illegal over \(A\); therefore the coefficient of \(z^2\) is strictly smaller. Equality holds only for the empty 3-graph.

The classical Erdős–Kleitman–Rothschild enumeration of triangle-free graphs gives \(t_n=2^{n^2/4+o(n^2)}\), yielding the asserted sharp exponent.

## Verification
The bundled `verify.py` independently checks the local-extension rule against the conflict-hypergraph independence polynomial for every legal labelled parameter 3-graph on at most five vertices. It also checks coefficientwise domination and the strictness criterion, and independently enumerates labelled triangle-free graphs through seven vertices, recovering
\[
1,1,2,7,41,388,5789,133501
\]
for \(n=0,\ldots,7\). Running the script prints `VERIFY_OK`.

## Relationship to prior work
Kikyo and Tsuboi provide the random-hypergraph class, the free-amalgamation criterion, and quantifier elimination; they do not state the finite-parameter 1-type polynomial or its sharp extremum. Falgas-Ravry, Pikhurko, Vaughan, and Volec explicitly note the classical combinatorial fact that a 3-graph is \(K_4^-\)-free exactly when every vertex link graph is triangle-free. That link characterization is therefore prior and is not part of the novelty claim.

The new step is parameter-sensitive: an old hyperedge strengthens the three link variables from a triangle prohibition to three pairwise conflicts. This yields the mixed-rank conflict hypergraph, the exact independence-polynomial formula for every finite parameter structure, and the unique coefficientwise triangle-free envelope. Searches for the exact model-theoretic type-count formulation and its equivalent conflict-hypergraph form found no matching result.

## Limitations
The result concerns 1-types, not higher-arity type spaces. The asymptotic statement uses the classical triangle-free graph enumeration theorem rather than deriving its error term. No complexity classification for evaluating \(I_{C(A)}(1)\) on this restricted family of conflict hypergraphs is claimed. The originality conclusion retains a modest folklore risk because the local deduction from quantifier elimination and the link condition is short.

## References
H. Kikyo and A. Tsuboi, “Dividing and forking in random hypergraphs,” *Annals of Pure and Applied Logic* 176 (2025), 103521, DOI 10.1016/j.apal.2024.103521. The version of record states “Available online 24 September 2024,” gives MSC 03C13 first, and records the free-amalgamation and quantifier-elimination facts used here.

V. Falgas-Ravry, O. Pikhurko, E. Vaughan, and J. Volec, “The codegree threshold of \(K_4^-\),” *Journal of the London Mathematical Society* 107 (2023), 1660–1691, DOI 10.1112/jlms.12722.

P. Erdős, D. J. Kleitman, and B. L. Rothschild, “Asymptotic enumeration of \(K_n\)-free graphs,” *Atti dei Convegni Lincei* 17 (1976), 19–27.
