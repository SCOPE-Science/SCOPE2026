# A four-state transfer formula for indegree-parity acyclic orientations of wheel graphs

## Finding

Let \(m\ge3\) be an integer and let \(W_m=K_1\vee C_m\) denote the labelled wheel with hub \(h\) and cyclically indexed rim vertices \(v_0,\ldots,v_{m-1}\). For a prescribed binary vector \(\mathbf p=(p_0,\ldots,p_{m-1})\), define \(A_m(\mathbf p)\) to be the number of **acyclic orientations** in which the indegree of each \(v_i\) is congruent to \(p_i\) modulo two. Subscripts on rim indices are taken modulo \(m\).

The hub parity is necessarily \(p_h\equiv\sum_i p_i\pmod2\). Every such full parity signature is feasible by an orientation, and it has exactly \(2^m\) realizing orientations before acyclicity is imposed.

For \(i\in\{0,\ldots,m-1\}\) define a \(4\)-by-\(4\) binary matrix \(T_i(\mathbf p)\), with rows and columns indexed by ordered pairs from \(\{0,1\}^2\). Entries vanish unless the row is \((a,b)\) and the column is \((b,c)\). For such an entry, set

\[
L= (1+p_i+a+b)\bmod2,\qquad R=(1+p_{i+1}+b+c)\bmod2.
\]

Define the entry to be zero precisely when either \(b=1,L=1,R=0\) or \(b=0,L=0,R=1\); otherwise it is one. Then the exact number is

\[
\boxed{A_m(\mathbf p)=\operatorname{tr}\left(T_0(\mathbf p)T_1(\mathbf p)\cdots T_{m-1}(\mathbf p)\right)-2\mathbf 1_{\{p_0=\cdots=p_{m-1}\}}.}
\]

The formula uses \(O(m)\) arithmetic operations for each prescribed parity signature, with no dependence on an exponential enumeration of orientations. Furthermore,

\[
\boxed{A_m(\mathbf p)>0\quad\Longleftrightarrow\quad m\text{ is even, or }\mathbf p\text{ is nonconstant}.}
\]

For even \(m\), the two constant signatures have exactly two acyclic realizations each. For odd \(m\), the two constant signatures are the only feasible signatures with no acyclic realization. For example, the full distribution for \(m=4\), in which \(z\) records \(A_m(\mathbf p)\), is \(2z^2+8z^4+4z^6+2z^9\).

## Assumptions and scope

The graphs are finite, simple, undirected before orientation, and labelled as above. An orientation assigns one direction to every edge. An acyclic orientation has no directed cycle. Parity always refers to **indegree**, not outdegree or the number of edges disagreeing with another orientation. The result holds for every integer \(m\ge3\), including \(W_3=K_4\). There is one hub and precisely \(m\) rim edges and \(m\) spokes. A prescribed full vertex-parity vector is feasible exactly when its hub coordinate equals the sum of its rim coordinates modulo two.

## Proof

**1. Parametrization of parity fibres.** Put \(e_i=1\) if the rim edge is directed \(v_i\to v_{i+1}\), and \(e_i=0\) otherwise. Put \(s_i=1\) if the spoke is \(h\to v_i\), and \(s_i=0\) otherwise. The indegree of \(v_i\), reduced modulo two, is

\[
p_i\equiv s_i+e_{i-1}+(1-e_i)\equiv1+s_i+e_{i-1}+e_i\pmod2.
\]

Consequently every choice of the \(m\) rim bits uniquely determines all spokes through \(s_i=(1+p_i+e_{i-1}+e_i)\bmod2\). This gives exactly \(2^m\) orientations in each rim-parity class. Because the total sum of indegrees is \(2m\), the hub parity is necessarily \(\sum_i p_i\bmod2\), and this necessary condition is sufficient by the parametrization.

**2. Local characterization of acyclicity.** Every directed triangle contains the hub and one rim edge. If \(e_i=1\), the triangle through \(v_i,v_{i+1},h\) is directed if and only if \(s_i=1,s_{i+1}=0\). If \(e_i=0\), it is directed if and only if \(s_i=0,s_{i+1}=1\). We claim that an orientation is acyclic if and only if it has no directed triangle and its rim is not itself a directed cycle.

Indeed, a directed cycle avoiding the hub must be the entire consistently oriented rim. Every simple directed cycle containing the hub consists of a spoke \(h\to v_i\), a directed path along consecutive rim edges from \(v_i\) to some \(v_j\), and a spoke \(v_j\to h\). On this path the spoke bits start at one and end at zero. At some consecutive pair they change from one to zero, and the intervening directed rim edge gives a directed triangle. Therefore no other directed cycles are possible without a directed triangle.

**3. Transfer count.** Write the local state at rim position \(i\) as \((e_{i-1},e_i)=(a,b)\). The next state is \((e_i,e_{i+1})=(b,c)\). The spoke values at the two endpoints of edge \(i\) are exactly the bits \(L\) and \(R\) in the matrix definition. The two forbidden configurations are exactly the directed triangles from step 2. A closed walk through the ordered product of all \(T_i\), counted by its trace, corresponds bijectively to a cyclic rim-bit assignment with no directed triangle. When all rim bits are equal, the triangle-free condition forces all spoke bits to be equal, because otherwise a change in the forbidden direction would occur around the consistently directed rim. Conversely, constant spoke bits make either directed-rim assignment triangle-free. For constant rim bits the spoke identity says \(s_i=1+p_i\), so such assignments occur exactly when \(\mathbf p\) is constant, and there are then exactly two. Removing them gives the boxed transfer formula.

**4. Exact existence criterion.** The binary system \(e_{i-1}+e_i=q_i\pmod2\) on the cyclic rim has a solution if and only if \(\sum_i q_i\equiv0\pmod2\); when solvable, it has exactly two solutions, complements of one another. A nonzero \(\mathbf q\) guarantees that these solutions are not constant rim assignments.

If \(m\) is odd, choose all spokes outgoing from the hub when \(\sum_i p_i\) is even, and all spokes incoming when it is odd. In the former case set \(q_i=p_i\); in the latter set \(q_i=1+p_i\). The cyclic system has a solution because the sum of the \(q_i\) is even. If \(\mathbf p\) is nonconstant, then \(\mathbf q\) is nonzero, the rim is not directed, and constant spoke directions exclude all directed hub triangles. Thus the orientation is acyclic. If \(\mathbf p\) is constant, there can be no acyclic orientation: every vertex of \(W_m\) has odd degree, and when all indegree parities are even there can be no sink, while when all are odd there can be no source.

If \(m\) is even and \(\sum_i p_i\) is even with \(\mathbf p\ne\mathbf0\), choose every spoke outgoing and solve with \(\mathbf q=\mathbf p\). The solution has a nondirected rim and no directed triangles. For \(\mathbf p=\mathbf0\), choose every spoke incoming, so \(\mathbf q=\mathbf1\); because \(m\) is even, the rim directions can alternate, producing an acyclic orientation.

Finally suppose \(m\) is even and \(\sum_i p_i\) is odd. Then some \(p_j=0\), since the all-one vector has even sum. Direct only the spoke at \(v_j\) into the hub and direct all other spokes outward. The associated \(q_i=1+p_i+s_i\pmod2\) has even sum and satisfies \(q_j=1\). Choose its unique cyclic solution with \(e_{j-1}=0\) and \(e_j=1\). Both rim edges incident to \(v_j\) now point away from it. No directed triangle can use the hub, since every spoke except the one at \(v_j\) is outgoing and neither rim neighbour points toward \(v_j\). The rim cannot be consistently directed because it has a source at \(v_j\). This completes the existence proof.

For completeness, when \(m\) is even and \(\mathbf p=\mathbf0\), any acyclic orientation must have the hub as its sink: all rim vertices have odd degree and even prescribed indegree, so none can be a sink. Hence all spokes are incoming and the rim bits must alternate; there are precisely two choices. The analogous source argument when \(\mathbf p=\mathbf1\) forces all spokes outward and again two alternating rim assignments. This proves the asserted exact boundary counts.

## Verification

A standalone program, `verify_wheel.py`, generates all orientations for \(3\le m\le8\) using actual directed edge lists. It computes indegree parities and tests acyclicity independently by a topological-sort algorithm; it separately evaluates the four-state trace formula. Every comparison agrees. This checks 87,360 orientations across six wheels and all 504 feasible parity classes. It also verifies that every class has \(2^m\) unrestricted orientations and that the number of empty acyclic fibres is two for odd \(m\) and zero for even \(m\).

The total acyclic counts are \(24,78,240,726,2184,6558\) for \(m=3,4,5,6,7,8\) respectively. They agree with the established total \(3^m-3\): indeed, \(\chi_{W_m}(q)=q[(q-2)^m+(-1)^m(q-2)]\), and the standard chromatic evaluation at \(-1\) counts acyclic orientations. This is a consistency check and is **not** used to infer the parity-refined formula. The code and finite checks do not replace the proof for arbitrary \(m\).

## Relationship to prior work

Gravier, Petiteau and Sivignon [1] study acyclic orientations with prescribed indegree parities and establish source/sink necessary conditions and results on Cartesian products of paths and cycles. Those necessary conditions explain the odd-rim obstruction in one direction, but the inspected theorem statements, relevant proofs and text do not establish the wheel parity-fibre counts or the four-state trace formula. The present result addresses a wheel, which is a cone over a cycle, not a Cartesian product of a cycle with a path.

Mühlherr and Poullot [2] study the graph of acyclic orientations, wheel Hamiltonicity, and a polynomial recording edge-orientation disagreement with a reference orientation. That univariate edge-disagreement statistic is different from a labelled vertex indegree-parity vector; the cited wheel results do not specify the cardinality of each such fibre. Stanley's classical evaluation [3] gives the total number of acyclic orientations, but cannot by itself recover their distribution among \(2^m\) parity classes.

## Limitations

The transfer formula applies to the labelled wheel family only, not arbitrary planar graphs or arbitrary graphs of small treewidth. Its \(O(m)\) bound counts arithmetic operations on integers with up to \(O(m)\) bits; it is not a constant-bit-operation complexity assertion. No independence, peer review or definitive bibliographic priority is claimed. The existence criterion alone may follow from general results in special cases; the refined exact counts are the central statement. Different graph families and potentially unindexed equivalences require separate comparison.

## References

[1] S. Gravier, M. Petiteau, I. Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475, first submitted 10 March 2026, https://arxiv.org/abs/2603.09475 .

[2] L. Mühlherr, G. Poullot, *Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*, arXiv:2609.02249, first submitted 2 September 2026, https://arxiv.org/abs/2609.02249 .

[3] R. P. Stanley, *Acyclic orientations of graphs*, Discrete Mathematics 5 (1973), 171–178; https://math.mit.edu/~rstan/pubs/pubfiles/18.pdf .
