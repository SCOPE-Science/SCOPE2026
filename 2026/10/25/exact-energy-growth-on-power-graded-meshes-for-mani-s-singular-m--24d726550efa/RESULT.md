# Exact energy growth on power-graded meshes for Manià's singular minimizer

## Finding

Let
\[
\mathcal I[v]=\int_0^1 (v(x)^3-x)^2(v'(x))^6\,dx,
\qquad u_*(x)=x^{1/3}.
\]
For any fixed grading exponent \(r>0\), let \(x_i=(i/N)^r\), \(i=0,\ldots,N\), and let \(I_N^{(r)}\) be the continuous piecewise-affine interpolant satisfying \(I_N^{(r)}(x_i)=u_*(x_i)\). Define, for \(0\le \rho<1\),
\[
s(\rho)=\frac{1-\rho^{1/3}}{1-\rho},\qquad
\phi_\rho(t)=\rho^{1/3}+s(\rho)(t-\rho),
\]
\[
F(\rho)=s(\rho)^6\int_\rho^1(\phi_\rho(t)^3-t)^2\,dt,
\]
and set \(F(1)=0\). Then the exact energy identity and asymptotic law are
\[
\mathcal I[I_N^{(r)}]
=N^r\sum_{i=1}^N i^{-r}F\!\left(\left(\frac{i-1}{i}\right)^r\right)
\sim C_rN^r,
\qquad
C_r=\sum_{i=1}^{\infty}i^{-r}F\!\left(\left(\frac{i-1}{i}\right)^r\right)\in(0,\infty).
\]
In particular, \(F(0)=8/105\), so \(C_r>8/105\) and \(\mathcal I[I_N^{(r)}]\ge (8/105)N^r\) for every \(N\). Thus every fixed power grading still yields energy blow-up, with the exact rate \(N^r\) and an explicit positive convergent-series coefficient. The case \(r=1\) recovers the uniform-mesh coefficient; the new statement supplies the full asymptotic law for every fixed \(r>0\).

## Assumptions and scope

The grading exponent \(r\) is fixed independently of \(N\) and strictly positive. The mesh nodes are exactly \(x_i=(i/N)^r\), and the interpolant is the nodal, continuous, piecewise-affine interpolant of \(u_*(x)=x^{1/3}\). The functional is evaluated exactly, not by quadrature. The theorem concerns this interpolant only; it does not assert the same asymptotic for discrete minimizers, for arbitrary meshes, or for enhanced/nonconforming finite-element schemes.

## Proof

Write \(x_i=(i/N)^r\) and \(\rho_i=x_{i-1}/x_i=((i-1)/i)^r\). On the cell \([x_{i-1},x_i]\), use \(x=x_it\). By the nodal conditions, \(I_N^{(r)}(x_it)=x_i^{1/3}\phi_{\rho_i}(t)\) and \((I_N^{(r)})'(x_it)=x_i^{-2/3}s(\rho_i)\). Hence
\[
(I_N^{(r)}(x_it)^3-x_it)^2((I_N^{(r)})'(x_it))^6\,x_i\,dt
=x_i^{-1}s(\rho_i)^6(\phi_{\rho_i}(t)^3-t)^2\,dt.
\]
The cell contribution is therefore \(x_i^{-1}F(\rho_i)=N^ri^{-r}F(\rho_i)\). Summing gives the displayed exact identity.

It remains to prove convergence of the series. As \(\rho\uparrow1\), the chord \(\phi_\rho\) interpolates \(f(t)=t^{1/3}\) over an interval of length \(h=1-\rho\). Taylor's formula, uniformly on this interval, gives \(\phi_\rho(t)^3-t=-(t-\rho)(1-t)/3+O(h^3)\), while \(s(\rho)=1/3+O(h)\). Consequently,
\[
F(\rho)=\frac1{729\cdot9}\int_\rho^1(t-\rho)^2(1-t)^2\,dt+O(h^6)
=\frac{h^5}{196830}+O(h^6).
\]
Since \(1-((i-1)/i)^r=r/i+O(i^{-2})\), the \(i\)-th series term is asymptotic to \(r^5/(196830\,i^{r+5})\). The series defining \(C_r\) therefore converges, and it is positive because every term is nonnegative and the first term is \(F(0)=\int_0^1(t^3-t)^2dt=8/105\). Dividing the exact identity by \(N^r\) and taking \(N\to\infty\) gives convergence of the partial sums to \(C_r\), proving \(\mathcal I[I_N^{(r)}]\sim C_rN^r\).

## Verification

The proof establishes the result for every fixed real \(r>0\); it does not rely on a finite enumeration. A standard-library checker is supplied in `verify.py`. It uses exact rational polynomial integration for the case \(r=3\), checks the first-cell constant \(8/105\), and numerically evaluates the defining series for selected grading exponents as a reproducibility check. Numerical checks are supplementary and are not used to justify the all-\(r\) proof.

## Relationship to prior work

Manià's functional is a classical example of the Lavrentiev phenomenon. Ball and Knowles discuss the singular minimizer and the failure of standard piecewise-linear finite elements; Feng and Schnake explain why ordinary finite-element approximations cannot converge to the singular minimizer and propose a derivative cut-off remedy. The closest exact quantitative comparison found is the previously recorded uniform-mesh asymptotic \(\mathcal I[I_N^{(1)}]\sim C_1N\). The present claim does not reassert that special case as new: it gives an exact series coefficient and the \(N^r\) law for every fixed power grading exponent \(r>0\). The general qualitative divergence theorem for approximants converging to \(u_*\) does not state this grading-dependent rate or its coefficient.

## Limitations

The coefficient \(C_r\) is represented by an explicit convergent series, not a closed elementary expression. The result is restricted to fixed power grading and the nodal piecewise-affine interpolant; it does not optimize over mesh families, characterize the energy-minimizing finite-element function, or show that every possible mesh has this same rate. The source literature contains broader qualitative divergence statements and an exact uniform-mesh calculation, so priority for any equivalent graded-mesh asymptotic outside the inspected material remains a residual risk.

## References

1. X. Feng and S. Schnake, “An enhanced finite element method for a class of variational problems exhibiting the Lavrentiev gap phenomenon,” arXiv:1610.03111, first submitted 2016-10-10. The manuscript states the Manià functional, its singular minimizer, and the qualitative failure of standard finite-element approximation.
2. J. M. Ball and G. Knowles, “A numerical method for detecting singular minimizers,” *Numerische Mathematik* 51 (1987), 181–197, DOI: 10.1007/BF01396748. The full paper discusses the Manià example and qualitative divergence of energies for approximants converging to the singular minimizer.
