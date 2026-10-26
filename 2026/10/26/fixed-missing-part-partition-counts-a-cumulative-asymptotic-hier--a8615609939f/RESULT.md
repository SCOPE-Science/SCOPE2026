# Fixed-missing-part partition counts: a cumulative asymptotic hierarchy

## Finding
Let \(P(n,m)\) be the number of ordinary integer partitions of \(n\) in which exactly \(m\) positive integers strictly below the largest part do not occur as part sizes. The empty partition contributes \(P(0,0)=1\). For each fixed integer \(m\ge0\), define \(C_m(X)=\sum_{0\le n\le X}P(n,m)\). Then, as real \(X\to\infty\),
\[
C_m(X)\sim\frac{3^{1/4}}{2\pi\,m!}\left(\frac{2\sqrt3(1-\log2)}{\pi}\right)^m X^{m/2-1/4}\exp\left(\pi\sqrt{X/3}\right).
\]
Equivalently, for every fixed \(m\ge0\),
\[
\frac{C_m(X)}{C_0(X)}\sim\frac1{m!}\left(\frac{2\sqrt3(1-\log2)}{\pi}\right)^m X^{m/2}.
\]
This includes the gap-free case \(m=0\); the asymptotic is cumulative rather than pointwise.

## Assumptions and scope
A partition is a multiset of positive integer part sizes. For a nonempty partition with largest part \(L\), the missing count is the number of elements of \(\{1,\ldots,L-1\}\) having multiplicity zero. The parameter \(m\) is fixed before \(X\) tends to infinity. All logarithms are natural. We use the classical eta-product asymptotic and the sectorial cumulative version of Ingham's Tauberian theorem, with its complex-domain hypothesis.

## Proof
**1. Separate the distinct-parts factor.** Bhoria--Eyyunni--Santra give the exact bivariate generating series
\[
F(w,q)=\sum_{n,m\ge0}P(n,m)w^m q^n=\frac{((w-1)q;q)_\infty}{(wq;q)_\infty},\qquad |q|<1,
\]
where \((a;q)_\infty=\prod_{j\ge0}(1-aq^j)\). Put \(Q(q)=(-q;q)_\infty\). Extracting the factor at \(w=0\) and expanding the logarithm formally in \(w\),
\[
F(w,q)=Q(q)\exp\left(\sum_{r\ge1}\frac{w^r}{r}H_r(q)\right),\qquad
H_r(q)=\sum_{k\ge1}\left(q^{kr}-\frac{q^{kr}}{(1+q^k)^r}\right).
\]
Consequently, for fixed \(m\), the coefficient \(F_m(q)=[w^m]F(w,q)\) is \(Q(q)\) times a finite polynomial in \(H_1(q),\ldots,H_m(q)\), whose only term with \(m\) factors is \(H_1(q)^m/m!\).

**2. The leading singularity.** For \(q=e^{-t}\), \(t\downarrow0\),
\[
H_1(e^{-t})=\sum_{k\ge1}\frac{e^{-2kt}}{1+e^{-kt}}\sim\frac1t\int_0^\infty\frac{e^{-2u}}{1+e^{-u}}\,du=\frac{1-\log2}{t}.
\]
For each fixed \(r\ge1\), the geometric bounds \(\sum_{k\ge1}e^{-rkt}=O_r(t^{-1})\) give \(H_r(e^{-t})=O_r(t^{-1})\). Every other monomial in the coefficient of \(w^m\) contains at most \(m-1\) factors. Thus
\[
F_m(e^{-t})\sim \frac{(1-\log2)^m}{m!\sqrt2}\,t^{-m}\exp\left(\frac{\pi^2}{12t}\right),
\]
using the standard eta-product estimate \(Q(e^{-t})\sim2^{-1/2}\exp(\pi^2/(12t))\). For \(m=0\) the identity \(F_0=Q\) gives the same formula directly.

**3. Check the necessary complex bound.** Fix \(\Delta>0\) and let \(z=x+iy\) with \(x>0\), \(|y|\le\Delta x\), and \(x\to0\). A constant \(c_\Delta>0\) satisfies \(|1+e^{-kz}|\ge c_\Delta\) for all \(k\ge1\): when \(kx\le \min(1,\pi/(2\max(\Delta,1)))\), the argument \(|ky|\le\pi/2\) makes the real part of \(e^{-kz}\) nonnegative; when \(kx\) is larger, the reverse triangle inequality gives the fixed positive lower bound \(1-e^{-\min(1,\pi/(2\max(\Delta,1)))}\). Thus \(H_r(e^{-z})=O_{r,\Delta}(x^{-1})\). As \(x\asymp_\Delta|z|\), every fixed coefficient \(F_m(e^{-z})/Q(e^{-z})\) is \(O_{m,\Delta}(|z|^{-m})\). The eta modular transformation gives, uniformly on this sector,
\[
Q(e^{-z})=2^{-1/2}\exp\left(\frac{\pi^2}{12z}\right)(1+O_\Delta(|z|)),
\]
and therefore \(|F_m(e^{-z})|\ll_{m,\Delta}|z|^{-m}\exp(\pi^2/(12|z|))\). This is the essential complex-sector hypothesis of the cumulative Ingham theorem; the positive-real asymptotic by itself would not suffice.

**4. Apply the cumulative Tauberian theorem.** The coefficients \(P(n,m)\) are nonnegative. Theorem 1.1 of Bringmann--Jennings-Shaffer--Mahlburg, with \(\lambda=(1-\log2)^m/(m!\sqrt2)\), \(\beta=-m\), \(\alpha=0\), and \(\gamma=\pi^2/12\), gives
\[
C_m(X)\sim\frac{\lambda\gamma^{-m/2-1/4}}{2\sqrt\pi}\,X^{m/2-1/4}\exp(2\sqrt{\gamma X}).
\]
Simplifying the constants proves the displayed theorem.

## Verification
The accompanying standalone `verify.py` recomputes the bivariate product coefficients and independently enumerates small integer partitions, checking their missing-size counts; it also checks the claimed singular leading factor and cumulative ratio numerically at increasing cutoffs. These finite checks do not replace the infinite proof, which uses the corrected sectorial Tauberian theorem. The computation is reproducible in Python 3 without third-party packages.

## Relationship to prior work
Bhoria--Eyyunni--Santra established the bivariate product generating function and related exact identities for missing integers. Aniceto--Ballantine subsequently supplied combinatorial proofs of missing-integer identities. These results motivate the fixed-missing-count question, but the inspected materials do not provide this all-fixed-\(m\) cumulative asymptotic or its constant \(1-\log2\). The distinct-parts eta asymptotic and the corrected Ingham theorem are known inputs, not claimed as new.

## Limitations
The formula is proved only for each fixed \(m\); no estimate uniform in growing \(m\), pointwise formula for \(P(n,m)\), effective rate, or independent priority certification is claimed. An equivalent unindexed result or an implicit earlier Tauberian specialization remains possible.

## References
1. S. C. Bhoria, P. Eyyunni, S. Santra, *On the number of missing integers in partitions*, arXiv:2604.12557 (first posted 2026-04-14), https://arxiv.org/abs/2604.12557 .
2. J. Aniceto, C. Ballantine, *Identities involving the number of missing integers in partitions — combinatorial proofs*, arXiv:2608.00278 (2026), https://arxiv.org/abs/2608.00278 .
3. K. Bringmann, C. Jennings-Shaffer, K. Mahlburg, *On a Tauberian theorem of Ingham and Euler--Maclaurin summation*, The Ramanujan Journal 61 (2023), 55--86, https://doi.org/10.1007/s11139-020-00377-5 .
