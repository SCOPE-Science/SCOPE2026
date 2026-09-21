# Arbitrarily high starlike order does not force harmonic univalence

## Statement

Let \(0<\beta<1\). Choose an integer
\[
N>\frac{3\beta}{2(1-\beta)}
\]
and set
\[
a=\frac{1-\beta}{N-\beta},\qquad
h(z)=z-a z^N,
\]
\[
g(z)=\frac{z^2}{2}-\frac{Na}{N+1}z^{N+1},\qquad
f(z)=h(z)+\overline{g(z)}.
\]
Then:

1. \(f\) is normalized, locally univalent, and sense-preserving in the unit disk \(\mathbb D\);
2. \(h\) is starlike of order \(\beta\), and its exact starlike order is \(\beta\);
3. \(f\) is not univalent in \(\mathbb D\).

Consequently, for every prescribed \(\beta_0<1\) there is a normalized locally univalent sense-preserving harmonic map whose analytic part is starlike of some order strictly larger than \(\beta_0\), but which is not injective. Thus no universal sufficient starlike-order threshold below \(1\) can guarantee univalence.

This addresses the threshold question raised in Remark 18 of Zhu and Huang (2015): all nondegenerate candidate orders below \(1\) fail. The limiting identity/convex endpoint is a separate classical sufficient case.

## Context

Zhu and Huang asked for the sharp order \(\beta\) for which local univalence and sense preservation, together with a starlike analytic part of order \(\beta\), force global univalence. Earlier work already showed that an arbitrary starlike analytic part (order zero) does not suffice. In particular, Nagpal and Ravichandran gave the example
\[
h(z)=z-\frac{z^2}{2},\qquad g(z)=\frac{z^2}{2}-\frac{z^3}{3},
\]
for which \(g'(z)=zh'(z)\) and the associated harmonic map is sense-preserving but nonunivalent. The theorem above shows that this obstruction persists at starlike orders arbitrarily close to one.

## Proof

Because
\[
g'(z)=z h'(z),
\]
the second complex dilatation is
\[
\omega(z)=\frac{g'(z)}{h'(z)}=z.
\]
Moreover,
\[
h'(z)=1-Na z^{N-1},
\qquad
Na=\frac{N(1-\beta)}{N-\beta}<1.
\]
Hence \(h'\) has no zero in \(\mathbb D\), and
\[
J_f(z)=|h'(z)|^2(1-|z|^2)>0.
\]
Thus \(f\) is locally univalent and sense-preserving.

To verify the starlike order, write \(w=z^{N-1}\). Then
\[
\frac{zh'(z)}{h(z)}=\frac{1-Na w}{1-a w},
\]
and the choice \((N-\beta)a=1-\beta\) gives
\[
\frac{zh'(z)}{h(z)}-\beta
=(1-\beta)\frac{1-w}{1-a w}.
\]
For \(|w|<1\),
\[
\operatorname{Re}\frac{1-w}{1-a w}
=\frac{1-(1+a)\operatorname{Re}w+a|w|^2}{|1-aw|^2}
>0,
\]
because if \(r=|w|<1\), the numerator is at least
\[
1-(1+a)r+ar^2=(1-r)(1-ar)>0.
\]
Therefore
\[
\operatorname{Re}\frac{zh'(z)}{h(z)}>\beta.
\]
Along positive real \(w\uparrow1\), the difference from \(\beta\) tends to zero, so the exact starlike order is \(\beta\).

It remains to show noninjectivity. Put
\[
H=h-g.
\]
Then
\[
H'(z)=(1-z)h'(z).
\]
At \(z=1\), define
\[
A=h'(1)=\frac{\beta(N-1)}{N-\beta}>0,
\qquad
B=h''(1)=-\frac{N(N-1)(1-\beta)}{N-\beta}<0.
\]
For \(u\to0\), Taylor expansion at \(1\) gives
\[
H(1-u)-H(1)=-\frac{A}{2}u^2+\frac{B}{3}u^3+O(u^4).
\]
Write \(u=x+iy\), and for \(y\ne0\) set
\[
\Psi(x,y)=\frac{\operatorname{Im}H(1-x-iy)}{y}.
\]
Since \(H\) has real coefficients, \(\Psi\) extends real-analytically across \(y=0\). Near \((0,0)\),
\[
\Psi(x,y)=-Ax+Bx^2-\frac{B}{3}y^2+O((|x|+|y|)^3).
\]
Thus \(\Psi(0,0)=0\) and \(\partial_x\Psi(0,0)=-A\ne0\). The implicit-function theorem gives a real-analytic branch \(x=x(y)\) with \(x(0)=0\), \(\Psi(x(y),y)=0\), and
\[
x(y)=c y^2+O(y^4),
\qquad
c=-\frac{B}{3A}=\frac{N(1-\beta)}{3\beta}.
\]
The hypothesis on \(N\) is precisely \(c>1/2\). Hence, for all sufficiently small nonzero \(y\),
\[
2x(y)-x(y)^2-y^2=(2c-1)y^2+O(y^4)>0.
\]
Therefore
\[
z_y=1-x(y)-iy\in\mathbb D.
\]
By construction \(H(z_y)\) is real. Since \(h\) and \(g\) have real coefficients,
\[
f(z)-f(\overline z)=H(z)-\overline{H(z)}.
\]
It follows that
\[
f(z_y)=f(\overline{z_y}),
\]
while \(z_y\ne\overline{z_y}\). Thus \(f\) is not univalent.

## Consequence for the threshold problem

Given any \(\beta_0<1\), select \(\beta\) with \(\beta_0<\beta<1\), and then choose \(N\) as above. The resulting analytic part has exact starlike order \(\beta>\beta_0\), yet the harmonic map is nonunivalent. Hence strengthening the analytic part merely by increasing its starlike order, short of the limiting endpoint, can never be a universal univalence criterion.

## Reproducibility

`artifacts/verify_starlike_order_harmonic.py` numerically checks representative parameters \((\beta,N)=(1/2,2),(0.9,14),(0.99,149)\): positivity of the starlike inequality at sample points and the local nonreal level branch \(\operatorname{Im}H=0\) inside \(\mathbb D\). The general result is proved analytically above; the numerical artifact is supplementary.

## Limitations and originality scope

The theorem does not classify additional hypotheses on the dilatation or on the analytic part that may restore univalence. It concerns universal criteria based only on the starlike order of the analytic part within the locally univalent sense-preserving class.

The originality assessment is to the best of our knowledge. The exact 2015 threshold question, synonymous formulations, the polynomial family above, and later literature on harmonic maps with starlike/Janowski-starlike analytic parts were compared. No prior result located in that comparison states that counterexamples exist for every order below one. A 2009 paper by Emel Yavuz on harmonic univalent functions with Janowski starlike analytic part is a residual literature risk because its full text was not inspected; available metadata suggests a sufficient subclass rather than the universal threshold considered here.

## References

1. M. Zhu and X. Huang, “The Distortion Theorems for Harmonic Mappings with Analytic Parts Convex or Starlike Functions of Order β,” *Journal of Mathematics* (2015), Article ID 460191. https://doi.org/10.1155/2015/460191
2. S. Nagpal and V. Ravichandran, “Starlikeness, convexity and close-to-convexity of harmonic mappings,” arXiv:1207.3404; later in *Current Topics in Pure and Computational Complex Analysis* (2014). https://arxiv.org/abs/1207.3404
3. I. Hotta and A. Michalski, “Locally one-to-one harmonic functions with starlike analytic part,” arXiv:1404.1826. https://arxiv.org/abs/1404.1826
4. J. G. Clunie and T. Sheil-Small, “Harmonic univalent functions,” *Ann. Acad. Sci. Fenn. Ser. A I Math.* 9 (1984), 3–25. https://doi.org/10.5186/aasfm.1984.0905
5. E. Yavuz, “Harmonic univalent functions with Janowski starlike analytic part,” *RIMS Kôkyûroku* 1626 (2009), 127–134. https://openaccess.iku.edu.tr/entities/publication/8c18390e-307d-40dc-9fc3-29365e174a3a
