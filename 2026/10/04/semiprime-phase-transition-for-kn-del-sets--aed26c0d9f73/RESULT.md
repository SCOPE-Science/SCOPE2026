# Semiprime phase transition for Knödel sets
## Finding
For a positive integer \(k\), define the Knödel set \(K_k\) to consist of the
composite integers \(m>k\) such that
\[
a^{m-k}\equiv1\pmod m
\]
for every integer \(a\) coprime to \(m\).

Let \(p<q\) be distinct primes. Then
\[
pq\in K_k
\]
if and only if exactly one of the following two alternatives holds:

1. \(p=k\), hence \(k\) is prime, and
   \[
   q\equiv1\pmod{k-1};
   \]
2. \(p<q<k\), \(pq>k\), and
   \[
   p-1\mid k-q,\qquad q-1\mid k-p.
   \]

Therefore \(K_k\) contains infinitely many squarefree semiprimes if and only if
\(k\) is prime.

More quantitatively, let \(N_k(x)\) denote the number of products \(pq\le x\)
with distinct primes \(p<q\) and \(pq\in K_k\). If \(k\) is prime, then
\[
N_k(x)\sim\frac{x}{k\varphi(k-1)\log x}.
\]
If \(k\) is composite, then \(N_k(x)\) is eventually constant.

## Assumptions and scope
Only squarefree semiprimes are classified here. Prime squares and integers with
three or more prime factors are not part of the theorem.

The Carmichael function \(\lambda(m)\) is the exponent of the unit group
\((\mathbb Z/m\mathbb Z)^\times\). Thus the defining Knödel condition is
equivalent to
\[
\lambda(m)\mid m-k.
\]
For distinct primes \(p,q\),
\[
\lambda(pq)=\operatorname{lcm}(p-1,q-1).
\]

The asymptotic statement uses the prime number theorem for arithmetic
progressions in the fixed progression \(1\pmod{k-1}\).

## Proof
Let \(m=pq\) with distinct primes \(p<q\). The defining condition for \(K_k\) is
equivalent to
\[
\operatorname{lcm}(p-1,q-1)\mid pq-k.
\]
Equivalently,
\[
p-1\mid pq-k,\qquad q-1\mid pq-k.
\]
Since \(p\equiv1\pmod{p-1}\) and \(q\equiv1\pmod{q-1}\), these become
\[
p-1\mid q-k,\qquad q-1\mid p-k. \tag{1}
\]

The second divisibility in (1) forces a sharp trichotomy.

If \(p>k\), then
\[
0<p-k<q-1,
\]
so \(q-1\mid p-k\) is impossible.

If \(p=k\), then \(k\) is prime and the second divisibility is automatic. The
first becomes
\[
k-1\mid q-k,
\]
which is equivalent to
\[
q\equiv1\pmod{k-1}.
\]

Finally suppose \(p<k\). If \(q\ge k\), then
\[
0<k-p<q-1,
\]
again contradicting \(q-1\mid p-k\). Hence \(q<k\). In this case (1) is
equivalent to
\[
p-1\mid k-q,\qquad q-1\mid k-p.
\]
The extra condition \(pq>k\) is exactly the defining size condition for
membership in \(K_k\).

This proves the classification.

If \(k\) is composite, the first alternative cannot occur, while the second
has \(p<q<k\); hence only finitely many squarefree semiprimes can belong to
\(K_k\).

If \(k\) is prime, Dirichlet's theorem gives infinitely many primes
\[
q\equiv1\pmod{k-1}.
\]
All sufficiently large such primes satisfy \(q>k\), and every corresponding
product \(kq\) belongs to \(K_k\). Thus infinitely many squarefree semiprimes
occur.

For fixed prime \(k\), all semiprime solutions not belonging to the family
\(kq\) lie in the finite region \(p<q<k\). Therefore
\[
N_k(x)
=
\pi\!\left(\frac{x}{k};k-1,1\right)+O_k(1).
\]
The prime number theorem for arithmetic progressions yields
\[
\pi(y;k-1,1)\sim\frac{y}{\varphi(k-1)\log y},
\]
and hence
\[
N_k(x)\sim\frac{x}{k\varphi(k-1)\log x}.
\]

## Verification
The proof is symbolic and complete for all positive \(k\).

The accompanying checker independently compares the classification against the
Carmichael-function criterion
\[
\operatorname{lcm}(p-1,q-1)\mid pq-k
\]
for every \(1\le k\le200\) and every pair of distinct primes
\(p<q\le997\). It also verifies the first several semiprime members for the
small Knödel sets \(K_2,K_3,K_5,K_7\). These computations corroborate the
algebraic classification; they are not used to prove infinitude or the
asymptotic formula.

## Relationship to prior work
The classical Knödel family generalizes Carmichael numbers. Makowski proved in
1962/63 that \(K_k\) is infinite for every fixed \(k\ge2\), but that theorem
does not identify the prime-factor complexity of those members.

The 2017 paper of Castillo and Caranguay Mainguez reformulates Knödel membership
through the condition that every unit modulo \(m\) is an \((m-k)\)-unit. Its
full text treats Knödel sets as a connection of the general \(k\)-unit
framework, but does not state a semiprime classification; targeted full-text
searches for "semiprime" and "two prime" return no occurrence.

The exact OEIS tables for \(K_2,K_3,K_5,K_7\) visibly exhibit the prime-index
families described here: for example, \(K_3\) contains \(3q\) for odd primes
\(q>3\), and \(K_5\) contains \(5q\) when \(q\equiv1\pmod4\). The tables do
not state the uniform classification for arbitrary \(k\), the finite/infinite
prime-index dichotomy, or the counting asymptotic.

## Limitations
The theorem is restricted to products of two distinct primes. It does not
classify prime powers or members with at least three prime factors.

The historical Makowski article was identified bibliographically but no
machine-readable full text was available in the inspected sources. The later
Castillo--Caranguay Mainguez primary paper was inspected in full-text HTML and
used for the closest statement comparison. A poorly indexed source could still
contain the same short semiprime deduction.

The exact public date used in the metadata is the creation date of the dated
PlanetMath Knödel-number entry. The much earlier Makowski source is historically
prior, but the inspected bibliographic records give only the volume year
1962/63, not an exact public day.

## References
1. A. Makowski, "Generalization of Morrow's D-Numbers", Simon Stevin 36
   (1962/63), 71.
2. John H. Castillo and Jhony Fernando Caranguay Mainguez, "The set of
   \(k\)-units modulo \(n\)", arXiv:1708.06812v1, 22 August 2017; Involve 15
   (2022), 367--378.
3. PlanetMath, "Knödel number", entry created 22 March 2013, classification
   11A51.
4. OEIS A050990, A033553, A050993, A208155, Knödel-number tables for
   \(k=2,3,5,7\).
