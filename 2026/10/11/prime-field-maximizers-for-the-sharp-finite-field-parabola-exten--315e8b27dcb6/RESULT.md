# Prime-field maximizers for the sharp finite-field parabola extension inequality
## Finding
Let \(p>3\) be prime, \(e_p(t)=\exp(2\pi i t/p)\), and \(\mathbb P^1=\{(t,t^2):t\in\mathbb F_p\}\). With normalized surface measure \(\sigma\), the sharp inequality
\[
\|(f\sigma)^\vee\|_{L^6(\mathbb F_p^2)}\le(1+p^{-1}-p^{-2})^{1/6}\|f\|_{L^2(\mathbb P^1)}
\]
has the following complete nonzero equality class:
\[
f(t,t^2)=\lambda e_p(a t+b t^2),\qquad \lambda\ne0,\quad a,b\in\mathbb F_p.
\]
Hence there are exactly \(p^2\) maximizers modulo nonzero scalars.

## Assumptions and scope
The field is the prime field \(\mathbb F_p\), with \(p>3\). The sharp constant and the fact that every maximizer has constant modulus are taken from González-Riquelme and Oliveira e Silva. The contribution here is the complete prime-field phase classification. No complete classification over extension fields is asserted.

Write a maximizer as \(f(t,t^2)=\lambda\rho(t)\), where \(|\rho(t)|=1\).

## Proof
Equality in the generic-fiber Cauchy--Schwarz step of the sharp proof forces all triple products in each generic convolution fiber to agree. The centered triples
\[
(m+u,m+v,m-u-v),\qquad(m-u,m-v,m+u+v)
\]
have the same sum and sum of squares, and their fiber is generic exactly when \(Q(u,v)=u^2+uv+v^2\ne0\). Therefore
\[
\rho(m+u)\rho(m+v)\rho(m-u-v)=\rho(m-u)\rho(m-v)\rho(m+u+v).
\]
Set \(R_m(t)=\rho(m+t)/\rho(m-t)\). Then
\[
R_m(u)R_m(v)=R_m(u+v)
\]
whenever \(Q(u,v)\ne0\).

If \(p\equiv2\pmod3\), \(Q\) has no nonzero zero, so the identity holds for all pairs. If \(p\equiv1\pmod3\), choose \(j\) with \(j^2+j+1=0\). The only missing nonzero pairs have \(v=ju\) or \(v=j^2u\). For \(v=ju\), choose \(w=cu\) with
\[
c\notin\{0,1,j,j^2,j^2-1,j^2-j\}.
\]
Such \(c\) exists: \(p\ge7\), the set has at most six elements, and for \(p=7\) it has only five distinct elements. Then the four pairs \((u,w)\), \((u+w,v)\), \((w,v)\), and \((u,v+w)\) are generic. Applying the identity to them and cancelling gives the missing relation for \((u,v)\). The case \(v=j^2u\) is symmetric. Thus every \(R_m\) is an additive character.

In particular \(R_m(2)=R_m(1)^2\). Put \(d(x)=\rho(x+1)/\rho(x)\). Expanding gives
\[
d(m-2)d(m+1)=d(m-1)d(m).
\]
Hence for \(E(x)=d(x)/d(x-1)\), one has \(E(x+2)=E(x)\). Since translation by \(2\) generates the cyclic additive group \(\mathbb F_p\), \(E\) is constant, say \(E(x)=r\). Thus \(d(x)=d(0)r^x\). Periodicity gives \(r^p=1\), while \(\prod_{x\in\mathbb F_p}d(x)=1\) gives \(d(0)^p=1\). Therefore \(d(0)=e_p(A)\) and \(r=e_p(B)\) for some \(A,B\in\mathbb F_p\), and summing first differences yields
\[
\rho(x)=\rho(0)e_p\!\left(Ax+\frac{B}{2}x(x-1)\right)=\rho(0)e_p(a x+b x^2).
\]
This proves necessity.

Conversely, multiplying by \(e_p(a t+b t^2)\) translates the extension in the two physical coordinates and preserves its \(L^6\) norm; it also preserves the \(L^2\) norm. Since constants attain the sharp constant, every displayed quadratic phase is a maximizer. Distinct \((a,b)\) give distinct scalar classes because a degree-two polynomial constant on all of \(\mathbb F_p\) has zero linear and quadratic coefficients.

## Verification
`verify.py` constructs the complete generic-fiber phase system over \(\mathbb F_p\) for \(p\in\{5,7,11,13,17,19,23,31\}\). In each case its rank is \(p-3\), leaving exactly the scalar, linear, and quadratic phase parameters. It also exhausts the bridge cases in the split primes and checks quadratic phases against every generic equation. These computations are corroborative; the analytic proof covers every prime \(p>3\).

## Relationship to prior work
Mockenhaupt and Tao introduced the finite-field extension framework; their paper has primary MSC 42B05. González-Riquelme and Oliveira e Silva proved the sharp \(L^2\to L^6\) constant for \(\mathbb P^1\) and proved that every maximizer has constant modulus, but their Theorem 1.3 does not classify the phases. The same paper explicitly gives full maximizer classifications for other surfaces. Foschi's Euclidean theorem gives a Gaussian symmetry orbit, not the finite-field conclusion. A later finite-field paper classifies cone maximizers rather than parabola maximizers.

## Limitations
The cyclic-prime-field step is essential to this proof. Over non-prime finite fields the additive group has extra directions, so no complete extension-field equality classification is claimed. No equivalent published prime-field phase classification was found, but differently indexed older literature remains a residual originality risk.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first public 18 April 2002.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public 26 May 2024, Theorem 1.3 and Section 6.
3. D. Foschi, *Maximizers for the Strichartz inequality*, arXiv:math/0404011, first public 1 April 2004.
4. C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600, first public 6 September 2025.
