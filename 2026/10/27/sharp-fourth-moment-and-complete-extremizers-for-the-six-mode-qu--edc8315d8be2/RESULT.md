# Sharp fourth moment and complete extremizers for the six-mode quadratic Fourier simplex

## Finding

Let \(m\) denote normalized Haar probability measure on the two-torus \(\mathbb T^2\). For arbitrary complex \(a,b,c,d,e,f\), set
\[
P(z,w)=a+bz+cw+dz^2+ezw+fw^2,\quad (z,w)\in\mathbb T^2.
\]
Write \(t_*\) for the unique positive root of
\[
2t^3+3t^2-6t-3=0,\qquad t_*=1.402255788644281\ldots
\]
and define
\[
K_* =\frac{5t_*^4+8t_*^3+16t_*^2+5}{3(1+t_*^2)^2}
=2.949235612050375\ldots.
\]
Then the **sharp unrestricted-complex-coefficient inequality** is
\[
\boxed{\int_{\mathbb T^2}|P|^4\,dm \le K_*\bigl(|a|^2+|b|^2+|c|^2+|d|^2+|e|^2+|f|^2\bigr)^2.}
\]
Every nonzero equality case, and no others, is
\[
\boxed{(a,b,c,d,e,f)=\lambda\bigl(1,t_*e^{i\theta},t_*e^{i\phi},e^{2i\theta},t_*e^{i(\theta+\phi)},e^{2i\phi}\bigr),}
\]
with \(\lambda\in\mathbb C\setminus\{0\}\) and real \(\theta,\phi\). The same sharp constant and equality classification hold on every finite product of cyclic Fourier grids \(\mathbb Z_N\times\mathbb Z_M\) with \(N,M\ge5\), under probability-normalized averaging and the standard generating characters.

Equivalently, \(K_*\) is the largest real root of \(2700K^3-15768K^2+28359K-15749=0\). For the six equal-magnitude coefficients, the sharp value in that restricted class is only \(102/36=17/6\), strictly less than \(K_*\). Thus an unrestricted maximizer necessarily breaks equal-magnitude symmetry between the three simplex vertices and its three edge midpoints.

## Assumptions and scope

The exponent support is the complete total-degree-at-most-two simplex \(S=\{(i,j)\in\mathbb Z_{\ge0}^2:i+j\le2\}\). Each coefficient is an arbitrary complex number, possibly zero; the sharp inequality applies to all six-dimensional coefficient vectors. The coefficient norm is unweighted Euclidean \(\ell^2\); Haar measure is normalized to mass one. For finite grids the bounds \(N,M\ge5\) guarantee that distinct elements of \(S+S\subset[0,4]^2\) do not alias after modular reduction. No sharp claim is made for smaller grids or other aperture shapes.

## Proof

**Fourier convolution and phases.** For the six coefficients regarded as a function \(c:S\to\mathbb C\), normalized Fourier Parseval gives
\[
\int_{\mathbb T^2}|P|^4\,dm=\sum_{\nu\in S+S}\left|\sum_{\alpha+\beta=\nu}c_\alpha c_\beta\right|^2.
\]
Replacing all coefficients by their nonnegative moduli weakly increases every term on the right, and leaves the coefficient norm unchanged. Put
\[
A=|a|,\ D=|d|,\ F=|f|,\qquad B=|b|,\ C=|c|,\ E=|e|,
\]
\[
U=A^2+D^2+F^2,\qquad V=B^2+C^2+E^2,\qquad
T=AD B^2+AF C^2+DF E^2.
\]
Direct enumeration of the 15 pair-sum frequencies gives the exact nonnegative-coefficient fourth moment
\[
\begin{aligned}
\mathcal Q={}&2U^2-(A^4+D^4+F^4)+2V^2-(B^4+C^4+E^4)\\
&+4UV+4T+8(A+D+F)BCE.\tag{1}
\end{aligned}
\]

**A globally sharp sum-of-squares symmetrization.** Define
\[
D_U=A^4+D^4+F^4-U^2/3,\qquad
D_V=B^4+C^4+E^4-V^2/3.
\]
The following exact polynomial identity holds for all real six-tuples (by expansion):
\[
\begin{aligned}
&D_U+D_V+\tfrac43UV-4T\\
={}&\bigl(A^2+E^2-(U+V)/3\bigr)^2
+\bigl(D^2+C^2-(U+V)/3\bigr)^2
+\bigl(F^2+B^2-(U+V)/3\bigr)^2\\
&+2B^2(A-D)^2+2C^2(A-F)^2+2E^2(D-F)^2\ge0.
\tag{2}
\end{aligned}
\]
Moreover, Cauchy–Schwarz and arithmetic–geometric mean give
\[
(A+D+F)BCE\le\sqrt{3U}\left(\frac V3\right)^{3/2}
=\frac{\sqrt U\,V^{3/2}}3.
\tag{3}
\]
Equations (1)–(3) imply the universal envelope
\[
\boxed{\mathcal Q\le\frac53(U^2+V^2)+\frac{16}3UV+\frac83\sqrt U\,V^{3/2}.}\tag{4}
\]
This envelope is **attainable at every fixed pair \((U,V)\)** by the equal-vertex and equal-edge choice \(A=D=F=\sqrt{U/3}\), \(B=C=E=\sqrt{V/3}\). When \(U,V>0\), equality in (3) also forces all three vertex moduli equal and all three edge moduli equal, so no other fixed-mass maximizers are possible.

**One-variable optimization.** Set the common vertex modulus to \(x\ge0\) and common edge modulus to \(y\ge0\). With aligned phases, (1) reduces to
\[
\mathcal Q=15x^4+48x^2y^2+24xy^3+15y^4,
\qquad\|P\|_2^2=3(x^2+y^2).
\]
For \(x>0\) put \(t=y/x\ge0\); the sharp quotient for these masses is
\[
R(t)=\frac{5t^4+8t^3+16t^2+5}{3(1+t^2)^2}.
\]
Its derivative factors **exactly** as
\[
R'(t)=-\frac{4t(2t^3+3t^2-6t-3)}{3(1+t^2)^3}.\tag{5}
\]
The cubic has exactly one positive root, by Descartes' sign rule together with negative value at zero and positive limit at infinity. Hence \(R\) strictly increases up to \(t_*\) and strictly decreases thereafter. The two boundary limits \(R(0)=\lim_{t\to\infty}R(t)=5/3\) are strictly smaller than \(R(t_*)\). Equation (4) and its equality conditions prove global sharpness and the unique vertex/edge modulus ratio \(1:t_*\).

**Every complex equality phase.** At a sharp nonzero maximizer all moduli are strictly positive. Equality in the Fourier triangle inequalities applied to the \((2,0)\), \((0,2)\), and \((1,1)\) pair-sum frequencies requires
\[
2\arg b\equiv\arg a+\arg d,\quad
2\arg c\equiv\arg a+\arg f,\quad
\arg a+\arg e\equiv\arg b+\arg c\pmod {2\pi}.
\]
Taking \(\lambda=a\), \(\theta=\arg b-\arg a\), \(\phi=\arg c-\arg a\) gives precisely the stated coefficient phases. These affine phases automatically align *every* pair-sum coefficient, proving sufficiency as well. The same proof applies on \(\mathbb Z_N\times\mathbb Z_M\) because, for \(N,M\ge5\), its degree-four pair-sum frequencies remain distinct.

## Verification

The included `CHECK.py` uses SymPy to reconstruct all ordered pair-sum convolution terms, verify identity (1), independently expand and confirm the entire square identity (2), factor the derivative (5), calculate the algebraic resultant for \(K_*\), and isolate \(t_*\) between two rational endpoints. It then checks 25 complex-coefficient samples against the sharp bound, 75 exact-frequency-versus-finite-grid fourth-moment comparisons, and three affine-phase extremizers. Run `python3 CHECK.py` with Python 3 and SymPy. Its completed run reported `PASS` with \(t_*=1.402255788644281\ldots\) and \(K_*=2.949235612050376\ldots\). The infinite-dimensional (all-complex-coefficient) inequality is proved algebraically above; finite samples are corroboration only.

## Relationship to prior work

Ciccone and Gonçalves (arXiv:2208.09441, first public 2022-08-19) establish a sharp Euclidean-plane \(L^6\) Fourier *circle-extension* inequality under arithmetic spectral constraints. Their theorem is not a torus \(L^2\)-to-\(L^4\) problem on the six-point quadratic simplex and cannot imply this coefficient ratio or equality family. Ganzburg (arXiv:1901.04400, first public 2019-01-14) studies asymptotic multivariate Bernstein–Nikolskii constants and existence questions rather than this exact fixed finite aperture. Bach and Rudi (arXiv:2211.04889, first public 2022-11-09) give generic approximation guarantees for sum-of-squares hierarchies, not the algebraic sharp constant here.

The publicly available result titled *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture* treats precisely this frequency set but **requires all six coefficients to have unit modulus**. Its sharp **maximum** is \(102\), or normalized \(17/6\), and thus does not cover the strictly larger unrestricted sharp value \(K_*\), nor the unequal-amplitude classification here. A published unrestricted result for the five-point Ferrers sub-aperture has constant \(2.646915130955\ldots\), smaller than \(K_*\) and cannot furnish its equality family. Similarly, the four-consecutive-character one-dimensional sharp constant \(2.808840165474\ldots\) has a different frequency support. The present result determines a distinct all-coefficient \(\Lambda(4)\) constant for a natural complete two-dimensional simplex.

## Limitations

No bound is claimed for other moments, larger or incomplete apertures, coefficient weights, or cyclic grids of order below five. The exact algebra does not prove historical priority. In particular, an older result in finite-impulse-response filter design, quadratic Steinhaus-chaos norms, or sparse autocorrelation optimization could express an equivalent result under different language; these remain bibliographic risks. The numerical checks are finite and do not replace the proof.

## References

1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1 (2022-08-19), https://arxiv.org/abs/2208.09441.
2. M. I. Ganzburg, *Sharp Constants of Approximation Theory. I. Multivariate Bernstein–Nikolskii Type Inequalities*, arXiv:1901.04400v1 (2019-01-14), https://arxiv.org/abs/1901.04400.
3. F. Bach and A. Rudi, *Exponential convergence of sum-of-squares hierarchies for trigonometric polynomials*, arXiv:2211.04889v1 (2022-11-09), https://arxiv.org/abs/2211.04889.
4. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, publicly available research result (2026), phase-only six-mode inequality.
5. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, publicly available research result (2026), unrestricted five-mode inequality.
6. *Exact fourth moment and all extremizers for four consecutive Fourier characters*, publicly available research result (2026), unrestricted four-mode inequality.
