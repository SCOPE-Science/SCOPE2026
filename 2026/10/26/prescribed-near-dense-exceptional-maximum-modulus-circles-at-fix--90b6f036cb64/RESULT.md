# Prescribed near-dense exceptional maximum-modulus circles at fixed Taylor gap

## Finding

For an entire nonmonomial function \(f\), let \(M_f(r)=\max_{|z|=r}|f(z)|\), let \(\nu_f(r)\) count the points attaining this maximum, and let \(E_f=\{r>0:\nu_f(r)>2\}\). The bound of two corresponds to the first nonconstant Taylor coefficient occurring at degree one.

**Prescribed-circle theorem.** Fix any integer \(n\ge3\). Let \((s_j)_{j\ge1}\) be any strictly increasing sequence of positive real numbers tending to infinity and satisfying \(\sum_{j=1}^\infty s_j^{-1}<\infty\). Then there is an explicit entire function \(f\) such that \(f(0)=1\), \(f'(0)\ne0\), its order is exactly \(n\) and its exponential type at order \(n\) is exactly one, and, for **every** \(j\ge1\),
\[
\{z:|z|=s_j^{1/n},\ |f(z)|=M_f(s_j^{1/n})\}
=\{s_j^{1/n}e^{2\pi i m/n}:0\le m<n\}.
\]
In particular, \(\nu_f(s_j^{1/n})=n>2\) simultaneously on all prescribed circles. Here exponential type one means
\[\limsup_{r\to\infty}\frac{\log M_f(r)}{r^n}=1.\]

**Quantitative consequence.** For every integer \(n\ge3\), one may choose such an \(f\) and a constant \(c_n>0\) for which
\[
\#\bigl(E_f\cap[1,R]\bigr)\ge c_n\frac{R^n}{(\log R)^2}
\]
for all sufficiently large \(R\). The right side counts distinct exceptional radii, not multiplicities of maximum points.

## Assumptions and scope

The prescribed sequence must be strictly increasing and reciprocal-summable; no assumption of geometric separation is made. The function is complex entire, not required to be zero-free or to have bounded singular values. The conclusion concerns exactly the stated circles, not the total list of exceptional radii, and \(n\) is a fixed finite integer. The growth order and normal exponential type are with respect to the usual maximum modulus.

## Proof

**1. Canonical product and its growth.** Define
\[
G(w)=\prod_{j=1}^\infty(1-w/s_j)^2,\qquad
H(T)=\prod_{j=1}^\infty(1+T/s_j)\quad(T\ge0).
\]
Reciprocal summability gives compact-uniform convergence of the product for \(G\), and convergence of \(H(T)\) for every finite \(T\). In particular \(G\) is entire, \(G(0)=1\), and \(|G(w)|\le H(|w|)^2\).

One has \(\log H(T)=o(T)\) as \(T\to\infty\). Indeed,
\[
\frac{\log H(T)}T=\sum_{j\ge1}\frac{\log(1+T/s_j)}T,
\quad 0\le\frac{\log(1+T/s_j)}T\le\frac1{s_j},
\]
and each summand tends to zero. The convergent dominating series permits passage to the limit. Thus \(H(T)^2=e^{o(T)}\).

**2. Uniform preservation of the maxima on every prescribed circle.** Put \(R_j=s_j^{1/n}\), and define
\[
B_j=R_j(2/s_j+4)e^{-s_j}H(s_j)^2,
\qquad B=\sup_{j\ge1}B_j.
\]
Because \(s_j\to\infty\), \(H(s_j)^2=e^{o(s_j)}\), and \(R_j(2/s_j+4)\) grows subexponentially, \(B_j\to0\). Consequently \(0<B<\infty\). Fix, for definiteness, the positive scalar
\[\varepsilon=\frac1{2(1+B)}\]
and define
\[f(z)=e^{z^n}+\varepsilon zG(z^n).\]

Fix \(j\) and put \(s=s_j\), \(R=R_j\), and \(w=z^n\) for \(|z|=R\). Then \(|w|=s\). Since \(|w-s|^2=2s(s-\operatorname{Re}w)\), with \(u=s-\operatorname{Re}w\ge0\), the elementary bound \(1-e^{-u}\ge u/(1+u)\) gives
\[
e^s-|e^w|=e^s(1-e^{-u})
\ge\frac{e^s|w-s|^2}{2s+|w-s|^2}
\ge\frac{e^s|w-s|^2}{2s+4s^2}.
\]
Here the last inequality uses \(|w-s|\le2s\). Because \(G(w)=(1-w/s)^2\prod_{\ell\ne j}(1-w/s_\ell)^2\),
\[
|\varepsilon zG(w)|\le\varepsilon R\frac{|w-s|^2}{s^2}H(s)^2
\le\varepsilon B_j\bigl(e^s-|e^w|\bigr).
\]
Our choice of \(\varepsilon\) ensures \(\varepsilon B_j<1/2\). If \(w\ne s\), then \(u>0\), and the triangle inequality yields the **strict** bound
\[
|f(z)|\le|e^w|+|\varepsilon zG(w)|
<e^s.
\]
If \(w=s\), the double zero of \(G\) makes the perturbation vanish and \(f(z)=e^s\). On \(|z|=R\), precisely \(n\) different roots solve \(z^n=s\). Hence they, and no other points, are the global maximizers of \(|f|\) on that circle. This proves the exact prescribed-circle assertion for all \(j\) with one common \(\varepsilon\).

**3. Taylor gap, order, and type.** Since \(n\ge3\) and \(G(0)=1\), \(f(z)=1+\varepsilon z+O(z^n)\) as \(z\to0\), so its first positive Taylor exponent is one. For every \(r\ge0\), the product bound gives
\[
M_f(r)\le e^{r^n}+\varepsilon rH(r^n)^2
=e^{r^n}+\varepsilon r e^{o(r^n)}.
\]
It follows that \(\limsup_{r\to\infty}r^{-n}\log M_f(r)\le1\). Along \(R_j\to\infty\), the maximum just proved is exactly \(e^{s_j}=e^{R_j^n}\); thus the same limsup is at least one. Its equality to one establishes order exactly \(n\) and exponential type exactly one. (For order, take logarithms again in the usual definition.)

**4. Near-power number of exceptional circles.** Take \(s_j=(j+1)[\log(j+2)]^2\) for \(j\ge1\). This sequence is strictly increasing and \(\sum_j s_j^{-1}<\infty\) by the integral test. If \(R\) is sufficiently large and \(1\le j\le\lfloor R^n/(16n^2(\log R)^2)\rfloor\), then \(\log(j+2)\le2n\log R\), and therefore \(s_j\le R^n\) once \(R\) is large enough (the fixed additive constants are harmless). Every such \(j\) yields a distinct exceptional radius \(s_j^{1/n}\le R\). This proves the claimed lower bound for a positive \(c_n\), for example any fixed sufficiently small multiple of \(1/n^2\). \(\square\)

## Verification

All estimates are analytic. In particular, the decisive inequality holds uniformly in the angular variable and uniformly over all prescribed indices: \(\varepsilon B_j<1/2\). The series bound \(\log H(T)=o(T)\) is proved by domination by the convergent reciprocal series, not by a truncation. The number of maximizers is exactly the number of roots of \(z^n=s_j\), and order/type are established by matching upper bounds with values on infinitely many radii. A separate elementary computational check of finite approximations may illustrate but is not needed for, or substituted for, the proof.

## Relationship to prior work

Li [1] proves that an entire nonmonomial function with first nonconstant Taylor exponent \(k\) has at most \(2k\) maximum-modulus points outside a locally finite family of circles. The construction above concerns the size, prescribed placement, and density of that permitted exceptional family when \(k=1\), not a counterexample to local finiteness. Li's sharpness example concerns attaining the baseline \(2k\), not an infinite prescribed family above it.

Pardo-Simón and Sixsmith [2] prove the existence of a finite-order entire function with unbounded maximum-point counts, and an interpolation theorem for single maximum points on pairwise distinct circles (with a geometric-separation condition in its finite-order clause). Thus **neither mere infinitude of exceptional circles nor existence of finite-order examples is claimed as new**. Their stated theorems do not imply exact simultaneous \(n\)-point maxima on an arbitrary reciprocal-summable family of circles, nor the near-power counting bound with first Taylor gap one and exact order/type. Their full discussion uses a tract construction with a different objective.

The earlier polynomial paper [3] prescribes finitely many discontinuity/singleton radii using perturbations involving factors with double zeros. It is an important antecedent for finite prescribed-circle methods, but a polynomial cannot realize infinitely many distinct exceptional radii. The present conclusion employs an infinite canonical product and a uniform, all-radii gap estimate to obtain an infinite prescription with growth control. No claim is made to priority for the generic idea of double-zero perturbations.

## Limitations

The reciprocal-summability condition is sufficient, not asserted necessary. The construction does not classify other maximum points on other radii, optimize the possible density, control membership in the Eremenko–Lyubich class, or show that the exponent \(n\) is minimal for an \(n\)-point prescription. No independent audit or exhaustive historical priority certification has been performed. Related unindexed entire-function constructions may entail overlapping special cases.

## References

[1] Yunpeng Li, *Maximum-modulus points on concentric circles*, arXiv:2610.15067v1 (first publicly posted 2026-10-10); expanded v2 posted 2026-10-14. https://arxiv.org/abs/2610.15067 .

[2] Leticia Pardo-Simón and David J. Sixsmith, *A finite-order answer to a problem of Erdős on maximum modulus points*, arXiv:2607.09462v1 (2026-07-10). https://arxiv.org/abs/2607.09462 .

[3] Leticia Pardo-Simón and David J. Sixsmith, *The maximum modulus set of a polynomial*, arXiv:2007.07529v1 (2020-07-15). https://arxiv.org/abs/2007.07529 .
