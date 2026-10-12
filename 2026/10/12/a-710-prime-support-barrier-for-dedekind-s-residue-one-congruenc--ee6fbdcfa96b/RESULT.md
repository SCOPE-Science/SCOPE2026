# A 710-prime-support barrier for Dedekind’s residue-one congruence
## Finding
Let \(\psi\) denote Dedekind's psi function,
\[
\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right),
\]
and let \(\omega(n)\) count the distinct prime divisors of \(n\).

**Theorem.** For every integer \(n>1\) with
\[
\omega(n)\le709,
\]
one has
\[
\psi(n)\equiv1\pmod n
\quad\Longleftrightarrow\quad
n\text{ is prime}.
\]
Equivalently, any composite counterexample to the prime-only conjecture for the residue of Dedekind's psi function must be an **odd squarefree integer with at least \(710\) distinct prime factors**.

The integer \(710\) is a certified sufficient lower bound, not an assertion of optimality or of the existence of a composite counterexample.

## Assumptions and scope
The Dedekind function is multiplicative, with prime-power factors
\[
\psi(p^a)=p^{a-1}(p+1),\qquad a\ge1.
\]
For squarefree integers,
\[
\psi(n)=\sigma(n)=\prod_{p\mid n}(p+1).
\]
The exact residue sequence is OEIS A253628. On squarefree inputs it coincides with the earlier divisor-sum residue sequence OEIS A054024. The result is about their **residue-one** fibers, not the zero-residue or divisor-average problem.

The proof uses a complete finite certificate on the first \(709\) eligible primes for each compatible pattern of intersection with
\[
B=\{3,5,7,11,13\}.
\]
No search bound is imposed on the integer \(n\) itself.

## Proof
Let \(n>1\) be composite and suppose, toward a contradiction, that
\[
\psi(n)\equiv1\pmod n,\qquad \omega(n)\le709.
\tag{1}
\]

**Reduction to odd squarefree numbers.** If \(p^a\parallel n\) with \(a\ge2\), then the multiplicative prime-power formula shows \(p\mid\psi(n)\). This contradicts (1) modulo \(p\). Thus \(n\) is squarefree. If \(n\) is even and composite, at least one odd prime also divides it; then \(\psi(n)=\prod_{p\mid n}(p+1)\) is even, contradicting (1) modulo \(2\). Therefore \(n\) is odd and squarefree.

For such a composite \(n\), the equality \(\psi(n)=\sigma(n)\) shows
\[
\psi(n)>n+1,
\]
since \(\sigma(n)\) includes at least two proper divisors besides \(1\). The integer
\[
k=\frac{\psi(n)-1}{n}
\]
is therefore greater than \(1\). Because \(n\) is odd and \(\psi(n)=\prod_{p\mid n}(p+1)\) is even, \(k\) is odd. Consequently \(k\ge3\), forcing the strict **abundancy obstruction**
\[
\prod_{p\mid n}\left(1+\frac1p\right)
=\frac{\psi(n)}n=k+\frac1n>3.
\tag{2}
\]

**Local forbidden residues.** If \(r\) and \(q\) are distinct prime divisors of \(n\) with
\[
q\equiv-1\pmod r,
\]
then \(r\mid(q+1)\mid\psi(n)\), contradicting \(\psi(n)\equiv1\pmod r\). Hence
\[
q\not\equiv-1\pmod r
\quad\text{for all distinct primes }r,q\mid n.
\tag{3}
\]

Set \(B=\{3,5,7,11,13\}\) and \(S=B\cap\{p:p\mid n\}\). The set \(S\) must be **compatible**, meaning no two distinct elements of \(S\) violate (3). For each compatible \(S\), define the increasing sequence of eligible primes \(q_{S,1}<q_{S,2}<\cdots\) as follows: an odd prime \(q\) is eligible exactly when (i) \(q\in B\) if and only if \(q\in S\), and (ii) \(q\not\equiv-1\pmod r\) for all \(r\in S\) with \(r\ne q\). Every prime divisor of \(n\) belongs to this eligible sequence.

If \(\omega(n)=t\le709\), monotonicity of \(1+1/q\) gives
\[
\frac{\psi(n)}n
\le\prod_{j=1}^{t}\left(1+\frac1{q_{S,j}}\right)
\le\prod_{j=1}^{709}\left(1+\frac1{q_{S,j}}\right)
=:R_S.
\tag{4}
\]
Indeed, the \(j\)-th smallest prime divisor of \(n\) cannot be smaller than the \(j\)-th eligible prime, and each additional factor is greater than \(1\).

**Exhaustive finite rational certificate.** There are \(32\) subsets of \(B\), of which exactly \(15\) are compatible. The following table gives every compatible \(S\), together with its \(709\)-th eligible prime. For each row the exact integer inequality
\[
\prod_{j=1}^{709}(q_{S,j}+1)
<3\prod_{j=1}^{709}q_{S,j}
\tag{5}
\]
is checked by the self-contained attached `certify.py` using a complete Eratosthenes prime sieve and arbitrary-precision integers.

| Compatible \(S\) | \(q_{S,709}\) |
|:--|--:|
| \(\varnothing\) | 5417 |
| \(\{3\}\) | 11959 |
| \(\{5\}\) | 7457 |
| \(\{7\}\) | 6619 |
| \(\{3,7\}\) | 14731 |
| \(\{5,7\}\) | 9103 |
| \(\{11\}\) | 6073 |
| \(\{5,11\}\) | 8311 |
| \(\{7,11\}\) | 7481 |
| \(\{5,7,11\}\) | 10193 |
| \(\{13\}\) | 5903 |
| \(\{3,13\}\) | 13159 |
| \(\{5,13\}\) | 8243 |
| \(\{11,13\}\) | 6661 |
| \(\{5,11,13\}\) | 9161 |

All fifteen strict inequalities (5) hold. The largest value of \(R_S\), compared as an exact rational number rather than a floating-point approximation, occurs at \(S=\{11,13\}\) and is approximately
\[
R_{\{11,13\}}=2.999709655050253636\ldots<3.
\]
For this worst branch the analogous product with \(710\) eligible factors first exceeds \(3\); this explains the cutoff for the stated five-prime sieve, without claiming a globally optimal lower bound.

Equations (4) and (5) imply \(\psi(n)/n<3\), contradicting (2). Therefore no composite \(n\) with at most \(709\) distinct prime factors satisfies (1). Conversely, for every prime \(p\), \(\psi(p)=p+1\equiv1\pmod p\). This proves the theorem.

## Verification
`certify.py` is a standalone, deterministic Python 3 verification program. It enumerates all \(32\) subsets of \(B\), rejects exactly the incompatible ones using (3), generates the first \(709\) eligible primes for each of the remaining \(15\) branches, and checks every inequality (5) by integer multiplication. It also verifies the largest rational product and its cutoff, and independently checks direct Dedekind-psi residues for integers through \(100{,}000\). No third-party package or external file is needed.

The exhaustive finite branch certificate supports the *unrestricted* theorem because (4) dominates every possible prime support of size at most \(709\), regardless of the magnitude of \(n\). The direct scan through \(100{,}000\) is corroborative only.

## Relationship to prior work
OEIS A253628 defines exactly the residue \(\psi(n)\bmod n\) and notes the conjecture that residue \(1\) occurs only at prime indices. The entry provides direct term tables and programs but no lower bound of \(710\) distinct prime factors for composite exceptions.

OEIS A001615 defines the Dedekind psi function and records its multiplicative product. OEIS A054024, first authored in January 2000, records \(\sigma(n)\bmod n\). The two residue sequences agree on squarefree inputs; the initial reduction in the proof makes this an exact alternative formulation for any hypothetical composite solution. Neither inspected entry states the quantified prime-support obstruction or the fifteen-branch residue sieve.

Alzer and Kwong, *Inequalities for the arithmetical functions of Euler and Dedekind*, study exponentiated inequalities for the normalized functions \(\varphi(n)/n\) and \(\psi(n)/n\). Their public full paper is classified under primary MSC 11A25. Its theorem statements and proof do not treat the congruence \(\psi(n)\equiv1\pmod n\) or exclusion by support size.

Searches under Dedekind-psi residue one, squarefree divisor-sum residue one, congruence aliases, and the prime-support bound located no stronger covering theorem. The closest indexed low-support obstructions concern different arithmetic predicates and do not imply (1)–(5).

## Limitations
The theorem gives a **necessary condition**, not a composite construction and not a proof of the prime-only conjecture for unrestricted integers. The number \(710\) is not asserted to be the best possible support threshold. The certificate uses only five small-prime local residue restrictions, and stronger exclusions may be obtained by a deeper compatible-support sieve.

The main originality risk is a related obstruction in unindexed discussions of the two residue sequences. The public database entries and the inspected arithmetic-inequality paper do not exhibit a result that implies the theorem.

## References
1. OEIS Foundation, A054024, “Sum of the divisors of \(n\) reduced modulo \(n\),” authored 19 January 2000.
2. OEIS Foundation, A253628, “\(a(n)=\psi(n)\bmod n\),” authored 6 January 2015.
3. OEIS Foundation, A001615, Dedekind psi function and its Euler product.
4. H. Alzer and M. K. Kwong, “Inequalities for the arithmetical functions of Euler and Dedekind,” *Czechoslovak Mathematical Journal* 70 (2020), 781–791, DOI 10.21136/CMJ.2020.0530-18.
