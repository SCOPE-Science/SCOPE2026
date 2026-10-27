# First Fefferman–Szegő zero transition for quartic eggs in complex dimension \(11\)

## Finding

For every integer \(n\ge 2\), let
\[
E_n=\{(z,w)\in\mathbb C^{n-1}\times\mathbb C:\ \|z\|^2+|w|^4<1\},
\]
and let \(S_n\) be its Fefferman–Szegő kernel, defined using the Fefferman boundary density of \(\rho=\|z\|^2+|w|^4-1\) and the closed holomorphic-polynomial subspace of boundary \(L^2\). Multiplication of the density by any positive constant leaves kernel zeros unchanged.

**Theorem (sharp first-dimension threshold).** The kernel \(S_n\) has no zeros on \(E_n\times E_n\) for every integer \(2\le n\le10\). For \(n=11\), the kernel has zeros, and its associated one-variable numerator has exactly two zeros in the open unit disk, both simple, nonreal and complex conjugate. Each is attained as an actual kernel zero for two points of \(E_{11}\). No conclusion about higher dimensions is asserted.

The critical roots are approximately \(0.539048877688\pm0.817441544338i\), each of modulus approximately \(0.9791753525\). All zero counts are proved by exact rational arithmetic rather than numerical root searches.

## Assumptions and scope

Set \(k=n-1\), \(\mu=(n+2)/(2(n+1))\) and \((x)_k=\prod_{j=0}^{k-1}(x+j)\). The normalized Fefferman surface density is proportional to \(M(\rho)^{1/(n+1)}dS/|\nabla\rho|\), where \(M(\rho)\) is Fefferman's bordered complex-Hessian determinant. On the boundary of this egg, \(M(\rho)=4|w|^2\). This density may vanish on the weakly pseudoconvex boundary locus; the Hardy space is the closure of holomorphic polynomials in the corresponding boundary \(L^2\) space.

Define the rational polynomial
\[
P_n(U)=(1-U)^n\sum_{b=0}^\infty (\mu+b/2)_k U^b,
\qquad |U|<1.
\]
It has degree at most \(k\) because its coefficient sequence is a degree-\(k\) polynomial in \(b\). The theorem counts all kernel zero fibers in \(U\), including multiplicity, only for the finite complete dimension range \(2\le n\le11\).

## Proof

**1. Reconstruct the normalized monomial expansion.** Integration over the level hypersurface, using \(u=|w|^4\), gives, for \(\alpha\in\mathbb N^{k}\) and \(b\in\mathbb N\),
\[
\|z^\alpha w^b\|^2=C_n\alpha!\,
\frac{\Gamma(\mu+b/2)}{\Gamma(\mu+b/2+k+|\alpha|)}.
\]
Indeed \(M(\rho)^{1/(n+1)}\) contributes \(u^{1/(2(n+1))}\), the polar coarea variable contributes \(u^{-1/2}\), and the \(w\)-monomial contributes \(u^{b/2}\); therefore the remaining beta-integral has exponent \(u^{\mu+b/2-1}(1-u)^{k+|\alpha|-1}\). Orthogonality of monomials and the multinomial identity imply
\[
S_n((z,w),(\zeta,\eta))=C'_n(1-\langle z,\zeta\rangle)^{-k-\mu}
\sum_{b\ge0}(\mu+b/2)_k U^b,
\]
where
\[
U=\frac{w\overline\eta}{(1-\langle z,\zeta\rangle)^{1/2}}.
\]
The fractional power is the analytic principal branch. The Cauchy–Schwarz estimate
\[
|1-\langle z,\zeta\rangle|^2\ge(1-\|z\|^2)(1-\|\zeta\|^2)
\]
ensures \(|U|<1\). Thus
\[
S_n=C'_n(1-\langle z,\zeta\rangle)^{-k-\mu}\frac{P_n(U)}{(1-U)^n}.
\]
All prefactors and denominators are nonzero in the domain. Conversely any \(u\in\mathbb D\) is attained as \(U\) with \(z=\zeta=0\) and \(w\overline\eta=u\): choose \(|w|=|\eta|=\sqrt{|u|}<1\) and suitable phases. Hence kernel zeros correspond *exactly* to disk zeros of \(P_n\).

**2. Compute the numerator without truncation.** For \(0\le j\le k\),
\[
[U^j]P_n(U)=c_{n,j}=
\sum_{\ell=0}^j(-1)^{j-\ell}\binom n{j-\ell}(\mu+\ell/2)_k.
\]
All the coefficients are rational. Since the finite-difference operator of order \(n=k+1\) annihilates a polynomial of degree \(k\), the remaining coefficients vanish identically. This is an exact rational function identity, not an asymptotic power-series approximation.

**3. Turn disk-root counting into a real half-plane problem.** Let
\[
Q_n(t)=(1+t)^kP_n\!\left(\frac{1-t}{1+t}\right).
\]
The Cayley transformation \(t=(1-U)/(1+U)\) maps \(|U|<1\) bijectively to \(\operatorname{Re}t>0\). The polynomial \(Q_n\) has exact rational coefficients, leading coefficient strictly positive and no vanishing leading Routh pivots for the tested dimensions. The classical Routh theorem counts roots in the open right half-plane by sign variations in the first Routh column; nonzero Hurwitz minors and pivots also exclude imaginary-axis roots here.

The accompanying `check.py` constructs *all* polynomial coefficients from the displayed closed formula using Python exact fractions; it separately computes the principal Hurwitz determinants via fraction-free Bareiss elimination and the Routh columns via independent rational elimination. It obtains the following complete sign certificate (the entry \(+^j\) denotes \(j\) positive signs):

| \(n\) | Signs of \(\Delta_1,\dots,\Delta_{n-1}\) | Signs of successive Routh pivots | Right-half-plane roots |
|---|---|---|---:|
| \(2\) | \(+\) | \(++\) | 0 |
| \(3\) | \(++\) | \(+++\) | 0 |
| \(4\) | \(++ +\) | \(++ ++\) | 0 |
| \(5\) | \(++++\) | \(+++++\) | 0 |
| \(6\) | \(+++++\) | \(++++++\) | 0 |
| \(7\) | \(++++++\) | \(+++++++\) | 0 |
| \(8\) | \(+++++++\) | \(++++++++\) | 0 |
| \(9\) | \(++++++++\) | \(+++++++++\) | 0 |
| \(10\) | \(+++++++++\) | \(++++++++++\) | 0 |
| \(11\) | \(+++++-----\) | \(++++++-++++\) | 2 |

For independent short reproduction, the primitive integral \(Q_{11}\), written in increasing powers of \(t\), has coefficients

```
1253826625536, 24031676989440, 217138391580672,
1227061877391360, 4848264135825408, 14167589762055168,
31520830021726464, 53923972270029696, 70091293939542360,
65386761710460684, 34205944490311243
```

Its Routh column has signs \(++++++-++++\), giving exactly two right-half-plane zeros counting multiplicity. For any real \(U\in[0,1)\), \(P_n(U)>0\) follows directly from the positive generating series. The exact checker also verifies \((-1)^j c_{n,j}>0\) for every \(0\le j\le k\) and \(2\le n\le11\), which gives \(P_n(U)>0\) for real \(-1<U<0\). Consequently neither of the two disk roots at \(n=11\) is real. Reality of the coefficients forces them to be a conjugate pair, each simple. This concludes the classification.

## Verification

Run `python3 check.py` with the standard Python 3 library (no packages required). It finishes with `CHECK_OK: full n=2..11 exact Hurwitz and Routh certificates` and prints the sign table. The calculation uses unbounded integers and rational fractions, compares two independent exact polynomial root-count algorithms, checks the generating-function identity through additional coefficients, and checks the displayed primitive \(Q_{11}\). The proof requires the classical Routh theorem; the checker implements all specific exact certificates used to invoke it. Numerical root approximations are illustrative only.

## Relationship to prior work

Pendyala's *Fefferman–Szegő kernels and finite-type rigidity on egg domains* (arXiv:2607.04100v1, 2026-07-05), Sections 2–4, derives the general Fefferman density, monomial norms, and one-variable rational kernel for all egg exponents. Those starting formulas are acknowledged and reconstructed above. Its Sections 5–7 study boundary blow-up and scalar-curvature, Einstein, and proportionality rigidity, not the positions or disk counts of complex zeros of the numerator. The present result applies an exact half-plane root-count certificate to give the **first nonzero complex dimension** in the quartic subfamily; this is not a stated conclusion or immediate coefficient identity of the general kernel formula.

Bhatnagar and Fan's 2026 two-dimensional egg paper analyzes the invariant Szegő metric in the two-variable case, not the high-dimensional zero transition. Kamimoto's 1998 analysis of weakly pseudoconvex egg kernels treats different boundary measures and diagonal asymptotics, not the same Fefferman measure and off-diagonal zero question. Studies of Bergman-kernel Lu Qi-Keng problems for ellipsoids concern different Hilbert kernels and cannot transfer zero-freeness to this Fefferman–Szegő kernel.

## Limitations

The theorem gives all dimensions up to and including the first failure, not a classification for \(n\ge12\), other egg powers, or the scalar curvature of any metric. The critical threshold concerns the Fefferman boundary measure specifically, not Euclidean-surface Szegő or volume Bergman kernels. Full independent mathematical audit and global historical-priority verification have not been performed. The rational generating-function formula was already known; the new contribution asserted is the sharp first zero-onset dimension, its exact certificate, and the two simple nonreal zero fibers.

## References

1. V. S. Pendyala, *Fefferman–Szegő kernels and finite-type rigidity on egg domains*, arXiv:2607.04100v1, 2026-07-05, https://arxiv.org/html/2607.04100v1 (full text, especially §§2–4 and §§6–7).
2. A. Bhatnagar and J. Fan, *The invariant Szegő metric on Egg domains*, arXiv:2606.24452v1, 2026-06-23, https://arxiv.org/abs/2606.24452 (two-dimensional comparison).
3. J. Kamimoto, *Singularities of the Bergman Kernel for Certain Weakly Pseudoconvex Domains*, J. Math. Sci. Univ. Tokyo **5** (1998), 99–117, https://www.ms.u-tokyo.ac.jp/journal/pdf/jms050105.pdf (full text inspected; different surface-measure and diagonal setting).
4. L. Zhang and W. Yin, *Lu Qi-Keng's problem on some complex ellipsoids*, J. Math. Anal. Appl. **357** (2009), 364–370, DOI:10.1016/j.jmaa.2009.04.018 (Bergman comparison).
