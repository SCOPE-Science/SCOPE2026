# Sharp determinant-optimal exponential Riesz bases on a three-cell multittile

## Finding
For the threefold unit-lattice multittile \(\Omega=[0,1)\cup[1,2)\cup[3,4)\), let
\[\mathcal E_\theta=\{e^{2\pi i(n+\theta_j)x}:n\in\mathbb Z,\ j=0,1,2\}\]
for three distinct phases modulo one. The exact maximal determinant of the three-by-three analysis Gram matrix is
\[D_{\max}=\frac{9748+1360\sqrt{10}}{729}=19.271190147913\ldots.\]
The complete equality family is
\[\{\theta_0,\theta_1,\theta_2\}=\left\{\tau-\frac{t_*}{2\pi},\tau,\tau+\frac{t_*}{2\pi}\right\}\pmod1,
\qquad t_*=\arccos\!\left(\frac{\sqrt{10}-2}{6}\right),\]
for arbitrary \(\tau\in\mathbb R/\mathbb Z\), with arbitrary permutation. Thus the determinant-optimal phases are symmetric with two equal short angular gaps; this is not the regular three-gon. In fact, regular three-gon shifts have identical exponent-zero and exponent-three rows and hence give determinant zero. No system in this class is orthogonal or tight.

## Assumptions and scope
All exponentials have their raw unit-modulus normalization on \(\Omega\) (each has squared norm \(3\)); the measure is Lebesgue measure. Phases are considered modulo one because shifting one phase by an integer does not alter its coset. Distinctness is necessary for a Riesz basis. Write
\[V(\theta)=\big(e^{2\pi i r\theta_j}\big)_{r\in\{0,1,3\},\ j=0,1,2}.\]
If \(0<A_1\le A_2\le A_3\) are the exact squared analysis singular values, equivalently the eigenvalues of \(VV^*\), the optimized quantity is \(D=A_1A_2A_3=|\det V|^2\). This is a determinant/volume optimum, not a claim that \(A_1\) or the condition number is individually optimal. All three cosets and all possible real phases are allowed.

## Proof
**Fiber reduction and invertibility.** For \(f\in L^2(\Omega)\), write \(f_r(t)=f(t+r)\), \(t\in[0,1)\), for \(r\in\{0,1,3\}\). Parseval for \(\{e^{2\pi int}\}_{n\in\mathbb Z}\) gives, for each \(j\),
\[\sum_{n\in\mathbb Z}|\langle f,e^{2\pi i(n+\theta_j)\cdot}\rangle|^2=\int_0^1\left|\sum_{r\in\{0,1,3\}}f_r(t)e^{-2\pi i r\theta_j}\right|^2dt.\]
The unit-modulus factor \(e^{-2\pi i\theta_jt}\) disappears in the modulus. Summing over \(j\), the optimal analysis frame bounds are exactly the least and greatest eigenvalues of \(VV^*\). The synthesis operator is unitarily equivalent, via three separate Fourier-series isometries, to multiplication by a fixed three-by-three matrix. Thus \(\mathcal E_\theta\) is a Riesz basis if and only if \(V\) is invertible. The determinant below is zero at any repeated phases, so optimizing over all phases or only distinct phases has the same positive maximum.

**Generalized Vandermonde reduction.** Put \(z_j=e^{2\pi i\theta_j}\). The elementary factorization
\[\det V=(z_1-z_0)(z_2-z_0)(z_2-z_1)(z_0+z_1+z_2)\]
is known for exponent rows \(\{0,1,3\}\); it is not claimed as new. After rotating by \(\overline z_0\), choose angular coordinates
\[z_0=1,\qquad z_1=e^{i(u+v)},\qquad z_2=e^{i(u-v)},\qquad X=\cos u,\quad Y=\cos v.\]
The pair \((X,Y)\) ranges independently over the full square \([-1,1]^2\). Direct trigonometry yields the exact polynomial
\[D=F(X,Y)=16(1-Y^2)(X-Y)^2(1+4Y^2+4XY).\]
This formula remains nonnegative throughout the square because its last factor equals \(|1+2Y e^{iu}|^2\).

**Complete global maximization.** At \(Y=\pm1\) the value is zero. At \(X=1\),
\[F(1,Y)=16(1-Y)^3(1+Y)(1+2Y)^2,\]
whose derivative is \(-32(Y-1)^2(2Y+1)(6Y^2+4Y-1)\). Apart from its zero and endpoints, the two critical values are
\[D_+=\frac{9748+1360\sqrt{10}}{729},\qquad D_-=\frac{9748-1360\sqrt{10}}{729},\]
at \(Y=(-2\pm\sqrt{10})/6\), respectively. The \(X=-1\) edge is the reflection of this edge under \((X,Y)\mapsto(-X,-Y)\).

For interior positive stationary points, the nonzero factor of
\[\frac{\partial F}{\partial X}=-32(X-Y)(Y-1)(Y+1)(6XY+2Y^2+1)\]
forces \(X=-(1+2Y^2)/(6Y)\), with \(Y\ne0\). Substitution gives
\[F=\frac{4(1-Y^2)(1+8Y^2)^3}{27Y^2}.\]
Stationarity in \(Y\) then requires \(24Y^4-16Y^2+1=0\), hence \(Y^2=(4\pm\sqrt{10})/12\). All four possible interior stationary points lie in the square, with objective values \(D_+\) and \(D_-\). The case \(X=Y\) is zero, and \(Y=0\) has no positive stationary point. Compactness now proves that \(D_+\) is the sharp global maximum.

**Equality geometry.** On \(X=1\), the maximizing value is \(Y=c_*=(\sqrt{10}-2)/6\); it yields the phase set \(\{1,e^{it_*},e^{-it_*}\}\), where \(t_*=\arccos c_*\). The edge \(X=-1\) yields the same set after common rotation. For interior maximizers, \(Y^2=(4+\sqrt{10})/12=\cos^2(t_*/2)\), and their \(X\) value is \(\cos(3t_*/2)\) up to the coordinate symmetries. The stationary identity \(24Y^4-16Y^2+1=0\) implies \(X=4Y^3-3Y\), so with \(Y=\cos(t_*/2)\) one has \(X=\cos(3t_*/2)\). The corresponding phase set is \(\{1,e^{it_*},e^{2it_*}\}\) or its reflected equivalent, which is again the same configuration after a common rotation. All maximizers have therefore been classified.

**Strict nonorthogonality.** Two distinct columns could be orthogonal only if \(1+z+z^3=0\) for a unit complex number \(z\). Three unit numbers summing to zero must be the three cube roots of unity. Thus \(z\) would be a primitive cube root, but then \(z^3=1\), a contradiction. Each column of \(V\) has squared norm \(3\); a three-by-three tight basis would require the columns to be mutually orthogonal. Hence there is no tight or orthogonal basis within this coset class, consistently with \(D_{\max}<27\).

## Verification
The accompanying `checker.py` independently verifies the derivative factorizations, all nonzero stationary candidate values, and the optimal value using exact symbolic arithmetic. It also runs 2000 seeded random-phase tests comparing the direct complex determinant, the real two-variable formula, and the product of Gram eigenvalues; five local perturbation tests and a fiber Parseval identity check. The maximal factorization discrepancy is below \(1.9\times10^{-14}\). These finite numerical checks do not prove the global optimum; the proof is the compact-square stationary-and-boundary enumeration above. Run `python checker.py` with Python 3, NumPy and SymPy.

## Relationship to prior work
Frederick and Okoudjou (2019 preprint; 2021 journal version), especially Theorem 2.1 and Section 3, establish the multittile Riesz-basis reduction using finite fiber matrices. Frederick and Yacoubou Djima (2023) provide explicit examples and bounds. These general existence/construction mechanisms are not claimed as new. Lundengård, Österberg, and Silvestrov (2013) record exactly the Schur/Vandermonde factorization for exponent rows \(\{0,1,3\}\), but their extremization concerns **real nodes on the Euclidean sphere**, not three complex nodes of unit modulus. Dubickas and Pritsker (2019) optimize fixed-product external-field weighted Vandermondes on the unit circle; the extra joint factor \(|z_0+z_1+z_2|\) in this problem is not an external-field weight of that type. The specific sharp unit-circle optimum and its equality orbit, interpreted as a determinant-optimal exponential Riesz basis for the stated multittile, are the new claim.

## Limitations
The result optimizes the product of the three exact frame bounds over three **integer-frequency cosets** only; it does not optimize each individual bound, condition numbers, arbitrary noncoset spectral sets, or unconstrained bases. It assumes an exact three-interval multittile and noiseless Fourier analysis. The search cannot rule out a less easily indexed older treatment of this exact constrained three-node generalized-Vandermonde maximum; scientific priority is not independently established. The proof is analytic, whereas the standalone checker is a finite numerical and symbolic aid.

## References
1. C. Frederick and K. A. Okoudjou, *Finding duality for Riesz bases of exponentials on multi-tiles*, arXiv:1910.09257 (first public 2019-10-21), Applied and Computational Harmonic Analysis 51 (2021), 104–117, https://arxiv.org/html/1910.09257v3 .
2. C. Frederick and K. Yacoubou Djima, *Examples of Riesz Bases of Exponentials for Multi-tiling Domains and Their Duals*, La Matematica 3 (2024), 108–123, online 2023-11-20, https://doi.org/10.1007/s44007-023-00078-7 .
3. K. Lundengård, J. Österberg, and S. Silvestrov, *Extreme points of the Vandermonde determinant on the sphere and some limits involving the generalized Vandermonde determinant*, arXiv:1312.6193 (2013), https://arxiv.org/html/1312.6193v1 .
4. A. Dubickas and I. E. Pritsker, *Weighted Fekete points on the real line and the unit circle*, arXiv:1902.08348 (2019), https://arxiv.org/abs/1902.08348 .
