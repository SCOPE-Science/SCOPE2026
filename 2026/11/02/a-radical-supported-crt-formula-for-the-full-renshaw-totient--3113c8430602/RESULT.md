# A radical-supported CRT formula for the full Renshaw totient

## Finding
Let \(T(n)\) count odd integers \(t\) in \([1,n]\) such that \(\gcd(t,n)=\gcd((t-1)/2,n)=1\), with \(T(1)=0\). For an odd integer \(m>1\), put \(R=\operatorname{rad}(m)\) and \(S(m)=m\prod_{p\mid m}(1-2/p)\). Form the set of ordered divisor pairs
\[
\mathcal D(R)=\{(a,b):a,b\mid R,\ \gcd(a,b)=1\}.
\]
For each pair, let \(M=ab\) and choose the unique \(\rho_{a,b}\in\{1,\ldots,M\}\) satisfying \(\rho_{a,b}\equiv0\pmod a\) and \(\rho_{a,b}\equiv1\pmod b\). In particular \(\rho_{1,1}=1\). Define
\[
\eta(t)=\begin{cases}1&t\equiv3\pmod4,\\-1&t\equiv1\pmod4,\\0&2\mid t,\end{cases}
\]
\[
E_0(R)=\sum_{(a,b)\in\mathcal D(R)}\mu(a)\mu(b)(-1)^{\rho_{a,b}+1},\quad
E_1(R)=\sum_{(a,b)\in\mathcal D(R)}\mu(a)\mu(b)\bigl(\eta(\rho_{a,b})+\eta(\rho_{a,b}+ab)\bigr).
\]
For every integer \(e\ge0\), the **exact evaluation at every modulus** \(2^e m>1\) is
\[
\boxed{T(2^e m)=\begin{cases}(S(m)+E_0(R))/2,&e=0,\\(S(m)+E_1(R))/2,&e=1,\\2^{e-2}S(m),&e\ge2.\end{cases}}
\]
For the remaining odd part \(m=1\), the values are \(T(1)=T(2)=0\) and \(T(2^e)=2^{e-2}\) for \(e\ge2\). The corrections \(E_0,E_1\) depend only on the set of odd prime factors, **not their exponents**, and each has at most \(3^{\omega(m)}\) explicitly computable summands. In the arithmetic-operation model, given the prime factorization, evaluation takes \(O(3^{\omega(m)}\operatorname{poly}(\log m))\) bit operations.

For distinct odd primes \(p,q\), writing \(u\) for the least positive inverse of \(p\) modulo \(q\), the two-prime correction has the explicit branch rule
\[
\boxed{T(p^a q^b)=\frac{p^{a-1}q^{b-1}(p-2)(q-2)-1}{2}+(-1)^{u+1}\qquad(a,b\ge1).}
\]
For each fixed odd prime \(p\), each sign occurs for precisely half of the primes \(q\ne p\), in natural relative density among primes.

## Assumptions and scope
All integers and congruences are ordinary; \(p\) denotes a prime, \(\mu\) the Möbius function, and \(\omega(m)\) the number of distinct prime divisors of \(m\). Empty products equal one. The statement includes all positive moduli and all exponents of their prime factors. Factorization is supplied to the algorithm, not computed in the stated complexity. Nothing here asserts a new factorization algorithm or a cryptographic security property.

## Proof
**Step 1: local two-residue sieve.** Let \(F_m(t)\) be one when \(\gcd(t(t-1),m)=1\) and zero otherwise. For each prime \(p\mid m\), the two events \(p\mid t\) and \(p\mid t-1\) are disjoint. Expanding their product gives the exact integer identity
\[
F_m(t)=\prod_{p\mid m}\bigl(1-\mathbf1_{p\mid t}-\mathbf1_{p\mid t-1}\bigr)
=\sum_{(a,b)\in\mathcal D(R)}\mu(a)\mu(b)\mathbf1_{a\mid t}\mathbf1_{b\mid t-1}.
\]
The Chinese remainder theorem makes each pair's constraints a single residue class \(\rho_{a,b}\pmod{ab}\); the canonical representative is well defined even for \(a=b=1\). Also, summing \(F_m\) over one complete period of length \(m\) yields the Schemmel value \(S(m)\), by the ordinary Chinese remainder theorem.

**Step 2: odd moduli.** Since \(m\) is odd, \(t\) is counted by \(T(m)\) exactly when \(F_m(t)=1\) and \(t\) is odd. Therefore
\[
2T(m)-S(m)=\sum_{t=1}^{m}(-1)^{t+1}F_m(t).
\]
For a fixed \((a,b)\), the solutions in \([1,m]\) are \(t=\rho_{a,b}+jM\), with \(0\le j<m/M\). Both \(M\) and \(m/M\) are odd, hence the alternating-sign sum equals \((-1)^{\rho_{a,b}+1}\). Expanding \(F_m\) proves the first formula.

**Step 3: twice an odd modulus.** If \(t\) is odd, the conditions \(\gcd(t,2m)=\gcd((t-1)/2,2m)=1\) amount to \(F_m(t)=1\) and \(t\equiv3\pmod4\). Among \(1\le t\le2m\), precisely \(S(m)\) acceptable values of \(F_m(t)\) are odd: pair each residue \(t\in[1,m]\) with \(t+m\), which has opposite parity. Consequently
\[
2T(2m)-S(m)=\sum_{t=1}^{2m}\eta(t)F_m(t).
\]
For a fixed pair, the contributing \(t\) are \(\rho_{a,b}+jM\), \(0\le j<2m/M\). Here \(2m/M\equiv2\pmod4\). Since \(M\) is odd, the sequence \(j\mapsto\eta(\rho_{a,b}+jM)\) has period four and each full period sums to zero; its remaining two terms sum to \(\eta(\rho_{a,b})+\eta(\rho_{a,b}+M)\). This proves the second formula and exponent-independence of both correction terms.

**Step 4: higher powers of two.** For \(e\ge2\), fix an admissible class \(r\pmod m\), of which there are \(S(m)\). Its \(2^e\) lifts in \([1,2^e m]\) each lie in one of the four classes modulo four equally often because \(m\) is odd. Exactly \(2^{e-2}\) lifts have residue three modulo four. This proves the third formula, including \(m=1\). The exceptions \(T(1)=T(2)=0\) follow immediately from the definition.

**Step 5: the semiprime branch and its frequency.** When \(R=pq\) the two unassigned, four singly assigned and two doubly assigned unmixed terms of \(E_0\) total \(-1\). The two mixed CRT terms both equal \((-1)^{u+1}\). Indeed if \(v\) is the least positive inverse of \(q\pmod p\), then \(pu+qv=pq+1\), and \(u,v\) have the same parity. Hence \(E_0(pq)=-1+2(-1)^{u+1}\), yielding the asserted formula. For fixed \(p\), \(v\) runs bijectively over \(1,\ldots,p-1\) as \(q\) runs over the nonzero residue classes modulo \(p\); exactly half those representatives are odd. The prime number theorem in arithmetic progressions supplies asymptotically equal prime counts in these classes, and therefore both branches have prime-relative density \(1/2\).

The number of ordered divisor pairs is exactly \(3^{\omega(m)}\) (each prime belongs to \(a\), to \(b\), or to neither). Each CRT representative is computed from the modular inverse \(a^{-1}\pmod b\) when \(a,b>1\), with elementary conventions otherwise. The complexity claim follows.

## Verification
The standalone `verify.py` implements the formulas by exact integer arithmetic and compares every \(T(n)\) for \(1\le n\le2000\) against literal enumeration. It additionally compares both correction sums to direct signed admissible-residue counts for all odd \(m\le999\), verifies invariance upon replacing the odd part by its radical, and checks the two-prime branch for all ordered distinct odd primes below \(100\). Run with `python3 verify.py`. These tests are finite checks; Steps 1–5 supply the unrestricted proof.

## Relationship to prior work
J. Renshaw, *A Totient Function Associated with Variants of Groups* (arXiv:2603.13939v1, March 14, 2026), defines \(T\), establishes the Schemmel comparison and exact prime-power and \(2^e\) cases, and gives finite error bounds for general odd parts. The uniform explicit radical-supported evaluations above replace the remaining bounds with exact CRT sums and resolve the two-prime branch by a canonical modular inverse, with a prime-density refinement. Classical Schemmel totients and the Chinese remainder theorem are used, not claimed to be novel. A. M. Salazar, *Restricted Coprime Representations Modulo 6P: Exact CRT Formulas and Positivity Thresholds* (arXiv:2609.22305v2), employs related \(3^r\)-term CRT sieves for a different additive-representation count; its formulas do not evaluate the present totient or its parity corrections.

## Limitations
The expression needs the distinct prime factors of the odd part and may require exponentially many terms in their count; no optimal-complexity assertion is made. The branch-density corollary uses the classical prime number theorem in progressions. Mathematical priority outside the inspected literature is not fully settled; independently published derivations may exist. There is no independent audit or formal verification.

## References
1. J. Renshaw, *A Totient Function Associated with Variants of Groups*, arXiv:2603.13939v1 (2026-03-14), https://arxiv.org/pdf/2603.13939.
2. A. M. Salazar, *Restricted Coprime Representations Modulo 6P: Exact CRT Formulas and Positivity Thresholds*, arXiv:2609.22305v2 (2026-10-03), https://arxiv.org/pdf/2609.22305.
3. J. F. Schemmel, original generalization of Euler's totient (1869), as cited and described in reference 1.
