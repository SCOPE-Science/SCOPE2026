# Uniform–geometric gcd-degree statistics of polynomial product collisions

## Finding

Let \(q\ge 2\) be a prime power and \(d\ge0\) an integer. Put \(\mathcal M_{q,d}=\{f\in\mathbb F_q[T]: f\text{ monic},\ 0\le\deg f\le d\}\). Choose uniformly an ordered quadruple \((f_1,f_2,f_3,f_4)\in\mathcal M_{q,d}^4\) subject to \(f_1f_2=f_3f_4\), and define
\[
A=\deg\gcd(f_1,f_3),\qquad B=\deg\gcd(f_2,f_4),\qquad J=A-B.
\]
For every \(0\le a,b\le d\), the exact number of such quadruples with \((A,B)=(a,b)\) is
\[
N_{q,d}(a,b)=\frac{q^{2d+1-|a-b|}-q^{a+b}}{q-1}.
\]
Consequently, the exact total number of quadruples is
\[
E_{q,d}=\frac{(d+1)(q^2-1)q^{2d+1}-3q^{2d+2}+4q^{d+1}-1}{(q-1)^3}.
\]
Let \(A_*\) be uniform on \(\{0,\dots,d\}\), independent of an integer-valued variable \(J_*\) with bilateral geometric law
\[
\mathbb P(J_*=j)=\frac{q-1}{q+1}q^{-|j|},\qquad j\in\mathbb Z.
\]
Then the **joint** total-variation estimate, valid uniformly over all prime powers \(q\) and integers \(d\ge0\), is
\[
d_{\rm TV}\big(\mathcal L(A,J),\mathcal L(A_*,J_*)\big)
\le\frac{3q}{(q^2-1)(d+1)}.
\]
In particular, for each fixed prime power \(q\), as \(d\to\infty\), the pair \((A/d,J)\) converges in distribution to \((U,J_*)\), where \(U\) is uniform on \([0,1]\) and independent of \(J_*\). Also \(B/d\) converges in distribution to \(U\). The latter is a weak-convergence statement; a continuous uniform law cannot be approached in total variation by discrete variables.

## Assumptions and scope

All polynomials are **nonzero monic**, so the only degree-zero polynomial counted is \(1\). Greatest common divisors are taken monic, including \(\gcd(1,1)=1\). The four factors are ordered, repetition is allowed, \(q\) is an arbitrary finite-field order, and \(d\) is a nonnegative degree cutoff. Total variation is \(d_{\rm TV}(P,Q)=\frac12\sum_x|P(x)-Q(x)|\) for distributions on the countable space \(\{0,\ldots,d\}\times\mathbb Z\). The limit keeps \(q\) fixed; the finite-\(d\) bound is uniform in \(q\).

## Proof

**1. Unique factorization of a product collision.** Write \(g=\gcd(f_1,f_3)\) and \(f_1=gu,\ f_3=gv\), with \(\gcd(u,v)=1\). Cancellation in \(f_1f_2=f_3f_4\) gives \(u f_2=v f_4\). Since \(u,v\) are coprime in \(\mathbb F_q[T]\), there is a unique monic \(h\) with
\[
(f_1,f_2,f_3,f_4)=(gu,hv,gv,hu),\qquad\gcd(u,v)=1.
\]
Here \(h=\gcd(f_2,f_4)\), so \(A=\deg g\), \(B=\deg h\). If \(\deg g=a\), \(\deg h=b\), all four cutoff conditions reduce to \(\deg u,\deg v\le L=d-\max(a,b)\).

**2. Exact coprime-pair count.** There are \(F_L=1+q+\cdots+q^L=(q^{L+1}-1)/(q-1)\) monic polynomials of degree at most \(L\). With \(F_{-1}=0\), polynomial Möbius inversion gives the number of ordered coprime pairs as
\[
C_L=\sum_{r=0}^{L}\Big(\sum_{\substack{h\text{ monic}\\\deg h=r}}\mu(h)\Big)F_{L-r}^2
=F_L^2-qF_{L-1}^2=\frac{q^{2L+1}-1}{q-1}.
\]
The middle equality uses the formal Euler product \(\sum_{h\text{ monic}}\mu(h)z^{\deg h}=1-qz\); the expression also holds for \(L=0\). There are \(q^a\) choices of \(g\) and \(q^b\) choices of \(h\). Therefore
\[
N_{q,d}(a,b)=q^{a+b}C_{d-\max(a,b)}
=\frac{q^{2d+1-|a-b|}-q^{a+b}}{q-1},
\]
proving the joint count. Summing over both degrees, or equivalently grouping terms by \(\ell=d-\max(a,b)\), gives
\[
E_{q,d}=\sum_{\ell=0}^{d}\frac{q^{2(d-\ell)}(q^{2\ell+1}-1)}{q-1}
\left(1+2\sum_{j=1}^{d-\ell}q^{-j}\right),
\]
which evaluates by finite geometric sums to the stated closed expression. This reproduces the previously known total energy, but the joint count retains a different statistic.

**3. Quantitative asymptotic independence.** For \(0\le a\le d\), \(j\in\mathbb Z\), put
\[
R_{a,j}=q^{-|j|},\quad
W_{a,j}=\mathbf{1}_{\{0\le a-j\le d\}}q^{-|j|}
\left(1-q^{-(2(d-\max(a,a-j))+1)}\right).
\]
The formula in Step 2 shows that \(W\), upon normalization, is the probability mass function of \((A,J)\), whereas normalizing \(R\) yields the independent reference law. In particular \(0\le W_{a,j}\le R_{a,j}\) pointwise, and
\[
R_0:=\sum_{a=0}^{d}\sum_{j\in\mathbb Z}R_{a,j}
=(d+1)\frac{q+1}{q-1}.
\]
The total removed mass \(D=\sum(R-W)\) consists of a boundary contribution (where \(b=a-j\) lies outside \([0,d]\)) and an interior correction. Two geometric-tail summations give
\[
D_{\mathrm{boundary}}=
\sum_{a=0}^{d}\frac{q^{-a}+q^{-(d-a)}}{q-1}
\le \frac{2q}{(q-1)^2},
\]
\[
D_{\mathrm{interior}}
\le\sum_{\ell=0}^{\infty}q^{-2\ell-1}
\left(1+2\sum_{j=1}^{\infty}q^{-j}\right)
=\frac q{(q-1)^2}.
\]
Indeed for each \(\ell=d-\max(a,b)\), there is one diagonal pair and at most two pairs of each positive imbalance \(|j|\). Hence \(D\le 3q/(q-1)^2\). A probability measure proportional to \(R\) is a mixture of the measure proportional to \(W\), with weight \((R_0-D)/R_0\), and the measure proportional to \(R-W\), with remaining weight \(D/R_0\). Consequently its total-variation distance from normalized \(W\) is at most \(D/R_0\), proving
\[
d_{\rm TV}\le\frac{3q}{(q^2-1)(d+1)}.
\]
For fixed \(q\), the right side tends to zero. A discrete uniform random variable on \(\{0,\dots,d\}\) divided by \(d\) converges weakly to a uniform variable on \([0,1]\) for \(d\to\infty\). Joint convergence and independence follow. Since \(B=A-J\) and \(J\) is tight under the bound, \(B/d\) has the same limit.

## Verification

The included standalone `checker.py` is a standard-library-only finite verifier; run `python3 checker.py`. It directly enumerates product collisions using independently implemented polynomial multiplication and Euclidean gcd, and checks every \((a,b)\) joint count for \(\mathbb F_2\) through \(d=4\), \(\mathbb F_3\) through \(d=3\), \(\mathbb F_4\) through \(d=2\), and \(\mathbb F_5\) through \(d=2\). The \(4\)-element field uses the relation \(z^2+z+1=0\). Exact rational computations check the total-variation inequality for five field orders and seven degree cutoffs; further exact-integer sums check the energy identity through \(d=100\). The recorded output is `checker_output.txt`. These tests are finite consistency checks, not proofs of the infinite claims; the algebraic and probabilistic arguments above supply those proofs.

## Relationship to prior work

Afifurrahman, *Statistics of divisor functions over function fields* (2026), Theorem 2.1, gives the scalar total multiplicative energy for exactly this monic bounded-degree collision model. Its Proposition 3.1 and formula (4.4) use coprime-factor parametrizations closely related to Step 1. Theorem 2.2 counts collisions with four prescribed factor degrees, while Section 7 stratifies a nonzero-shift problem by gcd factors. These are substantial precursors. The present result instead refines the **zero-shift** count by the *two gcd degrees*, then proves a quantitative joint limit with independent uniform and bilateral-geometric coordinates. That joint law and rate are not stated in the inspected paper; the total energy alone does not determine them. The source's parametrization makes the new refinement natural, and an earlier equivalent derivation remains a literature risk.

Earlier studies of polynomial divisor correlations (including Andrade–Bary-Soroker–Rudnick, 2014, and Yiasemides, 2024) address shifted products, prescribed total degree, or short-interval statistics rather than the present gcd-degree law for a bounded-degree zero-determinant ensemble.

## Limitations

The results require ordered nonzero **monic** factors. They do not include zero polynomial entries, different individual degree cutoffs, higher-order product collisions, or nonzero shifts. The exact joint enumeration is closely related to an established coprime parametrization, so its historical priority cannot be established from indexing alone. The total-variation upper bound is uniform but is not claimed to be optimal, and the continuum marginal limit is weak, not total-variation convergence.

## References

1. M. Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first posted October 8, 2026), especially Theorems 2.1–2.2, Proposition 3.1, equation (4.4), and Section 7. https://arxiv.org/abs/2610.11240
2. J. C. Andrade, L. Bary-Soroker and Z. Rudnick, *Shifted convolution and the Titchmarsh divisor problem over* \(\mathbb F_q[t]\), arXiv:1407.2076 (2014). https://arxiv.org/abs/1407.2076
3. M. Yiasemides, *The variance and correlations of the divisor function in* \(\mathbb F_q[T]\) *and Hankel matrices*, Research in the Mathematical Sciences 11 (2024), article 11. https://doi.org/10.1007/s40687-023-00418-7
