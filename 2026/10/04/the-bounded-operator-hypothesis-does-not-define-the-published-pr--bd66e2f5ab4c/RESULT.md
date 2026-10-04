# The bounded-operator hypothesis does not define the published predator–prey feedback

## Finding

Lamrani, El Harraki, Aziz-Alaoui, and El Alaoui propose the scalar feedback
\[
v(Z_1,Z_2)=-(D+\eta)
\frac{\|Z_1\|^2+\|Z_2\|^2}
{\langle BZ_1,Z_1\rangle+\langle BZ_2,Z_2\rangle}
\]
for every nonzero pair \((Z_1,Z_2)\), while Theorems 2.1 and 2.3 assume only that \(B\) is a bounded operator on the real Hilbert space \(H=L^2(\Omega)\).

Boundedness alone does not make this formula well defined. The bounded operator \(B=0\) makes the denominator vanish at every nonzero state. More generally, if
\[
S=\frac{B+B^*}2,
\]
then
\[
\langle Bz,z\rangle=\langle Sz,z\rangle,
\]
so the denominator depends only on the symmetric part of \(B\). A skew-adjoint operator therefore contributes zero quadratic form, and an indefinite symmetric part permits cancellation between the two state components.

There is an exact operator-theoretic classification. The denominator is nonzero for every nonzero pair \((Z_1,Z_2)\) if and only if the quadratic form
\[
q(z)=\langle Sz,z\rangle
\]
is strictly positive for every \(z\ne0\), or strictly negative for every \(z\ne0\).

For a uniformly bounded feedback, a uniform one-sided coercivity condition gives the required lower bound: for some \(\beta>0\),
\[
\langle Sz,z\rangle\ge\beta\|z\|^2
\]
for every \(z\), or the corresponding negative inequality. Under this condition,
\[
|v(Z_1,Z_2)|\le\frac{|D+\eta|}{\beta}
\]
for every nonzero pair. Strict positivity without coercivity is not enough: on \(\ell^2\), the bounded positive operator \(Be_n=n^-1e_n\) has positive quadratic form on every nonzero vector, but
\[
|v(e_n,0)|=|D+\eta|n,
\]
which is unbounded.

The issue reaches a concrete application in the paper. In its Holling-IV case the source takes
\[
BY=(1-\mu(x))Y
\]
with only \(\mu\in L^\infty(\Omega)\) stated. The admissible choice \(\mu\equiv1\) gives \(B=0\), so the printed feedback is undefined at every nonzero state although the text declares the system exponentially stabilizable.

## Assumptions and scope

The classification concerns the feedback denominator in the real Hilbert-space setting used by the source. It does not assert that coercivity alone repairs every other step of the nonlinear well-posedness proof. It gives the exact condition for pointwise nonvanishing of the denominator and a uniform lower bound sufficient for a state-independent bound on the feedback quotient.

The source's first listed subject classification is \(92D25\). Its public PDF states publication on 2 November 2022.

## Proof

Let
\[
Q(Z_1,Z_2)=\langle BZ_1,Z_1\rangle+\langle BZ_2,Z_2\rangle.
\]
For real \(H\), decompose \(B=S+K\), where
\[
S=\frac{B+B^*}2,\qquad K=\frac{B-B^*}2.
\]
Since \(K^*=-K\),
\[
\langle Kz,z\rangle=0
\]
for every \(z\), hence
\[
Q(Z_1,Z_2)=q(Z_1)+q(Z_2),\qquad q(z)=\langle Sz,z\rangle.
\]

Suppose first that \(Q\) is nonzero for every nonzero pair. Taking \((z,0)\) shows \(q(z)\ne0\) for every \(z\ne0\). If \(q\) assumed both signs, there would be vectors \(u,w\) with \(q(u)>0\) and \(q(w)<0\). Scaling \(w\) by
\[
t=\sqrt{\frac{q(u)}{-q(w)}}
\]
would give
\[
Q(u,tw)=q(u)+t^2q(w)=0,
\]
a contradiction. Thus \(q\) is strictly one-signed.

Conversely, if \(q(z)>0\) for every \(z\ne0\), then at least one term in
\[
Q(Z_1,Z_2)=q(Z_1)+q(Z_2)
\]
is positive for every nonzero pair, so \(Q>0\). The negative case is identical after changing signs. This proves the exact well-definedness classification.

If, more strongly,
\[
q(z)\ge\beta\|z\|^2
\]
for some \(\beta>0\), then
\[
Q(Z_1,Z_2)\ge\beta(\|Z_1\|^2+\|Z_2\|^2),
\]
and substitution into the feedback formula yields
\[
|v(Z_1,Z_2)|\le\frac{|D+\eta|}{\beta}.
\]
The negative-coercive case follows by absolute values.

To see that strict positivity need not imply such a uniform bound, let \((e_n)\) be the standard basis of \(\ell^2\) and define
\[
Be_n=\frac1n e_n.
\]
Then \(B\) is bounded, self-adjoint, and \(\langle Bz,z\rangle>0\) for every nonzero \(z\), but
\[
\langle Be_n,e_n\rangle=\frac1n.
\]
For \((Z_1,Z_2)=(e_n,0)\), the feedback magnitude equals \(|D+\eta|n\), proving lack of a state-independent bound.

Finally, the source's Holling-IV multiplier \(B=(1-\mu)I\) permits \(\mu\equiv1\) under the stated assumption \(\mu\in L^\infty\). That choice is exactly \(B=0\), so the theorem's denominator vanishes for every nonzero state.

## Verification

The bundled script checks four finite-dimensional representatives of the operator geometry: a zero operator, a skew-symmetric operator, an indefinite symmetric operator, and a coercive positive operator. It also verifies the exact cancellation for an indefinite form and the growing quotient for the diagonal family with eigenvalues \(1/n\).

These computations are finite checks of explicit witnesses; the infinite-dimensional statements above are proved analytically.

## Relationship to prior work

The source itself labels Theorem 2.3 as its main result and states only boundedness of \(B\) before displaying the quotient feedback. Its earlier linear Theorem 2.1 uses the same quotient and the same bounded-operator hypothesis. The paper's Holling-III application chooses a multiplication operator bounded below by a positive constant, which is compatible with coercivity; this shows that the missing condition is not merely cosmetic. By contrast, its Holling-IV application imposes only \(\mu\in L^\infty\) on \(B=(1-\mu)I\), which allows the zero operator.

Searches for the article title, DOI, the displayed quadratic denominator, and combinations of “bounded operator,” “coercive,” and “feedback stabilization” did not locate an erratum or a published correction of this operator hypothesis. Related bilinear-control literature cited by the source supplies general stabilization context, but it does not make the displayed quotient defined for an arbitrary bounded \(B\).

## Limitations

This result invalidates the literal all-bounded-operator formulation of the displayed feedback and identifies the missing denominator/coercivity requirement. It does not re-prove the source's complete nonlinear stabilization theorem under the repaired hypothesis, and it does not claim that every numerical example in the paper uses a singular control operator.

## References

1. I. Lamrani, I. El Harraki, M. A. Aziz-Alaoui, F.-Z. El Alaoui, “Feedback stabilization for prey predator general model with diffusion via multiplicative controls,” AIMS Mathematics 8 (2023), 2360–2385. DOI: 10.3934/math.2023122.
2. L. Berrahmoune, “Stabilization and decay estimate for distributed bilinear systems,” Systems & Control Letters 36 (1999), 167–171. DOI: 10.1016/S0167-6911(98)00065-6.
