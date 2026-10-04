# Replica-nullity proof of the fully symmetric Gaussian multi-entropy asymptotic
## Finding
For the real fully symmetric \(N\)-mode pure Gaussian states considered by Camargo and Nishida, take a nonempty tripartition with \(N_A,N_B,N_C\ge 1\) and \(N_A+N_B+N_C=N\). For every integer replica order \(n\ge 3\), as the inverse local purity \(a\to\infty\),
\[
\mathrm{GM}^{(3)}_n(A:B:C)=\frac{2-n}{2n}\log a+C_{n;N_A,N_B,N_C}+O(a^{-2}).
\]
Thus the GHZ-like logarithmic coefficient conjectured in arXiv:2609.30754v1 is valid for every integer \(n\ge3\), every \(N\ge3\), and every nonempty tripartition. The source already proves the separate \(n=2\) identity \(\mathrm{GM}^{(3)}_2=0\) for arbitrary pure bosonic Gaussian states.

The constant is explicit. Define \(c_N=(N-1)/N^2\). For the tripartite replica space let \(r=n^2\), let \(P_A\) and \(P_B\) be the cyclic shifts in the two directions of the \(n\times n\) replica grid, let \(P_C=I_r\), and put
\[
v=(\sqrt{N_A},\sqrt{N_B},\sqrt{N_C})^{\mathsf T},\qquad Q=\operatorname{diag}(P_A,P_B,P_C),
\]
\[
K_3=(vv^{\mathsf T})\otimes I_r+Q^{\mathsf T}\bigl((vv^{\mathsf T})\otimes I_r\bigr)Q.
\]
Let \(\Delta_3\) be the product of the nonzero eigenvalues of \(I-K_3/(2N)\). For a bipartition \(X:(ABC\setminus X)\), define \(K_X\) by the same construction with \(v_X=(\sqrt{N_X},\sqrt{N-N_X})^{\mathsf T}\), an \(n\)-cycle on the first replica block and identity on the second, and let \(\Delta_X\) be the product of the nonzero eigenvalues of \(I-K_X/(2N)\). Then
\[
C_{n;N_A,N_B,N_C}=\frac{n-2}{4n}\log c_N+\frac{\log\Delta_3}{2n(n-1)}-\frac{1}{4(n-1)}\sum_{X=A,B,C}\log\Delta_X.
\]
All \(\Delta\)'s are strictly positive.

## Assumptions and scope
The state is the real fully symmetric pure Gaussian family whose wavefunction matrix is
\[
W=\alpha I_N+eJ_N,\qquad \alpha=a-e,
\]
with the off-diagonal parameter \(e=e^{-}(a,N)\) of Eq. (30) in arXiv:2609.30754v1. The claim concerns fixed finite \(N\), fixed positive block sizes, fixed integer \(n\ge3\), and the limit \(a\to\infty\). Logarithms use one consistent base; changing base rescales all entropies and constants together.

No statement is made about analytic continuation in \(n\), noninteger replica order, mixed Gaussian states, or arbitrary nonsymmetric Gaussian states. The argument uses only the real member of the source family for which the position-space Gaussian kernel is positive definite.

## Proof
First localize the permutation-symmetric degrees of freedom. Within each of \(A,B,C\), make an orthogonal change of coordinates whose first coordinate is the normalized uniform mode. Since
\[
W=\alpha I_N+e\mathbf 1\mathbf 1^{\mathsf T},
\]
all relative coordinates inside a party decouple as one-mode pure Gaussians with scalar kernel \(\alpha\). The only correlated coordinates are the three block-uniform modes. Their kernel is
\[
W_3=\alpha I_3+evv^{\mathsf T},\qquad v=(\sqrt{N_A},\sqrt{N_B},\sqrt{N_C})^{\mathsf T}.
\]
This is the concrete wavefunction form of the unitary localization of block correlations known for multisymmetric Gaussian states. The local pure factors contribute exactly one to every replica contraction, so they may be omitted.

For \(q=3\), there are \(r=n^2\) replicas. With the replica variables grouped by party, the second copy of the Gaussian kernel is related to the first by
\[
Q=\operatorname{diag}(P_A,P_B,I_r),
\]
where \(P_A\) and \(P_B\) are the row and column cyclic shifts of the \(n\times n\) replica grid. The Gaussian integral therefore has quadratic matrix
\[
M_3=2\alpha I_{3r}+eK_3,
\]
where
\[
K_3=(vv^{\mathsf T})\otimes I_r+Q^{\mathsf T}\bigl((vv^{\mathsf T})\otimes I_r\bigr)Q.
\]
Since \(\det W_3=\alpha^2(\alpha+Ne)\), direct cancellation of the Gaussian normalization gives the exact replica partition function
\[
Z_n^{(3)}=\frac{\lambda^{r/2}}{\sqrt{\det(I+tK_3)}},\qquad
\lambda=\frac{\alpha+Ne}{\alpha},\qquad t=\frac{e}{2\alpha}=\frac{\lambda-1}{2N}.
\]

The matrix \((vv^{\mathsf T})\otimes I_r\) is positive semidefinite, has norm \(N\), and has top eigenspace
\[
\mathcal S=\{v\otimes y:y\in\mathbb R^r\}.
\]
Its conjugate by \(Q\) has the same norm. Consequently \(0\le K_3\le2NI\). Equality \(K_3x=2Nx\) holds exactly when \(x\) lies in the top eigenspaces of both summands. Writing \(x=v\otimes y\), this requires
\[
y=P_A^{\mathsf T}y=P_B^{\mathsf T}y.
\]
The row and column shifts act transitively on the \(n\times n\) grid, so their common fixed space consists only of constant vectors. Therefore \(2N\) is a simple eigenvalue of \(K_3\), and all other eigenvalues are strictly below \(2N\).

It follows that, as \(\lambda\downarrow0\),
\[
\det(I+tK_3)=\lambda\Delta_3\bigl(1+O(\lambda)\bigr),
\]
with \(\Delta_3>0\). The source expression for \(e^-(a,N)\) has the elementary large-\(a\) expansion
\[
e=-\frac{a}{N-1}+\frac{1}{N(N-1)a}+O(a^{-3}),
\]
so
\[
\lambda=\frac{N-1}{N^2a^2}+O(a^{-4})=c_Na^{-2}+O(a^{-4}).
\]
Hence
\[
\log Z_n^{(3)}=-(n^2-1)\log a+\frac{n^2-1}{2}\log c_N-\frac12\log\Delta_3+O(a^{-2}),
\]
and the definition \(S_n^{(3)}=[n(1-n)]^{-1}\log Z_n^{(3)}\) yields
\[
S_n^{(3)}=\frac{n+1}{n}\log a-\frac{n+1}{2n}\log c_N+\frac{\log\Delta_3}{2n(n-1)}+O(a^{-2}).
\]

The same argument for a bipartition has \(r=n\), one cyclic shift and one identity shift. Its common fixed space is again one-dimensional, so
\[
S_n^{(2)}(X:ABC\setminus X)=\log a-\frac12\log c_N+\frac{\log\Delta_X}{2(n-1)}+O(a^{-2}).
\]
Substituting the three bipartite expansions into
\[
\mathrm{GM}^{(3)}_n=S_n^{(3)}-\frac12\bigl(S_n^{(2)}(A:BC)+S_n^{(2)}(B:CA)+S_n^{(2)}(C:AB)\bigr)
\]
gives the stated logarithmic coefficient and the displayed constant.

## Verification
The proof is analytic. The accompanying verifier independently reconstructs the Gaussian replica matrices from the permutation contractions, checks the exact determinant formula against two closed-form entries of Table 1 of arXiv:2609.30754v1, checks the \(a^2\lambda\to(N-1)/N^2\) scaling for several \(N\), and checks that the row/column shift action has a single orbit on the replica grid. These finite checks corroborate the algebra but are not used to infer the universal theorem.

As a further symbolic consistency check, for \(n=3\) and \((N_A,N_B,N_C)=(m,1,1)\), the determinant constant above reduces numerically to the source's explicit constant in Eq. (38),
\[
\frac1{12}\log\!\left(\frac{2\bigl(4m(m+1)+1\bigr)}{3m(m+1)}\right),
\]
for tested positive integers \(m\); the universal proof does not depend on this sampling.

## Relationship to prior work
Camargo and Nishida derive the general Gaussian replica-determinant formalism, tabulate exact values for small \(N\) at \(n=3,4\), and explicitly conjecture
\[
\mathrm{GM}^{(3)}_n\sim\frac{2-n}{2n}\log a
\]
for arbitrary \(n\) and \(N\). They also state that closed forms become difficult for \(n\ge4\). The present result proves that conjecture for every integer \(n\ge3\), strengthens it to an \(O(a^{-2})\) expansion, and supplies an explicit finite-dimensional determinant formula for the constant term.

Adesso and Illuminati previously proved that correlations among blocks of multisymmetric Gaussian states can be unitarily localized to one mode per block. That structural theorem explains the three-collective-mode reduction, but it predates multi-entropy and studies residual contangle rather than the replica invariant here; it does not imply the one-soft-mode replica determinant or the coefficient above. Related exact multi-entropy results for Lifshitz ground states concern a different Gaussian field-theory family and do not cover this finite fully symmetric state family.

## Limitations
The theorem is asymptotic in large squeezing and fixed finite \(N,n\); it does not provide a simple closed form for the finite-\(a\) determinant at arbitrary \(n\). It does not address noninteger analytic continuation in \(n\), and therefore does not by itself solve the \(n\to1\) continuation problem. It is specific to the real fully symmetric pure Gaussian family and nonempty tripartitions. No claim is made for general pure Gaussian states at \(n\ge3\).

## References
1. H. A. Camargo and M. Nishida, “Genuine Multi-Entropy of Fully Symmetric Gaussian States,” arXiv:2609.30754v1 (first public 25 September 2026), especially Eqs. (30), (35), (37), (38) and Table 1.
2. G. Adesso and F. Illuminati, “Genuine multipartite entanglement of symmetric Gaussian states: Strong monogamy, unitary localization, scaling behavior, and molecular sharing structure,” arXiv:0805.2942v2; Phys. Rev. A 78, 042310 (2008).
3. C. Berthière and P. Gaudin, “Genuine multientropy, dihedral invariants, and Lifshitz theory,” Phys. Rev. D 113, 065029 (2026).