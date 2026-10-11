# Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius
## Finding
Let \(T\neq0\) be a rank-one operator on a complex Hilbert space. Define the normalized overlap
\[
r=\frac{|\operatorname{tr}T|}{\|T\|}\in[0,1].
\]
For the \(L^2\)-Cartesian numerical radius
\[
\omega_2(T)=\left(\frac1{2\pi}\int_0^{2\pi}\|\cos\theta\,H+\sin\theta\,K\|^2\,d\theta\right)^{1/2},
\qquad T=H+iK,
\]
one has
\[
\omega_2(T)^2=\|T\|^2\left(\frac14+\frac{r\sqrt{1-r^2}+\arcsin r}{2\pi}\right).
\]
The classical rank-one numerical-radius identity gives
\[
\omega(T)=\frac{\|T\|+|\operatorname{tr}T|}2=\frac{\|T\|(1+r)}2,
\]
so
\[
\frac{\omega_2(T)}{\omega(T)}=
\frac{\sqrt{1+\frac2\pi\left(r\sqrt{1-r^2}+\arcsin r\right)}}{1+r}.
\]
At \(r=0\), equivalently \(T^2=0\), the formula gives \(\omega_2(T)=\omega(T)=\|T\|/2\). At \(r=1\), equivalently \(T\) is rank-one normal, it gives \(\omega_2(T)=\omega(T)/\sqrt2=\|T\|/\sqrt2\). Hence rank-one operators already realize both sharp constants in the general comparison \(\omega(T)/\sqrt2\le\omega_2(T)\le\omega(T)\).

## Assumptions and scope
The Hilbert space is complex and \(T\) is nonzero and rank one. The trace is therefore well-defined. The claim concerns the specific \(L^2\)-Cartesian numerical radius introduced in arXiv:2610.04844v1. No assertion is made for higher-rank operators, for other \(q\)- or \(\rho\)-numerical radii, or for a classification of equality cases beyond rank one.

## Proof
Write \(\alpha=\|T\|\). The focal source proves absolute homogeneity, invariance under multiplication by unimodular scalars, and unitary similarity invariance of \(\omega_2\). A rank-one Schur reduction therefore puts \(T\), on the at-most-two-dimensional reducing span supporting \(T\) and \(T^*\), into the form
\[
T=\alpha
\begin{pmatrix}
r&\sqrt{1-r^2}\\
0&0
\end{pmatrix}
\oplus0,
\qquad 0\le r\le1.
\]
Indeed the nonzero singular value is \(\alpha\), the trace has modulus \(\alpha r\), and a scalar phase followed by a diagonal unitary makes the displayed entries nonnegative.

For
\[
A_\theta=\cos\theta\,H+\sin\theta\,K=\operatorname{Re}(e^{-i\theta}T),
\]
the nonzero block is
\[
A_\theta=\frac{\alpha}2
\begin{pmatrix}
2r\cos\theta&\sqrt{1-r^2}e^{-i\theta}\\
\sqrt{1-r^2}e^{i\theta}&0
\end{pmatrix}.
\]
Its two eigenvalues are
\[
\lambda_\pm(\theta)=\frac{\alpha}2\left(r\cos\theta\pm\sqrt{1-r^2\sin^2\theta}\right).
\]
Since \(\sqrt{1-r^2\sin^2\theta}\ge |r\cos\theta|\),
\[
\|A_\theta\|=\frac{\alpha}2\left(\sqrt{1-r^2\sin^2\theta}+r|\cos\theta|\right).
\]
Squaring gives
\[
\|A_\theta\|^2=\frac{\alpha^2}4\left(1+r^2\cos(2\theta)+2r|\cos\theta|\sqrt{1-r^2\sin^2\theta}\right).
\]
The \(\cos(2\theta)\) term has mean zero. By quarter-period symmetry and the substitution \(u=\sin\theta\),
\[
\frac1{2\pi}\int_0^{2\pi}|\cos\theta|\sqrt{1-r^2\sin^2\theta}\,d\theta
=\frac2\pi\int_0^1\sqrt{1-r^2u^2}\,du.
\]
For \(r>0\),
\[
\int_0^1\sqrt{1-r^2u^2}\,du
=\frac12\sqrt{1-r^2}+\frac{\arcsin r}{2r},
\]
and the \(r=0\) case is its continuous limit. Substitution into the defining average yields
\[
\omega_2(T)^2=\frac{\alpha^2}4\left(1+\frac2\pi\left(r\sqrt{1-r^2}+\arcsin r\right)\right),
\]
which is the asserted formula.

The standard rank-one identity \(\omega(T)=(\|T\|+|\operatorname{tr}T|)/2\) then gives the displayed ratio. Finally, for rank one, \(T^2=(\operatorname{tr}T)T\), so \(r=0\) is equivalent to nilpotence. Also \(r=1\) is equality in Cauchy--Schwarz for a rank-one factorization, hence exactly the normal rank-one case up to a scalar phase. The endpoint values follow directly.

## Verification
The proof reduces the entire problem to a Hermitian \(2\times2\) matrix, computes its two eigenvalues exactly, and evaluates one elementary integral. The endpoint \(r=1\) agrees with the focal paper's self-adjoint equality after a unimodular scalar rotation. The endpoint \(r=0\) satisfies the focal paper's anticommuting equal-square Cartesian-part condition, so it agrees with its upper-equality mechanism. The formula also remains within the focal sharp interval for all \(r\in[0,1]\).

No finite enumeration or numerical experiment is used as proof. The only external formula used after the integral calculation is the classical rank-one identity for \(\omega(T)\), which is explicitly recorded in arXiv:2503.05036v1, equation (1.2), and is not needed for the primary formula for \(\omega_2(T)\).

## Relationship to prior work
Audeh, Moradi, and Sahoo introduce \(\omega_2\), prove its invariances, and establish the sharp global comparison \(\omega(T)/\sqrt2\le\omega_2(T)\le\omega(T)\). Their full text contains no rank-one specialization. Their lower sharpness example is the full self-adjoint class, while their upper sharpness example is a particular anticommuting Cartesian pair; neither yields the interior rank-one dependence on \(r\).

Denčić, Stanković, Krstić, and Damnjanović give an exact rank-one formula for the different \(q\)-numerical radius and record the classical rank-one formula for \(\omega\). That result optimizes a two-vector constraint rather than averaging operator norms of rotated real parts, so it does not imply the integral formula above. Searches using the aliases “rank-one”, “overlap”, “root mean square”, “integral numerical radius”, and the exact \(L^2\)-Cartesian name did not locate an implication-equivalent prior statement.

## Limitations
The result is confined to rank-one operators. It does not claim that normalized trace controls \(\omega_2\) at higher rank, and it does not classify all higher-rank equality cases in the focal global inequality. The literature search cannot exclude every unindexed older formulation under different terminology; the strongest residual originality risk is an equivalent rank-one calculation hidden in broader numerical-radius literature without the new \(L^2\)-Cartesian name.

## References
1. W. Audeh, H. R. Moradi, S. Sahoo, “The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators,” arXiv:2610.04844v1, 2026.
2. D. Denčić, H. Stanković, M. Krstić, I. Damnjanović, “\(q\)-numerical radius of rank-one operators and the generalized Buzano inequality,” arXiv:2503.05036v1, 2025.
