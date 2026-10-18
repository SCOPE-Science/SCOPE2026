# Exact \(q\)-numerical annuli of two-dimensional antilinear quaternionic roots

## Finding

Let \(H\) be a two-dimensional complex Hilbert space, with inner product linear in the first argument. Let \(A:H\to H\) be **antilinear**, and assume
\[
A^2=-\rho^2I\qquad (\rho>0).
\]
Write \(a=\|A\|\) and \(b=\rho^2/a\); equivalently, \(a\ge b>0\) are the two singular values of \(A\). For \(q\in\mathbb C\), \(|q|\le1\), define the constrained numerical range
\[
W_q(A)=\bigl\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\bigr\},
\qquad k=\sqrt{1-|q|^2}.
\]
Then the complete set, including both boundary circles, is
\[
\boxed{W_q(A)=\{z\in\mathbb C:r_-(a,b,q)\le |z|\le r_+(a,b,q)\}},
\]
with **exact** radii
\[
\boxed{r_- =\frac12\bigl[k(a+b)-(a-b)\bigr]_+,\qquad
r_+=\frac12\bigl[k(a+b)+(a-b)\bigr]},
\qquad [t]_+=\max\{t,0\}.
\]
In particular,
\[
\boxed{0\in W_q(A)\ \Longleftrightarrow\ |q|\ge \frac{2\sqrt{ab}}{a+b}=\frac{2\rho}{a+b}.}
\]
Thus a nonzero central hole survives precisely below this *sharp anisotropy-dependent threshold*. Every allowed pair \(a\ge b>0\) is realized. At \(q=0\), the range is the closed annulus \(b\le|z|\le a\); at \(|q|=1\), it is the closed disk of radius \((a-b)/2\). For \(a=b\), it is the circle of radius \(a\sqrt{1-|q|^2}\) (a singleton at \(|q|=1\)).

A concrete nonconformal example is \(A(z_1,z_2)=(-\overline{z_2},4\overline{z_1})\), for which \(A^2=-4I\). At \(q=3/5\),
\[
\boxed{W_{3/5}(A)=\{z:1/2\le |z|\le7/2\}},
\]
and the hole closes exactly at \(|q|=4/5\).

## Assumptions and scope

The space is complex and exactly two-dimensional; the operator is bounded and antilinear, with its square a strictly negative **real scalar** multiple of the identity. No normality or isometry hypothesis is imposed. The scalar constraint \(q\) can have arbitrary complex phase. The inequalities for \(|z|\) include the boundaries. No assertion is made for real-linear maps with a nonzero complex-linear part, for other antilinear square relations, or for dimensions other than two.

## Proof

**1. Intrinsic canonical form.** Let \(a=\|A\|\). The identity \(A^2=-\rho^2 I\) implies for every unit \(v\) that
\[
\rho^2=\|A^2v\|\le a\|Av\|,
\]
so the minimum singular value is at least \(b=\rho^2/a\). Choose a unit vector \(e_1\) attaining the operator norm, and put \(e_2=Ae_1/a\). Then \(\|e_2\|=1\), \(Ae_1=a e_2\), and \(Ae_2=-b e_1\). In particular \(\|Ae_2\|=b\), so \(b\) is exactly the minimum singular value.

If \(a>b\), then \(e_1\) and \(e_2\) are eigenvectors of the positive complex-linear operator \(A^*A\) corresponding to its distinct maximum and minimum eigenvalues and are orthogonal. If \(a=b\), then \(A/a\) is antiunitary with square \(-I\). For an antiunitary \(U\) obeying \(U^2=-I\),
\[
\langle Ux,U(Ux)\rangle=\overline{\langle x,Ux\rangle}
\quad\Longrightarrow\quad
-\langle Ux,x\rangle=\langle Ux,x\rangle;
\]
hence \(e_1\perp e_2\) in this case also. Thus, in the orthonormal basis \((e_1,e_2)\),
\[
A(z_1,z_2)=(-b\overline{z_2},a\overline{z_1}).
\]
This proves both unitary reduction and realization of every \(a\ge b>0\) by the displayed model (with \(\rho^2=ab\)).

**2. Constrained pairs.** Write \(t=|q|\) and \(k=\sqrt{1-t^2}\). For a unit vector \(x=(x_1,x_2)\), choose the orthogonal unit vector \(v=(-\overline{x_2},\overline{x_1})\). All unit vectors \(y\) satisfying \(\langle x,y\rangle=q\) are exactly
\[
y=\overline q\,x+k e^{i\phi}v,
\qquad 0\le\phi<2\pi,
\]
with the circle redundant when \(k=0\). If \(u=|x_1|^2\in[0,1]\), then
\[
|\langle Ax,x\rangle|=(a-b)\sqrt{u(1-u)},\qquad
|\langle Ax,v\rangle|=b+(a-b)u.
\]
Consequently, varying \(\phi\) gives the interval of attainable moduli
\[
\bigl|t(a-b)\sqrt{u(1-u)}-k[b+(a-b)u]\bigr|
\ \le |\langle Ax,y\rangle|\le
 t(a-b)\sqrt{u(1-u)}+k[b+(a-b)u].
\]
The formulas hold for nonreal \(q\), because the phase of \(\phi\) compensates its argument.

**3. Exact extrema.** Set \(S=a+b\), \(c=a-b\ge0\), and \(z=2u-1\in[-1,1]\). The largest possible modulus equals
\[
\max_{-1\le z\le1}\frac12\bigl[kS+c(kz+t\sqrt{1-z^2})\bigr]
=\frac{kS+c}{2},
\]
since \(\max_{-1\le z\le1}(kz+t\sqrt{1-z^2})=\sqrt{k^2+t^2}=1\); the maximum occurs at \(z=k\).

The smallest possible modulus equals
\[
\min_{-1\le z\le1}\frac12\bigl|kS+c(kz-t\sqrt{1-z^2})\bigr|.
\]
The function \(kz-t\sqrt{1-z^2}\) has minimum \(-1\), at \(z=-k\). If \(kS\ge c\), its displayed absolute-value argument is everywhere nonnegative, with minimum \(kS-c\). If \(kS<c\), it is negative at \(z=-k\) and nonnegative at \(z=1\), so continuity gives a zero. Both cases include equality, and hence the minimum modulus is \([kS-c]_+/2\).

**4. No missing intermediate radii.** The set of admissible constrained pairs is connected: for \(t<1\), it is parametrized continuously by the connected unit sphere in \(\mathbb C^2\) and a circle of phases; for \(t=1\), by that unit sphere alone. Its continuous image under \((x,y)\mapsto\langle Ax,y\rangle\) is connected. Multiplying both \(x\) and \(y\) by \(e^{i\theta}\) preserves the constraint and multiplies the image by \(e^{-2i\theta}\), so the image is rotationally invariant. A nonempty compact, connected, rotationally invariant subset of the plane contains every circle between its minimum and maximum moduli. The preceding two extrema therefore describe **all** of \(W_q(A)\).

**5. Critical threshold.** The lower radius vanishes exactly when \(k(a+b)\le a-b\), or after squaring,
\[
|q|^2\ge 1-\frac{(a-b)^2}{(a+b)^2}=\frac{4ab}{(a+b)^2}.
\]
This is the stated threshold. The endpoint formulas and example follow by direct substitution. \(\square\)

## Verification

The standalone standard-library checker `check.py` independently evaluates the canonical antilinear square, constrained pair normalization, randomized complex-phase pairs, and constructive inner/outer extremizers. Running `python3 check.py` from the extracted package produces a finite-assertion PASS message. Its finite diagnostics do not prove the continuum classification; the proof above establishes all dimensions, parameters, and endpoints within the stated domain.

## Relationship to prior work

Kołaczek and Müller, *Real linear operators and numerical ranges* (arXiv:2508.04347, first public 6 August 2025), study the geometry of numerical ranges of real-linear and antilinear operators, but do not calculate the constrained \(q\)-numerical ranges. Their earlier *Numerical Ranges of Antilinear Operators* (2024) proves that ordinary numerical ranges are disks in dimension at least two; that covers the qualitative \(|q|=1\) conclusion, not the new sharp nonconformal \(q\)-profile. Jia and Liu (2025) give an ordinary-numerical-range classification, not a demonstrated extension of the displayed constrained-radii formula.

Majumdar and Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces* (arXiv:2610.16823v1, 12 October 2026), subsequently establish in their Section 6 that the constrained range is an annulus in dimension two and exhibit the special isometric skew example; their inspected section does not state the singular-value radii, unitary reduction for \(A^2=-\rho^2I\), or the exact anisotropy-dependent zero-inclusion threshold. The isometric-skew circle, and the ordinary \(q=1\) disk, are explicitly acknowledged as already covered. The asserted contribution is the complete **non-isometric** quaternionic-square class, including sharp radii and the collapse threshold.

## Limitations

The result neither extends to arbitrary antilinear matrices nor establishes higher-dimensional \(q\)-ranges. Publication priority beyond the inspected sources is not independently certified; earlier two-by-two real-linear reduction formulas could imply this class under different notation. In particular, the complete Jia–Liu article was not accessible in this investigation, and its publication record alone does not establish a negative whole-document comparison. All conclusions are exact mathematics, but independent validation has not been performed.

## References

1. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347v1, first public 2025-08-06, https://arxiv.org/html/2508.04347v1.
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96 (2024), article 17, https://doi.org/10.1007/s00020-024-02768-5.
3. B. Jia and T. Liu, *A characterization of numerical ranges for antilinear operators*, Canadian Mathematical Bulletin, first online 2025-04-14, https://doi.org/10.4153/S000843952500044X.
4. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1, 2026-10-12, https://arxiv.org/html/2610.16823v1.
