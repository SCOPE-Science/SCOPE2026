# Exact 2-adic peeling from a single cyclotomic value

## Statement

Let \(n>1\), let
\[
C=\Phi_n(2),\qquad a=\nu_2(C-1),\qquad r=n/a,
\]
and extend \(\nu_2\) to nonzero rationals by
\(\nu_2(u/v)=\nu_2(u)-\nu_2(v)\).  Write the distinct prime divisors of
\(r\) as
\[
p_1<p_2<\cdots<p_k,
\]
and put \(\varepsilon=(-1)^k\).  The 2-adic radical identity gives
\(a=n/\operatorname{rad}(n)\), hence \(r=\operatorname{rad}(n)\).

For a finite set \(Q\) of primes define the rational fingerprint
\[
H_a(Q)=\prod_{S\subseteq Q}
  \left(2^{a\prod_{p\in S}p}-1\right)^{(-1)^{|S|}},
\]
with the empty subset product equal to \(1\).  Then
\[
\boxed{C^{\varepsilon}=H_a(\{p_1,\ldots,p_k\}).}
\]
Moreover, for every nonempty proper initial segment
\(Q_j=\{p_1,\ldots,p_j\}\),
\[
\boxed{
\nu_2\!\left(\frac{C^{\varepsilon}}{H_a(Q_j)}-1\right)
=a p_{j+1}.
}
\tag{1}
\]
Thus, once the orientation \(\varepsilon\) and a nonempty initial segment are
known, every remaining prime divisor is obtained exactly from the same integer
\(C\), with no further cyclotomic evaluation and no real logarithm.

The orientation and the first prime(s) are themselves recoverable from \(C\):

### Nonsquarefree case \(a>1\)

Let \(A=2^a-1\), and for \(\sigma\in\{+1,-1\}\) set
\[
b_\sigma=\nu_2\!\left(\frac{C^\sigma}{A}+1\right).
\]
Then
\[
\boxed{b_\varepsilon=a p_1,\qquad b_{-\varepsilon}=a+1.}
\tag{2}
\]
Since \(p_1\ge2\) and \(a\ge2\), one has \(ap_1>a+1\).  Hence the larger
of \(b_+,b_-\) identifies \(\varepsilon\), and after division by \(a\) it
returns \(p_1\).  Formula (1) then recovers the remaining primes.

### Squarefree case \(a=1\)

The local least-prime identity gives
\[
p_1=\nu_2(C+1).
\]
If \(p_1=r\), the index is prime and the process stops.  Otherwise there are
three startup possibilities.

If \(p_1\ge3\), put \(Q=\{p_1\}\) and
\[
b_\sigma=\nu_2\!\left(\frac{C^\sigma}{H_1(Q)}-1\right).
\]
Then
\[
\boxed{b_\varepsilon=p_2,\qquad b_{-\varepsilon}=p_1+1.}
\tag{3}
\]
Because consecutive odd primes differ by at least two, \(p_2>p_1+1\), so the
larger valuation identifies \(\varepsilon\) and \(p_2\).

If \(p_1=2\) and \(3\nmid r\), take \(Q=\{2\}\).  Then
\[
\boxed{b_\varepsilon=p_2,\qquad b_{-\varepsilon}=3,}
\tag{4}
\]
and \(p_2\ge5\).

If \(p_1=2\) and \(3\mid r\), the second prime is \(3\).  If \(r=6\), this
already completes the support.  Otherwise take \(Q=\{2,3\}\); then
\[
\boxed{b_\varepsilon=p_3,\qquad b_{-\varepsilon}=3,}
\tag{5}
\]
with \(p_3\ge5\).  Again the larger valuation fixes the orientation, after
which (1) completes the peeling.

Consequently, for every \(n>1\), the single exact integer \(\Phi_n(2)\),
together with its index \(n\), admits an exact all-prime-support decoder using
only rational arithmetic and 2-adic valuations.

## Proof

Radical reduction gives
\[
\Phi_n(X)=\Phi_r(X^a),\qquad r=\operatorname{rad}(n),\quad a=n/r.
\]
For squarefree \(r\), the Möbius product gives
\[
\Phi_r(2^a)=
\prod_{S\subseteq P}
\left(2^{a d_S}-1\right)^{\varepsilon(-1)^{|S|}},
\qquad
d_S=\prod_{p\in S}p,
\]
where \(P=\{p_1,\ldots,p_k\}\).  Raising to \(\varepsilon\) proves
\(C^\varepsilon=H_a(P)\).  The same radical reduction at the origin gives
\(\nu_2(C-1)=a\), so the \(a\) appearing above is directly recovered from
\(C\).

Now fix a nonempty proper initial segment \(Q_j\subset P\), and put
\[
R_j=\frac{H_a(P)}{H_a(Q_j)}.
\]
The factors left in \(R_j\) correspond exactly to subsets \(S\subseteq P\)
that are not contained in \(Q_j\).  Their number is \(2^k-2^j\), which is
even.  Replacing each
\(2^{ad_S}-1\) by \(-(1-2^{ad_S})\), the signs therefore cancel.  The
uniquely smallest omitted subset product is \(d_S=p_{j+1}\), from the
singleton \(S=\{p_{j+1}\}\), and its exponent is \(-1\).  All other omitted
subset products are strictly larger.  Hence, modulo \(2^{a p_{j+1}+1}\),
\[
R_j\equiv(1-2^{a p_{j+1}})^{-1}
\equiv1+2^{a p_{j+1}},
\]
which proves (1).

For the nonsquarefree startup, divide \(H_a(P)\) by its empty-subset factor
\(A=2^a-1\).  The remaining number of factors is \(2^k-1\), which is odd, so
with \(T=H_a(P)/A\),
\[
T\equiv-1-2^{a p_1}\pmod{2^{a p_1+1}}.
\]
Thus \(\nu_2(T+1)=a p_1\), proving the first half of (2).  For the opposite
orientation,
\[
\frac{C^{-\varepsilon}}{A}=\frac1{A^2T}.
\]
Because \(T\equiv-1\pmod{2^{ap_1}}\), the numerator of this rational number
plus one is congruent to \(1-A^2\) modulo \(2^{ap_1}\).  But
\[
1-A^2=2^{a+1}(1-2^{a-1}),
\]
whose valuation is exactly \(a+1\) for \(a\ge2\), while
\(ap_1>a+1\).  This proves (2).

For squarefree odd startup, \(H_1(\{p_1\})=(2^{p_1}-1)^{-1}\).  The true
orientation is covered by (1).  In the opposite orientation the relevant
quantity is
\[
\frac1{H_1(\{p_1\})^2R_1}-1,
\]
where \(R_1\equiv1\pmod{2^{p_2}}\).  Since
\[
(2^{p_1}-1)^2-1
=2^{p_1+1}(2^{p_1-1}-1),
\]
its valuation is \(p_1+1\), and \(p_2\ge p_1+2\).  This proves (3).
The same calculation with \(p_1=2\) gives the false-orientation valuation
\(3\) whenever \(3\nmid r\), proving (4).

Finally,
\[
H_1(\{2,3\})=3.
\]
When \(2,3\mid r\) and another prime remains, the true residual differs from
\(1\) first at exponent \(p_3\ge5\), while the opposite orientation contains
\(1/(9R)-1\) with \(R\equiv1\pmod{2^{p_3}}\).  Since \(1-9=-8\), the latter
has valuation exactly \(3\).  This proves (5) and completes the theorem.

## Consequences

For \(m\ge4\), applying the theorem to \(n=m!\) gives an exact local analogue
of the recent Archimedean factorial decoder: the single integer
\(\Phi_{m!}(2)\), together with \(m\), recovers every prime at most \(m\)
using only exact rational 2-adic valuations.  No approximation to
\(\log_2\Phi_{m!}(2)\) is required.

Likewise, if
\[
R_m=\prod_{m<p\le2m}p
\]
is represented by the standard central-binomial quotient, then for \(m\ge2\)
\(R_m\) is odd and squarefree.  The same single value \(\Phi_{R_m}(2)\)
recovers the entire set of primes in \((m,2m]\), whereas the basic local
least-prime extractor returns only the smallest remaining prime per
cyclotomic evaluation.

These are reconstruction identities, not efficient factoring or
prime-generation algorithms: the cyclotomic values and rational fingerprints
can be enormous, and direct evaluation of \(H_a(Q)\) has exponentially many
subset factors.

## Verification

`artifacts/verify.py` implements the formulas with exact rational arithmetic.
It recomputes \(\Phi_n(2)\) from the Möbius product, compares the recovered
support with independent integer factorization, and checks every
\(2\le n\le1199\) plus 100 deterministic pseudorandom indices in
\([1200,5000]\).  All checks pass.  Representative outputs include
\(45\mapsto\{3,5\}\), \(105\mapsto\{3,5,7\}\),
\(210\mapsto\{2,3,5,7\}\), and \(315\mapsto\{3,5,7\}\).
The computation is supporting evidence; the theorem is proved above.

## Relation to the literature

Shunia's 2026 preprint *Cyclotomic Prime Extractors* proves the exact local
identities
\[
\nu_2(\Phi_n(2)-1)=n/\operatorname{rad}(n)
\]
and, for squarefree \(n\),
\(\nu_2(\Phi_n(2)+1)=\operatorname{lpf}(n)\).  Its local factor stripping
re-evaluates the plus identity after dividing the index, while its complete
single-value peeling uses real logarithmic fingerprints and rounding.  Its
concluding comparison explicitly describes the local formulas as recovering
the repeated-power quotient and the least prime, in contrast with the real
peeling formulas.

Pomerance and Rubinstein-Salzedo prove the classical radical reduction and
Archimedean size/first-gap estimates for cyclotomic polynomials.  Their
inspected paper does not contain the rational 2-adic residual recursion (1)--(5).
Searches for exact and synonymous formulations of single-value cyclotomic
2-adic prime-support peeling did not identify an earlier theorem.  Originality
is therefore asserted only to the best of our knowledge; the motivating
preprint is very recent, so contemporaneous unindexed work remains a residual
risk.

## Limitations

The theorem assumes the index \(n\) is given together with \(\Phi_n(2)\); it
is not a complexity improvement for integer factorization.  It uses exact
integer/rational arithmetic and does not address approximate input.  The
fingerprint can have exponential subset complexity.  No independent
validation or formal proof-assistant verification is asserted.

## References

1. J. M. Shunia, *Cyclotomic Prime Extractors*, arXiv:2609.18480, 2026. https://arxiv.org/abs/2609.18480
2. C. Pomerance and S. Rubinstein-Salzedo, *Cyclotomic Coincidences*, Experimental Mathematics 31 (2022), 596--605. https://arxiv.org/abs/1903.01962
3. J. M. Shunia, *Prime-Interval Algebras*, arXiv:2607.22347, 2026. https://arxiv.org/abs/2607.22347
