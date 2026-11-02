# A universal boundary-jet law for noncommuting radial poly-Bergman Toeplitz operators

## Finding
For every \(\alpha>-1\), the leading noncommutativity of two smooth radial multipliers compressed to the full bianalytic weighted Bergman space is determined by a **single antisymmetric boundary two-jet**. Write
\[
\Delta(f,g)=f'(1)g''(1)-f''(1)g'(1),\qquad
c_{\alpha,f,g}=(\alpha+2)\sqrt{\alpha+1}\,|\Delta(f,g)|.
\]
If \(\Delta(f,g)\ne0\), the ordered singular values of their Toeplitz commutator satisfy
\[
\boxed{\lim_{j\to\infty}j^3s_j([T_f,T_g])=8c_{\alpha,f,g}.}
\]
Consequently \([T_f,T_g]\in\mathcal S_p\) precisely for \(p>1/3\), for all real \(p>0\). At the critical weak-Schatten endpoint,
\[
\boxed{\lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^{N}s_j([T_f,T_g])^{1/3}=2c_{\alpha,f,g}^{1/3}.}
\]
Here \(s_j\) are singular values listed nonincreasingly with multiplicities. For \(f(t)=t\) and \(g(t)=t^2\) the singular values are given exactly by an explicit rational-square-root formula at **every** Fourier frequency.

## Assumptions and scope
Fix \(\alpha>-1\) and normalized weighted area measure
\[
 d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z),\qquad z\in\mathbb D.
\]
Let \(\mathcal A_2^2=\{u\in L^2(\mu_\alpha):\bar\partial^2u=0\}\), the **full** order-two polyanalytic Bergman space, not its true-order-two orthogonal summand. Let \(P_2\) be orthogonal projection onto this closed space. For \(f,g\in C^3([0,1];\mathbb C)\), define \(T_f=P_2M_{f(|z|^2)}|_{\mathcal A_2^2}\) and \(T_g\) analogously. Smoothness is only needed up to order three at the boundary, but the stated theorem assumes global \(C^3\) for a simple uniform estimate. All asymptotics keep \(\alpha,f,g\) fixed. No conclusion at the sharp \(p=1/3\) boundary is asserted when \(\Delta=0\).

## Proof
**1. Fourier blocks.** The standard angular decomposition of the full bianalytic Bergman space has one one-dimensional block of angular frequency \(-1\), followed by two-dimensional blocks indexed by \(m\in\mathbb Z_{\ge0}\). In the block of frequency \(m\), the radial component consists of \(r^m\) times real polynomials of degree at most one in \(t=r^2\), with radial probability measure
\[
 d\nu_m(t)=\frac{t^m(1-t)^\alpha\,dt}{B(m+1,\alpha+1)},\quad 0<t<1.
\]
Set \(\mu_m=(m+1)/(m+\alpha+2)\), \(p_{0,m}=1\), and \(p_{1,m}=(t-\mu_m)/b_{1,m}\), where
\[
 b_{1,m}^2=\operatorname{Var}_{\nu_m}(t)=
 \frac{(\alpha+1)(m+1)}{(m+\alpha+2)^2(m+\alpha+3)}.
\]
In this orthonormal basis the compression \(F_m(f)\) of radial multiplication is the symmetric matrix with entries \(\int f(t)p_{i,m}(t)p_{j,m}(t)d\nu_m(t)\). Hence its commutator block \([F_m(f),F_m(g)]\) is skew-symmetric (transpose), even for complex symbols. The negative-frequency block commutator vanishes.

**2. Exact model commutator.** Let \(J_m=F_m(t)\). Extend the orthonormal polynomials to degree two. The Jacobi three-term recurrence for multiplication by \(t\) has positive off-diagonal coefficients \(b_{1,m}\), \(b_{2,m}\), where
\[
 b_{2,m}^2=\frac{2(\alpha+2)(m+2)(m+\alpha+2)}{(m+\alpha+4)^2(m+\alpha+3)(m+\alpha+5)}.
\]
Equivalently, this value follows by applying Gram–Schmidt to \(1,t,t^2\) under \(\nu_m\) and evaluating beta moments. Projection of \(t^2\) onto the first two Jacobi degrees gives the exact identity
\[
 F_m(t^2)=J_m^2+b_{2,m}^2 E_{11},
\]
where \(E_{11}=\operatorname{diag}(0,1)\) in the ordered basis \((p_{0,m},p_{1,m})\). Since \((J_m)_{01}=b_{1,m}>0\),
\[
 [F_m(t),F_m(t^2)]
 =b_{1,m}b_{2,m}^2
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Both singular values of this block equal \(b_{1,m}b_{2,m}^2\), exactly. The rational formulas yield
\[
 \lim_{m\to\infty}m^3b_{1,m}b_{2,m}^2
 =2(\alpha+2)\sqrt{\alpha+1}.
\]

**3. Uniform Taylor remainder.** Taylor expansion at \(t=1\) gives
\[
 f(t)=f(1)+f'(1)(t-1)+\tfrac12f''(1)(t-1)^2+R_f(t),
 \qquad |R_f(t)|\le C_f(1-t)^3.
\]
For any fixed integer \(q\ge0\), direct beta moment formulas give
\[
 \mathbb E_{\nu_m}(1-t)^q
 =\frac{(\alpha+1)_q}{(m+\alpha+2)_q}=O(m^{-q}),
\]
where \((x)_q\) denotes the rising factorial. The centered formula for \(p_{1,m}\), its variance \(b_{1,m}^2\asymp m^{-2}\), and the same beta moments with powers \(q,q+1,q+2\) imply
\[
 \int(1-t)^q|p_{j,m}(t)|^2d\nu_m(t)=O(m^{-q}),\qquad j=0,1.
\]
Cauchy–Schwarz bounds the off-diagonal entries, so
\[
 \|F_m((1-t)^q)\|=O(m^{-q}),\quad
 \|F_m(R_f)\|=O(m^{-3}),
\]
and likewise for \(g\). In particular \(F_m(t)-I=O(m^{-1})\), and \(F_m((t-1)^2)=O(m^{-2})\). Expanding both compressed Taylor polynomials in their commutator, scalar terms cancel, and any term involving a remainder has norm \(O(m^{-4})\), because the other nonscalar factor is \(O(m^{-1})\). Thus
\[
 [F_m(f),F_m(g)]
 =\frac{\Delta(f,g)}2[F_m(t),F_m(t^2)]+O(m^{-4}).
\]
The exact model limit in Step 2 therefore proves
\[
 m^3[F_m(f),F_m(g)]\longrightarrow
 (\alpha+2)\sqrt{\alpha+1}\,\Delta(f,g)
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

**4. Singular values and the endpoint.** Every two-by-two complex skew-symmetric block has two identical singular values. When \(\Delta\ne0\), each high-frequency block contributes two values \(c_{\alpha,f,g}m^{-3}(1+O(m^{-1}))\). The finite initial blocks, including frequency \(-1\), do not affect the tail. Counting with multiplicity gives \(N(\tau)\sim2(c_{\alpha,f,g}/\tau)^{1/3}\) as \(\tau\downarrow0\), hence \(j^3s_j\to8c_{\alpha,f,g}\). Summing powers now yields \(\sum s_j^p<\infty\) if and only if \(3p>1\); at equality \(s_j^{1/3}\sim(8c_{\alpha,f,g})^{1/3}j^{-1}\), giving the claimed logarithmic constant. For \(f(t)=t\) and \(g(t)=t^2\), \(\Delta=2\ne0\), so the threshold is attained by a concrete polynomial pair. This completes the proof.

## Verification
The accompanying `CHECK.py` uses order-three Gauss–Jacobi quadrature to compute exact polynomial Toeplitz blocks by a route distinct from the closed recurrence coefficient formulas. It tests 35 parameter/frequency pairs, three commutator identities per pair, 10 large-frequency asymptotic checks and six further checks for a nonmonomial polynomial-symbol pair; 121 assertions pass. Run `python CHECK.py` with NumPy and SciPy installed. Numerical checks are finite and corroborative; the proof above supplies the infinite-dimensional statements.

## Relationship to prior work
Vasilevski's 2023 study of poly-Bergman space structures (primary MSC including `30H20`) motivates the underlying polyanalytic Hilbert-space setting. Barrera-Castelán, Maximenko, and Ramos-Vazquez (2020/2023) derive the radial Jacobi matrix model and the scalar boundary limit/C*-algebra description. The present result **uses** that existing block model; it does not claim discovery of radial decomposition or the Jacobi recurrence. The new asserted information is the universal boundary two-jet governing the precise commutator singular-value law and its optimal Schatten endpoint. The 2025 work by Shi et al. treats commutativity of certain 2-analytic Toeplitz families and was accessible only at abstract level; it remains a historical-priority risk, not a source claimed to exclude a potentially equivalent result.

## Limitations
The theorem concerns the full order-two space, not arbitrary polyanalytic order and not true-order-two alone. It requires \(C^3\) radial symbols and \(\Delta\ne0\) for the two-sided asymptotics; additional cancellation may occur when the determinant vanishes. It does not give uniform bounds as \(\alpha\) or the symbols vary, nor nonradial analogues. A literature search cannot establish historical uniqueness, and independent mathematical validation has not been performed.

## References
1. N. Vasilevski, *On Polyanalytic Functions in Several Complex Variables*, Complex Analysis and Operator Theory **17**, 80 (first public 14 July 2023), DOI: 10.1007/s11785-023-01386-0.
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces*, arXiv:2306.06231 (first posted 9 June 2023), DOI: 10.1007/s11785-024-01509-1.
3. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, arXiv:2009.14301 (first posted 29 September 2020), DOI: 10.1007/s40590-021-00348-w.
4. Y. Shi, Y. Li, B. Zhang, Y. Lu, *Commuting Toeplitz Operators on the 2-analytic Bergman Space*, Acta Mathematica Sinica **41** (2025), 1855–1867, DOI: 10.1007/s10114-025-3195-5.
