# The complete minimal-absent-subsequence basis of a four-run binary word

## Finding

Let \(a,b,c,d\) be arbitrary positive integers and let \(w=0^a1^b0^c1^d\). A word is a *scattered subsequence* of \(w\) when it can be formed by deleting symbols, without changing the order of those retained. A *minimal absent subsequence* is an absent word all of whose proper scattered subsequences occur in \(w\). The alphabet for absence is exactly \(\{0,1\}\).

The complete set \(\operatorname{MAS}(w)\) consists of these five words:

\[
0^{a+c+1},\quad 1^{b+d+1},\quad
0^{a+1}1^{d+1},\quad 1^{b+1}0,\quad 10^{c+1},
\]

plus \(0^{a+1}10\) if \(c\ge2\), plus \(101^{d+1}\) if \(b\ge2\), and plus \(1010\) if \(b,c\ge2\). All listed words are distinct. In particular,

\[
|\operatorname{MAS}(w)|
=5+\mathbf 1_{b\ge2}+\mathbf 1_{c\ge2}
+\mathbf 1_{b\ge2}\mathbf 1_{c\ge2}\in\{5,6,8\}.
\]

The complete length spectrum is given by the polynomial

\[
\begin{aligned}
P_w(z)={}&z^{a+c+1}+z^{b+d+1}+z^{a+d+2}
+z^{b+2}+z^{c+2}\\
&+\mathbf1_{c\ge2}z^{a+3}
+\mathbf1_{b\ge2}z^{d+3}
+\mathbf1_{b\ge2}\mathbf1_{c\ge2}z^4,
\end{aligned}
\]

where the coefficient of \(z^j\) counts the minimal absent subsequences of length \(j\). Colliding exponents contribute with their full multiplicity.

For a fixed length \(n\ge4\), among the \(\binom{n-1}{3}\) four-run words beginning with \(0\), exactly \(n-3\) have five minimal absent subsequences, exactly \(2\binom{n-3}{2}\) have six, and exactly \(\binom{n-3}{3}\) have eight (binomial coefficients with upper argument below the lower argument are understood as zero). Consequently their average basis cardinality is

\[
8-\frac{6(2n-5)}{(n-1)(n-2)},
\]

and the proportion having eight tends to one as \(n\to\infty\).

## Assumptions and scope

All four run lengths are positive integers, so \(w\) has exactly four nonempty, alternating runs. The theorem concerns noncontiguous scattered subsequences, not minimal absent contiguous factors; the latter use a different notion of minimality. Complementing every symbol gives the symmetric version beginning with \(1\). The lengths and multiplicities above are exact, not asymptotic, for each positive quadruple.

## Proof

Write \(u\preceq w\) when \(u\) is a scattered subsequence of \(w\). The set of subsequences is downward closed under \(\preceq\). Therefore it is enough to prove two assertions: every listed word is absent with every single-letter deletion present, and every absent binary word contains at least one listed word as a scattered subsequence.

**Absence and minimality of the candidates.** The two constant words have one symbol more than the respective total symbol counts in \(w\). The word \(0^{a+1}1^{d+1}\) is absent: choosing more than \(a\) leading zeros forces use of the third run, after which only \(d\) ones remain. Removing a zero allows the \(a\) first-run zeros followed by \(d+1\) of the \(b+d\) ones; removing a one allows \(a+1\) zeros followed by the \(d\) final ones. The word \(1^{b+1}0\) is absent because the only zeros after any ones are in the third run, preceded by at most \(b\) ones. Deleting a one makes \(1^b0\) present, and deleting its terminal zero leaves \(1^{b+1}\), present since \(d\ge1\). Similarly \(10^{c+1}\) is absent because only the \(c\) third-run zeros follow any one; deletion of its first one leaves \(0^{c+1}\) (present because \(a\ge1\)), while deletion of a zero leaves \(10^c\).

If \(c\ge2\), the word \(0^{a+1}10\) is absent: after \(a+1\) zeros, any subsequent one is in the last run, with no zero afterward. Removing a leading zero gives \(0^a10\), removing the middle one gives \(0^{a+2}\), and removing the final zero gives \(0^{a+1}1\); all are present. If \(b\ge2\), the word \(101^{d+1}\) is absent: after a one and a later zero, only the last \(d\) ones remain. The deletions produce \(01^{d+1}\), \(1^{d+2}\), or \(101^d\), all present (the second uses \(b\ge2\)). If \(b,c\ge2\), the word \(1010\) is absent because \(w\) has no zero after its last run of ones; its four single-letter deletions \(010\), \(110\), \(100\), and \(101\) are all present. Deletions of identical letters give the same shorter candidate, so the displayed cases cover every single-letter deletion. Every proper subsequence of each candidate is itself a subsequence of such a deletion and is therefore present. The listed words are distinct by their initial/terminal letters and run shapes; the two words of form \(1^i0^j\) are distinct because the former has \(i=b+1\ge2\) and the latter has \(i=1\).

**Exhaustion.** Take any absent binary word \(u\). If \(u\) has at least five maximal constant runs, then \(1010\preceq u\). The same is true if it has exactly four runs and starts with one. When \(b,c\ge2\), this directly supplies the listed word \(1010\); if \(b=1\), its subsequence \(110=1^{b+1}0\) is listed; if \(c=1\), its subsequence \(100=10^{c+1}\) is listed. Thus we need only treat words with one, two, or three runs, and four-run words beginning with zero.

One-run absent words contain \(0^{a+c+1}\) or \(1^{b+d+1}\). For two runs of shape \(1^i0^j\), subsequence occurrence is equivalent to \(i\le b\) and \(j\le c\); if either inequality fails, the word contains \(1^{b+1}0\) or \(10^{c+1}\). For two runs of shape \(0^i1^j\), occurrence is equivalent to

\[
(i\le a\ \text{and}\ j\le b+d)
\quad\text{or}\quad
(i\le a+c\ \text{and}\ j\le d).
\]

If this fails, then either \(i>a+c\), or \(j>b+d\), or both \(i>a\) and \(j>d\), yielding one of the first three listed words.

For three-run words \(0^i1^j0^k\), subsequence occurrence is equivalent to \(i\le a\), \(j\le b\), and \(k\le c\). Violations of the last two bounds produce \(1^{b+1}0\) or \(10^{c+1}\). A violation of \(i\le a\) produces \(0^{a+1}10\) if \(c\ge2\); if \(c=1\), it instead contains \(0^{a+c+1}\) after deleting its intervening ones. Likewise \(1^i0^j1^k\) occurs exactly when \(i\le b\), \(j\le c\), and \(k\le d\). Violating the first or second bound produces \(1^{b+1}0\) or \(10^{c+1}\). Violating \(k\le d\) produces \(101^{d+1}\) if \(b\ge2\); if \(b=1\), the word instead contains \(1^{b+d+1}\) after deleting its zero-run.

Finally, for a four-run word \(u=0^i1^j0^k1^\ell\), its four runs must embed in the four corresponding distinct runs of \(w\); hence it occurs exactly when \(i\le a\), \(j\le b\), \(k\le c\), and \(\ell\le d\). Any violated bound yields, respectively, the same obstruction as the corresponding violated bound for \(0^i1^j0^k\) or \(1^j0^k1^\ell\), which are subsequences of \(u\). This exhausts every absent word. Since each listed word is minimal absent, no other minimal absent word exists.

**Spectrum and finite-length distribution.** Counting the eight disjoint templates by length gives \(P_w(z)\). Its value at \(z=1\) is the stated cardinality. If \(a+b+c+d=n\), the five-element case is \(b=c=1\), with \(n-3\) choices for \(a,d\). The six-element case has exactly one of \(b,c\) equal to one and the other at least two, giving \(2\binom{n-3}{2}\) choices. The eight-element case has \(b,c\ge2\), giving \(\binom{n-3}{3}\) choices after subtracting one from each interior run. Their sum is \(\binom{n-1}{3}\). Weighted averaging yields the displayed mean and its limit.

## Verification

Run the self-contained file `verify.py` with Python 3.9 or later. It independently constructs the full set of scattered subsequences by position-by-position inclusion and enumerates the minimal absent candidates using the proper-prefix necessity and one-deletion criterion. It compares that exhaustive set with the symbolic templates for all \(256\) quadruples \(1\le a,b,c,d\le4\). It additionally checks the predicted candidates directly for \(625\) larger-parameter quadruples and checks the finite-length multiplicities for every \(4\le n\le40\). The successful run prints `VERIFY_OK exhaustive_quadruples=256 long_witness_checks=625 composition_lengths=4..40`. These tests are finite consistency checks; the case analysis above supplies the universal proof.

## Relationship to prior work

Kosche, Koß, Manea and Siemer introduced a general theory and characterizations of minimal absent scattered subsequences, including Theorem 3.1 and a general enumeration framework. Their theorem and algorithms cover arbitrary input words at the algorithmic level. The result here provides a closed symbolic minimal-forbidden basis, complete length spectrum, and fixed-length distribution specifically for four alternating runs; it does not claim to improve those general algorithms. Petković, Ćirić and Bogdanović previously studied minimal forbidden subwords and algorithms, including a binary-alphabet case. Their potentially overlapping full article could not be inspected, so possible exact overlap remains a material literature risk.

The related published finding on shortest absent subsequences of binary words concerns only the shortest layer of the absent-word order, not its complete minimal antichain. The existing calculation for the alternating family \((01)^k\) includes the special case \(a=b=c=d=1\), but does not establish the arbitrary-run formula.

## Limitations

The alphabet is binary and exactly four nonempty alternating runs are assumed. The theorem makes no claim about words with five or more runs or larger alphabets. General forbidden-subsequence algorithms already exist; novelty is asserted only for the explicit symbolic four-run classification, conditional thresholds, length spectrum, and distribution, subject to the identified older-literature uncertainty. The tests do not prove the infinite parameter range, and no independent audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, first public arXiv posting 2021-08-31, arXiv:2108.13968; subsequently *Fundamenta Informaticae* 189 (2023). https://arxiv.org/abs/2108.13968
2. T. Petković, M. Ćirić and S. Bogdanović, *Minimal Forbidden Subwords*, *Information Processing Letters* 92 (2004), 211–218. https://doi.org/10.1016/j.ipl.2004.09.001
