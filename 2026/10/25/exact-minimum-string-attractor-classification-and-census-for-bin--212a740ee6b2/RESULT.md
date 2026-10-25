# Exact minimum string-attractor classification and census for binary four-run words

## Finding

For every finite word \(w\), a *string attractor* is a set of positions meeting at least one occurrence of every nonempty distinct contiguous factor of \(w\). Write \(\gamma(w)\) for its minimum cardinality. For every four-tuple of positive integers \(a,b,c,d\), set
\[
w=0^a1^b0^c1^d.
\]
Then
\[
\gamma(w)=
\begin{cases}
3,& (a>c\text{ and }d>b)\text{ or }(c\ge a+2\text{ and }b\ge d+2),\\
2,&\text{otherwise}.
\end{cases}
\]
The same conclusion holds after interchanging the binary symbols. Both exceptional conditions are sharp.

If \(F_n\) is the number of *indexed* binary words of length \(n\) with exactly four maximal constant runs and string-attractor number three (not identifying rotations or reversals), then
\[
\sum_{n\ge0}F_nz^n=
\frac{2(z^6+z^8)}{(1-z)^2(1-z^2)^2}.
\]
Consequently the proportion of four-run binary length-\(n\) words requiring three attractor positions tends to \(1/2\) as \(n\to\infty\).

## Assumptions and scope

A position \(p\) *hits* an occurrence \(w[i..j]\) when \(i\le p\le j\). An attractor \(S\) requires, for each distinct nonempty contiguous factor \(u\), at least one occurrence \(w[i..j]=u\) hit by some position in \(S\). Occurrences need not be unique and different factors may be witnessed by different occurrences. Indices may be zero-based or one-based consistently. The theorem assumes all four run lengths are strictly positive, so that precisely three symbol-change boundaries exist. The two choices for the initial binary letter are counted separately in \(F_n\).

## Proof

**A three-position universal upper bound.** Denote the four consecutive maximal runs by \(A,B,C,D\). A nonconstant contiguous factor spans at least one of the three adjacent run boundaries; any occurrence spanning a boundary is hit by either position of its two-symbol boundary. If \(b\ge d\), select the *last* position in each of \(A,B,C\). The three boundaries are hit, and the selected positions also meet an occurrence of every constant-symbol factor: the longest zero run has length \(\max(a,c)\) and the longest one run has length \(b\), with the zero-run maximum handled by the chosen \(A\)- or \(C\)-position. If \(d>b\), select the last position of \(A\), the first position of \(C\), and the first position of \(D\). The same boundary and constant-factor argument applies. Thus \(\gamma(w)\le3\). Since both binary letters occur, \(\gamma(w)\ge2\).

**Two-position witnesses in all nonexceptional cases.** The notation “first/last of a run” below denotes one position, not an entire run.

(i) If \(a\ge c\) and \(b\ge d\), select the last of \(A\) and last of \(B\). These meet all factors containing the first or middle boundary, including every factor extending across multiple boundaries. A factor whose occurrence uses only the last boundary has form \(0^i1^j\) with \(1\le i\le c\le a\) and \(1\le j\le d\le b\); it also occurs at the first boundary, where it meets the last \(A\)-position. Constant factors are covered by the maximal first zero and second one runs.

(ii) If \(a\le c\) and \(b\le d\), select the first of \(C\) and the first of \(D\). The symmetric argument covers every factor, using the last boundary to replace any factor consisting only of the first boundary. The selected runs also realize both maximal constant-symbol factors.

(iii) If \(c=a+1\) and \(b>d\), select the first of \(B\) and first of \(C\). These meet the first and middle boundaries; a factor containing more than one boundary is also hit. A factor using only the last boundary is \(0^i1^j\), with \(i\le c\) and \(j\le d\). If \(i=c\), its occurrence at the last boundary meets the first position of \(C\). Otherwise \(i\le a\) and \(j\le d<b\), so an occurrence at the first boundary meets the first position of \(B\). Maximal zero and one factors meet \(C\) and \(B\), respectively.

(iv) If \(c>a\) and \(b=d+1\), select the last of \(B\) and last of \(C\). A factor using only the first boundary is \(0^i1^j\) with \(i\le a\), \(j\le b\). If \(j=b\), that occurrence meets the last position of \(B\). Otherwise \(j\le d\), so an occurrence at the last boundary meets the last of \(C\). All other nonconstant factors cross the middle or last boundary, and the selected positions hit maximal constant-symbol factors.

These four cases exhaust the complement of the two exceptional regimes. Indeed, if neither (i) nor (ii) applies, exactly one of \(a>c,d>b\) and \(c>a,b>d\) holds. The former is exceptional. In the latter, failure of \(c\ge a+2\) or failure of \(b\ge d+2\) forces (iii) or (iv).

**Three positions are necessary in the two exceptional regimes.** If \(a>c,d>b\), the factor \(0^a\) occurs only in \(A\), and \(1^d\) occurs only in \(D\). Every occurrence of \(10\) lies at the middle \(B/C\) boundary. These three factors therefore force three different positions.

Now suppose \(c\ge a+2\) and \(b\ge d+2\). The uniquely longest zero- and one-block factors \(0^c\), \(1^b\) force any hypothetical two-position attractor to choose one position in \(C\) and one in \(B\). The factor \(01^{d+1}\) can occur only at the first \(A/B\) boundary (the final one run is shorter); its intersection with \(B\) consists of the first \(d+1\) positions of \(B\). Hence the selected \(B\)-position is **not** the last position of \(B\). Similarly, \(0^{a+1}1\) occurs only at the last \(C/D\) boundary (the first zero run is shorter); its intersection with \(C\) consists of the final \(a+1\) positions of \(C\). Thus the selected \(C\)-position is **not** the first position of \(C\). But the factor \(10\) occurs only across the middle \(B/C\) boundary and can be hit, from those two runs, only at the last position of \(B\) or the first position of \(C\). This is a contradiction. The universal upper bound completes the classification.

**Exact enumeration and density.** The regimes are disjoint. For the first, write \(a=c+i\), \(d=b+j\), where \(b,c,i,j\ge1\). The ordinary length generating function for words starting with zero is
\[
\frac{z^6}{(1-z^2)^2(1-z)^2}.
\]
For the second, write \(c=a+i\), \(b=d+j\), where \(a,d\ge1\) and \(i,j\ge2\); its generating function is \(z^8/((1-z^2)^2(1-z)^2)\). Complementing the symbols doubles the count. As \(z\to1\), the combined rational function has leading singularity \((1-z)^{-4}\), giving \(F_n\sim n^3/6\). The number of all indexed four-run binary words is \(2\binom{n-1}{3}\sim n^3/3\). Their ratio therefore tends to \(1/2\).

## Verification

The standalone Python 3 program `verify.py` independently constructs distinct factor-occurrence masks and brute-forces candidate attractor sets. It exhausts all \(7^4=2401\) positive run-length quadruples with each parameter at most seven, compares the computed minimum with the formula, and separately tests the constructive witnesses. A separate integer calculation matches generating-function coefficients to run-composition counts for every length from \(4\) through \(22\). Run it with `python3 verify.py`. The finite checks support but do not replace the all-parameter proof above.

## Relationship to prior work

Mantaci et al. introduced finite string-attractor theory, including general bounds, while later papers examined infinite words and specific morphic, automatic, and Rote families. This result instead completely determines the attractor number and its exact binary length census in the four-run finite-word family. These earlier broad results and the general definition do not by themselves imply the present explicit parameter thresholds. Other published exact attractor enumerations for isolated finite lengths and special morphic prefixes likewise concern different domains. The particular theorem could still exist under a different formulation in literature not located by the searches described in `AUDIT.json`.

## Limitations

The theorem only concerns words with exactly four maximal runs on a binary alphabet, plus bit-complemented copies. It does not classify the positions or number of all minimum attractor sets, and it does not determine attractor numbers for words with five or more runs. Exhaustive computation stops at the ranges specified above. Published equivalence has not been definitively ruled out. Independent mathematical audit has not been performed.

## References

1. S. Mantaci and collaborators, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (first posted 2019-07-10), https://arxiv.org/abs/1907.04660.
2. G. Restivo, M. Romana, M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376 (first posted 2022-06-01), https://arxiv.org/abs/2206.00376.
3. F. Gheeraert, M. Romana, M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, arXiv:2302.13647 (first posted 2023-02-27), https://arxiv.org/abs/2302.13647.
4. L. Dvořáková and L. Hendrychová, *String attractors of Rote sequences*, arXiv:2308.00850 (first posted 2023-08-01), https://arxiv.org/abs/2308.00850.
