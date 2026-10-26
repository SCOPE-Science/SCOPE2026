# Eventual modular annihilation of primorial wheels and their prime-recurrence states

## Finding
Let \(p_1=2<p_2=3<\cdots\) be the primes, define the primorial \(P_k=\prod_{j=1}^{k+1}p_j\) for \(k\ge0\), and form its reduced-residue polynomial
\[
U_k(X)=\sum_{\substack{1\le a\le P_k\\\gcd(a,P_k)=1}}X^a\in\mathbb Z[X].
\]
**Theorem.** For every fixed pair of positive integers \(r,m\), there is an index \(K(r,m)\) such that
\[
U_k(X)\equiv0\pmod{m,\,X^r-1}\qquad(k\ge K(r,m)).
\]
Equivalently, for every residue \(j\pmod r\), the number of reduced residues \(a\in[1,P_k]\) with \(a\equiv j\pmod r\) is divisible by \(m\) once \(k\ge K(r,m)\). One may take \(K(r,m)\) to be the index at which the first prime congruent to \(1\pmod{mr}\) has entered the primorial (with the trivial case \(m=1\) unrestricted).

Let \(T_k\) denote the autonomous prime-generating integer state of Shunia and Prunescu [1], whose proved binary invariant is
\[
T_k=\sum_{\substack{2\le a\le P_k+1\\\gcd(a,P_k)=1}}2^a.
\]
For every fixed odd \(m\ge3\), writing \(r=\operatorname{ord}_m(2)\), the theorem gives the eventual exact congruence
\[
\boxed{T_k\equiv2\bigl(2^{P_k}-1\bigr)\pmod m.}
\]
In particular, \(P_{32}\) includes the prime \(137\equiv1\pmod{136}\), so for every \(k\ge32\),
\[
T_k\equiv\begin{cases}6\pmod{17}&P_k\equiv2\pmod8,\\7\pmod{17}&P_k\equiv6\pmod8.\end{cases}
\]
Both residues \(6\) and \(7\) occur infinitely often as \(k\) varies. Thus reduction of these growing binary states modulo \(17\) is eventually two-valued but does not converge.

## Assumptions and scope
All polynomial congruences are in \((\mathbb Z/m\mathbb Z)[X]/(X^r-1)\); equivalently, their coefficient sums over exponents congruent modulo \(r\) vanish modulo \(m\). The theorem concerns the full reduced-residue interval \(1\le a\le P_k\), including \(a=1\) and excluding \(a=P_k+1\). Its integer-state corollary concerns the corresponding binary encoding with those two endpoint positions exchanged. No assumption on \(\gcd(r,P_k)\), or on squarefreeness of \(r\) or \(m\), is needed. The state corollary is restricted to odd moduli because it uses the multiplicative order of \(2\).

## Proof
For squarefree \(L\ge2\), put
\[
U_L(X)=\sum_{\substack{1\le a\le L\\(a,L)=1}}X^a.
\]
If \(q\) is a prime not dividing \(L\), every reduced residue modulo \(Lq\) is one of the lifts \(a+tL\), with \(1\le a\le L\), \((a,L)=1\), and \(0\le t<q\), except for the unique lift divisible by \(q\). Those omitted lifts are exactly \(qa\) as \(a\) runs through the reduced residues modulo \(L\). Therefore the following identity holds in \(\mathbb Z[X]\):
\[
\tag{1} U_{Lq}(X)=U_L(X)\sum_{t=0}^{q-1}X^{tL}-U_L(X^q).
\]

Fix \(r,m\ge1\). When \(m=1\), the result is immediate. Otherwise Dirichlet's theorem supplies a prime \(q\equiv1\pmod{mr}\), and the ordered primorials eventually include this prime. For the product \(L\) of all smaller primes, work in \(A=(\mathbb Z/m\mathbb Z)[X]/(X^r-1)\). Because \(q-1\) is a multiple of \(mr\), the terms with \(1\le t<q\) in the geometric sum in (1) divide into \((q-1)/r\) consecutive blocks of length \(r\). Each block has the same sum in \(A\), as \(X^{rL}=1\), and the number of blocks is a multiple of \(m\). Hence
\[
\sum_{t=0}^{q-1}X^{tL}=1\quad\text{in }A.
\]
Also \(q\equiv1\pmod r\), so \(X^q=X\) in \(A\). Equation (1) now yields \(U_{Lq}(X)=U_L(X)-U_L(X)=0\) in \(A\).

To show persistence, note that if \(U_L(X)=0\) in \(A\) and \(s\nmid L\) is any further prime, then equation (1) gives \(U_{Ls}(X)=0\) in \(A\): the first term vanishes, and so does \(U_L(X^s)\), because substitution \(X\mapsto X^s\) preserves the ideal \((m,X^r-1)\). Applying this to every subsequent prime proves the theorem.

For the state formula, let \(W_k=U_k(2)\). The binary invariant of [1, Lemma 2.1 and the proof of Theorem 1.1] shows, by replacing the term \(2^1\) with \(2^{P_k+1}\), that
\[
\tag{2}T_k=W_k-2+2^{P_k+1}=W_k+2(2^{P_k}-1).
\]
For odd \(m\), set \(r=\operatorname{ord}_m(2)\). Evaluation \(X\mapsto2\pmod m\) factors through \(A\), because \(2^r\equiv1\pmod m\). Thus \(W_k\equiv0\pmod m\) for all sufficiently large \(k\), and equation (2) yields the displayed congruence.

For \(m=17\), \(\operatorname{ord}_{17}(2)=8\), and \(137\) is prime with \(137\equiv1\pmod{8\cdot17}\). It is the thirty-third prime, so the preceding argument applies for \(k\ge32\). Every primorial \(P_k\) is twice an odd integer and therefore \(P_k\equiv2\) or \(6\pmod8\). Direct modular exponentiation gives \(2(2^2-1)\equiv6\pmod{17}\) and \(2(2^6-1)\equiv7\pmod{17}\). Upon adjoining an odd prime congruent to \(3\pmod4\), the residue \(P_k\pmod8\) flips between \(2\) and \(6\). Dirichlet's theorem supplies infinitely many such primes, so both resulting residues modulo \(17\) occur infinitely often. This completes the proof.

## Verification
The standalone `verify.py` checks the lift-and-delete identity (1) against independently enumerated reduced residues for all primorials from \(2\) through \(2310\), using six residue moduli. It also checks the initial integer states \(8\), \(160\), and \(2693408896\), and tests exact modular vanishing after designated primes for four pairs of parameters, including \((r,m)=(8,17)\) at \(q=137\). For the explicit example, it computes the residues \(7\) and \(6\) at the stages ending in primes \(137\) and \(139\), respectively. Execute with `python3 verify.py` in a standard Python environment; the successful output begins `VERIFY_OK`. The infinite universal statement is proved above, not inferred from finite computations.

## Relationship to prior work
Shunia and Prunescu [1] establish the binary representation of the autonomous recurrence, its next-prime and prime-gap outputs, and twin-candidate counts. Their modulus-\(8\) test is applied to a normalized state for detecting twin-prime gaps; it is not a theorem about eventual reduction of the unnormalized state modulo arbitrary odd integers. Holt and Rudd [2] study the discrete dynamics of gap and constellation counts in primorial wheel cycles; their frequency recurrences neither state nor directly supply coefficientwise divisibility of the reduced-residue polynomial modulo every \((m,X^r-1)\). The new mechanism is the zeroing of every residue-count coordinate when a prime \(1\pmod{mr}\) is inserted, followed by permanence under further sieve stages.

## Limitations
The index \(K(r,m)\) obtained from the first prime in a progression need not be sharp, and no bound on the least such prime beyond classical existence is claimed. The congruence for the binary states concerns odd moduli, and says nothing about their \(2\)-adic valuations (studied in [1]). The binary states are not asserted to converge modulo every odd integer; the modulus-\(17\) example explicitly shows nonconvergence. An unindexed general theorem on modular wheel polynomials or finite-group-ring sieve dynamics could imply the first assertion; independent bibliographic priority review is outstanding.

## References
[1] J. M. Shunia and M. Prunescu, *Short Recurrences and Straight-Line Programs for Primes*, arXiv:2610.13365v1, first submitted 2026-10-09, Sections 1–2, particularly Lemma 2.1, Theorem 1.1, Corollary 2.2, and Proposition 2.7. https://arxiv.org/html/2610.13365v1

[2] F. B. Holt and H. Rudd, *On small gaps among primes*, arXiv:1312.7569, first submitted 2013-12-29, Sections 1–3 (primorial wheel and gap-constellation dynamics). https://arxiv.org/abs/1312.7569
