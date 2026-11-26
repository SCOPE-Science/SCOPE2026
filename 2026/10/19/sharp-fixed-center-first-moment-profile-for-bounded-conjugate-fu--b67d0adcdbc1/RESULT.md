# Extremizers and the logarithmic crossover in the half-strip first-moment problem

## Finding

Let \(F\) be holomorphic on the unit disk with \(\operatorname{Re}F>0\), \(|\operatorname{Im}F|<B\), and \(F(0)=M+iV\), where \(B>0\), \(M>0\), and \(|V|<B\). Put \(X=M/B\), \(Y=V/B\). Write \(v^*\) for the almost-everywhere radial boundary trace of \(\operatorname{Im}F\), and use normalized Lebesgue measure \(dm=dt/(2\pi)\) on the circle. The sharp first absolute moment is \(B\mathcal G(X,Y)\), where
\[
\mathcal G(X,Y)=1-\frac8{\pi^2}\sum_{j\ge0}
\frac{e^{-(2j+1)\pi X/2}\cos((2j+1)\pi Y/2)}{(2j+1)^2}.
\]
The profile itself is an endpoint consequence of Brazitikos' half-strip Dirichlet calculation (see below). The claims here are the **complete equality classification** and the **uniform corner law** for this profile:

* \(\int |v^*|\,dm=B\mathcal G(X,Y)\) if and only if \(\Phi=(\sinh(\pi F/(2B))-1)/(\sinh(\pi F/(2B))+1)\) is inner, meaning that its radial boundary values have modulus one almost everywhere. Equivalently, the extremizers at a specified center are precisely the inverse conformal images of inner maps with the corresponding value at zero. They exist at every allowed center and need not be univalent.
* Uniformly as \((X,Y)\to(0,0)\) with \(X>0\),
\[
\mathcal G(X,Y)=|Y|+\frac2\pi\left[
X\left(1+\log\frac4{\pi\sqrt{X^2+Y^2}}\right)-|Y|\arctan\frac X{|Y|}\right]
+O\bigl(X(X^2+Y^2)\bigr),
\]
with the arctangent product interpreted as zero at \(Y=0\). At the centered slice this is \(\frac{2X}{\pi}(1+\log(4/(\pi X)))+O(X^3)\); off center, at fixed \(0<|Y|<1\), the initial slope is the finite \((2/\pi)\log\cot(\pi|Y|/4)\). The two-parameter expression is uniform across these regimes, including \(|Y|\ll X\) and \(X\ll |Y|\).

## Proof

Scale by \(B\) to reduce to \(B=1\). Let \(\Omega=\{x+iy:x>0,\ -1<y<1\}\). Let \(U\) be the harmonic extension of \(|y|\) on its boundary, given by the expected value of the absolute imaginary coordinate at Brownian exit. Exit occurs almost surely since the imaginary coordinate exits \((-1,1)\) almost surely. This representation gives uniqueness in the bounded class by bounded optional stopping. Also, the imaginary coordinate at exit has mean \(y\) and has positive probability of either sign (each of the upper and lower sides has positive harmonic measure from any interior point). Thus \(U(x,y)>|y|\) inside \(\Omega\). The disk function \(U\circ F\) is bounded and harmonic; the mean-value theorem and bounded convergence for the radial imaginary trace give \(\int |v^*|\,dm\le U(F(0))\). No boundary integrability of \(\operatorname{Re}F\) is used.

For clarity about prior implication, Brazitikos solves the half-strip problem with boundary value \(|y|^p\), for \(p>1\), before restricting the eventual estimate to \(Y=0\). The two-variable extension \(U_p(X,Y)\) tends uniformly to \(U\) as \(p\downarrow1\), by uniform convergence of the boundary data and bounded harmonic comparison. The prior Fourier coefficients of \(1-U_p\), namely \(2\int_0^1(1-y^p)\cos(\lambda_j y)\,dy\) for \(\lambda_j=(j+1/2)\pi\), tend to \(2/\lambda_j^2\) by elementary integration. Passing to this limit in the series at \(X>0\) is justified by the summable exponential bound. Thus \(U=\mathcal G\), with \(\mathcal G(0,Y)=|Y|\). The linear constant from the final \(p>1\) theorem does not have a finite endpoint; the fixed-center Dirichlet solution does.

For equality, \(H(w)=\sinh(\pi w/2)\) maps \(\Omega\) biholomorphically onto the right half-plane. Indeed \(\operatorname{Re}\sinh(u+iv)=\sinh u\cos v>0\) for \(u>0, |v|<\pi/2\); the three finite boundary pieces map one-to-one onto the three successive segments of the imaginary axis separated by \(\pm i\), with infinity mapped to infinity. Alternatively the inverse is \((2/\pi)\operatorname{arsinh}\) with the branch into \(\Omega\). The inverse after the Cayley transform extends continuously at every point of the unit circle other than the point \(1\) corresponding to infinity. If \(\Phi\) is inner, its trace avoids \(1\) a.e. by boundary uniqueness for bounded analytic functions (\(\Phi\not\equiv1\)); hence \(F^*\) is on the finite boundary a.e. There \(U(F^*)=|\operatorname{Im}F^*|\). Conversely, if \(\Phi\) is not inner, \(|\Phi^*|<1\) on a positive-measure subset, on which \(F^*\in\Omega\) and the gap is strictly positive. The radial limit of the bounded nonnegative gap \(U\circ F-|\operatorname{Im}F|\) exists a.e. and its integral equals the moment deficit. This proves necessity. For attainment take any disk automorphism sending zero to the Cayley image of \(X+iY\), or compose such an automorphism with \(z^m\), \(m\ge2\), for nonunivalent examples.

For the corner law differentiate the exponentially convergent Fourier series and sum the odd-power series. This gives
\[
\partial_X\mathcal G(X,Y)=\frac1\pi\log\frac{\cosh(\pi X/2)+\cos(\pi Y/2)}{\cosh(\pi X/2)-\cos(\pi Y/2)}
=\frac2\pi\log\left|\coth\frac{\pi(X+iY)}4\right|.
\]
The ratio exceeds one for \(|Y|<1\) and decreases strictly with \(X>0\), giving strict increase and concavity of the profile in \(X\). Substituting \(X=0\) for \(Y\ne0\) gives the stated finite slope. Near zero, \(z\coth z=1+O(|z|^2)\), so the derivative is \((2/\pi)\log(4/(\pi\sqrt{X^2+Y^2}))+O(X^2+Y^2)\) with a direction-independent remainder. Integrating from zero at fixed \(Y\) gives the formula, since the integral of \(\log\sqrt{t^2+Y^2}\) from zero to \(X\) is \(X\log\sqrt{X^2+Y^2}-X+|Y|\arctan(X/|Y|)\). The integrated error is \(O(X(X^2+Y^2))\).

## Scope, verification, and prior work

The equality classification is for all holomorphic maps into the open half-strip, not for degree-bounded trigonometric polynomials. Endpoint centers are excluded; they enter only through profile limits. The accompanying numerical check evaluates the profile, conformal boundary integral, derivative and corner expression at sample points, not the equality characterization or uniform asymptotic proof. Brazitikos' *Sharp Estimates for Conjugate Functions with Applications to Trigonometric Polynomials*, [arXiv:2605.18087v1](https://arxiv.org/pdf/2605.18087v1), Theorem 1 proof, pp. 3–7, supplies the Dirichlet extension and all two-variable eigenfunction coefficients before the real-center linear estimate. The exact endpoint bound follows from this calculation, and its attainment is the standard conformal-boundary construction. The classification of **all** equality cases and the uniform corner formula are not stated in the compared passages. Broader techniques occur in Baernstein, DOI [10.1512/iumj.1978.27.27055](https://doi.org/10.1512/iumj.1978.27.27055), and Essén–Shea–Stanton, DOI [10.5802/aif.1896](https://doi.org/10.5802/aif.1896); exhaustive historical priority is not asserted.
