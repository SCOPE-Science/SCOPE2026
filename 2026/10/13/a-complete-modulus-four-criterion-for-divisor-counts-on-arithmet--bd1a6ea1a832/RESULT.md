# A complete modulus-four criterion for divisor counts on arithmetic progressions

## Finding
Let \(\tau(m)\) be the number of positive divisors of \(m\). For every pair of integers \(A\ge1\) and \(0\le B<A\), let \(\mathcal F(A,B)\) consist of the primes \(p\) for which \(p^a\Vert A\) and \(e_p:=\nu_p(B)<a\), with \(\nu_p(0)=+\infty\). Put
\[
J(A,B)=\prod_{p\in\mathcal F(A,B)}(e_p+1),
\]
where the empty product equals \(1\). Then
\[
\boxed{4\mid\tau(An+B)\ \text{for every }n\ge0\text{ with }An+B>0}
\]
holds **if and only if** one of the following two mutually exclusive conditions holds:

1. \(4\mid J(A,B)\).
2. \(J(A,B)\equiv2\pmod4\) and the congruence \(p t^2\equiv B\pmod A\) has no integer solution, where \(p\) is the unique member of \(\mathcal F(A,B)\) for which \(e_p\) is odd.

In condition 2, uniqueness follows from \(J\equiv2\pmod4\), and necessarily \(e_p\equiv1\pmod4\). The criterion is finite and effective for every progression.

As a concrete application, for every odd prime \(p\), define \(\mathcal B_{1,p}\) to be the set of integers \(0\le\beta<p^2\) for which \(4\mid\tau(8(p^2n+\beta)+1)\) for all \(n\ge0\). Then
\[
\boxed{\lvert\mathcal B_{1,p}\rvert=\begin{cases}
(p-1)/2,&p\equiv1\pmod8,\\
p-1,&p\not\equiv1\pmod8.
\end{cases}}
\]
In particular \(\lvert\mathcal B_{1,109}\rvert=108\). This contradicts the value \(54\) predicted for this prime in Conjecture 2 of Merca (2022), since \(109-1=108\) is not cubefree.

## Assumptions and scope
The indices \(n\) range over all nonnegative integers for which \(An+B\ge1\). The modulus is exactly \(4\), with no restriction on \(\gcd(A,B)\), parity of \(A\), or squarefreeness. The \(p\)-adic valuation at zero is only the formal convention \(\nu_p(0)=+\infty\), used to recognize that \(B\equiv0\pmod{p^a}\). A prime \(p\) belongs to \(\mathcal F\) precisely when its exponent in every positive member of the progression is fixed to \(e_p<a\).

## Proof
**1. Fixed exponents.** If \(p^a\Vert A\) and \(e=\nu_p(B)<a\), then every \(An+B\) has exact \(p\)-adic valuation \(e\). Consequently \(J(A,B)\mid\tau(An+B)\). Thus \(4\mid J\) suffices.

**2. When \(J\) is odd, the progression contains a term with divisor count \(2\pmod4\).** Here each fixed exponent \(e_p\) is even. For every \(p^a\Vert A\), set
\[
h_p=\begin{cases}\nu_p(B),&\nu_p(B)<a,\\2a,&\nu_p(B)\ge a,\end{cases}
\qquad E=\prod_{p^a\Vert A}p^{h_p}.
\]
All \(h_p\) are even, so \(E\) is a perfect square. For a prime \(p\in\mathcal F\), the congruence \(Eq\equiv B\pmod{p^a}\) is equivalent to
\[
q\equiv\frac{B/p^{e_p}}{E/p^{e_p}}\pmod{p^{a-e_p}},
\]
where the denominator is invertible modulo \(p^{a-e_p}\) because \(\nu_p(E)=e_p\). The prescribed class is a unit. For primes \(p\mid A\) not in \(\mathcal F\), both \(E\) and \(B\) are divisible by \(p^a\), imposing no restriction on \(q\). The Chinese remainder theorem therefore gives a reduced residue class modulo
\[
M=\prod_{p\in\mathcal F}p^{a_p-e_p}
\]
(with \(M=1\) allowed). By Dirichlet's theorem on primes in arithmetic progressions, there are arbitrarily large primes \(q\) in that class, and one may choose \(q\nmid E\). Then \(N=Eq\equiv B\pmod A\), \(N>B\), and
\[
\tau(N)=2\tau(E)\equiv2\pmod4,
\]
because every exponent of the square \(E\) contributes an odd factor to \(\tau(E)\). Thus the universal divisibility statement fails when \(J\) is odd.

**3. When \(J\equiv2\pmod4\).** Exactly one fixed prime \(p\in\mathcal F\) has odd exponent \(e_p\); necessarily \(e_p\equiv1\pmod4\). All other fixed exponents are even. A positive integer \(N\) with these fixed valuations can satisfy \(\tau(N)\equiv2\pmod4\) only if every exponent besides that of \(p\) is even. Indeed \(\tau(N)=\prod_{\ell^f\Vert N}(f+1)\), so exactly one factor is \(2\pmod4\) and all others odd. Since \(p\) already supplies this factor, it follows that \(N=p t^2\) for some positive integer \(t\).

Conversely, if \(p t^2\equiv B\pmod A\) has any integer solution, replacing \(t\) by a sufficiently large integer congruent to it modulo \(A\) yields \(N=p t^2>B\) in the progression. By the fixed-valuation property, \(\nu_p(N)=e_p\equiv1\pmod4\). Every other prime exponent in \(N\) is even, hence \(\tau(N)\equiv2\pmod4\). We have proved that a failure is equivalent to the existence of such a quadratic-congruence solution. With \(J\equiv2\pmod4\), no term can have odd divisor count; the only alternative to residue \(0\) is residue \(2\). The stated criterion follows.

**4. Exact cardinality in the prime-square family.** Let \(A=8p^2\), \(B=8\beta+1\). The residue \(B\) is odd. The only possible forced prime is \(p\): it occurs with exponent one exactly when \(p\mid B\) but \(p^2\nmid B\). Otherwise \(J=1\), so the progression fails the universal congruence. Among \(0\le\beta<p^2\), exactly \(p-1\) values satisfy \(p\Vert(8\beta+1)\), because multiplication by \(8\) is invertible modulo \(p^2\). Write \(B=pu\) for each such value. The remaining obstruction is
\[
p t^2\equiv pu\pmod{8p^2}.
\]
Since \(B\) is odd, \(t\) must be odd. Modulo \(8\), its square is \(1\), so this congruence is solvable only when \(p\equiv1\pmod8\). For \(p\not\equiv1\pmod8\), all \(p-1\) values qualify. When \(p\equiv1\pmod8\), the modulo-\(8\) condition is automatic, and the remaining congruence reduces modulo \(p\) to \(t^2\equiv u\pmod p\). The value \(u\) runs bijectively over \((\mathbb Z/p\mathbb Z)^\times\) as \(\beta\) runs over the \(p-1\) values; exactly half are quadratic nonresidues. Therefore precisely \((p-1)/2\) values qualify. For \(p=109\), the condition is \(p\equiv5\pmod8\); hence all \(108\) values qualify, contradicting the predicted \(54\).

## Verification
The standalone standard-library program `verify.py` checks every progression \(1\le A\le60\), \(0\le B<A\) against the first 100 positive terms whenever the theoretical criterion predicts universal divisibility. It also checks the exact cardinality of \(\mathcal B_{1,p}\) for all odd primes below \(200\), compares with the published \(p=3,5\) examples, and checks \(p=109\). Run `python3 verify.py`; its recorded output is `verification_output.txt`. The finite checks test implementation details; the unrestricted proof is the four-step symbolic argument above, relying on CRT and Dirichlet's theorem.

## Relationship to prior work
Merca, *Families of Ramanujan-Type Congruences Modulo 4 for the Number of Divisors* (2022), formulates the prime-square fibers \(\mathcal B_{r,p}\), conjectures a count for \(\mathcal B_{1,p}\), and proves individual cases for \(p=3,5\). This result classifies **all** progressions \(An+B\), rather than only a selected prime-square family. Its prime-square consequence corrects the conjectured dependence on whether \(p-1\) is cubefree: the decisive invariant is \(p\bmod8\). The originally proved examples are recovered but not counted as new. Related isolated cases for other odd residues \(r\) are specializations of the general criterion and are not separately claimed here.

## Limitations
No claim is made for modulus \(8\) or higher powers of \(2\), or for arbitrary non-linear progressions. The finite verifier does not establish infinitely many cases on its own. Novelty comparisons cannot rule out uncatalogued equivalent results or undiscovered stronger general theorems.

## References
1. M. Merca, *Families of Ramanujan-Type Congruences Modulo 4 for the Number of Divisors*, Axioms **11** (2022), 342, DOI: 10.3390/axioms11070342, published 2022-07-18, primary MSC 11A25. https://doi.org/10.3390/axioms11070342
2. Dirichlet's theorem on primes in reduced arithmetic progressions (classical; used only for the necessity construction).
