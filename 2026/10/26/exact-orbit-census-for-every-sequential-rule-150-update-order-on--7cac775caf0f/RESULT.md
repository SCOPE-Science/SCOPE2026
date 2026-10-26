# Exact orbit census for every sequential Rule-150 update order on a ring

## Finding
For every integer \(n\ge3\) and every permutation \(\pi\) of the vertices of the cycle \(C_n\), consider a complete sequential sweep \(F_\pi\) that visits each vertex once and replaces its bit with the sum modulo two of that bit and its two cyclic neighbors (asynchronously evaluated at the instant of update). Let \(p_\pi\) be the permutation of the \(n\) cyclic domain-wall coordinates induced by one sweep. It always has **exactly two cycles**, of lengths \(a,b\ge1\) with \(a+b=n\).

For each positive integer \(t\), set \(r=\gcd(a,t)\), \(s=\gcd(b,t)\), and let \(q_t\) be the rank over \(\mathbb F_2\) of the displayed two-by-two matrix:
\[
Q_t=\begin{pmatrix}
 a/r\pmod 2 & b/s\pmod 2\\
 t/r\pmod 2 & t/s\pmod 2
\end{pmatrix},\qquad q_t=\operatorname{rank}_{\mathbb F_2}(Q_t).
\]
Then the number of states fixed after \(t\) complete sweeps is exactly
\[
\boxed{\#\operatorname{Fix}(F_\pi^t)=2^{1+r+s-q_t}.}
\]
Consequently the number of primitive cycles of length \(t\) is
\[
\boxed{\frac1t\sum_{d\mid t}\mu(t/d)\,2^{1+\gcd(a,d)+\gcd(b,d)-q_d}.}
\]
With \(L=\operatorname{lcm}(a,b)\) and \(g=\gcd(a,b)\), the **exact** global permutation order is
\[
\boxed{\operatorname{ord}(F_\pi)=\begin{cases}L,&n/g\text{ even},\\2L,&n/g\text{ odd}.\end{cases}}
\]
Thus the two domain-wall cycle lengths determine the complete phase-space cycle census for **every** update order, not only for the natural cyclic sweep.

For example, on a six-site ring, orders \((0,1,2,3,4,5)\), \((0,1,2,3,5,4)\), and \((0,1,2,5,4,3)\) yield respective domain-wall types \((1,5)\), \((2,4)\), and \((3,3)\), and global map orders \(5\), \(8\), and \(3\).

## Assumptions and scope
All arithmetic on states and wall differences is over \(\mathbb F_2\). Vertex indices and wall indices run through \(\mathbb Z/n\mathbb Z\), and the wall between vertices \(j\) and \(j+1\) has index \(j\). Each site is updated exactly once per sweep; orders are permutations, not arbitrary words with repeated sites. The starting state is any element of \(\mathbb F_2^n\); \(t\) is any positive integer. The map is a bijection because a local Rule-150 update is an involution when neighbors are fixed.

The lengths \(a,b\) are computable: begin with the identity permutation on the \(n\) wall coordinates, and for each site \(j\) in chronological order transpose wall positions \(j-1\) and \(j\). Count the cycles of the resulting permutation. Their ordering is immaterial in all formulas.

## Proof
**Wall transpositions and the two-cycle property.** Define \(d_j=x_j+x_{j+1}\), so \(\sum_jd_j=0\). A local update at \(j\) changes \(x_j\) by \(x_{j-1}+x_{j+1}=d_{j-1}+d_j\). Consequently it interchanges \(d_{j-1}\) and \(d_j\), fixing all other walls. Let \(S\) be the transposition of wall positions \(e=n-1\) and \(f=0\), associated with updating vertex zero. Write the chronological wall map as \(P=A S B\), where \(B\) comprises the swaps preceding site zero, and \(A\) the swaps after it. In coordinates \(z=Bd\), one sweep is conjugate to \(p=B A S=H S\). Here \(H=BA\) uses the other \(n-1\) adjacent swaps, each once, on the path obtained by removing the edge \((e,f)\) from the wall cycle.

The product of the edge transpositions of any tree, in any order, is one cycle on its vertices. For completeness, induct on the number of edges: commuting an edge transposition to the end is unnecessary; instead delete the last transposition in chronological product. Its removal divides a tree into two components; the product of all remaining transpositions is a disjoint cycle on each component by induction, and the final transposition joins these two cycles into one. Thus \(H\) is a single \(n\)-cycle. Multiplication by \(S=(e\ f)\) splits it into exactly two cycles with \(e\) and \(f\) in different cycles, proving the claimed wall cycle structure.

**Lift to state coordinates.** The even-parity wall vectors \(z\in E=\{z:\sum_jz_j=0\}\) and the bit \(c=x_0\) parametrize the state space bijectively. The intermediate site-zero update changes \(c\) by \(z_e+z_f\), and all other updates leave \(c\) unchanged. Hence the entire sweep is conjugate to
\[
(z,c)\longmapsto(pz,\ c+z_e+z_f),\quad z\in E,
\]
with \(e,f\) in distinct cycles of \(p\) of lengths \(a,b\).

**Fixed points of every power.** A wall vector with \(p^t z=z\) has one independent period-\(r\) block on the first cycle and one independent period-\(s\) block on the second. Let \(U,V\in\mathbb F_2\) be the sums of these two blocks. Even wall parity is precisely \((a/r)U+(b/s)V=0\). During \(t\) sweeps, the bit \(c\) flips by the sum of the \(t\) observed entries at \(e\) and \(f\), namely \((t/r)U+(t/s)V\). Both coefficients are reduced modulo two. These are exactly the two linear equations represented by \(Q_t\). Their joint rank is \(q_t\); hence \(2^{r+s-q_t}\) wall vectors qualify. Every such wall vector permits both values of \(c\), giving \(2^{1+r+s-q_t}\) fixed states. Since every sweep is invertible, standard Möbius inversion gives the primitive-cycle formula.

**Exact global order.** The induced permutation of walls has order \(L\). Its action on \(E\) is faithful for \(n\ge3\): the vectors having ones in any two distinct positions span \(E\), and a permutation fixing all such vectors must fix every position. Therefore the state-map order is divisible by \(L\). At time \(L\), all walls return. The lift flips \(c\) by \((L/a)U+(L/b)V\), where \(U,V\) are the total parities of the two entire wall cycles. The even-wall condition says \(U=V\), so the flip is \(((a+b)/g)U=(n/g)U\) modulo two. Both values of \(U\) occur (take zero walls, or one occupied wall in each cycle). If \(n/g\) is even the \(L\)-th sweep is the identity; if it is odd the \(L\)-th sweep is a nontrivial order-two fiber translation. In the latter case exactly \(2L\) sweeps return every state. This proves minimality and the order formula.

## Verification
The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` to reproduce exact integer comparisons of full nonlinear-looking bit updates against the predicted fixed-point counts, global map orders, and primitive-period census. The verifier exhaustively checks **all** \(n!\) update orders for each \(3\le n\le6\) and deterministic samples of \(101\) orders for each \(7\le n\le9\), with all \(2^n\) binary initial states for each tested order. Its recorded completion was `VERIFY_OK fixed_comparisons 16089 map_order_comparisons 1173 primitive_period_comparisons 904`. These finite tests check implementation and small cases; the unrestricted theorem follows from the proof above.

## Relationship to prior work
Macauley, McCammond, and Mortveit's analysis of Rule-150 dynamics groups supplies the known permutation action on gaps and the surrounding group-theoretic structure, but not the exact cycle census of each arbitrary simple update order. Macauley and Mortveit established cycle equivalence relations and bounds on the number of distinct update-order orbit types, not an explicit count for every power. Defant gave an exact Rule-150 periodic-point classification for the **identity update order**; that special case is prior work, not a novelty claim here. The present formula applies to every permutation order and distinguishes different order-induced wall-cycle splits. Work on synchronous or alternating-substep Rule-150 dynamics concerns different time-update operators.

## Limitations
The theorem requires finite rings with \(n\ge3\) and one visit per vertex per sweep. It does not address non-permutation schedules, heterogeneous vertex rules, infinite lattices, or Rule 105. It does not assert that every pair of cycle lengths occurs for a fixed ring size (although several nontrivial types are shown). Numerical verification is finite and provides no independent certification. Earlier group-theoretic observations already contain the wall permutation action; priority for the complete arbitrary-order cycle formulas requires independent literature assessment.

## References
1. M. Macauley, J. McCammond, H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360 (first submitted 2007-07-16).
2. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412 (first submitted 2008-02-29).
3. M. Macauley, J. McCammond, and H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, Journal of Algebraic Combinatorics 33 (2011), 11–35, doi:10.1007/s10801-010-0231-y.
4. C. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966 (first submitted 2015-11-22), Theorem 4.1.
5. J. W. P. Wilkinson, T. Prosen, and J. P. Garrahan, *Exact solution of the Rule 150 reversible cellular automaton*, arXiv:2110.15085 (2021).
