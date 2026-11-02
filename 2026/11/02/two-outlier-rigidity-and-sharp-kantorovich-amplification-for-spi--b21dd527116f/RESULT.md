# Two-outlier rigidity and sharp Kantorovich amplification for spiked near-spectral endpoints

## Finding

Let \(H\) be a real or complex Hilbert space with \(\dim H\ge 2\). Let \(A\) be a bounded, strictly positive, self-adjoint operator with spectral endpoints \(0<m:=\min\sigma(A)\le M:=\max\sigma(A)<\infty\). Fix \(\alpha>\beta>0\). For every unit vector \(u\), let \(P_u\) be the orthogonal rank-one projection onto \(\mathbb F u\), and define
\[
B_u=\beta^2I+(\alpha^2-\beta^2)P_u,
\qquad
D_u=A^{-1/2}B_u^{1/2}AB_u^{1/2}A^{-1/2}.
\]
The operator \(D_u\) is the endpoint of the near-spectral geometric construction with inputs \(A,B_u\). Set
\[
k(u)=\langle Au,u\rangle\langle A^{-1}u,u\rangle,\qquad
T(u)=\alpha^2+\beta^2+(\alpha-\beta)^2(k(u)-1).
\]
Then \(D_u-\beta^2 I\) has rank at most two. Apart from the flat value \(\beta^2\), its only spectral values are the two positive numbers
\[
\Lambda_\pm(u)=\frac{T(u)\pm\sqrt{T(u)^2-4\alpha^2\beta^2}}2,
\qquad \Lambda_+(u)\Lambda_-(u)=\alpha^2\beta^2.
\]
More precisely, if \(u\) is not an eigenvector of \(A\), the two values are simple eigenvalues, with \(\Lambda_-(u)<\beta^2<\alpha^2<\Lambda_+(u)\); the orthogonal complement of a reducing two-dimensional subspace carries the scalar operator \(\beta^2 I\). If \(u\) is an eigenvector, \(D_u=B_u\), \(\Lambda_+=\alpha^2\), and \(\Lambda_-=\beta^2\). Thus the formula includes finite dimensions as well as infinite dimensions, where \(\beta^2\) is an essential spectral value.

Put
\[
K=\frac{(M+m)^2}{4Mm},\quad
T_*=\alpha^2+\beta^2+(\alpha-\beta)^2\frac{(M-m)^2}{4Mm},\quad
L_*=\frac{T_*+\sqrt{T_*^2-4\alpha^2\beta^2}}2.
\]
The complete sharp norm envelope over spike directions is
\[
\inf_{\|u\|=1}\|D_u\|=\alpha^2,
\qquad
\sup_{\|u\|=1}\|D_u\|=L_*.
\]
All intermediate norm values occur. The lower endpoint is attained exactly by eigenvectors of \(A\). If \(m<M\), the upper endpoint is attained exactly when both \(m\) and \(M\) are eigenvalues and \(u=(u_m+u_M)/\sqrt2\) up to independent phases, with unit \(u_m\in\ker(A-mI)\), \(u_M\in\ker(A-MI)\). If \(m=M\), the range is the singleton \(\{\alpha^2\}\). Endpoint inclusion is therefore completely determined even when \(A\) has continuous spectrum. The optimal least spectral value is \(\inf_{\|u\|=1}\min\sigma(D_u)=\alpha^2\beta^2/L_*\), with the same upper-envelope attainment condition.

For fixed \(\alpha,\beta\), as the condition number \(\kappa=M/m\) tends to infinity, the largest possible outlier and the smallest possible outlier obey the sharp asymptotics
\[
L_*\sim\frac{(\alpha-\beta)^2}{4}\kappa,
\qquad
\frac{\alpha^2\beta^2}{L_*}\sim
\frac{4\alpha^2\beta^2}{(\alpha-\beta)^2\kappa}.
\]
These are limits of sharp envelopes, not assertions that an endpoint is attained in every Hilbert space.

## Assumptions and scope

The field \(\mathbb F\) is \(\mathbb R\) or \(\mathbb C\); all operators act on the same Hilbert space \(H\). Strict positivity means \(A\ge mI\) for some \(m>0\), so the bounded inverse and fractional powers are well defined. The two spectral endpoints belong to \(\sigma(A)\), but need not be eigenvalues. The spike amplitudes are fixed and distinct, \(\alpha>\beta>0\); the only optimization is over \(u\) of norm one. The operator \(D_u\) is defined explicitly, without assuming an infinite-dimensional extension of any matrix-only geometric-mean axiom.

## Proof

**Rank-two reduction.** Since \(P_u^2=P_u\),
\[
B_u^{1/2}=\beta I+(\alpha-\beta)P_u.
\]
Let \(s=\alpha-\beta\), \(v=A^{1/2}u\), \(w=A^{-1/2}u\), and \(X=A^{1/2}B_u^{1/2}A^{-1/2}\). With the convention that \(|v\rangle\langle w|\) maps \(x\) to \(v\langle w,x\rangle\),
\[
X=\beta I+s|v\rangle\langle w|,
\qquad
D_u=X^*X,
\qquad
\langle w,v\rangle=1.
\]
The finite-dimensional subspace \(E=\operatorname{span}\{v,w\}\) reduces both \(X\) and \(X^*\); on \(E^\perp\), \(D_u=\beta^2 I\). Hence \(D_u-\beta^2 I\) has rank at most two. If \(v,w\) are dependent, equality in Cauchy–Schwarz forces \(Au=\lambda u\), so \(D_u=B_u\). Otherwise \(\dim E=2\). On \(E\), \(X\) has eigenvalue \(\alpha\) on \(v\) and eigenvalue \(\beta\) on the one-dimensional kernel of \(\langle w,\cdot\rangle\). Thus
\[
\det(D_u|_E)=|\det(X|_E)|^2=\alpha^2\beta^2.
\]
Expanding \(X^*X\) and taking the trace on the two-dimensional subspace gives
\[
\operatorname{tr}(D_u|_E)
=2\beta^2+2\beta s+s^2\|v\|^2\|w\|^2
=\alpha^2+\beta^2+s^2(k(u)-1).
\]
The quadratic formula yields \(\Lambda_\pm\). If \(u\) is not an eigenvector, strict Cauchy–Schwarz gives \(k(u)>1\). Hence the sum of the roots strictly exceeds \(\alpha^2+\beta^2\) while their product stays fixed, proving the strict two-sided outlier inequalities. Because \(\Lambda_+\ge\alpha^2>\beta^2\), one has \(\|D_u\|=\Lambda_+(u)\) in both cases, and \(\min\sigma(D_u)=\Lambda_-(u)\).

**Sharp range of the orientation parameter.** Cauchy–Schwarz applied to \(A^{1/2}u\) and \(A^{-1/2}u\) yields \(k(u)\ge1\), with equality exactly for an eigenvector of \(A\). For every \(t\in[m,M]\),
\[
t+\frac{mM}{t}\le m+M.
\]
By the spectral functional calculus, \(A+mMA^{-1}\le(m+M)I\). Thus
\[
2\sqrt{mMk(u)}\le\langle Au,u\rangle+mM\langle A^{-1}u,u\rangle\le m+M,
\]
so \(k(u)\le K\). For \(m<M\), equality in the operator inequality requires \(u\) to be supported by the endpoint eigenspaces, and equality in the scalar arithmetic–geometric inequality forces equal squared weights there. Conversely, equal weights on any unit endpoint eigenvectors give equality.

Even when the endpoints are not eigenvalues, nonzero spectral subspaces in shrinking intervals around \(m\) and \(M\) supply orthogonal unit vectors \(u_{m,j},u_{M,j}\). Their balanced sums satisfy \(k((u_{m,j}+u_{M,j})/\sqrt2)\to K\). An approximate eigenvector at any spectral value gives \(k(u_j)\to1\). These constructions prove both bounds are sharp. Since the unit sphere of a real or complex Hilbert space of dimension at least two is path connected and \(k\) is continuous, every value strictly between \(1\) and \(K\) is realized; endpoint membership is exactly as stated.

**Norm envelope and asymptotics.** For fixed positive product \(\alpha^2\beta^2\), the upper root of \(\lambda^2-T\lambda+\alpha^2\beta^2=0\) increases strictly with \(T\ge\alpha^2+\beta^2\). Apply the established sharp range \(1\le k\le K\), and use the product identity for the lower root. Since \(K-1=(\kappa-1)^2/(4\kappa)\sim\kappa/4\) as \(\kappa\to\infty\), the displayed asymptotics follow.

## Verification

The accompanying `verify.py` executes deterministic finite-dimensional numerical cross-checks for dimensions two through eight with reproducible complex spike directions, plus endpoint-equality examples. It verifies the complete eigenvalue multiset, two-outlier product, rank-two support, and the sharp orientation bounds. The run passed 8,076 assertions with maximum absolute residual under \(4.1\times10^{-13}\). The code requires Python 3 and NumPy, and can be run using `python verify.py`. These finite computations are not the proof of the infinite-dimensional statements, which rely on the reducing-subspace and spectral-functional-calculus arguments above.

## Relationship to prior work

Ibrahim and Huang (2026), Theorems 4.2 and 4.3, introduce the near-spectral endpoint and prove qualitative log-majorization \(B\prec_{\log}D\); Proposition 4.13 gives a closed matrix formula in dimension two with normalized determinants. Those statements do not classify spiked endpoints in arbitrary finite or infinite dimension, the two outlier multiplicities, the exact sharp norm envelope, or endpoint spectral-attainment conditions. The present theorem uses the established endpoint definition, not a claim of having invented it.

Franco, Gan, and Kim (2025) introduce the antecedent near-geometric means and study order and log-majorization. Bibliographic and abstract information, but not the full text, was available for this comparison. Rank-one perturbation singular-value interlacing, as in Zhu, Peng, and Liu (2019), gives general bounds, while the classical Kantorovich inequality supplies the sharp scalar upper factor. Neither ingredient alone supplies the stated near-spectral operator's complete two-outlier classification and infinite-dimensional attainment test. The generic rank-two singular-value mechanism is standard and is not claimed as independent novelty.

## Limitations

The input \(B_u\) has a single exceptional eigenvalue against a scalar background. The theorem does not determine the spectrum for arbitrary positive definite \(B\), for multiple spikes, or for noninvertible \(A\). Its spectral formulas involve a known rank-one perturbation mechanism and the classical Kantorovich inequality; independent reviewers should assess whether a different existing formulation already subsumes the exact combined result. The 2025 near-geometric article's full text could not be checked in this investigation. No independent mathematical audit or publication-priority certification has been performed.

## References

1. M. A. Ibrahim and H. Huang, *Order Relations for the Near Geometric and Near Spectral Geometric Curves*, arXiv:2610.23736v1 (first posted 2026-10-16), especially Theorems 4.2–4.3 and Proposition 4.13. https://arxiv.org/abs/2610.23736
2. J. A. Franco, L. Gan, and S. Kim, *Near-geometric mean of positive definite operators*, *Positivity* **29** (2025), article 54, DOI 10.1007/s11117-025-01147-7. https://doi.org/10.1007/s11117-025-01147-7
3. L. Zhu, X. Peng, and H. Liu, *Rank-one perturbation bounds for singular values of arbitrary matrices*, *Journal of Inequalities and Applications* **2019**, article 138, DOI 10.1186/s13660-019-2089-4. https://doi.org/10.1186/s13660-019-2089-4
4. The classical Kantorovich inequality for a bounded positive invertible operator, used only for the scalar product \(\langle Au,u\rangle\langle A^{-1}u,u\rangle\).
