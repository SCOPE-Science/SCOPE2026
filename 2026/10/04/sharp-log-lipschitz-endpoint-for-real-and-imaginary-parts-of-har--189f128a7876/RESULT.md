# Sharp log-Lipschitz endpoint for real and imaginary parts of harmonic quasiregular maps

## Finding

Let \(f=u+iv\) be a harmonic \(K\)-quasiregular mapping of the unit disk \(\mathbb D\). Assume that \(u\) extends continuously to \(\overline{\mathbb D}\) and that its boundary trace is Lipschitz:
\[
|u(e^{i\theta})-u(e^{i\phi})|
\le
L\,d_{\mathbb T}(\theta,\phi),
\]
where \(d_{\mathbb T}\) is the shortest angular distance on the circle.

Then \(v\) extends continuously to \(\overline{\mathbb D}\), and there is a constant \(C_K\), depending only on \(K\), such that
\[
|v(e^{i\theta})-v(e^{i\phi})|
\le
C_KL\,\delta\log\frac e\delta,
\qquad
\delta=d_{\mathbb T}(\theta,\phi),
\]
for \(0<\delta\le1/2\).

This logarithmic loss is sharp in order even in the analytic case \(K=1\). For the example with
\[
u(e^{i\theta})=|\theta|,
\qquad -\pi\le\theta\le\pi,
\]
the harmonic conjugate satisfies
\[
v(e^{i\theta})
=
-\frac{2}{\pi}\theta\log\frac1\theta
+
O(\theta)
\qquad(\theta\downarrow0),
\]
so
\[
\lim_{\theta\downarrow0}
\frac{|v(e^{i\theta})-v(1)|}
{\theta\log(1/\theta)}
=
\frac2\pi.
\]

Thus the endpoint replacement for the strict Hölder theorem is precisely log-Lipschitz regularity in order.

## Assumptions and scope

Write the harmonic map in its canonical form
\[
f=h+\overline g,
\]
with analytic \(h,g\). Its complex dilatation satisfies
\[
|g'|\le k|h'|,
\qquad
k=\frac{K-1}{K+1}.
\]
Set
\[
F=h+g.
\]
Then
\[
\operatorname{Re}F=u.
\]

The theorem assumes only boundary Lipschitz regularity of \(u\), not of the full boundary map \(f\) and not of \(|f|\). The conclusion is a first-order modulus of continuity for \(v\); it does not claim that \(v\) belongs to the Lipschitz class or that its derivative remains bounded at the boundary.

## Proof

The recent source proves the strict Hölder result by estimating \(F'\) from the boundary oscillation of \(u\). Its exact estimate is
\[
|F'(re^{i\theta})|
\le
\frac1\pi
\int_0^{2\pi}
\frac{
|u(e^{i(\theta+t)})-u(e^{i\theta})|
}{
1-2r\cos t+r^2
}\,dt.
\]
At the endpoint, the Lipschitz hypothesis gives
\[
|F'(re^{i\theta})|
\le
\frac{2L}{\pi}
\int_0^\pi
\frac{t}{
(1-r)^2+4r\sin^2(t/2)
}\,dt.
\]

For \(r\ge1/2\), use
\[
\sin(t/2)\ge \frac t\pi
\qquad(0\le t\le\pi).
\]
Hence
\[
|F'(re^{i\theta})|
\le
C L
\int_0^\pi
\frac{t}{
(1-r)^2+(2/\pi^2)t^2
}\,dt
\le
C L\log\frac e{1-r},
\]
with a universal constant \(C\). For \(r<1/2\), the denominator in the original integral is bounded below by \((1-r)^2\ge1/4\), so the same estimate, after enlarging \(C\), remains valid. Therefore
\[
|F'(re^{i\theta})|
\le
C L\log\frac e{1-r}
\qquad(0\le r<1).
\]

Quasiregularity gives the inequalities used in the source,
\[
|h'|
\le
\frac1{1-k}|F'|,
\qquad
|g'|
\le
\frac{k}{1-k}|F'|.
\]
Consequently
\[
|h'|+|g'|
\le
K|F'|
\le
CKL\log\frac e{1-r}.
\]

Because
\[
\int_0^1\log\frac e{1-r}\,dr<\infty,
\]
the radial limits of \(h\) and \(g\) exist uniformly in the angle; hence both extend continuously to the closed disk.

Let
\[
\delta=d_{\mathbb T}(\theta,\phi)\le\frac12
\]
and put
\[
r=1-\delta.
\]
Join \(e^{i\theta}\) to \(e^{i\phi}\) by two radial segments down to radius \(r\) and the circular arc between \(re^{i\theta}\) and \(re^{i\phi}\). The two radial pieces contribute at most
\[
2CKL
\int_{1-\delta}^{1}
\log\frac e{1-s}\,ds
\le
C_1KL\,\delta\log\frac e\delta,
\]
and the circular piece contributes at most
\[
CKL\,\delta\log\frac e\delta.
\]
Therefore both \(h\) and \(g\), and hence
\[
v=\operatorname{Im}h-\operatorname{Im}g,
\]
obey the stated log-Lipschitz modulus.

For sharpness, take the analytic example from the source with
\[
u(e^{i\theta})=|\theta|.
\]
Its cosine series is
\[
|\theta|
=
\frac\pi2
-
\frac4\pi
\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\frac{\cos(m\theta)}{m^2}.
\]
Choosing the analytic function with this real part and with \(v(1)=0\), its conjugate boundary function is
\[
v(e^{i\theta})
=
-\frac4\pi
\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\frac{\sin(m\theta)}{m^2}.
\]
For \(0<\theta<\pi\),
\[
\frac d{d\theta}v(e^{i\theta})
=
-\frac4\pi
\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\frac{\cos(m\theta)}m
=
-\frac2\pi
\log\cot\frac\theta2.
\]
Since
\[
\log\cot\frac\theta2
=
\log\frac2\theta+O(\theta^2),
\]
integration from \(0\) to \(\theta\) yields
\[
v(e^{i\theta})
=
-\frac2\pi\theta\log\frac1\theta
+
O(\theta).
\]
The coefficient \(2/\pi\) proves sharpness in order and rules out any universal \(o(\delta\log(1/\delta))\) replacement.

## Verification

The proof was checked directly against the exact derivative formula and quasiregular derivative comparison in the primary source. The endpoint integral is elementary:
\[
\int_0^\pi
\frac{t}{a^2+bt^2}\,dt
=
\frac1{2b}
\log\left(1+\frac{b\pi^2}{a^2}\right),
\]
so the logarithmic derivative growth is not inferred from numerical sampling.

The path estimate uses the integrability of the logarithmic derivative:
\[
\int_0^\delta\log\frac et\,dt
=
\delta\log\frac e\delta+\delta.
\]
The sharp example was independently reconstructed from the classical Fourier series of \(|\theta|\); differentiating its conjugate series gives the exact odd-harmonic identity
\[
\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\frac{\cos(m\theta)}m
=
\frac12\log\cot\frac\theta2.
\]

No finite experiment is used to justify the infinite-dimensional statement.

## Relationship to prior work

Das and Rasila prove that for a harmonic \(K\)-quasiregular map, Hölder regularity of the real boundary trace with exponent \(0<\alpha<1\) forces the same exponent for the imaginary boundary trace. Their proof stops at \(\alpha<1\) because the relevant derivative integral ceases to converge uniformly at the endpoint. They explicitly note that the Lipschitz conclusion is false at \(\alpha=1\) and exhibit the example \(u(e^{i\theta})=|\theta|\), for which the conjugate behaves logarithmically. The present result identifies the optimal replacement modulus at that excluded endpoint and gives the sharp leading coefficient for their example.

The paper by Das, Huang, and Rasila called “Zygmund's theorem” concerns the classical integrability theorem for conjugate functions: an \(\mathbf h\log^+\mathbf h\) condition on the real part implying \(h^1\) control. It does not concern the boundary Zygmund class or the log-Lipschitz modulus proved here.

Earlier quasiregular Lipschitz-type results of Mateljević and collaborators concern regularity inherited by a quasiregular map from its modulus, or regularity of a harmonic extension from the full prescribed boundary map. Those hypotheses already control the whole map and do not derive imaginary-part endpoint regularity from the real part alone.

## Limitations

The result is an endpoint upper modulus, not an exact best multiplicative constant for all \(K\). The dependence is controlled by a constant depending only on \(K\), and the proof gives linear dependence on \(K\) up to a universal numerical factor.

The sharp coefficient \(2/\pi\) is proved for the analytic model \(u(e^{i\theta})=|\theta|\); it is not asserted to be the optimal universal constant for all harmonic quasiregular maps.

The theorem is stated on the unit disk and for angular boundary distance. No claim is made here for arbitrary planar domains without tracking conformal boundary distortion.

## References

1. S. Das and A. Rasila, *Note on real and imaginary parts of harmonic quasiregular mappings*, arXiv:2506.04618v1; Canadian Mathematical Bulletin 69 (2026), 405--413.
2. S. Das, J. Huang, and A. Rasila, *Zygmund's theorem for harmonic quasiregular mappings*, Complex Analysis and Operator Theory 19 (2025), Article 91.
3. M. Mateljević, *Distortion of quasiregular mappings and equivalent norms on Lipschitz-type spaces*, Abstract and Applied Analysis 2014 (2014), Article 895074.
4. A. Abaob, M. Arsenović, M. Mateljević, and A. Shkheam, *Moduli of continuity of harmonic quasiregular mappings on bounded domains*, Annales Academiae Scientiarum Fennicae Mathematica 38 (2013), 839--847.
