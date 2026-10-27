# Exact angular stability frontier of a planar mismatched primal–dual iteration

## Finding
Consider the constant-step primal-first Chambolle–Pock iteration on two-dimensional strongly convex quadratics, with an exact forward operator and a rotationally mismatched backward operator. There is a **sharp angular stability boundary**, not determined by the mismatch norm alone. For equal primal and dual step sizes \(t>0\) and rotation angle \(\theta\in[-\pi,\pi]\), define
\[
H(t)=\frac{2t^4-6t^2-8t-3}{(2t+1)^2},\qquad
\varphi=\frac{1+\sqrt5}{2},\qquad T=1+\sqrt3.
\]
The iteration converges geometrically to the origin **from every initial state** precisely in the following regimes:

1. \(0<t\le\varphi\), with \(\theta\not\equiv\pi\pmod{2\pi}\);
2. \(\varphi<t<T\), with \(\cos\theta>H(t)\).

For \(t\ge T\), no rotation yields convergence to the origin from every initial state. At the antipodal rotation \(\theta\equiv\pi\pmod{2\pi}\), the update always has an eigenvalue equal to one; for the other boundary angles \(\cos\theta=H(t)\), the spectral radius is also exactly one. Away from these boundaries and the strict-stability region the spectral radius is strictly larger than one.

The frontier is an increasing function of \(t\), passes through \(-1\) at the golden ratio \(\varphi\), and passes through \(+1\) at \(T\). For example, at \(t=2\) the exact crossover is \(\cos\theta=-11/25\): a right-angle mismatch converges, whereas a \(120^\circ\) mismatch diverges for suitable initial conditions. The usual sufficient restriction \(t<1\) for the matched, non-strongly-convex general setting does not describe this exact quadratic stability domain.

## Assumptions and scope
Work in \(X=Y=\mathbb R^2\). Let \(G(x)=\frac12\|x\|_2^2\) and \(F^*(y)=\frac12\|y\|_2^2\). The forward linear operator is \(A=I_2\), and the implemented adjoint is \(V^*=R_{-\theta}\), where \(R_{\theta}\) is the planar rotation through angle \(\theta\). The step sizes are \(\tau=\sigma=t>0\), and extrapolation is \(\omega=1\). Both proximal steps are evaluated exactly, giving
\[
x_{n+1}=\frac{x_n-tR_{-\theta}y_n}{1+t},\qquad
y_{n+1}=\frac{y_n+t(2x_{n+1}-x_n)}{1+t},\quad n\ge0.
\]
No noise, forcing, restarts, finite-precision effects, or varying parameters are included. "Converges from every initial state" means \((x_n,y_n)\to(0,0)\) for all \((x_0,y_0)\in\mathbb R^4\), equivalently that the real \(4\times4\) update matrix has spectral radius strictly below one. Rotation angles are identified modulo \(2\pi\). The original matched saddle objective is strongly convex–concave with its unique saddle at the origin. At the antipodal mismatch the discrete fixed-point set is not reduced to the origin.

## Proof
Write \(u=(1+t)^{-1}\). The real iteration matrix in block form is
\[
B=\begin{pmatrix}
u I_2&-utR_{-\theta}\\ut(2u-1)I_2&uI_2-2u^2t^2R_{-\theta}\end{pmatrix}.
\]
Identify \(\mathbb R^2\) with \(\mathbb C\), so that \(R_{-\theta}\) becomes multiplication by \(z=e^{-i\theta}\) (\(|z|=1\)). The real spectrum is the union of the spectra of the complex matrix
\[
B_z=\begin{pmatrix}u&-ut z\\ut(2u-1)&u-2u^2t^2z\end{pmatrix}
\]
and its conjugate. The characteristic polynomial is \(\lambda^2-P\lambda+Q\), where
\[
P=2u-2u^2t^2z,\qquad Q=u^2(1-t^2z).
\]
For a monic complex quadratic \(\lambda^2-P\lambda+Q\), the strict Schur criterion is
\[
|Q|<1,\qquad |P-\overline P Q|<1-|Q|^2.
\]
This is the degree-two Schur reduction: subtract \(Q\) times the reversed conjugate polynomial, leaving \(\lambda[(1-|Q|^2)\lambda-(P-Q\overline P)]\), and apply the standard disk-root recursion.

Set \(c=\cos\theta=(z+z^{-1})/2\). Direct expansion shows
\[
1-|Q|^2=\frac{2t\{2+(3+c)t+2t^2\}}{(1+t)^4}>0
\]
for all \(t>0\) and \(-1\le c\le1\). The difference of squares in the second Schur inequality factorizes **exactly** as
\[
(1-|Q|^2)^2-|P-\overline P Q|^2
=\frac{4t^4(1+c)}{(1+t)^8}
\left((2t+1)^2c-2t^4+6t^2+8t+3\right).
\]
Therefore, when \(c>-1\), strict stability is equivalent to \(c>H(t)\). When \(c=-1\), the factored expression vanishes; directly, \(B_z\) has eigenvalues \(1\) and \((1+t^2)/(1+t)^2\), the latter strictly between zero and one. Thus this endpoint is never strictly stable and always has spectral radius exactly one.

Differentiating and factoring gives
\[
H'(t)=\frac{4(t+1)(2t^3+1)}{(2t+1)^3}>0,
\]
\[
H(t)+1=\frac{2(t^2-t-1)(t^2+t+1)}{(2t+1)^2},
\qquad
H(t)-1=\frac{2(t+1)^2(t^2-2t-2)}{(2t+1)^2}.
\]
Hence \(H(t)\le-1\) exactly when \(0<t\le\varphi\); \(-1<H(t)<1\) exactly when \(\varphi<t<T\); and \(H(t)\ge1\) exactly when \(t\ge T\). This proves all strict-stability cases, using the equivalence between convergence from all initial states and spectral radius below one. Where \(-1<c\le1\) and \(c=H(t)\), the Schur equality and \(|Q|<1\) put one root exactly on the unit circle (and the other strictly inside); wherever \(c>-1\) and \(c<H(t)\), one root lies strictly outside it. Finally, \(H(2)=-11/25\), proving the explicit contrasting-angle example.

## Verification
Run `python verify.py` with Python, SymPy, and NumPy installed. It symbolically reconstructs the block update, its characteristic polynomial, the complete Schur factorization, both factored endpoints, and the derivative. It independently builds the real iteration matrix for a grid of step sizes and rotation angles, evaluates its eigenvalues, and compares strict contraction with the theorem. These finite checks are reproducibility aids, not substitutes for the exact polynomial argument above.

## Relationship to prior work
Lorenz and Schneppe (first arXiv posting January 13, 2022) formulated the mismatched-adjoint Chambolle–Pock iteration, proved sufficient strongly convex convergence conditions, and evaluated quadratic instances. Their convergence conditions are not presented as necessary, and they do not give the displayed sharp rotational \((t,\theta)\)-classification. Chouzenoux, Contreras, Pesquet, and Savanier (2022 preprint) studied general mismatched primal–dual algorithms with sufficient conditions and fixed-point analysis, notably modified Condat–Vũ, Loris–Verhoeven, and Combettes–Pesquet schemes; those statements do not directly specify this exact complex Schur frontier. Existing sharp tuning results for matched scalar primal–dual iterations have \(\theta=0\), and hence do not imply the angular classification. The iteration, complex Schur criterion, and classical root-stability machinery are prior mathematics: only the exact planar rotational phase boundary and its two transition thresholds are assessed here.

## Limitations
The theorem is an exact-arithmetic statement for the specified unforced quadratic and constant equal-step scheme with extrapolation one. It is not a sufficient robustness guarantee for arbitrary nonorthogonal surrogate adjoints, nonlinear proximal maps, unequal steps, or other variants of primal–dual splitting. The full stable parameter range includes some large mismatch norms only because this particular two-dimensional linear model has additional structure. The exact priority of the angular factorization relative to all specialized literature remains open to external review; no independent audit has been performed.

## References
1. D. A. Lorenz and F. Schneppe, *Chambolle–Pock's Primal-Dual Method with Mismatched Adjoint*, arXiv:2201.04928 (first posted 2022-01-13), https://arxiv.org/abs/2201.04928; *Applied Mathematics & Optimization* 87 (2023), article 22.
2. E. Chouzenoux, A. Contreras, J.-C. Pesquet, and M. Savanier, *Convergence Results for Primal-Dual Algorithms in the Presence of Adjoint Mismatch*, https://optimization-online.org/wp-content/uploads/2022/04/8877.pdf (2022 preprint); *SIAM Journal on Imaging Sciences* 16 (2023), 1–34.
3. E. Chouzenoux, J.-C. Pesquet, and F. Roldán, *Solution of Mismatched Monotone+Lipschitz Inclusion Problems*, arXiv:2310.06402 (2023), https://arxiv.org/abs/2310.06402.
