# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces the theorem to two local facts about a summand
\[
F_N(k)=\binom{N+k-1}{k}^A\binom{2k}{k}^B
\binom{2(N-k)}{N-k}^C.
\]

The first is the valuation bound
\[
\nu_p F_N(k)\ge (A+1)(r-\nu_p(k))_+
\]
for \(N=mp^r\), \(p\nmid m\). The shifted-binomial contribution follows
from
\[
\binom{N+k-1}{k}=\frac Nk\binom{N+k-1}{k-1}.
\]
The remaining valuation comes from the two central binomial factors.
After dividing \(k\) and \(N-k\) by \(p^s\), with
\(s=\nu_p(k)<r\), their residues are complementary modulo each
\(p^j\), \(1\le j\le r-s\). Legendre's formula for
\(\nu_p\binom{2z}{z}\) then gives exactly one carry contribution between
the two factors at each such level.

The second fact is the scale relation for \(p\mid k\):
\[
F_N(k)=\lambda F_{N/p}(k/p),\qquad
\lambda\equiv1\pmod{p^{3\min(r,\nu_p(k))}}.
\]
For the shifted factor this follows from
\[
\binom{N+k-1}{k}
=\frac{N}{N+k}\binom{N+k}{N},
\]
whose prefactor is unchanged on dividing \(N,k\) by \(p\), followed by
Jacobsthal's binomial congruence. The two central binomial ratios are
handled by the same congruence. The case \(k=N\), where the final
central factor is \(\binom00=1\), is harmless.

For \(1\le s<r\), the lower summand contributes at least
\(e(r-s)\) powers of \(p\), where \(e=\min(A+1,3)\), while the scale
ratio contributes \(3s\). Thus the difference is divisible by
\(p^{er+(3-e)s}\), hence by \(p^{er}\). For \(s\ge r\), the scale ratio
alone supplies \(p^{3r}\). Terms with \(p\nmid k\) vanish modulo
\(p^{er}\), and the multiples of \(p\) reindex exactly to the lower
sum. The \(k=0\) endpoint is a direct central-binomial Jacobsthal
congruence. Factoring powers of \(p\) from \(m\) correctly extends the
argument from \(p\nmid m\) to arbitrary positive \(m\).

Adversarial checks focused on four possible failure points:

1. indices with \(\nu_p(k)>r\), which can occur when \(m>p\);
2. cancellation increasing \(\nu_p(N\pm k)\);
3. the endpoints \(k=0,N\);
4. the reduction when \(p\mid m\).

The proof covers all four. In particular, it does not assume
\(\nu_p(k)\le r\); the variable \(q=\min(r,\nu_p(k))\) handles the
large-valuation indices.

Exact-integer verification reproduced the A364111 initial values and
checked 96 congruences spanning \(A=0,1,2,3\), both \(r=1,2\), primes
5 and 7, and several \(B,C\) choices. Additional adversarial finite
checks included values of \(m\) larger than \(p\) and values divisible
by \(p\). These computations support but are not used in the proof.

## Originality

**PASS, to the best of our knowledge.**

OEIS A364111 explicitly conjectures
\[
T_{A,B,C}(mp^r)\equiv T_{A,B,C}(mp^{r-1})\pmod{p^{3r}}
\]
for every \(A\ge2\), \(B,C>0\), \(p\ge5\), and positive \(m,r\).
The page was last modified on 5 September 2026 and continues to label
the assertion as a conjecture. The present theorem proves that full
parameter family, not only the displayed sequence \(A=2,B=C=1\).

The most closely related established theorem inspected is Osburn--Sahu
(2013), which proves the same cubic modulus for generalized Domb sums
with \(\binom nk^A\) in place of
\(\binom{n+k-1}{k}^A\). Osburn--Sahu--Straub (2016) develops
Jacobsthal-based scaling for several broader Apéry-like and
central-binomial families and gives direct generalizations, but the
shifted generalized Domb family above is not among the stated
families. Those sources supply a method lineage, not an implication of
the present statement.

Searches were made using the exact OEIS identifier, the shifted
binomial summand, the equivalent negative-upper-index notation
\(\binom{-n}{k}\), "shifted generalized Domb", "negative-index Domb",
and stronger-covering supercongruence terminology. No prior proof of
A364111 or of the stated \(p^r,p^{2r},p^{3r}\) hierarchy was located.

Matthijs Coster's 1988 thesis *Supercongruences* is the principal
source-access risk. It is foundational for the binomial
supercongruence methods later used by Osburn and Sahu, but the thesis
was not inspected in full. Accessible later sources describing and
extending Coster's methods were inspected. The fact that the exact
A364111 statement remained explicitly conjectural in a September 2026
OEIS revision substantially reduces, but does not eliminate, the
residual priority risk from the thesis or unindexed literature.

## Value

**PASS.**

The main cubic layer settles an explicit generalized conjecture, not a
single numerical instance. The proof also isolates a reusable
mechanism: complementary base-\(p\) carries in
\(\binom{2k}{k}\binom{2(N-k)}{N-k}\) exactly supply the valuation lost
when the ordinary Domb factor \(\binom Nk^A\) is replaced by the
shifted factor \(\binom{N+k-1}{k}^A\).

The extension to all \(A\ge0\) gives a clean hierarchy
\[
p^r,\qquad p^{2r},\qquad p^{3r},
\]
for \(A=0,1,\ge2\), respectively. Explicit \(p=5,r=1\) examples attain
all three exponents, so the hierarchy is sharp as a uniform statement
over the family.

The result also clarifies a nearby boundary. For
\(A=1,B=C=1\), the sequence is OEIS A362676, for which a stronger
cubic congruence remains conjectural. The present proof establishes the
uniform quadratic layer but does not falsely promote that special
cubic conjecture to a theorem.

## Limitations

The proof applies to primes \(p\ge5\) and uses \(B,C\ge1\). It does not
settle the stronger cubic conjecture for A362676 or analogous
exceptional \(A=1\) subfamilies. Coster's 1988 thesis was not fully
inspected, leaving a residual originality risk. The finite verification
is corroborative rather than exhaustive. No independent validation or
formal proof-assistant verification is asserted.
