# A sharp midpoint-support obstruction to positivity of generalized Hilbert matrices

## Finding
Let \(\mu\) be any nonzero finite positive Borel measure on \((0,1)\), with compact support \(S\), invariant under reflection \(t\mapsto1-t\). Define the generalized Hilbert matrix on \(\ell^2(\mathbb N_0)\) by
\[
G^\mu_{n,k}=\binom{n+k}{k}\int_{(0,1)}(1-t)^n t^k\,d\mu(t),\qquad n,k\ge0.
\]
Suppose \(1/2\notin S\), and put \(s=\max(S\cap(0,1/2))\) and \(h=s(1-s)<1/4\). For integers \(m\to\infty\), set \(k_m=\lfloor sm\rfloor\), \(n_m=m-k_m\), and
\[
R_m=\frac{G^\mu_{n_m,k_m}}{\sqrt{G^\mu_{n_m,n_m}G^\mu_{k_m,k_m}}}.
\]
Then the following **exact exponential law** holds:
\[
\boxed{\displaystyle\lim_{m\to\infty}\frac{\log R_m}{m}=-\log(2\sqrt{s(1-s)})>0.}
\]
In particular, the bounded self-adjoint operator \(G^\mu\) is **not positive semidefinite**: for all sufficiently large \(m\), its principal two-coordinate determinant at \(\{n_m,k_m\}\) is negative. Therefore **a necessary condition for positivity among compactly supported reflection-symmetric measures is \(1/2\in S\)**.

For the symmetric two-point probability measure \(\mu_s=(\delta_s+\delta_{1-s})/2\), the law has the sharper equivalent
\[
\boxed{\displaystyle R_m\sim\frac{(2\sqrt{s(1-s)})^{-m}}{2\sqrt2\,[s(1-s)]^{1/4}}.}
\]
The support obstruction is sharp as a support-distance condition: for \(\mu=\delta_{1/2}\), the operator is positive semidefinite. This is **not** a sufficient-condition theorem for arbitrary measures whose support contains the midpoint.

## Assumptions and scope
Indices begin at zero. All measures are finite and positive; the main theorem requires compact support inside \((0,1)\), reflection invariance, and a support gap about \(1/2\). The operator acts on the complex Hilbert space \(\ell^2(\mathbb N_0)\). Positivity means \(\langle G^\mu x,x\rangle\ge0\) for every \(x\), rather than positivity of individual matrix entries. The logarithm is natural. The asymptotic is taken with the measure fixed, and \(n_m,k_m\to\infty\).

## Proof
**1. Bounded self-adjoint realization.** For an atomic kernel at parameter \(t\in(0,1)\), write \(B^t_{n,k}=\binom{n+k}{k}(1-t)^n t^k\). The negative-binomial series gives row sums \(\sum_k B^t_{n,k}=1/(1-t)\) and column sums \(\sum_n B^t_{n,k}=1/t\). The Schur test yields \(\|B^t\|_{2\to2}\le[t(1-t)]^{-1/2}\). Compact support inside \((0,1)\) makes the measure integral a bounded operator. Reflection invariance, together with \(B^{1-t}_{n,k}=B^t_{k,n}\), gives \(G^\mu=(G^\mu)^*\). Every displayed entry is strictly positive, because the measure is nonzero.

**2. A compact-support Laplace principle.** If \(\nu\) is a finite nonzero positive measure on a compact set \(S\), and real continuous \(f_m\to f\) uniformly on \(S\), then
\[
\lim_{m\to\infty}\frac1m\log\int_S e^{mf_m(t)}\,d\nu(t)=\max_{t\in S}f(t).
\]
For the upper bound use the total mass and uniform supremum. For the lower bound, choose a point maximizing \(f\) in the support, then a neighborhood of positive measure on which \(f\) is within an arbitrary \(\varepsilon>0\) of its maximum, and use uniform convergence. This argument includes measures with singular or purely atomic support.

**3. Diagonal asymptotics.** Reflection symmetry and the midpoint gap ensure \(s\in S\), \(0<s<1/2\), and \(\max_{S}t(1-t)=h=s(1-s)\). Since
\[
G^\mu_{j,j}=\binom{2j}{j}\int_S[t(1-t)]^j\,d\mu(t),
\]
Stirling's formula and Step 2 imply
\[
\lim_{j\to\infty}\frac1j\log G^\mu_{j,j}=\log(4h).
\]
With \(n_m/m\to1-s\) and \(k_m/m\to s\), this yields
\[
\lim_{m\to\infty}\frac1m\log\sqrt{G^\mu_{n_m,n_m}G^\mu_{k_m,k_m}}=\tfrac12\log(4h)=\log(2\sqrt h).
\]

**4. Off-diagonal asymptotics.** Let \(\alpha_m=n_m/m\to1-s\). Stirling gives \(m^{-1}\log\binom m{k_m}\to H(s)\), where \(H(u)=-u\log u-(1-u)\log(1-u)\). Step 2, applied to the continuous functions \(\alpha_m\log(1-t)+(1-\alpha_m)\log t\), shows
\[
\lim_{m\to\infty}\frac1m\log G^\mu_{n_m,k_m}
=H(s)+\max_{t\in S}\{(1-s)\log(1-t)+s\log t\}=0.
\]
Indeed, the expression inside the maximum plus \(H(s)\) is \(-D_{\mathrm{KL}}(\operatorname{Bern}(s)\|\operatorname{Bern}(t))\), which is never positive and vanishes at \(t=s\in S\). Subtracting the limit in Step 3 proves the boxed exponential law. Since that limit is strictly positive, \(R_m>1\) for all sufficiently large \(m\); hence
\[
G^\mu_{n_m,n_m}G^\mu_{k_m,k_m}-(G^\mu_{n_m,k_m})^2<0.
\]
A positive semidefinite matrix has nonnegative principal determinants of order two. This proves the claimed failure of positivity.

**5. Sharp prefactor for two atoms.** For \(\mu_s\), the diagonal is exactly \(G^{\mu_s}_{j,j}=\binom{2j}{j}h^j\), while
\[
G^{\mu_s}_{n,k}=\frac12\binom{n+k}{k}\bigl((1-s)^n s^k+s^n(1-s)^k\bigr).
\]
For \(n=n_m\), \(k=k_m\), the second parenthesized term divided by the first tends to zero exponentially, since \(n-k\sim(1-2s)m\). The local binomial Stirling formula gives \(\binom m{k_m}s^{k_m}(1-s)^{n_m}\sim(2\pi mh)^{-1/2}\); the central binomial estimate gives
\[
\sqrt{\binom{2n_m}{n_m}\binom{2k_m}{k_m}}\,h^{m/2}
\sim\frac{(2\sqrt h)^m}{\sqrt\pi\,m^{1/2}h^{1/4}}.
\]
Taking the quotient gives precisely \((2\sqrt2\,h^{1/4})^{-1}(2\sqrt h)^{-m}\).

**6. Positive midpoint boundary.** For \(\mu=\delta_{1/2}\), use \(\int_0^\infty e^{-u}u^{n+k}\,du=(n+k)!\) to obtain
\[
G^{\delta_{1/2}}_{n,k}=\binom{n+k}{k}2^{-(n+k)}
=\int_0^\infty e^{-u}\frac{(u/2)^n}{n!}\frac{(u/2)^k}{k!}\,du.
\]
This is a Gram matrix in \(L^2((0,\infty),e^{-u}du)\), hence positive semidefinite. Schur boundedness from Step 1 applies.

## Verification
The stand-alone standard-library script `check_minors.py` checks rational two-atom entries, exact negative principal determinants for \(s=1/4,1/3,2/5,9/20\), finite positive midpoint Gram determinants, and convergence of logarithmic ratios for selected rational parameters. Run `python check_minors.py` in the package directory. These tests are finite sanity checks; Steps 1--6 establish the infinite theorem for all allowed measures without extrapolation from calculations.

## Relationship to prior work
Athanasiou (2023) introduced and studied the same measure-induced generalized Hilbert matrix on \(\ell^p\), proving boundedness and norm results. Bellavita--Chalmoukis--Daskalogiannis--Stylogiannis (2023 preprint, 2024 journal) analyzed the corresponding Hardy-space operator, its adjoint and the rigidity of its Hankel form. Jin (2025 preprint, 2026 journal) established weighted-sequence-space boundedness and norm formulas. The inspected statements do not supply the midpoint-support positivity obstruction or the exact exponential two-coordinate violation. The known reflection-adjoint relation supplies a convenient self-adjoint setting but does not imply either positivity or indefiniteness.

## Limitations
The support-gap condition is necessary for positivity in this class, not a characterization when the midpoint lies in the support; singular measures accumulating there are not settled. Measures without compact support inside \((0,1)\) may require separate boundedness analysis. The two-atom prefactor does not extend unchanged to arbitrary measures, although the exact exponential rate does. The argument locates negative two-coordinate compressions and does not determine the full negative spectrum or its multiplicities. Priority remains subject to independent specialist comparison.

## References
1. N. Athanasiou, *On the boundedness and norm of certain generalized Hilbert operators in* \(\ell^p\), *Bull. Lond. Math. Soc.* **55** (2023), 2598--2610; first online July 5, 2023. DOI: `10.1112/blms.12882`. Full open article: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12882.
2. C. Bellavita, N. Chalmoukis, V. Daskalogiannis and G. Stylogiannis, *Generalized Hilbert operators arising from Hausdorff matrices*, arXiv:`2307.15334`, initial submission July 28, 2023; *Proc. Amer. Math. Soc.* **152** (2024), 4759--4773. https://arxiv.org/abs/2307.15334.
3. J. Jin, *Generalized Hilbert matrix operators acting on weighted sequence spaces*, arXiv:`2504.19743`, initially public April 2025; *Proc. Edinburgh Math. Soc.* **69** (2026), 1148--1167. https://arxiv.org/abs/2504.19743.
