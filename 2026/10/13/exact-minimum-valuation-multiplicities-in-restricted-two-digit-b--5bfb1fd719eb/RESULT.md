# Exact minimum-valuation multiplicities in restricted two-digit binomial rows

## Finding

Let \(p\) be a prime, let \(m\ge3\) divide \(p+1\), and let \(0\le s<t\) have odd difference \(g=t-s\). Put \(N=p^s+p^t>m\). For the restricted row
\[
\mathcal R(N;m)=\left\{\binom Nk:0<k<N,\ m\mid k\right\},
\]
let \(h=\min_{0<k<N,\,m\mid k}\nu_p\binom Nk\) and let \(H=\#\{k:0<k<N,\ m\mid k,\ \nu_p\binom Nk=h\}\). The main result determines *both* the minimum valuation and its exact multiplicity:

**Ordinary branch.** If \(p>m\), put \(a=(p+1)/m\). Then \(h=1\), and
\[
H=(a-1)\begin{cases}
1,&g=1,\ s=0,\\
3,&g=1,\ s\ge1,\\
2,&g\ge3,\ s=0,\\
4,&g\ge3,\ s\ge1.
\end{cases}
\]

**Exceptional branch.** If \(p=m-1\), then \(h=2\), and
\[
H=(p-1)\begin{cases}
1,&g=1,\ s=1,\\
3,&g=1,\ s\ge2,\\
2,&g\ge3,\ s=0,\\
3,&g\ge3,\ s=1,\\
5,&g\ge3,\ s\ge2.
\end{cases}
\]
The omitted case \(g=1,s=0,p=m-1\) has \(N=m\) and is excluded by hypothesis. The proof also gives an exact parametrization of *every* index attaining the minimum. In particular the multiplicity depends on the gap \(g\) only through whether it is \(1\) or at least \(3\); it stabilizes as the two occupied digit positions move farther apart.

## Assumptions and scope

All integers and divisibility requirements are as in the finding. There is no restriction on how large \(p\), \(s\), or \(t\) may be. For \(p>m\), \((p+1)/m\ge2\). For \(p=m-1\), necessarily \(m=p+1\). Because \(g\) is odd, \(p^s+p^t\equiv0\pmod m\). The selected set is nonempty when \(m<N\). \(\nu_p\) is the standard exponent of \(p\) in a nonzero integer; no valuation of zero is used.

## Proof

**Borrow runs.** The base-\(p\) expansion of \(N\) has digit \(1\) exactly at positions \(s,t\), with zeros elsewhere. By Kummer's theorem, \(\nu_p\binom Nk\) is the number of borrow positions when subtracting \(k\) from \(N\). A borrow cannot continue indefinitely, and a run of consecutive borrows must terminate at an occupied position \(s\) or \(t\). The only zero-borrow choices for \(k\) are \(0,p^s,p^t,N\); none is a proper nonzero multiple of \(m\), because \(p\equiv-1\pmod m\). Thus \(h\ge1\).

To state complete sets of minimal indices, write \(\{\cdots\}_{m}\) for the displayed indices for which \(m\mid k\); all other displayed parameter constraints are literal. Every such index lies strictly between \(0\) and \(N\). Borrow placements are unique, so the following families are disjoint.

**Exactly one borrow.** A single borrow can end at \(s\), when \(s\ge1\); it must then have
\[
k=d p^{s-1}+e p^t,\qquad 1\le d\le p-1,\quad e\in\{0,1\}.
\]
If the borrow ends at \(t\) and \(g\ge3\), it has
\[
k=d p^{t-1}+e p^s,\qquad1\le d\le p-1,\quad e\in\{0,1\}.
\]
For \(g=1\), ending at \(t\) instead gives
\[
k=d p^s,\qquad2\le d\le p-1.
\]
These are exhaustive: a one-borrow position must lie immediately below one of the two occupied digits; all untouched occupied digits may be independently selected as \(0\) or \(1\), except when adjacent, where the borrowed-from lower position has changed. In the first two families, \(p^{s-1}\) and \(p^t\), or \(p^{t-1}\) and \(p^s\), have the same sign modulo \(m\); hence the admissibility condition is \(d+e\equiv0\pmod m\). In the adjacent family it is \(d\equiv0\pmod m\).

If \(p>m\), set \(a=(p+1)/m\). For each fixed \(e\in\{0,1\}\), there are exactly \(a-1\) admissible \(d\)'s in the first two families; the third family likewise has \(a-1\) choices. This gives the ordinary formula by summing the applicable disjoint families. It also proves \(h=1\), since \(a\ge2\).

If \(p=m-1\), then \(m=p+1\). Neither \(d+e\) nor \(d\) can be a positive multiple of \(m\) in the permitted ranges. Therefore no selected coefficient has one borrow and \(h\ge2\).

**Exactly two borrows in the exceptional branch.** Two borrow positions can be adjacent (one run of length two) or separated (two length-one runs). All possibilities, and their exact admissible choices, are:

(i) One length-two run ending at \(s\) (requires \(s\ge2\)):
\[
k=d p^{s-2}+c p^{s-1}+e p^t,
\quad1\le d\le p-1,\ 0\le c\le p-1,\ e\in\{0,1\}.
\]
The mod-\(m\) condition is \(d-c-e=0\), equivalently \(c=d-e\), yielding \(2(p-1)\) indices.

(ii) One length-two run ending at \(t\), with \(g\ge3\):
\[
k=d p^{t-2}+c p^{t-1}+e p^s,
\quad1\le d\le p-1,\ 0\le c\le p-1,\ e\in\{0,1\}.
\]
Again \(c=d-e\), yielding \(2(p-1)\) indices.

(iii) One length-two run ending at \(t\), with \(g=1\) and \(s\ge1\):
\[
k=d p^{s-1}+c p^s,
\quad1\le d,c\le p-1.
\]
Here \(d-c=0\), yielding \(p-1\) indices.

(iv) Two separate length-one runs, one ending at each occupied position (requires \(s\ge1,g\ge3\)):
\[
k=d p^{s-1}+e p^{t-1},\qquad1\le d,e\le p-1.
\]
The condition is \(d-e=0\), yielding \(p-1\) indices.

For the single-run families, the signed residue difference lies strictly between \(-m\) and \(m\), so congruence zero modulo \(m\) forces the displayed *integer* equalities. Conversely, every displayed admissible index induces exactly its stated two borrows by direct base-\(p\) subtraction. The four families exhaust all two-borrow patterns: either both borrow positions end at the same occupied digit or each ends at a different occupied digit; neither can end at a zero digit, and the stated lower-position/adjacency restrictions are forced. Adding applicable family sizes yields the exceptional five-case formula. Each permitted case has at least one such index, so \(h=2\). This proves the claim and parametrizes every minimizer. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 standard library. It checks two independent exact valuation formulas (Legendre factorial sums and base-\(p\) digit sums), exhaustively compares every selected coefficient with the predicted minimizer set in 169 tested parameter cases, checks larger constructive examples, and directly computes 35 binomial coefficients as a third route. Exact run output is stored in `verification_output.txt`. Finite checks support the proof but cannot replace the exhaustive borrow-run argument for arbitrary parameters.

## Relationship to prior work

Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1* (arXiv:2609.37754v1), determines \(\nu_p(G(N;m))\), where \(G\) is the greatest common divisor of the selected coefficients. Its mixed two-digit theorem supplies the *minimum valuation only*. The present theorem instead counts and explicitly describes *all* indices where that minimum occurs; neither their cardinality nor their location follows from the value of the gcd. The general arithmetic-progression gcd literature of McTague (arXiv:1510.06696v5) concerns related valuations and provides no corresponding minimal-index multiplicity formula. Wu's 2026 treatment (arXiv:2606.20940v2) addresses restricted gcd formulas, not a verified minimizer census. The leading-order valuation formula itself is not claimed as new.

## Limitations

This counts only the first occupied prime-adic valuation layer in the two-one-digit, opposite-parity family, not all valuation layers or general digital patterns. The near literature includes gcd results but a differently worded or unindexed earlier enumeration could exist. The accessible examination of Wu's 2026 paper was partial. Independent mathematical validation has not been performed. The finite verifier is neither a substitute for the proof nor a formal certification.

## References

1. John Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754v1 (first posted 29 September 2026), https://arxiv.org/html/2609.37754v1.
2. Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients*, corrected arXiv:1510.06696v5, https://arxiv.org/html/1510.06696v5.
3. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940v2, https://arxiv.org/abs/2606.20940.
4. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik **44** (1852), 93–146.
