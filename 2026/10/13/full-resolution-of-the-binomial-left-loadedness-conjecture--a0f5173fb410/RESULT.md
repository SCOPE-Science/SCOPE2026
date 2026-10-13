# Full resolution of the binomial left-loadedness conjecture
## Finding
For positive integers \(n,m\) with \(n\ge 2m\), let
\[
X\sim\operatorname{Bin}(n,m/n),
\qquad
\alpha_i=\Pr(X\le m-i)-\Pr(X\ge m+i),\quad 1\le i\le m.
\]
Then \(X\) is left-loaded in the sense of Fokkink, Papavassiliou and Pelekis. Equivalently, Conjecture 4.1 of their paper holds on its full stated range. When \(n>2m\) and \(m\ge3\), the proof establishes condition \(L_1\): the sequence \(\alpha_1,\ldots,\alpha_m\) changes sign once from nonnegative to nonpositive. The cases \(m=1,2\) satisfy condition \(L_2\), and the boundary \(n=2m\) is symmetric.

## Assumptions and scope
Throughout, \(n,m\) are positive integers and \(n\ge2m\). The source definition calls an integer-mean law left-loaded when either \(L_1\) holds (one sign change of the \(\alpha_i\)) or \(L_2\) holds (all partial sums \(\sum_{i=1}^k\alpha_i\) are nonnegative). The theorem concerns only the binomial family with integer mean \(m\) and success probability \(m/n\le1/2\). It does not claim \(L_2\) for \(m\ge3\).

## Proof
If \(n=2m\), then \(X\sim\operatorname{Bin}(2m,1/2)\) is symmetric about \(m\), so \(\Pr(X\le m-i)=\Pr(X\ge m+i)\) and every \(\alpha_i\) vanishes.

Assume now \(n>2m\). For \(m=1\), the mean identity from Lemma 2.1 of the source gives \(\alpha_1\ge0\), so \(L_2\) holds. For \(m=2\), Simmons' inequality gives \(\alpha_1>0\), while the same mean identity gives \(\alpha_1+\alpha_2\ge0\); hence \(L_2\) holds. It remains to treat \(m\ge3\).

Put \(N=n-m\), so \(N>m\), and write \(a_j=\Pr(X=j)\). For \(1\le i\le m\), define
\[
\beta_i=\frac{a_{m+i}}{a_{m-i}}.
\]
For \(1\le i<m\), direct cancellation of consecutive binomial coefficients gives
\[
\frac{\beta_{i+1}}{\beta_i}
=
\frac{m^2(N-i)(N+i+1)}{N^2(m+i+1)(m-i)}.
\]
The difference between the numerator and denominator in this comparison with one factors as
\[
m^2(N-i)(N+i+1)-N^2(m+i+1)(m-i)
=(N-m)\bigl((N+m)i(i+1)-mN\bigr).
\]
Since \(N-m>0\) and \(i(i+1)\) is strictly increasing, the ratios \(\beta_{i+1}/\beta_i\) cross one at most once, from below to above. Thus \(\beta_1,\ldots,\beta_m\) is U-shaped. Also
\[
\beta_1=\frac{m(N+1)}{N(m+1)}<1.
\]

We next prove the endpoint lemma \(\beta_m>1\). Since
\[
\beta_m
=
\binom{N+m}{2m}\left(\frac{m}{N}\right)^{2m}
=:F_m(N),
\]
it suffices to show \(F_m(N)>1\) for integers \(m\ge3\) and \(N>m\). For real \(x\ge m\), set
\[
h_m(x)=\log\frac{x+m+1}{x-m+1}+2m\log\frac{x}{x+1}.
\]
Then \(F_m(N+1)/F_m(N)=\exp(h_m(N))\), and
\[
h_m'(x)=
\frac{2m(x+1-m^2)}{x(x+1)(x-m+1)(x+m+1)}.
\]
Hence \(h_m\) decreases up to \(x=m^2-1\) and then increases to its limit zero. Moreover,
\[
\exp(h_m(m))=(2m+1)\left(\frac{m}{m+1}\right)^{2m}>1.
\]
For \(m=3\) this is the exact inequality \(5103>4096\). For \(m\ge4\), \((1+1/m)^m<e<3\), so \((1+1/m)^{2m}<9\le2m+1\). Therefore \(h_m\) has a single zero and \(F_m(N)\) first increases and then decreases. Its infimum over integers \(N\ge m\) is consequently the smaller of its left endpoint and its limit:
\[
F_m(m)=1,
\qquad
\lim_{N\to\infty}F_m(N)=\frac{m^{2m}}{(2m)!}=:L_m.
\]
Now \(L_3=729/720>1\), and
\[
\frac{L_{m+1}}{L_m}
=
\left(1+\frac1m\right)^{2m}\frac{m+1}{2(2m+1)}.
\]
The first three terms of the binomial expansion give
\[
\left(1+\frac1m\right)^{2m}>5-\frac1m>rac{2(2m+1)}{m+1},
\]
so \(L_{m+1}>L_m\). Thus \(L_m>1\) for every \(m\ge3\), and the endpoint lemma follows, strictly when \(N>m\).

Because the U-shaped sequence \(\beta_i\) starts below one and ends above one, it crosses one exactly once. Therefore
\[
b_i:=a_{m-i}-a_{m+i}=a_{m-i}(1-\beta_i)
\]
changes sign once from positive to nonpositive. The identity
\[
\alpha_{i+1}=\alpha_i-b_i
\]
shows that \(\alpha_1,\ldots,\alpha_m\) is U-shaped. Simmons' inequality, in the form quoted and used by the source, gives \(\alpha_1>0\) for \(n>2m\). At the other endpoint,
\[
\alpha_m=\Pr(X=0)-\Pr(X\ge2m)
\le a_0-a_{2m}<0,
\]
because \(\beta_m=a_{2m}/a_0>1\). A U-shaped sequence that starts positive and ends negative can cross zero only once from positive to negative. Hence \(L_1\) holds for every \(m\ge3\), completing the proof.

## Verification
The algebraic identities above were independently re-expanded, including the factorization governing \(\beta_{i+1}/\beta_i\) and the derivative of \(h_m\). A standalone exact-integer checker additionally reconstructs binomial masses up to a common denominator and verifies left-loadedness on a broad finite grid; this finite computation is supplemental and is not used as a proof of the infinite theorem. The checker also verifies the endpoint inequality and the ratio-sign identity on its test grid.

## Relationship to prior work
Fokkink, Papavassiliou and Pelekis define left-loadedness, prove the Poisson analogue by a U-shape argument, and state that \(\operatorname{Bin}(n,m/n)\) is known to satisfy \(L_2\) for \(m\in\{1,2\}\) and \(L_1\) for \(4\le m\le n/3\). They then formulate Conjecture 4.1 for the full range \(n\ge2m\). The present proof supplies the missing binomial endpoint inequality and ratio analysis needed to extend their U-shape mechanism through the whole half-mean range. A previously recorded result proved only the slice \(m=3\); that slice is a strict special case of the theorem here.

A separate public question asks for the stronger property \(\sum_{i=1}^k\alpha_i\ge0\) for every \(k\), i.e. \(L_2\), throughout the same binomial family. The present theorem does not imply that stronger assertion for \(m\ge3\).

## Limitations
The theorem is specific to integer-mean binomial laws with \(m/n\le1/2\). It proves the source's left-loadedness conjecture through \(L_1\) for \(m\ge3\), not the stronger all-partial-sums condition \(L_2\). Its only imported non-elementary ingredient is the classical Simmons inequality \(\alpha_1>0\) for \(n>2m\); all remaining steps are proved above. No claim is made for noninteger means, negative-binomial analogues, or success probabilities above one half.

## References
1. R. Fokkink, S. Papavassiliou and C. Pelekis, “On the monotonicity of tail probabilities,” Probability and Mathematical Statistics 42 (2022), 133–141, DOI: 10.37190/0208-4147.00050. Published online 2022-06-06; primary MSC 60G50.
2. T. C. Simmons, “A new theorem in probability,” Proceedings of the London Mathematical Society 1 (1894), 290–325, DOI: 10.1112/plms/s1-26.1.290.
3. MathOverflow question 384456, “Simmons' inequality on binomial random variables” (2021), which formulates the stronger all-partial-sums condition.
