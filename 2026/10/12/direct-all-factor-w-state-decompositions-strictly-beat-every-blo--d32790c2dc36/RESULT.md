# Direct all-factor W-state decompositions strictly beat every blockwise composition of the same bound
## Finding
Let \(k\ge2\), let \(d_1,\ldots,d_k\ge3\), and let \(W_{d_i}\) denote the generalized W-state of order \(d_i\). For every nonempty block \(B\subseteq\{1,\ldots,k\}\), put
\[
U(B)=2^{|B|-1}\left(\sum_{i\in B}d_i-2|B|+2\right).
\]
For a singleton, \(U(\{i\})=d_i\), the exact rank of \(W_{d_i}\). For \(|B|\ge2\), the bound of Canino--Casarotti--Santarsiero supplies a partially symmetric decomposition of the block product of length at most \(U(B)\), and hence an ordinary tensor decomposition of the same length.

For any two disjoint nonempty blocks \(I,J\), the direct bound on their union is strictly smaller than the product of the two block bounds, with exact saving
\[
U(I)U(J)-U(I\cup J)=2^{|I|+|J|-2}\left(\sum_{i\in I}(d_i-2)\right)\left(\sum_{j\in J}(d_j-2)\right)>0.
\]
Therefore every nontrivial set partition \(\mathcal P\) satisfies
\[
U(\{1,\ldots,k\})<\prod_{B\in\mathcal P}U(B).
\]
Equivalently, within this constructive family of rank bounds, merging blocks always strictly improves the certified decomposition length.

## Assumptions and scope
The base field is \(\mathbf C\), matching the cited rank theorem. Every degree satisfies \(d_i\ge3\). The comparison concerns decomposition lengths certified by the Canino--Casarotti--Santarsiero bound on nonsingleton blocks and the exact one-factor rank on singleton blocks. It applies simultaneously to the partially symmetric decompositions furnished by that construction and to the resulting ordinary tensor-rank upper bounds.

No equality with the actual rank is assumed for nonsingleton blocks. In particular, the result does not exclude a different blockwise method, using sharper block ranks or a different construction, from producing a shorter decomposition than the displayed direct upper bound.

## Proof
Write
\[
A_B=\sum_{i\in B}(d_i-2).
\]
Since every \(d_i\ge3\), each nonempty block has \(A_B>0\), and the defining expression becomes
\[
U(B)=2^{|B|-1}(A_B+2).
\]
For disjoint nonempty \(I,J\), let \(r=|I|\) and \(s=|J|\). Then
\[
\begin{aligned}
U(I)U(J)-U(I\cup J)
&=2^{r+s-2}\left((A_I+2)(A_J+2)-2(A_I+A_J+2)\right)\\
&=2^{r+s-2}A_IA_J.
\end{aligned}
\]
This is strictly positive because \(A_I,A_J>0\). The same formula remains valid when either block is a singleton, because \(2^0((d_i-2)+2)=d_i\).

Now start with any nontrivial set partition \(\mathcal P\). Replace any two blocks \(I,J\) by their union. The displayed identity shows that replacing the factor \(U(I)U(J)\) by \(U(I\cup J)\) strictly decreases the product. Repeating until one block remains proves
\[
U(\{1,\ldots,k\})<\prod_{B\in\mathcal P}U(B).
\]

## Verification
The initiating paper was inspected at its definition of generalized W-states, the statement that \(\operatorname{rk}(W_d)=d\), Theorem 1.1, Corollary 1.2, and the comparison with earlier bounds. The theorem states that for every \(k\ge2\) and \(d_i\ge3\), the partially symmetric rank, and therefore the ordinary tensor rank, is at most
\[
2^{k-1}(d_1+\cdots+d_k-2k+2).
\]
The algebraic merge identity above was expanded directly. As a consistency check only, it was also evaluated on thousands of randomly chosen integer degree tuples and two-block splits; those finite tests are not used as proof.

## Relationship to prior work
Canino--Casarotti--Santarsiero give the new all-factor upper bound and an explicit decomposition attaining that length, but do not state the partition/merge inequality above. Their paper recalls that Ballico--Bernardi--Christandl--Gesmundo previously proved the weaker general bound \(2^{k-1}(d_1+\cdots+d_k)\), while also obtaining the sharper special bound \((k+2)2^{k-1}\) for \(W_3^{\otimes k}\). Gałązka's two-factor estimate coincides with the recent bound when \(k=2\). The older geometric strict-submultiplicativity paper studies conditions for rank or border-rank strictness, but does not provide this exact all-degree merge-saving identity.

The new statement is not merely qualitative strict submultiplicativity of tensor rank. It isolates a structural property of the recent constructive bound: every application to all factors at once is strictly more efficient than composing applications of that same bound across any partition, with an exact positive saving at each merge.

## Limitations
The statement compares certified upper-bound lengths, not exact ranks. It does not prove optimality of the direct decomposition, does not compare against every possible specialized block bound, and does not claim that the actual rank itself satisfies the same exact merge-gap formula. The underlying recent theorem is over \(\mathbf C\), and no extension to other fields is asserted here.

A residual originality risk is that the elementary merge identity may have been observed informally or in unindexed notes without being stated in the checked sources.

## References
1. S. Canino, A. Casarotti, P. Santarsiero, “A new bound on the rank of tensor product of W-states,” arXiv:2512.05828v1; Proc. Amer. Math. Soc. 154 (2026), 5095–5117, DOI 10.1090/proc/17856.
2. E. Ballico, A. Bernardi, M. Christandl, F. Gesmundo, “On the partially symmetric rank of tensor products of W-states and other symmetric tensors,” arXiv:1803.01623v2; Rend. Lincei Mat. Appl. 30 (2019), 93–124, DOI 10.4171/RLM/837.
3. E. Ballico, A. Bernardi, F. Gesmundo, A. Oneto, E. Ventura, “Geometric conditions for strict submultiplicativity of rank and border rank,” arXiv:1909.03811v2; Ann. Mat. Pura Appl. 200 (2021), 187–210.
4. M. Gałązka, “Multigraded apolarity,” Math. Nachr. 296 (2023), 286–313, DOI 10.1002/mana.202000484.
