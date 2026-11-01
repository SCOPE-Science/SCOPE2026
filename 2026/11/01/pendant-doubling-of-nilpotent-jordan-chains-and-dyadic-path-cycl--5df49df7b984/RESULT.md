# Pendant doubling of nilpotent Jordan chains and dyadic path–cycle clocks

## Finding

Let \(\mathbb F_q\) have characteristic two, \(q=2^h\), \(h\ge1\). For any finite simple graph \(G\) with \(m\ge1\) vertices, attach exactly one new pendant leaf to each vertex, obtaining the corona \(G\circ K_1\). Synchronous neighbor-sum dynamics on this corona acts on \(\mathbb F_q^{2m}\) by
\[
B_G=\begin{pmatrix}A_G&I_m\\ I_m&0\end{pmatrix},
\]
where \(A_G\) is the core adjacency matrix read in characteristic two. The following equivalence and precise structural law hold:

1. Every state of \(B_G\) has a primitive period that is a power of two if and only if \(A_G\) is nilpotent. Equivalently, this happens exactly when \(B_G\) is unipotent.
2. If \(A_G\) has nilpotent Jordan partition \((\lambda_1,\ldots,\lambda_b)\), then
\[
 B_G\sim \bigoplus_{i=1}^b J_{2\lambda_i}(1).
\]
For \(j\ge0\), write \(e_j=\sum_i\min(2^j,2\lambda_i)\). Then the exact fixed-point and primitive-cycle census is
\[
 \#\operatorname{Fix}(B_G^{2^j})=q^{e_j},\qquad C_1=q^b,
\]
\[
 C_{2^j}=\frac{q^{e_j}-q^{e_{j-1}}}{2^j}\quad(j\ge1),
\]
with zero counts after saturation. There are no transient states.
3. For the path core \(P_m\), with \(m\ge1\), the nilpotent condition holds exactly at \(m=2^r-1\), \(r\ge1\), and then \(B_{P_m}\sim J_{2m}(1)\). For the cycle core \(C_n\), with \(n\ge3\), it holds exactly at \(n=2^r\), \(r\ge2\), and then \(B_{C_n}\sim J_n(1)\oplus J_n(1)\).

In particular, when \(r\ge2\), the maximum primitive period on the path-corona of \(P_{2^r-1}\) is \(2^{r+1}\), whereas on the sunlet \(C_{2^r}\circ K_1\) it is \(2^r\). The former has two fewer vertices yet admits twice the maximum time period. Under uniform initial states, the respective fractions having maximal period are \(1-q^{2-2^r}\) and \(1-q^{-2^r}\).

## Assumptions and scope

Time is discrete and synchronous. The state space is the vector space of all labelled vertex configurations, not the set of configurations modulo graph automorphisms. Each vertex receives the sum of all neighboring vertex values without including its own previous state, over any finite field of characteristic two. The core graphs may be disconnected in the structural theorem; the two explicit families are simple paths and simple cycles with the stated size ranges. Primitive periods count distinct labelled cycles, while fixed-state populations count configurations, not cycles.

For any finite invertible map, a configuration is periodic from the initial time. No statement is made that all nonnilpotent cores have any particular odd period; only that they have at least one orbit whose period is not a power of two.

## Proof

**Invertibility and the all-period criterion.** Write \(N=A_G\) and \(B=B_G\). Direct multiplication gives
\[
 B^{-1}=\begin{pmatrix}0&I_m\\I_m&N\end{pmatrix},\qquad B+B^{-1}=\operatorname{diag}(N,N).
\]
The first identity holds over every field; the second uses characteristic two. Hence \(B\) is invertible. If \(N\) is nilpotent, decomposing \(N\) into its nilpotent Jordan blocks and applying the next paragraph makes \(B\) unipotent. Conversely, if \(B\) is unipotent, then \(B+B^{-1}=(B+I)B^{-1}(B+I)\) is nilpotent, because all factors commute and \(B+I\) is nilpotent. Thus \(N\) is nilpotent. Over characteristic two, a finite-order linear operator has all orbit lengths powers of two precisely when some common power \(B^{2^s}\) equals \(I\), which is equivalent to \((B+I)^{2^s}=0\). The common power exists because the finite state set has finitely many orbits. This proves the equivalence.

**Exact Jordan doubling.** Similarity transformations of \(N\) lift blockwise to \(B\), so it suffices to consider \(N=J_\ell(0)\). The characteristic-polynomial identity obtained by eliminating the pendant coordinates is
\[
 \det(tI_{2\ell}-B)=\det((t^2+1)I_\ell+tN)=(t+1)^{2\ell}.
\]
The equality is a polynomial identity (the Schur complement calculation for \(t\ne0\) extends identically). Furthermore,
\[
 (B+I)(x,y)=0\quad\Longleftrightarrow\quad y=x,\ Nx=0.
\]
Since a single nilpotent Jordan block has a one-dimensional kernel, \(B+I\) has one-dimensional kernel. All eigenvalues of \(B\) equal one and exactly one Jordan block occurs, whose size must therefore be \(2\ell\). Taking direct sums proves the asserted Jordan form.

**Fixed points and primitive periods.** On \(J_L(1)=I+J_L(0)\), characteristic two gives \((I+J_L(0))^{2^j}=I+J_L(0)^{2^j}\). The kernel of the difference from the identity has dimension \(\min(2^j,L)\). Summing dimensions over the doubled blocks proves the fixed-state formula. Since every orbit has two-power length, the number of states of *exact* period \(2^j\) equals the difference of fixed-state counts for \(2^j\) and \(2^{j-1}\). Dividing by period gives the displayed number of primitive orbits. For period one, each fixed state is one orbit. The largest necessary two-power satisfies \(2^j\ge2\max_i\lambda_i\); hence the order is the least such two-power, and that maximal length is attained by some state.

**Path core.** Let \(f_m(t)=\det(tI_m-A(P_m))\), with \(f_0=1\) and \(f_1=t\). The tridiagonal continuant relation is \(f_m=t f_{m-1}+f_{m-2}\). A concatenation identity, verifiable by this recurrence, is \(f_{u+v}=f_u f_v+f_{u-1}f_{v-1}\) for positive \(u,v\), and therefore
\[
 f_{2u+1}=f_u(f_{u+1}+f_{u-1})=t f_u^2.
\]
Every even-index polynomial \(f_{2u}\) has nonzero constant term one. Thus for a positive odd index, the condition \(f_{2u+1}=t^{2u+1}\) is equivalent to \(f_u=t^u\), because squaring polynomials is injective over a field. Repeated halving shows that \(f_m=t^m\) if and only if \(m=2^r-1\), \(r\ge1\). At these sizes, the path adjacency kernel is one-dimensional: endpoint equations force even-indexed coordinates to zero, while the odd-indexed coordinates are equal. Hence its nilpotent Jordan form consists of one block \(J_m(0)\), and the corona form is \(J_{2m}(1)\).

**Cycle core.** Let \(S\) be the cyclic shift of \(n\) rim coordinates. In characteristic two,
\[
 A(C_n)=S+S^{-1}=S^{-1}(S+I)^2.
\]
If \(n=2^r\) with \(r\ge2\), the cyclic shift has minimal and characteristic polynomial \((t+1)^n\), hence it is one Jordan block at eigenvalue one. Because \(S^{-1}\) is invertible and commutes with \(S+I\),
\[
 \dim\ker A(C_n)^j=\min(2j,n).
\]
This is exactly the kernel-growth sequence of two nilpotent blocks of size \(n/2\). Doubling produces \(J_n(1)\oplus J_n(1)\). If \(n\) is not a power of two, the cyclic shift has an eigenvalue \(\zeta\ne1\) over an algebraic closure (its characteristic polynomial is \(t^n-1\), which has a nontrivial odd-order root). Then \(\zeta+\zeta^{-1}\ne0\) in characteristic two, so \(A(C_n)\) cannot be nilpotent. This completes the exact if-and-only-if classification.

**Sharp maximal periods.** For path size \(m=2^r-1\), the largest doubled Jordan block is \(2m=2^{r+1}-2\). For \(r\ge2\), its least dominating power of two is \(2^{r+1}\). For cycle size \(n=2^r\), the largest doubled block is \(n\), with operator order \(2^r\). The fraction at maximal period is the complement of the fraction fixed by the preceding power of two, giving the two displayed probabilities.

## Verification

The standalone standard-library program `verify.py` reconstructs the corona matrices as GF(2) bit matrices and computes matrix-power kernel dimensions by independent elimination. It checks all \(66\) integer-partition nilpotent Jordan inputs of dimensions one through eight against the full doubling formula, the two dyadic graph families for \(r=2,3,4,5,6\), and complete labelled-state orbit enumerations for cycle-core sizes four and eight and path-core sizes three and seven. In the four exhaustive cases it evaluates respectively \(256\), \(65{,}536\), \(64\), and \(16{,}384\) states, for \(82{,}240\) states total, and compares each primitive-period census with its symbolic prediction. Run `python3 verify.py`; expected final output is `CORONA_JORDAN_DOUBLING_VERIFIED`. The full recorded output is in `verify_output.txt`.

These finite computations test the implementation and the stated formulas but are not a substitute for the all-size proof above. Since every matrix in the proof is defined over \(\mathbb F_2\), extending scalars to any \(\mathbb F_{2^h}\) retains the Jordan partitions and yields the symbolic \(q\)-dependent counts.

## Relationship to prior work

Macfarlane's 2004 second-order reversible cellular-automaton analysis introduces first-order matrix equivalents for XOR-type rules and studies their configuration weights. The reversible second-order construction itself is not claimed as new. Barik, Pati and Sarma's 2007 analysis proves eigenvalue reciprocity and nonsingularity of pendant coronas through real symmetric spectral methods (in particular their Lemma 2.1 and Corollary 2.2). The general block form and basic invertibility are likewise prior. The asserted additional contribution is the exact characteristic-two nilpotent-to-unipotent **Jordan partition doubling**, its complete finite-field primitive-orbit census, the exact nilpotence characterization for both path and cycle cores, and the sharp doubled-versus-undoubled dyadic maximum-period comparison. Real symmetric eigenvalue formulas do not determine Jordan block lengths after reduction to characteristic two; information about one-seed weights does not by itself yield the full finite-state orbit census. The nearest records located by mathematical database search concern different reversible rules and different Jordan lifts, without providing this graph-corona classification.

## Limitations

A complete full-text comparison against Macfarlane (2004) could not be completed: accessible abstracts summarize configuration-weight calculations, while an additional full-text access attempt did not return the paper. The possibility of an unindexed equivalent finite-ring computation remains. The result applies to the specified synchronous linear XOR rule, not nonlinear threshold dynamics, asynchronous updates, nor fields of odd characteristic. For nonnilpotent graph cores, the proof guarantees some primitive period with an odd factor but does not enumerate those periods or their basins. Independent external validation has not been performed.

## References

1. A. J. Macfarlane, “Linear reversible second-order cellular automata and their first-order matrix equivalents,” *Journal of Physics A: Mathematical and General* **37** (2004), 10791–10814. Published online 28 October 2004. DOI: 10.1088/0305-4470/37/45/006.
2. S. Barik, S. Pati and B. K. Sarma, “The Spectrum of the Corona of Two Graphs,” *SIAM Journal on Discrete Mathematics* **21** (2007), 47–56. Published online 12 January 2007. DOI: 10.1137/050624029.
