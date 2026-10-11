# Sharp small-angle Hankel law for spirallike convex disk maps

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). For \(|\beta|<\pi/2\), let \(\mathcal C_\beta\) consist of normalized holomorphic maps
\[
f(z)=z+a_2z^2+a_3z^3+a_4z^4+\cdots
\]
with \(f'(z)\ne0\) throughout \(\mathbb D\) and
\[
\operatorname{Re}\left[e^{i\beta}\left(1+\frac{zf''(z)}{f'(z)}\right)\right]>0
\qquad(z\in\mathbb D).
\]
Define the sharp second-Hankel constant
\[
M(\beta)=\sup_{f\in\mathcal C_\beta}
\left|a_2a_4-a_3^2\right|.
\]

**Theorem.** There exists \(\delta>0\) such that \(M\) is real analytic and even on \((-\delta,\delta)\), and
\[
\boxed{M(\beta)=\frac18-\frac{59}{432}\beta^2+O(\beta^4)}
\qquad(\beta\to0).
\]
For all sufficiently small \(|\beta|\), every extremal Carathéodory function has a degree-two Blaschke representation, uniquely determined up to simultaneous rotation of its Taylor coefficients. In the normalization where its first coefficient is positive real, its Schur parameters satisfy
\[
r(\beta)=\frac12+O(\beta^2),\qquad
x(\beta)=-\exp\left(-\frac{10i}{9}\beta+O(\beta^3)\right),
\qquad |x(\beta)|=1.
\]

The displayed all-angle upper-bound expression
\[
B(\beta)=\frac{17(1+\cos(2\beta))+2\cos\beta}
{144(1+\sec^2\beta)}
\]
in Ahamed--Sarkar--Das (2026, Theorems 2.1--2.2) therefore **cannot bound** this locally biholomorphic class near \(\beta=0\), because
\[
\boxed{M(\beta)-B(\beta)=\frac{41}{864}\beta^2+O(\beta^4)>0}
\]
for every sufficiently small nonzero \(\beta\). The counterexample already occurs in the one-dimensional Banach space \(\mathbb C\).

## Assumptions and scope

The class \(\mathcal C_\beta\) is defined by the local-invertibility and half-plane conditions above. It coincides in dimension one with the locally biholomorphic class appearing in Definition 1.3 of the 2026 source. Global injectivity is neither assumed nor concluded; no assertion about a smaller globally univalent subclass is made.

The estimate concerns the complex second Hankel functional
\[
H_{2,2}(f)=a_2a_4-a_3^2.
\]
All angular asymptotics are as \(\beta\to0\) through real values. Constants hidden in the remainder are uniform in a sufficiently small fixed neighborhood of zero.

## Proof

**1. Carathéodory representation and exact objective.** Put
\[
t_\beta=\cos\beta\,e^{-i\beta}.
\]
The defining positivity condition is equivalent to
\[
1+\frac{zf''(z)}{f'(z)}=1+t_\beta(p(z)-1),
\qquad p(0)=1,\quad \operatorname{Re}p(z)>0.
\]
Conversely, every such \(p\) yields an admissible \(f\) through
\[
f'(z)=\exp\left(t_\beta\int_0^z\frac{p(\zeta)-1}{\zeta}\,d\zeta\right),
\qquad f(z)=\int_0^z f'(u)\,du.
\]
The exponential is nonvanishing, and
\(\operatorname{Re}[e^{i\beta}(1+zf''/f')]=\cos\beta\operatorname{Re}p>0\).
Write \(p(z)=1+c_1z+c_2z^2+c_3z^3+\cdots\). Expanding the exponential gives
\[
a_2=\frac{t_\beta c_1}{2},\qquad
 a_3=\frac{t_\beta c_2+t_\beta^2c_1^2}{6},\qquad
 a_4=\frac{t_\beta c_3}{12}+\frac{t_\beta^2c_1c_2}{8}+\frac{t_\beta^3c_1^3}{24}.
\]
Consequently the **exact** complex expression to maximize is
\[
H_{2,2}(f)=\frac{t_\beta^2}{144}
\bigl(6c_1c_3-4c_2^2+t_\beta c_1^2c_2-t_\beta^2c_1^4\bigr).
\tag{1}
\]

**2. Compact Schur parametrization.** Rotating the source variable multiplies the complex Hankel functional by a unimodular fourth power. We may therefore assume \(c_1=2r\) for \(0\le r\le1\). The classical first two Schur steps give every possible first three coefficients as
\[
\begin{aligned}
c_1&=2r,\\
c_2&=2\bigl(r^2+(1-r^2)x\bigr),\\
c_3&=2\bigl(r^3+2r(1-r^2)x
 +(1-r^2)((1-|x|^2)y-rx^2)\bigr),
\end{aligned}
\]
where \(|x|\le1\) and \(|y|\le1\). Every choice arises from a positive-real-part function, including the boundary values; hence the supremum is a maximum over a compact parameter body.

At \(\beta=0\), substituting this parametrization into (1) gives
\[
H_0=\frac{1-r^2}{18}
\bigl(-(2+r^2)x^2+3r^2x+3r(1-|x|^2)y\bigr).
\tag{2}
\]
Writing \(\rho=|x|\), the triangle inequality yields
\[
|H_0|\le\frac{1-r^2}{18}
\bigl((2+r^2)\rho^2+3r^2\rho+3r(1-\rho^2)\bigr)
\le\frac{(1-r^2)(1+2r^2)}9\le\frac18.
\]
The middle inequality follows because the quadratic in \(\rho\in[0,1]\) is nondecreasing, and the last one is maximized at \(r^2=1/4\). Equality forces
\[
r=\frac12,\qquad x=-1,
\]
with \(y\) irrelevant since \(|x|=1\). Indeed the two nonzero complex terms in (2) must align. Thus the zeroth-angle extremal coefficient data are unique modulo rotations.

**3. Persistence on the Schur boundary.** Set \(x=-\rho\) and differentiate the modulus in the outward radial direction, keeping \(y\) fixed. At the unique zeroth-angle maximizer,
\[
\left.\frac{\partial |H|}{\partial\rho}\right|_{{r=1/2,\,\rho=1,\,\beta=0}}
=\frac{21/4+3\operatorname{Re}y}{24}\ge\frac3{32}.
\tag{3}
\]
This strict bound holds uniformly for \(|y|\le1\). Compactness and uniqueness in step 2 imply that all maximizing parameters for sufficiently small \(|\beta|\) lie near \((r,x)=(1/2,-1)\). By continuity, the outward derivative remains strictly positive there for every \(|y|\le1\). A maximizer must therefore have \(\rho=1\), and the free parameter \(y\) disappears. This boundary-rigidity conclusion is essential: maximizing only over degree-two Blaschke products at the outset would not establish a sharp result.

**4. Exact Hessian and envelope expansion.** On the boundary write
\[
x=-e^{i\phi},\qquad
F(r,\phi,\beta)=|H_{2,2}(r,-e^{i\phi},\beta)|^2.
\]
Direct differentiation of (1) at \((r,\phi,\beta)=(1/2,0,0)\) gives vanishing first derivatives and
\[
\begin{gathered}
F_{rr}=-\frac19,\qquad F_{r\phi}=F_{r\beta}=0,\\
F_{\phi\phi}=-\frac3{512},\qquad
F_{\phi\beta}=-\frac5{768},\qquad
F_{\beta\beta}=-\frac{29}{384}.
\end{gathered}
\tag{4}
\]
The Hessian in \((r,\phi)\) is negative definite. The real-analytic implicit-function theorem, together with step 3 and compactness, gives a unique analytic maximizing branch in the rotation normalization. Its first derivatives are
\[
r'(0)=0,\qquad
\phi'(0)=-\frac{F_{\phi\beta}}{F_{\phi\phi}}=-\frac{10}{9}.
\]
Consequently the second-order envelope coefficient is
\[
\begin{aligned}
M(\beta)^2
&=\frac1{64}+\frac12\left(
F_{\beta\beta}-\frac{F_{\phi\beta}^2}{F_{\phi\phi}}
\right)\beta^2+O(\beta^4)\\
&=\frac1{64}-\frac{59}{1728}\beta^2+O(\beta^4).
\end{aligned}
\]
Complex conjugation identifies the classes for opposite angles, so the maximized function is even. Taking the positive square root proves the asserted coefficient \(-59/432\) and fourth-order remainder.

**5. Explicit admissible witness and the displayed upper bound.** Fix the two Schur parameters
\[
r=\frac12,\qquad x_\beta=-e^{-10i\beta/9},
\]
and put
\[
w_\beta(z)=z\frac{1/2+x_\beta z}{1+(x_\beta/2)z},
\qquad p_\beta(z)=\frac{1+w_\beta(z)}{1-w_\beta(z)}.
\]
This is a finite Blaschke construction, so \(|w_\beta(z)|<1\) and \(\operatorname{Re}p_\beta(z)>0\) on \(\mathbb D\). The integral in step 1 therefore produces an explicit locally biholomorphic admissible map. Substituting its first three Carathéodory coefficients into (1) yields
\[
\left|H_{2,2}(f_\beta)\right|=\frac18-\frac{59}{432}\beta^2+O(\beta^4).
\]
On the other hand, Taylor expansion of the formula displayed in Ahamed--Sarkar--Das gives
\[
B(\beta)=\frac18-\frac{53}{288}\beta^2+O(\beta^4).
\]
Subtracting shows that the explicit admissible family already exceeds that formula by
\[
\frac{41}{864}\beta^2+O(\beta^4)
\]
for all sufficiently small nonzero \(\beta\). This proves the strict comparison without using any numerical approximation.

## Verification

The accompanying `verify.py` uses exact SymPy differentiation to recompute the coefficient Hessian, the angular slope, the envelope correction, and the difference from the quoted comparison expression. Run `python verify.py` with SymPy installed. The embedded `verification_output.txt` records the actual exact output, including `EXACT_CHECKS_PASSED`.

For a numerical sanity check, the explicit witness at \(\beta=0.1\) has
\[
|H_{2,2}(f_\beta)|\approx0.123639509894205441,
\quad B(0.1)\approx0.123168708536464139.
\]
This finite numerical evaluation is not used to establish any asymptotic or strict inequality; those follow from the exact proof above.

## Relationship to prior work

Ahamed--Sarkar--Das (2026), whose primary classification is 32H02, defines the β-spirallike quasi-convex Banach-space class and reduces its coefficient problem to Carathéodory data. It states the expression \(B(\beta)\) as an upper bound (Theorems 2.1--2.2), proves its equality at \(\beta=0\), and explicitly leaves the sharp nonzero-angle extremal problem open. The present result determines the previously unstated exact small-angle second variation, the extremal Schur-parameter drift, and an admissible violation of that displayed general bound.


Sarkar--Das (2026, arXiv:2607.12509v1) prove a sharp bound for the second Hankel determinant in the **spirallike**, not spirallike-convex, class, defined by
\[
\operatorname{Re}(e^{i\beta}zg'(z)/g(z))>0.
\]
For a spirallike-convex \(f\), Alexander's transform \(g(z)=zf'(z)\) satisfies that spirallike condition, but transforms the Hankel invariant as
\[
H_{2,2}(g)=8a_2a_4-9a_3^2,
\]
not as \(a_2a_4-a_3^2\). The sharp spirallike bound \(|H_{2,2}(g)|\le\cos^2\beta\) therefore does not determine this convex-spirallike small-angle extremum. Długosz--Liczberski--Trybucka (2026) likewise prove a sharp bound for unrotated starlike maps; their class does not retain the present nonlinear spiral-angle structure.

The cited predecessor by Krishna--Reddy (2015) studies second Hankel bounds for analytic functions. The 2026 source attributes the same upper-bound formula to its Theorem 3.3. Its complete original text was not independently accessible for comparison, so no statement is made about the exact assumptions or validity of that earlier theorem. Other Banach-space determinant works, including Xu--Długosz--Liczberski (2025), concern a third-order rather than the present second-order determinant. Hamada (2023) treats Fekete--Szegö functionals, not the present two-parameter sharp Hankel envelope.

## Limitations

Only the germ of the sharp constant near \(\beta=0\) is determined. No all-angle formula is claimed. No sharp characterization for an additional globally univalent constraint, nor an optimizer classification in Banach spaces of dimension greater than one, is asserted. The displayed comparison concerns the 2026 manuscript's stated formula under its locally biholomorphic Definition 1.3; it does not attribute the same wording to the inaccessible 2015 full text.

## References

1. M. B. Ahamed, N. Sarkar, and P. Das, *Second Hankel Determinant for \(\beta\)-Spirallike Convex Mappings in Complex Banach Spaces*, arXiv:2608.07563v1; author-uploaded public full text, ResearchGate publication 411145891, August 3, 2026.
2. D. Vamshee Krishna and T. Ram Reddy, *Coefficient inequality for certain subclasses of analytic functions associated with Hankel determinant*, Indian Journal of Pure and Applied Mathematics 46 (2015), 91--106, DOI: 10.1007/s13226-015-0111-1.
3. Q. Xu, R. Długosz, and P. Liczberski, *The sharp bound of the third Hankel determinant for quasi-convex mappings in complex Banach spaces*, Complex Analysis and Operator Theory 20 (2026), article 36, DOI: 10.1007/s11785-025-01888-z.
4. H. Hamada, *Fekete--Szegö problems for spirallike mappings and close-to-quasi-convex mappings on the unit ball of a complex Banach space*, Results in Mathematics 78 (2023), article 109.
5. N. Sarkar and P. Das, *On Hankel Determinants of \(\beta\)-Spirallike Mappings in Complex Banach Spaces*, arXiv:2607.12509v1, July 14, 2026.
6. R. Długosz, P. Liczberski, and E. Trybucka, *Hankel Determinants for Holomorphic Functions and Biholomorphic Mappings in Banach Spaces*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 138, DOI: 10.1007/s40840-026-02137-y.
