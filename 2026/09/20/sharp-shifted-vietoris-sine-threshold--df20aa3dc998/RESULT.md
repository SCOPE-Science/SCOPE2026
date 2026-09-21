# Sharp exponent threshold and endpoint boundary layer for shifted Vietoris sine sums

## Result

Fix
\[
\alpha,\beta,\lambda,\mu\ge 0,\qquad s:=\lambda+\mu,
\]
and define
\[
q_1=1,\qquad
q_k=\frac{1}{(k+\alpha)^\lambda(k+\beta)^\mu}\quad(k\ge2),
\]
together with
\[
S_n(x):=\sum_{k=1}^n q_k\sin(kx).
\]

Then
\[
\boxed{
S_n(x)>0\ \text{for every }n\ge1\text{ and every }x\in(0,\pi)
\quad\Longleftrightarrow\quad
\lambda+\mu\ge1.
}
\]

The sufficiency is the theorem of Sangal and Swaminathan. The new point is the converse, which is quantitative and independent of the shifts. If \(0\le s<1\), then along even \(n\),
\[
\boxed{
\sum_{k=1}^n(-1)^{k-1}kq_k
=
-\frac12\,n^{\,1-s}+o(n^{\,1-s}).
}
\]
Consequently every sufficiently large even partial sum is negative immediately to the left of \(\pi\).

More strongly, for each fixed \(y>0\), along even \(n\to\infty\),
\[
\boxed{
n^s S_n\!\left(\pi-\frac yn\right)\longrightarrow
-\frac12\sin y.
}
\]
Hence for every fixed \(y\in(0,\pi)\),
\[
S_n\!\left(\pi-\frac yn\right)<0
\]
for all sufficiently large even \(n\). Thus the failure below the threshold occurs on the natural \(1/n\) endpoint scale, with a universal leading profile that does not depend on \(\alpha,\beta\) or on how \(s\) is split between \(\lambda\) and \(\mu\).

Sangal and Swaminathan also prove positivity of the corresponding cosine partial sums when \(s\ge1\). Therefore \(s\ge1\) is likewise the exact threshold for simultaneous positivity of their sine and cosine families.

## Context

Sangal and Swaminathan introduced the coefficients
\[
q_0=2,\quad q_1=1,\quad
q_k=((k+\alpha)^\lambda(k+\beta)^\mu)^{-1}
\]
and proved positivity of the associated sine and cosine partial sums for \(\alpha,\beta,\lambda,\mu\ge0\) with \(\lambda+\mu\ge1\). Their paper also recalls Belov's necessary-and-sufficient alternating-sum criterion for positivity of all sine partial sums with nonincreasing positive coefficients.

The exponent condition in that theorem is therefore a natural sharpness question. The result above shows that no choice of nonnegative shifts can improve it: below \(1\), all sufficiently large even sine partial sums fail positivity near \(x=\pi\).

## Proof

### 1. A paired alternating-sum lemma

Let \(f:[0,1]\to\mathbb R\) be absolutely continuous, with \(f(0)=0\) and \(f'\in L^1(0,1)\). For even \(n\),
\[
\sum_{k=1}^n(-1)^{k+1}f(k/n)
=
\sum_{j=1}^{n/2}
\left[f((2j-1)/n)-f(2j/n)\right].
\]
Writing
\[
\chi_n=\mathbf 1_{\bigcup_{j=1}^{n/2}((2j-1)/n,\,2j/n]},
\]
this becomes
\[
-\int_0^1\chi_n(u)f'(u)\,du.
\]
The alternating half-mesh indicators \(\chi_n\) converge weakly against \(L^1(0,1)\) to \(1/2\). Hence
\[
\sum_{k=1}^n(-1)^{k+1}f(k/n)
\longrightarrow
-\frac12\int_0^1 f'(u)\,du
=
-\frac12 f(1).
\tag{1}
\]

### 2. Endpoint alternating slope for \(s<1\)

For \(k\ge2\),
\[
kq_k
=
k^{1-s}
\left(1+\frac{\alpha}{k}\right)^{-\lambda}
\left(1+\frac{\beta}{k}\right)^{-\mu}
=
k^{1-s}+O(k^{-s}).
\tag{2}
\]
The error term has first difference \(O(k^{-s-1})\). Thus its alternating partial sums are \(O(1)\) when \(s>0\); when \(s=0\), necessarily \(\lambda=\mu=0\), so the error vanishes identically.

Apply (1) to
\[
f(u)=u^{1-s}.
\]
Since \(0\le s<1\), \(f(0)=0\) and \(f'(u)=(1-s)u^{-s}\in L^1(0,1)\). Therefore, along even \(n\),
\[
n^{s-1}\sum_{k=1}^n(-1)^{k-1}k^{1-s}\to-\frac12.
\]
Together with (2),
\[
\sum_{k=1}^n(-1)^{k-1}kq_k
=
-\frac12 n^{1-s}+o(n^{1-s}).
\tag{3}
\]

Now \(S_n(\pi)=0\), and
\[
\lim_{\varepsilon\downarrow0}
\frac{S_n(\pi-\varepsilon)}{\varepsilon}
=
\sum_{k=1}^n(-1)^{k-1}kq_k.
\tag{4}
\]
By (3), the right side is negative for every sufficiently large even \(n\). Thus \(S_n(x)<0\) for \(x<\pi\) sufficiently close to \(\pi\). This proves the necessity of \(s\ge1\).

### 3. Universal \(1/n\) boundary layer

For fixed \(y>0\), first replace \(q_k\) by \(k^{-s}\). Then
\[
n^s\sum_{k=1}^n(-1)^{k+1}k^{-s}\sin(ky/n)
=
\sum_{k=1}^n(-1)^{k+1}F_y(k/n),
\]
where
\[
F_y(u)=u^{-s}\sin(yu),\qquad F_y(0):=0.
\]
Because \(s<1\),
\[
F_y'(u)
=
-s\,u^{-s-1}\sin(yu)+y\,u^{-s}\cos(yu)
\]
is integrable at \(0\). Applying (1),
\[
\sum_{k=1}^n(-1)^{k+1}F_y(k/n)
\longrightarrow
-\frac12F_y(1)
=
-\frac12\sin y.
\tag{5}
\]

It remains to show that the shifts do not change the limit. Put
\[
d_k=q_k-k^{-s}\quad(k\ge2),\qquad d_1=0.
\]
For \(s>0\),
\[
d_k=O(k^{-s-1}),\qquad d_{k+1}-d_k=O(k^{-s-2}).
\tag{6}
\]
Pairing adjacent terms, using \(|\sin(ky/n)|\le ky/n\) and
\[
|\sin((k+1)y/n)-\sin(ky/n)|\le y/n,
\]
gives
\[
\sum_{k=1}^n(-1)^{k+1}d_k\sin(ky/n)=O(n^{-1}).
\tag{7}
\]
Multiplication by \(n^s\) makes (7) \(o(1)\), since \(s<1\). For \(s=0\), \(d_k=0\) identically. Combining this with (5) proves the boundary-layer limit.

### 4. Sufficiency

For \(s\ge1\), strict positivity of every \(S_n\) on \((0,\pi)\) is exactly the Sangal--Swaminathan theorem. Their companion cosine theorem gives the simultaneous-positivity corollary.

As a consistency check with Belov's criterion, set \(b_k=kq_k\). For \(k\ge2\), the smooth extension
\[
b(x)=\frac{x}{(x+\alpha)^\lambda(x+\beta)^\mu}
\]
has logarithmic derivative whose sign is that of
\[
(1-s)x^2+
(\alpha+\beta-\lambda\beta-\mu\alpha)x+\alpha\beta.
\]
When \(s>1\), this quadratic has at most one positive zero, so the tail \((b_k)_{k\ge2}\) is unimodal; when \(s=1\), its linear coefficient is \(\lambda\alpha+\mu\beta\ge0\), so the tail is nondecreasing. Also \(b_k\le k^{1-s}\le1=b_1\). Pairing increments then yields
\[
\sum_{k=1}^{2m}(-1)^{k-1}b_k\ge0,
\]
which is precisely the endpoint alternating condition appearing in Belov's criterion.

## Originality and literature check

The 2017/2020 Sangal--Swaminathan paper proves the \(s\ge1\) direction and states the general Belov criterion, but does not state the sharp converse for this shifted power family or the endpoint asymptotics above. Their 2017 Cesàro-operator application repeats the same sufficient exponent condition.

Searches by the authors' names, the exact shifted coefficients, the condition \(\lambda+\mu\), Vietoris/Belov terminology, sharpness/necessity, and endpoint asymptotics did not locate a prior statement of the classification or the universal boundary-layer limit. A later accessible manuscript by M. K. Kwong restates the Vietoris--Belov criterion and the general derivative obstruction at \(x=\pi\), but studies a different coefficient family.

The originality claim is therefore limited to the exact threshold for the Sangal--Swaminathan shifted-power family and the quantitative endpoint asymptotics. Since the ingredients include the classical Belov endpoint criterion and standard alternating-sum asymptotics, a differently phrased prior application to regularly varying coefficients remains a concrete residual risk.

## Limitations

- The result classifies the sine family and, using the known cosine theorem above threshold, the simultaneous sine--cosine property. It does not determine the optimal threshold for cosine positivity alone when \(s<1\).
- The boundary-layer statement is given for each fixed \(y\); stronger uniform expansions with lower-order shift-dependent terms are not developed here.
- A prior result phrased only in terms of regularly varying coefficients or an unindexed application of Belov's criterion could overlap the converse.

## References

1. P. Sangal and A. Swaminathan, *Vietoris type theorem related to positivity of trigonometric polynomials*, arXiv:1705.03759 (2017; revised 2020). https://arxiv.org/abs/1705.03759
2. P. Sangal and A. Swaminathan, *Geometric Properties of Cesàro Averaging Operators*, Journal of Complex Analysis (2017), Article ID 6584584. https://doi.org/10.1155/2017/6584584
3. M. K. Kwong, *A New Family of Nonnegative Sine Polynomials*. https://ncts.ntu.edu.tw/upload/blistfs29160804294214120.pdf
