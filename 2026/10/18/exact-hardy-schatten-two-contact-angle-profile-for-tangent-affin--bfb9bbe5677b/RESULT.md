# Exact Hardy Schatten-two contact-angle profile for tangent affine composition products

## Finding
Let \(H^2(\mathbb D)\) be the classical Hardy Hilbert space. For \(0<a,b<1\) and \(|u|=|v|=|\xi|=|\eta|=1\), put
\[
\varphi(z)=u(1-a+a\xi z),\qquad \psi(z)=v(1-b+b\eta z),\qquad T=C_\varphi C_\psi^*.
\]
The image disks of these nonconstant affine self-maps are internally tangent to the unit circle at \(u\) and \(v\), respectively. Choose \(\delta\in[-\pi,\pi]\) such that \(u\overline v=e^{i\delta}\). If \(\delta\ne0\), then the *exact* squared Hilbert--Schmidt norm is
\[
\boxed{\|T\|_{\mathcal S_2}^{2}=
\frac{1}{4\sqrt{(1-a)(1-b)}\,|\sin(\delta/2)|\sqrt{ab+(1-a)(1-b)\sin^2(\delta/2)}}.}
\]
If \(\delta=0\), then \(T\notin\mathcal S_2\). Thus the boundary-contact collision is an exact singularity. For each fixed \(a,b\), the squared norm is strictly decreasing as \(|\delta|\) rises through \((0,\pi]\); its unique angular minimum is attained at antipodal contacts \(u=-v\). The sharp collision coefficient is
\[
\boxed{\lim_{\delta\to0}|\delta|\,\|T\|_{\mathcal S_2}^{2}
=\frac{1}{2\sqrt{ab(1-a)(1-b)}}.}
\]
More precisely, \(|\delta|\|T\|_{\mathcal S_2}^{2}\) equals this limit plus \(O(\delta^2)\), uniformly when \(a,b\) range over a fixed compact subset of \((0,1)\).

## Assumptions and scope
The Hardy norm is \(\|f\|_{H^2}^2=\sum_{n\ge0}|f_n|^2\) for \(f(z)=\sum_{n\ge0}f_n z^n\), and \(C_\chi f=f\circ\chi\). The Schatten-two norm is \(\|S\|_{\mathcal S_2}^2=\sum_{m,n\ge0}|\langle Se_n,e_m\rangle|^2\), allowing \(+\infty\). The weights \(a,b\) are strictly between zero and one; no endpoint statement about constant or automorphic symbols is asserted. The maps above exhaust all proper affine disk self-maps whose image disks touch the unit circle internally. The source image contacts are allowed to coincide; input contact points \(\overline\xi,\overline\eta\) are arbitrary.

## Proof
**Unitary reduction.** Each rotation-composition operator \(U_\xi f(z)=f(\xi z)\) is unitary on \(H^2\). Writing \(\varphi_0(z)=u(1-a+az)\) and \(\psi_0(z)=v(1-b+bz)\) yields \(C_\varphi=U_\xi C_{\varphi_0}\) and \(C_\psi=U_\eta C_{\psi_0}\). Consequently \(C_\varphi C_\psi^*=U_\xi(C_{\varphi_0}C_{\psi_0}^*)U_\eta^*\). Simultaneous rotation of both output symbols changes the associated two-variable kernel by a harmless unimodular change of phase; the norm therefore depends only on \(u\overline v\), and we can put \(u=1\) and \(v=e^{-i\delta}\) (the sign choice is immaterial).

**Kernel and two circle integrals.** The Hardy Szegő kernel is \(k_w(z)=(1-\overline w z)^{-1}\), and \(C_\psi^*k_w=k_{\psi(w)}\). Thus the two-variable coefficient kernel of \(T\) is
\[
K_T(z,w)=\frac1{1-\varphi(z)\overline{\psi(w)}}.
\]
Parseval in both variables gives the identity, with the value \(+\infty\) permitted,
\[
\|T\|_{\mathcal S_2}^2=\frac1{(2\pi)^2}\int_{-\pi}^{\pi}\int_{-\pi}^{\pi}
\frac{ds\,dt}{|1-\varphi(e^{it})\overline{\psi(e^{is})}|^2}.
\tag{1}
\]
This follows first at radial radii less than one by coefficient Parseval and then by monotone convergence of the nonnegative coefficient sums. For distinct output contacts, the denominator has a strictly positive minimum on the closed torus, so ordinary boundary Parseval applies directly. For coincident contacts, Fatou's lemma provides the infinite-value implication used below.

Write \(p(t)=1-a+ae^{it}\), and, with \(v=e^{-i\delta}\), put
\[
A(t)=1-(1-b)e^{i\delta}p(t),\qquad B(t)=b e^{i\delta}p(t).
\]
For \(\delta\ne0\), \(|A(t)|>|B(t)|\) for every real \(t\). Indeed, equality would force the two image disks to have a common point on the unit circle, whereas their distinct tangencies exclude this. Integrating the \(s\)-variable with the geometric-series/Poisson identity gives
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|A(t)-B(t)e^{-is}|^{-2}\,ds
=\bigl(|A(t)|^2-|B(t)|^2\bigr)^{-1}.
\]
The denominator is \(C+P\cos t+Q\sin t\), where
\[
\begin{aligned}
C&=1-2(1-a)(1-b)\cos\delta+(1-2b)((1-a)^2+a^2),\\
P&=2a((1-2b)(1-a)-(1-b)\cos\delta),\\
Q&=2a(1-b)\sin\delta.
\end{aligned}
\]
Changing the sign of \(\delta\) changes the sign of \(Q\) without affecting the norm. The elementary circle integral is
\[
\frac1{2\pi}\int_{-\pi}^{\pi}(C+P\cos t+Q\sin t)^{-1}\,dt
=\frac1{\sqrt{C^2-P^2-Q^2}},
\]
and expansion yields the *exact factorization*
\[
C^2-P^2-Q^2=4(1-a)(1-b)(1-\cos\delta)
\bigl(2ab+(1-a)(1-b)(1-\cos\delta)\bigr).
\tag{2}
\]
Combining (1)--(2) and \(1-\cos\delta=2\sin^2(\delta/2)\) proves the boxed norm formula.

**Collision and sharp angle law.** If \(\delta=0\), the singly integrated denominator is
\[
|A(t)|^2-|B(t)|^2=2a(a+b-2ab)(1-\cos t),
\]
whose reciprocal is not integrable near \(t=0\), proving \(T\notin\mathcal S_2\). When \(\delta\ne0\), the boxed formula is the reciprocal of a strictly increasing function of \(|\sin(\delta/2)|\) for \(|\delta|\in(0,\pi]\); thus the angular minimum and uniqueness follow. Finally, \(|\sin(\delta/2)|=|\delta|/2+O(|\delta|^3)\) and the remaining radical has a nonzero limit \(\sqrt{ab}\). This establishes the sharp coefficient and its locally uniform quadratic correction.

## Verification
The standalone `check.py` recomputes the two-variable boundary kernel integral by independent numerical quadrature, checks the one-variable Poisson-reduced integral against the radical, checks symmetry under interchange of \(a\) and \(b\), and tests the collision coefficient for decreasing \(|\delta|\). Run `python check.py` with NumPy installed. These finite diagnostics cannot establish the universal formula; the proof is the Parseval--Poisson calculation and factorization (2).

## Relationship to prior work
He, Yan, Zhang, and Zhao [1, Theorem 3.4] establish the all-Schatten versus noncompact dichotomy for products with linear-fractional symbols on weighted Dirichlet spaces, in particular the role of image-contact separation. Leng and Zhao [2, Section 3.3, Theorem 3.18 and Remark 3.19] provide Hilbert--Schmidt integrability criteria and trace-related representations for general Hardy composition products. These establish qualitative membership and generic integral conditions, not the above fully evaluated squared norm, angular monotonicity, or sharp contact-collision coefficient. The reproducing-kernel/Parseval identity used here is standard and is not itself claimed as new. Clifford and Zheng [3] provide earlier Hardy-space compactness background. No priority assertion is made beyond the explicit comparison of accessible results.

## Limitations
The exact formula is established only for affine disk self-maps with a single boundary tangency and strict radii in \((0,1)\); it does not cover general linear fractional maps, multiply contacting symbols, or the opposite product order. The \(\mathcal S_2\) collision divergence does not by itself quantify other Schatten norms. The older article [3] could not be inspected in complete text, leaving a nonzero risk of an equivalent prior computation. No independent validation has been performed.

## References
[1] L. He, Y. Yan, S. Zhang, X. Zhao, *Some Properties of Products of Linear Fractional Composition Operators on Weighted Dirichlet Spaces*, arXiv:2609.29897 (first publicly posted 2026-09-24), especially Theorem 3.4. https://arxiv.org/abs/2609.29897

[2] Q. Leng, X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472 (first publicly posted 2026-10-11), especially Section 3.3. https://arxiv.org/abs/2610.15472

[3] J. H. Clifford, D. Zheng, *Composition operators on the Hardy space*, Indiana Univ. Math. J. **48** (1999), 1585--1616. Complete text not inspected.
