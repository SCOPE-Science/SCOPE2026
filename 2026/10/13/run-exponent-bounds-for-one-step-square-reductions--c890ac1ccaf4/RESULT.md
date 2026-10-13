# Run-exponent bounds for one-step square reductions
## Finding
Let \(W\) be a finite word. A one-step square reduction replaces one occurrence \(XX\) by \(X\), and \(\deg^+(W)\) denotes the number of distinct resulting words. If \(\operatorname{Runs}(W)\) is the set of standard runs of \(W\), and a run \(R\) has minimum period \(d(R)\) and exponent
\[
e(R)=\frac{|R|}{d(R)},
\]
then
\[
\deg^+(W)\le
\sum_{R\in\operatorname{Runs}(W)}
\left\lfloor\frac{e(R)}{2}\right\rfloor.
\]

Consequently, for every alphabet size \(k\ge2\) and every \(n\ge1\),
\[
\deg_k^+(n)\le\left\lfloor\frac{23n}{20}\right\rfloor,
\]
where \(\deg_k^+(n)\) is the maximum one-step square-reduction out-degree of a length-\(n\) word over a \(k\)-letter alphabet. For binary words the sharper bound is
\[
\deg_2^+(n)\le\left\lfloor\frac{11n}{10}\right\rfloor.
\]
These are explicit near-conjectural bounds toward the proposed inequality \(\deg_k^+(n)\le n\).

## Assumptions and scope
A square is a nonempty factor \(XX\). A one-step square reduction changes a factor \(XX\) to one copy \(X\). Distinct outputs are counted as distinct words, regardless of how many square occurrences yield the same output.

A run is a factor of exponent at least \(2\) with minimum period \(d\), maximal under one-letter extension while preserving period \(d\). The proof uses the standard Fine--Wilf periodicity lemma and published upper bounds for the sum of exponents of runs.

No claim is made that the constants \(23/20\) or \(11/10\) are optimal. In particular, the coefficient-\(1\) conjecture remains open.

## Proof
Fix a root length \(p\ge1\). Define a binary match sequence by
\[
M_p(t)=1\quad\Longleftrightarrow\quad W_t=W_{t+p}
\]
whenever both positions exist. A square of root length \(p\) starts at position \(i\) exactly when
\[
M_p(i)=M_p(i+1)=\cdots=M_p(i+p-1)=1.
\]

For a square beginning at \(i\), let \(D_{p,i}\) be the word obtained by deleting its first copy. If \(i<j\) are two square starts with the same root length \(p\), direct comparison of the two shortened words gives
\[
D_{p,i}=D_{p,j}
\quad\Longleftrightarrow\quad
W_t=W_{t+p}\text{ for every }i\le t<j.
\]
Therefore the distinct reduction outputs of root length \(p\) are in bijection with the maximal runs of \(1\)s in \(M_p\) having length at least \(p\).

Take one such maximal match interval \([a,b]\). It corresponds to the factor
\[
I=W[a\,..\,b+p],
\]
which has period \(p\), length at least \(2p\), and is maximal for period \(p\). Let \(d\) be the minimum period of \(I\). Since \(d\le p\) and \(|I|\ge2p\), the Fine--Wilf lemma applied to periods \(d\) and \(p\) shows that \(\gcd(d,p)\) is also a period. Minimality of \(d\) therefore forces
\[
d\mid p.
\]

The factor \(I\) is also maximal for period \(d\). Indeed, if it extended one letter while preserving period \(d\), then, because \(d\mid p\), the same extension would preserve period \(p\), contradicting maximality of the match interval. Thus \(I\) is a standard run with minimum period \(d\).

Each distinct reduction class therefore maps to a pair \((R,p)\), where \(R\) is a run of minimum period \(d(R)\), the integer \(p\) is a positive multiple of \(d(R)\), and
\[
2p\le |R|.
\]
For a fixed run \(R\), there are at most
\[
\left\lfloor\frac{|R|}{2d(R)}\right\rfloor
=
\left\lfloor\frac{e(R)}{2}\right\rfloor
\]
such period labels. Different root lengths produce outputs of different lengths, so no additional collision can invalidate the upper count. Summing over runs proves
\[
\deg^+(W)\le
\sum_R\left\lfloor\frac{e(R)}{2}\right\rfloor.
\]

Czarkowski proved that the sum of run exponents in a length-\(n\) word is at most \(2.3n\), and at most \(2.2n\) for binary words. Hence
\[
\deg^+(W)
\le \frac12\sum_R e(R)
\le \frac{23n}{20},
\]
and in the binary case
\[
\deg^+(W)\le\frac{11n}{10}.
\]
Since the out-degree is an integer, taking floors gives the stated bounds.

## Verification
The bundled `verify.py` independently checks the structural correspondence on every binary word of lengths through \(11\) and every ternary word of lengths through \(7\). For each word it compares direct square-reduction outputs with maximal match intervals, reconstructs the associated standard runs, verifies that the run's minimum period divides the square-root length, and checks the structural inequality.

This finite computation is a consistency test, not the proof of the universal statement. The universal statement is established by the match-interval argument, Fine--Wilf periodicity, and the published run-exponent bounds.

The checker also verifies on the word `00100` that there are two distinct one-step reduction outputs but only one distinct square factor. This separates the present invariant from the solved distinct-square-factor problem.

## Relationship to prior work
Grytczuk and Stankiewicz introduced the one-step reduction out-degree \(\deg_k^+(n)\) and conjectured that
\[
\deg_k^+(n)\le n
\]
for every \(k\ge2\). They observed its resemblance to the then-open Fraenkel--Simpson distinct-squares conjecture.

The distinct-square-factor problem is now a different, better understood invariant: Brlek and Li proved a strong linear bound on the number of distinct square factors. That result does not imply a square-reduction out-degree bound, because different occurrences of the same square factor can produce different shortened words. The word `00100` already has two distinct square-reduction outputs although its only distinct square factor is `00`.

Czarkowski's run-exponent work gives the numerical estimates \(2.3n\) in general and \(2.2n\) for binary words, but does not discuss square reductions. The structural inequality above supplies the missing implication from square-reduction classes to period labels inside standard runs.

## Limitations
The coefficient-\(1\) conjecture is not proved. The argument loses information twice: it counts every admissible multiple of a run's minimum period, and it then replaces \(\lfloor e(R)/2\rfloor\) by \(e(R)/2\). Stronger constraints on which period labels actually yield distinct reductions could improve the constants.

The originality search cannot rule out an unindexed note or thesis containing the same run reformulation. The result should therefore be read as a proved mathematical implication with documented literature comparisons, not as a claim that no equivalent observation has ever been made.

## References
1. J. Grytczuk and M. Stankiewicz, “Square-free reducts of words,” arXiv:2011.12822, first public version 2020-11-25.
2. S. Brlek and S. Li, “On the number of squares in a finite word,” arXiv:2204.10204; published with DOI 10.5070/C65165014.
3. A. Czarkowski, “Improved Bounds on the Sum of Exponents of Runs in a String,” 37th Annual Symposium on Combinatorial Pattern Matching, 2026, DOI 10.4230/LIPIcs.CPM.2026.23.
4. N. J. Fine and H. S. Wilf, “Uniqueness theorems for periodic functions,” Proceedings of the American Mathematical Society 16 (1965), 109--114.
