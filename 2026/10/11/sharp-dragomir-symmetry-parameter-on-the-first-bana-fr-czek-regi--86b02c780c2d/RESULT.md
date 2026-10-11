# Sharp Dragomir symmetry parameter on the first Banaś--Frączek regime
## Finding
Let \(R_\lambda^2=(\mathbb R^2,N_\lambda)\), where \(1<\lambda\le\sqrt2\) and
\[
N_\lambda(u,v)=\max\{\lambda|u|,\sqrt{u^2+v^2}\}.
\]
For \(\varepsilon\in[0,1)\), write \(a\perp_D^\varepsilon b\) when
\[
N_\lambda(a+t b)\ge\sqrt{1-\varepsilon^2}\,N_\lambda(a)
\qquad(t\in\mathbb R).
\]
Then the least \(\varepsilon\) such that
\[
x\perp_B y\Longrightarrow y\perp_D^\varepsilon x
\qquad(x,y\in R_\lambda^2)
\]
is
\[
\varepsilon_D(R_\lambda^2)=\sqrt{1-\lambda^{-2}}.
\]
Equivalently,
\[
\inf_{\substack{x,y\in S_{R_\lambda^2}\\x\perp_B y}}
\inf_{t\in\mathbb R}N_\lambda(y+t x)=\frac1\lambda.
\]
Equality is attained at
\[
x=\left(\frac1\lambda,\sqrt{1-\lambda^{-2}}\right),
\qquad y=(0,-1),
\]
and at their images under the sign symmetries.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
N_\lambda(x+t y)\ge N_\lambda(x)
\qquad(t\in\mathbb R).
\]
The modified Dragomir relation is
\[
a\perp_D^\varepsilon b
\quad\Longleftrightarrow\quad
N_\lambda(a+t b)\ge\sqrt{1-\varepsilon^2}\,N_\lambda(a)
\qquad(t\in\mathbb R).
\]
Only the first Banaś--Frączek regime \(1<\lambda\le\sqrt2\) is treated.

## Proof
Put
\[
\alpha=\frac1\lambda,
\qquad
\beta=\sqrt{1-\alpha^2}.
\]
In the stated regime \(0<\beta\le\alpha<1\). The unit ball is the clipped Euclidean disk
\[
B=\{(u,v):u^2+v^2\le1,\ |u|\le\alpha\}.
\]
For a unit Birkhoff pair define the reverse line distance
\[
d(x,y)=\inf_{t\in\mathbb R}N_\lambda(y+t x).
\]
Then
\[
\sqrt{1-\varepsilon_D(R_\lambda^2)^2}
=
\inf_{\substack{x,y\in S_{R_\lambda^2}\\x\perp_B y}}d(x,y).
\]
We compute this infimum on the three possible sphere strata.

First let \(x=(c,s)\) be on a smooth circular arc, with \(0\le c<\alpha\), \(s=\sqrt{1-c^2}\), using the sign symmetries. The unique norming functional is the Euclidean functional \((c,s)\), so the Birkhoff direction is proportional to \((-s,c)\). If \(s\le\alpha\), then \((-s,c)\) is already a unit vector and the annihilating functional \((-s,c)\) has dual norm one; hence
\[
d(x,y)=1.
\]
If \(s>\alpha\), the unit Birkhoff vector is
\[
y=\frac{\alpha}{s}(-s,c),
\]
and the support of the clipped disk in the direction \((-s,c)\) is attained at the corner \((-\alpha,\beta)\). Therefore
\[
d(x,y)
=
\frac{\alpha}{s(\alpha s+\beta c)}.
\]
Now
\[
\alpha s^2+\beta s c
\le\frac{1+\alpha}{2},
\]
because this is the largest eigenvalue of the quadratic form \(\alpha s^2+\beta s c\) on \(s^2+c^2=1\), using \(\alpha^2+\beta^2=1\). Thus
\[
d(x,y)\ge\frac{2\alpha}{1+\alpha}>\alpha.
\]

Next let \(x=(\alpha,t)\) be in the relative interior of a vertical edge, \(|t|<\beta\). Its unique norming functional is horizontal, so the unit Birkhoff direction is \(y=(0,\pm1)\); take \(y=(0,1)\). The functional \((-t,\alpha)\) annihilates \(x\). Since \(\beta\le\alpha\), its Euclidean support point lies inside the clipped disk, so its dual norm is \(\sqrt{t^2+\alpha^2}\). The two-dimensional quotient-distance formula gives
\[
d(x,y)=\frac{\alpha}{\sqrt{t^2+\alpha^2}}\ge\alpha.
\]

Finally take the corner \(x=(\alpha,\beta)\). Its norming functionals form the segment joining the circular support \((\alpha,\beta)\) and the vertical support \((1/\alpha,0)\). Hence, apart from sign and normalization, every Birkhoff direction has the form
\[
y_r=\frac{(1,-r)}{\sqrt{1+r^2}},
\qquad
r\ge\frac{\alpha}{\beta},
\]
with the limiting case \(r=\infty\) interpreted as \((0,-1)\). The functional \((\beta,-\alpha)\) annihilates \(x\), is Euclidean unit, and has dual norm one because \(\beta\le\alpha\). Therefore
\[
d(x,y_r)=\frac{\beta+\alpha r}{\sqrt{1+r^2}}.
\]
Its derivative has the sign of \(\alpha-\beta r\), so it is nonincreasing for \(r\ge\alpha/\beta\), and
\[
\inf_{r\ge\alpha/\beta}d(x,y_r)=\alpha.
\]
The limit is attained by the endpoint Birkhoff direction \(y=(0,-1)\).

The circular arcs, open vertical edges, and four corners exhaust the unit sphere. Consequently
\[
\inf_{\substack{x,y\in S_{R_\lambda^2}\\x\perp_B y}}d(x,y)=\alpha=\frac1\lambda.
\]
Thus
\[
\varepsilon_D(R_\lambda^2)
=
\sqrt{1-\alpha^2}
=
\sqrt{1-\lambda^{-2}}.
\]

## Verification
The proof is exact and exhaustive. The unit ball is literally the intersection of the Euclidean disk with the vertical strip \(|u|\le1/\lambda\), so every unit vector lies on a circular arc, a vertical edge, or a corner. Smooth points have one norming functional, while each corner uses the complete segment of norming functionals.

For any nonzero functional \(\phi\) annihilating \(x\) in a two-dimensional normed space,
\[
\inf_{t\in\mathbb R}\|y+t x\|
=
\frac{|\phi(y)|}{\|\phi\|_*}.
\]
This quotient-space identity makes every displayed reverse line distance exact, not merely a lower estimate. No numerical optimization or finite sampling is used in the proof.

## Relationship to prior work
Yang's 2014 paper computes the Jordan--von Neumann constant of the Banaś--Frączek plane. Yang and Yang later study the generalized family
\[
\|x\|_{\lambda,p}=\max\{\lambda|x_1|,\|x\|_p\}
\]
and determine James-type and von Neumann--Jordan constants. These results concern different geometric functionals and do not determine reverse Birkhoff line distance.

Chmieliński, Khurana, and Sain define the modified Dragomir approximate relation and prove that every finite-dimensional Banach space has some global D-approximate-symmetry parameter. Their theorem is existential and does not provide the least parameter for the Banaś--Frączek family.

Targeted searches under the Banaś--Frączek, clipped-Euclidean-disk, modified-Dragomir, reverse Birkhoff line-distance, and exact-value formulations did not locate the formula above. Indexed same-object exact results concern Ptolemy, Banach--Mazur, Jordan--von Neumann, or related constants; indexed exact modified-Dragomir results concern different spaces.

## Limitations
The theorem is restricted to \(1<\lambda\le\sqrt2\). The second Banaś--Frączek regime has different boundary geometry because the corner height exceeds the strip half-width, and no claim about its optimal modified-Dragomir parameter is made here.

A differently notated exact treatment outside the checked sources remains a bibliographic risk. Search nonappearance by itself is not used as a novelty proof.

## References
1. C. Yang, “Jordan--von Neumann constant for Banaś--Frączek space,” *Banach Journal of Mathematical Analysis* 8 (2014), 185--192, DOI 10.15352/BJMA/1396640062.
2. C. Yang and X. Yang, “On the James type constant and von Neumann--Jordan constant for a class of Banaś--Frączek type spaces,” *Journal of Mathematical Inequalities* 10 (2016), 551--558, DOI 10.7153/jmi-10-43.
3. J. Chmieliński, D. Khurana, and D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” arXiv:2012.08162, first posted 2020-12-15.
