# Sharp weak-signal profiles for mirror Bernoulli products

## Result

For a vector \(a=(a_1,\ldots,a_m)\in[0,1]^m\), define the mirror product laws on \(\{-1,1\}^m\)
\[
R_a^\pm(x)=2^{-m}\prod_{i=1}^m(1\pm a_i x_i),
\]
their total variation distance
\[
\tau(a)=d_{\rm TV}(R_a^+,R_a^-),
\]
and
\[
\Delta(a)=\sqrt{1-\prod_{i=1}^m(1-a_i^2)}.
\]
The quantity \(\Delta(a)\) is also the pure-state trace distance of the mirror product states whose computational-basis measurement gives \(R_a^\pm\).

Smirnov (2026) proved uniformly that \(\tau(a)\asymp\Delta(a)\). In the weak-signal regime one can identify the ratio sharply.

### Theorem 1: uniform first-order profile

Put
\[
q=\sum_{i=1}^m a_i^2,
\qquad
w_i=\frac{a_i}{\sqrt q}
\]
when \(q>0\), and let \(\varepsilon_i\) be independent Rademacher signs. If \(0<q\le 1/2\), then
\[
\boxed{
\left|
\frac{\tau(a)}{\Delta(a)}
-
\mathbb E\left|\sum_{i=1}^m w_i\varepsilon_i\right|
\right|
\le 2q.
}
\]
Hence, uniformly over the dimension and the shape of \(a\),
\[
\frac{\tau(a)}{\Delta(a)}
=
\mathbb E\left|\sum_i w_i\varepsilon_i\right|+O(q).
\]
Thus the weak-signal efficiency of computational-basis measurement is governed not by a single universal constant, but by the normalized Rademacher profile of the coordinate strengths.

### Theorem 2: complete subsequential profile law

Consider any sequence of finite vectors \(a^{(N)}\) such that
\[
q_N=\sum_i (a_i^{(N)})^2\longrightarrow0.
\]
Let \(w^{(N)}=a^{(N)}/\sqrt{q_N}\), reorder its entries nonincreasingly, and pad by zeros. Along every subsequence on which
\[
w_j^{(N)}\longrightarrow w_j\qquad(j=1,2,\ldots),
\]
write \(w=(w_j)\in\ell_2\) and
\[
\sigma^2=1-\|w\|_2^2.
\]
Then
\[
\boxed{
\frac{\tau(a^{(N)})}{\Delta(a^{(N)})}
\longrightarrow
\mathbb E\left|
\sum_{j\ge1}w_j\varepsilon_j+\sigma Z
\right|,
}
\]
where \(Z\sim N(0,1)\) is independent of the Rademacher sequence.

Conversely, every \(w\in\ell_2\) with \(\|w\|_2\le1\) occurs as such a weak-signal profile after adding a diffuse cloud of coordinates carrying the missing variance \(1-\|w\|_2^2\).

Consequently the set of all possible weak-signal subsequential limits is exactly
\[
\boxed{
\left[\frac1{\sqrt2},1\right].
}
\]
The endpoints and an important interior point have transparent realizations:

- two equal weak coordinates give \(1/\sqrt2\), so the lower endpoint is sharp;
- one dominant weak coordinate gives \(1\);
- if \(\max_i a_i/\sqrt q\to0\), the Lindeberg/diffuse regime gives
  \[
  \boxed{
  \frac{\tau(a)}{\Delta(a)}\to\sqrt{\frac2\pi}.
  }
  \]

For \(m\) equal weak coordinates the limiting efficiency is
\[
\kappa_m
=
\frac1{\sqrt m}\mathbb E\left|\sum_{i=1}^m\varepsilon_i\right|
=
\sqrt m\,\frac{\binom{m-1}{\lfloor(m-1)/2\rfloor}}{2^{m-1}},
\]
and \(\kappa_m\to\sqrt{2/\pi}\).

### Corollary: an exact diffuse asymptotic for Bernoulli products

Let
\[
P_N=\bigotimes_i\operatorname{Ber}(p_{Ni}),
\qquad
Q_N=\bigotimes_i\operatorname{Ber}(q_{Ni}),
\]
and use Smirnov's parameters
\[
\lambda_{Ni}=p_{Ni}(1-q_{Ni})+(1-p_{Ni})q_{Ni},
\qquad
a_{Ni}=\frac{|p_{Ni}-q_{Ni}|}{\lambda_{Ni}}
\]
(with \(a_{Ni}=0\) when \(\lambda_{Ni}=0\)). Define
\[
V_N=\sum_i\lambda_{Ni}a_{Ni}^2.
\]
If
\[
V_N\to0,
\qquad
\frac{\max_i a_{Ni}^2}{V_N}\to0,
\]
then
\[
\boxed{
d_{\rm TV}(P_N,Q_N)
\sim \sqrt{\frac{V_N}{\pi}}.
}
\]
Moreover, for Smirnov's doubled experiment,
\[
\boxed{
d_{\rm TV}(P_N\otimes Q_N,Q_N\otimes P_N)
\sim\sqrt{\frac{2V_N}{\pi}},
}
\]
so that the doubled/original ratio converges to \(\sqrt2\).

This corollary is a local-asymptotic-normality specialization; the new point here is the explicit identification in Smirnov's \((\lambda_i,a_i)\) coordinates and its compatibility with the mirror-product profile theorem above.

## Proof of Theorem 1

Let \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)\) be uniform on \(\{-1,1\}^m\). Define
\[
h_a(\varepsilon)
=
\frac12\left[
\prod_i(1+a_i\varepsilon_i)
-
\prod_i(1-a_i\varepsilon_i)
\right].
\]
Then, directly from the definition of total variation,
\[
\tau(a)=\mathbb E|h_a(\varepsilon)|.
\]
Expanding the two products cancels every even Walsh monomial and leaves
\[
h_a(\varepsilon)
=
\sum_{\substack{S\subseteq[m]\\ |S|\text{ odd}}}
a_S\varepsilon_S,
\qquad
a_S=\prod_{i\in S}a_i.
\]
Let
\[
L=\sum_i a_i\varepsilon_i.
\]
Walsh orthogonality gives the exact remainder variance
\[
\mathbb E(h_a-L)^2
=
\sum_{\substack{|S|\ge3\\ |S|\text{ odd}}}a_S^2.
\]
Writing \(u_i=a_i^2\) and \(q=\sum_i u_i\), the elementary symmetric sums obey
\[
e_k(u_1,\ldots,u_m)\le\frac{q^k}{k!},
\]
so
\[
\mathbb E(h_a-L)^2
\le
\sum_{k\ge3}\frac{q^k}{k!}
\le
\frac{q^3e^q}{6}.
\]
Therefore
\[
\left|\tau(a)-\mathbb E|L|\right|
\le
\mathbb E|h_a-L|
\le
\frac{q^{3/2}e^{q/2}}{\sqrt6}.
\]
Since \(\mathbb E|L|=\sqrt q\,\mathbb E|\sum_iw_i\varepsilon_i|\), it remains to normalize by \(\Delta(a)\).

The elementary inequalities \(1-x\le e^{-x}\) and \(1-e^{-q}\ge q-q^2/2\) give
\[
q\left(1-\frac q2\right)
\le
\Delta(a)^2
\le q.
\]
Let \(r=\Delta(a)/\sqrt q\). For \(q\le1/2\), \(r\ge\sqrt3/2\). Also, by Cauchy--Schwarz,
\[
\mathbb E\left|\sum_iw_i\varepsilon_i\right|\le1.
\]
Consequently
\[
\left|\frac{\tau}{\Delta}-\mathbb E\left|\sum_iw_i\varepsilon_i\right|\right|
\le
\left(\frac1r-1\right)
+
\frac{qe^{q/2}}{\sqrt6\,r}.
\]
Here \(1/r-1\le q/\sqrt3\), while the second term is at most
\[
\frac{2e^{1/4}}{\sqrt{18}}q<0.61q.
\]
Thus the displayed error is strictly smaller than \(2q\), proving the claim.

## Proof of Theorem 2

Theorem 1 reduces the problem to the first absolute moment of the unit-variance Rademacher sum
\[
S_N=\sum_i w_i^{(N)}\varepsilon_i.
\]
After sorting, diagonal compactness gives a further subsequence with coordinatewise limits \(w_j\). Fatou implies \(\sum_jw_j^2\le1\).

Fix a large \(J\). The first \(J\) coordinates converge to \(\sum_{j\le J}w_j\varepsilon_j\). In the remaining tail, the largest coefficient is asymptotically at most \(w_{J+1}\), which tends to zero with \(J\). The expansion
\[
\log\cos(tu)=-\frac{t^2u^2}{2}+O_t(u^4)
\]
therefore shows that the infinitesimal part of the tail converges to an independent Gaussian carrying exactly the variance not retained by the limiting coordinates. Letting \(J\to\infty\) yields
\[
S_N\Rightarrow
\sum_{j\ge1}w_j\varepsilon_j
+
\sqrt{1-\|w\|_2^2}\,Z.
\]
Because \(\mathbb ES_N^2=1\), the family \(|S_N|\) is uniformly integrable, so first absolute moments converge as well. Theorem 1 then gives the displayed efficiency limit.

For the range, Cauchy--Schwarz gives the upper bound \(1\). The sharp \(p=1\) Khintchine inequality gives
\[
\mathbb E\left|\sum_i c_i\varepsilon_i\right|
\ge\frac1{\sqrt2}\left(\sum_i c_i^2\right)^{1/2}.
\]
Approximating the Gaussian component by a diffuse normalized Rademacher sum extends the same lower bound to every Rademacher--Gaussian profile above. Both endpoints are attainable. In fact every \(c\in[1/\sqrt2,1]\) is attained already by the two-coordinate profile
\[
(c,\sqrt{1-c^2}),
\]
because for \(c\ge\sqrt{1-c^2}\),
\[
\mathbb E|c\varepsilon_1+\sqrt{1-c^2}\,\varepsilon_2|=c.
\]
This proves that the complete scalar limit set is \([1/\sqrt2,1]\).

If \(\max_iw_i^{(N)}\to0\), the ordinary Lindeberg central limit theorem gives \(S_N\Rightarrow Z\), hence the diffuse constant \(\sqrt{2/\pi}\).

## Proof of the Bernoulli-product corollary

For one Bernoulli coordinate, let \(M_i=(P_i+Q_i)/2\), and define the signed contrast
\[
c_i(x)=\frac{P_i(x)-Q_i(x)}{P_i(x)+Q_i(x)}
\]
when the denominator is nonzero, with the harmless value zero otherwise. Under \(M_i\), \(\mathbb Ec_i=0\). If
\[
v_i=\lambda_i a_i^2=\frac{(p_i-q_i)^2}{\lambda_i},
\]
a direct two-point calculation gives the exact identity
\[
\mathbb E_{M_i}c_i^2=\frac{v_i}{2-v_i}.
\]
Moreover \(|c_i|\le a_i\).

With \(M=\bigotimes_iM_i\), the two product densities are
\[
\frac{dP}{dM}=\prod_i(1+c_i),
\qquad
\frac{dQ}{dM}=\prod_i(1-c_i).
\]
Exactly the same odd-product expansion as above yields
\[
d_{\rm TV}(P,Q)
=
\mathbb E_M\left|\sum_i c_i+\text{odd terms of degree at least three}\right|.
\]
If
\[
W=\sum_i\mathbb Ec_i^2,
\]
then the squared \(L_2(M)\) norm of the higher-degree remainder is at most
\[
e^W-1-W-W^2/2=O(W^3).
\]
Since \(V=\sum_iv_i\to0\),
\[
W=\sum_i\frac{v_i}{2-v_i}=\frac V2+o(V).
\]
The condition \(\max_i a_i^2/V\to0\), together with \(|c_i|\le a_i\), is a Lindeberg condition for \(\sum_i c_i/\sqrt W\). Hence
\[
\frac{1}{\sqrt W}\sum_i c_i\Rightarrow N(0,1),
\]
and uniform integrability gives
\[
d_{\rm TV}(P,Q)
\sim\sqrt W\,\mathbb E|Z|
\sim\sqrt{\frac{V}{\pi}}.
\]
Applying the same statement to \(P\otimes Q\) and \(Q\otimes P\) doubles \(V\), proving the second formula and the limiting ratio \(\sqrt2\).

## Context and originality

Smirnov's arXiv:2609.19222v1 (16 September 2026) introduces exactly the mirror product laws above inside a CNOT reduction for total variation between Bernoulli products. Its Theorem 4.1 proves only an absolute-constant comparison \(\tau\gtrsim\Delta\), using \(\operatorname{arctanh}(a_i)\), \(|\sinh t|\ge|t|\), and Khintchine's inequality. The paper then obtains \(d_{\rm TV}(P,Q)\asymp\mathbb E\min\{1,\sqrt G\}\). It does not state a weak-signal efficiency profile, a sharp local range, the Rademacher--Gaussian compactification, or the diffuse constants displayed here.

The sharp Khintchine constants are classical; in particular, the \(p=1\) constant \(1/\sqrt2\) is prior art. Likewise, triangular-array Gaussian limits and local asymptotic normality are classical. The originality claim is therefore narrow: **to the best of our knowledge**, the quantitative reduction
\[
\tau/\Delta=\mathbb E|\langle w,\varepsilon\rangle|+O(q),
\]
the resulting complete weak-signal profile law and exact limit interval for Smirnov's mirror-product measurement, and the explicit diffuse specialization in Smirnov's \((\lambda_i,a_i)\) coordinates have not previously been stated.

Searches for the exact mirror-product formulation together with Rademacher profiles, Gaussian diffuse limits, computational-basis efficiency, and Bernoulli-product total variation did not locate an equivalent result. A material residual risk remains because Smirnov explicitly says that the underlying quantum statement will be discussed elsewhere; no separate public paper or identifier for that announced treatment was located. More broadly, older binary-state discrimination or local-asymptotic-normality literature could contain equivalent special cases under different notation.

## Limitations

- The quantitative \(2q\) estimate is a weak-signal statement; no claim is made that \(1/\sqrt2\) is a global all-signal lower constant for \(\tau/\Delta\).
- The profile theorem concerns the mirror-product subproblem singled out by Smirnov's reduction. A non-diffuse full Bernoulli-product experiment can retain additional coordinate-specific asymmetry not encoded by the mirror Rademacher profile alone.
- The exact \(\sqrt{V/\pi}\) formula for the original product laws assumes both \(V\to0\) and the stated Lindeberg condition. It is not a finite-sample bound and is not claimed outside that regime.
- The literature search cannot exclude unpublished or differently formulated coverage, especially the announced future quantum treatment.

## Reproducibility

`artifacts/verify_weak_signal_profiles.py` uses only the Python standard library. It enumerates small mirror products, checks the quantitative inequality on deterministic pseudorandom examples, evaluates equal-coordinate diffuse limits by binomial aggregation, and checks the Bernoulli-product and doubled-experiment asymptotic constants in an exchangeable family. `artifacts/verification.txt` contains its output. These calculations are confirmatory; the general statements are proved above.

## References

1. G. Smirnov, *TV between Bernoulli products, up to constants*, arXiv:2609.19222v1 (2026). https://arxiv.org/abs/2609.19222
2. U. Haagerup, *The best constants in the Khintchine inequality*, Studia Mathematica 70 (1981), 231--283. https://doi.org/10.4064/sm-70-3-231-283
3. C. Fuchs and J. van de Graaf, *Cryptographic distinguishability measures for quantum-mechanical states*, IEEE Transactions on Information Theory 45 (1999), 1216--1227. https://doi.org/10.1109/18.761271
4. A. Kontorovich, *On the tensorization of the variational distance*, Electronic Communications in Probability 30 (2025). https://doi.org/10.1214/25-ECP674
