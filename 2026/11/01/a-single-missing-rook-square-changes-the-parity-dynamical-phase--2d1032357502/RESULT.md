# A single missing rook square changes the parity dynamical phase and creates a five-step Jordan chain

## Finding

Let \(a,b\ge2\). From the \(a\)-by-\(b\) rook graph \(K_a\square K_b\), delete one vertex (one square of the board), with its incident edges. Let \(F\) be simultaneous nearest-neighbor summation, without self-feedback, on the remaining \(E=ab-1\) vertices over any field \(\mathbb F_q\) with \(q=2^h\), \(h\ge1\). Put \(T(x)=\min\{t\ge0:F^t(x)\text{ is periodic}\}\). The **complete Jordan form**, all recurrent periods, and exact first-entry populations depend only on the parities of \(a,b\):

**Both even.**
\[
F\sim J_3(0)\oplus J_2(0)^{\oplus(a+b-4)}\oplus J_1(0)^{\oplus(a-2)(b-2)}.
\]
Every state reaches zero, and \(F^3=0\ne F^2\). Let \(N_t=\#\{x:T(x)=t\}\). Then
\[
(N_0,N_1,N_2,N_3)=(1,\ q^{(a-1)(b-1)}-1,\ q^{ab-2}-q^{(a-1)(b-1)},\ q^{ab-1}-q^{ab-2}).
\]

**Both odd.**
\[
F\sim J_2(1)\oplus J_1(1)^{\oplus(a+b-4)}\oplus J_1(0)^{\oplus(a-1)(b-1)}.
\]
Every state is periodic after at most one update: \(F^3=F\), and the bound is sharp. There are \(q^{a+b-3}\) fixed states and \((q^{a+b-2}-q^{a+b-3})/2\) primitive two-cycle orbits. The two entry-time layers have sizes \(N_0=q^{a+b-2}\) and \(N_1=q^{ab-1}-q^{a+b-2}\). In each layer, exactly a fraction \(1/q\) eventually reaches a fixed state and a fraction \(1-1/q\) enters a primitive two-cycle.

**Mixed parity.** Let \(o\ge3\) be the odd side length and \(s\ge2\) the even side length. Then
\[
F\sim J_5(0)\oplus J_2(0)^{\oplus(o-3)}\oplus J_1(0)^{\oplus(o-1)(s-2)}\oplus J_1(1)^{\oplus(s-2)}.
\]
Every state eventually becomes fixed and \(F^6=F^5\ne F^4\). In particular, deleting one square **eliminates every two-cycle** that existed for the undeleted mixed-parity rook graph, while creating a sharp five-update transient. Put \(r_0=E\) and
\[
(r_1,r_2,r_3,r_4,r_5)=(o+s-1,\ s+1,\ s,\ s-1,\ s-2).
\]
The precise first-entry populations are
\[
N_0=q^{s-2},\qquad N_t=q^{E-r_t+s-2}-q^{E-r_{t-1}+s-2}\quad(1\le t\le5).
\]
In particular, for independent uniformly distributed initial states, \(\Pr(T=5)=1-1/q\), independently of the graph dimensions.

## Assumptions and scope

The graph is simple and undirected; rook squares share an edge exactly when they lie in one row or one column. Exactly the bottom-right square is removed, without loss by symmetry. The state space is the \(E\)-dimensional vector space over \(\mathbb F_q\), and the update is the adjacency operator of the **vertex-deleted** rook graph. The characteristic-two assumption is essential. A primitive orbit has least period two and is counted once, not twice. The first periodic entry time \(T\) includes zero for initially recurrent states.

## Proof

**1. Incidence reduction.** Let \(H=K_{a,b}-e\), with \(e\) one distinguished bipartite edge, so that its line graph is the punctured rook graph. Let \(B\) be the unoriented vertex-edge incidence matrix of \(H\), reduced to the field of characteristic two. Every edge belongs to two endpoints, so
\[
F=B^{\mathsf T}B,\qquad Q=BB^{\mathsf T},\qquad F^k=B^{\mathsf T}Q^{k-1}B\quad(k\ge1).
\]
Because \(H\) is connected for \(a,b\ge2\), \(B\) maps onto the even-coordinate subspace \(U\) of dimension \(a+b-1\), and \(\ker(B^{\mathsf T}|_U)\) is zero when \(a+b\) is odd and is the one-dimensional space spanned by the global all-ones vector when \(a+b\) is even. Thus \(\operatorname{rank}F=a+b-1\) in mixed parity and \(a+b-2\) otherwise.

**2. Dimension-independent reduction.** On \(U\), split vertex coordinates into ordinary left vertices (\(a-1\) of them), one distinguished left vertex, ordinary right vertices (\(b-1\)), and one distinguished right vertex. Let \(\alpha=a\bmod2\) and \(\beta=b\bmod2\), viewed in \(\mathbb F_q\). For an input \((x_i;y_j)\in U\), write \(p=\sum_i x_i=\sum_j y_j\). Its image under \(Q\) is
\[
\begin{aligned}
(Qx)_i&=\beta x_i+p &&(i<a),\\
(Qx)_a&=(\beta+1)x_a+p+y_b,\\
(Qy)_j&=\alpha y_j+p &&(j<b),\\
(Qy)_b&=(\alpha+1)y_b+p+x_a.
\end{aligned}
\]
On the ordinary left coordinates, the zero-sum subspace is an eigenspace of eigenvalue \(\beta\); on the ordinary right coordinates it is an eigenspace of eigenvalue \(\alpha\). If the side length is even, its ordinary count is odd: split the ordinary space into its zero-sum subspace and the all-ones line (whose sum is one). If the side length is odd, its ordinary count is even: the ordinary all-ones vector has sum zero, so split its zero-sum subspace further into that all-ones line and a complementary space of dimension (side length minus three), and use one coordinate vector to represent the remaining sum-one direction. Each complementary space is invariant and \(Q\) acts there as the indicated scalar. The remaining core is invariant because the displayed formulas involve only the ordinary coordinate sum, the ordinary all-ones vector, and the distinguished coordinate. Its matrix and total-coordinate constraint depend only on the two parities.

Consequently, on \(U\) the operator \(Q\) is similar to a core corresponding to the **minimum dimensions of the same parity** (two for an even side and three for an odd side), plus \(a-a_0\) scalar blocks of eigenvalue \(\beta\) and \(b-b_0\) scalar blocks of eigenvalue \(\alpha\), where \(a_0=2\) or \(3\) and similarly for \(b_0\). The kernel of \(B^{\mathsf T}|_U\), when present, lies entirely in that core: it is the global all-ones vector, which is included in the displayed core basis. Hence the extra blocks contribute directly to the ranks of \(F^k\) at \(k\ge2\), while the first rank was determined in step 1. This is an **all-dimensions decomposition**, not finite-size extrapolation.

**3. Three exact core calculations.** Over \(\mathbb F_2\), use as basis of \(U\) the vectors \(e_i+e_{a+b}\), \(1\le i<a+b\), and form \(Q=BB^{\mathsf T}\). For the three minimum representatives, the rows of the core matrices, encoded as binary integers with bit \(j\) the coefficient of basis vector \(j\) (zero-indexed), are:

* \((a_0,b_0)=(2,2)\): \([3,6,3]\), whose power ranks are \((3,2,1,0)\);
* \((3,2)\): \([7,7,12,15]\), whose power ranks are \((4,3,2,1,0)\);
* \((3,3)\): \([6,5,24,15,23]\), whose ranks are \((5,4,4,4,\ldots)\).

Direct multiplication of the corresponding punctured-rook adjacency matrices gives, respectively, \(F^3=0\), \(F^5=0\), and \(F^3=F\), with rank sequences \((3,2,1,0)\), \((5,4,3,2,1,0)\), and \((8,4,4,\ldots)\). In the last case \(\operatorname{rank}(F^2+F)=1\), establishing one nontrivial unipotent block. These integer-bit matrix multiplications are reproduced in the bundled checkers. Since swapping board dimensions conjugates the update, these are all parity cores.

**4. Lift to all sizes and read Jordan blocks.** The scalar blocks from step 2 contribute zero or one to the positive-power ranks, while the global all-ones kernel in the two same-parity cases remains inside the core. Thus the exact \(\operatorname{rank}F^t\) sequences are:
\[
\begin{array}{c|l}
\text{parities}&\operatorname{rank}(F^0),\operatorname{rank}(F^1),\ldots\\\hline
\text{even--even}&E,a+b-2,1,0,0,\ldots\\
\text{odd--odd}&E,a+b-2,a+b-2,\ldots\\
\text{mixed}&E,o+s-1,s+1,s,s-1,s-2,s-2,\ldots
\end{array}
\]
The same core identities and scalar eigenblocks give \(F^3=0\), \(F^3=F\), and \(F^6=F^5\) in the respective cases. In the odd--odd case \(\operatorname{rank}(F^2+F)=1\); no odd--odd zero-eigenvalue block has length greater than one. In mixed parity the stable image is fixed pointwise, so the positive eigenvalue has only size-one blocks. Differences between successive ranks of \(F^t\) determine the number of nilpotent blocks with length at least \(t+1\), giving exactly the three Jordan forms in the Finding. For example, the mixed ranks leave one nilpotent block of length five, \(o-3\) of length two, and \((o-1)(s-2)\) of length one. The displayed forms also show that all stated sharp bounds are attained.

**5. Populations.** For each Jordan decomposition, the recurrent subspace is its eigenvalue-one generalized eigenspace, and the first-entry layers follow by counting kernels of successive powers on the nilpotent summand. A dimension-\(d\) space over \(\mathbb F_q\) has \(q^d\) states. In the odd--odd case the unique \(J_2(1)\) block induces one rank-one difference \(F+I\) on the recurrent space; therefore precisely \(q^{a+b-3}\) recurrent states are fixed and the remaining \(q^{a+b-2}-q^{a+b-3}\) are in primitive two-cycles. Each transient layer is a product of the same recurrent space with a nilpotent layer, so its fixed/two-cycle proportions are \(1/q\) and \(1-1/q\). All other counts are the differences of the nested kernel cardinalities. The mixed final shell has cardinality \(q^E-q^{E-1}\), proving its probability \(1-1/q\).

## Verification

`check_linear.py` constructs each punctured rook adjacency matrix directly, multiplies bit-packed matrices over \(\mathbb F_2\), and compares every rank of powers zero through six against the asserted formulas for all \(2\le a,b\le11\) (100 size pairs, up to 120 vertices). It also tests the universal annihilating identities. `check_states.cpp` separately builds adjacency masks from rook moves, evolves every binary initial state for all graph size pairs \(2\le a,b\le8\) with \(ab-1\le17\), and compares actual least periods and first-entry layers against the closed expressions (21 parameter pairs; 419,400 states). The two stdout records are included. These finite tests corroborate the core multiplication; the infinite theorem is the invariant decomposition in the proof.

## Relationship to prior work

Ducey, Gerhard, and Watson (arXiv:1507.06583v1, 2015-07-23), prove Smith and critical group formulas for the **intact square** rook graph, explicitly relating it to the line graph of a complete bipartite graph. Peeters (2002) develops modular ranks and minimal polynomials for Hamming graphs, including intact Cartesian products of complete graphs; its homogeneous-alphabet consequences, and the established mixed-parity Hamming-product classification, are prior coverage. None establishes the present *one-vertex-deleted* Jordan forms, the five-step transient in mixed parity, or the reversal from period-two activity to exclusively fixed points caused by the deletion. The graph \(L(K_{a,b}-e)\) is distinguished from the intact \(L(K_{a,b})\) and from line graphs of complete graphs with matchings deleted; no equivalence or general result in the inspected sources supplies these deleted-edge dynamics. A previous period-two chip-firing result on intact rook-related families concerns a different nonlinear rule, not adjacency summation.

## Limitations

The statement concerns one missing square, all side lengths at least two, fields of characteristic two, and synchronous neighbor sums without self-feedback. It does not treat deleting multiple squares, asynchronous updates, or positive characteristic other than two. Existing work already implies some intact-rook phenomena, so the novelty claim is restricted to the deletion-induced exact Jordan classification and dynamics. A full universal database search cannot guarantee absence of an unindexed equivalent result. The core matrix checks and direct enumerations do not constitute an independent audit; independent validation has not been performed.

## References

1. J. E. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, arXiv:1507.06583v1, first posted 2015-07-23, https://arxiv.org/abs/1507.06583. Especially introduction, Theorem 1.1 and Sections 2–3.
2. R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics 15 (2002), 127–149, DOI:10.1023/A:1013842904024. Especially Section 3, on intact Hamming graphs.
3. C. Marr and M.-T. Hütt, *Topology regulates pattern formation capacity of binary cellular automata on graphs*, arXiv:cond-mat/0502509v1, first posted 2005-02-21, https://arxiv.org/abs/cond-mat/0502509. This provides a distinct nonlinear graph-CA context, not a theorem about the current rule.
