# Exact modulo-four rigidity and Cantor support for ternary Pascal-row integers

## Finding

Let \(\langle m\rangle_3\in\{0,1,2\}\) denote the least nonnegative residue of an integer \(m\) modulo \(3\). Define the integer obtained by interpreting the \(n\)th row of Pascal's triangle reduced modulo \(3\) as a base-three numeral,
\[
T(n)=\sum_{j=0}^{n}\left\langle\binom nj\right\rangle_3 3^j\qquad(n\ge0).
\]
For every nonnegative integer \(n\), its value modulo \(4\) belongs to \(\{0,1\}\), and a complete digit classification holds:
\[
T(n)\equiv1\pmod4
\quad\Longleftrightarrow\quad
\text{the ternary digits of }n\text{ lie in }\{0,2\}
\text{ with an even number of }2\text{s}.
\]
All other \(T(n)\) are divisible by \(4\). In particular, no term is congruent to \(2\) or \(3\) modulo \(4\); the same criterion determines precisely the odd terms.

There is a stronger exact integer identity. Let \(r\) denote the number of digits \(2\) in the ordinary base-three expansion of \(n\). Then
\[
\sum_{j=0}^{n}(-1)^j\left\langle\binom nj\right\rangle_3
=\begin{cases}
0,&\text{if a ternary digit of }n\text{ is }1,\\
(3-3^r)/2,&\text{otherwise}.
\end{cases}
\]
For each integer \(k\ge1\), the number of indices \(0\le n<3^k\) with \(T(n)\equiv1\pmod4\) is exactly \(2^{k-1}\). Thus their counting function satisfies
\[
\#\{0\le n\le X:T(n)\equiv1\pmod4\}
=\Theta\!\left(X^{\log_3 2}\right)\qquad(X\longrightarrow\infty),
\]
and the set has natural density zero. The ordinary generating function of its indicator is the formal power series
\[
\frac12\left[
\prod_{i\ge0}(1+z^{2\cdot3^i})
+\prod_{i\ge0}(1-z^{2\cdot3^i})
\right].
\]

## Assumptions and scope

All statements are unconditional and apply to every integer \(n\ge0\). We use the standard (un-padded) ternary expansion, with the empty representation of zero, whose number of \(2\)-digits is zero. The sequence \(T(n)\) is the ternary Pascal-row integer sequence catalogued as OEIS A173019 and studied in the cited 2022 work. Only residues modulo \(3\) are taken inside the binomial coefficients; the outer congruence is modulo \(4\). The displayed signed sum is an equality of ordinary integers, not merely a congruence.

## Proof

Put \(c_j=\langle\binom nj\rangle_3\). Let \(\chi\) be the nontrivial multiplicative character on \(\mathbb F_3\), extended by \(\chi(0)=0\), so \(\chi(1)=1\) and \(\chi(2)=-1\). Introduce the signed sums
\[
U(n)=\sum_{j=0}^n(-1)^j\mathbf 1_{c_j\ne0},
\qquad
V(n)=\sum_{j=0}^n(-1)^j\chi(c_j).
\]
The elementary identity \(c=(3\mathbf1_{c\ne0}-\chi(c))/2\), valid for each \(c\in\{0,1,2\}\), implies
\[
A(n):=\sum_{j=0}^n(-1)^jc_j=\frac{3U(n)-V(n)}2.
\]

Write \(n=\sum_{i=0}^{d}n_i3^i\) with \(n_i\in\{0,1,2\}\), allowing the empty product when \(n=0\). Lucas's theorem shows that \(c_j\ne0\) exactly when each ternary digit \(j_i\) of \(j\) satisfies \(0\le j_i\le n_i\), and then its residue modulo \(3\) is the product of the local residues \(\binom{n_i}{j_i}\pmod3\). Since \(3^i\) is odd, \((-1)^j=\prod_i(-1)^{j_i}\). Consequently both sums factor over the digits of \(n\):
\[
U(n)=\prod_i\sum_{b=0}^{n_i}(-1)^b,
\qquad
V(n)=\prod_i\sum_{b=0}^{n_i}(-1)^b\chi\!\left(\binom{n_i}{b}\right).
\]
For a digit \(n_i\) equal to \(0,1,2\), the local factors in the first product are respectively \(1,0,1\); those in the second are respectively \(1,0,3\). The value \(3\) in the latter follows from the residues \(1,2,1\) in the second binomial row and the signs \(1,-1,1\). Hence if a digit \(1\) occurs, \(U(n)=V(n)=0\). If no such digit occurs and \(r\) digits are \(2\), we have \(U(n)=1\), \(V(n)=3^r\). Substitution proves the exact signed-sum identity.

Because \(3\equiv-1\pmod4\), we have \(T(n)\equiv A(n)\pmod4\). When a digit \(1\) occurs, this is zero. Otherwise \(T(n)\equiv(3-3^r)/2\pmod4\). Using \(3^r\equiv1\pmod8\) for even \(r\) and \(3^r\equiv3\pmod8\) for odd \(r\), the residue is respectively \(1\) or \(0\). This proves the complete modulo-four classification, including \(n=0\), for which \(T(0)=1\).

Among the integers \(0\le n<3^k\), each is uniquely represented by a length-\(k\) ternary word, possibly padded with leading zeroes. Precisely \(2^{k-1}\) of the \(2^k\) words over \(\{0,2\}\) contain an even number of digit \(2\), for \(k\ge1\). For \(3^k\le X<3^{k+1}\), monotonicity bounds the count between \(2^{k-1}\) and \(2^k\), proving the stated power-law growth. Finally, for every finite set of positions, the corresponding product monomial uniquely encodes the ternary index with digit \(2\) in exactly those positions. Averaging the positive and alternating products deletes all terms with odd cardinality, establishing the formal generating function.

## Verification

The accompanying standalone Python program independently constructs each row of Pascal's triangle modulo \(3\) by Pascal's recurrence, evaluates the resulting numeral modulo \(4\), and compares it with the ternary digit predicate and the exact signed-sum formula. It also checks the exact counts on finite triadic ranges. This is a finite consistency test; the preceding Lucas-factorization argument proves the infinite result.

## Relationship to prior work

Mathonet, Rigo, Stipulanti, and Zénaïdi introduce and investigate the prime-base Pascal-row integer sequences, including the ternary sequence, and derive Lucas-based digit recursions. OEIS A173019 records the ternary sequence and examples of odd values. The present statement concerns a distinct exact modulo-four congruence, its complete set of exception-free digit criteria, and the precise growth of the residue-one indices. The factorization in the proof is directly motivated by Lucas's theorem but uses a signed quadratic character to turn the row's residue values into a closed signed-sum identity. The checked sources do not explicitly state this result; unseen equivalent formulations remain a publication-priority risk.

## Limitations

The congruence determines the residue modulo \(4\), not arbitrary higher powers of \(2\), and the counting law has no claimed leading constant for arbitrary \(X\). The proof does not assert analogous criteria for general prime bases. The mathematical result has not undergone independent review. The literature comparison is not an exhaustive uniqueness or priority guarantee.

## References

1. P. Mathonet, M. Rigo, M. Stipulanti, N. Zénaïdi, *On digital sequences associated with Pascal's triangle*, arXiv:2201.06636, first posted 17 January 2022, https://arxiv.org/abs/2201.06636.
2. OEIS Foundation, entry A173019, *Triangle of binomial coefficients modulo 3, read as a ternary number*, https://oeis.org/A173019 (accessed 19 October 2026).
3. É. Lucas, original digitwise congruence for binomial coefficients modulo primes (1878), as reproduced in Reference 1, Theorem 1.
