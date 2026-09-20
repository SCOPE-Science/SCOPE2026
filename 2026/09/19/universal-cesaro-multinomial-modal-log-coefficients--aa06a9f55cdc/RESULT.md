# Universal Cesàro averages of the multinomial modal log expansion

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let
\[
X\sim\operatorname{Mult}(N;p_1,\ldots,p_n),\qquad p_i>0,\quad \sum_i p_i=1,
\]
and assume that \(p_1,\ldots,p_n\) are linearly independent over \(\mathbb Q\). Equivalently, under \(\sum_i p_i=1\), the only integer vectors \(v\) with \(v\cdot p\in\mathbb Z\) are multiples of \((1,\ldots,1)\). Let \(m(N)\) be the unique multinomial mode and
\[
\Delta_i(N)=m_i(N)-Np_i.
\]
Elezović (2026) identifies \(m(N)\) with the Jefferson--D'Hondt divisor allocation and gives the complete local logarithmic expansion
\[
\Pr\{X=m\}
=\frac{1}{(2\pi N)^{(n-1)/2}(p_1\cdots p_n)^{1/2}}
\exp\!\left(\sum_{k\ge1}\frac{c_k(t;p)}{N^k}\right),
\]
where, for bounded \(t_i=m_i-Np_i\),
\[
c_k(t;p)=\frac{(-1)^{k+1}}{k(k+1)}
\left[B_{k+1}-\sum_{i=1}^n p_i^{-k}B_{k+1}(t_i+1)\right].
\]
The same paper explicitly leaves the Cesàro averages at the on-slice modal reference open.

For every fixed \(k\ge1\), the modal coefficient has a Cesàro limit and that limit is independent of \(p\):
\[
\boxed{
\lim_{M\to\infty}\frac1M\sum_{N=1}^M c_k(\Delta(N);p)
=
\frac{(-1)^{k+1}}{k(k+1)}
\left[
B_{k+1}
-
\frac{(k+1)!(n-2)!}{(k+n-1)!}
\left\{\!\!\begin{matrix}k+n\\ n-1\end{matrix}\!\!\right\}
\right].
}
\]
Here \(B_j=B_j(0)\) are Bernoulli numbers with \(B_1=-1/2\), and \(\left\{{a\atop b}\right\}\) is a Stirling number of the second kind.

In particular,
\[
\boxed{\overline c_1=-\frac{(n-1)(3n+4)}{24}},\qquad
\boxed{\overline c_2=\frac{n(n-1)(n+2)}{48}}.
\]
For \(n=3\), the first four averages are
\[
-\frac{13}{12},\qquad \frac58,\qquad -\frac{187}{360},\qquad \frac{21}{40}.
\]

More generally, let \(F\) be any polynomial in the modal displacement vector. Then
\[
\frac1M\sum_{N=1}^M F(\Delta(N))\longrightarrow \mathbb E F(\Xi),
\]
where \(\Xi\) is the joint Jefferson seat-excess limit from Janson (2014). Consequently every fixed multiplicative coefficient \(Q_j\) in Elezović's expansion also has a modal Cesàro limit, explicitly representable as a finite moment of Janson's limit law. The universal closed form above is special to the individual logarithmic coefficients \(c_k\).

## Proof

### 1. The modal sequence is a Jefferson sequence

Elezović proves that the multinomial mode is exactly the Jefferson--D'Hondt allocation. Under the stated rational-independence assumption there are no persistent divisor ties, so its displacement vector is the Jefferson seat excess
\[
\Delta_i(N)=m_i(N)-Np_i.
\]
Janson studies exactly this fixed-\(p\) sequence with \(N\) uniform on \(\{1,\ldots,M\}\) and \(M\to\infty\). His Theorem 3.7 for the \(\beta\)-linear divisor method gives, for Jefferson \((\beta=1)\), joint convergence
\[
\Delta(N)\Rightarrow \Xi.
\]
The deterministic divisor bounds make all \(\Delta(N)\) lie in a common compact set. Hence weak convergence immediately upgrades to convergence of every polynomial moment. Since uniform randomization of \(N\in\{1,\ldots,M\}\) is exactly Cesàro averaging, the polynomial-transfer assertion follows.

For one coordinate Janson also gives the simpler marginal representation
\[
\Xi_i\overset d=
\frac{np_i-1}{2}+U_0+p_i\sum_{r=1}^{n-2}U_r,
\]
where \(U_0,U_1,\ldots\) are independent \(\operatorname{Unif}(-1/2,1/2)\).

### 2. Bernoulli-polynomial averaging collapses to one generating function

The Bernoulli-polynomial generating function is
\[
\sum_{m\ge0}B_m(x)\frac{z^m}{m!}=\frac{ze^{xz}}{e^z-1},
\]
and for \(U\sim\operatorname{Unif}(-1/2,1/2)\),
\[
\mathbb E e^{zU}=\frac{2\sinh(z/2)}{z}.
\]
Using the marginal law above,
\[
\begin{aligned}
\sum_{m\ge0}\mathbb E B_m(\Xi_i+1)\frac{z^m}{m!}
&=\frac{ze^{(np_i+1)z/2}}{e^z-1}
\frac{2\sinh(z/2)}{z}
\left(\frac{2\sinh(p_i z/2)}{p_i z}\right)^{n-2}\\
&=e^{np_i z/2}
\left(\frac{2\sinh(p_i z/2)}{p_i z}\right)^{n-2}.
\end{aligned}
\]
Writing \(w=p_i z\), define
\[
g_n(w)=e^{nw/2}\left(\frac{2\sinh(w/2)}{w}\right)^{n-2}
=e^w\left(\frac{e^w-1}{w}\right)^{n-2}.
\]
Therefore
\[
\mathbb E B_m(\Xi_i+1)=p_i^m m![w^m]g_n(w).
\]
At \(m=k+1\), the weighted sum appearing in \(c_k\) becomes
\[
\sum_i p_i^{-k}\mathbb E B_{k+1}(\Xi_i+1)
=(k+1)![w^{k+1}]g_n(w)\sum_i p_i,
\]
so all dependence on the probability vector cancels.

### 3. Stirling-number form

Using
\[
(e^w-1)^r=r!\sum_{q\ge r}
\left\{\!\!\begin{matrix}q\\r\end{matrix}\!\!\right\}\frac{w^q}{q!}
\]
and
\[
e^w(e^w-1)^{n-2}=\frac1{n-1}\frac{d}{dw}(e^w-1)^{n-1},
\]
one obtains
\[
[w^{k+1}]g_n(w)
=
\frac{(n-2)!}{(k+n-1)!}
\left\{\!\!\begin{matrix}k+n\\n-1\end{matrix}\!\!\right\}.
\]
Substitution into Elezović's formula for \(c_k\) proves the displayed theorem.

## Verification

`artifacts/verify_modal_cesaro.py` computes the universal constants exactly with rational arithmetic and independently generates the Jefferson allocation sequence by highest averages. For
\[
p=\left(\frac{\sqrt2}{4},\frac{\pi}{12},1-\frac{\sqrt2}{4}-\frac{\pi}{12}\right),
\]
using the first 200000 house sizes it gives
\[
\frac1M\sum c_1=-1.0833313326\quad\text{versus}\quad-13/12=-1.0833333333,
\]
and
\[
\frac1M\sum c_2=0.6249955290\quad\text{versus}\quad5/8=0.625.
\]
The artifact also checks the first-coefficient variance against a closed expression derived from Janson's joint limit; this numerical check is supplementary and is not needed for the theorem above.

## Relation to prior work and originality boundary

Elezović (2026) supplies both ingredients on the multinomial side: the exact identification of the mode with Jefferson and the all-orders Bernoulli-polynomial coefficients. Section 6 explicitly says that passage from its off-slice floor reference to an on-slice reference such as the mode is open and that the single-bin averaging argument no longer applies.

Janson (2014) supplies the decisive apportionment limit theorem: for rationally independent fixed \(p\), Jefferson seat excesses under Cesàro randomization of the house size have an explicit joint limiting distribution and a simple marginal representation. This record does not claim that apportionment limit law as new. The contribution is the bridge from that limit law to the later multinomial modal expansion, together with the all-orders cancellation yielding the universal Bernoulli--Stirling constants above.

Older work by Heinrich, Pukelsheim and Schwingenschlögl and by Heinrich and Schwingenschlögl develops limiting laws for rounding discrepancies and goodness-of-fit functionals. Those results are relevant prior machinery and are not claimed here. Searches of exact and synonymous formulations did not locate the all-orders modal coefficient average or the Bernoulli--Stirling formula. Originality is therefore asserted only **to the best of our knowledge**.

## Limitations

The theorem assumes fixed dimension and rationally independent \(p_i\). Rational relations can produce different orbit measures and divisor ties, so the displayed universal Cesàro law is not asserted there. The statement is Cesàro in the house size \(N\), not pointwise convergence. The closed universal formula concerns the logarithmic coefficients \(c_k\); multiplicative Bell-polynomial coefficients have modal Cesàro limits via the joint limit law but need not enjoy the same one-coordinate cancellation. No quantitative rate of Cesàro convergence is proved.

## References

1. N. Elezović, *Multinomial probabilities near the mode: integer modes and the complete local expansion*, arXiv:2609.20229v1, 2026. https://arxiv.org/abs/2609.20229v1
2. S. Janson, *Asymptotic bias of some election methods*, Annals of Operations Research 215 (2014), 89--136; arXiv:1110.6369. https://arxiv.org/abs/1110.6369
3. L. Heinrich, F. Pukelsheim, U. Schwingenschlögl, *On stationary multiplier methods for the rounding of probabilities and the limiting law of the Sainte-Laguë divergence*, Statistics & Decisions 23 (2005), 117--129. https://pukelsheim.narpan.net/2005c.pdf
4. L. Heinrich, U. Schwingenschlögl, *Goodness-of-fit Criteria for the Adams and Jefferson Rounding Methods and their Limiting Laws*, Metrika 64 (2006), 191--207. https://doi.org/10.1007/s00184-006-0044-0
