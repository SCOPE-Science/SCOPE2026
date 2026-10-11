# A convex-sector counterexample to the proposed Carathéodory-component positivity principle

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and let \(\mathcal K\) denote the normalized convex univalent functions on \(\mathbb D\). For \(f\in\mathcal K\), put
\[
A_f(z)=\frac{zf'(z)}{f(z)},\qquad P_f(z)=1+\frac{zf''(z)}{f'(z)}.
\]
Grigoriciuc's proposed \(\alpha\)-Carathéodory component, in his Definition 1, is
\[
h_\alpha[f](z)=\frac{\alpha(1-\alpha)A_f(z)^2+(2\alpha^2-\alpha)A_f(z)+(1-\alpha)(\alpha+P_f(z))}{P_f(z)(1-\alpha+\alpha A_f(z))}.
\]
The universal assertion \(\operatorname{Re}h_\alpha[f](z)>0\) for all \(f\in\mathcal K\), \(0\le\alpha\le1\), and \(z\in\mathbb D\) is **false**, already at \(\alpha=1/2\). Indeed, the normalized convex function
\[
f(z)=\sqrt{\frac{1+z}{1-z}}-1,
\]
where the square root takes the principal branch, has a point \(z_0\in\mathbb D\) with
\[
-\frac12<\operatorname{Re}h_{1/2}[f](z_0)<-\frac14.
\]
An exact rational-algebraic witness is obtained by setting
\[
T=\frac{29}{54}\left(1-\frac{99999}{100000}i\right),
\qquad z_0=\frac{T^2-1}{T^2+1}.
\]

## Assumptions and scope

The ratio \((1+z)/(1-z)\) maps \(\mathbb D\) conformally onto the right half-plane. The principal square root therefore takes its values precisely in the sector \(\{t:|\arg t|<\pi/4\}\). The statement concerns the particular \(\alpha\)-Carathéodory component defined above; it makes no assertion that the Graham–Kohr extension operator fails to preserve any other property.

## Proof

**Convexity and normalization.** The sector \(\{t:|\arg t|<\pi/4\}\) is the intersection of the two open half-planes \(\operatorname{Re}t>\operatorname{Im}t\) and \(\operatorname{Re}t>-\operatorname{Im}t\). It is convex. Hence \(f(\mathbb D)\), this sector translated by \(-1\), is convex; \(f\) is univalent. Direct differentiation gives \(f(0)=0\) and \(f'(0)=1\), so \(f\in\mathcal K\).

**Exact interior witness.** Since \(\operatorname{Re}T>|\operatorname{Im}T|\), the number \(T^2\) lies in the right half-plane. Its inverse Cayley image \(z_0\) is therefore inside \(\mathbb D\), and the chosen square root at \(z_0\) equals \(T\). More explicitly, rational arithmetic gives
\[
|z_0|^2=\frac{1133202532433629317088307281}{1133222151183535077088307281}<1.
\]
Writing \(t=\sqrt{(1+z)/(1-z)}\), elementary differentiation yields
\[
A_f(z)=\frac{(t+1)(t^2+1)}{4t},\qquad
P_f(z)=\frac{3t^4+1}{4t^2}.
\]
One can independently obtain these identities from \(f'(z)=1/\bigl(t(1-z)^2\bigr)\) and \(f''(z)/f'(z)=3/\bigl(2(1-z)\bigr)-1/\bigl(2(1+z)\bigr)\).

At \(\alpha=1/2\), the middle term in the numerator vanishes, giving
\[
h_{1/2}[f](z)=\frac{A_f(z)^2+1+2P_f(z)}{2P_f(z)(1+A_f(z))}.
\]
Substituting \(t=T\), simplifying over \(\mathbb Q(i)\), and taking the real part gives the exact value
\[
\operatorname{Re}h_{1/2}[f](z_0)=
-\frac{393604134232598370597082686478721497781923239383876934628488346374094310839195813073936519}{1003500319773081662035210917844648202605964049927384209786136637010545649385413321556380886}.
\]
The numerator and denominator are positive integers, and integer cross-multiplication places this fraction strictly between \(-1/2\) and \(-1/4\). Moreover, \(\operatorname{Re}P_f(z_0)>0\) and \(\operatorname{Re}(1+A_f(z_0))>0\), so all displayed denominators are nonzero. This proves the counterexample.

## Verification

The self-contained script `verify_counterexample.py` uses only Python's `fractions.Fraction` and exact rational-complex arithmetic. From the stated \(T\), it recomputes \(z_0\), the disk-membership inequality, both derivative identities, the original component expression, the simplified expression, and the exact negative real part. Run `python3 verify_counterexample.py` with the script beside this document. The strict inequalities follow from integer comparisons; no numerical sampling or approximation supplies the proof.

## Relationship to prior work

Grigoriciuc [1, Definition 1; Conjectures 1–3] proposed universal half-plane positivity of this component and presented positive numerical evidence on standard convex examples, including fractional linear maps, logarithmic maps, and coefficient-controlled polynomials. The present function maps the disk onto a translated proper convex sector, rather than a half-plane, and its component violates the proposed sign condition. Thus the conclusion of Conjecture 1, as well as its pointwise positivity reformulation (Conjecture 2), is false. The conditional extension statement in [1, Theorem 4] is **not** refuted as a separate theorem: its hypothesis is false, so that route to an unconditional conclusion does not apply. Earlier successful half-plane examples do not imply positivity for every convex range.

## Limitations

The example establishes failure for one explicit convex function and for the interior parameter \(\alpha=1/2\); it does not classify all failing functions or parameters, and it does not by itself establish nonmembership of a higher-dimensional Graham–Kohr extension in a prescribed mapping class. The witness lies near the unit circle, which explains why finitely sampled numerical tests need not detect it.

## References

[1] E. Ş. Grigoriciuc, *A conjecture related to convex functions on the unit disc: numerical approach and extension results*, The Journal of Analysis **34** (2026), 2013–2037. DOI: 10.1007/s41478-026-01067-z. First publicly verified 2026-04-20. Sections 2–3, especially Definition 1, Conjectures 1–3, Examples 2–12, and Theorem 4.
