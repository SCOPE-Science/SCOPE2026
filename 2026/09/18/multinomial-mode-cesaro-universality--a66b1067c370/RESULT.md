# On-slice Cesàro laws for multinomial modes

## Result

Let
\[
X^{(N)}\sim\operatorname{Mult}(N;p_1,\ldots,p_n),\qquad p_i>0,\quad \sum_i p_i=1,
\]
and suppose \(p_1,\ldots,p_n\) are linearly independent over \(\mathbb Q\). Equivalently,
\[
\{v\in\mathbb Z^n:v\cdot p\in\mathbb Z\}=\mathbb Z(1,\ldots,1).
\]
Under this generic arithmetic condition the multinomial mode \(m(N)\) is unique for every \(N\). Write
\[
t(N)=m(N)-Np.
\]
Elezović's complete local expansion at any bounded displacement is
\[
\Pr\{X^{(N)}=m\}
=\frac{1}{(2\pi N)^{(n-1)/2}\sqrt{\prod_i p_i}}
\exp\!\left(\sum_{k\ge1}\frac{c_k(t;p)}{N^k}\right),
\]
where
\[
c_k(t;p)=\frac{(-1)^{k+1}}{k(k+1)}
\left[B_{k+1}-\sum_{i=1}^n p_i^{-k}B_{k+1}(t_i+1)\right].
\]
The recent source explicitly leaves Cesàro averaging after passage from its off-slice floor reference to the actual multinomial mode open. The statements below give such on-slice averages for generic \(p\).

### 1. Polynomial transfer law at the mode

For any polynomial \(F\) on \(\mathbb R^n\),
\[
\boxed{
\lim_{M\to\infty}\frac1M\sum_{N=1}^M F(t(N))=\mathbb E F(T),
}
\]
where \(T\) has the following explicit law. Let \(J\in\{1,\ldots,n\}\) satisfy \(\Pr(J=j)=p_j\), independently of iid \(U_1,\ldots,U_n\sim U(0,1)\), and put
\[
V_i=\mathbf 1\{J\ne i\}U_i,\qquad
T_i=p_i\sum_{j=1}^nV_j-V_i.
\]
Equivalently, its joint moment generating function is
\[
\boxed{
M_T(z)=\sum_{j=1}^n p_j\prod_{i\ne j}h(p\cdot z-z_i),
\qquad h(w)=\frac{e^w-1}{w},\quad h(0)=1.
}
\]
Thus every polynomial on-slice modal average is obtainable by differentiation:
\[
\lim_{M\to\infty}\frac1M\sum_{N\le M}F(t(N))
=F(\partial_z)M_T(z)\big|_{z=0}.
\]
This is a direct bridge from the fixed-\(p\), random-house-size Jefferson seat-excess limit law of Janson to the modal local expansion.

### 2. Every logarithmic coefficient has a universal Cesàro mean

Define numbers \(b_{m,n}\) by
\[
\boxed{
\sum_{m\ge0}b_{m,n}\frac{y^m}{m!}
=e^{ny/2}\left(\frac{\sinh(y/2)}{y/2}\right)^{n-2}.
}
\]
Then for every fixed \(k\ge1\),
\[
\boxed{
\lim_{M\to\infty}\frac1M\sum_{N=1}^M c_k(t(N);p)
=\frac{(-1)^{k+1}}{k(k+1)}\bigl(B_{k+1}-b_{k+1,n}\bigr).
}
\]
In particular, the Cesàro mean of every logarithmic coefficient \(c_k\) is independent of the probability vector \(p\); it depends only on the number \(n\) of categories.

The first values are
\[
b_{1,n}=\frac n2,\qquad
b_{2,n}=\frac{(n+1)(3n-2)}{12},\qquad
b_{3,n}=\frac{n(n-1)(n+2)}8,
\]
so
\[
\boxed{\overline c_1=-\frac{(n-1)(3n+4)}{24}},
\qquad
\boxed{\overline c_2=\frac{n(n-1)(n+2)}{48}},
\]
and
\[
\overline c_3=-\frac{(n-1)(15n^3+45n^2-10n-32)}{2880}.
\]

### 3. Universality breaks for the multiplicative expansion at second order

Write
\[
\exp\!\left(\sum_{k\ge1}\frac{c_k}{N^k}\right)
=1+\frac{Q_1}{N}+\frac{Q_2}{N^2}+\cdots,
\]
so \(Q_1=c_1\) and \(Q_2=c_2+c_1^2/2\). Put
\[
A_1=\sum_{i=1}^n\frac1{p_i},\qquad
A_2=\sum_{i=1}^n\frac1{p_i^2}.
\]
Then
\[
\boxed{
\overline{Q}_2
=\frac{A_2}{1440}+\frac{A_1}{720}
+\frac{45n^4+150n^3-5n^2-238n+36}{5760}.
}
\]
Hence the all-order universality is specific to the logarithmic coefficients: the actual probability expansion already remembers heterogeneity in \(p\) at order \(N^{-2}\).

A directly probabilistic first-order consequence is obtained by normalizing the modal mass,
\[
R_N=(2\pi N)^{(n-1)/2}\sqrt{\prod_i p_i}\;\Pr\{X^{(N)}=m(N)\}.
\]
The uniform bounded-displacement expansion gives
\[
N(R_N-1)=c_1(t(N);p)+O(N^{-1}),
\]
and therefore
\[
\boxed{
\lim_{M\to\infty}\frac1M\sum_{N=1}^M N(R_N-1)
=-\frac{(n-1)(3n+4)}{24}.
}
\]

## Proof

Elezović identifies the multinomial mode with Jefferson/D'Hondt apportionment. Under rational linear independence no quotient tie \(p_i/k=p_j/\ell\) can occur, so the mode is unique. Janson's Theorem 3.7, specialized to the Jefferson parameter, states that if \(N\) is uniform on \(\{1,\ldots,M\}\) and \(M\to\infty\), then the seat-excess vector converges jointly to \(T\) above. The deterministic Jefferson bounds make all modal displacements uniformly bounded. Consequently weak convergence implies convergence of every polynomial moment, proving the polynomial transfer law.

Conditioning the joint representation on \(J=j\) gives
\[
z\cdot T=\sum_{i\ne j}(p\cdot z-z_i)U_i,
\]
which immediately yields the displayed formula for \(M_T\).

For the logarithmic coefficients only one-coordinate moments are needed. Janson's marginal form for Jefferson is
\[
T_i\overset d=\frac{np_i-1}{2}+\widetilde U_0
+p_i\sum_{r=1}^{n-2}\widetilde U_r,
\]
with independent \(\widetilde U_r\sim U(-1/2,1/2)\). Using the Bernoulli-polynomial generating function
\[
\sum_{m\ge0}B_m(x)\frac{z^m}{m!}=\frac{ze^{xz}}{e^z-1}
\]
and the centered-uniform moment generating function gives
\[
\begin{aligned}
\sum_{m\ge0}\mathbb E B_m(T_i+1)\frac{z^m}{m!}
&=\frac{ze^z}{e^z-1}\,\mathbb E e^{zT_i}\\
&=e^{np_i z/2}
\left(\frac{\sinh(p_i z/2)}{p_i z/2}\right)^{n-2}\\
&=\sum_{m\ge0}p_i^m b_{m,n}\frac{z^m}{m!}.
\end{aligned}
\]
Thus
\[
\mathbb E B_m(T_i+1)=p_i^m b_{m,n}.
\]
Substitution with \(m=k+1\) into Elezović's formula gives
\[
\sum_i p_i^{-k}\mathbb E B_{k+1}(T_i+1)
=b_{k+1,n}\sum_i p_i=b_{k+1,n},
\]
proving the universal formula for \(\overline c_k\).

For \(Q_2\), set
\[
q(T)=\sum_i\frac{T_i^2+T_i}{p_i},
\qquad c_1=\frac{1-A_1}{12}-\frac12q.
\]
Conditionally on \(J=j\), write \(r=n-1\), \(A_j=A_1-p_j^{-1}\), and \(B_j=A_2-p_j^{-2}\). Direct integration of iid uniforms gives
\[
\mathbb E(q\mid J=j)=\frac{r(3r+5)}{12}-\frac{A_j}{6},
\]
\[
\mathbb E(q^2\mid J=j)
=\frac{r(15r^3+50r^2+45r+18)}{240}
-\frac{(15r^2+25r+2)A_j}{180}
+\frac{B_j}{180}+\frac{A_j^2}{36}.
\]
Averaging with weights \(p_j\) uses
\[
\sum_jp_jA_j=A_1-n,
\quad
\sum_jp_jB_j=A_2-A_1,
\quad
\sum_jp_jA_j^2=A_1^2-(2n-1)A_1,
\]
and yields
\[
\operatorname{Var}(c_1)
=\frac{2A_2+4A_1-5n^2+21n-22}{1440}.
\]
Combining this with \(\overline c_1\), \(\overline c_2\), and \(Q_2=c_2+c_1^2/2\) gives the stated formula for \(\overline Q_2\).

## Numerical check

For the generic triple used in Elezović's discussion,
\[
p=\left(\frac{\sqrt2}{4},\frac\pi{12},1-\frac{\sqrt2}{4}-\frac\pi{12}\right),
\]
a direct highest-averages enumeration through \(N=300000\) gives

```text
mean c1  = -1.083333541441; prediction = -1.083333333333
mean c2  =  0.624999524646; prediction =  0.625000000000
mean Q2  =  1.243641989110; prediction =  1.243642355949
```

The standalone script `artifacts/check_low_order.py` reproduces these values.

## Context and originality boundary

Elezović (2026) supplies the exact Jefferson characterization of the multinomial mode and the complete Bernoulli-polynomial local expansion. Its Section 6 averages coefficients at an off-slice floor reference and explicitly says that passage to an on-slice reference such as the mode is open. The present result addresses that on-slice question under the generic arithmetic condition.

Janson (2011/2014) already proves the fixed-probability Jefferson seat-excess limit law used here, including both joint and marginal representations. Accordingly, that limit law, the Jefferson bias, and its variance are prior art and are not claimed here. Earlier apportionment work also studies seat-excess moments and Sainte-Laguë divergences under related but different asymptotic models.

The originality claim is restricted to the connection of the Jefferson seat-excess law with the multinomial modal local expansion, the resulting all-order probability-vector-independent Cesàro formula for the logarithmic coefficients, the explicit on-slice \(Q_2\) formula showing the first loss of universality, and the normalized modal-mass corollary. Targeted searches did not locate these statements. Older apportionment moment literature is extensive, and some older articles were inspected only through metadata or abstracts; equivalent prior coverage there remains the main residual originality risk. The claim is therefore only to the best of our knowledge.

## Limitations

The theorem assumes rational linear independence of \(p_1,\ldots,p_n\). Rational or otherwise arithmetically nongeneric probability vectors can have periodic structure and quotient ties, and require separate averaging laws. The formula gives Cesàro means, not pointwise convergence in \(N\). The logarithmic coefficients have universal means, but the multiplicative coefficients generally do not, as \(Q_2\) already shows. No convergence rate for the Cesàro averages is asserted.

## References

1. N. Elezović, *Multinomial probabilities near the mode: integer modes and the complete local expansion*, arXiv:2609.20229 (2026).
2. S. Janson, *Asymptotic bias of some election methods*, arXiv:1110.6369; Annals of Operations Research 215 (2014), 89-136, DOI: 10.1007/s10479-012-1141-2.
3. U. Schwingenschlögl and M. Drton, *Seat allocation distributions and seat biases of stationary apportionment methods for proportional representation*, Metrika 60 (2004), 191-202, DOI: 10.1007/s001840400347.
4. U. Schwingenschlögl and M. Drton, *Seat excess variances of apportionment methods for proportional representation*, Statistics & Probability Letters 76 (2006), 1723-1730, DOI: 10.1016/j.spl.2006.04.014.
5. L. Heinrich, F. Pukelsheim and U. Schwingenschlögl, *On stationary multiplier methods for the rounding of probabilities and the limiting law of the Sainte-Laguë divergence*, Statistics & Decisions 23 (2005), 117-129, DOI: 10.1524/stnd.2005.23.2.117.
