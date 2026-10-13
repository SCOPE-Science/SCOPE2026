# A multiplicative-order dichotomy for three-term power-sum congruences

## Finding
For integers \(q,e\ge2\) with \(\gcd(q,e)=1\), let \(m(q,e)\) be the least positive number of (not necessarily distinct) nonnegative integral powers of \(q\) whose sum is divisible by \(e\). For every fixed positive integer \(n\), define
\[
\mathcal E_n=\{e\ge2:\text{some }q\ge2\text{ has }\operatorname{ord}_e(q)=n\text{ and }m(q,e)=3\}.
\]
Then \(\mathcal E_n\) is infinite **if and only if** \(3\mid n\). More precisely:

1. If \(3\nmid n\), every \(e\in\mathcal E_n\) satisfies the explicit uniform bound \(e\le3^n\).
2. If \(3\mid n\), write \(C_n(X)=\Phi_n(X)\), the \(n\)-th cyclotomic polynomial. For every sufficiently large integer \(q\ge2\), \(e=C_n(q)\) belongs to \(\mathcal E_n\) when \(n\) is odd. When \(n\) is even, every sufficiently large \(q\equiv1\pmod3\) gives \(e=3C_n(q)\in\mathcal E_n\). These moduli are unbounded.

## Assumptions and scope
The order \(\operatorname{ord}_e(q)\) is the multiplicative order of the residue class of \(q\) in \((\mathbb Z/e\mathbb Z)^\times\), defined only when \(\gcd(q,e)=1\). Nonnegative exponents and repeated summands are allowed. The assertion concerns all positive orders \(n\), not just prime orders or prime-power moduli. The word "sufficiently" means beyond an explicit, finite, computable threshold depending on \(n\); the proof constructs that threshold using integer resultants.

## Proof
**A resultant obstruction.** Fix \(n\ge1\) with \(3\nmid n\). Suppose \(\operatorname{ord}_e(q)=n\) and \(m(q,e)=3\). Multiplying the three-term congruence by the inverse of one power and reducing exponents modulo \(n\), one obtains indices \(0\le a,b<n\) such that
\[
e\mid(1+q^a+q^b),\qquad e\mid(q^n-1).
\]
Set \(F_{a,b}(X)=1+X^a+X^b\). No complex \(n\)-th root of unity is a zero of \(F_{a,b}\): if \(1+u+v=0\) and \(|u|=|v|=1\), then \(|1+u|=1\), so \(\Re(u)=-1/2\) and \(\{u,v\}\) is precisely the pair of primitive cube roots of unity. Consequently, if \(u=\zeta^a\) for an \(n\)-th root \(\zeta\), then \(3\mid n\), contrary to the hypothesis.

Hence the Sylvester resultant
\[
R_{n,a,b}=\operatorname{Res}_X(X^n-1,F_{a,b}(X))
=\prod_{\zeta^n=1}(1+\zeta^a+\zeta^b)
\]
is a nonzero integer. The integral Bézout identity associated with the resultant shows that \(e\mid R_{n,a,b}\). Each factor has absolute value at most \(3\), whence
\[
1\le e\le |R_{n,a,b}|\le 3^n.
\]
This holds without restrictions on the factorization of \(e\).

**A cyclotomic order lemma.** For fixed \(n\ge3\), the polynomial \(C_n=\Phi_n\) is monic integral with constant term \(1\). For each proper divisor \(d\mid n\), the complex polynomials \(C_n(X)\) and \(X^d-1\) have no common root. Define the positive integer
\[
K_n=\max_{\substack{d\mid n\\d<n}}\left|\operatorname{Res}_X(C_n(X),X^d-1)\right|.
\]
Because \(C_n(q)\to\infty\) for integer \(q\to\infty\), choose \(q\) so large that \(C_n(q)>\max(1,K_n)\). Since \(C_n(q)\mid q^n-1\), the order of \(q\) modulo \(C_n(q)\) divides \(n\). If it were a proper divisor \(d\), then \(C_n(q)\) would divide the above fixed nonzero resultant of size at most \(K_n\), an impossibility. Thus
\[
\gcd(q,C_n(q))=1,\qquad \operatorname{ord}_{C_n(q)}(q)=n.
\]
The gcd equality also follows from \(C_n(0)=1\).

**Unbounded constructions.** Assume \(3\mid n\) and put \(r=n/3\). Every primitive \(n\)-th root \(\zeta\) satisfies \(1+\zeta^r+\zeta^{2r}=0\), so monicity and Gauss's lemma yield the integral polynomial divisibility
\[
\Phi_n(X)\mid (1+X^r+X^{2r}).
\]
For odd \(n\), take \(e=\Phi_n(q)\) for every sufficiently large \(q\). The order lemma supplies order \(n\), and the displayed polynomial identity gives a three-term zero sum. A one-term zero sum is impossible for an invertible residue. A two-term zero sum would imply \(q^j\equiv-1\pmod e\) for some \(j\), impossible when the order \(n\) is odd. Therefore \(m(q,e)=3\).

For even \(n\), necessarily \(6\mid n\). Since \(n\) has at least two distinct prime factors, \(\Phi_n(1)=1\). Choose all sufficiently large integers \(q\equiv1\pmod3\); then \(\Phi_n(q)\equiv1\pmod3\), so \(3\) and \(\Phi_n(q)\) are coprime. Put \(e=3\Phi_n(q)\). Modulo \(\Phi_n(q)\), \(q\) has exact order \(n\), and modulo \(3\), \(q\) has order \(1\). The Chinese remainder theorem gives order \(n\) modulo \(e\). The three-term sum \(1+q^r+q^{2r}\) vanishes modulo both relatively prime factors of \(e\), hence modulo \(e\). Every individual power is congruent to \(1\pmod3\), so no sum of one or two powers can vanish modulo \(e\). Thus \(m(q,e)=3\). In both parity cases \(\Phi_n(q)\to\infty\), giving infinitely many distinct moduli, which completes the proof.

## Verification
The accompanying standalone `verify.py` uses exact integer/SymPy arithmetic. It checked \(214\) nonvanishing resultants for eight orders not divisible by three, \(44\) cyclotomic construction cases across eight orders divisible by three, and \(4385\) coprime residue pairs for moduli through \(120\). The output is reproduced in `verification_output.txt`. These finite calculations check examples and boundary behavior; the proof above is the basis for the infinite quantified statement. In particular, for \(n=3,q=2\) the construction gives \(e=7\); for \(n=6,q=4\) it gives \(e=39\).

## Relationship to prior work
Jacob and Külshammer (arXiv:2204.09403, introduction) explicitly ask for criteria for \(m(q,e)=3\). Their Proposition 11 proves finiteness for moduli dividing \(\Phi_n(q)\) subject to a length threshold \(m(q,e)<n/(n-\varphi(n))\); that result does not imply the present bound for **every** modulus of fixed order \(n\) when \(3\nmid n\), and does not supply the infinite constructions at all multiples of three. Breuer, Héthelyi, Horváth and Külshammer (2021), Proposition 2.25, treats prime orders and divisors of a single cyclotomic value, while Lemma 2.11 treats a prime-power modulus when its order is divisible by three. Neither covers the mixed-modulus even-order construction. Lam and Leung classify lengths of sums of complex roots of unity; their weight-three obstruction motivates the first half, but does not itself classify or bound integer moduli or construct exact-order modular examples. An existing specialized order-four enumeration provides a stronger classification at that one order only, not this all-orders dichotomy.

## Limitations
The statement distinguishes finite from infinite admissible-modulus sets, not their complete enumeration. The universal bound \(3^n\) need not be sharp for a given \(n\). The cyclotomic construction gives infinitely many examples for each order divisible by three but does not capture all admissible pairs. The result has only the self-review described in the accompanying review; an independent audit has not been performed. An equivalent formulation in unindexed literature remains a bibliographic risk.

## References
1. L. Jacob and B. Külshammer, *Congruences for Sums of Powers of an Integer*, arXiv:2204.09403v1, publicly submitted 20 April 2022, https://arxiv.org/pdf/2204.09403, especially Introduction and Proposition 11.
2. T. Breuer, L. Héthelyi, E. Horváth and B. Külshammer, *The Loewy Structure of Certain Fixpoint Algebras, Part II*, International Electronic Journal of Algebra 30 (2021), 16–65, https://www.ieja.net/files/papers/volume-30/2-V30-2021.pdf, especially Lemma 2.11 and Proposition 2.25.
3. T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, Journal of Algebra 224 (2000), 91–109, arXiv:math/9511209, https://arxiv.org/pdf/math/9511209.
