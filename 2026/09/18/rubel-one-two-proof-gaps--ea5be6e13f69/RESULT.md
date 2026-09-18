# A curvature obstruction and implication gap in the Rubel(1)=Rubel(2) proof

## Statement

Cameron MacMahon's arXiv:2609.20607v1 states, as Theorem 1.4, that
\[
\operatorname{Rubel}(1)=\operatorname{Rubel}(2)
\]
for arbitrary plane domains, and derives the simply connected finite-inner-diameter characterization of \(\operatorname{Rubel}_0(2)\) as Corollary 1.5.

The proof given in v1 does not establish these conclusions. There are two logically independent gaps.

1. **The finite-inner-diameter implication is used in the wrong direction.**  
   The proof begins with \(\Omega\in\operatorname{Rubel}(1)\) and then asserts that \(\Omega\) has finite diameter in the interior path metric, including when \(\Omega\) is multiply connected. Theorem 1.1 of the same paper proves the relevant equivalence only for simply connected domains. The elementary path-integral direction valid on arbitrary domains is
   \[
   \operatorname{diam}_{d_\Omega}\Omega<\infty
   \quad\Longrightarrow\quad
   \Omega\in\operatorname{Rubel}(1),
   \]
   not the converse used in the proof.

2. **Second arc-length derivatives do not control the analytic second derivative on a curved path.**  
   If \(u=\operatorname{Re}f\) and \(\gamma\) is parametrized by arc length \(s\), then
   \[
   \frac{d^2}{ds^2}u(\gamma(s))
   =
   \operatorname{Re}\!\left(
      f''(\gamma(s))\,\gamma'(s)^2
      +f'(\gamma(s))\,\gamma''(s)
   \right).
   \]
   Thus Theorem 5.1, which produces large first and second derivatives of the restriction \(u|_\Gamma\), does not by itself produce large \(|f''|\). The curvature term \(f'\gamma''\) is not controlled in the proof.

Consequently, the argument in arXiv:2609.20607v1 does not prove Theorem 1.4 or Corollary 1.5 as written. This is a proof-gap result, not a counterexample to either statement.

## Definitions

For a plane domain \(\Omega\), let \(d_\Omega\) be the interior path metric:
\[
d_\Omega(p,q)
=
\inf_\gamma \ell(\gamma),
\]
where the infimum is over rectifiable curves in \(\Omega\) joining \(p\) to \(q\).

Following arXiv:2609.20607v1, \(\Omega\in\operatorname{Rubel}(k)\) means that every unbounded analytic \(f\) on \(\Omega\) admits a sequence \(z_n\in\Omega\) such that
\[
|f(z_n)|,\ |f'(z_n)|,\ldots,|f^{(k)}(z_n)|\to\infty.
\]

## 1. The implication available from finite inner diameter

The following elementary lemma is useful for separating the valid direction from the direction used in the proof.

### Lemma
For every plane domain \(\Omega\),
\[
\operatorname{diam}_{d_\Omega}\Omega<\infty
\quad\Longrightarrow\quad
\Omega\in\operatorname{Rubel}(1).
\]

### Proof
Write \(D=\operatorname{diam}_{d_\Omega}\Omega<\infty\), and let \(f\) be unbounded and analytic on \(\Omega\).

If the desired conclusion failed, then
\[
\min\{|f(z)|,|f'(z)|\}\le M
\]
for every \(z\in\Omega\), for some finite \(M\).

Fix \(p\in\Omega\), choose
\[
R>\max\{M,|f(p)|\},
\]
and then choose \(q\in\Omega\) with
\[
|f(q)|>R+M(D+1).
\]
Take a rectifiable path \(\gamma\subset\Omega\) from \(p\) to \(q\) of length \(<D+1\). By continuity there is a last point \(z_0\) on \(\gamma\) at which \(|f(z_0)|=R\). On the remaining subarc from \(z_0\) to \(q\),
\[
|f|>R>M,
\]
so the assumed pointwise alternative forces \(|f'|\le M\). Hence
\[
|f(q)|
\le |f(z_0)|+\int_{\gamma[z_0,q]}|f'(z)|\,|dz|
< R+M(D+1),
\]
a contradiction. Therefore \(\min\{|f|,|f'|\}\) is unbounded, which is precisely the \(\operatorname{Rubel}(1)\) conclusion. \(\square\)

MacMahon's Theorem 1.1 supplies the reverse implication in the simply connected setting by constructing an unbounded analytic function with bounded derivative whenever the inner diameter is infinite. That construction is where simple connectivity enters. No corresponding arbitrary-domain reverse implication is proved before Theorem 1.4.

## 2. An explicit curvature obstruction

The second issue can be isolated independently of domain topology.

Let
\[
f(z)=z^2,\qquad
\gamma(t)=t+i\sin t,\qquad t\ge0,
\]
and put
\[
u(t)=\operatorname{Re}f(\gamma(t))
=t^2-\sin^2 t.
\]
The curve \(\gamma\) is a smooth Jordan ray. Let \(s\) denote its arc-length parameter and
\[
v(t)=|\gamma'(t)|=\sqrt{1+\cos^2 t}.
\]
Then
\[
\frac{d}{ds}=\frac1{v(t)}\frac{d}{dt}.
\]

At
\[
t_n=2\pi n+\frac{\pi}{4}
\]
one has \(v(t_n)^2=3/2\), and direct differentiation gives
\[
u(t_n)=t_n^2-\frac12,
\]
\[
\frac{du}{ds}(t_n)
=
\sqrt{\frac23}\,(2t_n-1),
\]
and
\[
\frac{d^2u}{ds^2}(t_n)
=
\frac{4t_n+10}{9}.
\]
All three quantities tend to \(+\infty\), while
\[
|f''(\gamma(t_n))|=2
\]
for every \(n\).

Thus even on a smooth Jordan ray with bounded curvature, simultaneous divergence of
\[
|u|,\quad \left|\frac{du}{ds}\right|,\quad
\left|\frac{d^2u}{ds^2}\right|
\]
does not imply divergence of \(|f''|\).

The exact chain rule explains the phenomenon:
\[
u_{ss}
=
\operatorname{Re}\bigl(f''(\gamma)\gamma_s^2\bigr)
+
\operatorname{Re}\bigl(f'(\gamma)\gamma_{ss}\bigr).
\]
Only the first term is controlled by \(|f''|\); the second is curvature times \(f'\). The conformality of the complex derivative justifies
\[
|u_s|\le |f'|,
\]
but there is no analogous second-order conclusion without controlling the curvature term.

## 3. Consequence for the published proof

In Section 5 of arXiv:2609.20607v1, Theorem 5.1 is a one-dimensional statement about derivatives of a real-valued function along a smooth Jordan ray. In the proof of Theorem 1.4, it is applied to the real or imaginary part of an analytic function restricted to a smoothed concatenation of short paths. The final step then passes from large first and second derivatives along that path to large \(|f'|\) and \(|f''|\).

The first-order passage is valid. The second-order passage is not supplied by conformality and is contradicted as a general inference by the example above. Smoothing corners also does not remove the issue: smoothing introduces curvature, and the proof contains no estimate that makes the term \(f'\gamma_{ss}\) negligible.

Independently, the same proof assumes finite inner diameter from membership in \(\operatorname{Rubel}(1)\) on an arbitrary domain. The available arbitrary-domain elementary argument goes in the opposite direction, while the paper's reverse implication relies on its simply connected Theorem 1.1.

Accordingly, neither the all-domain equality in Theorem 1.4 nor the simply connected Corollary 1.5 is established by the argument presented in v1. The statements may still be true and may admit a different proof.

## Limitations

- No counterexample to \(\operatorname{Rubel}(1)=\operatorname{Rubel}(2)\) is produced.
- No counterexample to the simply connected finite-inner-diameter characterization of \(\operatorname{Rubel}_0(2)\) is produced.
- The lemma “finite inner diameter implies \(\operatorname{Rubel}(1)\)” is elementary and is not claimed as a new theorem.
- The record concerns arXiv:2609.20607v1, submitted 17 September 2026. A later revision may repair the argument.
- The older Gordon and Hinchliffe literature establishes strong-unboundedness results in special geometric settings; this record does not claim a new theorem about those settings.

## References

1. C. MacMahon, *On Simply Connected Domains Supporting an Unbounded Analytic Function with Bounded Derivative*, arXiv:2609.20607v1, 2026.  
   https://arxiv.org/abs/2609.20607

2. A. Y. Gordon, *Strong unboundedness of unbounded analytic functions*, Proc. Amer. Math. Soc. 122 (1994), 525–529.

3. J. D. Hinchliffe, *Unbounded analytic functions on plane domains*, Mathematika 50 (2003), 207–214.  
   https://doi.org/10.1112/S002557930001490X
