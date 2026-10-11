# Sharp norming-face error bounds and adjusted Bhatia–Šemrl membership in real \(L_1\)

## Finding

Let \((\Omega,\Sigma,\mu)\) be an arbitrary probability space, and let \(g\in L_\infty(\mu;\mathbb R)\) satisfy \(\|g\|_\infty=1\). Set \(A=\{|g|=1\}\) and \(B=\Omega\setminus A\), modulo null sets. The functional \(u\mapsto\int gu\,d\mu\) has the **adjusted Bhatia–Šemrl property** precisely when \(\mu(A)>0\) and either \(\mu(B)=0\) or
\[
 r=\operatorname*{ess\,sup}_{B}|g|<1.
\]
When \(\mu(A)>0\), the positive norming face is
\[
 F_g=\left\{v\in L_1(\mu;\mathbb R):\|v\|_1=1,\ \int gv\,d\mu=1\right\}.
\]
For every \(u\in S_{L_1}\), its exact distance to this face is
\[
 \operatorname{dist}_1(u,F_g)=2\left(1-\int_A(\operatorname{sgn}(g)u)_+\,d\mu\right).
\]
The *optimal global linear norming-face error constant*, with extended real values, is
\[
 K(g)=\sup_{\substack{u\in S_{L_1}\\\int gu<1}}
 \frac{\operatorname{dist}_1(u,F_g)}{1-\int gu\,d\mu}
 =\begin{cases}
 1,&\mu(B)=0,\\
 \displaystyle\frac{2}{1-r},&\mu(B)>0,\ r<1,\\
 +\infty,&\mu(B)>0,\ r=1.
 \end{cases}
\]
Consequently, among norm-attaining nonzero functionals, the adjusted Bhatia–Šemrl property is **equivalent** to a finite optimal global face-error constant.

## Assumptions and scope

All spaces and scalars are real. Measure spaces are arbitrary probability spaces, with no non-atomicity or separability assumption. As usual, the signed function \(\operatorname{sgn}(g)\) is defined almost everywhere, and \(t_+=\max\{t,0\}\). The essential supremum over \(B\) is only used when \(\mu(B)>0\). Equalities involving measurable sets are understood modulo null sets. The adjusted property is the 2022 definition: \(g\) attains its norm and, for every \(h\in L_\infty\) satisfying \(\|g+th\|_\infty>\|g\|_\infty\) for every nonzero real \(t\), some \(v\in S_{L_1}\) attains the norm of \(g\) and has \(h(v)=0\). There is no asserted complex analogue or operator-valued extension.

If \(\mu(A)=0\), the functional does not attain its norm: the associated face is empty and the error constant above is not defined. For nonzero functionals with other norms, first divide by their norm.

## Proof

**1. The norming face.** Equality in \(\int gv\le\int|v|=1\) holds exactly when \(v=0\) almost everywhere on \(B\) and \(\operatorname{sgn}(g)v\ge0\) almost everywhere on \(A\). The face is therefore nonempty exactly when \(\mu(A)>0\). Write
\[
 m=\int_A(\operatorname{sgn}(g)u)_+\,d\mu,\qquad 0\le m\le1.
\]
The nonnegative aligned portion of \(u\), multiplied by \(\operatorname{sgn}(g)\), has \(L_1\)-mass \(m\) and is disjoint pointwise from the rest of \(u\). Every \(v\in F_g\) has mass one in the aligned cone, so \(\|u-v\|_1\ge (1-m)+(1-m)\). When \(m>0\), normalizing the aligned portion to mass one attains equality; when \(m=0\), every \(v\in F_g\) is at distance two. This proves the distance formula and the attainment of that distance.

**2. The sharp error constant.** Put
\[
 b_A=\int_A(\operatorname{sgn}(g)u)_-\,d\mu,
 \qquad b_B=\int_B|u|\,d\mu.
\]
Then the distance is exactly \(2(b_A+b_B)\). Its norm-attainment defect satisfies
\[
 1-\int gu\,d\mu
 =2b_A+\int_B(|u|-gu)\,d\mu
 \ge 2b_A+(1-r)b_B.
\]
When \(\mu(B)=0\), defect equals distance and \(K(g)=1\), witnessed by \(u\in-F_g\). When \(\mu(B)>0\) and \(r<1\), this inequality gives \(K(g)\le 2/(1-r)\). For every sufficiently small \(\delta>0\), by definition of essential supremum there is a measurable positive-measure set \(E\subseteq B\) on which \(|g|>r-\delta\). Choose \(u\in S_{L_1}\) supported on \(E\) and aligned in sign with \(g\) wherever \(g\ne0\). Its distance to \(F_g\) is two and its defect is at most \(1-r+\delta\). Therefore \(K(g)=2/(1-r)\). The same witnesses make \(K(g)=+\infty\) when \(r=1\). If \(r=0\), any unit density supported on \(B\) gives the claimed equality directly.

**3. The adjusted property in the gap case.** Suppose \(\mu(A)>0\) and either \(\mu(B)=0\) or \(r<1\). For \(h\in L_\infty\), define \(q=\operatorname{sgn}(g)h\) on \(A\). We claim
\[
 g\perp_S h\quad\Longleftrightarrow\quad
 \mu(A\cap\{q>0\})>0\ \text{and}\ \mu(A\cap\{q<0\})>0.
\]
The reverse implication follows because, for positive \(t\), the first set gives an essential norm strictly above one; for negative \(t\), the second does. For the forward implication, if \(q\ge0\) almost everywhere on \(A\), then for every sufficiently small negative \(t\) we have \(|1+tq|\le1\) on \(A\) and \(\|g+th\|_{L_\infty(B)}\le r+|t|\|h\|_\infty\le1\) when \(B\) is nonnull. This contradicts strong orthogonality. The case \(q\le0\) is symmetric.

Consequently there are positive-mass sets on \(A\) where \(q\) has either sign. Choose two nonnegative unit \(L_1\) densities supported there, multiply by \(\operatorname{sgn}(g)\), and take a convex combination whose \(h\)-integral vanishes. The resulting unit vector is in \(F_g\) and satisfies \(h(v)=0\). This proves the adjusted property.

**4. Necessity of the gap.** If \(\mu(A)=0\), norm attainment fails. Otherwise suppose \(\mu(B)>0\) and \(\operatorname*{ess\,sup}_{B}|g|=1\). Define the bounded function \(h\) by \(h=\operatorname{sgn}(g)\) on \(A\), \(h=-\operatorname{sgn}(g)\) on \(B\cap\{g\ne0\}\), and \(h=0\) elsewhere. For every \(t>0\), \(\|g+th\|_\infty\ge1+t\) using \(A\); for every \(t<0\), \(\|g+th\|_\infty\ge1+|t|\) using the essential supremum on \(B\). Hence \(g\perp_S h\). But for every \(v\in S_{L_1}\) norming \(g\) with either sign, support lies in \(A\) and \(h(v)=g(v)=\pm1\). Thus there is no norming vector orthogonal to \(h\), and the adjusted property fails.

Steps 1–4 prove both the classification and its equivalence to finite \(K(g)\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic on finite atomic models. It checks the face-distance formula against a direct discrete minimization, the sharp upper bound for the error constant, and sharp single-coordinate witnesses. Running `python verify.py` produced:

`VERIFY_OK finite_functionals=242 exact_face_distances=14772 sharp_ratio_witnesses=230 infinite_case_requires_proof=True`

These tests are not a proof for arbitrary measure spaces; the preceding analytic argument supplies the infinite-dimensional and non-atomic cases. The path is relative to this package.

## Relationship to prior work

Choi, Jung and Kim (arXiv:2208.11987v1, 25 August 2022) introduce adjusted Bhatia–Šemrl orthogonality (Definition 1.2). Their Theorem 2.13 proves norm density for scalar functionals on \(L_1[0,1]\) by constructing functions with an isolated maximum-modulus level, a **sufficient condition**. Theorem 2.15 constructs dense norm-attaining operators without the adjusted property, but neither theorem gives the above necessity criterion or the best linear distance-to-face constant for arbitrary probability spaces. The present statement makes the isolation condition an equivalence and gives the exact quantitative norming-face stability profile, including the infinite-constant boundary.

Kim and Lee (2019) treat the original Bhatia–Šemrl property, rather than the subsequently introduced adjusted variant. Martín, Merí, Quero and Roy (2024) study general numerical-range Birkhoff–James orthogonality, including a result for continuous functions with connected norming sets; its hypotheses and property do not imply the scalar \(L_1\) error constant. Jayanarayanan and Rajpopat (2025) connect the original property with essential norm and strong subdifferentiability for different operator spaces. These comparisons do not exclude equivalent formulations under other terminology.

## Limitations

Only real scalar functionals on probability \(L_1\) spaces are covered. The nonzero normalization is essential and the error constant is only defined when \(F_g\ne\varnothing\). No assertion is made about arbitrary Banach-space operators, complex orthogonality, strong exposure of individual points, or optimal perturbation size in the dual norm. A potentially related 2019 paper could be checked only at the abstract and bibliographic level; complete literature novelty remains subject to independent verification.

## References

1. G. Choi, M. Jung, S. K. Kim, *On a set of norm attaining operators and the strong Birkhoff-James orthogonality*, arXiv:2208.11987v1 (public 25 August 2022); later *Results in Mathematics*, doi:10.1007/s00025-023-01852-3. https://arxiv.org/html/2208.11987v1
2. S. K. Kim, H. J. Lee, *The Birkhoff-James orthogonality of operators on infinite dimensional Banach spaces*, *Linear Algebra and its Applications* 582 (2019), 440–451. doi:10.1016/j.laa.2019.08.012.
3. M. Martín, J. Merí, A. Quero, S. Roy, *A numerical range approach to Birkhoff–James orthogonality with applications*, *Banach Journal of Mathematical Analysis* 18 (2024), article 24. doi:10.1007/s43037-024-00333-1. https://link.springer.com/article/10.1007/s43037-024-00333-1
4. C. R. Jayanarayanan, R. R. Rajpopat, *On Bhatia-Šemrl Property, Strong Subdifferentiability and Essential Norm of Operators on Banach Spaces*, arXiv:2512.15208v1 (2025). https://arxiv.org/html/2512.15208v1
