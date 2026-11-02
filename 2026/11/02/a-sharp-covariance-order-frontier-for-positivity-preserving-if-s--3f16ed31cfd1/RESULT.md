# A sharp covariance-order frontier for positivity-preserving IF-SSPRK2

## Finding

For a constant positive-semidefinite forcing, the positivity-preserving two-stage integrating-factor scheme of Zhang, Lan, and Jing (2026, equation (5)) may approach a stationary covariance which is neither above nor below the true stationary covariance in Loewner order. The exact boundary is determined by forcing correlation.

Let \(a,b,h>0\), \(A=-\operatorname{diag}(a,b)\), and \(Q=(q_{ij})_{i,j=1}^2\succeq0\) be constant. Consider
\[
\dot X=AX+XA^{\mathsf T}+Q.
\]
Denote by \(X_*\) its continuous stationary solution and by \(X_h\) the unique stationary state of the specified IF-SSPRK2 step. Define the Langevin function \(L(t)=\coth t-1/t\) for \(t>0\), and
\[
d_a=\tfrac h2L(ha),\qquad d_b=\tfrac h2L(hb),\qquad d_m=\tfrac h2L(h(a+b)/2).
\]
Then the stationary error is exactly
\[
E_h=X_h-X_*=
\begin{pmatrix}q_{11}d_a&q_{12}d_m\\q_{12}d_m&q_{22}d_b\end{pmatrix}.
\]
If \(q_{11}q_{22}>0\), put \(r=|q_{12}|/\sqrt{q_{11}q_{22}}\in[0,1]\) and
\[
\theta_h(a,b)=\frac{\sqrt{L(ha)L(hb)}}{L(h(a+b)/2)}.
\]
The sharp Loewner-order trichotomy is
\[
\begin{array}{ll}
E_h\succ0 &\Longleftrightarrow r<\theta_h(a,b),\\
E_h\succeq0\text{ and singular} &\Longleftrightarrow r=\theta_h(a,b),\\
E_h\text{ is indefinite} &\Longleftrightarrow r>\theta_h(a,b).
\end{array}
\]
If \(q_{11}q_{22}=0\), positivity of \(Q\) forces \(q_{12}=0\), and \(E_h\succeq0\). In particular, \(0<\theta_h(a,b)<1\) whenever \(a\ne b\); if \(a=b\), then \(\theta_h(a,b)=1\).

Consequently, for every distinct pair of decay rates and every timestep \(h>0\), any rank-one forcing \(Q=vv^{\mathsf T}\) with \(v_1v_2\ne0\) produces an **indefinite** error \(X_h-X_*\), even though the time-stepping scheme and both stationary covariances preserve positive semidefiniteness. For rank-one forcing with both entries nonzero, both stationary covariances are in fact positive definite when \(a\ne b\).

The transition ratio has sharp endpoint limits
\[
\lim_{h\downarrow0}\theta_h(a,b)=\frac{2\sqrt{ab}}{a+b},
\qquad
\lim_{h\to\infty}\theta_h(a,b)=1.
\]
For the rank-one forcing \(Q=\mathbf{1}\mathbf{1}^{\mathsf T}\), where \(\mathbf{1}=(1,1)^{\mathsf T}\), the negative eigenvalue has the quantitative limits
\[
\lambda_{\min}(E_h)=
\frac{h^2}{12}\left(a+b-\sqrt{2(a^2+b^2)}\right)+O(h^4)
\quad(h\downarrow0),
\]
\[
\lim_{h\to\infty}\lambda_{\min}(E_h)=-\frac{(a-b)^2}{4ab(a+b)}.
\]

## Assumptions and scope

The matrix dimension is exactly two, \(A\) is real symmetric strictly stable with diagonal rates \(-a,-b\), and \(Q\) is any real constant symmetric positive-semidefinite matrix. The timestep \(h\) is arbitrary and strictly positive. All statements concern exact arithmetic and the specific full-matrix, final IF-SSPRK2 update (equation (5) of the cited 2026 paper), without low-rank truncation or additional corrections. A real orthogonal change of coordinates transports the result unchanged to every real symmetric negative-definite \(2\times2\) drift.

The statement compares the method's **limiting stationary state**, not its finite-time global error, and does not assert that the two stationary matrices themselves are indefinite.

## Proof

**1. The actual stage map.** Write \(D=e^{hA}=\operatorname{diag}(e^{-ah},e^{-bh})\). When \(Q\) is constant, the three stages printed in equation (5) are
\[
\widehat X_1=DXD+hDQD,\quad
\widehat X_2=D\widehat X_1D+hDQD,\quad
\Phi_h(X)=\tfrac12DXD+\tfrac12D^{-1}\widehat X_2D^{-1}.
\]
Substitution, without any asymptotic approximation, yields
\[
\boxed{\Phi_h(X)=DXD+\tfrac h2(DQD+Q).}
\]
The two forcing terms are positive semidefinite when \(Q\succeq0\); every iterate starting from \(X_0\succeq0\) therefore remains positive semidefinite. Since each multiplier \(e^{-h(a_i+a_j)}\) is strictly below one, the map has exactly one attracting fixed point, entrywise
\[
(X_h)_{ij}=\frac h2\frac{1+e^{-h(a_i+a_j)}}{1-e^{-h(a_i+a_j)}}q_{ij}
=\frac h2\coth\!\left(\frac{h(a_i+a_j)}2\right)q_{ij},
\quad(a_1,a_2)=(a,b).
\]
The continuous Lyapunov equation gives \((X_*)_{ij}=q_{ij}/(a_i+a_j)\). Subtracting proves the stated formula for \(E_h\).

**2. Strict concavity of the error kernel.** First \(L(t)>0\), since \(\tanh t<t\) for \(t>0\). Direct differentiation gives
\[
L''(t)=2\left(\frac{\cosh t}{\sinh^3t}-\frac1{t^3}\right).
\]
To prove strict negativity, define
\[
g(t)=3\log\!\frac{\sinh t}{t}-\log\cosh t.
\]
The sign of \(g'(t)\) is the sign of
\[
H(t)=t(2+\cosh2t)-\tfrac32\sinh2t.
\]
Here \(H(0)=H'(0)=0\) and
\[
H''(t)=2(2t\cosh2t-\sinh2t)>0,
\]
since \(\tanh(2t)<2t\). Thus \(g(t)>g(0)=0\), giving \(\sinh^3t>t^3\cosh t\) and \(L''(t)<0\). Because \(L\) is positive and strictly concave, \(\log L\) is strictly concave. Hence for \(a\ne b\)
\[
L(h(a+b)/2)^2>L(ha)L(hb),
\]
whereas equality holds for \(a=b\). This proves the claimed sharp range of \(\theta_h\).

**3. Correlation classification.** All three multipliers \(d_a,d_b,d_m\) are positive. If \(q_{11}q_{22}>0\), the error has two positive diagonal entries, and
\[
\det E_h=q_{11}q_{22}d_m^2(\theta_h^2-r^2).
\]
The sign of this determinant proves all three cases, including equality. If \(q_{11}q_{22}=0\), the positive-semidefinite forcing condition implies \(q_{12}=0\) and the error is diagonal positive semidefinite. For rank-one \(Q=vv^{\mathsf T}\) with \(v_1v_2\ne0\), \(r=1\), so strict indefiniteness follows for every \(h>0\) when \(a\ne b\).

Both stationary states are positive semidefinite by their integral and convergent-step representations. In the nondegenerate rank-one setting, \(X_*\succ0\), since its determinant is \(v_1^2v_2^2(a-b)^2/[4ab(a+b)^2]>0\). Also \(X_h\succ0\), because
\[
X_h=\frac h2vv^{\mathsf T}+h\sum_{k=1}^{\infty}
(D^kv)(D^kv)^{\mathsf T},
\]
and the vectors \(v\) and \(Dv\) are linearly independent for distinct rates with nonzero components.

**4. Endpoints and a quantitative witness.** The classical Taylor expansion, obtained directly from the definitions,
\[
L(t)=t/3-t^3/45+O(t^5)
\]
proves the small-step transition limit and
\[
E_h=\frac{h^2}{12}
\begin{pmatrix}
2a q_{11}&(a+b)q_{12}\\
(a+b)q_{12}&2b q_{22}
\end{pmatrix}+O(h^4)
\]
entrywise with fixed \(a,b,Q\). For \(Q=\mathbf{1}\mathbf{1}^{\mathsf T}\), diagonalizing the leading \(2\times2\) symmetric coefficient yields the asserted negative-eigenvalue expansion.

As \(h\to\infty\), \(L(t)\to1\), so \(\theta_h\to1\). For the same rank-one forcing,
\[
E_h=\tfrac h2\mathbf{1}\mathbf{1}^{\mathsf T}-X_*+o(1).
\]
In the orthonormal basis \(\mathbf{1}/\sqrt2\), \((1,-1)^{\mathsf T}/\sqrt2\), one eigenvalue grows like \(h\) and the other converges to the negative of the second basis vector's quadratic form under \(X_*\), namely \(-(a-b)^2/[4ab(a+b)]\). This proves the second eigenvalue limit.

For an explicit witness, \(a=1,b=3,h=1,Q=\mathbf{1}\mathbf{1}^{\mathsf T}\) yields \(d_a\approx0.15651764275\), \(d_m\approx0.26865736036\), \(d_b\approx0.33581824499\), \(\det E_h\approx-0.01961529718\), and \(\lambda_{\min}(E_h)\approx-0.03705273646\). These values illustrate, but are not needed for, the proof.

## Verification

Run the standalone standard-library script `python3 verify.py` in the same folder. It reconstructs all three source stages and the collapsed update, verifies both stationary equations, checks the correlation frontier and rank-one counterexamples over parameter grids, and checks the two asymptotic regimes. The test contains deterministic and fixed-seed examples; the proof above establishes the statements for all permitted parameters. No finite computational test is used to establish universal strict concavity or the exact correlation classification.

## Relationship to prior work

Zhang, Lan, and Jing (2026), Section 2 and Theorem 3.2, introduce the IF-SSPRK2 stage map and prove positive-semidefinite preservation; Theorem 3.4 provides a finite-time convergence estimate. Those results are inputs, not new claims here. Their inspected text does not give the stationary fixed-point matrix, its Langevin-function error kernel, or the sharp forcing-correlation criterion for Loewner overestimation.

Chen and Borzì (2023) investigate positivity-preserving exponential Euler and midpoint integrators for differential Riccati equations. These are different integration maps; positivity and error estimates for those methods do not by themselves yield the present IF-SSPRK2 fixed-point classification. Gillis and Diehl (2013) introduce a positivity-preserving discretization based on collocation, not equation (5). The classic continuous controllability-Gramian identity and elementary scalar trapezoidal bias are not presented as new.

The contribution is the sharp **matrix-order** threshold and its all-positive-step, heterogeneous-decay consequence. Related positivity and stationary-covariance literature may still contain earlier equivalent formulations; see limitations.

## Limitations

The complete 2023 Riccati-integrator paper and 2013 collocation paper were not inspected in full; the comparison uses accessible abstracts and publisher-preview material. Their methods appear different, but an unnoticed historical equivalence cannot be excluded. The result is a two-dimensional exact-arithmetic classification with constant forcing and symmetric stable drift. It makes no claims about nonnormal drift, nonlinear forcing, general high-dimensional forcing-correlation phase boundaries, low-rank truncation, finite-precision error, or numerical safety certification. The finding has not received an independent audit.

## References

1. W. Zhang, R. Lan, X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703v1, first posted 2026-06-14. https://arxiv.org/abs/2606.15703
2. H. Chen, A. Borzì, *Positivity Preserving Exponential Integrators for Differential Riccati Equations*, Journal of Scientific Computing 96 (2023), article 50. DOI:10.1007/s10915-023-02275-6.
3. J. Gillis, M. Diehl, *A Positive Definiteness Preserving Discretization Method for Lyapunov Differential Equations*, IEEE Conference on Decision and Control (2013), 7759–7764. DOI:10.1109/CDC.2013.6761121.
4. H. Chen, A. Borzì, *Low-rank exponential integrators for stiff differential Riccati equations*, Advances in Computational Mathematics 51 (2025), article 17. DOI:10.1007/s10444-025-10228-w.
