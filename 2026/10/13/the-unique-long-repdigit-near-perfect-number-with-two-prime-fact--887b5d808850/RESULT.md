# The unique long repdigit near-perfect number with two prime factors in all bases

## Finding
For integers \(g\ge2\), \(1\le c<g\), and \(\ell\ge3\), let
\[
U_\ell(g)=1+g+\cdots+g^{\ell-1},\qquad N=cU_\ell(g).
\]
A positive integer is near-perfect if \(\sigma(N)=2N+d\) for some proper positive divisor \(d\mid N\). Let \(\omega(N)\) count its distinct prime factors. Then
\[
N\text{ near-perfect and }\omega(N)=2
\quad\Longleftrightarrow\quad
(g,c,\ell,N,d)=(3,1,4,40,10).
\]
In particular, \(40=(1111)_3\) is the only near-perfect repdigit with at least three digits and exactly two prime factors, in any base.

## Assumptions and scope
All bases, digits, lengths and divisor conditions are integral. The statement classifies only \(\ell\ge3\) and \(\omega(N)=2\); it does not concern arbitrary prime support or two-digit repdigits.

Use the Ren–Chen two-prime near-perfect classification: besides \(40\), every such integer is one of three types, each with precisely one odd prime \(q\):
\[
\begin{aligned}
\mathrm A &: 2^{p-1}(2^p-1)^2,\\
\mathrm B &: 2^{2p-1}(2^p-1),\\
\mathrm C &: 2^{t-1}(2^t-2^k-1),
\end{aligned}
\]
where the displayed odd factor is prime and parameters obey the conventional positivity conditions (in particular \(p\ge2\), \(0\le k<t\)). Thus the odd-prime exponent is at most \(2\), and a square odd-prime exponent occurs only in Type A. The classical Ljunggren square-repunit classification is used in one step.

## Proof
First consider the three parametric types, writing their unique odd prime \(q\). Define \(U=U_\ell(g)\). Since \(\ell\ge3\),
\[
U\ge g^2+g+1>2g>c.
\]
**Case 1: \(U\) odd.** This holds for all even \(g\), and for odd \(g\) when \(\ell\) is odd. Every odd factor of \(U\) must equal \(q\), so \(U=q\) or \(U=q^2\). If \(U=q^2\), Type A is forced. Ljunggren's theorem on square repunits with exponent exceeding \(2\) gives only \((g,\ell,q)=(3,5,11)\) when the square root is prime; \(11\) is not of the required form \(2^p-1\). Hence \(U\ne q^2\).

If \(U=q\), then in Type A the digit \(c\) must contain the remaining factor \(q\), contradicting \(c<g<U\). In Type B the digit is \(c=2^{2p-1}>2^p-1=q=U>g\). In Type C it is \(c=2^{t-1}\), whereas \(U=q=2^t-2^k-1<2^t\), and \(U>2g\) forces \(2^{t-1}>g\). Thus no parametric example has odd \(U\).

**Case 2: \(g\) odd and \(\ell\equiv2\pmod4\).** Write \(\ell=2m\) with odd \(m\ge3\). The positive odd integers
\[
U_m(g)\quad\text{and}\quad\frac{g^m+1}{g+1}
\]
are both greater than \(1\), are factors of \(U_{2m}(g)\), and are relatively prime: the former divides \(g^m-1\), the latter divides \(g^m+1\), and their gcd, being odd, divides \(2\). Hence \(U\) has at least two distinct odd prime factors, impossible for Types A–C.

**Case 3: \(g\) odd and \(4\mid\ell\).** The integer \((g+1)(g^2+1)=U_4(g)\) divides \(U\). Set \(Q=(g^2+1)/2\), an odd integer \(>g\). Because the odd parts of \(g+1\) and \(Q\) are coprime and \(Q>1\), the requirement of a single odd prime factor forces \(g+1=2^s\) with \(s\ge2\), so \(g=2^s-1\), and
\[
Q=2^{2s-1}-2^s+1,\qquad 2^{2s-2}<Q<2^{2s-1}.
\]
If \(\ell\ge8\), the elementary lifting-the-exponent formula gives
\[
\nu_2(U)=\nu_2(g+1)+\nu_2(\ell)-1,
\quad 2^{\nu_2(U)}=2^{s-1}2^{\nu_2(\ell)}\le\frac{(g+1)\ell}{2}.
\]
Therefore the odd part of \(U\) exceeds
\[
\frac{2g^{\ell-1}}{(g+1)\ell}.
\]
For \(g\ge3\) and \(\ell\ge8\), this quantity exceeds \(Q^2\): at \(\ell=8\) the inequality reduces to \(g^7>(g+1)(g^2+1)^2\), true because \((g+1)(g^2+1)^2\le(16/3)g^5<g^7\); and \(g^{\ell-1}/\ell\) increases thereafter. But since \(Q\mid U\), its only possible odd prime \(q\) satisfies \(q\le Q\); the complete odd part is \(q\) or \(q^2\), at most \(Q^2\). Contradiction. Hence \(\ell=4\).

Now \(U_4=2^{s+1}Q\) and \(c<g=2^s-1\). The odd-prime restriction forces \(Q=q\) or \(Q=q^2\). In the latter case Type A is forced and \(c\) is a power of \(2\). Write its exponent \(u\ge0\). The Type-A valuation identity gives \(p-1=s+1+u\), so \(q=2^p-1>g\), whereas \(q^2=Q<g^2\) gives \(q<g\); impossible. In the former case \(Q=q\), the digit must be \(c=2^u\), where \(0\le u\le s-1\), and the exponent of \(2\) in \(N\) is
\[
a=s+1+u\in[s+1,2s].\]
Type A cannot have \(Q=q\) because the digit would need a factor \(q=Q>g\). Type B would give \(a=2p-1\) and \(p\le s\), forcing \(q=2^p-1<2^s-1=g<Q\). Type C would give
\[
Q=2^{a+1}-2^k-1,\qquad0\le k\le a.
\]
The inequalities \(2^{2s-2}<Q<2^{2s-1}\), together with \(2^a-1\le Q<2^{a+1}\), force \(a=2s-2\) or \(a=2s-1\). If \(a=2s-2\), then \(2^k=2^s-2\), which cannot be a power of two for \(s\ge3\); the case \(s=2\) has \(a=2<s+1\), contrary to the admissible range. If \(a=2s-1\), then
\[
2^k=2^{2s-1}+2^s-2,
\]
which lies strictly between consecutive powers \(2^{2s-1}\) and \(2^{2s}\). Thus Type C also cannot occur. All three parametric types are excluded.

**The exceptional integer.** Finally \(N=40\) must be checked separately. Because \(U_\ell(g)\mid40\) and \(U_\ell(g)\ge7\), direct monotone bounds leave only finitely many candidates: for \(\ell=3\), \(g\le5\); for \(\ell=4\), \(g\le3\); for \(\ell=5\), \(g=2\); and for \(\ell\ge6\), \(U_\ell(g)\ge63>40\). Direct evaluation yields only \(U_4(3)=40\) dividing \(40\) with a valid digit, namely \(c=1\). Moreover \(\sigma(40)=90=2\cdot40+10\), with \(10\) a proper divisor. This proves both directions and uniqueness.

## Verification
The accompanying standard-library `verify.py` independently enumerates the recognized two-prime near-perfect families with parameters \(p\le16\) and \(t\le18\), then tests all possible base representations with at least three equal digits using exact integer arithmetic. It checks \(60\) instances and detects only \((g,c,\ell,N)=(3,1,4,40)\). It also verifies \(\sigma(40)=90\) and the local inequalities for \(2\le s\le19\). These finite checks corroborate the reasoning but are not a proof for unbounded parameters.

## Relationship to prior work
Ren and Chen classified near-perfect integers with precisely two distinct prime factors into Types A–C and the exceptional integer \(40\). Hasanalizade's repdigit study restricts its digit-length result to bases at most \(10\); the exceptional case is essential when treating that statement carefully. A subsequent complete classification in **even** bases establishes the absence of long even-base repdigits. The theorem here settles the complementary unbounded odd-base problem and identifies the unique long repdigit across all bases, not merely a numerical cutoff. It relies on the classical Ljunggren square-repunit theorem in the odd-repunit case.

## Limitations
The theorem is conditional on the established Ren–Chen classification and Ljunggren's theorem, not an elementary proof of those antecedents. It is specific to near-perfect integers with exactly two prime factors and lengths of at least three; it makes no claim for larger prime support or the complete two-digit classification. The literature comparison does not exclude unindexed equivalent formulations.

## References
1. Elchin Hasanalizade, “On near-perfect numbers of special forms,” arXiv:2206.10353v1, first public 14 June 2022, primary MSC \(11A25\).
2. Xiao-Zhi Ren and Yong-Gao Chen, “On near-perfect numbers with two distinct prime factors,” *Bulletin of the Australian Mathematical Society* 88 (2013), 520–524, DOI:10.1017/S0004972713000178.
3. Wilhelm Ljunggren, “Some theorems on indeterminate equations of the form \((x^n-1)/(x-1)=y^q\),” *Norsk Matematisk Tidsskrift* 25 (1943), 17–20.
4. “Even-base repdigit near-perfect numbers with two distinct prime factors,” publicly available mathematical research record, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-base-repdigit-near-perfect-numbers-with-two-distinct-prime--5e580ff645c3.
