# Sharp local and diffuse distinguishability for Bernoulli mirror products

## Statement

For `m >= 1` and `a=(a_1,...,a_m)` with `0 <= a_i < 1`, define the mirror Bernoulli products on `{-1,+1}^m` by

\[
R_a^\pm(x)=2^{-m}\prod_{i=1}^m(1\pm a_i x_i).
\]

Write

\[
\tau(a)=d_{\mathrm{TV}}(R_a^+,R_a^-),\qquad
\Delta(a)=\sqrt{1-\prod_{i=1}^m(1-a_i^2)},\qquad
v=\sum_{i=1}^m a_i^2.
\]

Here `Delta(a)` is exactly the pure-state distinguishability upper quantity appearing in Smirnov's mirror-product reduction [1, Eq. (3.3), Theorem 4.1].

The following sharpenings hold.

### Theorem 1: uniform local expansion and sharp local efficiency range

For `v -> 0`, uniformly over the dimension and over all vectors `a` with `sum a_i^2=v`, let

\[
w_i=\frac{a_i}{\sqrt v},\qquad \sum_iw_i^2=1,
\]

and let `eps_i` be independent Rademacher variables. Then

\[
\boxed{
\frac{\tau(a)}{\Delta(a)}
=
\mathbb E\left|\sum_iw_i\varepsilon_i\right|+O(v).
}
\]

Consequently, by the sharp `p=1` Khintchine inequality,

\[
\boxed{
\lim_{v\downarrow0}\inf_{\sum a_i^2=v}\frac{\tau(a)}{\Delta(a)}=\frac1{\sqrt2},
\qquad
\lim_{v\downarrow0}\sup_{\sum a_i^2=v}\frac{\tau(a)}{\Delta(a)}=1.
}
\]

Every constant in `[1/sqrt(2),1]` is attained as a local subsequential efficiency. In particular, Smirnov's unspecified absolute constant in the mirror-product lower bound cannot exceed `1/sqrt(2)`, and `1/sqrt(2)` is the sharp lower constant to first order in the weak-signal regime.

Two exact endpoint witnesses are useful. With a single nonzero coordinate, `tau=Delta=a_1`. With two equal coordinates `a_1=a_2=e`,

\[
\tau=e,\qquad \Delta=e\sqrt{2-e^2},
\]

so `tau/Delta -> 1/sqrt(2)`.

### Theorem 2: diffuse local universality

Define the fourth-order participation ratio

\[
r_4(a)=\frac{(\sum_i a_i^2)^2}{\sum_i a_i^4}.
\]

If `v -> 0` and `r_4(a) -> infinity`, then

\[
\boxed{
\frac{\tau(a)}{\Delta(a)}\longrightarrow\sqrt{\frac2\pi}.
}
\]

Thus the least-efficient local configurations are concentrated on two equal coordinates, while diffuse weak signals have the strictly larger universal efficiency `sqrt(2/pi)`.

### Theorem 3: finite-signal diffuse efficiency curve

Consider a triangular array `a^(n)` such that

\[
\eta_n:=\max_i a_{n,i}\to0,
\qquad
\sum_i a_{n,i}^2\to v\in(0,\infty).
\]

Then

\[
\boxed{
\tau(a^{(n)})\longrightarrow 2\Phi(\sqrt v)-1,
\qquad
\Delta(a^{(n)})\longrightarrow\sqrt{1-e^{-v}},
}
\]

and hence

\[
\boxed{
\frac{\tau(a^{(n)})}{\Delta(a^{(n)})}
\longrightarrow
\mathcal R(v):=
\frac{2\Phi(\sqrt v)-1}{\sqrt{1-e^{-v}}}.
}
\]

The function `R(v)` is strictly increasing on `(0,infinity)` and

\[
\boxed{
\mathcal R(0+)=\sqrt{\frac2\pi},
\qquad
\mathcal R(\infty)=1.
}
\]

Thus computational-basis distinguishability interpolates continuously from the Gaussian local efficiency `sqrt(2/pi)` to asymptotically perfect efficiency as the diffuse aggregate signal grows.

For the homogeneous specialization `a_i=t/sqrt(m)`, if `K` is binomial with parameters

\[
m,\qquad p_m=\frac{1+t/\sqrt m}{2},
\]

then exactly

\[
\tau_{m,t}=\Pr(K>m/2)-\Pr(K<m/2),
\qquad
\Delta_{m,t}=\sqrt{1-(1-t^2/m)^m},
\]

and therefore

\[
\frac{\tau_{m,t}}{\Delta_{m,t}}\to \mathcal R(t^2).
\]

## Proof

### 1. Walsh expansion

Under a uniform Rademacher vector `eps`,

\[
\tau(a)=\mathbb E|H_a(\varepsilon)|,
\]

where

\[
H_a(\varepsilon)
=\frac12\left\{\prod_i(1+a_i\varepsilon_i)-\prod_i(1-a_i\varepsilon_i)\right\}
=\sum_{|S|\ \mathrm{odd}}a_S\varepsilon_S.
\]

Let

\[
L_a=\sum_i a_i\varepsilon_i.
\]

Walsh orthogonality gives

\[
\mathbb E(H_a-L_a)^2
=
\sum_{\substack{|S|\ge3\\ |S|\ \mathrm{odd}}}\prod_{i\in S}a_i^2
\le
\sum_{k\ge3}\frac{v^k}{k!}
=e^v-1-v-\frac{v^2}{2}.
\]

Therefore

\[
\tau(a)
=
\sqrt v\,\mathbb E\left|\sum_iw_i\varepsilon_i\right|+O(v^{3/2})
\]

uniformly as `v -> 0`.

On the other hand,

\[
1-e^{-v}
\le
1-\prod_i(1-a_i^2)
\le v,
\]

so

\[
\Delta(a)=\sqrt v\{1+O(v)\}.
\]

Dividing proves Theorem 1. Haagerup's sharp Khintchine constants give

\[
\frac1{\sqrt2}\le \mathbb E\left|\sum_iw_i\varepsilon_i\right|\le1.
\]

For every `c in [1/sqrt(2),1]`, choose two normalized weights

\[
w=(c,\sqrt{1-c^2}).
\]

Because `c >= sqrt(1-c^2)`, a direct four-point average gives

\[
\mathbb E|c\varepsilon_1+\sqrt{1-c^2}\varepsilon_2|=c,
\]

which proves attainability of the whole interval.

If `r_4 -> infinity`, then `max_i |w_i| -> 0`; the Lindeberg central limit theorem gives

\[
\sum_iw_i\varepsilon_i\Rightarrow N(0,1).
\]

The second moments are identically one, hence the absolute values are uniformly integrable, and Theorem 2 follows.

### 2. Likelihood-ratio limit for diffuse finite signal

Set

\[
\theta_{n,i}=\operatorname{atanh}(a_{n,i}).
\]

Under `R^+`, the coordinate signs are independent with

\[
\mathbb E_+[\varepsilon_i]=a_{n,i}.
\]

Half of the log-likelihood ratio between `R^+` and `R^-` is

\[
S_n=\sum_i\theta_{n,i}\varepsilon_i.
\]

The likelihood-ratio test changes sign at zero, and reflection of all signs interchanges the two mirror laws. Hence exactly

\[
\tau(a^{(n)})
=
\Pr_+(S_n>0)-\Pr_+(S_n<0).
\]

As `eta_n -> 0`, Taylor expansion gives

\[
\mu_n:=\mathbb E_+S_n
=
\sum_i a_{n,i}\operatorname{atanh}(a_{n,i})
=v+o(1),
\]

and

\[
\sigma_n^2:=\operatorname{Var}_+(S_n)
=
\sum_i(1-a_{n,i}^2)\operatorname{atanh}(a_{n,i})^2
=v+o(1).
\]

The maximal centered summand tends to zero, so Lindeberg's theorem yields

\[
S_n\Rightarrow N(v,v).
\]

Therefore

\[
\tau(a^{(n)})\to2\Phi(\sqrt v)-1.
\]

Also

\[
\log\prod_i(1-a_{n,i}^2)
=-\sum_i a_{n,i}^2+O\!\left(\eta_n^2\sum_i a_{n,i}^2\right)
\to-v,
\]

which proves the limit for `Delta` and the efficiency curve.

### 3. Monotonicity of the diffuse curve

Write `t=sqrt(v)` and

\[
I(t)=\int_0^t e^{-u^2/2}\,du.
\]

Up to the positive constant `sqrt(2/pi)`,

\[
\mathcal R(t^2)=\frac{I(t)}{\sqrt{1-e^{-t^2}}}.
\]

Its logarithmic derivative is positive exactly when

\[
2\sinh(t^2/2)>tI(t).
\]

For every `t>0`,

\[
2\sinh(t^2/2)>t^2
\quad\text{and}\quad
I(t)<t,
\]

so the inequality is strict. The endpoint limits follow from the elementary Gaussian expansions at zero and infinity.

## Relation to prior work and originality boundary

Smirnov [1] introduced the mirror-product reduction in this Bernoulli-product setting, identified `Delta` as the corresponding pure-state distinguishability, and proved that computational-basis total variation is bounded below by an unspecified absolute constant times `Delta`. The present result does not claim the mirror construction or a new constant-factor theorem.

The sharp `p=1` Khintchine constant `1/sqrt(2)` is classical [5]. Local asymptotic normality and Gaussian limits for likelihood-ratio experiments are classical [6]. Product-measure total variation and its tensorization/homogenization have also been studied recently [2--4]. These ingredients are prior art.

The claims made here, to the best of our knowledge, are the source-specific uniform local identity

\[
\tau/\Delta=\mathbb E|\sum_iw_i\varepsilon_i|+O(v),
\]

the resulting complete sharp local efficiency interval `[1/sqrt(2),1]`, and the explicit finite-signal diffuse efficiency curve `R(v)` together with its strict monotonicity. Searches for equivalent formulations in the Bernoulli-product, Rademacher/Riesz-product, likelihood-ratio, and quantum measurement literature did not locate these statements. Because the derivation combines classical Khintchine and LAN ideas with a very recent mirror-product construction, an unlocated equivalent formulation in older binary-experiment or Riesz-product literature remains a residual originality risk.

No global claim that `tau(a) >= Delta(a)/sqrt(2)` is made; only the sharp weak-signal lower constant is proved here.

## Limitations

- The finite-signal curve requires diffuseness: `max_i a_{n,i} -> 0`.
- The sharp interval theorem is local in `v=sum a_i^2`; it does not determine the globally optimal constant in Smirnov's Theorem 4.1.
- No rate is claimed for the finite-signal triangular-array convergence.
- The LAN mechanism and the sharp Khintchine inequality are classical and are not originality claims.
- Older binary statistical-experiment and Riesz-product literature was not exhaustively inspected.
- Cross-model review has not been performed.

## Reproducibility

`artifacts/verify_mirror_tv.py` exactly enumerates low-dimensional mirror total variation, computes homogeneous binomial total variation, and compares it with the displayed limiting curve. `artifacts/verification_output.txt` contains the corresponding deterministic numerical output.

## References

1. G. Smirnov, *TV between Bernoulli products, up to constants*, arXiv:2609.19222 (2026). https://arxiv.org/abs/2609.19222
2. A. Avital, A. Kontorovich, G. Salafatinos, *TV over Bernoulli products: the small parameter regime*, arXiv:2602.21828 (2026). https://arxiv.org/abs/2602.21828
3. A. Kontorovich, *A homogenization principle for total variation*, arXiv:2604.03882 (2026). https://arxiv.org/abs/2604.03882
4. A. Kontorovich, *On the tensorization of the variational distance*, Electronic Communications in Probability 30 (2025), article 32. https://doi.org/10.1214/25-ECP680
5. U. Haagerup, *The best constants in the Khintchine inequality*, Studia Mathematica 70 (1981), 231--283. https://doi.org/10.4064/sm-70-3-231-283
6. A. W. van der Vaart, *Asymptotic Statistics*, Chapter 7: Local Asymptotic Normality, Cambridge University Press (1998). https://doi.org/10.1017/CBO9780511802256.008
