# A sharp fractional small-time energy law for a two-mode control system

## Finding

Consider the Caputo system
\[
D_C^\alpha x(t)=-\operatorname{diag}(\lambda_1,\lambda_2)x(t)+(1,1)^T u(t),\qquad x(0)=0,
\]
with fixed \(1/2<\alpha<1\), distinct \(\lambda_1,\lambda_2\ge0\), and scalar control \(u\in L^2(0,T)\). Let \(W_T\) be its minimum-energy controllability Gramian. Then, as \(T\downarrow0\),
\[
\lambda_{\max}(W_T)\sim C_+(\alpha)T^{2\alpha-1},\qquad
\lambda_{\min}(W_T)\sim C_-(\alpha,\lambda_1,\lambda_2)T^{4\alpha-1},
\]
where
\[
C_+(\alpha)=\frac{2}{\Gamma(\alpha)^2(2\alpha-1)},\qquad
C_-(\alpha,\lambda_1,\lambda_2)=\frac{(\lambda_1-\lambda_2)^2\alpha^2}{2\Gamma(2\alpha)^2(4\alpha-1)(3\alpha-1)^2}.
\]
Thus the worst-case minimum control energy over unit terminal targets is asymptotic to \(C_-^{-1}T^{-(4\alpha-1)}\). The eigenvector for the smallest Gramian eigenvalue tends to \((1,-1)^T/\sqrt2\): the common input initially excites the symmetric mode, while the antisymmetric mode is reached only through the separation of the two decay rates.

## Assumptions and scope

The fractional order is fixed in \((1/2,1)\); the endpoints are excluded. The distinct modal rates are fixed as \(T\to0\). The initial state is zero, the input is scalar and square-integrable, and the terminal target is prescribed at time \(T\). This is a two-mode finite-dimensional benchmark, not a theorem for an infinite-dimensional PDE, constrained controls, or a uniform limit as \(\alpha\downarrow1/2\) or \(\lambda_1\to\lambda_2\).

## Proof

For \(i=1,2\), set
\[
g_i(t)=t^{\alpha-1}E_{\alpha,\alpha}(-\lambda_i t^\alpha),\qquad
E_{\alpha,\alpha}(z)=\sum_{k=0}^{\infty}\frac{z^k}{\Gamma(\alpha k+\alpha)}.
\]
The endpoint map is \(u\mapsto\int_0^T(g_1(t),g_2(t))^T u(T-t)\,dt\), so
\[
W_T=\int_0^T g(t)g(t)^T\,dt,\qquad g=(g_1,g_2)^T.
\]
Since \(\alpha>1/2\), both kernel coordinates belong to \(L^2(0,T)\). For fixed rates, the convergent Mittag-Leffler series gives
\[
g_i(t)=a t^{\alpha-1}+b_i t^{2\alpha-1}+O(t^{3\alpha-1}),\quad
a=\frac1{\Gamma(\alpha)},\quad b_i=-\frac{\lambda_i}{\Gamma(2\alpha)}.
\]
The trace is therefore
\[
\operatorname{tr}W_T=\frac{2}{\Gamma(\alpha)^2(2\alpha-1)}T^{2\alpha-1}(1+o(1)).
\]
For the determinant, the leading two independent kernel shapes are \(f_0(t)=t^{\alpha-1}\) and \(f_1(t)=t^{2\alpha-1}\). Their Gram determinant is
\[
\begin{aligned}
\det\operatorname{Gram}(f_0,f_1)
&=\frac{T^{2\alpha-1}}{2\alpha-1}\frac{T^{4\alpha-1}}{4\alpha-1}-\left(\frac{T^{3\alpha-1}}{3\alpha-1}\right)^2\
&=\frac{\alpha^2 T^{6\alpha-2}}{(2\alpha-1)(4\alpha-1)(3\alpha-1)^2}.
\end{aligned}
\]
The coefficient determinant of the two leading kernel expansions is \(a(b_2-b_1)\). Higher series terms contribute only lower-order corrections. Hence
\[
\det W_T=\frac{(\lambda_1-\lambda_2)^2\alpha^2}{\Gamma(\alpha)^2\Gamma(2\alpha)^2(2\alpha-1)(4\alpha-1)(3\alpha-1)^2}T^{6\alpha-2}(1+o(1)).
\]
Because \(W_T\) is positive semidefinite, its largest eigenvalue is asymptotic to its trace, and its smallest eigenvalue is \(\det(W_T)/\lambda_{\max}(W_T)\). Dividing the two asymptotics gives the stated constant \(C_-\) and exponent \(4\alpha-1\). The leading Gramian is a positive multiple of the matrix with every entry equal to one; its null direction is antisymmetric. The smaller-eigenvalue eigenvector therefore tends to \((1,-1)^T/\sqrt2\). Finally, the minimum energy for a target \(z\) is \(z^TW_T^{-1}z\), so the supremum over \(\|z\|_2=1\) is \(1/\lambda_{\min}(W_T)\), proving the energy law.

## Verification

The coefficient identity used above is exact: \(1/[(2\alpha-1)(4\alpha-1)]-1/(3\alpha-1)^2=\alpha^2/[(2\alpha-1)(4\alpha-1)(3\alpha-1)^2]\). The determinant and trace powers are respectively \(T^{6\alpha-2}\) and \(T^{2\alpha-1}\), so their quotient has the required \(T^{4\alpha-1}\) power. The result is analytic and asymptotic; no finite numerical experiment is used as proof. It makes no claim at \(\alpha=1/2\), where the kernel is not square-integrable, or uniformly as the two rates coalesce.

## Relationship to prior work

Ge and Chen study regional tracking and control cost for time-fractional diffusion systems (arXiv:2104.12303v1, first public 26 April 2021); the accessible abstract motivates the fractional-control setting but does not state this two-mode small-time eigenvalue law. Xu, Li, and Zhou give a full-text Gramian nonsingularity criterion for fractional linear systems with different orders (The Scientific World Journal, 2014, DOI 10.1155/2014/618162), which addresses controllability equivalence rather than the asymptotic eigenvalue constants. Trélat and Zuazua's 2026 preprint on small-time controllability Gramian spectra treats classical integer-order systems and recovers the familiar \(T,T^3,\ldots\) hierarchy; it does not establish the fractional-order exponents or constants here. The present statement is restricted to fixed \(1/2<\alpha<1\), so it does not claim novelty for the classical endpoint.

## Limitations

The statement is specific to two distinct diagonal decay rates and one input with equal nonzero modal gains. It does not establish a general \(n\)-mode hierarchy, a PDE-level regional-control theorem, or a constrained-control result. A broader fractional-control source could contain an equivalent asymptotic under different notation; the full text of the 2021 motivating paper could not be accessed through the available routes, so this is a best-knowledge novelty assessment rather than an independent priority certification.

## References

1. F. Ge and Y. Chen, “Optimal Regional Tracking Control of Time-Fractional Diffusion Systems,” arXiv:2104.12303v1, first public 26 April 2021.
2. D. Xu, Y. Li, and W. Zhou, “Controllability and Observability of Fractional Linear Systems with Two Different Orders,” *The Scientific World Journal* (2014), DOI: 10.1155/2014/618162.
3. E. Trélat and E. Zuazua, “Two-term small-time spectral expansions for controllability Gramians,” arXiv:2609.37077v1, first public 29 September 2026.
