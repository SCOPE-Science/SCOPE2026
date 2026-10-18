# Opposite-parity walk certificates for rooted products of unequal odd cycles

## Finding
Let \(5\le m<n\) be odd integers. Form the finite simple undirected graph
\[
G=C_m\square C_n
\]
with vertex set \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\) and the usual Cartesian adjacency. Give the origin \(o=(0,0)\) a unique initial vertex colour and every other vertex one common initial colour. Perform synchronous one-dimensional counting colour refinement, retaining the previous colour at each round.

**Theorem.** Stable refinement colours coincide exactly with the orbits of the automorphism group fixing \(o\). For a vertex \(v=(x,y)\), put
\[
a=\min\{x,m-x\},\qquad b=\min\{y,n-y\},
\]
using representatives \(0\le x<m\), \(0\le y<n\). Its stable class is indexed by the **ordered** pair \((a,b)\), with \(0\le a\le(m-1)/2\) and \(0\le b\le(n-1)/2\). Consequently the number of classes is
\[
\frac{(m+1)(n+1)}4,
\]
and the class \((a,b)\) has \((1+\mathbf 1_{a>0})(1+\mathbf 1_{b>0})\) vertices. The rooted automorphism group has order four.

More precisely, the stable colour of \(v\) determines the three integers
\[
 d=a+b,\qquad g=\binom{a+b}{a},\qquad
 L=\min\{m-a+b,\ n+a-b\}.
\]
Here \(d\) is distance from \(o\), \(g\) is the number of shortest walks from \(o\) to \(v\), and \(L\) is the length of a shortest walk from \(o\) to \(v\) whose parity is **opposite** to that of \(d\). These three integers distinguish all ordered distance profiles \((a,b)\). Moreover the orbit partition is reached no later than refinement round
\[
\frac{m+n}{2}=rac{m-1}{2}+\frac{n-1}{2}+1.
\]
This is an upper bound, not a claim of the exact stabilization round.

## Assumptions and scope
The cycles are simple and have different odd lengths at least five. An automorphism of the rooted coloured graph is an automorphism fixing \(o\). Colour refinement starts from exactly two colours and uses the signature consisting of each vertex's previous colour and the counted multiset of neighbours' previous colours. A round is one simultaneous update. All quantifiers in the theorem range over **every** pair of odd integers \(5\le m<n\) and over **every** vertex of the corresponding graph. No statement is made here about products with an even factor, equal factors, general initial colourings, or distinguishing this graph from arbitrary nonisomorphic competitors.

## Proof
**1. Rooted automorphisms.** As \(m,n\ge5\), every four-cycle in the Cartesian graph is an elementary coordinate square. At any vertex, two incident edges lie on a common four-cycle if and only if their coordinate directions differ. Consequently the graph intrinsically partitions the four incident edges into two opposite pairs. A graph automorphism preserves these pairs, possibly interchanging the two directions, and the pairing propagates to all vertices via the elementary squares. If an automorphism fixes \(o\), then specifying its images of the four neighbours fixes every coordinate-axis walk by straight continuation and then the entire graph by square propagation. Thus the rooted automorphism is determined by signed permutations of the two coordinate directions. Interchanging directions would send an \(m\)-cycle straight coordinate axis onto an \(n\)-cycle straight coordinate axis; since \(m\ne n\), that is impossible. There are at most four rooted automorphisms. Independent reflections \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(x,-y)\) provide all four. Their orbits are exactly the sets having fixed ordered cyclic-distance profile \((a,b)\). A nonzero distance coordinate has two possible signs because its cycle length is odd; a zero coordinate has one.

**2. Every rooted walk count is a refinement invariant.** Write \(A\) for the adjacency matrix and \(W_k(v)=(A^k)_{o,v}\), the number of length-\(k\) walks from the uniquely coloured origin to \(v\). The initial colour determines \(W_0\). Inductively,
\[
W_{k+1}(v)=\sum_{u\sim v}W_k(u).
\]
If the colour after round \(k\) determines \(W_k\), then the counted neighbour-colour multiset in round \(k+1\) determines \(W_{k+1}\). Since later colours retain earlier colours, round \(t\) determines all \(W_j\) with \(0\le j\le t\). In particular, the stable colour determines the full walk sequence. The first positive entry of this sequence gives the graph distance \(d\); its entry at \(d\) gives \(g\); and the first positive entry of parity opposite to \(d\) gives \(L\). Both odd cycles ensure such an opposite-parity walk exists.

**3. Walk formulae.** Choose the unique signed shortest-coordinate representatives of \(x\) and \(y\), whose absolute values are \(a\) and \(b\). A shortest path takes exactly \(a\) moves in the first cycle and \(b\) moves in the second. Each coordinate has a unique shortest direction because the corresponding cycle length is odd. The coordinate moves may be interleaved in \(\binom{a+b}{a}\) ways. Hence
\[
 d=a+b,\qquad g=\binom{a+b}{a}.
\]
To find the first walk of opposite parity, lift a graph walk uniquely to the integer square lattice \(\mathbb Z^2\), beginning at \((0,0)\). Lifts of the target vertex have coordinates congruent to the chosen signed representatives modulo \(m\) and \(n\). A lattice walk to \((s,t)\) has length at least \(|s|+|t|\), and its length has the parity of \(|s|+|t|\). Because both moduli are odd, changing one coordinate's winding number by one flips parity. The least possible displacement with opposite parity is obtained by taking the opposite arc in exactly one cycle, giving respective lengths \((m-a)+b\) and \(a+(n-b)\). Every other parity-flipping lift is at least as far away: in each coordinate the nearest alternative representative has absolute value \(m-a\), respectively \(n-b\), and extra windings cannot reduce displacement. A monotone lifted lattice walk attains either bound. Therefore
\[
 L=\min\{m-a+b,\ n+a-b\},\qquad L-d=\min\{m-2a,\ n-2b\}.
\]
The excess \(L-d\) is a positive odd integer.

**4. Injectivity of the walk certificate.** Suppose two ordered profiles \((a,b)\) and \((a',b')\) have the same \(d\) and \(g\). For a fixed nonnegative integer \(d\), the binomial sequence \(\binom dj\) is strictly increasing from \(j=0\) to \(j=\lfloor d/2\rfloor\) apart from the evident central symmetry. Consequently the two profiles either coincide or are coordinate swaps: \((a',b')=(b,a)\). In the latter case assume without loss of generality \(a<b\); this swap is only an allowed profile if \(b\le(m-1)/2\). Since \(n>m\),
\[
 L(b,a)=\min\{m-b+a,\ n+b-a\}=m-b+a.
\]
Both terms in \(L(a,b)=\min\{m-a+b,n+a-b\}\) strictly exceed \(m-b+a\): the first by \(2(b-a)\), the second by \(n-m\). Thus \(L(a,b)>L(b,a)\). The reversed inequality holds if \(a>b\). So the triple \((d,g,L)\) uniquely determines the ordered profile.

**5. Completion and round bound.** By step 2, stable colours cannot merge different triples and hence cannot merge different profiles. By step 1, automorphism-invariance prevents refinement from splitting any one profile. The stable partition is exactly the four-element rooted automorphism group's orbit partition, yielding the claimed class numbers and sizes.

Finally, the first opposite-parity walk length satisfies
\[
L=\min\{m-a+b,n+a-b\}\le\frac{(m-a+b)+(n+a-b)}2=\frac{m+n}2.
\]
Thus the colours at round \((m+n)/2\) already determine \(d\), \(g\), and \(L\) for every vertex; step 4 then shows that no further colour split is possible. This proves the quantitative upper bound and all assertions. \(\square\)

## Verification
The standalone Python programs `verify_direct.py`, `verify_walks.py`, `verify_profiles.py`, and `verify_automorphisms.py` supply complementary finite corroborations. Literal vertex-level refinement was tested on 105 unequal odd cycle pairs, covering 33,855 vertices; a separate pair of graph searches used breadth-first geodesic counts and a parity-double-cover BFS to verify the formulas on all 33,855 vertices. An arithmetic checker verified injectivity for all 4,950 pairs with odd \(5\le m<n\le203\), covering 13,601,775 coordinate-distance profiles. Exact rooted automorphisms were enumerated on three small instances. The recorded commands and outputs are in `VERIFICATION.md` and the companion text files. The infinite theorem is established by the preceding proof, not by extrapolating these finite tests.

## Relationship to prior work
Arvind, Köbler, Rattan, and Verbitsky (2015, arXiv:1502.01255) develop refinability and its relation to automorphism orbits, compactness and colour refinement. Kiefer, Schweitzer, and Selman (2015, arXiv:1503.08792) study the distinct, stronger property of identification by two-variable counting logic. Their inspected relevant sections do not state this particular rooted product classification. An equal-factor square-torus orbit classification does not settle unequal factors: equal factors permit coordinate swapping as a rooted automorphism, whereas here the two lengths forbid it. The shortest-path count \(\binom{a+b}{a}\) nevertheless remains symmetric under swapping; the genuinely new certificate is the first opposite-parity walk length \(L\), which detects which distance belongs to the shorter cycle. For example, at \((m,n)=(5,9)\), profiles \((1,2)\) and \((2,1)\) have the same distance three and three geodesics, but opposite-parity walk lengths six and four respectively.

## Limitations
The graph family is restricted to **distinct odd cycle lengths at least five**, with one initially individualized origin. Even-cycle antipodes and equal-factor automorphisms require different arguments. The upper bound on refinement rounds is not asserted to be exact. Orbit recovery inside this rooted graph is weaker than identification from all graph competitors. Published-priority searches do not exclude every possible earlier specialized treatment.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*. Public version first posted 2015-02-04; arXiv:1502.01255, https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*. Public version first posted 2015-03-30; arXiv:1503.08792, https://arxiv.org/abs/1503.08792.
