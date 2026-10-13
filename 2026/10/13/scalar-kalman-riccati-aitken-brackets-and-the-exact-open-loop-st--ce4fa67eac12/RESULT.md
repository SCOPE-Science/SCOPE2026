# Scalar Kalman Riccati Aitken brackets and the exact open-loop stability boundary

## Finding
For the scalar Kalman prediction-covariance Riccati map
\[
F(P)=q+\frac{a^2rP}{h^2P+r},
\qquad
q>0,\quad r>0,\quad h\ne0,
\]
let \(p>0>m\) be its two fixed points. If
\[
0<|a|\le1,\qquad 0\le P_0<p,
\]
then the raw Riccati iteration \(P_{n+1}=F(P_n)\) and its three-point Aitken transforms
\[
\widehat P_n
=
P_n-\frac{(P_{n+1}-P_n)^2}{P_{n+2}-2P_{n+1}+P_n}
\]
form a two-sided certificate:
\[
P_{n+2}<p<\widehat P_n
\qquad(n\ge0).
\]
The lower bounds increase to \(p\), while the Aitken upper bounds decrease to \(p\).

More strongly, Aitken has an exact projective-error interpretation. Define
\[
t(P)=\frac{P-p}{P-m},
\qquad
\rho=F'(p)
=
\frac{a^2r^2}{(h^2p+r)^2}.
\]
Then
\[
t(P_{n+1})=\rho\,t(P_n)
\]
and
\[
t(\widehat P_n)=t(P_{n+1})^2.
\]
Thus the acceleration squares the one-step projective error exactly.

The condition \(|a|\le1\) is sharp as a parameter-uniform bracketing condition. For every \(|a|>1\), some positive-noise scalar filter started from zero has a negative first Aitken estimate, despite a positive stabilizing Riccati solution.

## Assumptions and scope
The state and measurement model is scalar and time invariant:
\[
X_{k+1}=aX_k+W_k,\qquad
Y_k=hX_k+V_k,
\]
with process-noise variance \(q>0\) and measurement-noise variance \(r>0\). The map above is the one-step prediction-covariance Riccati recursion obtained by composing measurement correction with prediction.

The theorem assumes a nonzero plant gain \(a\), a nonzero observation coefficient \(h\), exact arithmetic, and a lower initial covariance \(0\le P_0<p\). The case \(a=0\) is trivial because the Riccati map is the constant \(F(P)=q\).

The statement concerns the scalar covariance recursion and one Aitken transform applied to each consecutive triple. It does not assert an analogous Loewner-order bracket for matrix Riccati equations or stability of recursively feeding the Aitken value back into the filter.

## Proof
The fixed-point equation \(P=F(P)\) is
\[
h^2P^2+\bigl(r(1-a^2)-qh^2\bigr)P-qr=0.
\]
Its constant term is negative, so its two roots satisfy
\[
p>0>m,
\qquad
pm=-\frac{qr}{h^2}.
\]
The sum is
\[
p+m
=
q-\frac{r(1-a^2)}{h^2}.
\]

The map is a Möbius transformation:
\[
F(P)
=
\frac{(qh^2+a^2r)P+qr}{h^2P+r}.
\]
Conjugating a Möbius transformation by the cross-ratio coordinate that sends its fixed points to \(0\) and infinity yields multiplication. Here
\[
t(P)=\frac{P-p}{P-m}
\]
gives
\[
t(F(P))=\rho\,t(P),
\]
where the multiplier equals the derivative at the attracting fixed point:
\[
\rho=F'(p)
=
\frac{a^2r^2}{(h^2p+r)^2}.
\]
For \(a\ne0\), one has \(0<\rho<1\). Indeed, if \(|a|<1\), then \(h^2p+r>r>|a|r\); if \(|a|\ge1\), the fixed-point identity implies \(h^2p+r>a^2r\ge|a|r\).

Write the inverse projective coordinate as
\[
\phi(t)=\frac{p-mt}{1-t}.
\]
Thus
\[
P_n=\phi(t_n),
\qquad
t_n=\rho^nt_0.
\]
Because \(0\le P_0<p\), one has \(t_0<0\), and hence every \(P_n<p\) while \(P_n\uparrow p\).

For any \(t\) and \(0<\rho<1\), direct algebra applied to the three Möbius-orbit values
\[
\phi(t),\qquad \phi(\rho t),\qquad \phi(\rho^2t)
\]
gives
\[
\phi(t)
-\frac{\bigl(\phi(\rho t)-\phi(t)\bigr)^2}
{\phi(\rho^2t)-2\phi(\rho t)+\phi(t)}
=
\phi(\rho^2t^2).
\]
Therefore
\[
\widehat P_n=\phi(t_{n+1}^2),
\]
or equivalently
\[
\frac{\widehat P_n-p}{\widehat P_n-m}
=
\left(
\frac{P_{n+1}-p}{P_{n+1}-m}
\right)^2.
\]

It remains to show that the squared projective coordinate lies in \((0,1)\). Since \(F\) is increasing,
\[
P_1\ge F(0)=q.
\]
Also
\[
2q-(p+m)
=
q+\frac{r(1-a^2)}{h^2}>0
\]
when \(|a|\le1\). Hence
\[
P_1>\frac{p+m}2.
\]
For \(P>m\), the inequality \(t(P)>-1\) is equivalent to \(P>(p+m)/2\). Thus
\[
-1<t_1<0.
\]
Since \(t_{n+1}=\rho^nt_1\),
\[
-1<t_{n+1}<0
\]
for every \(n\ge0\), so
\[
0<t_{n+1}^2<1.
\]
The function \(\phi\) is strictly increasing, \(\phi(0)=p\), and \(\phi(s)>p\) for \(0<s<1\). Therefore
\[
P_{n+2}<p<\widehat P_n.
\]
Moreover \(|t_{n+1}|\) decreases strictly, so \(t_{n+1}^2\downarrow0\) and \(\widehat P_n\downarrow p\). The same inequalities also exclude a vanishing Aitken denominator.

For sharpness, let \(|a|>1\), set
\[
h=r=1,\qquad P_0=0,
\]
and choose
\[
0<q<a^2-1.
\]
Then
\[
P_1=q,
\qquad
P_2=q+\frac{a^2q}{q+1},
\]
and
\[
P_2-2P_1+P_0
=
\frac{q(a^2-1-q)}{q+1}>0.
\]
Hence
\[
\widehat P_0
=
-\frac{q(q+1)}{a^2-1-q}<0.
\]
The positive fixed point \(p\) still exists because the fixed-point quadratic has negative constant term. Thus no parameter-uniform conservative-bracket theorem can extend past \(|a|=1\).

## Verification
The embedded `verify.py` uses exact rational and symbolic arithmetic.

For the stable unit-parameter case
\[
a=h=q=r=1,\qquad P_0=0,
\]
the raw values are
\[
P_0=0,\qquad P_1=1,\qquad P_2=\frac32,\qquad P_3=\frac85.
\]
The first two Aitken estimates are
\[
\widehat P_0=2,\qquad
\widehat P_1=\frac{13}8.
\]
The stabilizing covariance is
\[
p=\frac{1+\sqrt5}2,
\]
so
\[
\frac32<p<\frac{13}8<2.
\]

For the unstable witness
\[
a=2,\qquad h=q=r=1,\qquad P_0=0,
\]
one has
\[
P_1=1,\qquad P_2=3,\qquad \widehat P_0=-1.
\]
The stabilizing covariance is \(2+\sqrt5>0\).

The verifier also symbolically checks the Möbius-orbit Aitken identity. These finite and symbolic checks corroborate the displayed derivations; the theorem itself is proved above.

## Relationship to prior work
Classical Kalman-filter convergence theory studies the covariance through the discrete Riccati iteration. Carli and Sepulchre emphasize that the Riccati map is naturally understood through projective geometry and contraction, and their full text recalls both monotone covariance convergence from a zero start and geometric contraction approaches. Their paper does not discuss Aitken acceleration or the scalar cross-ratio squaring identity.

Han and Zhang derive optimal filters in terms of Riccati difference equations and classify their filtering paper primarily under \(93\mathrm E11\), confirming the control/filtering ownership of this problem.

A recent paper by Xie, Ma, and Li applies Aitken acceleration to a different nonsymmetric algebraic Riccati equation arising in transport theory. The accessible article material states that Aitken can improve simple iteration but can also slow convergence in a critical case. That work has different Riccati structure and does not supply the scalar Kalman covariance bracket or the open-loop stability boundary proved here.

The closest semantic-database comparison is a black-box Aitken--Steffensen robustness theorem for arbitrary scalar contractions. Under that much weaker hypothesis, Aitken may amplify fixed-point error. The present result identifies a Möbius Riccati subclass where projective structure instead gives an exact squared-error law and certified two-sided bounds.

## Limitations
The result is scalar. Matrix Riccati maps do possess projective and order geometry, but scalar cross-ratio squaring does not automatically lift to a matrix Aitken transform.

The upper bracket assumes a lower start \(P_0<p\). It does not classify Aitken behavior from arbitrary overestimates of the steady covariance.

The stable-side theorem applies Aitken as a diagnostic/extrapolation formula to raw Riccati triples. It does not claim that feeding \(\widehat P_n\) back into a Kalman recursion preserves covariance consistency.

The sharpness statement is parameter-uniform: an unstable plant can still have particular parameter choices for which Aitken behaves conservatively, but for every \(|a|>1\) there are positive noise parameters producing a negative first extrapolate.

Residual originality risk remains that older scalar Riccati or continued-fraction literature may encode the same cross-ratio/Aitken identity without Kalman terminology. A highly relevant 2026 Aitken--Riccati paper was accessible only at abstract/reference level in the retrieval used here, so it remains an explicit comparison risk rather than whole-document noncoverage evidence.

## References
1. C. Han and H. Zhang, “Optimal Filtering in Discrete-Time Systems with Time Delays and Markovian Jump Parameters,” ANZIAM Journal 51 (2009), 218–233, DOI 10.1017/S1446181110000076; published online 2010-06-18; primary MSC 93E11.
2. F. P. Carli and R. Sepulchre, “On the Projective Geometry of Kalman Filter,” arXiv:1503.09113, first public version 2015-03-31.
3. Z. Xie, C. Ma, and S. Li, “An Aitken method for accelerating the solution of the non-symmetric algebraic Riccati equation in transport theory,” AIMS Mathematics 11 (2026), 24090–24105, DOI 10.3934/math.2026971.
