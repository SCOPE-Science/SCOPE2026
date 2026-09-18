# Rare-event Bernoulli TV: signed mass balance and proxy information loss

## Statement

Let
\[
P_{\mathbf p}=\bigotimes_{i=1}^n \operatorname{Ber}(p_i),\qquad
P_{\mathbf q}=\bigotimes_{i=1}^n \operatorname{Ber}(q_i),
\]
with \(p_i,q_i\in[0,1]\). Write
\[
A=\sum_{i=1}^n p_i,\qquad B=\sum_{i=1}^n q_i,
\]
\[
L=\sum_{i=1}^n |p_i-q_i|,\qquad M=|A-B|.
\]
Then
\[
\boxed{
\left|d_{\rm TV}(P_{\mathbf p},P_{\mathbf q})-
\frac{L+M}{2}\right|\le A^2+B^2.
}
\tag{1}
\]
Consequently, whenever \(A+B\to0\),
\[
d_{\rm TV}(P_{\mathbf p},P_{\mathbf q})
=\frac12\left(\sum_i|p_i-q_i|+
\left|\sum_i(p_i-q_i)\right|\right)
+O((A+B)^2).
\tag{2}
\]
The first-order term therefore contains both the unsigned coordinatewise discrepancy and the net signed intensity discrepancy.

Now use the quantities introduced by Smirnov for Bernoulli-product total variation:
\[
\lambda_i=p_i(1-q_i)+(1-p_i)q_i,\qquad
 a_i=\begin{cases}|p_i-q_i|/\lambda_i,&\lambda_i>0,\\0,&\lambda_i=0,\end{cases}
\]
and let independent \(D_i\sim\operatorname{Ber}(\lambda_i)\). Define
\[
G=\sum_{i=1}^n a_i^2D_i,\qquad
\mathcal T(\mathbf p,\mathbf q)=\mathbb E\min\{1,\sqrt G\},\qquad
\Lambda=\sum_i\lambda_i.
\]
Then
\[
\boxed{L-\Lambda^2\le \mathcal T(\mathbf p,\mathbf q)
\le L+\frac12\Lambda^2.}
\tag{3}
\]
Since \(\Lambda\le A+B\), equations (1) and (3) imply
\[
\boxed{
\left|d_{\rm TV}(P_{\mathbf p},P_{\mathbf q})-
\frac{\mathcal T(\mathbf p,\mathbf q)+|A-B|}{2}\right|
\le A^2+B^2+\frac12\Lambda^2.
}
\tag{4}
\]
Thus the rare-event correction missing from the sign-blind proxy \(\mathcal T\) is exactly the net signed mass imbalance at first order.

## A sharp information-loss family

Fix an integer \(m\ge1\), constants \(\alpha>\beta\ge0\), and a sign vector \(s=(s_1,\ldots,s_m)\in\{-1,1\}^m\). For sufficiently small \(\varepsilon>0\), set
\[
(p_i,q_i)=
\begin{cases}
(\varepsilon\alpha,\varepsilon\beta),&s_i=1,\\
(\varepsilon\beta,\varepsilon\alpha),&s_i=-1.
\end{cases}
\tag{5}
\]
Every coordinate, for every sign pattern, has exactly the same
\[
\lambda=\varepsilon(\alpha+\beta)-2\varepsilon^2\alpha\beta,
\qquad
a=\frac{\varepsilon(\alpha-\beta)}{\lambda}.
\tag{6}
\]
Hence the full ordered tuple \((\lambda_i,a_i)_{i=1}^m\), the law of \(G\), and \(\mathcal T\) are identical for all choices of \(s\). Nevertheless, (1) gives
\[
\boxed{
d_{\rm TV}(P_{\mathbf p},P_{\mathbf q})
=\frac{\alpha-\beta}{2}
\left(m+\left|\sum_{i=1}^m s_i\right|\right)\varepsilon
+O(\varepsilon^2),
}
\tag{7}
\]
whereas (3) gives
\[
\boxed{
\mathcal T(\mathbf p,\mathbf q)
=m(\alpha-\beta)\varepsilon+O(\varepsilon^2).
}
\tag{8}
\]
Therefore
\[
\frac{d_{\rm TV}}{\mathcal T}
\longrightarrow
\frac12\left(1+\frac{|\sum_i s_i|}{m}\right).
\tag{9}
\]
For aligned signs the limit is \(1\). For even \(m\) and perfectly balanced signs it is \(1/2\). In particular:

1. Smirnov's exact upper bound \(d_{\rm TV}\le\mathcal T\) has asymptotically sharp constant \(1\).
2. No universal inequality \(d_{\rm TV}\ge c\mathcal T\) can hold with \(c>1/2\). This does **not** prove that \(1/2\) is a valid universal lower constant.
3. Two Bernoulli-product pairs can have exactly the same complete \((\lambda_i,a_i)\) data and exactly the same law of \(G\), while their true total variation distances differ asymptotically by a factor of two.
4. Any estimator depending only on \((\lambda_i,a_i)_i\) that promises a symmetric universal multiplicative guarantee
\[
C^{-1}d_{\rm TV}\le F\le C d_{\rm TV}
\]
must have \(C\ge\sqrt2\). Any such estimator with a uniform relative-error guarantee \(|F-d_{\rm TV}|\le r d_{\rm TV}\) must have \(r\ge1/3\).

The last two bounds follow by applying the same estimator value to aligned and balanced sign patterns and letting \(\varepsilon\downarrow0\).

## Proof of the finite rare-event expansion

For \(k=0,\ldots,n\), let \(\Delta_k\) be the total absolute discrepancy between \(P_{\mathbf p}\) and \(P_{\mathbf q}\) on the Hamming-weight-\(k\) slice. Then
\[
2d_{\rm TV}(P_{\mathbf p},P_{\mathbf q})=\sum_{k=0}^n\Delta_k.
\tag{10}
\]

For the zero slice,
\[
\prod_i(1-p_i)=1-A+r_{\mathbf p},
\qquad
0\le r_{\mathbf p}\le\sum_{i<j}p_ip_j\le\frac{A^2}{2},
\]
and analogously for \(\mathbf q\). Hence
\[
|\Delta_0-M|\le\frac{A^2+B^2}{2}.
\tag{11}
\]

For the singleton slice, set
\[
P_i=p_i\prod_{j\ne i}(1-p_j),\qquad
Q_i=q_i\prod_{j\ne i}(1-q_j).
\]
If \(N_{\mathbf p}\) denotes the number of successes under \(P_{\mathbf p}\), then
\[
\sum_i(p_i-P_i)
=A-\Pr(N_{\mathbf p}=1)
=\mathbb E[N_{\mathbf p}\mathbf1_{\{N_{\mathbf p}\ge2\}}]
\le\mathbb E[N_{\mathbf p}(N_{\mathbf p}-1)]
\le A^2.
\]
The same holds for \(\mathbf q\), so the reverse triangle inequality in \(\ell_1\) gives
\[
|\Delta_1-L|\le A^2+B^2.
\tag{12}
\]
Finally,
\[
\sum_{k\ge2}\Delta_k
\le\Pr(N_{\mathbf p}\ge2)+\Pr(N_{\mathbf q}\ge2)
\le\frac{A^2+B^2}{2},
\tag{13}
\]
because \(\Pr(N\ge2)\le\mathbb E\binom N2\). Combining (10)--(13) proves (1).

## Proof of the proxy expansion

First note that \(|p_i-q_i|\le\lambda_i\), so \(0\le a_i\le1\), \(L\le\Lambda\), and \(\Lambda\le A+B\). On the event that exactly \(D_i=1\), the integrand in \(\mathcal T\) is exactly \(a_i\). The contribution of all singleton-disagreement events is therefore
\[
S_1=\sum_i |p_i-q_i|\prod_{j\ne i}(1-\lambda_j).
\]
Using \(\prod_j(1-x_j)\ge1-\sum_jx_j\) for \(x_j\in[0,1]\),
\[
S_1\ge L-L\Lambda\ge L-\Lambda^2,
\qquad S_1\le L.
\tag{14}
\]
All events with at least two disagreements contribute at most their probability, which is bounded by
\[
\Pr\left(\sum_iD_i\ge2\right)
\le\sum_{i<j}\lambda_i\lambda_j
\le\frac{\Lambda^2}{2}.
\tag{15}
\]
Equations (14) and (15) prove (3), and (4) follows from (1).

## Context and relation to prior work

Smirnov (2026) introduced \((\lambda_i,a_i)\), the random variable \(G\), and the computable proxy \(\mathbb E\min\{1,\sqrt G\}\), proving that it controls Bernoulli-product total variation up to universal constants and, in particular, proving the exact upper inequality \(d_{\rm TV}\le\mathcal T\). The result above identifies a first-order piece of information that this representation discards in the rare-event limit.

Avital, Kontorovich, and Salafatinos (2026) proved that Bernoulli-product total variation is comparable to \(\|\mathbf p-\mathbf q\|_1\) in a tiny-parameter regime and to the singleton-slice discrepancy in a larger small-parameter regime. Equation (1) refines the rare-event picture in a different direction: it gives an additive second-order remainder and exposes the signed total-intensity term \(|A-B|\).

Kontorovich (2025) showed that marginal total-variation distances alone cannot determine product total variation within arbitrarily good universal factors. The obstruction here is narrower but stronger for the newer representation: even the full sign-blind data \((\lambda_i,a_i)_i\), and hence the exact law of Smirnov's \(G\), can be identical while the true Bernoulli-product TV differs asymptotically by a factor two.

## Limitations

The additive expansion is most informative when \(A+B\) is small; if \(L\) is much smaller than \((A+B)^2\), its first-order term need not dominate the remainder. The factor-two construction is an information-loss statement only for methods that retain no information beyond the sign-blind \((\lambda_i,a_i)\) representation; it is not an algorithmic lower bound for procedures using the full vectors \(\mathbf p,\mathbf q\). The construction shows that a universal lower comparison \(d_{\rm TV}\ge c\mathcal T\) cannot have \(c>1/2\), but it does not establish \(c=1/2\). No higher-order expansion or optimal universal comparison constant is claimed.

## References

- G. Smirnov, *TV between Bernoulli products, up to constants*, arXiv:2609.19222, 2026. https://arxiv.org/abs/2609.19222
- A. Avital, A. Kontorovich, G. Salafatinos, *TV over Bernoulli products: the small parameter regime*, arXiv:2602.21828, 2026. https://arxiv.org/abs/2602.21828
- A. Kontorovich, *On the tensorization of the variational distance*, Electronic Communications in Probability 30 (2025), Article 32. https://doi.org/10.1214/25-ECP680
- A. Kontorovich, *A homogenization principle for total variation*, arXiv:2604.03882, 2026. https://arxiv.org/abs/2604.03882
