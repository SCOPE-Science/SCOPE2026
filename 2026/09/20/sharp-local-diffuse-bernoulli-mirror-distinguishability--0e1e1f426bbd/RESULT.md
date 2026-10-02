# Diffuse finite-signal efficiency for Bernoulli mirror products

## Statement

For each \(n\), let \(a^{(n)}=(a_{n,1},\ldots,a_{n,m_n})\) with
\(0\le a_{n,i}<1\), and define the mirror product measures on
\(\{-1,+1\}^{m_n}\) by
\[
R_{a^{(n)}}^\pm(x)
=
2^{-m_n}\prod_i(1\pm a_{n,i}x_i).
\]
Put
\[
\tau_n=d_{\rm TV}(R_{a^{(n)}}^+,R_{a^{(n)}}^-),
\qquad
\Delta_n=
\sqrt{1-\prod_i(1-a_{n,i}^2)}.
\]

Assume the diffuse finite-signal regime
\[
\eta_n:=\max_i a_{n,i}\longrightarrow0,
\qquad
\sum_i a_{n,i}^2\longrightarrow v\in(0,\infty).
\]

Then
\[
\boxed{
\tau_n\longrightarrow 2\Phi(\sqrt v)-1,
\qquad
\Delta_n\longrightarrow\sqrt{1-e^{-v}}.
}
\]
Consequently
\[
\boxed{
\frac{\tau_n}{\Delta_n}
\longrightarrow
\mathcal R(v)
:=
\frac{2\Phi(\sqrt v)-1}{\sqrt{1-e^{-v}}}.
}
\]

The function \(\mathcal R\) is strictly increasing on \((0,\infty)\), with
\[
\boxed{
\mathcal R(0+)=\sqrt{\frac2\pi},
\qquad
\mathcal R(\infty)=1.
}
\]

Thus, in the diffuse regime, the computational-basis distinguishability has
an exact finite-signal efficiency profile: it starts at the Gaussian
weak-signal constant and increases continuously to one as aggregate signal
strength grows.

For the homogeneous specialization \(a_{n,i}=t/\sqrt{m_n}\) with
\(m_n\to\infty\), one has \(v=t^2\), hence
\[
\frac{\tau_n}{\Delta_n}\longrightarrow
\frac{2\Phi(t)-1}{\sqrt{1-e^{-t^2}}}.
\]

## Proof

Set
\[
\theta_{n,i}=\operatorname{atanh}(a_{n,i}).
\]
Under \(R_{a^{(n)}}^+\), the coordinate signs are independent and satisfy
\[
\mathbb E_+ X_i=a_{n,i}.
\]
Half of the log-likelihood ratio between the two mirror laws is
\[
S_n=\sum_i\theta_{n,i}X_i.
\]

Reflection \(x\mapsto-x\) interchanges the two laws. Therefore the
likelihood-ratio test has threshold zero and
\[
\tau_n
=
\Pr_+(S_n>0)-\Pr_+(S_n<0).
\]

Since \(\eta_n\to0\),
\[
\mathbb E_+S_n
=
\sum_i a_{n,i}\operatorname{atanh}(a_{n,i})
=
v+o(1),
\]
and
\[
\operatorname{Var}_+(S_n)
=
\sum_i(1-a_{n,i}^2)\operatorname{atanh}(a_{n,i})^2
=
v+o(1).
\]
The largest centered summand tends to zero, so the Lindeberg condition
holds and
\[
S_n\Rightarrow N(v,v).
\]
The limiting Gaussian has no atom at zero, giving
\[
\tau_n\longrightarrow 2\Phi(\sqrt v)-1.
\]

Also,
\[
\log\prod_i(1-a_{n,i}^2)
=
-\sum_i a_{n,i}^2
+
O\!\left(\eta_n^2\sum_i a_{n,i}^2\right)
\longrightarrow -v.
\]
Hence
\[
\Delta_n\longrightarrow\sqrt{1-e^{-v}},
\]
which proves the profile.

For strict monotonicity, write \(t=\sqrt v\) and
\[
I(t)=\int_0^t e^{-u^2/2}\,du.
\]
Up to the positive constant \(\sqrt{2/\pi}\),
\[
\mathcal R(t^2)=\frac{I(t)}{\sqrt{1-e^{-t^2}}}.
\]
Its logarithmic derivative is positive exactly when
\[
2\sinh(t^2/2)>tI(t).
\]
For every \(t>0\),
\[
2\sinh(t^2/2)>t^2
\qquad\text{and}\qquad
I(t)<t,
\]
so the inequality is strict. The endpoint limits follow from the standard
Gaussian expansions at zero and infinity.

## Prior work and scope

The mirror-product reduction and its constant-factor comparison are due to
Smirnov. An earlier result on these same mirror products established the
uniform weak-signal profile, the full local efficiency interval
\([1/\sqrt2,1]\), and the diffuse weak-signal limit \(\sqrt{2/\pi}\).
Those local statements are prior work and are not claimed here.

The claim here is only the fixed-positive-signal diffuse limit
\(\sum_i a_{n,i}^2\to v\in(0,\infty)\), its closed efficiency curve
\(\mathcal R(v)\), and strict monotonicity of that curve. The proof uses a
standard triangular-array central limit argument for the exact
log-likelihood ratio.

## Limitations

- Diffuseness \(\max_i a_{n,i}\to0\) is required.
- No quantitative convergence rate is proved.
- The weak-signal profile and its sharp interval are prior work.
- The globally optimal constant for arbitrary finite mirror products is not
  determined here.
- Originality is asserted only to the best of our knowledge; an equivalent
  fixed-signal formulation may exist in older binary-experiment literature.

## References

1. G. Smirnov, *TV between Bernoulli products, up to constants*,
   arXiv:2609.19222 (2026).
2. A. Avital, A. Kontorovich, G. Salafatinos,
   *TV over Bernoulli products: the small parameter regime*,
   arXiv:2602.21828 (2026).
3. A. W. van der Vaart, *Asymptotic Statistics*, Chapter 7,
   Cambridge University Press (1998).
