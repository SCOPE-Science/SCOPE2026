# Circular-lens Berezin ranges of nonlinear monomial composition operators

## Finding
For the Hardy Hilbert space \(H^2(\mathbb D)\) and every integer \(m\ge2\), the Berezin range of composition by \(\varphi(z)=\lambda z^m\), \(|\lambda|\le1\), depends only on \(a=|\lambda|\), not on \(m\) or the phase of \(\lambda\). For \(0<a<1\), set \(b=\sqrt{1-a^2}\) and \(R=1/(2a)\). Then
\[
\operatorname{Ber}(C_{\lambda z^m})=\bigl(\overline D(1/2+ib/(2a),R)\cap\overline D(1/2-ib/(2a),R)\bigr)\setminus\{0\}.
\]
Here \(\overline D(c,R)=\{z\in\mathbb C:|z-c|\le R\}\). This is an exactly convex circular lens with one boundary point removed, and remains convex. Its planar area, boundary length, and maximal absolute imaginary coordinate are, respectively,
\[
A(a)=\frac{\arcsin a-a\sqrt{1-a^2}}{2a^2},\qquad P(a)=\frac{2\arcsin a}{a},\qquad H(a)=\frac{1-\sqrt{1-a^2}}{2a}.
\]
For \(a=0\), the range is \((0,1]\). For \(a=1\), the range is \(\{z:|z-1/2|<1/2\}\cup\{1\}\), namely the open diameter disk plus its point \(1\). Thus the parameter \(a=1\) changes boundary attainment: for \(0<a<1\), every point of the lens boundary other than \(0\) is attained, whereas at \(a=1\) no boundary point other than \(1\) is attained.

## Assumptions and scope
Let \(k_w(z)=(1-\overline wz)^{-1}\) and \(\widehat k_w=(1-|w|^2)^{1/2}k_w\). The Berezin range of a bounded operator \(T\) means \(\{\langle T\widehat k_w,\widehat k_w\rangle:w\in\mathbb D\}\), with inner product linear in the first variable. Each \(z\mapsto\lambda z^m\) is a disk self-map, and the induced composition operator is bounded on \(H^2\). The formula holds for all integers \(m\ge2\), including \(|\lambda|=0,1\); it is not asserted for \(m=1\).

## Proof
The reproducing identity gives
\[
\langle C_\varphi\widehat k_w,\widehat k_w\rangle=\frac{1-|w|^2}{1-\overline w\varphi(w)}=\frac{1-t}{1-\lambda t e^{i(m-1)\theta}},\quad w=\sqrt t e^{i\theta},\quad 0\le t<1.
\]
For \(m\ge2\), \(\lambda e^{i(m-1)\theta}\) runs through the entire circle of radius \(a\). Calling the displayed transform value \(z\), introduce \(u=(1-z)/z\). The denominator cannot vanish, and \(z\ne0\). Rearranging yields
\[
u=s(1-ae^{i\psi}),\qquad s=\frac{t}{1-t}\in[0,\infty).
\]
For \(0<a<1\), the union of these circles is **exactly** the closed sector
\[
S_a=\{u\in\mathbb C:\operatorname{Re}u\ge\sqrt{1-a^2}|u|\}.
\]
Indeed every represented \(u\) has \(\operatorname{Re}u=s(1-a\cos\psi)\ge0\) and \(|\operatorname{Im}u|\le a\operatorname{Re}u/\sqrt{1-a^2}\), geometrically the tangents to the radius-\(a s\) circle at center \(s\). Conversely, for \(u=U+iV\ne0\) in that sector, the quadratic equation \(|u-s|^2=a^2s^2\) has a nonnegative root
\[
s=\frac{U+\sqrt{a^2U^2-(1-a^2)V^2}}{1-a^2}>0,
\]
which yields \(e^{i\psi}=(1-u/s)/a\) of unit modulus. For \(u=0\), take \(s=0\). Thus the transformed range is precisely \(\{(1+u)^{-1}:u\in S_a\}\). With \(z=x+iy\ne0\), we have
\[
\operatorname{Re}\frac{1-z}{z}=\frac{x-|z|^2}{|z|^2},\qquad \operatorname{Im}\frac{1-z}{z}=-\frac{y}{|z|^2}.
\]
The sector inequality is equivalent to
\[
x-|z|^2\ge\frac{\sqrt{1-a^2}}{a}|y|,
\]
which, by completing squares for each choice of sign, is exactly the intersection of the two stated closed disks. The origin is the only missing point, since \(u\) must be finite. Removing this extreme point preserves convexity: a proper convex combination of nonzero points in the lens cannot be zero because the lens lies in \(\operatorname{Re}z\ge0\) and meets the imaginary axis only at zero.

The disk centers have separation \(b/a\), while both radii are \(1/(2a)\). Standard sector-circle geometry gives half-angle \(\delta=\arcsin a\): the two boundary arcs each have length \(\delta/a\), and the equal-radius disk-intersection area is
\[
2R^2\delta-\frac{b}{2a}\sqrt{4R^2-(b/a)^2}=\frac{\delta-ab}{2a^2}.
\]
The point of maximal imaginary coordinate lies on the perpendicular bisector of the joining chord and has height \(R-b/(2a)=(1-b)/(2a)\). Deleting the origin leaves these geometrical measures unchanged.

For \(a=0\), the transform becomes \(1-t\) and has range \((0,1]\). For \(a=1\), \(u=s(1-e^{i\psi})\): every nonzero represented \(u\) has strictly positive real part, and conversely every \(U+iV\) with \(U>0\) is represented by \(s=(U^2+V^2)/(2U)>0\); additionally \(u=0\) is represented. Under \(z=(1+u)^{-1}\), \(\operatorname{Re}u>0\) is exactly \(|z-1/2|<1/2\), while \(u=0\) maps to \(z=1\). This proves the endpoint claim.

## Verification
A standalone script `check_lens.py` evaluates the analytic parametrization against both the sector inequalities and the two-disk membership inequalities for deterministic grids, and reconstructs admissible kernel parameters from sampled sector points. It also cross-checks the lens area, perimeter, and maximal height formulas against independent one-dimensional quadrature. These are diagnostic checks only; the all-parameter claim follows from the displayed algebra and geometry.

## Relationship to prior work
Augustine, Das, Bhunia and Shankar (arXiv:2507.22427v1, posted 2025-07-30) investigate convexity of Berezin ranges for Hardy composition operators. Their accessible Theorem 3.5 concerns a radial expression \(\varphi(z)=\zeta |z|^k z\), not the holomorphic monomials \(\lambda z^m\) with exponent at least two. Bourdon, Le and Thompson (arXiv:2610.17634v1, posted 2026-10-13) subsequently studied Berezin ranges of composition operators on \(H^2\), with abstract-level convexity criteria for **linear** symbols. Cowen and Felder (arXiv:2109.12095) and Augustine, Garayev and Shankar (Complex Analysis and Operator Theory 17 (2023), article 126) established earlier convexity phenomena for linear and automorphic symbols. This classification concerns the genuinely nonlinear monomial family \(\lambda z^m\), \(m\ge2\), with complete boundary attainment and lens geometry. The recent papers' complete full texts were unavailable during comparison; its abstract does not assert this lens classification, but a latent equivalent formulation in the full article has not been ruled out.

## Limitations
The theorem is confined to the classical Hardy kernel and nonlinear monomial symbols, not arbitrary finite Blaschke products, affine maps, or weighted Bergman kernels. The result is an elementary exact classification, not a new general theory of Berezin convexity. Priority is provisional because the October 2026 paper could only be inspected at abstract level and part of the older literature was examined through accessible textual excerpts; independent audit and comprehensive publication-priority confirmation have not occurred.

## References
1. A. Augustine, P. Hiran Das, P. Bhunia, P. Shankar, *On the convexity of Berezin range and Berezin radius inequalities via a class of semi-norms*, arXiv:2507.22427v1 (2025-07-30), https://arxiv.org/abs/2507.22427.
2. P. Bourdon, T. Le, D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)*, arXiv:2610.17634v1 (2026-10-13), https://arxiv.org/abs/2610.17634.
3. C. C. Cowen and C. Felder, *Convexity of the Berezin Range*, arXiv:2109.12095 (2021), https://arxiv.org/abs/2109.12095.
4. A. Augustine, M. Garayev, P. Shankar, *Composition Operators, Convexity of Their Berezin Range and Related Questions*, Complex Analysis and Operator Theory 17 (2023), article 126, DOI:10.1007/s11785-023-01432-x.
