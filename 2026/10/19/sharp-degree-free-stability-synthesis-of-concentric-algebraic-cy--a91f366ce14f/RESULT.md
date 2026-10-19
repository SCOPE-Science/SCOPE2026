# Sharp-degree free-stability synthesis of concentric algebraic cycles

## Finding

**Theorem.** Let \(n\geq1\) be an integer, let \(0<a_1<\cdots<a_n\) be arbitrary real numbers, and independently designate each Euclidean circle \(\Gamma_i=\{(x,y):x^2+y^2=a_i\}\) as attracting or repelling. Among all real planar polynomial vector fields having every \(\Gamma_i\) as a **hyperbolic periodic orbit** with its designated stability, the smallest possible polynomial degree is exactly \(2n\). A degree-\(2n\) realization is given by explicit interpolation and has exact, nonzero transverse Floquet multipliers.

There is also a rigidity statement at the optimal degree: if a real polynomial field \(X=(P,Q)\) of degree at most \(2n\) leaves all these circles invariant, then
\[
xP(x,y)+yQ(x,y)=\bigl(\alpha x+\beta y\bigr)\prod_{i=1}^n(x^2+y^2-a_i)
\]
for constants \(\alpha,\beta\in\mathbb R\). In particular, radial forcing at the degree threshold necessarily has only a first angular Fourier harmonic. The theorem does **not** assert that the realized field has no additional, noncircular periodic orbits.

## Assumptions and scope

The polynomial degree of \(X=(P,Q)\) is \(\max(\deg P,\deg Q)\). A circle is a hyperbolic periodic orbit if the vector field does not vanish on it and its nontrivial Poincaré multiplier differs from \(1\); it is attracting if that multiplier lies in \((0,1)\) and repelling if it is greater than \(1\). Circles are centered at the origin, nested, and of pairwise distinct strictly positive radii. The surrounding dynamics need not be radial, equivariant, integrable, or free from further limit cycles. Stability designations are independent binary choices; no periods or basins are prescribed.

## Proof

**1. Universal degree lower bound and rigidity.** Put \(s=x^2+y^2\), \(H(s)=\prod_{i=1}^n(s-a_i)\), and \(F=xP+yQ\). Invariance of \(\Gamma_i\) means \(F\) vanishes on the entire real circle \(s=a_i\). Divide \(F\), as a polynomial in \(y\) over \(\mathbb R[x]\), by the monic quadratic \(y^2+x^2-a_i\). The remainder is \(u(x)y+v(x)\). For every \(|x|<\sqrt{a_i}\), its values at the two distinct points \(y=\pm\sqrt{a_i-x^2}\) are zero. Hence \(u(x)=v(x)=0\) on an interval, so these remainder polynomials vanish identically. Therefore \(s-a_i\) divides \(F\).

Distinct factors \(s-a_i\) and \(s-a_j\) are coprime, since their difference is the nonzero constant \(a_j-a_i\). Consequently \(H(s)\) divides \(F\). If the vector-field degree is \(d\), then \(\deg F\leq d+1\), whereas \(\deg H(s)=2n\). When \(d\leq2n-1\), the quotient is at most constant. But \(F(0,0)=0\), whereas \(H(0)=(-1)^n\prod_i a_i\neq0\); therefore \(F\equiv0\). In that case \(\dot s=2F\equiv0\), and no invariant circle can be hyperbolic in the radial direction. Thus \(d\geq2n\).

When \(d\leq2n\), divisibility gives \(F=H(s)L(x,y)\) with \(\deg L\leq1\). Again \(F(0,0)=0\) and \(H(0)\neq0\), so the constant term of \(L\) vanishes. This proves the asserted degree-threshold rigidity \(L=\alpha x+\beta y\).

**2. Explicit degree-\(2n\) field.** Define \(h_0=H(0)\neq0\) and \(J(s)=(H(s)-h_0)/s\), a polynomial of degree \(n-1\). For each \(i\), put \(\varepsilon_i=+1\) for a desired attractor, and \(\varepsilon_i=-1\) for a desired repeller. The simple roots ensure \(H'(a_i)\neq0\). Choose the unique interpolation polynomial \(B\) of degree at most \(n-1\) such that
\[
B(a_i)=\beta_i:=\varepsilon_i\operatorname{sgn}H'(a_i)\in\{-1,+1\}.
\]
Choose any real constant \(C>\max_i\sqrt{a_i\beta_i^2+h_0^2/a_i}\). With \(s=x^2+y^2\), set
\[
\begin{aligned}
P(x,y)&=xyJ(s)-y\bigl(C+yB(s)\bigr),\\
Q(x,y)&=y^2J(s)+h_0+x\bigl(C+yB(s)\bigr).
\end{aligned}
\]
Both components have degree at most \(2n\), and the coefficient of the term \(xy s^{n-1}\) in the leading homogeneous part of \(P\) cannot be canceled by any term proportional to \(y^2s^{n-1}\); hence the degree is exactly \(2n\). Direct cancellation gives
\[
xP+yQ=yH(s),\qquad xQ-yP=s\bigl(C+yB(s)\bigr)+h_0x.
\]
For \(r>0\), polar coordinates yield the **exact** equations
\[
\dot r=H(r^2)\sin\theta,\qquad
\dot\theta=C+rB(r^2)\sin\theta+\frac{h_0}{r}\cos\theta.
\]
On \(r=\sqrt{a_i}\), the radial velocity vanishes. The angular velocity becomes
\[
w_i(\theta)=C+\beta_i\sqrt{a_i}\sin\theta+\frac{h_0}{\sqrt{a_i}}\cos\theta>0
\]
by the strict choice of \(C\). Thus every \(\Gamma_i\) is a nonstationary periodic orbit, traversed once with positive angular orientation.

**3. Exact multiplier and stability design.** On the \(i\)-th circle, linearizing the radial equation gives \(\delta\dot r=2\sqrt{a_i}H'(a_i)\sin\theta\,\delta r\). The coefficient of angular variation in this radial equation vanishes on the circle, so radial perturbations satisfy a scalar Floquet equation. Write \(A_i=\beta_i\sqrt{a_i}\), \(D_i=\sqrt{C^2-A_i^2-h_0^2/a_i}>0\). The classical circle integral, obtainable by differentiating the logarithmic integral, is
\[
\int_0^{2\pi}\frac{\sin\theta}{C+A\sin\theta+B\cos\theta}\,d\theta=-\frac{2\pi A}{\sqrt{C^2-A^2-B^2}\bigl(C+\sqrt{C^2-A^2-B^2}\bigr)}
\]
for \(C>\sqrt{A^2+B^2}\). Hence the nontrivial multiplier \(\mu_i\) satisfies the **exact formula**
\[
\boxed{\log\mu_i=-\frac{4\pi a_i H'(a_i)\beta_i}{D_i(C+D_i)}.}
\]
Because \(\beta_i=\varepsilon_i\operatorname{sgn}H'(a_i)\), the sign of this logarithm is \(-\varepsilon_i\). In particular \(\mu_i\neq1\) for every \(i\); the designated attractors have \(0<\mu_i<1\) and the designated repellers have \(\mu_i>1\). This completes the sharp-degree realization and the proof. \(\square\)

## Verification

The included standalone `verify.py` uses Python's standard library. It constructs \(H\), \(B\), \(P\), and \(Q\) with exact rational arithmetic; checks \(xP+yQ=yH(s)\) and polynomial degree \(2n\); verifies all angular-positivity inequalities and Floquet signs; and compares the analytical multiplier integral with independent periodic midpoint quadrature. All \(2^n\) attracting/repelling choices are checked for each \(1\le n\le5\) at the distinct squared radii chosen from \(1,2,4,7,11\). The extracted checker passed **1,414 assertions**. These finite tests are corroboration, not a proof for general real radii or arbitrarily large \(n\); the proof above supplies the universal quantifiers.

## Relationship to prior work

Song Fei, *Algebraic Synthesis of Polynomial Vector Fields with Prescribed Invariant Spheres* (first posted September 21, 2026), gives the radial-factorized equivariant family \(\dot r=rH(r^2)\), \(\dot\theta=1\), of degree \(2n+1\), and establishes its degree optimality **inside that family**. Its alternating hyperbolic stability follows from one-dimensional radial dynamics. Our statement removes equivariance, establishes the universal lower bound \(2n\), and permits **every** prescribed stability pattern at that sharp degree.

The degree-\(2n\) existence statement **without freely prescribed stabilities** should not be attributed to this finding: Colin Christopher (2001) already constructs degree-\(m\) polynomial systems realizing the bounded components of a nonsingular algebraic curve of degree \(m\); taking the product of \(n\) circle equations yields \(m=2n\). The contribution here is the **simultaneous sharp-degree guarantee and independent Floquet-sign control**, with the first-harmonic structural necessity and exact multipliers. Christopher's complete article was not available for full-text comparison; the prior theorem is credited on the basis of its published abstract, and the possibility of a stronger implicit stability result is a residual priority risk.

Margalef-Bentabol and Peralta-Salas (2015), Theorems 4.2 and 5.2, solve far more general prescribed configurations with independently set periods, stabilities, and multiplicities, but their explicit arbitrary-stability construction has a larger degree bound (for \(n\) nested simple cycles, Theorem 4.2 yields \(\deg X<2(3n+1)\)). This does not imply exact, radius-preserving, arbitrary stability at degree \(2n\). Gasull and Santana (2025) construct hyperbolic algebraic ovals within fields of controlled degree but do not provide this optimal-degree all-sign interpolation. Yeung and Erban (2025), in their treatment of planar chemical systems, give alternative invariant-curve constructions; their pointwise transversality criteria do not deliver the same sharp independent assignment at fixed concentric radii.

## Limitations

The theorem prescribes each of the specified circles, its hyperbolicity and its attracting/repelling character; it does **not** classify all equilibria, other limit cycles or basin boundaries. Arbitrary independently prescribed **periods** are not asserted. In particular, adjacent designated attracting circles may require additional intervening invariant dynamics; the construction permits this. No quantitative uniform multiplier margin is asserted when circles coalesce or radii tend to zero. A bibliographic priority risk remains for unavailable full text by Christopher and other older inverse-realization work. This is an analytical result with computational corroboration, not an independent audit.

## References

1. S. Fei, *Algebraic Synthesis of Polynomial Vector Fields with Prescribed Invariant Spheres*, Preprints.org version 1 (posted September 21, 2026), https://www.preprints.org/manuscript/202609.1834 . Primary MSC2020 37C25, 37D10.
2. C. Christopher, *Polynomial Vector Fields with Prescribed Algebraic Limit Cycles*, Geometriae Dedicata **88** (2001), 255–258, https://doi.org/10.1023/A:1013171019668 .
3. J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698 (first public 2015), https://arxiv.org/abs/1507.00698 .
4. A. Gasull and P. Santana, *Limit cycles and invariant algebraic curves*, arXiv:2510.11705 (first public October 13, 2025), https://arxiv.org/abs/2510.11705 .
5. C. Yeung and R. Erban, *Planar chemical reaction systems with algebraic and non-algebraic limit cycles*, Journal of Mathematical Biology (2025), https://doi.org/10.1007/s00285-025-02221-0 .
