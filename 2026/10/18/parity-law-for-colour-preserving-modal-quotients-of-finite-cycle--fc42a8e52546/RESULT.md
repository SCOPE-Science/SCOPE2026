# Parity law for colour-preserving modal quotients of finite cycles

## Finding
Let \(m\geq3\) and let \(w=(w_0,\ldots,w_{m-1})\) be a cyclic word over any finite nonempty alphabet. Regard its positions as the vertices of the irreflexive, undirected cycle \(C_m\), with the given named unary colours. Let \(p\mid m\) be the least cyclic period of \(w\). A quotient means an onto colour-preserving bounded morphism of these Kripke models, with the target a finite connected irreflexive undirected simple graph.

Every quotient target is a path or a cycle. For each divisor \(d\mid m\) with \(d\geq3\) and \(p\mid d\), there is exactly one isomorphism type of coloured cycle quotient on \(d\) vertices, and there are no other cycle quotients.

Put \(R(w)=1\) precisely when \(w_i=w_{2s-i\pmod m}\) for every \(i\), for at least one integer \(s\) (reflection through vertices). If \(m\) is odd or \(R(w)=0\), there is no path quotient. Otherwise, path quotient orders are **exactly**
\[
\ell=1+L/2,\qquad L\mid m,\quad 2\mid L,\quad p\mid L.
\]
At each admissible \(L\), the number of nonisomorphic colour-preserving path targets is
\[
q_L=\begin{cases}2,& 2\mid p\text{ and }2\mid(L/p),\\ 1,&\text{otherwise}.\end{cases}
\]
Thus a symmetric coloured cycle has a smallest path quotient of order \(1+\operatorname{lcm}(p,2)/2\). Writing \(\tau(r)\) for the number of positive divisors of \(r\), the total number of path-quotient isomorphism classes is \(\tau(m/(2p))\) if \(p\) is odd and \(m\) is even, and it is \(\tau(m/p)+\mathbf1_{2\mid(m/p)}\tau(m/(2p))\) if \(p\) is even and \(R(w)=1\). In the latter expression the second summand is defined to be zero when \(m/p\) is odd. The count is zero when \(m\) is odd or \(R(w)=0\).

## Assumptions and scope
All graphs are finite, simple, undirected and **irreflexive**. The source is the simple cycle on \(m\ge3\) vertices, not a reflexive cycle or a directed cycle. Each vertex has exactly one of finitely many named colours; colours must be preserved pointwise. A bounded morphism \(f:X\to Y\) satisfies (forth) \(i\sim j\Rightarrow f(i)\sim f(j)\) and (back) for every \(i\in X\) and \(y\sim f(i)\), some \(j\sim i\) has \(f(j)=y\). Equivalently, \(f(N_X(i))=N_Y(f(i))\). The target is connected; onto follows from nonempty image and the back condition, but is included explicitly to fix terminology. Targets are considered up to colour-preserving graph isomorphism. No claim is made for arbitrary graphs in the source or for relations with loops.

## Proof
**1. Shape and normal forms.** The image of the two neighbours of each source vertex must equal the neighbours of its image. Therefore every target vertex has degree at most two. Connectivity and the absence of loops make the target a path \(P_\ell\), \(\ell\ge2\), or a simple cycle \(C_d\), \(d\ge3\); a singleton target is impossible because source edges must map to edges.

If the target is \(C_d\), its two neighbours must receive the two source neighbours separately. Once images of source vertices \(0\) and \(1\) are fixed, there can be no reversal of traversal direction: the only possibilities are \(f(i)=a+i\pmod d\) and \(f(i)=a-i\pmod d\). Closing the source requires \(d\mid m\), and every such map is locally onto. In the uncoloured case there are exactly \(2d\) maps. Colour preservation makes the target colour at each residue the corresponding source colour, which is well defined exactly when \(d\) is a period of \(w\), equivalently \(p\mid d\). Different choices of offset/direction yield rotations or reversals of the same target word and hence a single target isomorphism type.

If the target is the path \(P_\ell\), write \(h=\ell-1\) and \(L=2h\). At an interior target vertex of degree two, a locally onto walk must take the two distinct possible directions; at an endpoint it must reflect. Consequently every bounded morphism is a phase translate of the deterministic reflected walk
\[
f(i)=\rho_L(i+t),\qquad \rho_L(j)=\min(j\bmod L,\ L-(j\bmod L)).
\]
The reflected walk has least period \(L\) for \(h\ge1\), so closing the source requires \(L\mid m\). Conversely all \(L\) phase translates give bounded morphisms when \(L\mid m\), including \(\ell=2\). The fibres identify source positions reflected about an integer axis and repeated modulo \(L\). Preservation of colour is thus equivalent to the conjunction of \(p\mid L\) and existence of a vertex-axis reflection \(w_i=w_{2s-i}\). In particular \(2\mid m\). Every such \(L\) and reflecting centre \(s\) gives a target colouring \((w_s,w_{s+1},\ldots,w_{s+L/2})\).

**2. Counting nonisomorphic path targets.** Fix an admissible \(L\). Two vertex-centred reflections of a primitive word of period \(p\), about indices \(s\) and \(t\), compose to a rotation by \(2(s-t)\). Primitivity therefore forces \(p\mid2(s-t)\). If \(p\) is odd, all reflecting centres agree modulo \(p\), hence give the same target word. If \(p\) is even, there are exactly two centre classes modulo \(p\), represented by \(s\) and \(s+p/2\), and thus at most two path target words.

Isomorphism of a coloured path either preserves or reverses its linear order. For \(p\) even, reversing the target word based at \(s\) produces the target word based at \(s+L/2\). If \(L/p\) is odd, this swaps the two centre classes, so there is one target type. If \(L/p\) is even, the reversal fixes each centre class. The two target words cannot agree: equality across \(L/2+1\ge p+1\) positions would force \(p/2\) to be a period of \(w\), contradicting minimality of \(p\). Thus there are two types. The odd-period case has one type. Summing the stated per-length counts over even divisors \(L\mid m\) that are multiples of \(p\) gives the divisor formulas.

**3. Least quotient.** The smallest positive even multiple of \(p\) is \(\operatorname{lcm}(p,2)\), and it divides \(m\) whenever \(m\) is even and \(p\mid m\). Reflection symmetry makes it admissible. Substituting this \(L\) gives the asserted smallest path quotient.

## Verification
Two independently organized checks are supplied. `check_candidate.py` computes predicted and explicitly realized coloured quotient target isomorphism classes by enumerating phases and induced target words, without using the parity multiplicity formula in its realization routine. It exhaustively checks all \(32{,}760\) binary cyclic words of lengths \(3\) through \(14\), and all \(29{,}511\) ternary words of lengths \(3\) through \(9\). `verify_graph_maps.py` independently enumerates all locally-surjective adjacency walks from uncoloured cycles \(C_m\) for \(3\le m\le18\) into every admissible-sized path/cycle target; it checks \(288\) domain/target configurations and their exact map counts. Run both with Python 3, without third-party dependencies. Finite checks corroborate, but do not replace, the all-size argument.

## Relationship to prior work
Locally-surjective graph homomorphisms, also known as role assignments, are studied systematically by Chaplick, Fiala, van 't Hof, Paulusma and Tesař (arXiv:1408.6676, first posted 28 August 2014). Their general decision/complexity treatment supplies the operative local-surjectivity notion, but the present coloured-cycle quotient-spectrum formulas and the parity-dependent one-versus-two isomorphism-type law are not stated in the inspected paper. A general graph-homomorphism or dynamic-programming algorithm does not by itself specify these closed orbit counts. The proof here is direct, self-contained, and specific to bidirected simple cycles and colour-preserving modal bounded morphisms.

## Limitations
Specialized modal-logic or labelled-graph quotient literature could contain an equivalent argument; checking one general algorithm paper cannot exclude all prior coverage. The target graph must be connected and irreflexive and colours must be preserved; loops, directed edges, relaxed colour conditions, and source graphs of maximum degree above two are not addressed. No assertion of minimal first-order or modal description length is made.

## References
1. S. Chaplick, J. Fiala, P. van 't Hof, D. Paulusma and M. Tesař, *Locally Constrained Homomorphisms on Graphs of Bounded Treewidth and Bounded Degree*, arXiv:1408.6676, 28 August 2014, https://arxiv.org/abs/1408.6676.
