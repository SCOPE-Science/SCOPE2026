# Sharp false-acceptance asymptotics for Gaussian two-column sketch conditioning

## Finding
A Gaussian sketch can incorrectly certify the conditioning of a two-column nonorthogonal basis. The probability of this false acceptance admits both an exact finite-sample beta integral and a sharp large-sample asymptotic including the leading constant.

**Theorem.** Let \(d\ge 2\), let \(B\in\mathbb R^{d\times2}\) have linearly independent columns, and write \(\kappa=\kappa_2(B)>1\). For each integer \(s\ge2\), let \(S_s\in\mathbb R^{s\times d}\) have independent real Gaussian entries \(N(0,1/s)\). Hold \(B\), \(\kappa\), and the false-acceptance threshold \(\tau\) fixed, with \(1<\tau<\kappa\). Write
\[
K=\kappa^2,\qquad T=\tau^2,\qquad w=\tau+\tau^{-1},\qquad
h(x)=\frac{(1+(K-1)x)^2}{K w^2x(1-x)}\quad(0<x<1).
\]
With \(I_z(a,b)=\mathrm B_z(a,b)/\mathrm B(a,b)\) the regularized incomplete beta function, the false-pass probability is, exactly,
\[
\boxed{p_s=\Pr\{\kappa_2(S_sB)\le\tau\}
=\frac{1}{\mathrm B(s/2,s/2)}\int_0^1 x^{s/2-1}(1-x)^{s/2-1}
\mathbf1_{\{h(x)<1\}} I_{1-h(x)}\!\left(\frac12,\frac{s-1}{2}\right)\,dx.}
\]
Moreover, as \(s\to\infty\),
\[
\boxed{p_s=\frac{\mathcal C(\kappa,\tau)+o(1)}{\sqrt s}\exp[-s\mathcal I(\kappa,\tau)],}
\]
where both the rate and the leading multiplier are explicit:
\[
\boxed{\mathcal I(\kappa,\tau)=\log\frac{\kappa^2+\tau^2}{2\kappa\tau}>0,\qquad
\mathcal C(\kappa,\tau)=
\frac{\kappa^2+\tau^2}{\kappa^2-\tau^2}
\sqrt{\frac{(\kappa^2+\tau^2)(\tau^2-1)}{4\pi\tau^2(\kappa^2-1)}}.}
\]
The single most likely falsely accepted sample Gram matrix, in singular-vector coordinates for the normalized Gaussian-sketch sample covariance, is
\[
\boxed{C_*=\operatorname{diag}\left(\frac{2\kappa^2\tau^2}{\kappa^2+\tau^2},\frac{2\kappa^2}{\kappa^2+\tau^2}\right).}
\]
The ratio of its two eigenvalues is exactly \(\tau^2\), so the large-deviation optimizer lies on the conditioning-test boundary.

## Assumptions and scope
All matrices are real and all Gaussian coordinates independent; \(S_s\) is sampled independently of the fixed deterministic \(B\). The singular values of \(B\) are positive, and \(1<\tau<\kappa_2(B)\) is essential for the stated interior-boundary asymptotic. The probability is for the condition number of a *single fixed two-column basis*, not an adaptively generated basis depending on the same sketch. Singular-value scaling and orthogonal changes of coordinates do not affect the probability.

## Proof
**1. Gaussian reduction and an exact beta integral.** Singular-value decomposition and Gaussian rotational invariance reduce the sample Gram matrix, up to an irrelevant positive scalar, to the Wishart matrix with population covariance \(\Sigma=\operatorname{diag}(K,1)\). The real Bartlett/Gram-Schmidt decomposition yields
\[
C=\frac1s\begin{pmatrix}
KU&\sqrt{KU}\,Z\\
\sqrt{KU}\,Z&Z^2+V
\end{pmatrix},\qquad
U\sim\chi_s^2,\quad V\sim\chi_{s-1}^2,\quad Z\sim N(0,1),
\]
with the three random variables independent. Thus \(U\), \(V\), and \(Z^2\) are independent gamma variables with common scale two and respective shapes \(s/2\), \((s-1)/2\), and \(1/2\). Their beta-gamma factorization implies independent random variables
\[
X=\frac{U}{U+V+Z^2}\sim\operatorname{Beta}(s/2,s/2),\quad
R=\frac{V}{V+Z^2}\sim\operatorname{Beta}((s-1)/2,1/2).
\]
For any positive definite \(2\times2\) matrix, \(\kappa_2(C^{1/2})\le\tau\) is equivalent to \((\operatorname{tr}C)^2/\det C\le(\tau+\tau^{-1})^2\). Substituting the Bartlett representation and cancelling the total gamma mass gives precisely \(R\ge h(X)\). Conditioning on \(X\) proves the displayed finite-sample integral. Equalities on the integration boundary have probability zero.

**2. Unique large-deviation saddle.** Let \(C\) now denote the normalized sample Gram matrix. Its positive-definite Wishart large-deviation rate is
\[
J(C)=\tfrac12\big[\operatorname{tr}(\Sigma^{-1}C)-\log\det(\Sigma^{-1}C)-2\big].
\]
The constraint \(\kappa_2(C^{1/2})\le\tau\) means that the ordered eigenvalue ratio lies in \([1,T]\). At fixed ordered eigenvalues, the trace rearrangement inequality minimizes \(J\) by aligning the larger eigenvalue with the \(K\)-eigenvector of \(\Sigma\). Write the two eigenvalues \(rb,b\) with \(1\le r\le T\). Direct differentiation in \(b\) minimizes the rate at \(b=2K/(K+r)\), leaving
\[
J(r)=\log\frac{K+r}{2\sqrt{Kr}},\qquad
J'(r)=\frac{r-K}{2r(K+r)}<0\quad(1\le r\le T<K).
\]
Thus the unique saddle is \(r=T\), the matrix \(C_*\) displayed above, and its rate is \(\mathcal I=J(T)\). Strict convexity of the Wishart rate away from this saddle controls all contributions outside any fixed neighborhood of \(C_*\).

**3. Exact tilt and the sharp multiplier.** Set
\[
A=\frac{2KT}{K+T},\quad D=\frac{2K}{K+T},\quad
\eta=\frac{T-K}{4KT}<0,\quad H(C)=C_{11}-TC_{22}.
\]
Under \(P_*\), let the \(s\) Gaussian sketch rows instead have covariance \(C_*=\operatorname{diag}(A,D)\) and retain normalization by \(1/s\). A direct comparison of Wishart densities gives, *exactly*,
\[
\frac{dP_\Sigma}{dP_*}(C)=e^{-s\mathcal I-s\eta H(C)}.
\]
For \(P_*\), the joint (local) central limit theorem gives asymptotically independent coordinates
\[
\sqrt s\,H(C)\Rightarrow N(0,\sigma_H^2),\quad
\sqrt s\,C_{12}\Rightarrow N(0,AD),\qquad \sigma_H=2TD.
\]
The relevant event is localized by the exponential weight to \(sH(C)=O(1)\) and \(\sqrt{s}C_{12}=O(1)\). Specifically, writing \(z=\sqrt{s}C_{12}\) and \(u=sH(C)\), the eigenvalue perturbation at the distinct-eigenvalue saddle gives, uniformly on compact \((u,z)\)-sets,
\[
s\big(\lambda_{\max}(C)-T\lambda_{\min}(C)\big)
=u+c z^2+o(1),\qquad c=\frac{T+1}{A-D}>0.
\]
The standard smooth Wishart local limit (obtained directly from its explicit density and Stirling's formula) has density \(1/(\sigma_H\sqrt{2\pi})\) at \(H=0\), jointly with \(z\sim N(0,AD)\). The strict rate minimum established above bounds contributions away from the saddle exponentially, and the strict positive quadratic curvature and \(\eta<0\) give integrable Gaussian/exponential domination in the localized coordinates. Applying the density limit and dominated convergence to the exact tilt therefore yields
\[
\begin{aligned}
\lim_{s\to\infty}\sqrt s\,e^{s\mathcal I}p_s
&=\frac1{\sigma_H\sqrt{2\pi}}\int_{\mathbb R}\frac{e^{-z^2/(2AD)}}{\sqrt{2\pi AD}}
\int_{-\infty}^{-cz^2}e^{-\eta u}\,du\,dz\\
&=\frac1{|\eta|\sigma_H\sqrt{2\pi}}
\left(1+2|\eta|cAD\right)^{-1/2}.
\end{aligned}
\]
Here \(u\le-cz^2\le0\), and \(-\eta=|\eta|\) makes the inner integral finite. Elementary simplification uses
\[
|\eta|\sigma_H=\frac{K-T}{K+T},\qquad
1+2|\eta|cAD=\frac{2T(K-1)}{(K+T)(T-1)},
\]
which is exactly \(\mathcal C(\kappa,\tau)\). This proves the sharp asymptotic.

**4. Numerical-linear-algebra realization.** These fixed two-column bases can arise at the first two steps of an unorthogonalized Krylov basis. For a specified \(\kappa>1\), put \(\rho=(K-1)/(K+1)\in(0,1)\), \(v=\sqrt{1-\rho^2}\), and
\[
M=\begin{pmatrix}\rho&v\\v&1+v^2/\rho\end{pmatrix}.
\]
Then \(M\) is symmetric positive definite because its leading principal minor is \(\rho>0\) and its determinant is \(\rho>0\). For the seed \(e_1\), the normalized unorthogonalized columns \([e_1,Me_1]\) are unit vectors with inner product \(\rho\); their singular-value condition number is exactly \(\sqrt{(1+\rho)/(1-\rho)}=\kappa\). This connects the false-acceptance event to matrix-function restarting, without assuming any particular global adaptive path.

## Verification
A standalone Python program `verify_condition.py` evaluates the exact beta quadrature, checks saddlepoint and likelihood-tilt identities, compares direct Gaussian simulation with finite exact probabilities, and compares tilted importance sampling with the sharp multiplier. It needs Python, NumPy, and SciPy. Run `python verify_condition.py` in the directory containing that extracted program. Reproducible sample for \(\kappa=3\), \(\tau=2\), \(s=100\): the exact integral gives \(p_{100}\approx0.0000252080258035\); the leading asymptotic is \(0.0000270467510988\). For these same parameters \(\mathcal I\approx0.080042707674\), \(\mathcal C\approx0.809702966340\). Simulation supports the formula but is not substituted for the proof.

## Relationship to prior work
Güttel, Liu, and Nyman (2026, arXiv:2607.10354v1) introduce a sketch-conditioned restart mechanism based on monitoring the condition number of a sketched nonorthogonal Krylov basis. Their analyzed general conditioning/stability framework does not supply this *fixed two-column* false-acceptance probability or its sharp exponential rate and multiplier. Classical Gaussian-matrix condition-number distributions (including Edelman and Anderson–Wells) concern principally isotropic Gaussian matrices, rather than the anisotropic fixed-basis false-acceptance tail and its exact saddlepoint multiplier. Singull, Uwamariya, and Yang (2021) study large-deviation behavior of condition numbers in a different independent-entry setting; its full text was not completely inspected, so possible conceptual overlap remains a literature risk. The exact beta-gamma and Wishart tools themselves are classical; the claim is the particular calibrated false-acceptance law and sharp multiplier.

## Limitations
The probability concerns one fixed deterministic two-column real basis and an independent Gaussian sketch. In a restart algorithm where the basis depends on this same sketch, conditioning decisions across steps can be dependent, so this theorem alone does not give a global adaptive-failure probability or numerical stability guarantee. The asymptotic is for fixed \(1<\tau<\kappa\) as \(s\to\infty\); it is not uniform at coalescing thresholds, at \(\tau=1\), or for larger numbers of columns. Neither floating-point arithmetic nor non-Gaussian sketch families are covered. The proof invokes the explicit smooth two-dimensional Wishart density for its local limit and Gaussian domination; independent verification and broader bibliographic auditing remain appropriate.

## References
1. S. Güttel, J. Liu, and L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354v1, publicly released 2026-07-11. https://arxiv.org/abs/2607.10354
2. A. Edelman, *Eigenvalues and condition numbers of random matrices*, SIAM Journal on Matrix Analysis and Applications 9 (1988), 543–560.
3. T. W. Anderson and M. T. Wells, *The Exact Distribution of the Condition Number of a Gaussian Matrix*, 2009 (classical isotropic condition-number distribution).
4. M. Singull, D. Uwamariya, and Z. Yang, *Large-deviation asymptotics of condition numbers of random matrices*, 2021 (independent-entry large-deviation setting).
