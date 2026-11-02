# Three parity phases in neighbor-sum dynamics on subdivided complete bipartite graphs

## Finding

Let \(S(K_{a,b})\) be the graph obtained by subdividing every edge of the labelled complete bipartite graph \(K_{a,b}\) exactly once, for integers \(a,b\ge1\). Over a finite field \(\mathbb F_q\) of characteristic two, update all vertex labels synchronously to the sum of their neighbors' labels. Write \(n=a+b\), \(N=a+b+ab\), and let \(J_t(\lambda)\) denote a single Jordan block of size \(t\) with eigenvalue \(\lambda\). The complete similarity class of the global update \(F\) is as follows (a zero multiplicity means no block):

1. If \(a,b\) are even,
   \[
   F\sim J_4(0)^{\oplus2}\oplus J_3(0)^{\oplus(n-4)}\oplus J_1(0)^{\oplus(a-2)(b-2)}.
   \]
2. If \(a,b\) are odd,
   \[
   F\sim J_3(0)\oplus J_1(0)^{\oplus(a-1)(b-1)}\oplus J_2(1)^{\oplus(n-2)}.
   \]
3. If exactly one of \(a,b\) is even, denote it by \(e\ge2\), and denote the odd one by \(o\ge1\). Then
   \[
   F\sim J_3(0)^{\oplus(o-1)}\oplus J_1(0)^{\oplus((e-2)(o-1)+1)}\oplus J_4(1)\oplus J_2(1)^{\oplus(e-2)}.
   \]

Thus all states become zero in at most four steps when both sizes are even. When both are odd, all eventual periods divide two. When one size is even and the other odd, genuine primitive four-cycles exist for every \(q\), and all eventual periods divide four. In the mixed-parity case, the unsubdivided \(K_{a,b}\) neighbor-sum map is nilpotent of index at most four: edge subdivision creates recurrence rather than merely delaying it.

For the exact transient census, let \(d\) be the total dimension of the eigenvalue-one blocks and let \(m_j\) be the number of zero-eigenvalue blocks of length \(j\) in the corresponding displayed decomposition. For every integer \(t\ge0\), the number \(C_t\) of initial states whose orbit is already periodic at or before time \(t\) is
\[
 C_t=q^{d+\sum_{j\ge1}m_j\min(t,j)}.
\]
Here \(d=0\), \(2(n-2)\), or \(2e\), in the three cases, respectively. The number entering for the first time at positive time \(t\) is \(C_t-C_{t-1}\), and \(C_0=q^d\).

Let \(R_k\) be the number of states fixed by \(F^k\). The exact exponents \((\log_q R_1,\log_q R_2,\log_q R_4)\) are
\[
 (0,0,0),\qquad (n-2,2(n-2),2(n-2)),\qquad (e-1,2(e-1),2e)
\]
for even-even, odd-odd, and mixed parity, respectively. Consequently the numbers of primitive temporal orbits of lengths \(1,2,4\) are \(R_1\), \((R_2-R_1)/2\), and \((R_4-R_2)/4\). No other primitive lengths occur.

The maximum first-entry time is exactly four in the even-even case, exactly three in the odd-odd case, exactly three in the mixed case with \(o\ge3\), and exactly one in the mixed case with \(o=1\).

## Assumptions and scope

The graph is simple, finite and labelled. Each old edge has one distinct inserted degree-two vertex. There are no self-loops; the current vertex's own label is excluded from its update. Every sum is in \(\mathbb F_q\), where \(q\) is any positive integral power of two. The domain includes the boundaries \(a=1\), \(b=1\), \(a=b=1\), and \(a=b=2\). Jordan blocks and counts are for the full \(N\)-coordinate state space, not just vertex or edge coordinates. A configuration is periodic precisely when some positive power of \(F\) fixes it.

## Proof

**Incidence reduction.** Let \(B\) be the unsigned vertex-edge incidence matrix of \(K_{a,b}\), of size \(n\times ab\), over \(\mathbb F_q\). Every column has two ones. Order the coordinates of \(S(K_{a,b})\) by old vertices followed by inserted vertices. Then
\[
 F=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\quad
 F^2=\begin{pmatrix}L&0\\0&C\end{pmatrix},\quad L=BB^{\mathsf T},\quad C=B^{\mathsf T}B.
\]
The connectedness of \(K_{a,b}\) and the characteristic-two incidence relation give \(\operatorname{rank}B=n-1\), \(\ker B^{\mathsf T}=\langle\mathbf1_n\rangle\), and
\[
 U=\operatorname{im}B=\{x\in\mathbb F_q^n:\sum_i x_i=0\}.
\]
Therefore \(\operatorname{rank}C=n-1-\mathbf1_{2\mid n}\). Writing \(J_{r,s}\) for the \(r\times s\) all-one matrix and \(\epsilon_c=c\pmod2\), direct multiplication yields
\[
 L=\begin{pmatrix}\epsilon_bI_a&J_{a,b}\\J_{b,a}&\epsilon_a I_b\end{pmatrix}.
\]
For \(k\ge1\),
\[
 F^{2k}=\operatorname{diag}(L^k,C^k),\qquad
 F^{2k+1}=\begin{pmatrix}0&L^kB\\B^{\mathsf T}L^k&0\end{pmatrix}.
\]
In particular \(\operatorname{rank}F=2(n-1)\), and \(\operatorname{rank}F^3=2\operatorname{rank}(L|_U)\).

**Powers and ranks.** When \(a,b\) are even, \(L^2=0\), \(\operatorname{rank}L=2\), and \(\operatorname{rank}(L|_U)=1\). Every column of \(LB\) equals \(\mathbf1_n\), so \(B^{\mathsf T}LB=0\) and \(F^4=0\). The ranks of \(F,F^2,F^3,F^4\) are respectively
\[
 2(n-1),\quad n,\quad2,\quad0.
\]
When both sizes are odd, \(L^2=\operatorname{diag}(I_a+J_{a,a},I_b+J_{b,b})\) and \(L^2+L=J_{n,n}\). Because \(J_{n,n}B=0\), one has \(F^5=F^3\). Here \(\operatorname{rank}L=n-1\) and \(\operatorname{rank}(L|_U)=n-2\). The ranks of \(F,F^2,F^3,F^4\) are
\[
 2(n-1),\quad 2n-3,\quad 2n-4,\quad2n-4.
\]
When \(e\) is even and \(o\) odd, use the two corresponding blocks in either order. Direct block multiplication gives \(L^3=L\), \(\operatorname{rank}L=e\), and \(\operatorname{rank}(L|_U)=e\). Thus \(F^7=F^3\), and the ranks of \(F,F^2,F^3,F^4\) are
\[
 2(n-1),\quad2e+o-1,\quad2e,\quad2e.
\]
These polynomial identities show that only the eigenvalues zero and one are possible and that the powers shown already stabilize in rank. Rank differences yield all zero-eigenvalue block multiplicities. For example, in mixed parity the nilpotent part has ranks \(2(o-1),o-1,0\) after its first, second and third powers, hence exactly \(o-1\) blocks of length three, with the remainder of length one. The other two cases follow analogously.

**Nonzero blocks.** Solving \(F(x,y)=(x,y)\) gives \(y=B^{\mathsf T}x\), \(Lx=x\), so \(\dim\ker(F+I)=\dim\ker(L+I)\). For each positive integer \(k\), the operators \(C\) and \(L\) have isomorphic eigenspaces satisfying \((X+I)^k=0\): the maps \(B\) and \(B^{\mathsf T}\) intertwine them and are injective in both directions on those generalized eigenspaces. Consequently
\[
 \dim\ker(F^{2}+I)=2\dim\ker(L+I),\qquad
 \dim\ker(F^{4}+I)=2\dim\ker(L^2+I).
\]
For both odd, direct inspection of \(L\) gives \(\dim\ker(L+I)=n-2\) and \(\dim\ker(L^2+I)=n-2\). The eigenvalue-one primary component has dimension \(2(n-2)\), and its fixed-space dimensions force \(n-2\) blocks \(J_2(1)\). For mixed parity these two dimensions are \(e-1\) and \(e\), respectively. The eigenvalue-one component has dimension \(2e\), and its fixed-space dimensions force one \(J_4(1)\) and \(e-2\) blocks \(J_2(1)\). In the even-even case no nonzero eigenvalue occurs. This completes all three Jordan decompositions.

**Counting and sharpness.** On a nilpotent Jordan block of length \(j\), the kernel of its \(t\)-th power has dimension \(\min(t,j)\). All eigenvalue-one blocks are periodic immediately, and their direct sum has dimension \(d\). This proves the formula for \(C_t\). On a length-\(j\) block at eigenvalue one, the kernel of \((F+I)^{2^k}\) has dimension \(\min(j,2^k)\), which proves the three return-count formulas and their orbit-count consequences. The largest zero block gives the exact maximum transient time, and the presence of \(J_4(1)\) in mixed parity gives primitive four-cycles. The smallest cases are included by the zero-multiplicity convention.

Finally, on the unsubdivided \(K_{e,o}\), its neighbor-sum matrix \(M\) satisfies \(M^2=\operatorname{diag}(J_{e,e},0_o)\) after putting the even shore first. Since \(J_{e,e}^2=eJ_{e,e}=0\) in characteristic two, \(M^4=0\). This proves the subdivision-induced recurrence contrast.

## Verification

The standalone program `check.py` constructs each subdivided graph directly, evolves configurations, computes exact binary matrix ranks, and separately checks the predicted Jordan and return-count consequences. It performs all 648 powers and 243 shifted-rank comparisons for 81 parameter pairs with \(1\le a,b\le9\), complete binary trajectory enumeration on 13 parameter pairs (71,240 initial states), and a separate \(\mathbb F_4\)-valued trajectory enumeration on four parameter pairs (83,008 initial states). Running `python check.py` produces the accompanying `verification_output.txt`. These finite checks corroborate the formulas but the proof above establishes them for all permitted parameters.

## Relationship to prior work

Finite-field additive cellular automata and characteristic-positive spectral methods are classical; see Zaidenberg (2006). Liu and Zhang (first posted 2012) explicitly use vertex-edge incidence matrices and study adjacency spectra of subdivision-join graph operations over conventional coefficient fields. Aledo, Martínez, and Valverde (2015) review general orbit-structure questions for parallel graph dynamical systems. The present statement concerns the characteristic-two Jordan similarity class, sharp transient-entry census, and primitive periods for the *ordinary one-subdivision* of every complete bipartite graph, including nonregular ones. Real adjacency spectra alone do not identify these modular Jordan block lengths or determine the return-space counts. A separately indexed parity census on unsubdivided complete multipartite graphs has a different update matrix and does not imply the present conclusion.

## Limitations

The theorem concerns one simultaneous open-neighborhood sum step per time unit, one subdivision vertex per original edge, and fields of characteristic two. It does not classify nonbinary characteristic, unequal subdivision lengths, asynchronous schedules, or perturbed weights. Results are established by algebraic proof; finite computations are supporting checks, not substitutes for the infinite-parameter argument. The related-literature search was finite and cannot exclude every unindexed equivalent treatment.

## References

1. M. Zaidenberg, *Convolution equations on lattices: periodic solutions with values in a prime characteristic field*, arXiv:math-ph/0606070, first submitted 29 June 2006, https://arxiv.org/abs/math-ph/0606070.
2. X. Liu and Z. Zhang, *Spectra of subdivision-vertex join and subdivision-edge join of two graphs*, arXiv:1212.0619, first submitted 4 December 2012, https://arxiv.org/abs/1212.0619; especially the incidence-matrix discussion in Section 2.
3. J. A. Aledo, S. Martínez, and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), Article 594294, first published 24 March 2015, https://doi.org/10.1155/2015/594294.
4. O. Ogurisu, *Supersymmetric analysis of discrete magnetic Schrödinger operators*, report dated 6 October 2003, Section 3.2 (subdivision and bipartite operator decomposition), https://www.kurims.kyoto-u.ac.jp/~ito/MPHP/confs/rims03/proc/ogurisu.pdf. The original public posting date of this report is not established here.
