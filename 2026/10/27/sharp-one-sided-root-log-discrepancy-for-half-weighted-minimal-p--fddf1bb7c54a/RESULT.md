# Sharp one-sided root-log discrepancy for half-weighted minimal-power divisor sums

## Finding
For an integer \(r\ge 2\), define the minimal \(r\)-th-power root \(M_r(n)=\min\{m\ge1:n\mid m^r\}\), the divisor-counting function \(\tau\), and the number \(\omega(n)\) of distinct prime factors. Put
\[
f_r(n)=\frac{\tau(M_r(n))}{2^{\omega(n)}},\qquad S_r(X)=\sum_{n\le X}f_r(n).
\]
Define the strictly positive convergent product
\[
C_r=\prod_p\left(1+\frac{1}{2p^{r+1}(1-p^{-r})}\right)
=\zeta(r)\prod_p\left(1-p^{-r}+\frac1{2p^{r+1}}\right).
\]
Set \(k=r+1\) and
\[
\kappa_r=\sqrt{\frac{k}{\pi}}\prod_p
\left(1-\frac1p\right)^{1/2}
\left(1+\frac{1}{2p(1-p^{-r/k})}\right)>0.
\]
The product for \(\kappa_r\) converges absolutely after pairing its displayed local factors. The signed discrepancy \(E_r(X)=C_rX-S_r(X)\) is strictly positive for every real \(X\ge1\) and satisfies
\[
\frac{\kappa_r}{r}\ \le\ \liminf_{X\to\infty}\frac{E_r(X)\sqrt{\log X}}{X^{1/(r+1)}}
\ \le\ \limsup_{X\to\infty}\frac{E_r(X)\sqrt{\log X}}{X^{1/(r+1)}}
\ \le\ \frac{(r+1)\kappa_r}{r}.
\]
In particular,
\[
S_r(X)=C_rX-\Theta_r\left(\frac{X^{1/(r+1)}}{\sqrt{\log X}}\right).
\]
The \(\Theta\) statement is a positive two-sided order estimate, **not** a claim that the normalized error has a limit.

## Assumptions and scope
All sums are over positive integers, \(X\ge1\) is real, and \(r\ge2\) is a fixed integer. The expression \(\Theta_r\) permits positive constants depending on \(r\). Prime products extend over all rational primes. This is specifically the half-weight \(2^{-\omega(n)}\), not a statement for every real weight.

## Proof
**A sparse nonnegative convolution.** At a prime power, \(M_r(p^a)=p^{\lceil a/r\rceil}\), so \(f_r(p^a)=(\lceil a/r\rceil+1)/2\) for \(a\ge1\), and \(f_r(1)=1\). Let \(b_r\) be multiplicative with \(b_r(1)=1\) and
\[
b_r(p^a)=\begin{cases}
\frac12,&a=jr+1\text{ for an integer }j\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
For every \(a\ge1\),
\[
\sum_{j=0}^{a}b_r(p^j)=1+\frac12\left\lfloor\frac{a-1}{r}\right\rfloor
=\frac{\lceil a/r\rceil+1}{2}.
\]
Thus, exactly and pointwise, \(f_r=\mathbf1*b_r\) under Dirichlet convolution. The support of \(b_r\), apart from \(1\), consists of integers each of whose prime exponents is at least \(r+1\). Its Dirichlet series is
\[
G_r(s)=\sum_{d\ge1}\frac{b_r(d)}{d^s}
=\prod_p\left(1+\frac{p^{-(r+1)s}}{2(1-p^{-rs})}\right)
\quad(\Re s>1/(r+1)).
\]
In particular \(C_r=G_r(1)<\infty\), with the displayed product identities following by multiplying each local factor by \((1-p^{-r})/(1-p^{-r})\).

**Sharp size of the sparse kernel.** Write \(k=r+1\), \(\alpha=1/k\), and
\[
H_r(s)=\prod_p\left(1-p^{-ks}\right)^{1/2}
\left(1+\frac{p^{-ks}}{2(1-p^{-rs})}\right).
\]
Locally \(H_{r,p}(s)=1+O_r(p^{-(2r+1)\Re s}+p^{-2k\Re s})\). The same bound holds for the sum of the absolute values of the nonconstant local Dirichlet coefficients, uniformly on every half-plane \(\Re s\ge\sigma>1/(2r+1)\). Hence \(H_r(s)\) is represented by an absolutely convergent Dirichlet series in this half-plane. Moreover
\[
G_r(s)=\zeta(ks)^{1/2}H_r(s),\quad
H_r(\alpha)=\prod_p\left(1-p^{-1}\right)^{1/2}
\left(1+\frac{1}{2p(1-p^{-r/k})}\right)>0.
\]
Let \(u_{1/2}(m)\) be the nonnegative Dirichlet coefficients of \(\zeta(s)^{1/2}\). The classical Selberg--Delange estimate gives
\[
\sum_{m\le Y}u_{1/2}(m)\sim\frac{Y}{\sqrt{\pi\log Y}}.
\]
The absolute convergence just proved allows convolution transfer, because the coefficients of \(H_r\) are absolutely summable after weighting by \(d^{-\sigma}\) for some \(\sigma<\alpha\). Equivalently, apply the same Selberg--Delange estimate at the rescaled variable \(ks\). It follows that
\[
B_r(X):=\sum_{d\le X}b_r(d)
\sim\kappa_r\frac{X^{\alpha}}{\sqrt{\log X}},\qquad
\kappa_r=\frac{\sqrt{k}\,H_r(\alpha)}{\sqrt\pi}.
\]
For completeness, the transfer follows by splitting the convolution at \(d\le\exp(\sqrt{\log X})\): the classical estimate is uniform there with \(\log(X/d)=\log X+o(\log X)\), while the remaining coefficients contribute \(o(X^\alpha/\sqrt{\log X})\) by absolute convergence at \(\sigma<\alpha\) and the bound \(\sum_{m^k\le Y}u_{1/2}(m)\le Y^\alpha\).

**One-sided error and sharp exponent.** The convolution identity gives, exactly,
\[
S_r(X)=\sum_{d\le X}b_r(d)\left\lfloor\frac Xd\right\rfloor.
\]
Consequently
\[
E_r(X)=\sum_{d\le X}b_r(d)\left\{\frac Xd\right\}
+X\sum_{d>X}\frac{b_r(d)}d.
\]
Both terms are nonnegative; the second is strictly positive since infinitely many prime powers support \(b_r\). Partial summation from the estimate for \(B_r\) gives
\[
X\sum_{d>X}\frac{b_r(d)}d
\sim\frac{\alpha\kappa_r}{1-\alpha}
\frac{X^\alpha}{\sqrt{\log X}}
=\frac{\kappa_r}{r}\frac{X^\alpha}{\sqrt{\log X}}.
\]
Using \(0\le\{X/d\}<1\) bounds the first term between \(0\) and \(B_r(X)\). Therefore
\[
X\sum_{d>X}\frac{b_r(d)}d\le E_r(X)
\le B_r(X)+X\sum_{d>X}\frac{b_r(d)}d,
\]
which gives both explicit liminf/limsup inequalities and the claimed two-sided sharp order. The same reasoning proves strict positivity at every real \(X\ge1\).

## Verification
The standalone Python script `verify.py` performs 10,000 exact-rational coefficient comparisons between direct prime-factor formulas and independent divisor-convolution sums for \(r=2,3,4,5\), together with 32 complete finite summatory comparisons and 100 local-Euler coefficient checks. Run `python3 verify.py`; expected final line begins `VERIFY_OK`. Its checks are finite and do not establish the infinite Selberg--Delange or partial-summation steps.

## Relationship to prior work
M. Bouderbala, *On the Mean Value of a Weighted Composite Arithmetic Function* (2026), introduces exactly \(D_k(M_r(n))\) and obtains the mean \(C_rX+O_r(X/\log X)\) at \(k=2\); its Euler product supplies the input local factor. The present result uses that setting, but asserts a new signed, two-sided **sharp-order** discrepancy of magnitude \(X^{1/(r+1)}/\sqrt{\log X}\), not merely existence or computation of the leading constant. The difference relies on a further sparse convolution and the nonnegative fractional-part error, followed by a second half-order zeta singularity.

The author's earlier paper *On a sum of a multiplicative function linked to the divisor function over the set of integers B-multiple of 5* concerns \(\tau(n)/2^{\omega(n)}\) on a decimal-defined subset, rather than the minimal-power composition. Classical Selberg--Delange theory supplies the analytic transfer input; no novelty is claimed for that general method.

## Limitations
The inequalities do not determine a limiting constant for the normalized discrepancy, nor treat weights other than \(2^{-\omega(n)}\). The new argument depends on established Selberg--Delange asymptotics; the finite verifier cannot certify those infinite inputs. Bibliographic priority remains subject to independent checking of specialized mean-value literature: an unpublished or unindexed equivalent sharp-error result might exist.

## References
- Mihoub Bouderbala, *On the Mean Value of a Weighted Composite Arithmetic Function*, arXiv:2602.16027, first submitted 2026-02-17, https://arxiv.org/abs/2602.16027 .
- Mihoub Bouderbala, *On a sum of a multiplicative function linked to the divisor function over the set of integers B-multiple of 5*, Communications in Mathematics 31 (2023), 369--374, https://cm.episciences.org/10467 .
- Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, standard Selberg--Delange estimate for Dirichlet coefficients of \(\zeta(s)^z\).
