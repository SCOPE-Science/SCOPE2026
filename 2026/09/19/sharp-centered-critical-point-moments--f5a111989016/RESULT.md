# Sharp centered critical-point power moments and parity-dependent extremizers

## Statement

Let \(p\) be a polynomial of degree \(n\ge2\), all of whose zeros lie in the closed unit disk, and suppose that \(p(0)=0\). Let
\(\zeta_1,\ldots,\zeta_{n-1}\) be the critical points of \(p\), counted with multiplicity. A vanishing denominator below is interpreted as \(+\infty\).

For every exponent \(\lambda>0\),
\[
\boxed{
\sum_{j=1}^{n-1}|\zeta_j|^{-\lambda}
\ge
(n-1)n^{\lambda/(n-1)}.
}
\tag{1}
\]
Equivalently, every positive reciprocal power mean of the critical radii is at least
\[
\left(\frac1{n-1}\sum_{j=1}^{n-1}|\zeta_j|^{-\lambda}\right)^{1/\lambda}
\ge n^{1/(n-1)}.
\tag{2}
\]

The constant is sharp for every \(\lambda>0\), and all equality cases can be classified.

Write \(m=n-1\).

### Even degree

If \(n\) is even, equality in (1) holds if and only if
\[
\boxed{
p(z)=Cz\bigl(z^{n-1}-\omega\bigr),
\qquad C\ne0,\quad |\omega|=1.
}
\tag{3}
\]

### Odd degree

If \(n=2h+1\) is odd, equality in (1) holds if and only if
\[
\boxed{
p(z)=Cz\left(z^{2h}+t\eta z^h+\eta^2\right),
}
\tag{4}
\]
where
\[
C\ne0,\qquad |\eta|=1,\qquad
t\in\mathbb R,\qquad
|t|\le \frac{4\sqrt n}{n+1}.
\tag{5}
\]
Thus the centered extremizer set has a parity bifurcation: in even degree only the binomial family (3) occurs, whereas in odd degree there is a genuine real one-parameter family.

For every equality case, all nonzero zeros of \(p\) lie on the unit circle and all \(n-1\) critical points lie on the circle
\[
|\zeta|=n^{-1/(n-1)}.
\tag{6}
\]

## Quantitative radial stability

Assume the left side of (1) is finite and
\[
\frac1{(n-1)n^{\lambda/(n-1)}}
\sum_{j=1}^{n-1}|\zeta_j|^{-\lambda}
\le 1+\varepsilon.
\tag{7}
\]
Write the nonzero zeros as \(z_1,\ldots,z_{n-1}\), and put
\[
x_j=n^{-\lambda/(n-1)}|\zeta_j|^{-\lambda}.
\]
Then every nonzero zero is forced radially toward the unit circle:
\[
\boxed{
|z_k|\ge (1+\varepsilon)^{-(n-1)/\lambda}
\qquad(1\le k\le n-1),
}
\tag{8}
\]
and the critical radii satisfy the entropy-type defect bound
\[
\boxed{
\sum_{j=1}^{n-1}\bigl(x_j-1-\log x_j\bigr)
\le (n-1)\varepsilon.
}
\tag{9}
\]
Since \(x-1-\log x\ge0\), (9) quantitatively forces all normalized reciprocal critical radii toward \(1\) as \(\varepsilon\to0\).

## Context

Teng Zhang's 2026 preprint *Beyond Sendov's conjecture: the quadratic Tang--Zhang inequality* proves, for an arbitrary distinguished zero \(a\),
\[
\sum_{j=1}^{n-1}|a-\zeta_j|^{-2}\ge n-1
\]
and consequently the Tang--Zhang inequalities for all \(\lambda\ge2\). For the special endpoint \(a=0\), Zhang's Lemma 8.3 already records the stronger quadratic estimate
\[
\frac1{n-1}\sum_{j=1}^{n-1}|\zeta_j|^{-2}
\ge n^{2/(n-1)}
\]
by comparing constant terms and applying arithmetic--geometric mean.

The contribution here is not that product argument itself. It is the sharp all-positive-exponent centered theorem (including \(0<\lambda<1\), below the range of the Tang--Zhang conjecture as originally formulated), the complete equality classification for the stronger centered bound, and the resulting quantitative radial stability. In particular, equality for the centered strengthening is much less rigid than equality in the global quadratic Tang--Zhang theorem.

## Proof

Multiplying \(p\) by a nonzero constant does not affect its zeros or critical points. If \(0\) is a multiple zero, then \(0\) is also a critical point and (1) is infinite. Hence only the simple-zero case needs consideration.

Write
\[
p(z)=A z\prod_{k=1}^{m}(z-z_k),
\qquad |z_k|\le1,
\]
and
\[
p'(z)=nA\prod_{j=1}^{m}(z-\zeta_j).
\]
Evaluation at \(z=0\) gives the exact product identity
\[
\prod_{k=1}^{m}z_k
=
n\prod_{j=1}^{m}\zeta_j.
\tag{10}
\]
Thus
\[
\prod_{j=1}^{m}|\zeta_j|
\le \frac1n.
\tag{11}
\]
Arithmetic--geometric mean applied to the positive numbers
\(|\zeta_j|^{-\lambda}\) gives
\[
\frac1m\sum_{j=1}^{m}|\zeta_j|^{-\lambda}
\ge
\left(\prod_{j=1}^{m}|\zeta_j|^{-\lambda}\right)^{1/m}
\ge n^{\lambda/m},
\]
which proves (1).

Equality holds if and only if both inequalities above are equalities. Hence
\[
|z_1|=\cdots=|z_m|=1
\tag{12}
\]
and
\[
|\zeta_1|=\cdots=|\zeta_m|=r,
\qquad r=n^{-1/m}.
\tag{13}
\]

It remains to classify polynomials satisfying (12)--(13).

Normalize \(p\) to be monic and write
\[
p(z)=zq(z),\qquad
q(z)=\sum_{k=0}^{m}c_kz^k,\qquad c_m=1.
\]
Since every zero of \(q\) is unimodular, \(q\) is self-inversive:
\[
c_k=c_0\overline{c_{m-k}},
\qquad |c_0|=1.
\tag{14}
\]
Set \(D=p'/n\). Then \(D\) is monic and
\[
D(z)=\sum_{k=0}^{m}\frac{k+1}{n}c_kz^k.
\]
Because every zero of \(D\) has modulus \(r\), the rescaled polynomial
\[
E(w)=r^{-m}D(rw)
\]
has all zeros on the unit circle. Since \(r^m=1/n\), its constant term is again \(c_0\), so \(E\) is self-inversive as well. Combining its coefficient relations with (14), for each \(k\) with \(c_k\ne0\) one obtains
\[
(k+1)r^{k-m}=(m-k+1)r^{-k},
\]
or
\[
\frac{k+1}{m-k+1}=n^{-1+2k/m}.
\tag{15}
\]

Define for \(0\le x\le m\)
\[
F(x)=
\log\frac{x+1}{m-x+1}
+
\left(1-\frac{2x}{m}\right)\log n.
\]
Then
\[
F(0)=F(m/2)=F(m)=0,\qquad
F(m-x)=-F(x),
\]
and
\[
F''(x)=
-\frac1{(x+1)^2}
+\frac1{(m-x+1)^2}<0
\qquad(0<x<m/2).
\]
Thus strict concavity shows \(F(x)>0\) on \(0<x<m/2\). Consequently (15) can hold only for
\[
k=0,\quad k=m,\quad\text{and, if \(m\) is even, }k=m/2.
\tag{16}
\]

If \(m\) is odd, (16) yields
\[
q(z)=z^m+c_0,
\qquad |c_0|=1,
\]
which is exactly (3).

If \(m=2h\), choose \(|\eta|=1\) with \(c_0=\eta^2\). The middle self-inversive relation implies
\[
c_h=t\eta,\qquad t\in\mathbb R,
\]
so
\[
q(z)=z^{2h}+t\eta z^h+\eta^2.
\tag{17}
\]
The zeros of \(q\) are unimodular exactly when the roots of
\[
y^2+ty+1
\]
are unimodular, equivalently \(|t|\le2\).

On the other hand,
\[
E(w)=
w^{2h}
+
\frac{h+1}{\sqrt n}\,t\eta w^h
+
\eta^2.
\tag{18}
\]
Its zeros are unimodular exactly when
\[
\left|\frac{h+1}{\sqrt n}t\right|\le2,
\]
that is,
\[
|t|\le\frac{2\sqrt n}{h+1}
=\frac{4\sqrt n}{n+1}.
\]
This bound is at most \(2\), so it is the only restriction needed. This proves (4)--(5), including sufficiency.

For stability, let
\[
P=\prod_{k=1}^{m}|z_k|.
\]
By (10),
\[
\prod_{j=1}^{m}x_j=P^{-\lambda}\ge1.
\]
The geometric mean is bounded by the arithmetic mean in (7), hence
\[
P^{-\lambda/m}\le1+\varepsilon,
\]
which gives \(P\ge(1+\varepsilon)^{-m/\lambda}\). Since all \(|z_k|\le1\), their product is no larger than any individual factor, proving (8). Finally,
\[
\sum_{j=1}^{m}(x_j-1-\log x_j)
=
\sum_{j=1}^{m}x_j-m+\lambda\log P
\le m\varepsilon,
\]
because \(\log P\le0\). This proves (9).

## Literature and originality assessment

The directly relevant source is Teng Zhang, arXiv:2609.19126 (submitted 16 September 2026). Its Theorem 1.3 is the global quadratic Tang--Zhang inequality; Corollary 1.4 covers \(\lambda\ge2\); and Lemma 8.3 gives the stronger centered quadratic lower bound used as the starting point here. The source does not classify equality for that stronger centered estimate and does not state the all-\(\lambda>0\) centered strengthening or the stability bounds above.

Classical self-inversive-polynomial theory supplies the coefficient symmetry used in (14); no novelty is claimed for that fact. Literature on Smale's mean-value problem also treats polynomials whose critical points have equal modulus. In particular, secondary discussions of Sheil-Small's *Complex Polynomials*, pp. 361--362, and Dubinin's work report mean-value bounds under the equal-critical-radius hypothesis. Those results concern Smale-type critical values rather than the simultaneous unit-root/equal-critical-radius classification in (3)--(5).

Targeted searches for the exact centered reciprocal-moment constant, equal-critical-radius equality cases, self-inversive derivative classifications, and the sparse odd-degree family (17) did not locate the theorem above. The originality claim is therefore **to the best of our knowledge**. A residual risk remains that older geometric-polynomial literature contains an equivalent equality classification in different notation; the most relevant full source not independently inspected here is Sheil-Small's 2002 book.

## Limitations

This theorem concerns the special distinguished zero \(a=0\). It does not advance the open general Tang--Zhang range \(1\le\lambda<2\) for noncentral zeros. The stability statement is radial only: it controls the moduli of the nonzero zeros and critical points but does not give angular closeness to the extremizer families. No optimal angular stability modulus is claimed. No independent validation or formal proof-assistant verification is asserted.

## References

1. Teng Zhang, *Beyond Sendov's conjecture: the quadratic Tang--Zhang inequality*, arXiv:2609.19126 (2026), https://arxiv.org/abs/2609.19126.
2. Terence Tao, *A digestion of the proof of Sendov's conjecture* (2026), https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/.
3. T. Sheil-Small, *Complex Polynomials*, Cambridge Studies in Advanced Mathematics 75, Cambridge University Press (2002), https://doi.org/10.1017/CBO9780511543074.
4. A. Hinkkanen and I. Kayumov, *Smale's problem for critical points on certain two rays*, https://doi.org/10.1017/S1446788710000030.
