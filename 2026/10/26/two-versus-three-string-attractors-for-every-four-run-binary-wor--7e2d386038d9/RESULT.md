# Two-versus-three string attractors for every four-run binary word

## Finding

A **string attractor** of a finite word is a set of positions such that every distinct nonempty contiguous factor of the word has at least one occurrence meeting the set. Its **attractor number**, \(\gamma(w)\), is the minimum cardinality of such a set.

**Theorem.** For every quadruple of positive integers \(a,b,c,d\), put
\[
w=0^a1^b0^c1^d.
\]
Then \(\gamma(w)\) is always either \(2\) or \(3\), and the latter value occurs **if and only if**
\[
 (a>c\ \text{and}\ d>b)\quad\text{or}\quad
 (c\ge a+2\ \text{and}\ b\ge d+2).
\]
Thus the minimum-attractor decision problem on four-run binary words admits a constant-time decision in the four run lengths, together with explicit optimal position sets given below.

Let \(T_n\) count length-\(n\) binary words with precisely four nonempty maximal runs whose attractor number is \(3\). Both possible initial letters are counted. Then
\[
\sum_{n\ge4}T_nz^n=
\frac{2z^6(1+z^2)}{(1-z)^2(1-z^2)^2}.
\]
Consequently, among length-\(n\) binary words with exactly four runs, the proportion whose attractor number is \(3\) tends to \(1/2\), and the complementary proportion with attractor number \(2\) also tends to \(1/2\).

## Assumptions and scope

All four run lengths are arbitrary **positive integers**; there is no bound on the total length. Factors are contiguous, not scattered, and their different occurrences count as alternative ways of attracting the *same* factor. Positions in the constructions below use **one-based indexing**. The result applies equally to words beginning in \(1\) by interchanging the alphabet symbols. The generating function counts labeled binary words, not conjugacy or reversal classes.

Write \(U=a+b\) for the last position of the first one-run, and \(V=a+b+1\) for the first position of the second zero-run. Write \(P=a\) for the last position of the first zero-run, \(Q=a+1\) for the first position of the first one-run, \(R=a+b+c\) for the last position of the second zero-run, and \(S=a+b+c+1\) for the first position of the final one-run.

For \(\gamma(w)=2\), an explicit optimum is selected by the first applicable row:

| Condition | Two attracting positions |
| --- | --- |
| \(a\ge c\) and \(b\ge d\) | \(\{P,U\}\) |
| \(c\ge a\) and \(d\ge b\) | \(\{V,S\}\) |
| \(c>a\), \(b>d\), and \(b\le d+1\) | \(\{U,R\}\) |
| \(c>a\), \(b>d\), and \(c\le a+1\) | \(\{Q,V\}\) |

If neither condition holds, the optimal cardinality is \(3\). An explicit optimum then is \(\{P,U,S\}\) when \(a\ge c\), and \(\{Q,V,S\}\) when \(c>a\).

## Proof

**1. Reduction to four factor types.** Any factor is a constant run, changes symbol once (type \(01\) or \(10\)), or changes symbol at least twice. The factor \(10\) occurs at exactly one adjacent pair of positions, \(U,V\), so **every attractor contains \(U\) or \(V\)**. Moreover, every factor with at least two symbol changes contains that same unique \(10\) transition, and so every occurrence of such a factor contains both \(U\) and \(V\). Thus choosing either central position attracts all factors with a \(10\) transition.

For constant factors, it suffices to hit an occurrence of the **longest** zero run \(0^{\max(a,c)}\) and the **longest** one run \(1^{\max(b,d)}\): every shorter constant factor can be placed to overlap the same chosen position in an appropriate longest run. Hence it remains to address factors of the form \(0^i1^j\), for \(i,j\ge1\).

Such a factor has an occurrence if and only if its parameter pair lies in the union of two integer rectangles
\[
\mathcal R_1=[1,a]\times[1,b],\qquad
\mathcal R_2=[1,c]\times[1,d].
\]
A first-transition occurrence crosses \(U\) exactly when \(j=b\); a second-transition occurrence crosses \(V\) exactly when \(i=c\). The positions \(P,Q\) each attract **all** first-transition factors, and \(R,S\) each attract **all** second-transition factors. These assertions follow by writing their unique occurrences at the respective \(01\) boundaries.

**2. Universal three-position upper bound.** If \(a\ge c\), the set \(\{P,U,S\}\) attracts every factor with a \(10\) transition via \(U\), every \(01\) factor via \(P\) or \(S\), the longest zero run via \(P\), and the longest one run via \(U\) or \(S\). If \(c>a\), use \(\{Q,V,S\}\): \(V\) attracts the \(10\)-containing factors and the longest zero run, while \(Q,S\) attract the two \(01\) rectangles and a longest one run. Thus \(\gamma(w)\le3\). Because both letters occur, \(\gamma(w)\ge2\).

**3. Four constructive two-position regimes.** If \(a\ge c\) and \(b\ge d\), then \(\mathcal R_2\subseteq\mathcal R_1\), so \(\{P,U\}\) attracts every \(01\) factor as well as every other type and both maximal constant factors. If \(c\ge a\) and \(d\ge b\), the containment is reversed, and \(\{V,S\}\) works.

Suppose next \(c>a\), \(b>d\), and \(b\le d+1\). The position \(R\) attracts \(\mathcal R_2\), hence every first-transition factor with \(j\le d\), while \(U\) attracts the only possibly remaining row \(j=b\). The pair \(\{U,R\}\) also hits the longest one and zero runs and the unique \(10\) transition.

Finally, suppose \(c>a\), \(b>d\), and \(c\le a+1\). The position \(Q\) attracts \(\mathcal R_1\), hence every second-transition factor with \(i\le a\), while \(V\) attracts the only possibly remaining column \(i=c\). The pair \(\{Q,V\}\) also attracts the longest constant runs and the unique \(10\) transition. Thus all four listed regimes have \(\gamma(w)=2\).

**4. Necessary three positions in the complementary regimes.** If \(a>c\) and \(d>b\), the factor \(0^a\) occurs only in the first zero-run, the factor \(1^d\) only in the final one-run, and the unique \(10\) factor only at \(U,V\). These three disjoint regions force three attracting positions.

If \(c\ge a+2\) and \(b\ge d+2\), suppose there were a two-position attractor. One selected position must be \(U\) or \(V\). If \(U\) is selected, the other must belong to the second zero-run to attract \(0^c\). But \(01^{b-1}\) occurs only at the first \(01\) transition, ends strictly before \(U\), and never meets that second zero-run. It is therefore not attracted. If \(V\) is selected, the other must belong to the first one-run to attract \(1^b\). But \(0^{c-1}1\) occurs only at the second \(01\) transition, begins strictly after \(V\), and does not meet the first one-run. Again there is a contradiction. These arguments also cover a proposed pair containing both \(U\) and \(V\).

The order comparisons between \(a,c\) and \(b,d\) exhaust the possibilities: the two aligned-maxima regimes are constructive cases one and two; the outward-opposed regime is \(a>c,d>b\); and the remaining crossed regime \(c>a,b>d\) has a two-attractor exactly when one of its excesses is at most one. This proves the classification.

**5. Generating function and density.** For words beginning with \(0\), the first three-position regime can be parametrized by \(a=c+p\), \(d=b+q\), where \(b,c,p,q\ge1\). Its generating function by total length is
\[
\left(\sum_{b\ge1}z^{2b}\right)
\left(\sum_{c\ge1}z^{2c}\right)
\left(\sum_{p\ge1}z^p\right)
\left(\sum_{q\ge1}z^q\right)
=\frac{z^6}{(1-z^2)^2(1-z)^2}.
\]
The other regime is \(c=a+2+p\), \(b=d+2+q\), where \(a,d\ge1\) and \(p,q\ge0\). Its generating function is \(z^8/((1-z^2)^2(1-z)^2)\). The regimes are disjoint. Interchanging the symbols doubles the sum, yielding the claimed generating function. The total number of words with exactly four runs is \(2\binom{n-1}{3}\), whose generating function is \(2z^4/(1-z)^4\). The ratio of fourth-order pole coefficients at \(z=1\) is \(1/2\), proving the density limit.

## Verification

The standalone standard-library script `standalone/verify.py` constructs distinct-factor occurrence masks independently of the proof, determines whether any two positions form an attractor, compares that optimum with the theorem, and checks the explicit position witnesses. It checks every \((a,b,c,d)\in\{1,\ldots,8\}^4\), totaling \(4096\) quadruples. It also checks the generating-function coefficients against direct composition counts at lengths \(4\) through \(22\). Running `python3 standalone/verify.py` yields:

`VERIFY_OK exhaustive_parameter_quadruples=4096 generating_coefficients=19 parameters=1..8 lengths=4..22`

These finite experiments are supplementary. The unbounded theorem is proved by the factor classification and case analysis above.

## Relationship to prior work

String attractors were introduced in the context of dictionary compression by Prezza (2017) and further analyzed algorithmically by Kempa, Policriti, Prezza and Rotenberg (2018). Mantaci, Restivo, Romana, Rosone and Sciortino studied combinatorial behavior, conjugation, powers and classical word families (2019 preprint; 2021 journal version). Dvořáková and Hendrychová studied two-versus-three attractors for certain Rote and pseudostandard sequence prefixes (2023 preprint; 2024 journal version).

The present result concerns *all* finite binary words with exactly four nonempty constant runs. The cited general or special-sequence results supply the concept and motivation but do not state the two explicit run-length obstruction regimes or the distribution for this unrestricted four-run family. General methods for computing attractors are not themselves an all-parameter evaluation of this class. A published equivalent derivation might nonetheless exist outside the inspected corpus.

## Limitations

The statement does **not** characterize every optimal attractor position set; it provides an optimal explicit witness and the exact minimum size. It does not address five or more runs, circular attractors, scattered factors, or nonbinary alphabets. A search of accessible literature and mathematical-research records is not a proof of global novelty; specialized unindexed statements remain a residual originality risk. No independently conducted audit or external formal verification is claimed.

## References

1. N. Prezza, *String Attractors*, arXiv:1709.05314 (first version 2017-09-15), https://arxiv.org/abs/1709.05314.
2. D. Kempa, A. Policriti, N. Prezza, E. Rotenberg, *String Attractors: Verification and Optimization*, arXiv:1803.01695 (2018), https://arxiv.org/abs/1803.01695.
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (2019), https://arxiv.org/abs/1907.04660.
4. Same authors, *A Combinatorial View on String Attractors*, *Theoretical Computer Science* (2021), DOI: 10.1016/j.tcs.2020.11.006, lawful postprint: https://arpi.unipi.it/handle/11568/1062328.
5. L. Dvořáková, V. Hendrychová, *String Attractors of Rote Sequences*, arXiv:2308.00850 (first version 2023-08-01), https://arxiv.org/abs/2308.00850.
