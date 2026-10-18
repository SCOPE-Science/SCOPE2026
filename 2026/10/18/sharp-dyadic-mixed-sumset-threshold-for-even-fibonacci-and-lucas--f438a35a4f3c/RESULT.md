# Sharp dyadic mixed-sumset threshold for even Fibonacci and Lucas numbers

## Finding

Let \(F_0=0\), \(F_1=1\), \(L_0=2\), \(L_1=1\), with both sequences satisfying \(X_{n+2}=X_{n+1}+X_n\). For each integer \(m\ge3\), work in \(R_m=\mathbb Z/2^m\mathbb Z\), and let
\[
\mathcal F_m=\{F_{3j}\bmod2^m:j\ge1\},\qquad
\mathcal L_m=\{L_{3j}\bmod2^m:j\ge1\}.
\]
(The index restriction picks precisely the even-valued terms of each sequence.) For sumsets in \(R_m\), the exact identities are
\[
\boxed{\mathcal F_m+\mathcal L_m
=\{x\in R_m:x\equiv2,4,6\pmod8\},}
\]
\[
\boxed{\mathcal F_m+\mathcal F_m+\mathcal L_m
=\mathcal F_m+\mathcal L_m+\mathcal L_m
=2R_m.}
\]
In particular, the two-term mixed sumset misses precisely the \(2^{m-3}\) classes divisible by eight, while either three-term mixed composition represents every even class. Three is therefore the sharp universal number of even-valued Fibonacci/Lucas summands required for these two mixed compositions to be locally complete at all dyadic moduli \(2^m\) with \(m\ge3\). Repeated terms and arbitrary positive indices are permitted.

## Assumptions and scope

The theorem concerns residue-class sumsets, not representations by small positive integers and not representations involving odd-valued Fibonacci/Lucas terms. It holds for every \(m\ge3\) without a size bound on the indices, and makes no claim of new prime-representation asymptotics. The restriction \(3\mid j\) is equivalent to evenness of \(F_j\) and \(L_j\), by reducing the recurrence modulo two. For \(m\le2\), the displayed two-term obstruction is not present and the asserted threshold is not intended.

## Proof

**A dyadic lifting lemma.** Let \(G_t=F_{6t}/8\) for integers \(t\ge0\). The identities \(F_0=0\), \(F_6=8\), and \(L_6=18\) give
\[
G_0=0,\quad G_1=1,\quad G_{t+2}=18G_{t+1}-G_t.
\]
Consequently the formal power series generating function and its coefficient expansion are
\[
\sum_{t\ge0}G_tz^t=\frac z{1-18z+z^2}
=\frac z{(1-z)^2}\sum_{j\ge0}\frac{16^jz^j}{(1-z)^{2j}},
\qquad
G_t=\sum_{j\ge0}16^j\binom{t+j}{2j+1}.
\]
Here binomial coefficients are zero when the lower argument exceeds the nonnegative upper argument, so each sum is finite. For \(r,t\ge0\), Vandermonde's identity gives
\[
\binom{t+2^r+j}{2j+1}-\binom{t+j}{2j+1}
=\sum_{i=1}^{\min(2^r,2j+1)}\binom{2^r}{i}\binom{t+j}{2j+1-i}.
\]
For \(1\le i\le2^r\), the integer identity
\(i\binom{2^r}{i}=2^r\binom{2^r-1}{i-1}\) implies
\(\nu_2\binom{2^r}{i}\ge r-\nu_2(i)\).
Thus for \(j\ge1\), every summand after multiplying by \(16^j\) is divisible by \(2^{r+3}\), since
\[
4j-\lfloor\log_2(2j+1)\rfloor\ge3.
\]
The \(j=0\) term is exactly \(t\). Hence
\[
G_{t+2^r}-G_t\equiv2^r\pmod{2^{r+1}}.\tag{1}
\]
Starting from the single residue modulo one, this congruence inductively shows that \(G_0,\ldots,G_{2^r-1}\) run through all residues modulo \(2^r\): every pair of indices \(t\) and \(t+2^r\) represents the two different lifts of the same class. Therefore, for every \(m\ge3\),
\[
\boxed{\{F_{6t}\bmod2^m:t\ge1\}=8R_m.}\tag{2}
\]
For the zero residue, take \(t=2^{m-3}\), so restricting from nonnegative to positive indices does not remove it.

Define \(J_t=L_{6t+3}/4\) for \(t\ge0\). Both \(J_t\) and \(G_t+G_{t+1}\) satisfy the recurrence with coefficient 18, and their first two terms are respectively \(1,19\), so
\[
J_t=G_t+G_{t+1}.
\]
The stronger divisibility \(2^{r+3}\) for the terms with \(j\ge1\) in the binomial argument above gives
\[
J_{t+2^r}-J_t\equiv2^{r+1}\pmod{2^{r+2}}.\tag{3}
\]
Since \(J_0=1\), induction on \(r\) now proves that \(J_0,\ldots,J_{2^r-1}\) represent every **odd** residue modulo \(2^{r+1}\) exactly once. Multiplying by four gives
\[
\boxed{\{L_{6t+3}\bmod2^m:t\ge0\}=
\{x\in R_m:x\equiv4\pmod8\}.}\tag{4}
\]

**Only three residue types are possible.** Every even Fibonacci number has index divisible by three. The subsequences \(F_{6t}\) and \(F_{6t+3}\) satisfy the recurrence \(X_{t+2}=18X_{t+1}-X_t\). Since their first two values are \(0,8\) and \(2,34\), respectively, reduction modulo eight gives the residues \(0\) and \(2\). Similarly \(L_{6t}\) has initial terms \(2,18\) and is always \(2\pmod8\), whereas \(L_{6t+3}\) begins with \(4,76\) and is always \(4\pmod8\). Consequently,
\[
\mathcal F_m\bmod8=\{0,2\},\qquad
\mathcal L_m\bmod8=\{2,4\}.
\]
The mixed sumset therefore has no class \(0\pmod8\) and can only have classes \(2,4,6\pmod8\).

**All permitted classes occur.** For any target \(x\equiv2\pmod8\), use the fixed Lucas summand \(L_6=18\) and choose \(F_{6t}\equiv x-18\pmod{2^m}\) by (2). For \(x\equiv4\pmod8\), use \(L_3=4\) and (2). For \(x\equiv6\pmod8\), use \(F_3=2\) and choose \(L_{6t+3}\equiv x-2\pmod{2^m}\) by (4). This proves the exact two-term sumset identity.

**Sharp completion by one further term.** Put \(S_m=\mathcal F_m+\mathcal L_m\). As proved, \(S_m\) comprises *every lift* of the three residue classes \(2,4,6\pmod8\). Adding \(F_3=2\) covers every class \(0,4,6\pmod8\), and adding \(F_6=8\) covers every class \(2,4,6\pmod8\). Thus \(S_m+\mathcal F_m=2R_m\). Adding instead \(L_3=4\) covers \(0,2,6\pmod8\), while adding \(L_6=18\) covers \(0,4,6\pmod8\); hence \(S_m+\mathcal L_m=2R_m\). All summands in both constructions are even, so no odd class can occur. Finally, \(S_m\) misses the zero class modulo eight, proving that two mixed summands do not suffice. This completes the proof.

## Verification

The independent script `verify.py` recomputes residue sets of both recurrences from their defining recursion modulo \(2^m\), checks the two mixed-sumset identities for every \(3\le m\le12\), and tests 576 instances of lifting congruences (1) and (3). It prints `VERIFY_OK modulus_exponents=10 shift_congruences=576 largest_modulus=4096`. The finite calculation corroborates but is not used to prove the infinitely many modular identities.

## Relationship to prior work

Shen and Xu (2026) obtain large-integer representations involving two primes and five mixed Fibonacci-Lucas summands; their parity-resolved recurrence sums motivate determining precise local sumsets of even summands. The present theorem isolates the complete mixed two/three-summand obstruction at every power of two and neither asserts nor follows from a prime-pair asymptotic. Park and coauthors (2020) establish representations by a varying number of Fibonacci or Lucas terms subject to index restrictions, which does not determine fixed mixed-summand images modulo powers of two. Southwick (2014) studies residue completeness for single Gibonacci sequences, not the exact mixed sumsets or the sharp three-summand threshold. The OEIS entries A066853 and A066981 tabulate counts of residues of the individual sequences, not these mixed restricted sumsets.

## Limitations

This is a local theorem: the indices witnessing a residue may depend on the modulus, and neither bounded-index representation nor a global fixed-three-summand integer theorem follows. The proof is independent of but compatible with classical Pisano-period information; an earlier implicit derivation from detailed residue distribution theory remains possible. No independent audit has been performed.

## References

1. Z. Shen and C. Xu, *Two Primes and Five Mixed Fibonacci–Lucas Summands*, arXiv:2610.12291v1 (public 2026-10-08), https://arxiv.org/html/2610.12291v1.
2. H. Park, B. Cho, D. Cho, Y. D. Cho and J. Park, *Representation of Integers as Sums of Fibonacci and Lucas Numbers*, Symmetry **12** (2020), article 1625, https://doi.org/10.3390/sym12101625.
3. J. T. Southwick, *The Lucas Numbers and other Gibonacci Sequences mod m*, arXiv:1402.0598 (2014), https://arxiv.org/abs/1402.0598.
4. OEIS A066853, *Number of different remainders for the Fibonacci numbers modulo n*, https://oeis.org/A066853; and OEIS A066981, *Number of residues of Lucas numbers modulo n*, https://oeis.org/A066981.
