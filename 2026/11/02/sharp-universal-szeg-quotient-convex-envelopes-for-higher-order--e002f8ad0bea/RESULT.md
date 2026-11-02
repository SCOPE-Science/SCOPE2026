# Sharp universal Szegő-quotient convex envelopes for higher-order disk zeros

## Finding

For every integer \(m\ge 2\), let \(\mathcal S_m\) consist of all holomorphic functions \(f:\mathbb D\to\mathbb D\) whose zero at the origin has order at least \(m\). For such a function define the normalized Szegő-kernel quotient
\[
\mathcal B_f(z)=\frac{1-|z|^2}{1-\overline z f(z)},\qquad z\in\mathbb D.
\]
Set \(c_m=1/(m+1)\), and let \(\mathcal K_m\) be the closed convex hull of the point \(1\) and the closed Euclidean disk \(\{w:|w-c_m|\le c_m\}\). Then
\[
\boxed{\ \mathcal B_f(\mathbb D)\subset\mathcal K_m\quad\text{for every }f\in\mathcal S_m,\qquad
\overline{\operatorname{conv}}\,\mathcal B_{z^m}(\mathbb D)=\mathcal K_m.\ }
\]
Thus a *single* degree-\(m\) power map simultaneously makes the universal convex envelope optimal in every supporting direction. Explicitly, for each real \(\vartheta\),
\[
\boxed{\ \sup_{f\in\mathcal S_m}\sup_{z\in\mathbb D}\operatorname{Re}(e^{-i\vartheta}\mathcal B_f(z))
=\max\left\{\cos\vartheta,\frac{1+\cos\vartheta}{m+1}\right\}.
\ }
\]
The support changes branch precisely at \(\cos\vartheta=1/m\). The two nontrivial tangent points of the boundary are
\[
\boxed{\ t_\pm=\frac1m\pm i\,\frac{\sqrt{m^2-1}}{m(m+1)}.\ }
\]
The boundary is the two straight segments from \(1\) to \(t_\pm\), together with the major circular arc of \(\{w:|w-c_m|=c_m\}\) joining the tangent points. Its exact area and perimeter are
\[
\boxed{\ \operatorname{Area}(\mathcal K_m)=\frac{\sqrt{m^2-1}+\pi-\arccos(1/m)}{(m+1)^2},\quad
\operatorname{Perimeter}(\mathcal K_m)=\frac{2\sqrt{m^2-1}+2\pi-2\arccos(1/m)}{m+1}.\ }
\]
In particular, \(\operatorname{Area}(\mathcal K_m)\sim1/m\) and \(\operatorname{Perimeter}(\mathcal K_m)\to2\) as \(m\to\infty\). These are two-dimensional area and boundary-length statements, respectively.

## Assumptions and scope

The unit disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The integer \(m\) is at least two. Zero maps are allowed in \(\mathcal S_m\), interpreted as vanishing to every order. For \(z=0\), the quotient is defined by the displayed formula and equals \(1\). All convex hulls and disks are in the Euclidean complex plane, and an overline denotes topological closure. The result concerns the sharp *closed convex envelope* of the quotient values; it does not assert that each individual range is convex. No boundary extension of \(f\) is required.

For the Hardy space \(H^2(\mathbb D)\) with normalized Szegő kernel \(k_z(w)=\sqrt{1-|z|^2}/(1-\overline z w)\), the quotient is the Berezin symbol \(\langle C_f k_z,k_z\rangle\) of composition \(C_fh=h\circ f\), under the conventional choice of inner-product orientation. This gives a reproducing-kernel interpretation but does not change the function-theoretic assumptions.

## Proof

**Step 1: exact fixed-radius disk bound.** By the iterated Schwarz lemma, \(f(z)=z^m g(z)\) for an analytic \(g\) with \(|g(z)|\le1\). Put \(s=|z|^2\). Then \(|\overline z f(z)|\le s^{(m+1)/2}\). For \(0<s<1\), the Möbius map \(v\mapsto(1-s)/(1-v)\) sends the closed disk \(|v|\le s^{(m+1)/2}\) onto a closed disk \(D_s\) whose center and radius are
\[
q_s=\frac{1-s}{1-s^{m+1}}=\frac1{1+s+\cdots+s^m},\qquad
\rho_s=q_s s^{(m+1)/2}.
\]
Consequently \(\mathcal B_f(z)\in D_s\) whenever \(|z|^2=s\), for every permitted \(f\).

**Step 2: a sharp convex containment.** Arithmetic–geometric mean gives
\[
\sum_{j=1}^m s^j\ge m\left(\prod_{j=1}^m s^j\right)^{1/m}
=m s^{(m+1)/2};
\]
hence
\[
\rho_s\le\frac{1-q_s}{m}.
\]
The closed disk with center \(q_s\) and radius \((1-q_s)/m\) is precisely the Minkowski interpolation between the singleton \(\{1\}\) and the disk of center and radius \(c_m\), with parameter \(\lambda=(1-q_s)/(1-c_m)\in[0,1]\). Therefore \(D_s\subset\mathcal K_m\). The case \(z=0\) follows from \(\mathcal B_f(0)=1\). This proves the universal inclusion.

**Step 3: simultaneous sharpness in every direction.** For \(f(z)=z^m\), write \(z=\sqrt{s}e^{it}\). Then \(\overline z f(z)=s^{(m+1)/2}e^{i(m-1)t}\), which traverses the entire boundary of its modulus disk when \(t\) traverses the circle because \(m-1\ge1\). Thus \(\mathcal B_{z^m}(\{|z|=\sqrt{s}\})\) is the boundary circle of \(D_s\), not merely a subset. As \(s\uparrow1\), \(q_s\to c_m\) and \(\rho_s\to c_m\), so every point of the outer circle \(|w-c_m|=c_m\) is a limit point of \(\mathcal B_{z^m}(\mathbb D)\). The point \(1\) itself is obtained at \(z=0\). Convexification and closure supply \(\mathcal K_m\); Step 2 supplies the reverse inclusion. Since support functions respect convexification, the universal support is the maximum of the support of the singleton \(\{1\}\), namely \(\cos\vartheta\), and that of the disk, namely \(c_m(1+\cos\vartheta)\). Equality of these two branches is equivalent to \(\cos\vartheta=1/m\).

**Step 4: tangent geometry and size.** The distance from the external point \(1\) to the disk center is \(d=m/(m+1)\), and the disk radius is \(r=1/(m+1)\). The tangent-segment length is \(\ell=\sqrt{d^2-r^2}=\sqrt{m^2-1}/(m+1)\), and the angle between the center-to-point ray and a tangent radius is \(\alpha=\arccos(r/d)=\arccos(1/m)\). Orthogonality gives the displayed \(t_\pm\). The boundary arc has central angle \(2(\pi-\alpha)\); adding two tangent lengths yields \(2\ell+2r(\pi-\alpha)\) for the perimeter. Green's theorem, or decomposition into the major circular segment and the external tangent triangle, yields \(r^2(\pi-\alpha)+r\ell\) for the area. These equal the boxed expressions. The asymptotics use \(\ell=1+O(1/m)\), \(r=O(1/m)\), and \(\alpha\to\pi/2\).

**Step 5: an operator-theoretic scale comparison.** For the monomial composition operator \(C_{z^m}\) on \(H^2\), the monomial basis splits orthogonally into the one-dimensional invariant space spanned by \(1\) and unilateral-shift chains spanned by \(\{z^{q m^j}:j\ge0\}\), where \(q\) runs through positive integers not divisible by \(m\). Hence \(C_{z^m}\) is unitarily equivalent to the direct sum of \(1\) and countably many unilateral shifts. The numerical range of a unilateral shift is the open unit disk; therefore the numerical range of this direct sum is \(\mathbb D\cup\{1\}\) and its closure is the closed unit disk. Meanwhile the closed convex hull of its Szegő-kernel Berezin range is \(\mathcal K_m\). Their exact area difference is \(\pi-\operatorname{Area}(\mathcal K_m)\), approaching \(\pi\) as \(m\to\infty\). This comparison uses the standard shift numerical-range fact and is not claimed as a new calculation of the ordinary numerical range.

## Verification

The inequality in Step 2 is strict for \(0<s<1\) and \(m\ge2\), because the geometric progression \(s,s^2,\ldots,s^m\) has unequal entries. This eliminates possible fixed-radius boundary exceptions. The \(s\uparrow1\) limit is taken only after computing exact circle images for the monomial extremizer; a finite sampling of \(s\) cannot prove this limit. The supplementary standard-library checker in `CHECK.py` tests the AM–GM disk containment on exact rational grids, support inequalities in selected directions, tangency orthogonality, and monomial-circle identities. It does not replace the proof for all integers and all disk points. Run `python3 CHECK.py` from the extracted package directory.

## Relationship to prior work

Bourdon–Le–Thompson (first posted October 13, 2026) give the general normalized Hardy composition Berezin formula, sharp scalar bounds, examples of circular fibers, and a global study of convexity and boundary corners. In particular their Proposition 3.7 treats the family \(f(z)=z\psi(z^n)\) with linear-fractional \(\psi\), including the degree-two power case. Those circle and qualitative results do not state a common optimal convex target over **all** disk maps with a prescribed higher-order zero, its all-direction support function, or the explicit degree-dependent area and tangent geometry proved here. The new input is a uniform AM–GM disk interpolation combined with sharpness of the monomial family.

Cowen–Felder (2021 preprint) discuss Berezin-range convexity for composition operators, and Augustine–Garayev–Shankar (2023 preprint) examine linear and automorphism symbols. They do not present the prescribed higher-order-zero universal envelope. The standard generalized Schwarz lemma and the elementary numerical range of a unilateral shift are used as known ingredients; neither is claimed as novel. Full-text inspection of the first three sources, rather than abstracts alone, supported these distinctions; obscure earlier equivalent geometry remains a residual literature risk.

## Limitations

Only the Euclidean closed convex hull of the Szegő-kernel quotient is determined, not the exact possibly nonconvex pointwise range for every \(f\in\mathcal S_m\). Sharp support at boundary-circle points may occur only as a limit toward \(|z|=1\); it need not be attained inside the disk. The theorem makes no assertion for \(m=1\), disk maps not fixing the origin to higher order, weighted kernels, or alternate Hardy norms. The asymptotics are for integer \(m\to\infty\). The finding has undergone an internal proof review only; no independent mathematical audit has been performed.

## References

1. P. S. Bourdon, T. Le, D. Thompson, *Berezin Ranges of Composition Operators on* \(H^2\), arXiv:2610.17634, first public version October 13, 2026, https://arxiv.org/abs/2610.17634. In particular Proposition 2.1 and Sections 3–4.
2. C. C. Cowen, C. Felder, *Convexity of the Berezin Range*, arXiv:2109.12095, first public version September 24, 2021, https://arxiv.org/abs/2109.12095.
3. A. Augustine, M. Garayev, P. Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547, first public version February 24, 2023, https://arxiv.org/abs/2302.12547.
4. V. Matache, *Numerical Ranges of Composition Operators*, Linear Algebra Appl. 331 (2001), 61–74; numerical-range background only.
