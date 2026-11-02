# Scan-order phase diagram and exact Rule 150 cycle census on binary rings

## Finding

For every cycle of \(n\ge 3\) binary sites, and for **every permutation** of the \(n\) single-site Rule 150 updates, the entire primitive-period census depends on just one cyclic-ascent statistic of the update order. This upgrades the previously studied monotone update order to arbitrary one-pass schedules.

Index sites by \(\mathbb Z/n\mathbb Z\). For a scan permutation \(\pi\), write \(p_i\) for the position of site \(i\) in the scan, and define
\[
k=\#\{i\in\mathbb Z/n\mathbb Z:p_i<p_{i+1}\},\qquad m=n-k.\]
Necessarily \(1\le k,m\le n-1\). Define, for each positive integer \(t\),
\[
g_t=\gcd(k,t),\qquad h_t=\gcd(m,t),\qquad
\epsilon_t=\left(\frac{nt}{g_th_t}\right)\bmod 2.\]
The displayed quotient is an integer. Let \(F_\pi\) be one full scan. Then
\[
\boxed{\#\operatorname{Fix}(F_\pi^t)=2^{g_t+h_t-\epsilon_t}.}
\]
Thus the number of states of **primitive** period \(d\) and the number of distinct primitive \(d\)-cycles are, respectively,
\[
P_d=\sum_{e\mid d}\mu(d/e)\,2^{\gcd(k,e)+\gcd(m,e)-\epsilon_e},
\qquad C_d=P_d/d.
\]
The exact permutation order of \(F_\pi\) is
\[
\boxed{\operatorname{ord}(F_\pi)=
\begin{cases}
\operatorname{lcm}(k,m),&\nu_2(k)=\nu_2(m),\\
2\operatorname{lcm}(k,m),&\nu_2(k)\ne\nu_2(m).
\end{cases}}
\]
All binary states are periodic from time zero. Furthermore, exactly \(nA(n-1,k-1)\) of the \(n!\) scan permutations have statistic \(k\), where \(A(r,s)\) is the Eulerian number counting permutations of \(r\) symbols with \(s\) ascents. In particular, the number of fixed states of a single scan is four for even \(n\) and two for odd \(n\), independently of the order.

For example, on the six-site ring, the scans \((0,5,4,3,2,1)\), \((0,1,5,4,3,2)\), and \((0,1,2,5,4,3)\) have \(k=1,2,3\) and exact whole-scan orders \(5,8,3\), respectively. Scheduling changes the possible orbit lengths even though every individual local rule is unchanged.

## Assumptions and scope

The state space is \(\mathbb F_2^n\), and the graph is the simple undirected cycle \(C_n\) with \(n\ge3\), not an infinite lattice. Each site occurs **exactly once per scan**. When site \(i\) is updated, its current value becomes \(x_{i-1}+x_i+x_{i+1}\) in \(\mathbb F_2\); all other values are left unchanged. Neighborhood values are read at the instant of that update. The same scan permutation is repeated at each subsequent time step. A fixed point of a power means equality of complete \(n\)-bit configurations, not merely of edge differences. No assertions are made here for different local rules, repeated vertices within one scan, or larger characteristic-two alphabets.

## Proof

**1. The induced edge action.** Put \(y_i=x_i+x_{i+1}\) and note \(\sum_{i=0}^{n-1}y_i=0\). The map \(x\mapsto y\) has kernel \(\{(0,\ldots,0),(1,\ldots,1)\}\); conversely every even-sum edge word \(y\) has exactly two preimages, distinguished by \(x_0\). Updating site \(i\) changes \(x_i\) by \(x_{i-1}+x_{i+1}=y_{i-1}+y_i\) and therefore swaps exactly \(y_{i-1}\) and \(y_i\). The local vertex update is an involution, so every complete scan is a bijection.

**2. Reduction of arbitrary scan orders.** Orient edge \(i\to i+1\) when \(p_i<p_{i+1}\), and orient it oppositely otherwise. This acyclic orientation is recorded by a cyclic binary word with exactly \(k\) ones and \(m\) zeros. Two linear extensions of the same acyclic orientation differ by interchanging consecutive nonadjacent vertices; their local update maps commute, so their complete scan maps coincide. Moving the first vertex to the last position in a scan conjugates its full map by that vertex's involution. This moves a source to a sink (or reverses the move), changing the orientation word by exchanging one adjacent unequal pair of bits. Conversely any adjacent unequal bits represent a source/sink at their common vertex; choosing a linear extension starting/ending at that vertex implements the exchange. The graph of cyclic binary words with fixed numbers \(k\) and \(m\) of bits is connected under such exchanges. Hence **all** scans having the same \(k\) have conjugate global maps, and in particular identical fixed-power counts and exact orders.

It is therefore enough to use the canonical scan
\[
\pi_k=(0,1,\ldots,k-1,\;n-1,n-2,\ldots,k).
\]
This is a scan with exactly \(k\) forward-oriented edges.

**3. Two edge rotations and an anchor cocycle.** Split the edge word into \(u=(y_0,\ldots,y_{k-1})\) and \(v=(y_k,\ldots,y_{n-1})\), of respective lengths \(k,m\). Directly composing the local adjacent swaps in the canonical order yields
\[
(u_0,\ldots,u_{k-1};v_0,\ldots,v_{m-1})\longmapsto
(u_1,\ldots,u_{k-1},u_0;v_{m-1},v_0,\ldots,v_{m-2}).
\]
Thus the first block rotates left, the second right. Site zero is updated first and changes by \(y_{n-1}+y_0=u_0+v_{m-1}\). Write the state uniquely as \((u,v,a)\) with \(a=x_0\) and the constraint \(\sum u+\sum v=0\); then the two rotations and this anchor change describe the entire scan.

**4. Exact fixed-power count.** A word fixed by the \(t\)-th power of a rotation on \(k\) coordinates is determined by \(g=\gcd(k,t)\) free bits. Similarly the second block has \(h=\gcd(m,t)\) free bits. Let \(U\) and \(V\) be the respective sums of those \(g\) and \(h\) free bits. The edge-sum constraint is
\[
(k/g)U+(m/h)V=0\pmod2.
\]
Over \(t\) steps, the anchor change is \((t/g)U+(t/h)V\), so return of the complete state imposes the second equation
\[
(t/g)U+(t/h)V=0\pmod2.
\]
All four coefficients are integers. These equations define a linear map from \(\mathbb F_2^2\) to itself whose two rows are not simultaneously zero: since \(g\) and \(h\) are greatest common divisors, \(k/g\) and \(t/g\) cannot both be even, and neither can \(m/h\) and \(t/h\). Its rank is \(1+\epsilon_t\) because the determinant modulo two is
\[
\frac{k}{g}\frac{t}{h}+\frac{m}{h}\frac{t}{g}
\equiv\frac{nt}{gh}\pmod2.
\]
The map from the \(g+h\) independent edge-pattern bits to \((U,V)\) is surjective. Thus exactly \(2^{g+h-1-\epsilon_t}\) even-sum edge words meet the return conditions. Every one permits two anchor values, giving the claimed \(2^{g+h-\epsilon_t}\) complete fixed points. Möbius inversion on the divisor lattice yields \(P_d\), and dividing by \(d\) gives the cycle count.

**5. Exact scan order.** The edge permutation consists of cycles of lengths \(k,m\), so its order is \(L=\operatorname{lcm}(k,m)\). For \(n\ge3\), the action of a coordinate permutation on even-sum binary edge words is faithful: vectors with exactly two selected ones distinguish any nonidentity coordinate permutation. Therefore the complete scan order is a multiple of \(L\). After \(L\) scans the edge word returns; the anchor difference is
\[
(L/k)U+(L/m)V,
\]
where now \(U=\sum u\), \(V=\sum v\), and \(U=V\) by even parity. Both values \(U=V=0\) and \(U=V=1\) occur. Hence \(F_\pi^L\) is the identity precisely when \(L/k\) and \(L/m\) have the same parity; otherwise it is a nontrivial involution changing the anchor. This parity condition is equivalent to equal \(2\)-adic valuations of \(k\) and \(m\), and \(F_\pi^{2L}=I\), proving the exact order formula.

**6. Frequency of the scan-order statistic.** Cyclically rotating a permutation of the vertices leaves \(k\) unchanged (the corresponding scan maps are conjugate). Every class of such rotations has a unique representative with vertex zero first and has size \(n\). For a representative beginning with zero, the ascending cycle-edge count equals one plus the number of ascents in the induced ordering of vertices \(1,\ldots,n-1\). Hence the frequency is \(nA(n-1,k-1)\).

The fixed-point corollary follows from \(t=1\), giving \(g=h=1\) and \(\epsilon_1\equiv n\pmod2\).

## Verification

The self-contained Python 3 verifier in `verify.py` computes the binary linear scan matrix directly, checks the nullity of each \(F_\pi^t-I\) against the formula, checks the exact candidate order, and exhaustively enumerates orbit sizes and scan-order frequencies in small dimensions. The recorded run in `verification_output.txt` reports `ALL_CHECKS_PASSED`, covering 12,310 matrix/order cases, 5,910 exhaustively enumerated scan permutations on rings of sizes three through seven, and 695,472 configurations in those exhaustive checks. Sampling additionally covers dimensions eight through twenty-five. The computation checks finite instances; the preceding algebraic argument proves the general result.

Run from a directory containing both files: `python3 verify.py`. Only the Python standard library is used.

## Relationship to prior work

Macauley, McCammond and Mortveit (2008, arXiv:0808.1238), in their Section 5 and Theorem 5.4, study the **same Rule 150** on binary cycles and identify its global dynamics group. They explicitly describe local swaps of block boundaries, which supplies a natural conceptual antecedent of the edge-difference coordinates used above. Their theorem classifies the generated group and its group-action orbits, not the primitive-period census of **each one-scan permutation**. The present statements concern individual products of all local generators, not the global group orbit count.

Macauley and Mortveit (2008, arXiv:0802.4412) establish cycle equivalence under shifts and source-to-sink moves for general sequential graph dynamical systems; their orientation-count results are relevant to the conjugacy step. Those general equivalence theorems do not determine the explicit fixed-power formula on the two rotation blocks.

Defant (2015, arXiv:1511.06966), Theorem 4.1, determines Rule 150/105 primitive-period populations with the **identity scan order**. The identity case of the formula here is \(k=n-1\) or \(k=1\); the new scope is every possible permutation, including scan-order-dependent periods. The underlying invertibility and adjacency-swap ideas are prior art; the claim of contribution is the complete arbitrary-schedule enumeration and the exact order phase diagram, not the invention of those tools.

## Limitations

Only simple scans (each vertex updated once) and binary Rule 150 on finite simple cycles are covered. General fair update words, heterogeneous local rules, and other fields remain unproved. The period formulas do not claim independence of update order; only dependence through \(k\). The finite experiments are supporting checks, not independent verification of the infinite proof. Although comparisons with the three cited primary full texts and accessible mathematical research records found no same-strength theorem, a differently phrased or less accessible historical equivalent remains possible. No independent audit has been performed.

## References

- Colin Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966 (first submitted 2015-11-22). Particularly Theorem 4.1 and the definition of the identity scan.
- Matthew Macauley, Jon McCammond and Henning S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238 (first submitted 2008-08-08). Particularly Section 5, Theorem 5.4, on Rule 150.
- Matthew Macauley and Henning S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412 (first submitted 2008-02-29). Particularly the cycle-orientation and source/sink equivalence results.
