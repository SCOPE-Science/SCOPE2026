# Sharp perimeter–radius phase diagram for lattice-free ellipses

## Finding
Let \(\Lambda\subset\mathbb R^2\) be any full-rank Euclidean lattice, let \(\rho(\Lambda)=\max_{z\in\mathbb R^2}\min_{v\in\Lambda}\lVert z-v\rVert_2\) denote its covering radius, and let \(\mathcal E_\Lambda\) be the set of all nondegenerate closed ellipses whose interiors contain no lattice point. For any real penalty coefficient \(\lambda\), define
\[
M_\Lambda(\lambda)=\sup_{E\in\mathcal E_\Lambda}\bigl(P(E)-\lambda R(E)\bigr),
\]
where \(P\) is Euclidean perimeter and \(R\) the Euclidean circumradius. Then the following **complete sharp phase diagram** holds:
\[
\boxed{
M_\Lambda(\lambda)=
\begin{cases}
+\infty,&\lambda<4,\\
(2\pi-\lambda)\rho(\Lambda),&4\le\lambda\le2\pi,\\
0,&\lambda>2\pi.
\end{cases}}
\]
For \(4\le\lambda<2\pi\), precisely the radius-\(\rho(\Lambda)\) disks centered at deepest holes of the lattice attain the supremum. At \(\lambda=2\pi\), precisely **all lattice-free disks** attain it. At \(\lambda>2\pi\), the supremum is not attained. Below \(\lambda=4\), the functional is unbounded above already among arbitrarily elongated ellipses in a fixed lattice-free strip.

For the square lattice \(\mathbb Z^2\), \(\rho(\mathbb Z^2)=1/\sqrt2\). In particular, the sharp ellipse-only version of the perimeter–circumradius question is
\[
\boxed{P(E)-4R(E)\le\sqrt2(\pi-2)=1.6144558134\ldots,}
\]
with equality precisely for radius-\(1/\sqrt2\) disks centered at points \((k+1/2,\ell+1/2)\), \(k,\ell\in\mathbb Z\). Since the diameter of any ellipse is twice its circumradius, the same sharp statement concerns \(P(E)-2D(E)\), where \(D\) is its diameter.

## Assumptions and scope
A full-rank planar lattice is \(\Lambda=\mathbb Zu+\mathbb Zv\) with linearly independent \(u,v\in\mathbb R^2\). Its covering radius is finite and attained because the distance to the lattice is continuous and periodic on a compact fundamental parallelogram. An ellipse is a translation and rotation of a set with semiaxes \(a\ge b>0\). Lattice-free means \(\operatorname{int}(E)\cap\Lambda=\varnothing\); lattice points on the boundary are permitted. No restriction is placed on the ellipse center or orientation. The coefficient \(\lambda\) is any real number. The three cases above exhaust all coefficients and include the two threshold values with their exact attainment conditions.

## Proof
**1. Elliptic perimeter inequality and its strictness.** In principal-axis coordinates, the ellipse with semiaxes \(a\ge b>0\) has circumradius \(a\) and perimeter
\[
P(a,b)=4\int_0^{\pi/2}\sqrt{a^2\sin^2\theta+b^2\cos^2\theta}\,d\theta.
\]
For fixed \(b>0\), differentiating under the integral gives
\[
\frac{\partial P}{\partial a}=4\int_0^{\pi/2}
\frac{a\sin^2\theta}{\sqrt{a^2\sin^2\theta+b^2\cos^2\theta}}\,d\theta
<4\int_0^{\pi/2}\sin\theta\,d\theta=4.
\]
The inequality is strict for every finite \(a\ge b>0\), since the integrands differ strictly on the whole open interval. Integrating from \(b\) to \(a\) and using \(P(b,b)=2\pi b\), for every \(\lambda\ge4\) this yields
\[
P(a,b)-\lambda a\le (2\pi-\lambda)b,
\]
with equality exactly when \(a=b\). The statement remains valid when the right-hand side is nonpositive.

**2. Lattice constraint.** An ellipse with minor semiaxis \(b\) contains the closed Euclidean disk of radius \(b\) about its center \(z\). By the definition of \(\rho(\Lambda)\), some lattice point is at distance at most \(\rho(\Lambda)\) from \(z\). If \(b>\rho(\Lambda)\), that point lies strictly inside the disk, contradicting lattice-freeness. Hence every admissible ellipse has \(b\le\rho(\Lambda)\). Conversely, at any deepest hole \(z\) of the lattice, the disk \(\overline B(z,\rho(\Lambda))\) has no interior lattice points and is admissible.

**3. Bounded branch and equality.** If \(4\le\lambda<2\pi\), the two preceding inequalities give
\[
P(E)-\lambda R(E)\le(2\pi-\lambda)b\le(2\pi-\lambda)\rho(\Lambda).
\]
The deepest-hole disk realizes equality. Equality in the first step forces \(a=b\), and equality in the second forces \(b=\rho(\Lambda)\), proving the full optimizer classification. For \(\lambda=2\pi\), the bound is zero and equality in the first step holds precisely for circles; each lattice-free circle is admissible. For \(\lambda>2\pi\), the first inequality gives a strictly negative value for any admissible ellipse, but shrinking admissible disks to radius zero makes the value tend to zero, proving an unattained supremum of zero.

**4. Unbounded branch.** Choose any primitive lattice vector \(u\) and consider the parallel lattice rows in its direction, whose perpendicular spacing is \(h>0\). The open strip between two consecutive rows contains no lattice point. Fix \(0<b<h/2\), center an ellipse halfway between the rows, direct its major axis along \(u\), and let its major semiaxis \(a\) grow without bound. Every such ellipse is lattice-free. Its boundary consists of two arcs joining opposite major-axis endpoints, each of length at least \(2a\), so \(P(a,b)\ge4a\). Thus for \(\lambda<4\),
\[
P(a,b)-\lambda a\ge(4-\lambda)a\longrightarrow+\infty.
\]
This completes all branches and their sharpness statements.

**5. Square-lattice specialization.** Coordinatewise nearest-integer rounding gives \(\min_{v\in\mathbb Z^2}\lVert z-v\rVert_2\le1/\sqrt2\), with equality exactly when both coordinates are half-integers. Therefore \(\rho(\mathbb Z^2)=1/\sqrt2\) with precisely the specified deepest holes modulo lattice translations. Substitution at \(\lambda=4\) proves the numerical and equality assertions.

## Verification
The crucial continuous inequality was proved by a strict integral comparison, not by a computation. The covering-radius argument is exact and works for every full-rank lattice. The auxiliary `verify.py` numerically integrates the perimeter and its derivative for representative semiaxis pairs, tests five coefficient values, checks square-lattice extremal disks, and checks elongated ellipses confined to a lattice-free strip. Running `python3 verify.py` produced `VERIFY_OK`; these finite diagnostics are not an exhaustive proof of the quantified theorem.

## Relationship to prior work
González Merino and Henze formulated the general lattice-free perimeter–circumradius bound \(P-4R\le2\) for the square lattice and proved it for unconditional bodies, along with other partial inequalities. The current formula gives the sharp smaller constant for **all ellipses, regardless of orientation**, and determines the entire coefficient phase diagram for **every full-rank lattice**. It neither proves the conjectured universal bound for nonsmooth arbitrary bodies nor improves the sharp general rectangular-strip examples. Pain examined upper estimates for ellipse perimeter without a lattice constraint. Those estimates and the classical lattice-covering observation are relevant ingredients, but the cited texts do not state the lattice-free ellipse extremum, optimizer classification, or coefficient thresholds. A published record of a stronger triangle-only lattice-free bound concerns a distinct shape class and is not asserted to imply the ellipse theorem.

## Limitations
The theorem is restricted to nondegenerate ellipses and Euclidean perimeter and circumradius in the plane. It does not give bounds for arbitrary lattice-free convex bodies or higher-dimensional ellipsoids. The proof is elementary and could have been independently obtained in earlier lattice-free geometry or ellipse-perimeter literature not indexed in the searches; no claim of exhaustive historical priority or independent validation is made. Numerical checks concern only sample parameters and do not verify infinite quantifiers.

## References
1. B. González Merino and M. Henze, *A remark on perimeter-diameter and perimeter-circumradius inequalities under lattice constraints*, arXiv:1310.6534v1 (public 24 October 2013), https://arxiv.org/pdf/1310.6534 .
2. J.-C. Pain, *A simple upper bound for the perimeter of an ellipse*, arXiv:2205.12266v1 (public 23 May 2022), https://arxiv.org/pdf/2205.12266 .
