# A parity-square law for recurrent majority configurations on Möbius ladders

## Finding
For each integer \(n\ge3\), consider synchronous, open-neighbourhood binary majority dynamics on the Möbius ladder \(M_{2n}\). Let \(F_n\) be the one-round update, \(Q_n=\#\{x:F_n(x)=x\}\), and \(P_n=\#\{x:F_n^2(x)=x\}\). Let \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\). Then
\[
Q_n=L_n+2\cos(n\pi/3),
\qquad
P_n=\begin{cases}
Q_n^2,&n\text{ odd},\\
L_n^2+2,&n\equiv0\pmod6,\\
L_n^2-1,&n\equiv2,4\pmod6.
\end{cases}
\]
Every recurrent state is fixed or belongs to a primitive two-cycle; consequently the exact number of primitive two-cycles is \((P_n-Q_n)/2\). The odd-width square identity and the even-width Lucas corrections distinguish two parity regimes in an entire cubic, vertex-transitive graph family.

## Assumptions and scope
The vertex set is \(\{(i,a):0\le i<n,\ a\in\{0,1\}\}\). Horizontal edges join \((i,a)\) to \((i+1,a)\) when \(0\le i<n-1\), while crossed-seam edges join \((n-1,a)\) to \((0,1-a)\); each rung joins \((i,0)\) to \((i,1)\). This is the simple cubic Möbius ladder, including \(M_6\cong K_{3,3}\). Every bit changes synchronously to the strict majority of its three neighbouring bits; no self-loops or random updates are used. Configurations and two-cycles are labelled, without quotienting by graph automorphisms. Only recurrence counts are asserted, not transient-depth or attraction-basin counts.

## Proof
First, a fixed configuration cannot disagree across a rung. If \(x_{i,0}\ne x_{i,1}\), each endpoint already has an opposing rung neighbour, and so both horizontal neighbours must match its own bit for it to retain its majority. The adjacent rungs must consequently have the same oriented disagreement; this propagates around the strip and contradicts the crossed seam. Hence fixed configurations have \(x_{i,0}=x_{i,1}=b_i\) for all \(i\). A vertex can then change only when both cyclic horizontal neighbours are opposite to \(b_i\). Thus fixed configurations correspond exactly to cyclic binary words of length \(n\) with no isolated symbols. The ordinary adjacent-pair transfer of these words has characteristic polynomial
\[
(t^2-t-1)(t^2-t+1).
\]
Its trace at power \(n\) is \(L_n+2\cos(n\pi/3)\), proving the fixed-state formula.

For recurrent states, the finite-graph period-two theorem for synchronous majority dynamics implies that recurrence is exactly \(F_n^2(x)=x\). Put \(y=F_n(x)\). At each column use a four-bit symbol \(v=(v_{0,0},v_{0,1},v_{1,0},v_{1,1})\), with temporal index zero for \(x\) and one for \(y\). If \(u,v,w\) are three consecutive column symbols, the two simultaneous transition equations at each row \(a\in\{0,1\}\) are
\[
v_{1,a}=\operatorname{maj}(u_{0,a},w_{0,a},v_{0,1-a}),\qquad
v_{0,a}=\operatorname{maj}(u_{1,a},w_{1,a},v_{1,1-a}).
\]
Define the zero-one matrix \(T\) on the \(256\) states \((u,v)\in(\{0,1\}^4)^2\) by \(T_{(u,v),(v,w)}=1\) exactly when all four equations hold (and zero otherwise). Let \(S\) interchange the two spatial rows in each four-bit column, acting also on pairs. The crossed seam says that a length-\(n\) admissible path goes from \((u,v)\) to \(S(u,v)\), not necessarily back to itself. Therefore
\[
P_n=\operatorname{tr}(T^n S).
\]
This is a bijective encoding: for any \(x\), the companion \(y=F_n(x)\) is unique, and the second equation enforces \(F_n(y)=x\).

The directed graph of \(T\) has precisely six strongly connected components containing a directed cycle, of respective sizes \(16,8,8,2,1,1\). The row swap \(S\) fixes the components of sizes \(16\) and \(2\), exchanges the two size-eight components, and exchanges the two singletons. Since \(T\) commutes with \(S\), a path from a state \(p\) to \(S(p)\) can exist only if \(p\) and \(S(p)\) lie in the same strongly connected component: applying \(S\) to the path gives a path back. Hence only the two invariant components contribute to the twisted trace.

The size-two component has \(S=I\) and characteristic polynomial \(t^2-1\). On the size-sixteen component, the invariant and anti-invariant subspaces of \(S\) have dimensions ten and six. Their respective characteristic polynomials for \(T\) are
\[
\begin{aligned}
\chi_+(t)&=(t-1)(t+1)(t^2-3t+1)(t^2+t+1)
(t^4-t^3+2t^2+t+1),\\
\chi_-(t)&=(t-1)(t+1)(t^4+t^3+2t^2-t+1).
\end{aligned}
\]
These are exact finite rational-matrix calculations from the displayed transition rule, and are reproduced by the accompanying verifier; no numerical eigenvalue inference is involved. The two quartics satisfy \(q_-(t)=q_+(-t)\). Moreover, the roots of \(q_+\) are the products of each root of \(t^2-t-1\) with each root of \(t^2-t+1\). Combining the signed traces therefore yields, for all \(n\ge1\),
\[
P_n=L_{2n}+2\cos(2\pi n/3)+(1-(-1)^n)2L_n\cos(n\pi/3)+1+(-1)^n.
\]
For odd \(n\), use \(L_n^2=L_{2n}-2\) and \(4\cos^2(n\pi/3)=2+2\cos(2n\pi/3)\) to obtain \(P_n=Q_n^2\). For even \(n\), use \(L_n^2=L_{2n}+2\); the remaining term is \(2\cos(2\pi n/3)\), equal to \(2\) or \(-1\) according to \(n\equiv0\) or \(2,4\pmod6\). This proves the recurrent-state formulas. Since every recurrent orbit has length one or two, dividing \(P_n-Q_n\) by two counts primitive two-cycles.

## Verification
Execute `python mobius_majority_verify.py` with Python 3, NumPy, NetworkX, and SymPy installed. It reconstructs every allowed transition from the explicit local rule, identifies the cyclic strongly connected components and row-swap action, computes the displayed characteristic polynomials over the integers, and compares twisted traces with both formulas. An independently implemented vertexwise majority update then exhaustively tests every one of the \(2^{2n}\) configurations for each \(3\le n\le11\), including all \(4{,}194{,}304\) configurations at \(n=11\). The accompanying log contains the observed counts. The all-size proof is the transfer construction and exact finite algebra; the finite exhaustive tests are corroboration, not a substitute for it.

## Relationship to prior work
The eventual-period-at-most-two theorem is classical (Goles and Olivos, 1980), and is used here without a novelty claim. The cyclic no-isolated-symbol count appearing in the fixed-point formula is already proved by Agur, Fraenkel and Klein (1988) for a different one-dimensional local majority rule, and its Lucas expression is not claimed as new. The new result is the complete Möbius-ladder recurrent-state and two-cycle census with a twisted-boundary parity-square law. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486, first posted 2014-05-11) study convergence, unanimity and disagreement for majority dynamics on general and random graphs; their stated results do not give these Möbius-ladder recurrent-state counts. Turau (arXiv:2202.01580) studies fixed points and two-cycles principally for trees, a graph class distinct from these cubic cyclic ladders. Closely related exact enumerations for untwisted circular prisms do not imply the crossed-seam result: for four rungs the untwisted prism has \(64\) recurrent states, while the Möbius ladder has \(48\). The essential new calculation is the swap-twisted trace and its exact parity-sensitive factorization.

## Limitations
The result concerns only synchronous open-neighbourhood majority on the specified labelled Möbius ladders, not arbitrary cubic graphs, other update schedules, minority rules or basin measures. The paper of McSorley (1998) counts various combinatorial structures on Möbius ladders; an accessible abstract did not determine whether any of its results imply this precise majority-dynamics census. Its full text was not available in this review, leaving a residual literature-overlap risk. Other unindexed equivalences are also possible. This is a mathematical proof with reproducible finite algebra, not an independently audited or formally certified result.

## References
1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first posted 2014-05-11), https://arxiv.org/abs/1405.2486.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189.
3. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, https://doi.org/10.1016/0012-365X(88)90005-2.
4. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580, https://arxiv.org/abs/2202.01580.
5. J. P. McSorley, *Counting structures in the Möbius ladder*, Discrete Mathematics 184 (1998), 137–164, https://doi.org/10.1016/S0012-365X(97)00086-1.
