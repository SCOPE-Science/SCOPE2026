# Spectral-radius ordered-product growth can oscillate under a smooth hyperbolic cocycle

## Statement

Sornette, Saiprasad and Troude (arXiv:2609.18017v1) introduce, for tangent products
\[
P_L(n)=J_{n+L-1}\cdots J_n,
\qquad
h_L=\frac1L\left\langle \log\rho(P_L(n))\right\rangle,
\]
and state that increasing \(L\) makes \(h_L\) approach the top Lyapunov exponent \(\lambda_1\), attributing this to alignment of a leading eigenvector of the product with the leading Oseledets direction. That convergence is not valid for general smooth tangent cocycles, even when the cocycle is bounded, invertible, periodic, non-normal, and has a strict top Lyapunov gap.

For every \(s>1\), define a smooth diffeomorphism on \(\mathbb T\times\mathbb R^2\) by
\[
F(\theta,v)=\left(\theta+\frac{\pi}{2},\;R_{\theta+\pi/2} D R_{-\theta}v\right),
\qquad
D=\begin{pmatrix}s&0\\0&s^{-1}\end{pmatrix},
\]
where \(R_\alpha\) is planar rotation through angle \(\alpha\). The circle
\[
\mathcal C=\{(\theta,0):\theta\in\mathbb T\}
\]
is invariant, and every orbit on it has period four. Along \(\mathcal C\), the tangent cocycle has Lyapunov exponents
\[
\boxed{\lambda_1=\log s,\qquad \lambda_2=0,\qquad \lambda_3=-\log s,}
\]
while its ordered-product spectral rate is exactly
\[
\boxed{
 h_L=
 \begin{cases}
 0,&L\ \text{odd},\\[2mm]
 \log s,&L\ \text{even}.
 \end{cases}}
\]
Hence
\[
\boxed{\liminf_{L\to\infty}h_L=0<\log s=\limsup_{L\to\infty}h_L=\lambda_1,}
\]
so \(h_L\) need not converge at all.

The same example also shows that finite-\(L\) spectral-radius growth is not invariant under smooth coordinate conjugacy. The smooth change of variables
\[
H(\theta,v)=(\theta,R_{-\theta}v)
\]
conjugates \(F\) to
\[
G=H\circ F\circ H^{-1},
\qquad
G(\theta,w)=\left(\theta+\frac\pi2,Dw\right).
\]
For \(G\), the identical dynamical orbit has
\[
\boxed{h_L^{G}=\log s\quad\text{for every }L,}
\]
even though \(F\) and \(G\) are smoothly conjugate and have the same Lyapunov spectrum. Along \(\mathcal C\), the derivative of \(H\) is block-orthogonal, so this discrepancy is not caused by a change of Euclidean norm on the invariant orbit.

## Proof

Along \(v=0\), derivatives with respect to \(\theta\) of the fiber map are proportional to \(v\) and vanish. Therefore
\[
DF(\theta,0)=
\begin{pmatrix}
1&0\\
0&A_\theta
\end{pmatrix},
\qquad
A_\theta=R_{\theta+\pi/2}DR_{-\theta}.
\]
The fiber products telescope:
\[
A_{\theta+(L-1)\pi/2}\cdots A_\theta
=R_{\theta+L\pi/2}D^L R_{-\theta}.
\]
Since rotations commute in dimension two,
\[
R_{\theta+L\pi/2}D^L R_{-\theta}
=R_\theta\bigl(R_{L\pi/2}D^L\bigr)R_{-\theta},
\]
so its eigenvalues are those of \(R_{L\pi/2}D^L\), independently of \(\theta\).

If \(L\) is odd, \(R_{L\pi/2}=\pm R_{\pi/2}\), and
\[
\bigl(R_{L\pi/2}D^L\bigr)^2=-I.
\]
Its two fiber eigenvalues are therefore \(\pm i\), with spectral radius one. The full tangent product has the additional base eigenvalue \(1\), hence \(\rho(DF^L)=1\) and \(h_L=0\).

If \(L\) is even, \(R_{L\pi/2}=\pm I\), so the fiber eigenvalue moduli are \(s^L\) and \(s^{-L}\). Thus \(\rho(DF^L)=s^L\) and \(h_L=\log s\).

By contrast, left and right multiplication by rotations does not alter singular values. The singular values of the fiber product are exactly \(s^L\) and \(s^{-L}\). Consequently the finite-time maximal singular-value rate is
\[
\frac1L\log\sigma_{\max}(DF^L)=\log s
\]
for every \(L\). This proves the Lyapunov spectrum and shows explicitly why a strict Oseledets gap does not force spectral-radius convergence.

The one-step fiber maps are genuinely non-normal. For example, after an orthogonal similarity they reduce to
\[
R_{\pi/2}D=
\begin{pmatrix}0&-s^{-1}\\s&0\end{pmatrix},
\]
whose products with its transpose in the two orders are \(\operatorname{diag}(s^{-2},s^2)\) and \(\operatorname{diag}(s^2,s^{-2})\), respectively.

Finally,
\[
R_{-(\theta+\pi/2)}A_\theta R_\theta=D,
\]
which proves the stated conjugacy and gives \(DG^L=\operatorname{diag}(1,D^L)\). Hence \(h_L^G=\log s\) for every \(L\).

## Mechanism: endpoint-frame mismatch

For a cocycle \(A(x)\) over \(T\), a smooth change of tangent frame \(C(x)\) gives the cohomologous cocycle
\[
\widetilde A(x)=C(Tx)A(x)C(x)^{-1}.
\]
Its length-\(L\) product is
\[
\widetilde A^{(L)}(x)=C(T^Lx)A^{(L)}(x)C(x)^{-1}.
\]
This is generally **not** a similarity transform, because the two endpoint frames are different. Norm growth changes only by bounded endpoint factors and therefore has the same asymptotic Lyapunov exponent, but the spectral radius can change at order one or even at exponential scale along selected subsequences. In the construction above, the endpoint-frame mismatch is exactly a quarter turn for odd \(L\), converting an \(s^L\) singular stretch into eigenvalues of modulus one.

This also identifies the missing point in an eigenvector-alignment argument. A large singular-value gap controls singular directions, but the spectral radius additionally depends on how the outgoing dominant direction closes against the incoming dual direction. For an approximately rank-one product \(P\approx\sigma_1 u v^T\), its nonzero eigenvalue is approximately \(\sigma_1(v^Tu)\). A small or vanishing endpoint overlap can therefore suppress the spectral radius without suppressing singular growth.

For a periodic orbit of period \(p\), endpoint frames coincide whenever \(L=kp\). Then the length-\(L\) product is a power of the monodromy matrix and the spectral-radius rate equals the largest Floquet/Lyapunov rate. The counterexample is consistent with this: all multiples of four give \(h_L=\log s\), but the intervening odd lengths remain exactly zero forever.

## Relation to prior literature

General failure of spectral-radius-product convergence is not new. Martínez Ramos (2026) reviews that Morris proved the almost-everywhere formula
\[
\limsup_{n\to\infty}\frac1n\log\rho(A^{(n)}(x))=\lambda_1
\]
for general linear cocycles, following an earlier \(SL(2,\mathbb R)\) result of Avila and Bochi, and explicitly notes that the full limit may fail. Martínez Ramos then proves actual convergence under additional strong-irreducibility and Lyapunov-gap hypotheses for locally constant cocycles over mixing subshifts. Thus the general nonconvergence phenomenon and the need for additional assumptions are established prior art.

The contribution here is narrower: an explicit smooth source-specific counterexample to the unrestricted convergence statement in arXiv:2609.18017v1, with exact even/odd values, a strict Lyapunov gap, genuinely non-normal tangent maps, exact singular-value growth, and a smooth conjugacy showing that the proposed finite-horizon spectral-radius diagnostic is not coordinate invariant.

## Consequences for the source claim

The numerical observations in arXiv:2609.18017v1 are not contradicted: its reported systems may well have \(h_L\) approaching \(\lambda_1\) over the tested horizons. The correction is to the general statement that this behavior follows from Oseledets alignment alone. A convergence theorem for spectral-radius products requires additional hypotheses that prevent persistent endpoint cancellation, as reflected in the existing cocycle literature.

For a coordinate-invariant asymptotic diagnostic, the singular-value/norm rate
\[
L^{-1}\log\sigma_{\max}(P_L)
\]
has the standard Oseledets limit under the usual integrability assumptions. Spectral-radius products can remain useful finite-horizon, coordinate-specific observables, but they should not be identified with a universally convergent Lyapunov approximation without further conditions.

## Verification

`artifacts/verify_spectral_radius_cocycle.py` independently evaluates the telescoping product, spectral radii, singular-value rates, non-normality, and the conjugacy for \(s=2\) over representative horizons. `artifacts/verification.txt` records the output. The theorem itself is algebraic and does not depend on floating-point computation.

## Limitations

This result does not challenge the source paper's numerical Hénon or Ikeda calculations, its finite-horizon separation statistic as an empirical observable in a fixed coordinate system, or its chaos-control experiments. It only invalidates an unrestricted mathematical convergence claim and the stated Oseledets-eigenvector justification. It also does not classify the weakest sufficient hypotheses under which the source's \(h_L\) does converge.

## References

1. D. Sornette, V. R. Saiprasad, V. Troude, *A New Route to Chaos through the Geometric Composition of Non-Normal Amplification*, arXiv:2609.18017v1 (2026). https://arxiv.org/abs/2609.18017v1
2. N. Martínez Ramos, *Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles*, International Mathematics Research Notices 2026, rnag038; arXiv:2507.19624v2. https://arxiv.org/abs/2507.19624v2
3. I. D. Morris, *The generalised Berger-Wang formula and the spectral radius of linear cocycles*, Journal of Functional Analysis 262 (2012), 811–824.
4. A. Avila, J. Bochi, *A formula with some applications to the theory of Lyapunov exponents*, Israel Journal of Mathematics 131 (2002), 125–137.
