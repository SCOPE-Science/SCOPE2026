# Complete binary residue classification of restricted binomial gcds at modulus five

## Finding
For every integer \(N>5\) divisible by \(5\), define
\[
G(N;5)=\gcd\left\{\binom Nk:0<k<N,\ 5\mid k\right\}.
\]
Let \(I=\{i\geq0:\text{the binary digit of }N\text{ at }i\text{ is }1\}\), and let \(R\) be the multiset of residues \(2^i\pmod5\), for \(i\in I\). The multiset \(R\) is a *minimal zero-sum multiset* if its total is zero modulo \(5\), but no nonempty proper submultiset has sum zero modulo \(5\). Put \(w=|I|\). Then the following classification is exact:
\[
\nu_2(G(N;5))=\begin{cases}
0,&R\text{ is not minimal zero-sum};\\
3,&R\text{ is minimal},\ w=2,\ N\text{ odd};\\
2,&R\text{ is minimal},\ w=2,\ N\text{ even};\\
2,&R\text{ is minimal},\ w=3,\ N\text{ odd},\ R=\{1,2,2\};\\
1,&\text{all other minimal zero-sum cases}.
\end{cases}
\]
In particular, the valuation always belongs to \(\{0,1,2,3\}\); it is \(3\) precisely for
\[
N=2^{4h+2}+1,\qquad h\geq1.
\]
This gives a complete answer for the prime \(2\), which has multiplicative order \(4\) modulo \(5\), beyond the congruence classes of primes handled by the initiating work.

## Assumptions and scope
The claim concerns *only* the exponent of \(2\) in this fixed-row, progression-restricted binomial gcd; it does not determine other prime factors of \(G(N;5)\). All quantifiers range over integers \(N>5\) with \(5\mid N\). The gcd is over a nonempty set because \(k=5\) is admissible. Binary positions are distinct nonnegative integers and their residues cycle as \(1,2,4,3\pmod5\). Multiplicity is essential in forming \(R\).

## Proof
**1. From carries to minimal zero-sums.** By Legendre's formula, for every \(0<k<N\),
\[
\nu_2\binom Nk=s_2(k)+s_2(N-k)-s_2(N),
\]
where \(s_2\) is binary digit weight; equivalently the valuation counts carries when adding \(k\) and \(N-k\). A zero-carry decomposition is a partition of the occupied binary powers of \(N\) between the two summands. Therefore some admissible \(5\)-divisible \(k\) has valuation zero exactly when the residues in \(R\) admit a proper nonempty zero-sum submultiset. This proves the zero branch and supplies a lower bound of one in all minimal cases.

**2. Exhaustive minimal shapes.** A nonempty minimal zero-sum sequence in the cyclic group of order five has length at most five: if six terms were present, their first five proper partial sums, considered with zero, would yield a forbidden nonempty proper contiguous zero-sum subsequence, by pigeonhole. More precisely, for a purported length at least six, the six partial sums at lengths zero through five force a collision; the collided interval has size between one and five, hence is proper. Direct finite classification of multisets of nonzero residues of lengths two through five gives exactly:

\(w=2\): \((1,4),(2,3)\).

\(w=3\): \((1,1,3),(1,2,2),(2,4,4),(3,3,4)\).

\(w=4\): \((1,1,1,2),(1,3,3,3),(2,2,2,4),(3,4,4,4)\).

\(w=5\): \((1,1,1,1,1),(2,2,2,2,2),(3,3,3,3,3),(4,4,4,4,4)\).

The four lines can also be verified by checking all multisets of the four nonzero residues of length at most five and every proper submultiset; a standalone exact checker accompanies this proof.

**3. One-carry witnesses for ordinary minimal shapes.** To split a binary summand \(2^i\) with \(i\geq1\), replace it by two copies of \(2^{i-1}\). Modulo five this replaces one residue \(r\) by two copies of \(3r\), since \(2^{-1}\equiv3\pmod5\). If a proper nonempty submultiset of the resulting terms sums to zero, and the new residue \(3r\) is absent from the unsplit terms, assign that submultiset to \(k\) and the complement to \(N-k\). Minimality of the original multiset forces such a proper zero-sum selection to contain exactly one of the two newly created equal powers: selecting both or neither would yield a prohibited proper zero-sum selection of the original terms. Therefore this has exactly one binary carry, at position \(i-1\). For each minimal shape with \(w\geq3\), except \((1,2,2)\), the following choice of split residue has this property:

\((1,1,3):3\), \((2,4,4):2\), \((3,3,4):4\), \((1,1,1,2):1\), \((1,3,3,3):3\), \((2,2,2,4):2\), \((3,4,4,4):4\). For the four five-term constant-residue shapes, split any term at a positive binary position. In each case the new-residue terms and suitable unsplit terms contain a proper zero-sum: \(4+1\), \(1+4\), \(2+3\), \(3+2\), \(4+1\), \(1+4\), \(2+3\), and respectively \(3+1+1\), \(1+2+2\), \(4+3+3\), \(2+4+4\). The chosen split term has positive exponent automatically except possibly in the \((1,1,1,2)\) and all-one five-term shapes; each of these has at least three occupied positions with residue one, so at least one is positive. As the chosen new residue does not appear among remaining original terms, no other carry is created. This proves valuation one in these shapes.

For \(R=(1,2,2)\), splitting the unique residue-one term gives one carry when its binary exponent is positive: the two new terms have residue three and either original residue-two term completes \(3+2\equiv0\pmod5\). This handles even \(N\). If \(N\) is odd, that term is \(2^0=1\) and cannot be split. Splitting either residue-two term yields residues \((1,1,1,2)\), with no proper zero-sum; thus no one-carry witness exists. Writing \(N=1+2^a+2^b\) with \(a>b\geq1\), both \(a,b\equiv1\pmod4\), let
\[
k=2^{a-2}+2^b,\qquad N-k=2^{a-1}+2^{a-2}+1.
\]
The first is divisible by five since its two residues are three and two. Their respective weights are two and three, while \(s_2(N)=3\), so this witness has valuation two.

**4. Two-term cases.** Every minimal shape with two terms consists of complementary residues \((r,5-r)\). Splitting either positive-exponent term gives two residues \(3r\) and the other unsplit residue \(-r\); none of the proper nonempty submultisets has sum zero modulo five, since their possible sums are \(3r\), \(6r\equiv r\), \(-r\), and \(2r\), all nonzero. Hence every admissible binomial coefficient has at least two carries. If \(N\) is even, \(k=N/2\) is a positive proper multiple of five, and \(s_2(k)=s_2(N)=2\), giving valuation \(2\).

If \(N\) is odd, its two binary digits lie at positions zero and \(a\), with \(a\equiv2\pmod4\). Because \(N>5\), \(a\geq6\). The low bit cannot be split. After splitting the high bit once, its two halves have residue two; after a second split, the residue multiset is \((1,1,1,2)\), still with no proper zero-sum, so two carries cannot suffice. For the upper bound put
\[
k=1+3\cdot2^{a-3},\qquad N-k=5\cdot2^{a-3}.
\]
Here \(a-3\equiv3\pmod4\), so \(5\mid k\); the summands have binary weights three and two, yielding exactly three carries and valuation three.

**5. Characterization of the maximum.** The only valuation-three case was shown to be odd and two-term, namely \(N=2^a+1\) with \(a\equiv2\pmod4\) and \(a\geq6\). Writing \(a=4h+2\) gives \(h\geq1\), as claimed. Every minimal shape has already received an explicit witness of valuation at most three. This completes the classification.

## Verification
Run `python3 restricted_gcd5_verify.py`. The verifier compares the classification against an independent digitwise dynamic program that optimizes \(s_2(k)+s_2(N-k)\) with \(5\mid k\), for all \(3999\) multiples of five from ten to twenty thousand; for \(199\) cases through one thousand it also exhausts every admissible \(k\). It independently enumerates the fourteen minimal zero-sum multiset types and checks all ordinary splitting witnesses. Expected output is recorded in `verification_output.txt`. These checks are finite support only; the universal theorem follows from the proof above.

## Relationship to prior work
Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1* (arXiv:2609.37754v1, first public September 29, 2026) introduces the same quantity, proves the complete regime \(p\equiv-1\pmod m\), records McTague's earlier \(p\equiv1\pmod m\) and same-residue cases, and derives the small-modulus specializations \(m=3,4,6\). At modulus five, prime two has order four, so neither the plus-one nor the minus-one hypothesis holds; this classification addresses that excluded regime. McTague (2017) and Wu (2026) concern additional related valuation or gcd formulas, with different stated prime restrictions. This statement neither claims novelty for Kummer's theorem nor asserts that other unindexed equivalent treatments are impossible.

## Limitations
Only \(\nu_2\), not the full gcd or valuations at odd primes, is determined. The work uses a complete proof and reproducible finite checks but has not received independent audit. Novelty comparisons use the full accessible motivating preprint and available evidence from related literature; a separate independently equivalent derivation could remain unlocated.

## References
1. John Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754v1 (first public September 29, 2026), Sections 1–9, https://arxiv.org/abs/2609.37754.
2. Carl McTague, *On the greatest common divisor of binomial coefficients C(n,q), C(n,2q), C(n,3q), ...*, corrected preprint arXiv:1510.06696v5; American Mathematical Monthly 124 (2017), 353–356.
3. Chai Wah Wu, *Computing the greatest common divisor of binomial coefficients*, arXiv:2606.20940v2 (2026).
4. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik 44 (1852), 93–146.
