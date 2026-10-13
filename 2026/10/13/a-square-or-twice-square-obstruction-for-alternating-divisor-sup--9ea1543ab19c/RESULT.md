# A square-or-twice-square obstruction for alternating-divisor superimperfect numbers

## Finding
Let \(\beta\) denote the multiplicative alternating divisor-sum function. A positive integer \(n\) is superimperfect for \(\beta\) if \(2\beta(\beta(n))=n\). Every such integer is **an even square or twice a square**. Thus the odd part of every solution is a perfect square. In particular, for every real \(X\ge1\),
\[
\#\{n\le X:2\beta(\beta(n))=n\}
\le\left\lfloor\frac{\sqrt X}{2}\right\rfloor+
\left\lfloor\sqrt{\frac X2}\right\rfloor
\le\left(\frac12+\frac1{\sqrt2}\right)\sqrt X.
\]
These are necessary restrictions, not an assertion that every integer of the prescribed shapes satisfies the equation.

## Assumptions and scope
For each prime \(p\) and integer \(e\ge1\), define
\[\beta(1)=1,\qquad \beta(p^e)=p^e-p^{e-1}+\cdots+(-1)^e=\frac{p^{e+1}+(-1)^e}{p+1},\]
and extend by multiplicativity to all positive integers. For an even positive integer \(n\), write uniquely \(n=2^a m\), where \(a\ge1\) and \(m\ge1\) is odd. An even square means \(n=(2j)^2\) for an integer \(j\ge1\); twice a square means \(n=2j^2\) for an integer \(j\ge1\). The theorem ranges over all positive integers; it imposes no bound on prime factors or exponents.

## Proof
For each prime power one has \(0<\beta(p^e)/p^e<1\), and hence \(0<\beta(u)\le u\) for all positive integers \(u\). For integers \(t\ge1\), put
\[
R(t)=\frac{\beta(2^t)}{2^t}=\frac{2+(-1)^t2^{-t}}3.
\]
Direct comparison of the odd and even cases gives
\[
R(t)\le\frac34,\quad R(t)\le\frac{11}{16}\ \text{if }t\ne2,
\quad R(t)<\frac23\ \text{if }t\text{ is odd},
\quad R(t)\le\frac{11}{16}\ \text{if }t\ge4\text{ is even}.
\]
Also, for every \(e\ge1\),
\[
\frac{\beta(3^e)}{3^e}=\frac{3+(-1)^e3^{-e}}4\le\frac79.
\]
If \(u\) is even and \(t=\nu_2(u)\), multiplicativity therefore gives
\[
\frac{\beta(u)}u\le R(t),
\]
and if additionally \(3\mid u\), then \(\beta(u)/u\le(7/9)R(t)\).

Suppose that \(2\beta(\beta(n))=n\). Odd \(n\) are impossible because the left side is even. Write \(n=2^a m\), with \(m\) odd. For odd primes \(p\), the sum defining \(\beta(p^e)\) has \(e+1\) odd terms and hence is odd exactly when \(e\) is even. Consequently \(\beta(m)\) is even if and only if \(m\) is **not** a square. We show this possibility is impossible.

Assume \(m\) is not a square. Then \(u=\beta(n)=\beta(2^a)\beta(m)\) is even, because \(\beta(2^a)\) is odd. Write \(t=\nu_2(u)\ge1\). If \(a\) is odd, then
\[
\frac{\beta(u)}n
=R(a)\frac{\beta(m)}m\frac{\beta(u)}u
<\frac23\cdot1\cdot\frac34=\frac12,
\]
contrary to \(\beta(u)=n/2\).

If \(a=2\), then \(\beta(2^a)=3\), so \(6\mid u\). The local factors at \(2\) and \(3\) imply
\[
\frac{\beta(u)}n\le\frac34\cdot1\cdot\frac34\cdot\frac79
=\frac7{16}<\frac12,
\]
a contradiction.

Finally suppose \(a\ge4\) is even. If \(t\ne2\), then
\[
\frac{\beta(u)}n\le\frac{11}{16}\cdot1\cdot\frac{11}{16}
=\frac{121}{256}<\frac12.
\]
If \(t=2\), write \(u=4v\) with \(v\) odd. The identity \(\beta(u)=\beta(4)\beta(v)=3\beta(v)\) shows that the proposed equation forces \(3\mid n\), and thus \(3\mid m\). This improves the bound to \(\beta(m)/m\le7/9\). Therefore
\[
\frac{\beta(u)}n\le\frac{11}{16}\cdot\frac79\cdot\frac34
=\frac{77}{192}<\frac12,
\]
the last contradiction. Thus \(m\) is a square, and every solution is an even square or twice a square, according to the parity of \(a\).

The sets of even squares and twice squares are disjoint, because the \(2\)-adic valuation of the former is even and that of the latter is odd. Up to real \(X\ge1\), there are exactly \(\lfloor\sqrt X/2\rfloor\) even squares and \(\lfloor\sqrt{X/2}\rfloor\) twice squares. Counting the candidate set proves both asserted upper bounds.

## Verification
A standalone standard-library Python verifier (`artifacts/verify.py`) computes the function by prime-power multiplicativity for all \(n\le10^6\), independently checks its Liouville-divisor-sum formula for \(n\le5000\), enumerates the superimperfect examples through \(10^6\), and verifies exclusion of every even \(n\le10^6\) with nonsquare odd part. The exact observed solutions are \(2,4,8,128,32768\). It separately verifies the known larger power-of-two witness \(2^{31}\) using its Fermat-prime factorization. These finite checks are auxiliary; the proof above is unrestricted.

## Relationship to prior work
László Tóth's arXiv:1111.4842v1 (2011), §2, establishes the parity characterization \(\beta(n)\) odd exactly when \(n\) is a square or twice a square. Its §7 introduces the iterated superimperfect equation, gives six examples, proves a special family among powers of two, and asks whether other solutions exist. The present statement is a new necessary condition **linking that iterated equation to the parity characterization**, rather than merely restating either fact. The associated database record OEIS A200758 lists known witnesses and a finite search but not the all-input square-shape obstruction or its counting bound. Published-record comparisons did not identify a stronger theorem that already implies this one; an unindexed earlier proof remains possible.

## Limitations
The theorem does not classify solutions among even squares or twice squares, does not prove that only the six known solutions exist, and does not give a matching lower bound for the solution-count function. The coefficient in the counting upper bound counts all shape-admissible candidates, most of which need not be solutions. The proof relies on exact local inequalities, not on extrapolating a finite search. Prior-art screening cannot establish absolute novelty.

## References
1. L. Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842v1, first posted 2011-11-21, especially §§2, 7, 8. https://arxiv.org/abs/1111.4842
2. OEIS Foundation, *A200758: Superimperfect numbers*, first submitted by L. Tóth 2011-11-22. https://oeis.org/A200758
