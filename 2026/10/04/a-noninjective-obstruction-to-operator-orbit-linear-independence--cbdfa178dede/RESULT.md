# A noninjective obstruction to operator-orbit linear independence for g-fusion frames
## Finding
Proposition 4.1 of Jahedi--Javadi--Mehdipour, arXiv:2305.08182v1, is false without an injectivity hypothesis on the representing operator. Its perturbative consequence, Theorem 4.3(ii), is also false as stated. The failure occurs even for a tight \(g\)-fusion frame represented by a bounded operator.

More precisely, there is a separable infinite-dimensional Hilbert space \(H\), closed subspaces \((M_k)_{k\in\mathbb Z}\), bounded operators \((\Theta_k)_{k\in\mathbb Z}\), and a bounded noninjective operator \(T\) such that
\[
\Theta_{k+1}=T\Theta_k\qquad(k\in\mathbb Z),
\]
\[
\sum_{k\in\mathbb Z}\|\Theta_k f\|^2=\frac53\|f\|^2\qquad(f\in H),
\]
the linear span of \(\{\Theta_k:k\in\mathbb Z\}\) is infinite-dimensional and the set itself is infinite, but
\[
\Theta_2=\frac12\Theta_1.
\]
Thus the operator family is linearly dependent despite satisfying the hypotheses of Proposition 4.1. Taking \(\widehat\Theta_k=\Theta_k\) and \(\alpha=\beta=0\) also satisfies the perturbation hypothesis of Theorem 4.3 and contradicts its conclusion (ii).

There is a direct repair of Proposition 4.1: if \(T\) is injective on \(\operatorname{span}\{M_k:k\in\mathbb Z\}\), then an operator orbit \((\Theta_k)_{k\in\mathbb Z}\) with infinite-dimensional operator span is linearly independent.
## Assumptions and scope
Use the definition in arXiv:2305.08182v1: each \(\Theta_k\in\mathcal L(H)\) has range in \(M_k\), a \(g\)-fusion frame satisfies two-sided bounds for \(\sum_k\|\Theta_k f\|^2\), and representation via \(T\) means \(\Theta_{k+1}=T\Theta_k\) for every \(k\in\mathbb Z\).

Let \(H\) be a separable infinite-dimensional Hilbert space with an orthogonal decomposition
\[
H=\left(\bigoplus_{n=0}^{\infty}E_n\right)\oplus F,
\]
where every \(E_n\) and \(F\) is unitarily isomorphic to \(H\). Choose unitaries \(U_n:H\to E_n\) and \(U_+:H\to F\). Put
\[
M_{-n}=E_n\quad(n\ge0),\qquad M_k=F\quad(k\ge1),
\]
and
\[
\Theta_{-n}=2^{-n}U_n\quad(n\ge0),\qquad
\Theta_k=2^{-k}U_+\quad(k\ge1).
\]
Define \(T\in\mathcal L(H)\) blockwise by
\[
T(U_nx)=2U_{n-1}x\quad(n\ge1),\qquad
T(U_0x)=\frac12U_+x,\qquad
T(U_+x)=\frac12U_+x.
\]
## Proof
The block definition gives a bounded operator. On \(\bigoplus_{n\ge1}E_n\) it has norm \(2\). On \(E_0\oplus F\),
\[
\left\|T(U_0x+U_+y)\right\|=\frac12\|x+y\|
\le\frac1{\sqrt2}\left(\|x\|^2+\|y\|^2\right)^{1/2},
\]
so \(\|T\|=2\). It is not injective because
\[
T(U_0x-U_+x)=0
\]
for every nonzero \(x\in H\).

The orbit relation is exact. For \(n\ge1\),
\[
T\Theta_{-n}=2^{-n}(2U_{n-1})=2^{-(n-1)}U_{n-1}=\Theta_{-n+1}.
\]
At the transition,
\[
T\Theta_0=\frac12U_+=\Theta_1,
\]
and for \(k\ge1\),
\[
T\Theta_k=2^{-k}\frac12U_+=\Theta_{k+1}.
\]

The family is a tight \(g\)-fusion frame, since each \(U_n\) and \(U_+\) is an isometry and
\[
\sum_{k\in\mathbb Z}\|\Theta_k f\|^2
=\left(\sum_{n=0}^{\infty}4^{-n}+\sum_{k=1}^{\infty}4^{-k}\right)\|f\|^2
=\left(\frac43+\frac13\right)\|f\|^2
=\frac53\|f\|^2.
\]
The negative-index operators are linearly independent: in any finite relation among \(U_0,U_1,\ldots\), orthogonal projection onto \(E_n\) isolates the coefficient of \(U_n\). Hence \(\operatorname{span}\{\Theta_k:k\in\mathbb Z\}\) is infinite-dimensional. Nevertheless,
\[
\Theta_2=\frac14U_+=\frac12\Theta_1,
\]
so the full family is linearly dependent. This disproves Proposition 4.1. For Theorem 4.3(ii), set \(\widehat\Theta_k=\Theta_k\). The left side of its perturbation inequality is identically zero with \(\alpha=\beta=0\), while the hypotheses of infinite operator span and an infinite set are satisfied; its claimed linear independence therefore fails as well.

For the repaired proposition, assume instead that \(T\) is injective on \(\operatorname{span}\{M_k:k\in\mathbb Z\}\). Suppose a nontrivial finite relation has extreme nonzero indices \(a<b\):
\[
\sum_{j=a}^{b}c_j\Theta_j=0,
\qquad c_a c_b\ne0.
\]
Let \(V=\operatorname{span}\{\Theta_a,\ldots,\Theta_b\}\). Solving for \(\Theta_b\) and applying \(T\) shows \(T(V)\subseteq V\), hence every \(\Theta_j\) with \(j>b\) lies in \(V\). Solving instead for \(\Theta_a\), write
\[
\Theta_a=\sum_{j=a+1}^{b}d_j\Theta_j.
\]
Then
\[
A:=\Theta_{a-1}-\sum_{j=a+1}^{b}d_j\Theta_{j-1}
\]
has range in \(\operatorname{span}\{M_k\}\) and satisfies \(TA=0\). Injectivity of \(T\) gives \(A=0\), so \(\Theta_{a-1}\in V\). Repeating the same argument inductively gives \(\Theta_j\in V\) for every \(j<a\). Thus the entire operator span equals the finite-dimensional space \(V\), contradicting the assumption of infinite-dimensional span. Hence the family is linearly independent.
## Verification
The counterexample is verified by exact operator identities and geometric-series sums; no finite computation is used to infer an infinite statement. The critical checks are: every range lies in its prescribed \(M_k\); \(T\) is bounded; \(T\Theta_k=\Theta_{k+1}\) for every integer \(k\); the frame energy is exactly \(5\|f\|^2/3\); the negative orbit has infinite-dimensional linear span; and \(\Theta_2=\Theta_1/2\).

The repair uses only injectivity of \(T\) on the algebraic span of the subspaces, not surjectivity or a bounded inverse. The step missing from the published preprint proof is precisely the unlicensed use of negative powers of \(T\): its proof invokes \(T^{-i}\) although Proposition 4.1 assumes no injectivity or invertibility.
## Relationship to prior work
The source explicitly states Proposition 4.1 and says it “plays an important role in the sequel”; its proof passes from forward iterates to \(T^{-i}\) without an invertibility hypothesis. Theorem 4.3(ii) then invokes Proposition 4.1 to conclude linear independence. The preprint first appeared on 14 May 2023 and lists MSC 42C15.

Christensen and Hasannasab, arXiv:1704.08918, study ordinary frame orbits and explicitly distinguish bounded representations from representations extending to bounded bijective operators. That literature does not imply Proposition 4.1 under mere forward representability and does not contain the tight \(g\)-fusion counterexample above. The journal paper with DOI 10.1007/s11868-023-00546-2 describes itself as a reedited copy of the preprint; the accessible preview was used for bibliographic and classification comparison, but the present claim is deliberately scoped to arXiv:2305.08182v1 because the full journal theorem text was not independently inspected.
## Limitations
This finding does not assert that every noninjective representing operator produces dependence, nor that injectivity is necessary for linear independence in each individual orbit. It proves that noninjectivity invalidates the universal statement as written and that injectivity is a sufficient repair for Proposition 4.1. It does not re-audit unrelated results in the source. The possibility of an unindexed correction or a theorem-level change in the inaccessible portions of the reedited journal version remains a literature risk.
## References
1. S. Jahedi, F. Javadi, M. J. Mehdipour, “On \(g\)-Fusion Frames Representations via Linear Operators,” arXiv:2305.08182v1, 14 May 2023. Proposition 4.1 and Theorem 4.3.
2. O. Christensen, M. Hasannasab, “Operator representations of frames: boundedness, duality, and stability,” arXiv:1704.08918, 2017; Integral Equations and Operator Theory 88 (2017), 483–499.
3. S. Jahedi, F. Javadi, M. J. Mehdipour, “On \(g\)-frame representations via linear operators,” Journal of Pseudo-Differential Operators and Applications 14 (2023), article 52, DOI:10.1007/s11868-023-00546-2.
