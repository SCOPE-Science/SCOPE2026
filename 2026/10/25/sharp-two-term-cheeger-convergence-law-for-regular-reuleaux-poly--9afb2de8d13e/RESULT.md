# Sharp two-term Cheeger convergence law for regular Reuleaux polygons

## Finding
For each odd integer \(n\ge3\), the regular Reuleaux \(n\)-gon \(K_n\) of width one has planar Cheeger constant \(h_n\) satisfying
\[
h_n=4+\frac{5\pi^2}{18n^2}+\frac{2063\pi^4}{38880n^4}+O(n^{-6}),
\qquad n\to\infty\ \text{through odd integers}.
\]
Equivalently, its Cheeger radius \(t_n=1/h_n\) satisfies
\[
t_n=\frac14-\frac{5\pi^2}{288n^2}-\frac{1313\pi^4}{622080n^4}+O(n^{-6}).
\]
For area \(A_n=|K_n|\),
\[
\frac\pi4-A_n=\frac{\pi^3}{48n^2}+O(n^{-4}),
\qquad
\lim_{n\to\infty\atop n\ \mathrm{odd}}
\frac{h_n-4}{\pi/4-A_n}=\frac{40}{3\pi}.
\]
Thus the Cheeger gap has an exact nonzero quadratic rate and a determined fourth-order correction, whereas the disk of width one has Cheeger constant \(4\).

## Assumptions and scope
All sets are in the Euclidean plane. Fix odd \(n\ge3\), put \(z=\pi/n\), and define
\[
R=\frac1{2\cos(z/2)},\quad
v_j=R(\cos(2\pi j/n),\sin(2\pi j/n)),\quad
K_n=\bigcap_{j=0}^{n-1}\overline B(v_j,1).
\]
This is the standard width-one regular Reuleaux \(n\)-gon. For a measurable set \(E\) of finite perimeter, write \(P(E)\) for its De Giorgi perimeter and \(|E|\) for its area; the Cheeger constant is \(h_n=\inf\{P(E)/|E|:E\subseteq K_n,\ |E|>0\}\). Its unique relevant Cheeger radius is \(t_n=1/h_n\). Only odd \(n\) are in the statement; the remainder \(O(n^{-6})\) is uniform along this sequence for all sufficiently large odd \(n\).

## Proof
**Step 1: the erosion and its exact area.** For \(0\le t<1-R\), let \(\rho=1-t\). Euclidean erosion by a closed radius-\(t\) disk commutes with intersection, and the erosion of a disk is a concentric disk with decreased radius, so
\[
(K_n)_{-t}=\bigcap_{j=0}^{n-1}\overline B(v_j,\rho).
\]
Because \(n\) is odd, the most restrictive center for a ray in any of the \(n\) symmetric angular sectors is an antipodal center. Parametrize a representative sector by \(-z\le\theta\le z\), measured from the direction opposite its restrictive center. The radial boundary is therefore
\[
r_\rho(\theta)=-R\cos\theta+\sqrt{\rho^2-R^2\sin^2\theta}.
\]
This expression is nonnegative for the relevant erosions, since \(\rho\ge R\) and the centered inradius is \(1-R\). Polar integration gives
\[
F_n(\rho):=\left|\bigcap_j\overline B(v_j,\rho)\right|
=\frac n2\int_{-z}^z r_\rho(\theta)^2\,d\theta.
\]
Evaluating the elementary integral yields the exact finite-\(n\) formula
\[
F_n(\rho)=n\left[\rho^2\left(z-\arcsin\frac{R\sin z}{\rho}\right)
+\frac{R^2}2\sin(2z)
-R\sin z\sqrt{\rho^2-R^2\sin^2z}\right].
\]
For all \(n\ge3\) odd, \(F_n(1)>0\) and \(F_n(R)=0\). As \(t\) increases, \(F_n(1-t)\) decreases continuously and strictly until it reaches zero, whereas \(\pi t^2\) increases strictly. The planar convex Cheeger characterization of Lachand-Robert and Kawohl, as stated for example in Henrot–Lucardesi and Bogosel, says that the unique \(t_n\in(0,1-R)\) satisfying
\[
F_n(1-t_n)=\pi t_n^2
\]
is precisely \(1/h_n\).

**Step 2: uniform analytic expansion.** Set \(\theta=zu\), with \(-1\le u\le1\), and provisionally write
\[
t=\frac14+a z^2+b z^4.
\]
Substitution of \(R=\tfrac12\sec(z/2)\), \(\rho=1-t\), followed by Taylor expansion of the **exact** square root gives, uniformly in \(u\in[-1,1]\),
\[
\begin{aligned}
r_\rho(zu)={}&\frac14+z^2\left(-a+\frac{u^2}{12}-\frac1{16}\right)\\
&+z^4\left(-b-\frac{2au^2}{9}+\frac{7u^4}{432}-\frac{u^2}{96}-\frac5{768}\right)+O(z^6).
\end{aligned}
\]
Uniformity follows because for \(z\) near zero, \(u\in[-1,1]\), and \(t\) near \(1/4\), the square-root argument stays bounded strictly away from zero. Since \(nz=\pi\), the exact area identity becomes
\[
\frac{F_n(1-t)}\pi=\frac12\int_{-1}^1r_{1-t}(zu)^2\,du.
\]
The moments \(\tfrac12\int_{-1}^1u^2du=1/3\) and \(\tfrac12\int_{-1}^1u^4du=1/5\) yield
\[
\frac{F_n(1-t)}\pi-t^2
=z^2\left(-a-\frac5{288}\right)
+z^4\left(\frac{7a}{216}-b-\frac{107}{69120}\right)+O(z^6).
\]
For \(z=0\), the corresponding disk radius is \(1/2\), so the last expression with unrestricted \(t\) is exactly \((1/2-t)^2-t^2=1/4-t\). Its derivative with respect to \(t\) is \(-1\) at \(t=1/4\). The analytic implicit-function theorem therefore supplies a unique even analytic solution \(t(z)\) for all sufficiently small \(z\), and its coefficients must cancel the displayed powers. Hence
\[
a=-\frac5{288},\qquad b=-\frac{1313}{622080}.
\]
Taking the reciprocal of \(t(z)\) gives the asserted expansion for \(h_n\), including the \(O(z^6)\) remainder. This establishes the statement for all sufficiently large odd \(n\); the implicit defining equation already holds for every odd \(n\ge3\).

**Step 3: exact leading area-normalized gap.** Repeat the polar integral at \(t=0\). Taylor expansion of its exact radial integrand gives
\[
\frac{|K_n|}\pi=\frac14-\frac{z^2}{48}+O(z^4).
\]
Therefore \(\pi/4-|K_n|=\pi z^2/48+O(z^4)\), while \(h_n-4=5z^2/18+O(z^4)\). Their quotient converges to \(40/(3\pi)\), as claimed.

## Verification
Run the standalone file `check_cheeger.py` using Python with SymPy and mpmath available. It symbolically reconstructs the fourth-order radial jet, integrates its moments, solves the two coefficient equations in exact rational arithmetic, and checks the disk-area deficit. It also solves the exact finite-\(n\) area equation at eight odd values from \(3\) to \(401\) with 60-digit arithmetic. The numeric solves are consistency checks only, not a proof for unbounded \(n\); the all-\(n\) asymptotic follows from analytic implicit-function theory above. At \(n=3\), the \(t=0\) formula reproduces the classical Reuleaux triangle area \((\pi-\sqrt3)/2\).

## Relationship to prior work
Falco–Myroshnychenko (2026) identifies regular Reuleaux \(n\)-gons as the area minimizers in odd cyclic-symmetry classes, motivating quantitative comparisons of their geometric functionals. Pan–Yao–Zhang (2026) establishes that the regular Reuleaux \(n\)-gon minimizes the Cheeger constant among Reuleaux polygons with at most \(n\) sides. Consequently the stated asymptotics also quantify the optimal Cheeger values for those finite-complexity classes, assuming that published theorem. Neither classification itself is asserted as new. Henrot–Lucardesi (2020) gives the convex Cheeger erosion criterion and discusses exact computation for regular Reuleaux polygons; Bogosel (2023) treats inner parallel sets of constant-width bodies. The new quantitative content here is the exact quadratic and quartic Cheeger coefficients and the area-normalized leading ratio. Existing exact-area formulas imply implicit numerical computability, which is not the asserted novelty.

## Limitations
No assertion is made about arbitrary nonregular constant-width bodies, monotonicity in \(n\), closed forms for the roots at finite \(n\), or the next \(n^{-6}\) coefficient. Some recent closely relevant literature was available only as an abstract rather than full text; the risk that it already contains the asymptotic coefficients cannot be eliminated by the accessible comparison. There is no independent scientific audit or certification.

## References
1. J. Falco and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width* (2026), arXiv:2608.05125; first public 2026-08-05. https://arxiv.org/abs/2608.05125
2. S. Pan, T. Yao and Q. Zhang, *Minimization of the Cheeger Constant for Reuleaux Polygons*, Proc. Amer. Math. Soc. **154** (2026), 3495–3506. https://doi.org/10.1090/proc/17686
3. A. Henrot and I. Lucardesi, *A Blaschke–Lebesgue Theorem for the Cheeger Constant* (2020), arXiv:2011.07244. https://arxiv.org/abs/2011.07244
4. B. Bogosel, *On the Blaschke–Lebesgue theorem for the Cheeger constant* (2023), arXiv:2303.15559. https://arxiv.org/abs/2303.15559
