# Prime-support rigidity and stretched-exponential escape for two quadratic Collatz maps

## Finding
For \(\varepsilon\in\{-1,1\}\), consider the integer map
\[
Q_{\varepsilon}(n)=\begin{cases}n/2,&n\text{ even},\\ n(n+\varepsilon)/2,&n\text{ odd}.\end{cases}
\]
Let \((x_t)_{t\ge0}\) be any orbit starting from a nonnegative integer and satisfying \(x_t\to\infty\). Natural logarithms are denoted by \(\log\). Then
\[
\liminf_{t\to\infty}\frac{\log x_t}{\sqrt{t\log t}}\;\ge\;\sqrt{\frac{\log2}{2}}.
\]
More precisely, write the successive odd members of the orbit as \(y_0,y_1,\ldots\), after discarding the initial finite block of even halvings, and put \(j_r=v_2(y_r+\varepsilon)\), \(k_r=(y_r+\varepsilon)/2^{j_r}\). Every \(k_r\) is an odd integer at least three; the integers \(y_0,k_0,k_1,\ldots\) are pairwise coprime; and
\[
y_r=y_0\prod_{i=0}^{r-1}k_i,\qquad
\omega(y_r)=\omega(y_0)+\sum_{i=0}^{r-1}\omega(k_i)\ge\omega(y_0)+r,
\]
where \(\omega\) counts distinct prime divisors. In particular, \(\log y_r\ge(1+o(1))r\log r\).

## Assumptions and scope
The claim concerns either of the two signed quadratic maps \(Q_{-1}\) and \(Q_{+1}\) on the nonnegative integers, but **not** the distinct symmetric map whose odd branch is \((n^2-1)/4\). It applies to every individual orbit which tends to infinity and does not assume any statistical model for starting values. For these two maps, the classification of which starting values escape was established in Ye [1]; the present quantitative conclusion is conditional only on escape, so its proof does not depend on re-proving that classification. Times \(t\) count **all** map applications, including divisions by two, not just the odd returns. All asymptotics hold along a fixed escaping orbit as the indicated integer index tends to infinity; the lower-bound constant is universal across both signs and all such starts.

## Proof
**Odd-return decomposition.** If the initial value is \(2^\ell y_0\) with \(y_0\) odd, \(\ell\) halvings reach \(y_0\). Escape entails \(y_0\ge3\). At every subsequent odd term \(y_i\), write
\[
y_i+\varepsilon=2^{j_i}k_i,\quad j_i\ge1,\quad k_i\text{ odd}.
\]
The next map application gives \(2^{j_i-1}k_i y_i\); precisely \(j_i-1\) halvings then give the next odd term \(y_{i+1}=k_i y_i\). If any \(k_i=1\), the odd term repeats after \(j_i\) steps and the orbit is eventually periodic, contrary to escape. Thus every \(k_i\ge3\) and \(y_i\) increases strictly. Every intermediate term is a power-of-two multiple of \(y_{i+1}\).

**New prime support at every odd return.** Because \(\varepsilon=\pm1\),
\[
\gcd(y_i,k_i)=1,\qquad k_i\mid(y_i+\varepsilon).
\]
Induction from \(y_i=y_0\prod_{h<i}k_h\) therefore shows that \(y_0,k_0,k_1,\ldots\) are pairwise coprime. Multiplicativity of \(\omega\) on coprime factors gives the displayed exact formula. At least \(r\) distinct odd primes divide \(y_r\). If \(p_1<p_2<\cdots\) are the odd primes, then \(p_i\ge i+2\), and so
\[
y_r\ge\prod_{i=1}^r p_i\ge\frac{(r+2)!}{2}.
\]
Writing \(L_r=\log y_r\), Stirling's elementary factorial asymptotic yields \(L_r\ge (1+o(1))r\log r\). Monotonic inversion of \(u\mapsto u\log u\) gives
\[
r\le(1+o(1))\frac{L_r}{\log L_r}.
\]
This inversion remains valid when \(L_r\) is much larger than \(r\log r\).

**Conversion to the ordinary iteration clock.** Put \(T_r=\ell+\sum_{i<r}j_i\), the time of the \(r\)-th odd term. For any large \(t\), take the unique \(r\) with \(T_r\le t<T_{r+1}\); necessarily \(r\to\infty\). The exact intermediate orbit formula gives \(x_t\ge y_r\). Since \(y_0\le y_1\le\cdots\le y_r\), for \(i\le r\) we have
\[
j_i\le\log_2(y_i+1)\le\frac{\log(y_r+1)}{\log2}.
\]
Consequently,
\[
t<\ell+\sum_{i\le r}j_i\le\ell+(r+1)\frac{\log(y_r+1)}{\log2}
\le\left(\frac1{\log2}+o(1)\right)\frac{L_r^2}{\log L_r}.
\]
Taking logarithms of this upper bound gives \(\log t\le(2+o(1))\log L_r\). Hence
\[
\frac{t\log t}{L_r^2}\le\frac2{\log2}+o(1).
\]
Finally \(\log x_t\ge L_r\), proving the asserted liminf bound.

## Verification
The standalone standard-library program `verify.py` checks both signed maps by exact integer arithmetic. It independently reconstructs each block of ordinary iterates, checks \(j_i\) and \(k_i\), tests the coprimality relations, and compares finite odd-return products with the appropriate product of small odd primes. Its output on execution is: `PASS: 2157 exact odd-return identities; 947 pairwise-coprime multipliers; 947 prime-product lower-bound comparisons`. These are finite regression tests, **not** a proof of the asymptotic statement, which follows from the preceding argument.

## Relationship to prior work
Ye [1] classifies bounded and escaping orbits for three quadratic Collatz-type maps and gives the exact odd-return formula (Lemma 1 and Lemma 2). Sedaghat [2] derives the same odd-return multiplication for the divide-or-choose-2 rule and the lower bound of geometric growth in the count of odd returns; Sedaghat [3] studies a related arithmetic iteration. The present finding uses these return identities but additionally proves disjoint successive prime supports and a uniform quantitative rate in **the full iteration clock**. Neither inspected source states the prime-support law or the stretched-exponential time-normalized lower bound. These conclusions are an arithmetic refinement of, not a new classification of, escaping starting values.

## Limitations
The theorem supplies a universal lower bound only, with no assertion that the constant is best possible. It gives no upper bound on escaping orbit growth or asymptotic for individual orbits; the corresponding result for the symmetric third quadratic map is not claimed. The prime-support identity requires \(\varepsilon=\pm1\) and fails to follow from this argument for other odd branches. The result is a mathematical deduction from previously known exact return formulas; an implicit earlier derivation cannot be ruled out despite the inspected sources and targeted searches.

## References
[1] Xuda Ye, *Classification of the Orbits of Three Quadratic Collatz-type Maps*, arXiv:2610.10660v1, first submitted October 7, 2026. https://arxiv.org/html/2610.10660v1

[2] H. Sedaghat, *Bounded Orbits of Quadratic Collatz-type Recursions*, arXiv:2004.07357v1, 2020. https://arxiv.org/html/2004.07357v1

[3] H. Sedaghat, *Dual Nature of Orbits of the Divide-or-Choose 2 Rule*, arXiv:2005.10712v1, 2020. https://arxiv.org/abs/2005.10712
