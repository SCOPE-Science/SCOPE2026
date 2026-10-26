# An odd-degree attractor inversion between crown and rook majority dynamics

## Finding

Let \(R_n=K_2\square K_n\), the two-row rook graph (equivalently, the complement of the crown graph \(K_{n,n}-M_n\)), with \(n\ge3\). Apply synchronous binary majority voting over **open** neighborhoods, retaining the old bit in case of a tie. Write \(F_n\) for the update and \(d(x)=\min\{t\ge0:F_n^{t+2}(x)=F_n^t(x)\}\) for the transient depth. Put \(k=\lfloor n/2\rfloor\), \(B=\binom{n}{k}\) and \(L=\sum_{j=0}^{k-1}\binom{n}{j}\). All configurations are labelled.

The only primitive periods are one and two. If \(n=2k\ge4\), the numbers of fixed and primitive-period-two configurations are, respectively,
\[
Q_n=4+B,\qquad C_n=B^2-B.
\]
The exact numbers \(D_{n,t}=|\{x:d(x)=t\}|\) are
\[
D_{n,0}=4+B^2,\qquad D_{n,1}=4L^2+4B-4,\qquad D_{n,2}=4B(L-1),\qquad D_{n,t}=0\ (t\ge3).
\]

If \(n=2k+1\ge3\), the corresponding numbers are
\[
Q_n=4,\qquad C_n=2(k+2)B,\qquad D_{n,0}=4+2(k+2)B.
\]
Define
\[
A_n=4L^2+2B\bigl(2^{k+1}+(k+1)^2\bigr),\qquad
H_n=4\sum_{a=1}^{k-1}a\binom{n}{a}\binom{n-a}{k}.
\]
Then
\[
D_{n,1}=A_n-D_{n,0},\qquad
D_{n,2}=4^n-A_n-H_n,\qquad
D_{n,3}=H_n,\qquad D_{n,t}=0\ (t\ge4).
\]
Thus the sharp maximum depth is two for even \(n\) and for \(n=3\), and three for odd \(n\ge5\). In particular \(F_n^5=F_n^3\) for all \(n\ge3\), and \(F_n^4=F_n^2\) for even \(n\).

For odd \(n\), the previously determined total recurrent count on the complementary crown graph equals \(4+2(k+2)B\), exactly the new rook-graph count. But on the crown graph \(2(k+2)B+2\) of these states are fixed and only two have period two, whereas the rook graph has just four fixed states and \(2(k+2)B\) period-two states. Complementing the graph therefore preserves the entire recurrent count but nearly exchanges fixed and oscillatory behaviour.

## Assumptions and scope

The graph has vertices \((r,j)\), \(r\in\{0,1\}\) and \(j\in\{1,\ldots,n\}\). Two vertices are adjacent if they are in the same row and different columns, or in different rows and the same column. Its degree is \(n\). A state is an ordered pair \((U,V)\) of subsets of \(\Omega=\{1,\ldots,n\}\) indicating the occupied columns in the two rows. The result holds for all initial states, without stochastic assumptions, and all counts distinguish vertex labels. A primitive-period-two configuration is a state, so there are \(C_n/2\) distinct nontrivial two-cycles. No assertion is made about asynchronous voting or larger row dimensions.

## Proof

Write \(a=|U|\), \(b=|V|\) and \(c=|U\cap V|\). A top-row site \(j\) sees \(a-\mathbf1_U(j)+\mathbf1_V(j)\) occupied neighbors; a bottom-row site has the analogous count with \(U,V\) exchanged. Taking the strict majority of \(n\) neighbours, with tie retention, gives the following **exact** set update \(F_n(U,V)=(g(U,V),g(V,U))\).

For \(n=2k\):
\[
g(U,V)=\begin{cases}\varnothing,&a<k,\\ V,&a=k,\\ \Omega,&a>k.\end{cases}\tag{1}\]
If both row populations equal \(k\), the two sets swap forever; this yields \(B^2\) recurrent configurations, of which \(B\) are fixed. If neither population equals \(k\), the first image consists of two monochromatic rows and is fixed, giving the four other fixed configurations. If exactly one row is balanced, its image is the other old row while the other image is monochromatic. The next image is fixed. Such a state is already one update from periodicity only if the unbalanced row is empty or full. Among the \(2B\cdot2L\) states with exactly one balanced row, \(4B\) have this property and the remaining \(4B(L-1)\) have depth two. All \(4L^2\) states with no balanced row are mapped to recurrent states in one update. Together these give the even formulas and show sharpness of depth two for \(k\ge2\), by choosing row populations \(k\) and \(k-1\).

For \(n=2k+1\), let \(U^c=\Omega\setminus U\). The exact update is
\[
g(U,V)=\begin{cases}
\varnothing,&a<k,\\
V\setminus U,&a=k,\\
U^c\cup V,&a=k+1,\\
\Omega,&a>k+1.
\end{cases}\tag{2}\]
Classify each row population as \(L\) (less than \(k\)), \(M\) (equal to \(k\)), \(N\) (equal to \(k+1\)) or \(H\) (greater than \(k+1\)). Equation (2) makes the full global dynamics a four-by-four type analysis, with only intersection \(c\) needed inside each type pair. The following details prove both the period classification and the maximum depth.

For types \(MM\), the image is \((V\setminus U,U\setminus V)\), two disjoint sets of size \(k-c\). It is a two-cycle precisely when \(c=0\); otherwise it reaches the empty state in at most two updates. For \(NN\), the image is \((\Omega\setminus(U\setminus V),\Omega\setminus(V\setminus U))\), both of size \(k+c\), and is a two-cycle precisely when \(c=1\); otherwise it reaches the full state in at most two updates. For \(MN\), the image is \((W,\Omega\setminus W)\), where \(W=V\setminus U\) has size \(k+1-c\). If \(c=0\), the original complementary-row state belongs to a two-cycle; if \(c=1\), its image belongs to a two-cycle; and if \(c\ge2\), it reaches \((\varnothing,\Omega)\) by the second update. The \(NM\) case is symmetric.

If both types lie in \(\{L,H\}\), the first image is one of the four fixed homogeneous-row states. If the types are \(LM\) or \(ML\), the first image has one empty row and the other has fewer than \(k\) ones, so the second image is empty; by exchanging zeros and ones, \(HN\) and \(NH\) reach the full state within two steps. In the \(LN\) case, the first image is \((\varnothing,W)\) with \(|W|=k+c\). It reaches a fixed point on the second update unless \(c=1\), when the next row contains \(k\) ones and the third update makes it empty. The \(NL\) case is symmetric. Taking bitwise complements gives the corresponding \(HM\) and \(MH\) cases, with an extra third update precisely at the complementary exceptional intersection. This exhausts the 16 type pairs, proving the universal depth-three bound and the absence of other cycles.

The recurrent odd states are: the four homogeneous-row states; ordered disjoint pairs of \(k\)-sets (\((k+1)B\) states); ordered pairs of \((k+1)\)-sets meeting in exactly one column (\((k+1)B\) states); and the \(2B\) pairs of complementary row sets with cardinalities \(k,k+1\). All nonuniform listed states have exact period two. The resulting count is \(4+2(k+2)B\).

For odd \(n\), the number \(A_n\) of initial states whose **first image** is already recurrent is obtained by partitioning the 16 type pairs: types in \(\{L,H\}^2\) contribute \(4L^2\); \(LM,ML,HN,NH\) contribute \(4B(2^k-1)\); \(MM,NN\) contribute \(2B(k+2)\); and \(MN,NM\) contribute \(2B(1+k(k+1))\). Their sum simplifies to the displayed \(A_n\). Depth exactly three occurs only in \(LN,NL,HM,MH\) with the exceptional intersection condition. In \(LN\), fixing the small-row size \(a\in\{1,\ldots,k-1\}\), the condition \(|U\cap V|=1\) yields \(a\binom{n}{a}\binom{n-a}{k}\) choices. The other three cases contribute equally by row exchange or bit complementation, proving the formula for \(H_n\). Subtracting \(A_n\) and \(H_n\) from the total \(4^n\) configurations gives the depth-two count. When \(n=3\), the sum defining \(H_n\) is empty; when \(n\ge5\) is odd, choosing \(a=1\) and \(c=1\) realizes depth three. Choosing \(U=\varnothing\) and \(|V|=k+1\) realizes depth two at \(n=3\). This proves sharpness in all sizes.

The complementary crown-graph comparison uses the previously established crown census solely as a numerical comparison; it is **not** used to prove any rook-graph formula above.

## Verification

The standalone standard-library program `verify_rook.py` independently computes each individual vertex's neighbour votes and separately computes the set update (1)–(2). For every labelled state and every \(3\le n\le9\), it verifies equality of these independent updates, the period-entry identity, all recurrence and depth counts, and sharpness; this covers 349,504 initial configurations. It additionally checks nonnegativity and population-total consistency of the displayed formulas for \(3\le n\le400\). Run `python3 verify_rook.py` from the directory containing this document. The recorded stdout is in `verification_output.txt`. Exhaustive checks for finite \(n\) are supplemental to the all-size case proof.

## Relationship to prior work

Goles and Olivos (1980) established eventual period at most two for symmetric threshold maps; that theorem alone gives neither a graph-specific recurrence census nor a constant sharp transient bound. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, Sections 1 and 3) study majority-voting convergence bounds on general graphs and graph modules, not the two-row rook-graph period and basin census. Their general bounds do not imply the particular formulas or parity-dependent exact depth. The rook graph is also the complement of the crown graph, whose previously derived majority census has a matching total recurrent count when \(n\) is odd but strikingly different fixed-versus-period-two composition. The equality of totals in the odd case is an explicit comparison, not a claim that graph complementation generally preserves recurrence.

## Limitations

This class-specific result does not classify majority dynamics on \(K_m\square K_n\) for \(m\ge3\), quantify mixing from random initial opinions or extend to asynchronous updates. Search-based novelty is not a proof of historical uniqueness: an equivalent analysis of two matched cliques under another name may exist. The historical 1980 paper was checked through bibliographic metadata and abstract, not its full text; the closest 2015 majority-convergence preprint was inspected in full through its accessible PDF. No independent external audit has been performed.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn, and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519v1 (first posted 2015-08-14), especially Definitions 2–3 and Theorem 1.2.
3. The majority-dynamics attractor census of the crown graph \(K_{n,n}-M_n\) (accessible previous research record, item identifier `e46cbd31-3c95-45da-a8b4-e0e0f1485ee7`, used for numerical comparison only).
