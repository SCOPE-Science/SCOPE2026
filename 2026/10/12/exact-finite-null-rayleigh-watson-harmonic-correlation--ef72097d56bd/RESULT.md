# Exact finite-null Rayleigh–Watson harmonic correlation
## Finding
Let
\[
\Theta_1,\ldots,\Theta_n
\]
be independent and uniform on \([0,2\pi)\), with \(n\ge2\). For each integer \(k\ge1\), define the normalized harmonic energy
\[
Z_{n,k}
=
\frac1n\left|\sum_{j=1}^n e^{ik\Theta_j}\right|^2.
\]
The first harmonic \(Z_{n,1}\) is the usual Rayleigh statistic under the normalization whose null limit is exponential with mean one.

The harmonic energies have the exact finite-sample second-moment law
\[
\mathbb E Z_{n,k}=1,
\qquad
\operatorname{Var}(Z_{n,k})=\frac{n-1}{n},
\]
and, for distinct positive integers \(k\ne\ell\),
\[
\boxed{
\operatorname{Cov}(Z_{n,k},Z_{n,\ell})=0.
}
\]

Let \(F_n\) be the empirical distribution function of
\[
U_j=\frac{\Theta_j}{2\pi}\in[0,1),
\]
and define Watson's one-sample circular statistic by
\[
U_n^2
=
n\int_0^1
\left(
F_n(t)-t-\int_0^1(F_n(s)-s)\,ds
\right)^2dt.
\]
Then
\[
\boxed{
U_n^2
=
\frac1{2\pi^2}\sum_{k=1}^{\infty}\frac{Z_{n,k}}{k^2}.
}
\]
Consequently
\[
\mathbb E U_n^2=\frac1{12},
\qquad
\boxed{
\operatorname{Var}(U_n^2)=\frac{n-1}{360n}.
}
\]
For every \(j\ge1\),
\[
\boxed{
\operatorname{Cov}(Z_{n,j},U_n^2)
=
\frac{n-1}{2\pi^2 n j^2}
}
\]
and
\[
\boxed{
\operatorname{Corr}(Z_{n,j},U_n^2)
=
\frac{3\sqrt{10}}{\pi^2j^2}.
}
\]

In particular,
\[
\boxed{
\operatorname{Corr}(Z_{n,1},U_n^2)
=
\frac{3\sqrt{10}}{\pi^2}
}
\]
for every \(n\ge2\). Numerically this is about \(0.9612\), and
\[
\operatorname{Corr}(Z_{n,1},U_n^2)^2
=
\frac{90}{\pi^4}.
\]
Thus about \(92.4\%\) of the null variance of Watson's statistic lies in the first harmonic in the exact \(L^2\) projection sense, uniformly in sample size.

More precisely,
\[
U_n^2-\frac1{12}
=
\frac{Z_{n,1}-1}{2\pi^2}
+
V_n,
\]
where
\[
V_n
=
\frac1{2\pi^2}
\sum_{k=2}^{\infty}
\frac{Z_{n,k}-1}{k^2},
\]
\[
\operatorname{Cov}(Z_{n,1},V_n)=0,
\]
and
\[
\operatorname{Var}(V_n)
=
\frac{n-1}{4\pi^4n}
\left(\frac{\pi^4}{90}-1\right).
\]
No independence of the finite-sample harmonic energies is claimed.

## Assumptions and scope
The null distribution is exactly circular uniformity, and the observations are independent. The result is finite-sample and holds for every \(n\ge2\).

The normalization of the Rayleigh statistic is \(Z_{n,1}\). Some references use \(2Z_{n,1}\); multiplying one statistic by a positive constant does not change the correlation.

The statement concerns second moments and \(L^2\) orthogonality. Distinct finite-sample harmonic energies need not be independent.

## Proof
Put
\[
\xi_r=e^{i\Theta_r}
\]
and
\[
A_k=\left|\sum_{r=1}^n\xi_r^k\right|^2.
\]
Then
\[
A_k
=
\sum_{a,b=1}^n \xi_a^k\xi_b^{-k}.
\]
Uniformity gives
\[
\mathbb E \xi_r^q=0
\]
for every nonzero integer \(q\). Hence
\[
\mathbb E A_k=n.
\]

For \(k\ne\ell\), expand
\[
\mathbb E[A_kA_\ell].
\]
A term indexed by \(a,b,c,d\) can have nonzero expectation only if, for each sample index appearing among \(a,b,c,d\), the sum of its assigned frequencies from
\[
k,-k,\ell,-\ell
\]
is zero. Because \(k\) and \(\ell\) are distinct positive integers and each signed frequency occurs once, this forces \(k\) to pair with \(-k\) and \(\ell\) to pair with \(-\ell\). There are exactly \(n^2\) such assignments, including the \(n\) cases where both pairs use the same sample index. Therefore
\[
\mathbb E[A_kA_\ell]=n^2
\]
and
\[
\operatorname{Cov}(Z_{n,k},Z_{n,\ell})=0.
\]

For \(k=\ell\), the two positive and two negative copies can be paired in two ways. Each pairing contributes \(n^2\) assignments, while their intersection consists of the \(n\) all-equal assignments. Thus
\[
\mathbb E A_k^2=2n^2-n.
\]
It follows that
\[
\operatorname{Var}(A_k)=n(n-1)
\]
and
\[
\operatorname{Var}(Z_{n,k})=\frac{n-1}{n}.
\]

Now define
\[
G_n(t)
=
F_n(t)-t-\int_0^1(F_n(s)-s)\,ds.
\]
The function \(G_n\) has mean zero and matching endpoint values. For every nonzero integer \(k\), distributional integration by parts gives its Fourier coefficient
\[
\widehat G_n(k)
=
\frac1{2\pi i k n}
\sum_{r=1}^n e^{-2\pi i kU_r}.
\]
Parseval's identity therefore yields
\[
n\int_0^1G_n(t)^2dt
=
\frac1{2\pi^2n}
\sum_{k=1}^{\infty}
\frac{\left|\sum_r e^{2\pi i kU_r}\right|^2}{k^2},
\]
which is exactly
\[
U_n^2
=
\frac1{2\pi^2}
\sum_{k=1}^{\infty}\frac{Z_{n,k}}{k^2}.
\]

Because
\[
\sum_{k\ge1}\frac1{k^4}<\infty
\]
and the harmonic variances are uniformly bounded, the centered series converges in \(L^2\). Pairwise orthogonality then gives
\[
\operatorname{Var}(U_n^2)
=
\frac1{4\pi^4}
\frac{n-1}{n}
\sum_{k=1}^{\infty}\frac1{k^4}.
\]
Using
\[
\sum_{k=1}^{\infty}\frac1{k^2}=\frac{\pi^2}{6},
\qquad
\sum_{k=1}^{\infty}\frac1{k^4}=\frac{\pi^4}{90},
\]
proves the mean and variance formulas.

Only the \(j\)-th harmonic survives in the covariance with \(Z_{n,j}\), so
\[
\operatorname{Cov}(Z_{n,j},U_n^2)
=
\frac1{2\pi^2j^2}\frac{n-1}{n}.
\]
Dividing by the exact variances gives
\[
\operatorname{Corr}(Z_{n,j},U_n^2)
=
\frac{3\sqrt{10}}{\pi^2j^2}.
\]
Separating the \(j=1\) term proves the final orthogonal decomposition.

## Verification
The accompanying `checker.py` gives two independent exact finite checks.

First, it enumerates all assignments of the four harmonic frequencies to sample indices and verifies the mixed fourth-moment counts for many \(n,k,\ell\), including commensurate frequencies such as \(\ell=2k\). This directly checks the finite orthogonality mechanism.

Second, it checks the Fourier representation without truncating an infinite Fourier series. The classical Bernoulli identity
\[
\sum_{k=1}^{\infty}\frac{\cos(2\pi kx)}{k^2}
=
\pi^2\left(\{x\}^2-\{x\}+\frac16\right)
\]
turns the harmonic representation into a finite pairwise kernel. For deterministic rational samples, the checker evaluates this kernel with exact rational arithmetic and compares it to the usual ordered-sample Watson formula.

The universal theorem is supplied by the proof; the finite checks are supplementary.

## Relationship to prior work
Watson introduced the circular goodness-of-fit statistic now bearing his name. Later Sobolev formulations place Watson and Rayleigh in a common harmonic family: Watson gives weight \(k^{-2}\) to the \(k\)-th circular harmonic, while Rayleigh keeps only the first harmonic.

A complete modern treatment of these Sobolev tests gives precisely these harmonic representations and states asymptotic independence for fixed distinct harmonic components under circular uniformity. The finite-sample result above is stronger at the second-moment level: the harmonic energies are exactly uncorrelated for every \(n\), which makes the Rayleigh–Watson correlation constant exact and sample-size invariant.

Power studies emphasize the complementary roles of the two procedures: Rayleigh is strongest for simple unimodal departures, while omnibus procedures such as Watson retain sensitivity to higher harmonics and multimodal alternatives. The orthogonal decomposition quantifies the null redundancy while displaying the exact residual higher-harmonic variance.

## Limitations
The exact orthogonality uses the circular uniform null and integer Fourier harmonics. It does not extend automatically to nonuniform nulls, estimated nuisance parameters, axial transformations with data-dependent choices, or finite-sample independence.

The original Watson article was available only through abstract and bibliographic material in the comparison performed here. An equivalent finite mixed-moment identity in older circular-statistics literature therefore remains a specific residual originality risk.

## References
1. G. S. Watson, “Goodness-of-fit tests on a circle,” *Biometrika* 48 (1961), 109–114. DOI: 10.1093/biomet/48.1-2.109.
2. S. Rao Jammalamadaka, S. G. Meintanis, and T. Verdebout, “On Sobolev tests of uniformity on the circle with an extension to the sphere,” *Bernoulli* 26 (2020), 2226–2252. DOI: 10.3150/19-BEJ1191.
3. J.-R. Pycke, “Some tests for uniformity of circular distributions powerful against multimodal alternatives,” *The Canadian Journal of Statistics* 38 (2010), 80–96. DOI: 10.1002/cjs.10048.
