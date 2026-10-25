# Exact prime-square denominators of the Wang–Sun affine-derangement sum

## Finding

For every prime \(p\ge5\), let \(n=2p^2\), \(\zeta=e^{2\pi i/n}\), and let \(\Delta_n\) be the fixed-point-free affine bijections \(\pi(x)=vx+u\) of \(\mathbb Z/n\mathbb Z\), with \(v\) invertible. Define
\[
S_n=\sum_{\pi\in\Delta_n}\operatorname{sgn}(\pi)
\prod_{x\in\mathbb Z/n\mathbb Z}
\frac{1+\zeta^{x-\pi(x)}}{1-\zeta^{x-\pi(x)}}.
\]
Then \(S_{2p^2}\) is rational and its reduced denominator is **exactly \(p^{2p}\)**. More precisely,
\[
p^{2p}S_{2p^2}\in\mathbb Z,
\qquad p^{2p}S_{2p^2}\equiv-2\cdot3^{-1}\pmod p.
\]
Here \(3^{-1}\) denotes the inverse of \(3\) modulo \(p\). The displayed nonzero residue proves that no smaller power of \(p\) clears the denominator.

## Assumptions and scope

The prime \(p\) is at least \(5\); all affine maps are over the cyclic ring \(\mathbb Z/(2p^2)\mathbb Z\). Only derangements occur in the sum, so all denominators in its defining products are nonzero. All number-theoretic valuations below satisfy \(v_p(p)=1\). The conclusion is an *exact rational denominator*, not a real asymptotic statement.

## Proof

**1. Reduction to two alternating cotangent sums.** Write
\[
C_d=\sum_{r=1}^{d-1}(-1)^r\left(i\cot\frac{\pi r}{d}\right)^d
\qquad(d\text{ even}).
\]
For an affine map \(x\mapsto vx+u\), put \(d=\gcd(1-v,n)\). Such a map is a derangement exactly when \(d\nmid u\). Because \(n/d\) is odd for \(n=2p^2\), the elementary product over each fiber of \((1-v)x-u\) gives
\[
\prod_{x\bmod n}\frac{1+\zeta^{(1-v)x-u}}{1-\zeta^{(1-v)x-u}}
=\left(\frac{1+e^{-2\pi iu/d}}{1-e^{-2\pi iu/d}}\right)^d.
\]
The sign of multiplication by any unit \(v\) modulo \(2p^2\) is \(+1\): under the Chinese remainder decomposition, the sign on the odd prime-square factor is the square of the quadratic character and the factor modulo \(2\) is trivial. The translation has sign \((-1)^u\). Summing the \(n/d\) translations in each nonzero residue class modulo \(d\) produces \((n/d)C_d\). There is one unit \(v\) giving \(d=2p^2\), exactly \(p-1\) giving \(d=2p\), and the remaining ones give \(d=2\). Since \(C_2=0\),
\[
\boxed{S_{2p^2}=C_{2p^2}+p(p-1)C_{2p}.}\tag{1}
\]
The identity also establishes rationality once the two cotangent sums are shown rational.

**2. Root polynomials and rational integrality outside \(p\).** Put \(m=p^2\), and let \(\alpha_\omega=(1+\omega)/(1-\omega)\) for nonidentity \(m\)-th roots \(\omega\), and \(\beta_\eta=(1+\eta)/(1-\eta)\) for roots satisfying \(\eta^m=-1\). Since \(m\) is odd, even-index terms in \(C_{2m}\) correspond to the \(\alpha\)'s and odd-index terms to the \(\beta\)'s. Consequently
\[
C_{2m}=\sum_{\omega^m=1,\ \omega\ne1}\alpha_\omega^{2m}
-\sum_{\eta^m=-1}\beta_\eta^{2m}.\tag{2}
\]
The \(\beta\)'s are the roots of the monic integer polynomial
\[
G_m(Y)=\frac{(Y+1)^m+(Y-1)^m}{2},
\]
so their power sum is an integer by Newton's identities. The \(\alpha\)'s are roots of
\[
F_m(Y)=\frac{(Y+1)^m-(Y-1)^m}{2m},
\]
a monic polynomial with coefficients in \(\mathbb Z[1/p]\). Thus \(C_{2p^2}\in\mathbb Z[1/p]\). The analogous argument with \(m=p\) proves \(C_{2p}\in\mathbb Z[1/p]\).

**3. Primitive \(p^2\)-th roots do not contribute at the leading pole order.** Divide the first sum in (2) into primitive \(p\)-th and primitive \(p^2\)-th roots. For primitive \(p^2\)-th roots, the cyclotomic identity yields \(v_p(1-\omega)=1/(p(p-1))\), whereas \(1+\omega\) is a unit. With exponent \(2p^2\), each term has valuation \(-2p/(p-1)>-2p\). Non-Archimedean addition preserves this strict lower bound for their sum. The integral \(\beta\) sum likewise cannot affect the coefficient of the leading power \(p^{-2p}\).

**4. Exact leading pole from primitive \(p\)-th roots.** Let \(k=2p^2\) and
\[
A_p(k)=\sum_{\omega^p=1,\ \omega\ne1}\alpha_\omega^k,
\quad
E(t)=\prod_{\omega^p=1,\ \omega\ne1}(1+\alpha_\omega t)
= B(t)+\frac{t^{p-1}}p,
\]
where
\[
B(t)=1+\sum_{j=1}^{(p-3)/2}
\frac1p\binom p{2j+1}t^{2j}\in\mathbb Z[t],
\qquad b_2=[t^2]B(t)=\frac{(p-1)(p-2)}6.
\]
The formula for \(E\) follows directly from \(F_p\) by reversing its coefficients. Newton's logarithmic identity gives
\[
A_p(k)=-k[t^k]\log E(t).
\]
Expand \(\log E\) formally around zero:
\[
\log E=\log B+
\sum_{j\ge1}\frac{(-1)^{j+1}}{jp^j}
\frac{t^{j(p-1)}}{B(t)^j}.\tag{3}
\]
Only \(j\le J=\lfloor k/(p-1)\rfloor=2p+2\) contribute. At \(j=J\), the remaining degree is exactly \(2\); since \([t^2]B^{-J}=-Jb_2\) and \(J\) is even, this term contributes \(-kb_2/p^J\) to \(A_p(k)\). For every \(1\le j<J\), integrality of \(B^{-j}\) over \(\mathbb Z_p\) and \(j+v_p(j)\le2p+1\) give valuation at least \(2-j-v_p(j)\ge-2p+1\). Finally, \(-k[t^k]\log B=-[t^{k-1}]B'/B\) is \(p\)-integral. Because \(v_p(k)=2\) and \(b_2\equiv3^{-1}\pmod p\), we deduce
\[
\boxed{v_p(A_p(2p^2))=-2p,
\qquad p^{2p}A_p(2p^2)\equiv-2\cdot3^{-1}\pmod p.}\tag{4}
\]
By Step 3, exactly the same statements hold for \(C_{2p^2}\).

**5. The lower-order divisor term.** Repeat the formal argument (3) with \(k=2p\): now \(J=2\), and the only negative-valuation term is \(-2b_2/p\). Consequently \(C_{2p}\in p^{-1}\mathbb Z\), so \(p(p-1)C_{2p}\) is an integer. Combining (1) and (4) proves both the integrality and the nonzero residue of \(p^{2p}S_{2p^2}\), hence the exact reduced denominator. \(\square\)

## Verification

The accompanying standalone `verify.py` uses only Python's exact `fractions.Fraction` arithmetic. Two independent Newton-power-sum implementations compute the rational cotangent blocks. For \(p=5,7,11,13,17\), each resulting affine sum has reduced denominator \(p^{2p}\) and normalized numerator residue \(-2\cdot3^{-1}\pmod p\). Running `python3 verify.py` prints `CERTIFICATE_OK prime_cases=5 exact_newton_methods=2`. These finite checks corroborate, but do not replace, Steps 1–5.

## Relationship to prior work

Agustín Aquino's 2026 article [1] introduces the present affine-derangement sum, reduces general even moduli to alternating cotangent power sums, and obtains prime denominator for \(S_{2p}\) when \(p>3\). Its general expressions do not explicitly determine the reduced denominator for \(S_{2p^2}\). The new argument isolates the unique leading \(p\)-adic pole for the first prime-square family, providing a precise denominator and a nonzero normalized residue. Agustín Aquino's earlier article [2] studies affine versions and involutive subfamilies; Liu and Xin [3] give general weighted cotangent evaluations. An alternative formula in earlier work could conceal an equivalent special-case valuation.

## Limitations

The theorem covers \(p\ge5\) and modulus \(2p^2\) only; it neither asserts the same exponent at \(p=3\) nor covers \(2p^a\) for \(a\ge3\). Exact computation for finitely many primes is not a proof for all primes. Historical literature and general cotangent-sum identities may contain an implicit reformulation. Independent mathematical review has not been performed.

## References

[1] O. A. Agustín Aquino, *The Wang--Sun Sum over Affine Derangements*, arXiv:2610.02806v1 (first public 2026-10-02), https://arxiv.org/abs/2610.02806.

[2] O. A. Agustín-Aquino, *Wang-Sun Formula in the Affine Group of Even Cyclic Rings*, arXiv:2207.14495v1 (2022), https://arxiv.org/abs/2207.14495.

[3] Liu and Xin, *Root-of-unity weighted trigonometric power sums: a constant term approach*, arXiv:2607.29130 (2026), https://arxiv.org/abs/2607.29130.
