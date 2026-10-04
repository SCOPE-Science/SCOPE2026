# Exact spherical isotropization of subspace-isotropic measures
## Finding
Let \(d\ge 2\), let \(U\subset\mathbb R^d\) be an \(r\)-dimensional subspace with \(1\le r\le d\), and let \(P_U\) be the orthogonal projection onto \(U\). Suppose \(\mu\) is a probability measure on \(\mathbb S^{d-1}\), supported on \(U\cap\mathbb S^{d-1}\), whose second-moment matrix is
\[
\Gamma_\mu:=\int xx^{\mathsf T}\,d\mu(x)=\frac1rP_U.
\]
Let \(\mathcal T(\mathbb S^{d-1})\) be the probabilities \(\nu\) on \(\mathbb S^{d-1}\) satisfying \(\Gamma_\nu=I_d/d\), and define
\[
I(\mu,\mathbb S^{d-1})=\inf_{\nu\in\mathcal T(\mathbb S^{d-1})}W_2^2(\mu,\nu).
\]
Then
\[
I(\mu,\mathbb S^{d-1})=2-2\sqrt{\frac rd}.
\]
For \(r<d\), if \((X,Y)\) is a coupling of \(\mu\) with a spherical tight probability, then it is optimal if and only if
\[
P_UY=\sqrt{\frac rd}\,X\qquad\text{almost surely}.
\]
Equivalently, with
\[
Y=\sqrt{\frac rd}\,X+\sqrt{\frac{d-r}{d}}\,Z,
\]
all optimal couplings are exactly those for which \(Z\in U^\perp\cap\mathbb S^{d-1}\) almost surely and
\[
\mathbb E[ZZ^{\mathsf T}]=\frac1{d-r}P_{U^\perp},\qquad \mathbb E[XZ^{\mathsf T}]=0.
\]
An explicit optimum is obtained by taking \(Z\) independent of \(X\) with any centered tight spherical law on \(U^\perp\). When \(r=d\), \(\mu\) is already spherical tight and the value is \(0\).

## Assumptions and scope
The moment matrix here is the uncentered second moment, not the covariance. No condition on the mean of \(\mu\) is imposed. For \(r<d\), the source is intentionally rank deficient as a measure in \(\mathbb R^d\): it is isotropic only inside its supporting subspace. The target is required to remain on the same ambient unit sphere and to be tight in all \(d\) dimensions.

## Proof
Fix \(\nu\in\mathcal T(\mathbb S^{d-1})\) and a coupling \(\pi\) of \(\mu\) and \(\nu\), realized as random vectors \((X,Y)\). Since both marginals lie on the unit sphere,
\[
\mathbb E\|X-Y\|^2=2-2\mathbb E\langle X,Y\rangle.
\]
Because \(X\in U\) almost surely,
\[
\mathbb E\langle X,Y\rangle=\mathbb E\langle X,P_UY\rangle.
\]
Cauchy--Schwarz in \(L^2(\pi;U)\) gives
\[
\mathbb E\langle X,P_UY\rangle
\le \bigl(\mathbb E\|X\|^2\bigr)^{1/2}
   \bigl(\mathbb E\|P_UY\|^2\bigr)^{1/2}.
\]
The first factor is \(1\). Tightness of \(\nu\) gives
\[
\mathbb E\|P_UY\|^2=\operatorname{tr}(P_U\Gamma_\nu)=\frac rd.
\]
Hence every admissible coupling has cost at least
\[
2-2\sqrt{\frac rd}.
\]

For \(r<d\), choose a probability \(\eta\) on \(U^\perp\cap\mathbb S^{d-1}\) with zero mean and second moment \(P_{U^\perp}/(d-r)\). Such a measure exists, for example the rotationally invariant law, or the equally weighted antipodal pair when \(d-r=1\). Let \(X\sim\mu\) and \(Z\sim\eta\) be independent and put
\[
Y=\sqrt{\frac rd}\,X+\sqrt{\frac{d-r}{d}}\,Z.
\]
Orthogonality gives \(\|Y\|=1\) almost surely. Independence and \(\mathbb EZ=0\) eliminate the mixed second moment, so
\[
\mathbb E[YY^{\mathsf T}]
=\frac rd\frac1rP_U+\frac{d-r}{d}\frac1{d-r}P_{U^\perp}
=\frac1dI_d.
\]
Thus the law of \(Y\) is spherical tight. Moreover
\[
\langle X,Y\rangle=\sqrt{\frac rd}
\]
almost surely, so this coupling attains the lower bound.

It remains to identify equality. Equality in the displayed \(L^2\) Cauchy--Schwarz inequality, with positive extremal correlation, holds exactly when
\[
P_UY=cX
\]
almost surely for a constant \(c\ge0\). Taking squared norms and expectations determines \(c=\sqrt{r/d}\). Since \(\|Y\|=\|X\|=1\), the orthogonal component of \(Y\) then has constant norm \(\sqrt{(d-r)/d}\). Defining \(Z\) by the displayed decomposition gives \(Z\in U^\perp\cap\mathbb S^{d-1}\). The diagonal and off-diagonal blocks of the identity \(\mathbb E[YY^{\mathsf T}]=I_d/d\) are exactly
\[
\mathbb E[ZZ^{\mathsf T}]=\frac1{d-r}P_{U^\perp},\qquad
\mathbb E[XZ^{\mathsf T}]=0.
\]
Conversely, those two moment conditions make the law of \(Y\) spherical tight and give equality in the cost bound. This proves both the exact value and the optimal-coupling characterization. For \(r=d\), the source moment is already \(I_d/d\), so \(I=0\).

## Verification
The argument is analytic and uses no finite experiment as a substitute for an infinite statement. The critical identities can be checked directly: the lower bound depends only on \(\operatorname{tr}(P_U\Gamma_\nu)=r/d\), and the explicit lift has unit norm because its two components are orthogonal. Its second moment is exactly \(I_d/d\). At the endpoints, \(r=d\) gives zero distance, while \(r=1\) gives \(2-2/\sqrt d\); the latter applies to every probability supported on an antipodal pair, regardless of its mean.

## Relationship to prior work
Cheng and Okoudjou prove that a full-rank probabilistic frame in \(\mathbb R^d\) has a closest Parseval probabilistic frame obtained by a canonical linear push-forward. Their hypothesis excludes the rank-deficient sources considered here, and their target is not constrained to the unit sphere.

Maslouhi and Loukili formulate the spherical problem \(I(\mu,\mathbb S^{d-1})\), prove compactness of the spherical tight class, and conclude that the expression of this quantity is still open in general. The result above gives an exact family of solutions, with all optimal couplings, for every subspace dimension and without a mean-zero assumption.

Chen's 2024 dissertation abstract reports existence and a lower-bound estimate for the closest spherical probabilistic Parseval frame. Chen and Schmoll later derive the frame-operator/Bures lower bound for prescribed second moments and extend the associated matrix metric continuously to positive semidefinite operators. For \(\Gamma_\mu=P_U/r\) and target moment \(I_d/d\), that matrix lower bound equals \(2-2\sqrt{r/d}\). The new ingredient here is an explicit sphere-preserving attainment for every such singular source, together with the equality characterization of all optimal couplings.

## Limitations
The theorem does not solve the spherical minimization problem for arbitrary source measures. It uses the exact subspace-isotropy condition \(\Gamma_\mu=P_U/r\). Optimal target measures need not be unique; the theorem instead characterizes optimal couplings through their fixed projection and orthogonal second-moment conditions. The full text of the 2024 dissertation was not materially inspected here, so an equivalent special case hidden there remains a residual priority risk.

## References
D. Cheng and K. A. Okoudjou, *Optimal properties of the canonical tight probabilistic frame*, arXiv:1705.03437, dated 2017-05-09.

M. Maslouhi and S. Loukili, *Probabilistic tight frames and representation of Positive Operator-Valued Measures*, Applied and Computational Harmonic Analysis, DOI:10.1016/j.acha.2018.06.003.

D. Chen, *Probabilistic Frames and Concepts from Optimal Transport*, Clemson University dissertation, 2024, All Dissertations 3677.

D. Chen and M. Schmoll, *Probabilistic frames and Wasserstein distances*, arXiv:2501.02602, 2025.
