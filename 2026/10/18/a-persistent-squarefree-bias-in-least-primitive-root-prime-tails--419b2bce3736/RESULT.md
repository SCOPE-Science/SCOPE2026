# A persistent squarefree bias in least-primitive-root-prime tails

## Finding

Let \(P(g)\) be the least prime \(p\) modulo which the positive integer \(g\) is a primitive root, allowing \(P(g)=\infty\). For real \(y\ge2\), define
\[
Q(y)=\prod_{p\le y}p,\qquad
A(y)=\prod_{p\le y}\left(1-\frac{\varphi(p-1)}p\right),\qquad
B(y)=\prod_{p\le y}\left(1-\frac{p\varphi(p-1)}{p^2-1}\right).
\]
Here and throughout, \(p\) ranges over primes and \(\varphi\) is Euler's totient.

For every positive integer \(N\) and \(y\ge2\), the following **uniform absolute-error formulas** hold:
\[
\begin{aligned}
U_N(y)&:=\#\{1\le g\le N:P(g)>y\}=N A(y)+O(Q(y)),\\
S_N(y)&:=\#\{1\le g\le N:g\text{ squarefree},\ P(g)>y\}
=\frac{N}{\zeta(2)}B(y)+O\!\left(Q(y)^2\sqrt N\right).
\end{aligned}
\]
Both implicit constants are absolute. For every fixed \(\epsilon\in(0,1/4)\), both formulas are relative asymptotics uniformly as \(N\to\infty\) in the range
\[
2\le y\le(1/4-\epsilon)\log N.
\]

The quotient of the two survival products has the **strictly positive infinite-product limit**
\[
K:=\lim_{y\to\infty}\frac{B(y)}{A(y)}
=\prod_p\frac{1-p\varphi(p-1)/(p^2-1)}{1-\varphi(p-1)/p},
\qquad 0.59166<K<0.59168.
\]
Therefore, whenever \(y=y(N)\to\infty\) inside the displayed range,
\[
\boxed{\lim_{N\to\infty}\frac{S_N(y)}{U_N(y)}=\frac{K}{\zeta(2)}\approx0.35970.}
\]
The unconditional squarefree density is \(1/\zeta(2)\approx0.60793\): repeated failure of small-prime primitive-root tests leaves an enduring squarefree deficit. Equivalently, the squarefree-conditioned survival tail is asymptotically \(K\) times the unrestricted survival tail.

## Assumptions and scope

All integers \(g\) are positive. The case \(g=1\) is harmless and included using the literal primitive-root definition (modulo \(2\), the group is trivial); excluding that single integer changes counts by at most one. No generalized Riemann hypothesis or other unproved conjecture is assumed. The assertion concerns distributions as \(g\) varies, *not* infinitude of Artin primes for any fixed \(g\). The cutoff \(y\) may be real and need not itself be prime.

## Proof

**1. The unrestricted sieve.** A cyclic group of order \(p-1\) has exactly \(\varphi(p-1)\) generators. Thus, among residue classes modulo \(p\), exactly \(p-\varphi(p-1)\) fail the primitive-root test. By the Chinese remainder theorem, there are
\[
R_0(y)=\prod_{p\le y}\bigl(p-\varphi(p-1)\bigr)=Q(y)A(y)
\]
classes modulo \(Q(y)\) failing every test up to \(y\). Each class contributes \(N/Q(y)+O(1)\) integers in \([1,N]\), so \(U_N(y)=NA(y)+O(R_0(y))=NA(y)+O(Q(y))\).

**2. Squarefree local conditions.** A residue modulo \(p^2\) is squarefree at \(p\) precisely when it is not zero modulo \(p^2\); there are \(p^2-1\) such classes. Each of the \(\varphi(p-1)\) primitive-root classes modulo \(p\) has exactly \(p\) lifts, all squarefree at \(p\). Hence the number of classes satisfying *both* local squarefreeness and failure of the primitive-root test is exactly
\[
r_p=p^2-1-p\varphi(p-1).
\]
This includes \(p=2\): of four classes modulo four, only the class of two is locally squarefree and fails the primitive-root test. The Chinese remainder theorem produces
\[
R(y)=\prod_{p\le y}r_p
\]
admissible residue classes modulo \(Q(y)^2\).

**3. The squarefree sieve with an explicit uniform error.** For \(n\le N\) in one of the \(R(y)\) classes, the condition of having no squared prime divisor exceeding \(y\) has exact indicator
\[
\sum_{\substack{d^2\mid n\\(d,Q(y))=1}}\mu(d).
\]
For each such \(d\le\sqrt N\), coprimality of \(d^2\) and \(Q(y)^2\) means that the congruences specifying an admissible class modulo \(Q(y)^2\) and \(n\equiv0\pmod{d^2}\) select a unique residue modulo \(Q(y)^2d^2\). Consequently,
\[
\begin{aligned}
S_N(y)&=\sum_{\substack{d\le\sqrt N\\(d,Q(y))=1}}\mu(d)
\left(\frac{N R(y)}{Q(y)^2d^2}+O(R(y))\right)\\
&=\frac{N R(y)}{Q(y)^2}\prod_{p>y}(1-p^{-2})+O\!\left(R(y)\sqrt N\right).
\end{aligned}
\]
The extension of the absolutely convergent divisor sum contributes at most \(O(\sqrt N)\); the displayed bound absorbs it since \(1\le R(y)\le Q(y)^2\). By the Euler product for \(\zeta(2)\),
\[
\frac{R(y)}{Q(y)^2}\prod_{p>y}(1-p^{-2})
=\frac1{\zeta(2)}\prod_{p\le y}\frac{r_p}{p^2-1}
=\frac{B(y)}{\zeta(2)}.
\]
This proves both uniform error bounds.

**4. Relative range.** The prime number theorem gives \(\log Q(y)=\sum_{p\le y}\log p=(1+o(1))y\). For \(p\ge3\), \(\varphi(p-1)\le(p-1)/2\), so all odd-prime factors in \(A(y)\) and \(B(y)\) are at least \(1/2\); at \(p=2\), they are respectively \(1/2\) and \(1/3\). Thus
\[
A(y),B(y)\ge \tfrac13 2^{-\pi(y)}=\exp(-O(y/\log y))
\]
for increasing \(y\). When \(y\le(1/4-\epsilon)\log N\), the squarefree error satisfies \(Q(y)^2\sqrt N\le N^{1-2\epsilon+o(1)}\), while the main term is \(N^{1-o(1)}\). The unrestricted error is smaller. Both relative formulas follow.

**5. Strictly positive bias factor.** Put \(a_p=\varphi(p-1)/p\). Direct subtraction gives
\[
\frac{1-p\varphi(p-1)/(p^2-1)}{1-a_p}
=1-\frac{\varphi(p-1)}{p(p^2-1)(1-a_p)}.
\]
Each factor is strictly between zero and one. Since \(a_p\le1/2\) for every prime \(p\), the subtraction is at most \(2/(p^2-1)\), a summable majorant. Hence \(0<K<1\), and the limit defining \(K\) exists. Dividing the relative asymptotics and sending \(y\to\infty\) proves the final limit.

To bound \(K\) numerically, multiply the exact rational factors for primes up to \(L=100000\). The omitted product lies between \(1-2/L\) and \(1\), because \(\prod(1-e_p)\ge1-\sum e_p\) and \(\sum_{n>L}(n^2-1)^{-1}=\frac12(L^{-1}+(L+1)^{-1})\). The companion program uses outward-rounded integer intervals for the exact rational partial product and obtains \(0.5916660377<K<0.5916778714\), proving the stated decimal enclosure.

## Verification

The standalone program `VERIFY.py` implements prime and totient sieves, exact modular primitive-root identification, local prime-square residue counts, a complete check of the \(900\) residue classes for the three primes \(2,3,5\), direct interval counts, and a high-precision finite Euler product with its proved analytic tail bound. Its deterministic checks pass. These are finite consistency checks: the unbounded statements follow from the proof, the squarefree divisor identity, and the prime number theorem.

## Relationship to prior work

Johnston and Naik (October 6, 2026, Theorem 1.3 and Section 4) prove an unconditional almost-all bound for the least primitive-root prime across all integers, using the unsieved residue product \(A(y)\). Their proof does not impose global squarefreeness on the sampled integer. Fan and Pollack (2025, Introduction and Section 4) give the unrestricted limiting residue law and consider squarefree *fixed bases* in a different, conditional uniform bound. Their unrestricted formula does not determine the conditional bias \(K\), because squarefree conditioning changes the local law from modulus \(p\) to modulus \(p^2\). The theorem above establishes the new squarefree local product, a uniform growing-cutoff asymptotic, and a nonvanishing conditional-density correction. The classical count of primitive roots and the squarefree sieve are acknowledged as inputs, not claimed as new.

## Limitations

The growing-cutoff range stops below \((\log N)/4\) because of the elementary \(Q(y)^2\sqrt N\) error bound; optimality of that restriction is not asserted. The theorem does not control any one fixed base \(g\) or prove Artin's conjecture. Its bias factor is determined exactly by an Euler product, but no simpler closed form is claimed. The rarity exponent of the unrestricted survival product is known from Fan and Pollack and is not claimed here as new. Earlier literature may contain an implicit squarefree-conditioned consequence of more general sieve principles.

## References

1. Daniel R. Johnston and Sunil Naik, *The least prime with a given primitive root and a variant of the larger sieve*, arXiv:2610.08569v1 (first posted October 6, 2026), Section 4.
2. Kai (Steve) Fan and Paul Pollack, *Counting primes with a given primitive root, uniformly*, arXiv:2505.05601v1 (first posted May 8, 2025), Introduction and Section 4.
3. Classical inputs: cyclicity of finite-field multiplicative groups, the Chinese remainder theorem, the squarefree Möbius sieve, Euler products, and the prime number theorem.
