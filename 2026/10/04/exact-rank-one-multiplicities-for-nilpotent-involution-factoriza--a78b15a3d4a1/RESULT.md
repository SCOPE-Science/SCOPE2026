# Exact rank-one multiplicities for nilpotent–involution factorizations in \(M_3(\mathbb F_q)\)
## Finding
Let \(q\) be a prime power and let \(A\in M_3(\mathbb F_q)\) have rank one. Define \(\nu(A)\) to be the number of ordered factorizations \(A=NU\) with \(N\) nilpotent and \(U^2=I_3\). Then \(\nu(A)\) depends only on the characteristic and on whether \(\operatorname{tr}A\) vanishes. If \(q\) is odd, then \(\nu(A)=4q^3+2q^2+2\) when \(\operatorname{tr}A=0\), and \(\nu(A)=2q(q^2-1)\) when \(\operatorname{tr}A\ne0\). If \(q\) is even, then \(\nu(A)=2q^3-q\) when \(\operatorname{tr}A=0\), and \(\nu(A)=q(q^2-1)\) when \(\operatorname{tr}A\ne0\). In every such factorization, \(N\) has rank one and satisfies \(N^2=0\).

Equivalently, the complete rank-one stratum of \(M_3(\mathbb F_q)\) has exactly two factorization-multiplicity values, separated by the similarity-invariant condition \(\operatorname{tr}A=0\). For \(q=2,3,4\), the two counts (trace zero, nonzero trace) are respectively \((14,6)\), \((128,48)\), and \((124,60)\).

## Assumptions and scope
The field is the finite field \(\mathbb F_q\), with \(q\) any prime power. An involution means a matrix \(U\in M_3(\mathbb F_q)\) satisfying \(U^2=I_3\); such a matrix is automatically invertible. A factorization is ordered: different involutions count separately, and once \(U\) is fixed the nilpotent factor is forced to be \(N=AU\). The matrix \(A\) is assumed to have rank exactly one.

The claim does not count nilpotent–idempotent factorizations, does not treat ranks zero or two, and does not assert a formula in dimensions other than three.

## Proof
Write a rank-one matrix as \(A=u\varphi\), where \(u\in\mathbb F_q^3\setminus\{0\}\) and \(\varphi\in(\mathbb F_q^3)^*\setminus\{0\}\). For any matrix \(U\),
\[
AU=u(\varphi U),\qquad (AU)^2=\operatorname{tr}(AU)\,AU.
\]
Thus a nonzero rank-one matrix is nilpotent exactly when its trace is zero. Since an involution is invertible, \(AU\) always has rank one. Therefore \(A=NU\) with \(N\) nilpotent and \(U^2=I_3\) is equivalent to choosing an involution \(U\) such that \(\operatorname{tr}(AU)=0\), after which \(N=AU\) is unique and square-zero.

Similarity preserves the number of such involutions. If \(\operatorname{tr}A=0\), every nonzero rank-one \(A\) is similar to \(E_{12}\); take \(u=e_1\) and \(\varphi=e_2^*\). If \(\operatorname{tr}A\ne0\), scaling by the nonzero trace does not change the condition \(\operatorname{tr}(AU)=0\), so one may take \(A=E_{11}\), with \(u=e_1\) and \(\varphi=e_1^*\).

Assume first that \(q\) is odd. Every involution has the unique form \(U=I_3-2P\) with \(P^2=P\). Hence the condition is
\[
\varphi(Pu)=\frac{\varphi(u)}{2}.
\]
For rank-one idempotents write \(P=x\psi\) with \(\psi(x)=1\), modulo the equivalence \((x,\psi)\sim(cx,c^{-1}\psi)\) for \(c\ne0\).

If \(\varphi(u)=0\), the rank-zero and rank-three idempotents both qualify. For rank one, in the coordinates above the condition is \(x_2\psi_1=0\). Counting representatives \((x,\psi)\) with \(\psi(x)=1\): the condition \(x_2=0\) gives \((q^2-1)q^2\) pairs, the condition \(\psi_1=0\) gives the same number, and their intersection has \(q^2(q-1)\) pairs. Dividing by \(q-1\) gives \(q^2(2q+1)\) rank-one idempotents. The involution \(P\mapsto I_3-P\) pairs these with the same number of rank-two idempotents. Therefore
\[
\nu(A)=2+2q^2(2q+1)=4q^3+2q^2+2.
\]

If \(\varphi(u)=1\), ranks zero and three do not qualify. For rank one the condition \(x_1\psi_1=1/2\) lets us scale uniquely to \(x_1=1\), \(\psi_1=1/2\). Writing \(x=(1,a,b)\) and \(\psi=(1/2,c,d)\), the idempotent condition becomes \(ac+bd=1/2\). There are \(q^2-1\) nonzero pairs \((a,b)\), and for each there are \(q\) choices of \((c,d)\), giving \(q(q^2-1)\) rank-one idempotents. Rank two contributes the same number by \(P\mapsto I_3-P\). Hence
\[
\nu(A)=2q(q^2-1).
\]

Now assume that \(q\) is even. Every involution has the unique form \(U=I_3+S\) with \(S^2=0\). In dimension three such an \(S\) has rank at most one. A nonzero one can be written \(S=x\psi\) with \(\psi(x)=0\), again modulo \((x,\psi)\sim(cx,c^{-1}\psi)\).

If \(\varphi(u)=0\), the zero matrix \(S=0\) qualifies. For nonzero rank-one \(S\), the condition is again \(x_2\psi_1=0\). The sets \(x_2=0\) and \(\psi_1=0\) each contribute \((q^2-1)^2\) representative pairs. Their intersection has \((q-1)^2(2q+1)\) pairs, because after writing \(x=(x_1,0,x_3)\) and \(\psi=(0,\psi_2,\psi_3)\), the equation \(\psi(x)=0\) is \(x_3\psi_3=0\). After inclusion-exclusion and division by \(q-1\), the number of nonzero qualifying \(S\) is \((q-1)(2q^2+2q+1)\). Adding \(S=0\) gives
\[
\nu(A)=1+(q-1)(2q^2+2q+1)=2q^3-q.
\]

If \(\varphi(u)=1\), the condition is \(x_1\psi_1=1\). Scale uniquely to \(x_1=\psi_1=1\). With \(x=(1,a,b)\) and \(\psi=(1,c,d)\), the square-zero condition becomes \(ac+bd=1\). This has \(q(q^2-1)\) solutions, so
\[
\nu(A)=q(q^2-1).
\]
This proves all four formulas.

## Verification
The proof is field-uniform and does not rely on computation. As a separate finite replay, `verify_factorizations.py` exhaustively enumerates all \(3\times3\) matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), retains exactly those satisfying \(U^2=I_3\), and counts the conditions \(U_{21}=0\) and \(U_{11}=0\), corresponding to \(A=E_{12}\) and \(A=E_{11}\). It returns \((14,6)\), \((128,48)\), and \((124,60)\), exactly matching the formulas. The replay output is stored in `verification_output.txt`.

## Relationship to prior work
Mabilat, arXiv:2608.17569v1, characterizes when a matrix over an arbitrary field can be written as a product of a nilpotent matrix and an involution. In particular, the paper proves the existence criterion in terms of invariant factors and remarks explicitly that such factorizations are generally not unique. It does not give a factorization-count formula, a rank-one finite-field multiplicity distribution, or the four characteristic-dependent formulas above.

The classical finite-field literature counts solutions of the unconstrained matrix equation \(U^2=I\), but an unconstrained involution count does not determine the incidence condition \(\operatorname{tr}(AU)=0\) for a fixed rank-one \(A\). The proof above resolves that incidence count directly.

## Limitations
Only rank-one matrices in dimension three are covered. No formula is claimed for rank-two matrices, for nilpotent–idempotent factorization multiplicities, or for higher dimension. The literature search found no statement equivalent to the exact multiplicity formulas, but an older unindexed source using different terminology remains a residual originality risk. The finite replays cover \(q=2,3,4\) only; they check the general proof but do not replace it.

## References
1. F. Mabilat, “Decomposition of a square matrix into a product of a nilpotent matrix and an involutive or idempotent matrix,” arXiv:2608.17569v1, 18 August 2026.
2. J. H. Hodges, “The Matrix Equation \(X^2-I=0\) Over a Finite Field,” American Mathematical Monthly 65 (1958), 518–520, doi:10.2307/2308579.
