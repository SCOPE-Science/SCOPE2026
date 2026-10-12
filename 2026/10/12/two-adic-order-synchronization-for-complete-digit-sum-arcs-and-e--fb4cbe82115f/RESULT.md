# Two-adic order synchronization for complete digit-sum arcs and exact base densities

## Finding
For an integer base \(b\ge3\), write \(s_b(N)\) for the sum of the base-\(b\) digits of \(N\), and put
\[
\mathcal O_b(n)=\{s_b(N):N\in\mathbb Z_{>0},\ n\mid N\}.
\]
Suppose that \(n\ge2\) and \(\gcd(b-1,n)=2\), so \(b\) is odd and \(n\) is even. Factor \(n=n_0m\), where \(n_0\) is the product of the *full* prime-power factors of \(n\) whose primes divide \(b\). Thus \(\gcd(m,b)=1\) and \(m\) is even. Write
\[
m=2^e\prod_{i=1}^r p_i^{a_i},\qquad
p_i\text{ distinct odd primes},\quad e\ge1,
\]
and let \(o_i=\operatorname{ord}_{p_i^{a_i}}(b)\), \(h_i=\nu_2(o_i)\). The following conditions are equivalent:

1. \(\mathcal O_b(n)=2\mathbb Z_{>0}\).
2. \(2\in\mathcal O_b(n)\).
3. There exists \(t\in\mathbb Z_{\ge0}\) with \(b^t\equiv-1\pmod m\).
4. One of the following *complete local criteria* holds:
   * \(e=1\) and either \(r=0\), or every \(h_i\) is positive and all \(h_i\) are equal;
   * \(e\ge2\), \(b\equiv-1\pmod{2^e}\), and \(h_i=1\) for every \(i\) (with the last condition vacuous when \(r=0\)).

There is also an exact counting consequence, with no coprimality restriction on the bases. Fix any even integer \(n\), and write
\[
n=2^e\prod_{i=1}^{r}p_i^{a_i},\quad
\phi_i=p_i^{a_i-1}(p_i-1),\quad
s_i=\nu_2(\phi_i),\quad
u_i=\phi_i/2^{s_i},\quad d_i=p_i^{a_i-1}.
\]
Let \(C(n)\) count residue classes \(b\pmod n\) represented by odd integer bases \(b\ge3\) for which \(\gcd(b-1,n)=2\) and \(\mathcal O_b(n)=2\mathbb Z_{>0}\). Then
\[
\boxed{
C(n)=\begin{cases}
1,&r=0,\\[2pt]
\displaystyle\prod_{i=1}^r(d_i+u_i),&r\ge1,\ e\ge2,\\[5pt]
\displaystyle\prod_{i=1}^{r}d_i+
\sum_{\emptyset\ne S\subseteq\{1,\ldots,r\}}
\left(\prod_{i\notin S}d_i\right)
\left(\prod_{i\in S}u_i\right)
\frac{2^{|S|\min_{i\in S}s_i}-1}{2^{|S|}-1},&r\ge1,\ e=1.
\end{cases}}
\]
Consequently the natural density among all positive integral base candidates is exactly \(C(n)/n\). For comparison, the number of counted classes also coprime to \(n\) equals \(1\) when \(r=0\), and for \(r\ge1\) is
\[
\boxed{C_{\rm unit}(n)=
\begin{cases}
\displaystyle\prod_i u_i,&e\ge2,\\[3pt]
\displaystyle\left(\prod_i u_i\right)
\frac{2^{r\min_i s_i}-1}{2^r-1},&e=1.
\end{cases}}
\]

The classification also supplies a counterexample to the proposed necessity of \(s_b(n)\mid\gcd(b-1,n)\) for complete digit-sum arcs: \(b=19\), \(n=70\) has \(\gcd(18,70)=2\), \(s_{19}(70)=16\), yet \(19^3+1=6860\) is divisible by \(70\) and has digit sum \(2\) in base \(19\). Thus all positive even sums occur although \(16\nmid2\).

## Assumptions and scope
All integer bases are \(b\ge3\), with \(\gcd(b-1,n)=2\). The local order \(\operatorname{ord}_{p^a}(b)\) is used only when \(p\nmid b\). The prime powers incorporated in \(n_0\) are *whole* prime-power factors, even if the base contains a smaller power of that prime. All valuations are ordinary nonnegative integer \(2\)-adic valuations of positive integers. The empty product equals \(1\); when \(r=0\), no odd-primary order is required. The base-density assertion counts congruence classes modulo \(n\); every such class has arbitrarily large representatives that are valid bases.

## Proof
**Digit-sum reduction.** Since \(b\equiv1\pmod{b-1}\), every multiple \(N\) of \(n\) has \(s_b(N)\equiv N\equiv0\pmod 2\). Conversely, if \(N\) is a positive multiple of \(n\) with digit sum \(2\), choose an integer \(L\) exceeding its number of base-\(b\) digits. Then
\[
N\left(1+b^L+\cdots+b^{(q-1)L}\right)
\]
is a multiple of \(n\) with digit sum exactly \(2q\) for every \(q\ge1\), because its separated copies produce no carries. This proves \((1)\Longleftrightarrow(2)\).

For odd \(b\ge3\), a positive integer has digit sum \(2\) if and only if it is \(b^j(1+b^t)\) with \(j,t\ge0\); the special case \(t=0\) gives the single digit \(2\). If \(n\mid b^j(1+b^t)\), then \(m\mid1+b^t\) because \(\gcd(m,b)=1\). Conversely, if \(m\mid1+b^t\), choose \(j\) large enough that \(n_0\mid b^j\). The coprime factors \(m,n_0\) then yield \(n\mid b^j(1+b^t)\). This proves \((2)\Longleftrightarrow(3)\).

**Odd prime powers and phase synchronization.** For every odd \(p_i\), the unit group modulo \(p_i^{a_i}\) is cyclic and \(-1\) is its unique element of order \(2\). Therefore \(b^t\equiv-1\pmod{p_i^{a_i}}\) is possible precisely when \(o_i\) is even; its solution exponents are exactly
\[
t\equiv o_i/2\pmod{o_i}.
\]
Writing \(o_i=2^{h_i}v_i\) with \(v_i\) odd, each such solution has \(\nu_2(t)=h_i-1\). Thus a common solution forces all \(h_i\) to agree and be positive. Conversely, when they agree, setting \(L=\operatorname{lcm}(o_1,\ldots,o_r)\), \(t=L/2\) works: the ratio \(L/o_i\) is odd for each \(i\), so \(b^{L/2}=(b^{o_i/2})^{L/o_i}\equiv-1\) in each odd prime-power modulus.

When \(e=1\), the condition modulo \(2\) is automatic for odd \(b\), so these are all constraints. If no odd prime factor occurs, take \(t=0\).

When \(e\ge2\), reduction modulo \(4\) forces \(t\) odd: an even power of odd \(b\) is \(1\) modulo \(4\). For odd \(t\), the quotient \((b^t+1)/(b+1)=b^{t-1}-b^{t-2}+\cdots-b+1\) is odd, and therefore \(\nu_2(b^t+1)=\nu_2(b+1)\). It follows that \(b^t\equiv-1\pmod{2^e}\) is equivalent to \(b\equiv-1\pmod{2^e}\) for an odd exponent. Compatibility with the odd-primary conditions therefore requires \(h_i=1\) for all \(i\). Conversely, if this holds, \(t=L/2\) is odd and satisfies every odd-primary condition as well as the \(2\)-primary condition; for \(r=0\), choose \(t=1\). This proves \((3)\Longleftrightarrow(4)\) and completes the classification.

**Exact base-residue count.** The criterion depends only on \(b\pmod n\). At a fixed odd prime power \(p_i^{a_i}\), there are exactly \(d_i=p_i^{a_i-1}\) residues divisible by \(p_i\), which impose no order condition. The remaining \(\phi_i=2^{s_i}u_i\) units form a cyclic group. For each \(1\le h\le s_i\), exactly
\[
\varphi(2^h)u_i=2^{h-1}u_i
\]
units have multiplicative order with \(\nu_2\) equal to \(h\): choose an element of order \(2^h\) in its \(2\)-primary cyclic factor and any element of its odd-order factor.

If \(e\ge2\), the sole allowed residue modulo \(2^e\) is \(-1\). At each odd primary coordinate one may independently choose a nonunit (\(d_i\) possibilities) or a unit with \(h=1\) (\(u_i\) possibilities), giving \(\prod(d_i+u_i)\). If \(e=1\), the sole odd residue modulo \(2\) is \(1\). The all-nonunit choice contributes \(\prod d_i\); for a nonempty set \(S\) of unit coordinates, a common phase \(h\) can range from \(1\) to \(\min_{i\in S}s_i\), contributing
\[
\left(\prod_{i\notin S}d_i\right)
\left(\prod_{i\in S}u_i\right)
\sum_{h=1}^{\min_{i\in S}s_i}2^{(h-1)|S|}.
\]
Summing this finite geometric progression gives the displayed formula. Each selected odd-primary residue is either divisible by its prime or has positive \(2\)-adic order valuation, hence is not congruent to \(1\) modulo that prime; the selected residue modulo \(2^e\) has \(\gcd(b-1,2^e)=2\). Thus all counted classes satisfy the stipulated exact gcd, with no overcount. The Chinese remainder theorem makes all coordinate counts independent. Imposing that *every* odd-primary coordinate is a unit retains only \(S=\{1,\ldots,r\}\) in the \(e=1\) case, or only the \(u_i\) term in each factor when \(e\ge2\), giving \(C_{\rm unit}(n)\). Finally, periodicity modulo \(n\) gives density \(C(n)/n\) among positive integer bases.

## Verification
The standalone standard-library script `verify.py` independently enumerates all modular residues represented by exactly two base-\(b\) digit units, compares this exhaustive finite-state criterion with the local-order criterion for \(2292\) eligible base/modulus pairs, and compares both exact base-class count formulas with enumeration for \(250\) even moduli through \(500\). The script and its actual output are included. For illustration, \(b=3\) succeeds separately for \(n=10\) and \(n=14\), but fails for \(n=70\) because \(\nu_2(\operatorname{ord}_5(3))=2\) while \(\nu_2(\operatorname{ord}_7(3))=1\); a common exponent cannot satisfy both negative-one congruences. The finite computations are corroboration, not a substitute for the unrestricted proof.

## Relationship to prior work
Phunphayap, Noppakaew, and Pongsriiam establish \(\mathcal O_b(n)\subseteq\{u>0:\gcd(n,b-1)\mid u\}\) and in Question 1 of their 2023 preprint (Question 3.1 of the 2025 published version) ask for an equality criterion for \(\gcd(n,b-1)>1\). Their known sufficient condition \(s_b(n)\mid\gcd(n,b-1)\) does not imply the new necessity-and-sufficiency theorem; the explicit \((b,n)=(19,70)\) instance shows it is not necessary. The later minimal-Hamming-multiple work of Ionascu, Luca, and Merino treats binary weight and multiplicative orders of the *fixed* base \(2\) for odd moduli, whereas the present theorem handles odd bases with \(\gcd(b-1,n)=2\), incompatible local phases and exact base-residue densities.

## Limitations
Only the exact equality problem for \(\gcd(b-1,n)=2\) is classified; the theorem does not classify the full attainable digit-sum set when equality fails, nor the analogous higher-gcd cases. The base-density statement varies the base at a *fixed* modulus, and does not assert a distribution over moduli. The novelty comparison is relative to the cited primary texts and recorded related searches; independently published but unindexed equivalent formulations cannot be ruled out. No independent mathematical audit has been performed.

## References
1. P. N. Phunphayap, P. Noppakaew, and P. Pongsriiam, *Directed graphs of integers with arcs determined by an arithmetic function*, arXiv:2303.13017v1 (first public 23 March 2023), Sections 2–3, Theorems 1–3 and Question 1. https://arxiv.org/html/2303.13017v1
2. P. N. Phunphayap, P. Pongsriiam, and P. Noppakaew, same work, *Utilitas Mathematica* **124** (2025), 101–114, Question 3.1, doi:10.61091/um124-06. https://combinatorialpress.com/um-articles/vol-124/directed-graphs-of-integers-with-arcs-determined-by-an-arithmetic-function/
3. E. J. Ionascu, F. Luca, and T. Merino, *On the average value of the minimal Hamming multiple*, arXiv:2412.10839v1 (14 December 2024), Sections 1–2 and 4.2. https://arxiv.org/html/2412.10839v1
