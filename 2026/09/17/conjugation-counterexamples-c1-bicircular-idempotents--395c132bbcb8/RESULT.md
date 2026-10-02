# Non-antipodal counterexamples to the \(C^1\) bicircularity dichotomy

## Finding

On \(X=C^1[0,1]\) with \(\|f\|_\sigma=|f(0)|+\|f'\|_\infty\), the phase pair \((\lambda,\mu)=(1,i)\) gives nonzero complementary real-linear idempotents whose designated phase combination is a surjective Form III isometry, although the family is not bi-circular. A second pair gives the same obstruction in Form IV. Hence the abstract's dichotomy and Theorems 3.3 and 3.4 of arXiv:2609.18967v1 are false as stated.

The asserted contribution is this correction to those specific conclusions and identification of their failed proof step. Scalar conjugation projections and the general reflection recipe used here are older mathematics, not discoveries asserted by this record.

## Assumptions and scope

Write \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). A generalized bi-circular idempotent family consists of distinct nonzero idempotents \(P_1,P_2\) with
\[
P_1+P_2=I,\qquad P_1P_2=P_2P_1=0,
\]
for which \(\lambda P_1+\mu P_2\) is a surjective isometry for some distinct unit phases. A bi-circular family requires every permitted unimodular phase combination to be a surjective isometry. The target's idempotents are not assumed complex-linear; our examples are bounded real-linear maps.

The conclusion addresses v1 as written, not every result or a later revision. The all-phase construction is supporting structure, not a claim of priority for that construction. We assert no replacement classification of all four isometry forms.

## Proof

### Coordinates and older scalar projections

The complex-linear isometric bijection
\[
Jf=(f(0),f'),\qquad J:X\longrightarrow\mathbb C\oplus_1 C[0,1],
\]
has inverse \(J^{-1}(a,g)(t)=a+\int_0^t g(s)\,ds\). For distinct \(\lambda,\mu\in\mathbb T\), define
\[
Cz=\overline z,\qquad
Q_\lambda z=\frac{\overline z-\mu z}{\lambda-\mu},
\qquad Q_\mu=I-Q_\lambda.
\]
Using \(\overline\lambda=1/\lambda\) and \(\overline\mu=1/\mu\) gives
\[
\overline{Q_\lambda z}=\lambda Q_\lambda z,\qquad
\overline{Q_\mu z}=\mu Q_\mu z.
\]
Their ranges are the nonzero real lines \(L_\nu=\{z:\overline z=\nu z\}\). These intersect only at zero. On \(L_\lambda\), \(Q_\lambda\) is the identity; on \(L_\mu\), it is zero. Consequently
\[
Q_\lambda^2=Q_\lambda,\quad Q_\mu^2=Q_\mu,\quad
Q_\lambda Q_\mu=Q_\mu Q_\lambda=0,\quad
\lambda Q_\lambda+\mu Q_\mu=C.
\]
The bounded real-linear maps act pointwise on continuous functions.

This is an older reflection recipe. For
\[
R=\lambda^{-1}C,\qquad \kappa=\mu/\lambda,
\]
one has \(R^2=I\), \(|\kappa|=1\), \(\kappa\ne1\), and
\[
\frac{R-\kappa I}{1-\kappa}=Q_\lambda.
\]
Remark 1 of the 2019 Botelho--Miura corrigendum describes this conjugate-linear mechanism. The scalar substitutions \(\alpha=1/\lambda\), \(\kappa=\mu/\lambda\) also give
\[
\frac{\alpha\overline z-\kappa z}{1-\kappa}=Q_\lambda z,
\]
the overlap with the scalar ingredient of Remark 2's evaluation-supported conjugation example.

### Form III

Set
\[
JP_1J^{-1}(a,g)=(a,Q_\lambda g),\qquad
JP_2J^{-1}(a,g)=(0,Q_\mu g).
\]
The two blocks establish all complementarity and idempotence relations. The maps are bounded, nonzero and distinct. Moreover
\[
J(\lambda P_1+\mu P_2)J^{-1}(a,g)=(\lambda a,\overline g).
\]
This preserves \(|a|+\|g\|_\infty\) and has inverse
\((a,g)\mapsto(\overline\lambda a,\overline g)\). Thus
\[
(Tf)(t)=\lambda f(0)+\int_0^t\overline{f'(s)}\,ds
\]
is the target's surjective Form III isometry with \(c=\lambda\), \(\beta\equiv1\), \(\phi=\mathrm{id}\).

Choose unit generators \(u_\lambda\in L_\lambda\), \(u_\mu\in L_\mu\), and let
\[
\rho=u_\lambda/u_\mu,\qquad f(t)=t(u_\lambda-u_\mu).
\]
Distinct lines imply \(f\ne0\) and \(\rho\ne1\), so \((1,\rho)\) is a permitted distinct phase pair. The constant coordinates vanish and
\[
(P_1f)'=u_\lambda,\qquad (P_2f)'=-u_\mu,\qquad
(P_1+\rho P_2)f=0.
\]
Hence that combination is not injective and is not an isometry. The family is not bi-circular.

Explicitly, for \((\lambda,\mu)=(1,i)\), writing \(z=x+iy\),
\[
Q_1z=x+y,\quad Q_i z=-y+iy,\quad
u_1=1,\quad u_i=\frac{1-i}{\sqrt2},\quad
\rho=\frac{1+i}{\sqrt2}.
\]
The surjective combination \(P_1+iP_2\) and the nonzero killed function
\[
f(t)=t\left(1-\frac{1-i}{\sqrt2}\right)
\]
prove the failure of the abstract's dichotomy and Theorem 3.3, since \(1+i\ne0\).

### Form IV and the invalid inference

Define
\[
J\widetilde P_1J^{-1}(a,g)=(Q_\lambda a,Q_\lambda g),\qquad
J\widetilde P_2J^{-1}(a,g)=(Q_\mu a,Q_\mu g).
\]
These are nonzero complementary idempotents and
\[
J(\lambda\widetilde P_1+\mu\widetilde P_2)J^{-1}(a,g)
=(\overline a,\overline g).
\]
The associated operator is \(\widetilde T f=\overline f\), a surjective Form IV isometry. The same zero-constant test function proves non-bicircularity, refuting Theorem 3.4 as stated.

The Form IV projections are directly the older conjugate-linear reflection construction on the whole function space and are not asserted to be new. The later proofs incorrectly treat idempotence of phase-dependent displayed projections as permission to replace their designated phases by arbitrary new phases without changing those projections. For fixed projections only \(\lambda P_1+\mu P_2=T\) has been established. The cancellation above disproves the unrestricted new-phase assertion. Real-linearity does not permit complex-linear spectral manipulations.

### Auxiliary phase check

Equations (3.4) and (3.6) of the target paper give
\[
\beta(t)\beta(\phi(t))f'(\phi^2(t))
-(\lambda_1+\lambda_2)\beta(t)f'(\phi(t))
+\lambda_1\lambda_2f'(t)=0.
\]
In the stated nontrivial involutive branch \(\phi^2=\mathrm{id}\), \(\lambda_2=-\lambda_1\), constant nonzero derivatives force
\[
\beta(t)\beta(\phi(t))=\lambda_1^2.
\]
The target's relation \(\pm\lambda_1\) has the wrong phase weight. This is a direct algebraic check, not a separate discovery or a complete replacement for Theorems 3.1 and 3.2.

## Verification

The proof covers every distinct unit pair, including a phase equal to \(-1\). The explicit \((1,i)\) witness alone suffices for the asserted refutation.

Run python artifacts/verify.py from the record directory with SymPy installed. It checks exact real-matrix identities, the designated conjugation combination, equality with the older scalar phase substitution, and the explicit \(\sqrt2\) cancellation. Generic Cayley coordinates cover all phases except \(-1\); both single-\(-1\) patches are checked separately. Actual output is in artifacts/verification.json. These checks supplement the function-space proof and establish neither priority nor formal or expert certification.

## Relationship to prior work

The old norm family does include this norm. The 2017 discussion and 2018 paper use
\[
\|f\|_{\langle D\rangle}
=\sup_{(t,s)\in D}\bigl(|f(t)|+|f'(s)|\bigr).
\]
With \(D=\{0\}\times[0,1]\) this equals \(\|f\|_\sigma\). A different-norm exclusion would be false.

The corrected 2019 Proposition 3.1 assumes connected closed \(D\subset[0,1]^2\), projection intervals \([a,b]\) and \([c,d]\), their union equal to \([0,1]\), and expressly \(a<b\). Thus it does not classify the present \(a=b=0\) case. Remark 2 explicitly separates \(D=\{a\}\times[0,1]\) and gives examples there. Corrected Proposition 3.2 again requires \(a<b\). Corrected Proposition 3.5 concerns decreasing symbols: its second branch requires \(a<b\), while its first branch has both projection intervals equal to \([0,1]\). Neither is this degenerate identity-symbol setting. The uncorrected 2018 propositions cannot be used as valid stronger coverage after the corrigendum.

This boundary distinction does not make the scalar construction new. Remark 1 already supplies arbitrary-phase conjugate-linear reflection projections. Remark 2's second example places a conjugation projection on the evaluation coordinate and zero on the derivative coordinate. Our Form III map places the identity on the evaluation coordinate and the scalar projection pointwise on the derivative coordinate. This is a simple coordinate lifting of the known ingredient, not a newly invented technique. The surviving claim is the explicit non-antipodal failure of the later v1 classification and its invalid change-of-phase proof inference.

The related analytic-space manuscript's Example 1.9 uses fixed real-part and imaginary-part projections with antipodal associated phases. It does not give this \((1,i)\) correction to the \(C^1\) v1 theorem. Its analogous asserted bicircularity conclusion is not valid stronger coverage proving the audited correction. Published-corpus follow-ups dated after this record do not establish priority over it.

## Limitations

The scalar/reflection formulas are known and the coordinate lifting is elementary. Originality is claimed only for the correction to the identified later statements, to the best of available knowledge. An unlocated earlier correction of those exact statements remains a priority risk; search absence is not proof of first discovery.

This is not a classification of all idempotents, degenerate norm sets, or allowed phase combinations. The phase-squared check is confined to the specified involutive branch.

## References

- H. Kumar, H. Kumar, A. B. Abu Baker, *Structure of Generalized bi-circular idempotents and isometric reflections on \(C^1[0,1]\)*, arXiv:2609.18967v1, abstract and Theorems 3.1--3.4. [Full text](https://arxiv.org/html/2609.18967v1).
- F. Botelho, T. Miura, *Corrigendum to “Examples of generalized bi-circular idempotents on spaces of continuously differentiable functions”*, JMAA 474 (2019), 1481--1487, Proposition 3.1, Remarks 1--2, Propositions 3.2 and 3.5. [DOI](https://doi.org/10.1016/j.jmaa.2019.02.032).
- F. Botelho, T. Miura, *Examples of generalized bi-circular idempotents on spaces of continuously differentiable functions*, JMAA 465(2) (2018), 795--802; use with its corrigendum. [DOI](https://doi.org/10.1016/j.jmaa.2018.05.022).
- F. Botelho, T. Miura, *Contractive projections on subspaces of continuous functions*, RIMS Kôkyûroku 2035 (2017), 156--167, Section 3, page 165. [Primary PDF](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2035-19.pdf).
- H. Kumar, A. B. Abu Baker, F. Botelho, *Generalized bi-circular idempotents on some spaces of analytic functions*, author-hosted manuscript, Example 1.9 and Section 3. [Primary PDF](https://profile.iiita.ac.in/abdullah/F13.pdf).
