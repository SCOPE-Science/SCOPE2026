# Non-polydisc equality cases for complex fractional illumination in every dimension

## Finding

For every integer \(n\ge 2\), let \(D=\{z\in\mathbb C:|z|\le1\}\) and set
\[
 B=\{(z_1,z_2)\in\mathbb C^2:|z_1|+|z_2|\le1\},\qquad
 K_n=B\times D^{n-2}\subset\mathbb C^n.
\]
Then
\[
 \boxed{\operatorname{ill}^{*}(K_n)=2^n},
\]
although \(K_n\) is **not** a complex-linear image of the polydisc \(D^n\). In particular, the statement in Conjecture 1.2 of Rotem, Schejter and Slomka that equality in \(\operatorname{ill}^{*}(K)\le2^n\) characterizes complex-linear images of \(D^n\) is false for every \(n\ge2\). The asserted universal upper bound itself is **not** contradicted.

## Assumptions and scope

A complex convex body is a full-dimensional unit ball of a norm on \(\mathbb C^n\), viewed as a real convex body in \(\mathbb R^{2n}\). A nonzero vector \(v\in\mathbb C^n\) *illuminates* \(x\in K\) if \(x+tv\in\operatorname{int}K\) for some real \(t>0\). A nonnegative finite Borel measure \(\mu\) on the vector space is a fractional illumination measure when
\[
 \mu(\{v:v\text{ illuminates }x\})\ge1\quad\text{for every }x\in K.
\]
Its mass has infimum \(\operatorname{ill}^{*}(K)\). These are exactly the definitions in the cited primary paper; no complex-direction restriction or change of normalization is introduced. Empty products have value one for \(n=2\).

## Proof

**1. A sharp covering measure on the two-coordinate block.** Let \(\sigma_j\) be normalized Haar probability measure on the circle of vectors \(e^{i\theta}e_j\), where \(e_j\) is the \(j\)-th complex coordinate basis vector. Set \(\nu_B=2\sigma_1+2\sigma_2\), a measure of mass four on \(\mathbb C^2\).

For \(x=(z_1,z_2)\) on the boundary of \(B\), the strict inward derivative of the active constraint \(|z_1|+|z_2|\) along \(e^{i\theta}e_j\) is \(\operatorname{Re}(e^{-i\arg z_j}e^{i\theta})<0\) whenever \(z_j\ne0\). Precisely one half of the \(j\)-th circle satisfies this condition. If \(z_j=0\), the corresponding derivative is \(+1\), so that circle contributes zero; since \(x\in\partial B\), at least one \(z_j\ne0\). Consequently \(\nu_B\) assigns illuminating directions mass at least one at every boundary point. At interior points, every direction in its support illuminates for sufficiently small positive \(t\), giving mass four. Thus \(\nu_B\) fractionally illuminates \(B\) with total mass four.

For each remaining disk coordinate \(j\in\{3,\ldots,n\}\), the measure \(\nu_j=2\sigma_j\) has mass two and illuminates every point of the disk with mass at least one: at \(|z_j|=1\), exactly one half of its phase circle is inward, and at \(|z_j|<1\), the whole circle is available.

Form the product \(\nu_B\otimes\nu_3\otimes\cdots\otimes\nu_n\), and push it forward by addition of its components in their disjoint coordinate subspaces. Its total mass is \(4\cdot2^{n-2}=2^n\). For any \(x\in K_n\), the sets of directions illuminating its respective factors have weights at least one. Their Cartesian product therefore has product weight at least one, and every resulting sum direction illuminates \(x\) because the finitely many factorwise strict inward inequalities hold simultaneously for a sufficiently small common \(t>0\). Hence
\[
 \operatorname{ill}^{*}(K_n)\le2^n.
\]

**2. An exact lower-bound measure on extremal boundary points.** Select an index \(J\in\{1,2\}\) uniformly; select independent uniform phases \(\theta,\phi_3,\ldots,\phi_n\) on \([0,2\pi)\); and define \(X\in\partial K_n\) by setting \(X_J=e^{i\theta}\), \(X_{3-J}=0\), and \(X_j=e^{i\phi_j}\) for \(j\ge3\). Let \(\lambda\) be the resulting probability distribution.

Fix an arbitrary direction \(v=(v_1,\ldots,v_n)\). At a point selected with index \(J\), the right derivative of the first active gauge constraint along \(v\) is
\[
 \operatorname{Re}(e^{-i\theta}v_J)+|v_{3-J}|.
\]
Its negativity is **necessary** for illumination, since the constraint is convex as a function of the real step \(t\), starts at value one, and cannot drop below one if its right derivative is nonnegative. Negativity is also sufficient for that block. If \(|v_J|\le|v_{3-J}|\), no phase \(\theta\) works; otherwise the permitted phases form an arc of relative length
\[
 \frac1\pi\arccos\!\left(\frac{|v_{3-J}|}{|v_J|}\right)\le\frac12.
\]
Only one index \(J\in\{1,2\}\) can satisfy the strict inequality \(|v_J|>|v_{3-J}|\). Since \(J\) is uniform, the probability of illuminating the first factor is at most \(1/4\).

For each \(j\ge3\), the active disk inequality at \(X_j\) requires \(\operatorname{Re}(e^{-i\phi_j}v_j)<0\), an event of probability \(1/2\) when \(v_j\ne0\) and zero otherwise. By independence,
\[
 \Pr_{X\sim\lambda}\{v\text{ illuminates }X\}\le\frac14\left(\frac12\right)^{n-2}=2^{-n}.
\]
Let \(\mu\) be any fractional illumination measure of finite mass. Tonelli's theorem, applied to the Borel illumination relation, gives
\[
 1\le\int\mu(\{v:v\text{ illuminates }x\})\,d\lambda(x)
 =\int\Pr_{X\sim\lambda}\{v\text{ illuminates }X\}\,d\mu(v)
 \le2^{-n}\mu(\mathbb C^n).
\]
Thus \(\operatorname{ill}^{*}(K_n)\ge2^n\), establishing the exact value.

**3. No complex-linear equivalence to a polydisc.** Suppose an invertible complex-linear map \(T\) satisfied \(K_n=T(D^n)\). The gauge of \(K_n\) would be
\[
 \lVert z\rVert_{K_n}=\max_{1\le k\le n}|(T^{-1}z)_k|.
\]
Restrict to \(z=(z_1,z_2,0,\ldots,0)\). There would be complex numbers \(a_k,b_k\) such that, for all \(z_1,z_2\in\mathbb C\),
\[
 |z_1|+|z_2|=\max_{1\le k\le n}|a_kz_1+b_kz_2|.
\]
Taking \((z_1,z_2)=(1,0)\) and \((0,1)\) yields \(|a_k|,|b_k|\le1\) for every \(k\). Now put \((z_1,z_2)=(1,e^{i\theta})\). For *every* phase \(\theta\), the maximum must be two. The triangle inequality implies that a fixed index \(k\) can realize this value only when \(|a_k|=|b_k|=1\) and \(a_k\) is phase-aligned with \(b_ke^{i\theta}\). Each \(k\) permits at most one phase modulo \(2\pi\). Finitely many such indices cannot cover all phases. This contradiction proves non-equivalence and completes the theorem.

## Verification

The covering normalization can be checked at all boundary strata: the two-coordinate block contributes weight at least one whether exactly one or both coordinates are nonzero; each disk contributes weight one on its boundary. The product has total mass \(4\cdot2^{n-2}=2^n\). The lower bound uses the exact phase-arc probability rather than finite-angle sampling and supplies the matching dual witness \(2^{-n}\). In dimension two this gives the explicit matching upper and lower value four; in dimension three it gives eight. The non-equivalence argument is a continuum-of-phases obstruction to representing a sum of two complex moduli by a maximum of finitely many complex moduli. No numerical experiments, unverified integral estimates, or computer certificates are needed for the proof.

## Relationship to prior work

Rotem, Schejter and Slomka, *The Complex Illumination Problem*, arXiv:2410.12021v1, Conjecture 1.2, propose the universal upper bound and polydisc-only equality condition; their Theorem 1.3 gives \(\operatorname{ill}^{*}(D^n)=2^n\). Their Theorems 1.9 and 1.10 prove strictness for non-polydisc complex zonotopes and zonoids. The present body is a product with a two-coordinate complex \(\ell_1\)-ball rather than a polydisc, and the present lower-bound witness covers exactly the extremal boundary strata missing from the polydisc calculation. The unrestricted equality statement does not follow from the earlier zonoid results; the present theorem gives explicit non-polydisc equality cases. The original preprint and the later open-access published version were inspected in the sections containing the conjectures, illumination definitions, polydisc computation, and zonotope/zonoid theorems.

## Limitations

This theorem leaves open whether \(\operatorname{ill}^{*}(K)\le2^n\) for *every* complex convex body and does not address the classical (integer-valued) illumination conjecture. It does not characterize all fractional-equality cases, determine the classical illumination numbers of \(K_n\), or imply any universality beyond the specified product family. A published but unindexed equivalent calculation cannot be excluded merely by bibliographic searches.

## References

1. L. Rotem, A. Schejter and B. A. Slomka, *The Complex Illumination Problem*, arXiv:2410.12021v1, first posted 15 October 2024. https://arxiv.org/html/2410.12021v1
2. L. Rotem, A. Schejter and B. A. Slomka, *The complex Illumination problem*, **Combinatorica** 46, article 3 (2026), doi:10.1007/s00493-025-00195-7. https://link.springer.com/article/10.1007/s00493-025-00195-7
