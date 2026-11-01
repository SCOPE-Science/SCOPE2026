# The unique exceptional circle for cubic exponential phases and its deltoid criterion

## Finding
Let \(a,c\in\mathbb C\setminus\{0\}\), \(b\in\mathbb C\), and
\[f(z)=\exp(az+bz^2+cz^3).\]
For \(r>0\), let \(\nu_f(r)\) be the number of distinct points on \(|z|=r\) where \(|f|\) attains its maximum on that circle. Choose any \(\vartheta\in\mathbb R\) such that \(c e^{3i\vartheta}=|c|\) and define
\[A=ae^{i\vartheta},\quad B=be^{2i\vartheta},\quad C=|c|,\quad d=\frac{B^2}{4C}-A.\]
Then \(\nu_f(r)\le3\) for every \(r>0\), and **there can be at most one radius with \(\nu_f(r)>2\)**. Such a radius exists if and only if all three conditions hold:

1. \(B\ne0\);
2. \(dB\) is a strictly positive real number;
3. with \(r_*=d/\overline B>0\) and \(s=-B/(2Cr_*)\),
\[\Delta(s)=|s|^4+18|s|^2-8\operatorname{Re}(s^3)-27<0.\]

When these conditions hold, \(r_*\) is the sole exceptional radius, \(\nu_f(r_*)=3\), and its maximum points are precisely \(r_*e^{i\vartheta}w\), where \(w\) ranges over the three distinct unit-circle zeros of
\[Q_s(w)=w^3-sw^2+\overline s w-1.\]
At that radius the complete angular defect is
\[\log|f(r_*e^{i\vartheta}w)|=Cr_*^3(1+|s|^2)-\frac{Cr_*^3}{2}|Q_s(w)|^2\qquad(|w|=1).\]
The condition \(\Delta(s)<0\) says exactly that \(s\) lies in the interior of the standard three-cusped deltoid.

If only the first two conditions hold, the same factorization is valid: at \(r_*\) the number of maxima is \(1\) for \(\Delta(s)>0\), \(2\) for \(\Delta(s)=0\) except at the three cusp values \(s=3e^{2\pi ij/3}\) (where it is \(1\)), and \(3\) for \(\Delta(s)<0\). Regardless of these nonexceptional boundary cases, no other radius can have more than two maxima.

For example, \(f(z)=\exp(8z-4z^2+z^3)\) has exactly three maximum-modulus points on \(|z|=1\), at \(z=1,e^{i\pi/3},e^{-i\pi/3}\), and has at most two at every other radius. Among exponential phases with a nonzero linear coefficient, cubic degree is the **least degree** allowing more than two maximum-modulus points on one circle.

## Assumptions and scope
The exponential phase is a polynomial of degree exactly three with nonzero linear coefficient; its coefficients may be complex. The radius is strictly positive, angular maxima are distinct points (not counted with multiplicity), and an arbitrary constant term in the phase merely rescales \(|f|\) and may be omitted. The choice of \(\vartheta\) is immaterial: replacing it by \(\vartheta+2\pi/3\) rotates \(s\) by a cube root of unity while preserving \(dB\), \(r_*\), and \(\Delta(s)\). No conclusion is asserted for arbitrary entire functions or phases of degree at least four.

## Proof
**1. Maxima give double Laurent roots.** Rotate the variable by \(e^{i\vartheta}\); it suffices to work with \(F(w)=\exp(Aw+Bw^2+Cw^3)\), \(C>0\). Put \(h_r(w)=\operatorname{Re}(Arw+Br^2w^2+Cr^3w^3)\) on \(|w|=1\), and \(M_r=\max h_r\). The nonnegative real trigonometric polynomial \(T_r=M_r-h_r\) has degree exactly three. Multiplication by \(w^3\) makes \(T_r\) a degree-six polynomial whose leading and constant coefficients are both \(-Cr^3/2\). Every angular zero is a real local minimum of the analytic function \(T_r(e^{it})\), so has even order at least two. Consequently there are at most three distinct zero points. If there are three distinct points \(w_1,w_2,w_3\), each has multiplicity exactly two and
\[w^3T_r(w)=-\frac{Cr^3}{2}\prod_{j=1}^3(w-w_j)^2.\]
Write \(p=w_1w_2w_3\). The constant coefficient gives \(p^2=1\). For \(|w|=1\), if \(Q(w)=\prod(w-w_j)\), then the unit-root identity
\[|Q(w)|^2=-\overline p\,w^{-3}Q(w)^2\]
shows \(T_r=(Cr^3p/2)|Q|^2\). Nonnegativity and nontriviality force \(p=1\). Thus \(Q(w)=w^3-sw^2+\overline s w-1\) with \(s=w_1+w_2+w_3\). (The coefficient of \(w\) equals \(\overline s\) because each root has modulus one and their product is one.)

**2. Coefficient comparison pins down the radius.** Expanding the preceding identity and matching the positive Fourier harmonics yields
\[B=-2Cr s,\qquad A=Cr^2(s^2+2\overline s).\]
In particular \(B\ne0\), since otherwise \(s=0\) and \(A=0\), contrary to the hypothesis. Eliminating \(s\) gives
\[\frac{B^2}{4C}-A=r\overline B,\qquad dB=r|B|^2>0.\]
Thus every possible three-point circle has the unique radius \(r_*=d/\overline B\), with \(s=-B/(2Cr_*)\). This already proves uniqueness, including when no such positive radius exists.

**3. Converse by a spectral-square identity.** Suppose \(B\ne0\) and \(dB>0\) real, and define \(r_*\), \(s\) as above. Rearranging the relation defining \(d\) gives exactly \(B=-2Cr_*s\) and \(A=Cr_*^2(s^2+2\overline s)\). Direct expansion of \(Q_s(w)\overline{Q_s(w)}\) on \(|w|=1\) proves the identity
\[h_{r_*}(w)=Cr_*^3(1+|s|^2)-\frac{Cr_*^3}{2}|Q_s(w)|^2.\]
The cubic is self-inversive: \(Q_s(w)=-w^3\overline{Q_s(1/\overline w)}\). Hence its roots are invariant, with multiplicities, under \(w\mapsto1/\overline w\). Since its degree is odd and its constant term is nonzero, at least one zero lies on the unit circle. Therefore the displayed constant really is the global maximum, and the distinct maximum points are precisely the distinct unimodular zeros of \(Q_s\).

**4. Deltoid discriminant and distinctness.** Ordinary cubic discriminant expansion gives
\[\operatorname{disc}(Q_s)=\Delta(s)=|s|^4+18|s|^2-8\operatorname{Re}(s^3)-27\in\mathbb R.\]
If its roots are three distinct unit numbers with product one, their pairwise-difference product \(\prod_{i<j}(w_i-w_j)^2\) is strictly negative, since writing \(w_j=e^{it_j}\) gives \(-64\prod_{i<j}\sin^2((t_i-t_j)/2)\). Otherwise, with no multiple root, there is exactly one unit root and a nonunit reciprocal-conjugate pair. Writing that pair as \(\rho e^{i\phi},\rho^{-1}e^{i\phi}\), \(\rho>1\), and the unit root as \(e^{-2i\phi}\) shows the same discriminant is strictly positive: it is a square of nonzero real factors \((\rho-\rho^{-1})^2(2\cos(3\phi)-\rho-\rho^{-1})^2\). At discriminant zero all roots are unimodular, but not distinct; the triple-root cases are exactly \(s=3e^{2\pi ij/3}\). This establishes all stated cases, including the strict criterion for three maxima.

**5. Sharp minimum degree.** For a polynomial exponential phase of degree at most two with a nonzero linear coefficient, \(M_r-h_r\) is a nonzero nonnegative trigonometric polynomial of degree at most two and can have at most two distinct angular zeros by the same multiplicity argument. For \(F(z)=\exp(8z-4z^2+z^3)\), the formulas give \(r_*=1\), \(s=2\), \(\Delta(2)=-3\) and \(Q_2(w)=(w-1)(w^2-w+1)\). These are exactly the three claimed maximum points, and uniqueness gives at most two maxima for every \(r\ne1\).

## Verification
A standalone exact symbolic checker is provided as `check.py` with the version-independent dependency declaration in `requirements.txt`. It reconstructs the Laurent-square identity and cubic discriminant over symbolic real parameters, and checks both the explicit three-point example and an independent rational-coefficient example. The checker reports `CHECK_OK`. The proof of the infinite set of radii and the sign-discriminant root classification is mathematical, not a finite computation; no numerical radius scan is treated as proof.

## Relationship to prior work
Yunpeng Li, *Maximum-modulus points on concentric circles* (arXiv:2610.15067, first publicly submitted 2026-10-10, v2 2026-10-14), Theorem 1, proves local finiteness of radii having more than twice the first Taylor gap, and Example 10 constructs exceptional circles with higher-degree exponential phases. That general theorem does not imply an at-most-one exceptional radius, an explicit complex-coefficient criterion, or the least possible polynomial-phase degree. This finding settles these questions for the entire cubic phase family.

Michael Q. Rieck, *The Deltoid Curve and Triangle Transformations* (arXiv:2307.09219, 2023), Section 4 and Lemma 4.1, gives the standard deltoid/unit-circle cubic-root equivalence. That cubic-root criterion is treated here as classical mathematical structure, not a new discovery. The new relationship is the exact factorization forced by three maximum-modulus points and its coefficient-to-radius implication. General degree-three nonnegative trigonometric-polynomial factorization likewise is not claimed as new.

## Limitations
The contribution is a complete exact classification of the **exceptional** radius for cubic exponential phases, not a classification of all ordinary one- versus two-point maximum radii. The proof does not address degree-four or higher phases. Discriminant zero contains multiple roots and does not yield three distinct maximizers; this boundary is explicitly excluded from the strict exceptional criterion. Independently establishing literature priority remains necessary.

## References
1. Y. Li, *Maximum-modulus points on concentric circles*, arXiv:2610.15067v2 (2026), Sections 1 and 10. https://arxiv.org/html/2610.15067v2
2. M. Q. Rieck, *The Deltoid Curve and Triangle Transformations*, arXiv:2307.09219v1 (2023), Section 4, Lemma 4.1. https://arxiv.org/pdf/2307.09219
3. MSC2020, classification 30D20, *Entire functions of one complex variable (general theory)*. https://mathscinet.ams.org/msc/msc2020.html?t=30D99
