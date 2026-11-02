# Reverse likelihood-ratio ordering of midpoint height and zero contacts in uniform Dyck excursions

## Finding

Let a Dyck excursion of semilength \(n\) be sampled uniformly, and let \(H\) be its altitude after exactly \(n\) steps. Let \(R\) be its number of strictly interior zero contacts (excluding times \(0\) and \(2n\)). For every \(n\ge 1\), the conditional mass kernel
\[
K_n(h,r)=\Pr(R=r\mid H=h)
\]
is reverse totally positive of order two: for any feasible \(h_1<h_2\) and integers \(r_1<r_2\),
\[
K_n(h_1,r_1)K_n(h_2,r_2)\le K_n(h_1,r_2)K_n(h_2,r_1).
\]
Equivalently, \(R\mid(H=h_2)\le_{\mathrm{lr}}R\mid(H=h_1)\), where \(\le_{\mathrm{lr}}\) denotes likelihood-ratio order. The stochastic ordering is strict between distinct feasible heights. For \(n\ge2\), every pair of nondecreasing real functions \(f,g\) obeys
\[
\operatorname{Cov}(f(H),g(R))\le0;
\]
in particular \(\operatorname{Cov}(H,R)<0\). This is a finite-sample result, not an asymptotic approximation.

## Assumptions and scope

A Dyck excursion has steps \(+1\) and \(-1\), starts and ends at height zero, and stays nonnegative throughout its \(2n\) steps. The midpoint height belongs to
\[
\mathcal H_n=\{h:0\le h\le n,\ h\equiv n\pmod 2\}.
\]
An interior zero contact is a time \(t\in\{1,\dots,2n-1\}\) at which the height is zero. All conditional distributions exist because every feasible midpoint height occurs with positive probability. A zero outside the support of a conditional mass function is interpreted literally as zero. The case \(n=1\) has a single path and only a vacuous ordering.

The conditional law is given explicitly. For feasible \(h>0\), put \(m=(n-h)/2\) and \(\ell=(n+h)/2\), and define
\[
b_{n,h}(j)=\frac{h+j}{\ell}\binom{n-j-1}{m-j},\qquad 0\le j\le m.
\]
For feasible \(h=0\), necessarily \(n=2m\), define
\[
b_{n,0}(j)=\frac{j+1}{m}\binom{n-j-2}{m-j-1},\qquad 0\le j\le m-1.
\]
Both expressions are nonnegative integers. Write \(F_{n,h}(z)=\sum_jb_{n,h}(j)z^j\), and let \(T_{n,h}=F_{n,h}(1)\). Then
\[
K_n(h,r)=
\begin{cases}
[z^r]F_{n,h}(z)^2/T_{n,h}^2,&h>0,\\
[z^{r-1}]F_{n,0}(z)^2/T_{n,0}^2,&h=0,
\end{cases}
\]
with out-of-range coefficient extraction interpreted as zero. In both cases \(T_{n,h}=\frac{h+1}{n+1}\binom{n+1}{m}\), the standard ballot count.

## Proof

**1. Count one half by its zero contacts.** Let \(C(x)=\sum_{j\ge0}C_jx^j\) be the Catalan series, satisfying \(C(x)=1+xC(x)^2\). A positive, completed primitive excursion has step-length generating series \(u^2C(u^2)\). A nonnegative prefix ending at positive height \(h\), without returning to zero after departure, has series \(u^hC(u^2)^h\): its unique last-passage decomposition contains \(h\) up-steps, each followed by a Dyck subpath. Thus a prefix of length \(n\) ending at \(h>0\) and returning to zero exactly \(j\) times has generating series \(u^{h+2j}C(u^2)^{h+j}\). The generalized Catalan coefficient identity
\[
[x^q]C(x)^p=\frac{p}{2q+p}\binom{2q+p}{q}\qquad(p\ge1,q\ge0)
\]
gives \(b_{n,h}(j)\) above. When \(h=0\), a prefix ending at zero with \(j\) returns strictly before its endpoint is a concatenation of \(j+1\) primitive excursions, with generating series \(u^{2(j+1)}C(u^2)^{j+1}\). The same coefficient formula gives \(b_{n,0}(j)\). Their sums are the ballot counts, as also follows by forgetting the return statistic.

**2. Log-concavity and adjacent likelihood ratios.** For \(h>0\), with \(m=(n-h)/2\), direct cancellation shows
\[
\frac{b_{n,h}(j+1)}{b_{n,h}(j)}=
\frac{h+j+1}{h+j}\frac{m-j}{n-j-1}
\]
throughout the interior support. Both factors are nonincreasing in \(j\); the first is strictly decreasing, and the second is nonincreasing because \(n-m-1\ge0\). Thus each positive sequence \(b_{n,h}\) is log-concave, with interval support. For \(h=0\), the analogous consecutive ratio is
\[
\frac{b_{n,0}(j+1)}{b_{n,0}(j)}=
\frac{j+2}{j+1}\frac{m-j-1}{n-j-2},
\]
which is likewise nonincreasing. Empty or singleton interiors require no test.

For feasible \(h>0\) with \(h+2\le n\), one has on the common support
\[
\frac{b_{n,h+2}(j)}{b_{n,h}(j)}=
\frac{h+j+2}{h+j}\frac{m-j}{\ell+1},
\]
which is strictly decreasing in \(j\). The distribution at the higher height also has no additional right support. For \(h=0\), writing \(n=2m\), direct cancellation instead gives
\[
\frac{b_{n,2}(j)}{b_{n,0}(j)}=
\frac{j+2}{j+1}\frac{n-j-1}{m+1},
\]
again strictly decreasing. After normalization, the half-prefix contact counts therefore decrease in likelihood-ratio order with every increase of midpoint height by two.

**3. Convolution preserves this order.** For a nonnegative log-concave finite sequence \(a\) with no internal zeros, the Toeplitz matrix \(T_{i,j}=a(j-i)\), with \(a(k)=0\) off support, is totally positive of order two. If \(q\le_{\mathrm{lr}}p\), multiplying the two-row likelihood-ratio matrix by \(T\) and using the two-by-two Cauchy--Binet identity proves \(q*a\le_{\mathrm{lr}}p*a\). Convolution also preserves log-concavity with interval support (apply the same matrix product to the Toeplitz kernels). Hence, for two log-concave half-prefix distributions \(p\) and \(q\) with \(q\le_{\mathrm{lr}}p\),
\[
q*q\le_{\mathrm{lr}}p*q\le_{\mathrm{lr}}p*p.
\]
No independence between two different midpoint-height conditionings is assumed; each convolution is within one conditional experiment.

**4. Midpoint splitting, including the zero boundary.** Conditioned on \(H=h\), the two halves of the Dyck excursion are independent uniform ballot prefixes from height zero to \(h\), after reversing the second half. When \(h>0\), the total number of interior zero contacts is the sum of the two half-prefix contact counts. Step 3 gives the claimed likelihood-ratio order for all consecutive positive feasible heights. When \(n\) is even and \(h=0\), the midpoint itself contributes one extra interior zero contact. Before adding this one, the two half-prefix counts are likelihood-ratio larger than those at \(h=2\), by steps 2--3. If \(Z\) has a log-concave interval-supported mass function, then \(Z\le_{\mathrm{lr}}Z+1\), because its adjacent mass ratios are nonincreasing. The convolution \(p*p\) is log-concave; therefore the extra midpoint contact can only strengthen the order. Transitivity proves the assertion for every pair of feasible heights.

The half-prefix ratio is strict where two indices are common, and otherwise the higher-height law loses a positive upper-tail value. The boundary \(h=0\) has an additional positive contact. Thus successive conditional laws are distinct and strictly stochastically ordered. The reverse order implies decreasing conditional expectations of all nondecreasing functions of \(R\). Applying the independent-copy covariance identity to the ordered heights gives the stated covariance inequality and strict negativity for \(\operatorname{Cov}(H,R)\) when \(n\ge2\).

## Verification

The standalone \(verify.py\) independently enumerates full Dyck paths (through semilength eleven), compares their exact midpoint-contact table against the half-prefix convolution formula, and separately checks the half-profile formula using a nonnegative-walk dynamic program. It verifies every two-by-two reverse-minor of the full conditional count matrices through semilength eighty and the exact binomial formulas and log-concavity through half-length one hundred fifty. All arithmetic is integer-exact; these finite tests corroborate but do not replace the all-size proof above. The reproduced verifier completed 1,430,938 assertions.

For illustration, at semilength \(n=4\), the unnormalized rows for midpoint heights \(h=0,2,4\) have respective interior-contact count polynomials \(z+2z^2+z^3\), \(4+4z+z^2\), and \(1\); their total counts \(4+9+1=14\) recover the Catalan number.

## Relationship to prior work

The Catalan/ballot decomposition and zero-contact enumeration belong to the classical lattice-path literature. Brak and Essam (2003) give contact-polynomial formulas and ballot decompositions, but the inspected statements concern contact enumeration and nonintersecting configurations, not a likelihood-ratio comparison across a fixed middle height. Khorunzhiy and Marckert (2009) study the same uniform Dyck-excursion measure and exponential moments of its maximum, with primary probability classification \(60C05\), but do not give this zero-contact conditional ordering. Mortimer and Prellberg (2012) study bijections preserving contacts and various peak statistics, rather than this conditional sign structure.

The new assertion is the reverse-total-positivity inequality for the complete midpoint-height/zero-contact joint law; it is not a claim to have discovered the constituent ballot counts or the general convolution closure of likelihood-ratio order.

## Limitations

This is specific to uniform nonnegative nearest-neighbor excursions and the exact midpoint. It does not assert the same order for drifted or differently weighted excursions, for arbitrary observation times, or for unconditioned signed bridges. The theorem gives an ordering rather than a closed scalar formula for every covariance. Relevant older local-time studies may contain implicit equivalent expressions; mathematical correctness does not establish definitive historical priority.

## References

- O. Khorunzhiy and J.-F. Marckert, *Uniform bounds for exponential moment of maximum of a Dyck path*, arXiv:0902.1229, first posted 2009-02-07; *Electronic Communications in Probability* 14 (2009), 327--333, DOI 10.1214/ECP.v14-1486.
- R. Brak and J. W. Essam, *Bicoloured Dyck paths and the contact polynomial for n non-intersecting paths in a half-plane lattice*, *Electronic Journal of Combinatorics* 10 (2003), R35, DOI 10.37236/1728.
- P. R. G. Mortimer and T. Prellberg, *A Bijection on Bilateral Dyck Paths*, arXiv:1208.3061, first posted 2012-08-15.
- E. Csáki and S. G. Mohanty, *Some joint distributions for conditional random walks*, *Canadian Journal of Statistics* 14 (1986), 19--28, DOI 10.2307/3315033 (abstract reviewed; full-text comparison unavailable).
- E. Csáki, *Some joint distributions in Bernoulli excursions*, *Journal of Applied Probability* 31A (1994), 239--250, DOI 10.2307/3214959 (abstract reviewed; full-text comparison unavailable).
