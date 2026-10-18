# Odd-prime exponent rigidity in harmonious partners of powers of two

## Finding

Write \(\sigma(n)=\sum_{d\mid n}d\). Two positive integers \(a,b\) form a **harmonious pair** if
\[
\frac{a}{\sigma(a)}+\frac{b}{\sigma(b)}=1.
\]
**Theorem.** Let \(k,r,s\geq1\) be integers and let \(p\) be an odd prime. The pair \((2^k,2^r p^s)\) is harmonious if and only if
\[
\boxed{s=1,\quad r=k,\quad p=2^k-1\text{ is prime}.}
\]
In particular, a harmonious partner of a power of two cannot have the form \(2^r p^s\) with \(s\geq2\), for **any** exponents \(k,r\geq1\). The remaining partners in this two-prime-support family correspond exactly to Mersenne primes. For example, \((4,12)\), \((8,56)\) and \((32,992)\) satisfy the equation. The theorem does **not** classify partners with multiple distinct odd primes, such as the known pair \((2,120)\).

## Assumptions and scope

All exponents are strictly positive; \(p\) is an odd prime, and the two coordinates are ordered as stated (the defining equation is symmetric). A prime power \(p^s\) means an exact power of a single odd prime; there is no bound on its exponent. This is a theorem about the classical, ordinary sum-of-divisors function, not the harmonic-number or unitary-divisor variant.

## Proof

**Step 1: Remove \(k=1\).** Put \(X=2^r\) and \(S_s(p)=1+p+\cdots+p^s\). Then
\[
\frac{2^r p^s}{\sigma(2^r p^s)}=\frac{X}{2X-1}\frac{p^s}{S_s(p)}
>\frac12\frac{p-1}{p}\geq\frac13.
\]
Both strict inequalities follow from \(X/(2X-1)>1/2\) and \(S_s(p)<p^{s+1}/(p-1)\). When \(k=1\), the first coordinate contributes \(2/\sigma(2)=2/3\), so the second must contribute exactly \(1/3\), which is impossible. Henceforth \(k\geq2\).

**Step 2: Force a prime Mersenne number.** Set \(Y=2^k\), \(X=2^r\), and \(S=S_s(p)\). By multiplicativity,
\[
\sigma(2^k)=2Y-1,\qquad \sigma(2^r p^s)=(2X-1)S.
\]
Clearing positive denominators in the harmonious equation gives
\[
Xp^s(2Y-1)=(Y-1)(2X-1)S. \tag{1}
\]
Since \(Y-1\) is odd and
\[
\gcd(Y-1,X)=\gcd(Y-1,2Y-1)=1,
\]
(1) implies \(Y-1\mid p^s\). As \(Y-1>1\), there is an integer \(j\) with \(1\leq j\leq s\) such that \(Y-1=p^j\).

We prove that \(j=1\) using only elementary factorization. If \(j\) is even, \(p^j\equiv1\pmod8\), whereas \(2^k-1\equiv3\pmod8\) for \(k=2\), and \(2^k-1\equiv7\pmod8\) for \(k\geq3\). If \(j\geq3\) is odd, then
\[
p+1\mid p^j+1=2^k.
\]
But the quotient \((p^j+1)/(p+1)=p^{j-1}-p^{j-2}+\cdots-p+1\) is an odd integer larger than \(1\), which cannot divide a power of \(2\). Thus \(j=1\), and necessarily
\[
p=Y-1=2^k-1. \tag{2}
\]

**Step 3: Exclude repeated odd primes.** Substitute (2) into (1) and cancel \(p\):
\[
p^{s-1}X(2p+1)=(2X-1)S_s(p). \tag{3}
\]
Because \(p\nmid S_s(p)\), (3) implies \(p^{s-1}\mid2X-1\). Put
\[
t=\frac{2X-1}{p^{s-1}}\in\mathbb Z_{\geq1}.
\]
Replacing \(2X-1\) by \(p^{s-1}t\) in (3), and using \(2X=p^{s-1}t+1\), yields
\[
2p+1=t\left(p^{s-1}+2\sum_{i=0}^{s-2}p^i\right). \tag{4}
\]
The sum is empty (and zero) when \(s=1\). For \(s=2\), the parenthesis is \(p+2\), strictly between \((2p+1)/2\) and \(2p+1\), so (4) would require \(1<t<2\), impossible. For \(s\geq3\), the parenthesis is at least \(p^2+2p+2>2p+1\), impossible for positive \(t\). Therefore \(s=1\).

For \(s=1\), equation (4) becomes \(t=2p+1\). As \(t=2X-1\), this forces \(X=p+1=Y\), hence \(r=k\). Conversely, if \(r=k\), \(s=1\), and \(p=2^k-1\) is prime, then
\[
\frac{2^k}{2^{k+1}-1}+\frac{2^k(2^k-1)}{(2^{k+1}-1)2^k}
=\frac{2^k+(2^k-1)}{2^{k+1}-1}=1.
\]
This proves both directions. \(\square\)

## Verification

The proof is unconditional and infinite: it uses multiplicativity of \(\sigma\), coprimality, modulo-\(8\) parity, elementary geometric sums, and integer inequalities. No computer result is required for the theorem. The included standalone `verify.py` independently constructs \(\sigma(2^k)\) and \(\sigma(2^r p^s)\), tests the cross-multiplied defining equation over a stated finite grid, and checks the expected classification. Run with `python3 verify.py`. Finite tests do not replace Steps 1–3.

## Relationship to prior work

Kozek, Luca, Pollack and Pomerance introduced and investigated harmonious pairs in *Harmonious pairs* (2015): their principal theorems treat sparsity and discordance and include the example \((4,12)\), rather than an exhaustive two-prime-support prime-power classification. A later published mathematical research record, *Powers of two in two-prime-support harmonious pairs* (published-finding corpus identifier below), **already proves** the complete case \(s=1\); no novelty is claimed for that specialization. The new content is the full, **unbounded exclusion of all \(s\geq2\)**, which converts the squarefree-odd-part result into a classification for arbitrary odd-prime exponents. The 2021 paper *The Abundancy Index and Feebly Amicable Numbers* studies the same identity under the name “feebly amicable,” including several general abundancy-index criteria and numerical pairs; its stated results do not imply the \(s\geq2\) obstruction. Searches for synonymous names and higher odd prime-power exponents yielded no stronger covering theorem, but this is not proof of universal novelty.

## Limitations

No assertion is made about more than one distinct odd prime in the partner, about all partners of powers of two, or about the infinitude of Mersenne primes. The only new claim relative to the closest indexed exact classification is the exponent-uniform elimination of nonsquarefree odd prime-power partners. An equivalent formulation could exist outside the inspected literature; independent audit has not been performed.

## References

1. M. Kozek, F. Luca, P. Pollack and C. Pomerance, *Harmonious pairs*, International Journal of Number Theory **11** (2015), 1633–1651. Author-hosted full text: https://www.pollack-math.net/harmonious5.pdf . First verified publication date: 2015-05-22.
2. *Powers of two in two-prime-support harmonious pairs*, published-finding corpus record `2026/10/4/SCOPE-powers-of-two-in-two-prime-support-harmonious-pairs--94f9b7228e53`. This contains the previously covered odd-exponent-one subcase.
3. J. Bishop, A. Bozarth, R. Kuss and B. Peet, *The Abundancy Index and Feebly Amicable Numbers*, arXiv:2104.11366 (2021), https://arxiv.org/abs/2104.11366 .
