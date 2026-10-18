# Exact prime-square denominator for the affine Wang–Sun sum at \(2p^{2}\)

## Finding
Let \(p\ge5\) be prime, \(n=2p^{2}\), and let \(\zeta\) be a primitive \(n\)-th root of unity. For the set \(\Delta_n\) of fixed-point-free affine permutations \(\pi(x)=vx+u\) of \(\mathbb Z/n\mathbb Z\), with \(v\) invertible, define
\[
S_n=\sum_{\pi\in\Delta_n}\operatorname{sgn}(\pi)
 \prod_{x\in\mathbb Z/n\mathbb Z}
 \frac{1+\zeta^{x-\pi(x)}}{1-\zeta^{x-\pi(x)}}.
\]
Then \(S_n\) is rational and its positive reduced denominator is exactly
\[
\boxed{\operatorname{den}(S_{2p^{2}})=p^{2p}.}
\]
In particular, the denominator exponent increases linearly in \(p\) along this first prime-square layer, unlike the exponent-one law for \(S_{2p}\).

## Assumptions and scope
A reduced denominator means the unique positive denominator in lowest terms of a rational number. Throughout, \(p\) is an arbitrary prime at least \(5\); no asymptotic or computational hypothesis is imposed. We write \(v_p\) for the normalized valuation on \(\overline{\mathbb Q}_p\), with \(v_p(p)=1\). For any even positive integer \(m\), put
\[
C_m=\sum_{r=1}^{m-1}(-1)^r
 \left(\frac{1+\zeta_m^r}{1-\zeta_m^r}\right)^m,
\]
where \(\zeta_m\) is primitive of order \(m\). This agrees with the alternating cotangent block in Agustín-Aquino's divisor formula. The value is rational by Galois invariance, and does not depend on the primitive root.

## Proof
**1. Reduction to the largest cotangent block.** By Theorem 5.1 of Agustín-Aquino [1], for \(n=2p^2\) the only possible nonzero blocks come from even divisors \(2\), \(2p\), and \(2p^2\). Their local coefficients are respectively irrelevant because \(C_2=0\), \(p(p-1)\) because exactly \(p-1\) units satisfy \(\gcd(1-v,2p^2)=2p\), and \(1\) because only \(v=1\) has the full gcd. Thus
\[
S_{2p^2}=C_{2p^2}+p(p-1)C_{2p}.
\]
Theorem 8.2 of [1] says \(\operatorname{den}(C_{2p})=p\) for \(p>3\), hence the second summand is integral. It remains to prove \(v_p(C_{2p^2})=-2p\) and integrality at every other rational prime.

**2. Root-of-unity split and the integral odd part.** Put \(q=p^2\), \(\alpha(z)=(1+z)/(1-z)\). Splitting even and odd residues yields
\[
C_{2q}=A_q-B_q,\qquad
A_q=\sum_{\substack{z^q=1\\z\ne1}}\alpha(z)^{2q},\qquad
B_q=\sum_{z^q=-1}\alpha(z)^{2q}.
\]
The \(q\) numbers \(\alpha(z)\) with \(z^q=-1\) are roots of the monic polynomial
\[
\frac{(X+1)^q+(X-1)^q}{2}\in\mathbb Z[X].
\]
Therefore they are algebraic integers, so their power sum \(B_q\) is an integer (it is also rational). Moreover, for each rational prime \(\ell\ne p\), all roots of unity of order dividing \(p^2\) have \(1-z\) an \(\ell\)-adic unit: its algebraic norm divides a power of \(p\). Thus \(A_q\), and hence \(C_{2q}\), is \(\ell\)-integral. Only \(p\) can occur in the reduced denominator.

**3. Primitive \(p^2\)-roots cannot control the valuation.** Separate \(A_q\) into its primitive \(p\)-root and primitive \(p^2\)-root contributions. For a primitive \(p^2\)-root \(z\), the ramification law for cyclotomic extensions gives
\[
v_p(1-z)=\frac1{p(p-1)},\qquad v_p(1+z)=0.
\]
Consequently every summand \(\alpha(z)^{2p^2}\) has valuation
\[
-\frac{2p}{p-1}>-2p
\]
for \(p\ge5\). The ultrametric inequality gives the same strict lower bound for their sum. It suffices to show that the primitive-\(p\) contribution has valuation exactly \(-2p\).

**4. A dominant term in Newton's identities.** Let \(d=(p-1)/2\). The \(d\) distinct squares of \(\alpha(z)\), for \(z\) running over primitive \(p\)-roots modulo inversion, are roots \(y_1,\ldots,y_d\) of
\[
H_p(Y)=\frac{(\sqrt Y+1)^p-(\sqrt Y-1)^p}{2p}
=Y^d+\sum_{j=1}^{d}c_jY^{d-j},\qquad
c_j=\frac1p\binom p{2j+1}.
\]
The displayed square-root notation denotes the even polynomial obtained by expansion; no branch is involved. For \(j<d\), the coefficient \(c_j\) is an integer, while \(c_d=1/p\). Also
\[
c_1=\frac{(p-1)(p-2)}6\in\mathbb Z_p^{\times}
\]
for every \(p\ge5\). Write \(T_m=\sum_{i=1}^d y_i^m\), so the primitive-\(p\) portion of \(A_q\) is \(2T_{p^2}\).

Set \(F(t)=1+\sum_{j=1}^dc_jt^j=\prod_i(1-y_it)\). The identity \(T_m=-m[t^m]\log F(t)\) gives the finite exact expansion
\[
T_m=\sum_{\substack{k_1,\ldots,k_d\ge0\\\sum_j jk_j=m}}
(-1)^K\frac{m(K-1)!}{\prod_jk_j!}
\prod_j c_j^{k_j},\qquad K=\sum_jk_j.
\]
Each displayed combinatorial multiplier \(m(K-1)!/\prod k_j!\) is an integer: use \(m=\sum_jjk_j\) and distribute the sum as weighted multinomial coefficients. Now take \(m=p^2\), set \(s=k_d\) and \(R=(p^2-1)/d=2p+2\). Necessarily \(s\le R\). If \(s=R\), the remaining weighted degree equals \(1\), forcing \(k_1=1\) and all other \(k_j=0\). Its unique contribution is
\[
(-1)^{R+1}p^2c_1c_d^R,
\]
of valuation \(2-R=-2p\).

All other contributions have valuation at least \(-2p+1\). Indeed, for \(s\le R-3=2p-1\), integrality of the combinatorial multiplier and of all \(c_j\) for \(j<d\) suffices. For \(s=R-1=2p+1\), let \(t=\sum_{j<d}k_j\). The remaining weighted degree is \(d+1\), hence \(2\le t\le d+1<p\). In the ratio
\[
p^2\frac{(s+t-1)!}{s!\prod_{j<d}k_j!},
\]
all extra numerator factors are between \(2p+2\) and \(3p-1\), and the factorials in the denominator are \(p\)-adic units; the multiplier therefore has valuation \(2\). The whole contribution has valuation \(2-s=-2p+1\). For \(s=R-2=2p\), the remaining weighted degree is \(2d+1=p\), giving \(t\le p\). All extra numerator factors lie between \(2p+1\) and \(3p-1\), so are units, while \(\sum_{j<d}v_p(k_j!)\le1\). Thus the multiplier has valuation at least \(1\), and the contribution has valuation at least \(1-s=-2p+1\).

The unique term of valuation \(-2p\) cannot cancel with terms of larger valuation. Hence \(v_p(T_{p^2})=-2p\), and the primitive-\(p\) trace \(2T_{p^2}\) has the same valuation because \(p\) is odd. Step 3 shows that addition of the primitive-\(p^2\) trace does not change it. Step 2 shows subtraction of \(B_q\) does not change it. Step 1 concludes \(v_p(S_{2p^2})=-2p\). As every other rational prime is integral, its exact positive reduced denominator is \(p^{2p}\), as claimed. \(\square\)

## Verification
Run `python3 check_denominator.py` using standard Python 3 (no packages). The program implements the same alternating cotangent power sums with exact `fractions.Fraction` arithmetic and Newton–Girard recurrences, then applies the reduction of Step 1. It checks the exact denominator law for \(p\in\{5,7,11,13,17,19\}\), and checks three published small cotangent-block values. It is a finite numerical cross-check; the proof of the assertion for every prime \(p\ge5\) is the valuation argument above.

## Relationship to prior work
Agustín-Aquino [1], publicly posted October 2, 2026, proves the general divisor formula and the reduced denominator \(p\) at \(n=2p\), but does not state the prime-square family law at \(n=2p^2\). The closed Bernoulli-polynomial expression in [1], drawing on Liu and Xin, can in principle evaluate any fixed modulus; extracting a uniform exact reduced denominator requires controlling cancellations between all terms. The 2022 precursor [2] treats the same affine sum and tabulates only small moduli. The established separate family \(n=4p\) requires a different modulus and does not imply the present prime-square assertion. Related finite Fourier or cotangent norm formulas address different sums and cannot be directly substituted here.

## Limitations
The law is proved only for prime-square indices \(n=2p^2\) with \(p\ge5\); no formula is claimed for higher prime powers, general composite indices, or the full numerator. Exact-rational experiments check a small set of primes and are not a substitute for the universal proof. A pre-existing equivalent prime-square denominator computation not identified by the literature searches remains a possible originality risk. The formula does not assert independent external verification.

## References
[1] O. A. Agustín-Aquino, *The Wang–Sun Sum over Affine Derangements*, arXiv:2610.02806v1 (first public version October 2, 2026), Sections 5–8, https://arxiv.org/abs/2610.02806.

[2] O. A. Agustín-Aquino, *Wang–Sun Formula in the Affine Group over Even Cyclic Rings*, arXiv:2207.14495 (2022), https://arxiv.org/abs/2207.14495.
