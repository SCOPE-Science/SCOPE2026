# Quartic stabilization of the rectangle obstruction at the dual Brunn–Minkowski endpoint

## Finding

Li, Wan, and Zhang study the dual quermassintegral
\[
\widetilde V_q(K)
=
\frac1n\int_{\mathbb S^{n-1}}\rho_K(u)^q\,du
=
\frac qn\int_K |x|^{q-n}\,dx
\]
and the Brunn--Minkowski inequality for \(\widetilde V_q\). Their symmetric counterexample mechanism is built from the planar rectangles
\[
R_t=[-1-t,1+t]\times[-1+t,1-t],
\qquad |t|<1,
\]
which satisfy
\[
\frac12R_t+\frac12R_{-t}=R_0.
\]

At the critical planar exponent \(Q=4\), this family has the exact profile
\[
\boxed{
\widetilde V_4(R_t)=\frac{16}{3}(1-t^4).
}
\]
Consequently the normalized endpoint Brunn--Minkowski deficit along this family is
\[
\boxed{
1-
\left(
\frac{\widetilde V_4(R_t)}
{\widetilde V_4(R_0)}
\right)^{1/4}
=
1-(1-t^4)^{1/4}
=
\frac14t^4+O(t^8).
}
\]

The second-variation formula in the source shows that \(t=0\) is quadratically stable for \(2<Q<4\) and quadratically unstable for \(Q>4\). Thus \(Q=4\) is not merely a point where the Hessian test becomes inconclusive: the quadratic term vanishes and the first nonzero deficit is strictly stabilizing and quartic.

This critical law lifts to every dimension through the same thin-box degeneration used in the source. For
\[
K_{t,\varepsilon}
=
R_t\times[-\varepsilon,\varepsilon]^{n-2},
\qquad
q=n+2,
\]
one has, for every fixed \(n\ge2\) and \(|t|<1\),
\[
\boxed{
\lim_{\varepsilon\downarrow0}
\left[
1-
\left(
\frac{\widetilde V_{n+2}(K_{t,\varepsilon})}
{\widetilde V_{n+2}(K_{0,\varepsilon})}
\right)^{1/(n+2)}
\right]
=
1-(1-t^4)^{1/(n+2)}.
}
\]
In particular, as \(t\to0\), the limiting normalized deficit is
\[
\frac{t^4}{n+2}+O(t^8).
\]

## Assumptions and scope

The parameter satisfies \(|t|<1\), so every \(R_t\) is an origin-symmetric rectangle with nonempty interior. For \(n>2\), \(\varepsilon>0\), and
\[
K_{t,\varepsilon}
=
R_t\times[-\varepsilon,\varepsilon]^{n-2},
\]
the bodies are origin-symmetric convex bodies containing the origin in their interiors.

The statement concerns the canonical rectangle and thin-box family used in the source's proof of failure above the symmetric threshold. It does not assert a universal quantitative stability estimate for all origin-symmetric convex bodies at \(q=n+2\).

For \(2<Q<4\) and \(Q>4\), only the local sign near \(t=0\) is claimed. At \(Q=4\), the formula is exact for every \(|t|<1\).

## Proof

In dimension two, the polar-coordinate identity from the source gives
\[
\widetilde V_4(R_t)
=
2\int_{R_t}(x^2+y^2)\,dx\,dy.
\]
Write
\[
a=1+t,\qquad b=1-t.
\]
Then
\[
\int_{R_t}(x^2+y^2)\,dx\,dy
=
\frac{4}{3}ab(a^2+b^2).
\]
Since
\[
ab=1-t^2
\]
and
\[
a^2+b^2=2(1+t^2),
\]
we obtain
\[
\int_{R_t}(x^2+y^2)\,dx\,dy
=
\frac83(1-t^4),
\]
and hence
\[
\widetilde V_4(R_t)
=
\frac{16}{3}(1-t^4).
\]

Because \(R_{-t}\) is a rotation of \(R_t\),
\[
\widetilde V_4(R_{-t})=\widetilde V_4(R_t).
\]
Moreover,
\[
\frac12R_t+\frac12R_{-t}=R_0.
\]
Therefore the endpoint inequality along this pair reduces exactly to
\[
\widetilde V_4(R_0)^{1/4}
\ge
\widetilde V_4(R_t)^{1/4},
\]
and the normalized difference is
\[
1-(1-t^4)^{1/4}.
\]
The binomial expansion gives
\[
1-(1-t^4)^{1/4}
=
\frac14t^4+O(t^8).
\]

For the neighboring exponents, the source defines
\[
P(Q)
=
(Q-2)
\frac{
\int_0^1(1-s^2)(1+s^2)^{(Q-4)/2}\,ds
}{
\int_0^1(1+s^2)^{(Q-2)/2}\,ds
}
\]
and proves
\[
P(2)=0,\qquad P(4)=1,
\]
with strict increase on \([2,4]\). Its rectangle second-variation formula at Minkowski addition, corresponding to \(p=1\), is
\[
F''_{1,Q}(0)
=
4Q\bigl(P(Q)-1\bigr)
\int_0^1(1+s^2)^{(Q-2)/2}\,ds.
\]
Hence
\[
F''_{1,Q}(0)<0
\qquad(2<Q<4).
\]
For \(Q>4\), Lemma 4.1 of the source proves the opposite sign. Thus the rectangle changes from quadratic stability to quadratic instability at \(Q=4\), while the exact calculation above resolves the degenerate endpoint with a quartic stabilizing term.

Finally, the source's dimension-reduction formula states that, with
\[
Q=q-n+2,
\]
\[
\widetilde V_q(K_{t,\varepsilon})
=
\frac{2^q}{nQ}
(2\varepsilon)^{n-2}
\widetilde V_Q(R_t)
+
o(\varepsilon^{n-2})
\]
as \(\varepsilon\downarrow0\), uniformly for \(t\) near zero. At the symmetric endpoint
\[
q=n+2,
\]
one has \(Q=4\). Dividing the formula for \(t\) by the formula for \(0\) yields
\[
\frac{\widetilde V_{n+2}(K_{t,\varepsilon})}
{\widetilde V_{n+2}(K_{0,\varepsilon})}
\longrightarrow
\frac{\widetilde V_4(R_t)}
{\widetilde V_4(R_0)}
=
1-t^4.
\]
Taking the positive \((n+2)\)-nd root proves the all-dimensional thin-box limit.

## Verification

The bundled checker uses exact rational polynomial arithmetic to reconstruct
\[
\int_{R_t}(x^2+y^2)\,dx\,dy
=
\frac83(1-t^4)
\]
from the side lengths \(1+t\) and \(1-t\). It verifies the exact ratio
\[
\frac{\widetilde V_4(R_t)}{\widetilde V_4(R_0)}
=
1-t^4
\]
and symbolically checks the first nonzero Taylor coefficient of the normalized root deficit.

The source's full text was inspected at the definitions of \(\widetilde V_q\), Lemma 4.1, the dimension-reduction formula, the function \(P(Q)\), Proposition 4.3, and Theorem 1.5. The finite checker is supplementary; the proof above is exact and all-dimensional where claimed.

## Relationship to prior work

Li, Wan, and Zhang prove that the dual Brunn--Minkowski inequality fails for origin-symmetric bodies when
\[
q>n+2
\]
and holds at
\[
q=n+2.
\]
Their failure proof uses precisely the rectangle family \(R_t\) and a second-variation argument. They record that the relevant second derivative changes sign at the reduced exponent \(Q=4\), but do not evaluate the critical rectangle profile or identify its first nonzero stabilizing order.

The present calculation supplies that missing endpoint geometry: the canonical obstruction is exactly quartically stable at the threshold, and the source's own thin-box reduction transports the corresponding normalized quartic law to every dimension.

Targeted searches by the source identifier, the rectangle family, the endpoint \(q=n+2\), and the phrases “quartic deficit” and “quartic stability” found no prior statement of this profile.

## Limitations

The result is a complete critical-order description of the source's rectangle mechanism, not a global stability theorem for arbitrary origin-symmetric bodies.

For \(n>2\), the displayed formula is an \(\varepsilon\downarrow0\) limit along the source's thin-box family. No claim is made that the same exact finite-\(\varepsilon\) profile holds before degeneration.

The main residual bibliographic risk is that the elementary endpoint rectangle integral may have been observed informally without being indexed or stated in the literature.

## References

1. Haizhong Li, Yao Wan, Yijia Zhang, *On the Brunn--Minkowski inequality for \(q\)-th dual quermassintegrals with \(q>n\)*, arXiv:2608.03949v1, 4 August 2026.
2. H. Hadwiger, *Vorlesungen über Inhalt, Oberfläche und Isoperimetrie*, Springer, 1957.
