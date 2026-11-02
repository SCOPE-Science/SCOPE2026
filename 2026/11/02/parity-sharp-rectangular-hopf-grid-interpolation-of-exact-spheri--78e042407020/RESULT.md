# Parity-sharp rectangular Hopf-grid interpolation of exact spherical harmonics

## Finding
Fix \(s=e^{-1}\) and embed a flat Hopf torus in the unit three-sphere by
\[
X_{N,M,s}=\left\{\left(\sqrt{s}\,e^{2\pi ia/N},\sqrt{1-s}\,e^{2\pi ib/M}\right):0\le a<N,\ 0\le b<M\right\}\subset S^3\subset\mathbb C^2.
\]
For every integer \(k\ge0\), evaluation of the **exact-degree** spherical harmonics \(\mathcal H_k(S^3)\) on this rectangular grid is injective if and only if, for **each** \(T=N,M\),
\[
\boxed{\bigl(T\text{ odd and }T\ge k+1\bigr)\ \text{or}\ \bigl(T\text{ even and }T>2k\bigr).}
\]
Consequently, among all rectangular root-of-unity grids on this one fixed torus, the minimum number of sites is
\[
\boxed{\begin{cases}(k+1)^2&k\text{ even},\\(k+2)^2&k\text{ odd},\end{cases}}
\]
achieved uniquely in the grid-size parameters at \(N=M=k+1\) for even \(k\), or \(N=M=k+2\) for odd \(k\). For even degree the count exactly equals \(\dim\mathcal H_k(S^3)=(k+1)^2\): no angular oversampling is needed. For odd degree there is a sharp one-step penalty in each angular direction. The entire assertion also holds at every radius whose squared first-coordinate radius lies outside an explicit countable set of algebraic numbers.

## Assumptions and scope
The vector space \(\mathcal H_k(S^3)\) is the complexification of the restrictions of homogeneous degree-\(k\) harmonic polynomials on \(\mathbb R^4\). The positive integers \(N,M\) may equal one, and \(k=0\) is included. Points in the grid are distinct for every \(s\in(0,1)\). Unisolvent means that the only degree-\(k\) harmonic vanishing at every grid point is zero. No statement is made about arbitrary irregular point sets or recovery of mixed-degree polynomials.

For \(k\ge0\) put
\[
\mathcal W_k=\left\{(u,v)\in\mathbb Z^2:|u|+|v|\le k,\ k-|u|-|v|\in2\mathbb Z_{\ge0}\right\}.
\]
Its cardinality is exactly \((k+1)^2\). For \((u,v)\in\mathcal W_k\), let \(\alpha=|u|\), \(\beta=|v|\), \(m=(k-\alpha-\beta)/2\), and \(c_0=1\). Define rational coefficients recursively by
\[
c_{a+1}=-c_a\frac{(m-a)(m-a+\beta)}{(a+1)(a+1+\alpha)},\qquad0\le a<m,
\]
and the radial polynomial
\[
Q_{k,u,v}(s)=\sum_{a=0}^m c_a s^a(1-s)^{m-a}.
\]
The exceptional radius set is the union, over all degrees and weights, of the roots in \((0,1)\) of these nonzero polynomials; it is countable and algebraic.

## Proof
Write \(z_1=x_1+ix_2\), \(z_2=x_3+ix_4\). For every \((u,v)\in\mathcal W_k\) construct the homogeneous polynomial
\[
H_{u,v}(z_1,z_2)=z_1^{u_+}\overline z_1^{u_-}z_2^{v_+}\overline z_2^{v_-}\sum_{a=0}^m c_a|z_1|^{2a}|z_2|^{2(m-a)},
\]
where \(u_+=\max(u,0)\), \(u_-=\max(-u,0)\), and analogously for \(v\). Using \(\Delta=4(\partial_{z_1}\partial_{\overline z_1}+\partial_{z_2}\partial_{\overline z_2})\), the coefficient of \(|z_1|^{2a}|z_2|^{2(m-1-a)}\) in the harmonicity equation is
\[
c_{a+1}(a+1)(a+1+\alpha)+c_a(m-a)(m-a+\beta).
\]
It vanishes by the stated recurrence. Distinct \((u,v)\) are distinct angular weights for the \(U(1)\times U(1)\) action and hence give linearly independent polynomials. The number of weights is \((k+1)^2=\dim\mathcal H_k(S^3)\), so these form a basis.

On the torus at squared radius \(s\), each basis vector restricts to
\[
H_{u,v}\bigl(\sqrt{s}e^{i\theta},\sqrt{1-s}e^{i\phi}\bigr)
=s^{\alpha/2}(1-s)^{\beta/2}Q_{k,u,v}(s)e^{i(u\theta+v\phi)}.
\]
Because \(Q_{k,u,v}(0)=1\), every radial polynomial is nonzero with rational coefficients. The transcendence of \(e^{-1}\) therefore implies \(Q_{k,u,v}(e^{-1})\ne0\) simultaneously for every degree and every weight. On the rectangular grid, distinct residue classes of \((u,v)\bmod(N,M)\) give orthogonal discrete Fourier characters, while colliding classes give proportional columns. It follows that
\[
\operatorname{rank} E_{k,N,M,s}=\#\bigl(\mathcal W_k\bmod(N,M)\bigr)
\]
whenever the radial amplitudes are nonzero. At arbitrary \(s\in(0,1)\), the rank is the number of residue classes containing at least one weight with \(Q_{k,u,v}(s)\ne0\).

For necessity of the grid-size criterion, take the \(k+1\) weights \((u,0)\) with \(u=-k,-k+2,\ldots,k\). They must be distinct modulo \(N\). The sequence has period \(N\) for odd \(N\) and period \(N/2\) for even \(N\), forcing \(N\ge k+1\) when odd, or \(N\ge2(k+1)\) when even. Similarly, weights \((0,v)\) force the same condition for \(M\).

Conversely, suppose both conditions hold. For any two weights, \(|\Delta u|+|\Delta v|\le2k\) and \(\Delta u+\Delta v\) is even. If \(N\) is even and \(N>2k\), a congruence \(\Delta u\equiv0\pmod N\) forces \(\Delta u=0\); the analogous statement holds for even \(M\). If both periods are odd, a nonzero congruent difference in exactly one coordinate would have to be an **even** multiple of the corresponding period and therefore have magnitude at least \(2(k+1)>2k\). If both coordinate differences are nonzero, their total absolute size is at least \(N+M\ge2(k+1)>2k\). These contradictions prove injectivity. The same argument covers mixed odd/even periods. Minimizing the two independent grid sizes yields the two sharp point counts.

## Verification
The self-contained program `verify.py` checks the harmonic recurrence with exact rational arithmetic for degrees through twelve, exhaustively compares the all-parameter residue criterion over a bounded integer mesh, and reconstructs seventeen selected evaluation matrices over exact finite fields. The reproduced certificate is `HOPF_GRID_CHECK_OK 5385 exact assertion groups 17 independent finite-field matrix ranks`. The proof of the theorem, including infinitely many degrees and radii, is analytic; the finite checks do not certify the infinite quantifiers. A rational test radius in the checker is used only for bounded numerical/algebraic corroboration, not in place of the transcendental radius required for the universal assertion.

## Relationship to prior work
Ben Achour, Huguet, Queva and Renaud (arXiv:1505.03426, first submitted 2015-05-13) recall the separated scalar three-sphere harmonics in Hopf coordinates in Section II, equation (3), and use these modes to construct one-form eigenmodes. The **separated harmonics and Jacobi factors themselves are not new**. The contribution here is an exact all-degree classification of finite *rectangular root-of-unity sampling* on one fixed nonresonant torus, including the parity-sensitive necessary-and-sufficient Nyquist conditions and the optimal point counts. The inspected article does not state such a grid theorem. Previously known sampling results on circles or other spherical configurations are geometrically different and do not immediately imply this two-dimensional product-grid criterion.

## Limitations
This is a claim about exact-degree harmonic spaces, **not** the whole low-pass band \(\bigoplus_{j=0}^k\mathcal H_j(S^3)\). A single torus is not unisolvent for the low-pass space once \(k\ge2\), because a nonzero polynomial of degree at most two vanishes identically on any fixed torus. The ordinary balanced Clifford torus at \(s=1/2\) is not universally nonresonant: for example, an exact-degree-two harmonic vanishes on it, so no sampling grid there can recover every degree-two harmonic. The algebraic exceptional-radius sets are not classified individually. No stability/optimal condition number is claimed; full column rank can coexist with poor numerical conditioning. The novelty assessment is limited to accessible literature and may miss an equivalent statement under other interpolation terminology. Independent mathematical validation has not been performed.

## References
- J. Ben Achour, E. Huguet, J. Queva and J. Renaud, *Explicit vector spherical harmonics on the 3-sphere*, arXiv:1505.03426v1 (2015-05-13); Section II records the scalar Hopf-coordinate modes. https://arxiv.org/abs/1505.03426 and https://arxiv.org/html/1505.03426v2.
