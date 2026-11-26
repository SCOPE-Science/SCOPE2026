# Nonvanishing and exponential rational homology in circular-ladder two-independence complexes

## Finding
Let \(X_n=\operatorname{Ind}_2(C_n\square K_2)\) for every integer \(n\ge3\). Write \(E_n=\sum_{S\in X_n}(-1)^{|S|}=-\widetilde\chi(X_n)\). Then \(E_4=-3\), and \(E_n>0\) for every other \(n\ge3\). In particular every \(X_n\) is noncontractible and has nonzero reduced rational homology. More quantitatively,
\[
\sum_{j\ge0}\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q)
\ge |E_n|>\frac{(1.386)^n}{3}\qquad(n\ge20).
\]
The sign conclusion and cutoff come from the signed specialization of the previously computed dissociation polynomial. The signed sums satisfy \(E_n=\alpha^n+O(1.31^n)\), where \(\alpha\in(1.386,1.387)\) is the larger real root of \(t^4-t^2-2t+1\).

## Assumptions and scope
The graphs are simple and undirected. The circular ladder has consecutive cyclic edges in each layer and one rung at each index of \(\mathbb Z/n\mathbb Z\). A face is a vertex subset whose induced components have size at most two, equivalently whose induced graph has maximum degree at most one. These are exactly the dissociation sets, including the empty set. Homology is reduced simplicial homology over \(\mathbb Q\).

## Proof
Let \(P_n(z)=\sum_{S\in X_n} z^{|S|}\). The earlier complete dissociation-polynomial formula [1, Finding and Proof §1] gives
\[
\sum_{n\ge3}P_n(z)u^n=-u\partial_u\log Q(u,z)-u-(1+2z)^2u^2,
\]
where
\[
Q(u,z)=(1+zu+z^2u^2)(1-(z+1)u-(2z^2+z)u^2+(z^3-z^2)u^3+z^4u^4).
\]
At \(z=-1\), write \(Q(u,-1)=\prod_{k=1}^6(1-\lambda_k u)\). The logarithmic derivative gives \(E_n=\sum_k\lambda_k^n\) for \(n\ge3\), where the \(\lambda_k\) are the roots of
\[
(t^2-t+1)(t^4-t^2-2t+1)=t^6-t^5-t^3+2t^2-3t+1.
\]
In particular, as a consequence of the prior formula,
\[
 E_{n+6}=E_{n+5}+E_{n+3}-2E_{n+2}+3E_{n+1}-E_n\qquad(n\ge3).
\]
The first six terms from the logarithmic derivative are \((4,-3,11,10,1,29)\). Iterating this integer recurrence gives the full list for \(3\le n\le19\):
\[
4,-3,11,10,1,29,4,21,67,6,105,113,44,317,171,298,761.
\]

For a uniform sign certificate beyond this finite list, put \(q(t)=t^4-t^2-2t+1\). Its derivative is \(2(t-1)(2t^2+2t+1)\), with a positive quadratic factor on the real line. Exact signs at \(0.425,0.430,1.386,1.387\) are respectively \(+,-,-,+\). Hence the only real roots are \(\beta\in(0.425,0.430)\) and \(\alpha\in(1.386,1.387)\). Its conjugate pair has modulus \(\rho=(\alpha\beta)^{-1/2}<1.31\), by the constant term and \(1/(1.386\cdot0.425)<1.31^2\). The two roots of \(t^2-t+1\) have unit modulus. The power-sum formula gives the stated growth law for \(E_n\) and also the lower bound
\[
 E_n>\alpha^n\left[1-(0.430/1.386)^n-2(1.31/1.386)^n-2/(1.386)^n\right].
\]
At \(n=20\), the sum of the three subtracted terms is less than \(\tfrac23\) by the exact rational comparison
\[
 3\big(430^{20}+2\,1310^{20}+2\,1000^{20}\big)<2\,1386^{20}.
\]
Each subtracted term decreases as \(n\) increases. It follows that \(E_n>\alpha^n/3>(1.386)^n/3\) for every \(n\ge20\). Together with the finite list this proves the sign assertion at every length. Finally Euler–Poincaré identifies \(-E_n\) with the alternating sum of reduced rational Betti numbers; taking absolute values gives the claimed lower bound. A nonzero reduced Euler characteristic precludes contractibility.

## Verification and limitations
The proof uses a supplied polynomial identity from prior work; the finite list alone does not certify the infinite sign claim. The root brackets and the inequality at exponent twenty are rational checks. The companion verifier `verify_prism.py` (Python and SymPy; see `requirements.txt`) computes the signed list and verifies these exact comparisons. Its checks of the full face polynomial and transfer determinant verify the input identity, not a novelty claim for that identity. The Betti lower bound does not determine the separate Betti numbers, integral torsion or homotopy type.

## Relationship to prior work
The complete dissociation polynomial and its transfer determinant for the same family are already in [1]. The signed recurrence and growth rate follow from specializing that identity. The contribution here is the all-length sign classification and resulting uniform rational-homology nonvanishing and explicit lower bound, not a new full face enumerator. Higher-independence results for cycles [2] and chordal graphs [3] do not cover these nonchordal prisms. The later catalogue entry [4] has substantially overlapping signed and homological results; no claim of independent provenance or absolute priority is made.

## References
1. [*Complete dissociation polynomial and Lucas maximum-set law for cycle prisms*](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-complete-dissociation-polynomial-and-lucas-maximum-set-law-for-c--862aa31d85c9/RESULT.md), Resultary record 862aa31d85c9, 13 October 2026.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448.
3. F. M. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863.
4. [*Exponential homology growth in circular-ladder two-independence complexes*](https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-exponential-homology-growth-in-circular-ladder-two-independence--fb91d040f763/RESULT.md), Resultary record fb91d040f763, 1 November 2026.
