# Exact fixed-content Simon-congruence classes for binary two-marker words

## Finding
Let \(m\ge0\), \(k\ge3\), and \(q=k-2\). Work over the ordered alphabet \(\{0,1\}\) and consider exactly the words
\[
w(a,b,c)=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\quad a+b+c=m.
\]
For words \(u,v\), let \(u\sim_k v\) mean that they have identical **sets** (not multisets) of scattered subsequences of length at most \(k\). Set
\[
\Phi_{m,k}(a,b,c)=\bigl(\min(a,q),\min(b,q),\min(c,q),
\mathbf1_{a+b\ge q+1},\mathbf1_{b+c\ge q+1}\bigr).
\]
Then \(w(a,b,c)\sim_k w(a',b',c')\) **if and only if** \(\Phi_{m,k}(a,b,c)=\Phi_{m,k}(a',b',c')\), whenever both triples sum to the same \(m\).

Write \(F_k(m)\) for the number of \(\sim_k\)-classes among these \(\binom{m+2}{2}\) words. Define \(\binom{N}{3}_+=\binom{N}{3}\) for integers \(N\ge3\), and \(0\) otherwise. The complete class-count formula is
\[
\boxed{F_k(m)=\sum_{j=0}^3(-1)^j\binom3j\left[
\binom{m-j(q+1)+3}{3}_+-\binom{m-jq+2}{3}_+\right]
+3\mathbf1_{m\ge2q+1}+\mathbf1_{m\ge2q+2}.}
\]
In particular, the class count stabilizes at
\[
\boxed{F_k(m)=3(k-2)^2+3(k-2)+5}
\]
for all \(m\ge3(k-2)\) when \(k\ge4\), and \(F_3(m)=11\) for all \(m\ge4\). These stabilization thresholds are sharp. At depth \(k=2\), the class count is \(1\) for \(m=0\) and \(3\) for \(m\ge1\); at depth \(k=1\), it is \(1\) for every \(m\).

## Assumptions and scope
A scattered subsequence results from deleting zero or more positions while keeping the surviving positions in order. The empty subsequence is included but affects no equivalence. Words are linear, not circular. The two occurrences of \(1\) are exact and all \(m\) zeros are distributed over the three indicated gaps. Only set membership matters; multiplicities of embeddings are ignored. The equivalence comparison is between words having the **same** \(m\); it is not asserted that the five-coordinate invariant classifies words with different zero counts.

## Proof
**Step 1 (recover the five coordinates).** Any scattered subsequence containing two ones must use both marked positions. For \(0\le t\le q\), the patterns \(0^t11\), \(10^t1\), and \(110^t\), each of length at most \(k\), occur respectively exactly when \(a\ge t\), \(b\ge t\), and \(c\ge t\). Their membership therefore recovers the three clipped coordinates. The two patterns \(0^{q+1}1\) and \(10^{q+1}\), both of length \(k\), occur respectively when \(a+b\ge q+1\) and \(b+c\ge q+1\). Thus \(\sim_k\) implies equality of \(\Phi_{m,k}\).

**Step 2 (sufficiency).** There are at most two ones in any scattered subsequence of the word. Patterns with no ones are \(0^t\), determined by the common total \(m\). A pattern with both ones has form \(0^u1\,0^v1\,0^t\), with \(u+v+t\le q\), and occurs precisely when \(u\le a\), \(v\le b\), \(t\le c\); the clipped coordinates determine this. A pattern with one one is \(0^u1\,0^v\), with \(u+v\le q+1\). It occurs precisely if
\[
(a\ge u\ \land\ b+c\ge v)\quad\lor\quad(a+b\ge u\ \land\ c\ge v).
\]
If \(u,v\ge1\), both are at most \(q\); all four comparisons are determined by clipped gaps because, for integers \(0\le s\le q\), both \(x\ge s\) and \(x+y\ge s\) are determined by \(\min(x,q)\) and \(\min(y,q)\). If \(u=0\) or \(v=0\), the only possible test above clip depth \(q\) is \(v=q+1\) or \(u=q+1\), exactly the two recorded flags. Hence equality of \(\Phi_{m,k}\) determines every length-at-most-\(k\) subsequence, proving the equivalence.

**Step 3 (count clipped triples).** For a triple \((A,B,C)\in\{0,\ldots,q\}^3\) to equal the clipped version of a nonnegative triple summing to \(m\), either \(A+B+C=m\), or \(A+B+C<m\) and at least one coordinate equals \(q\). Thus the number \(B_q(m)\) of realizable clipped triples is the number of points in \(\{0,\ldots,q\}^3\) with sum at most \(m\), minus the number of points in \(\{0,\ldots,q-1\}^3\) with sum strictly less than \(m\). Counting bounded triples by inclusion–exclusion yields
\[
B_q(m)=\sum_{j=0}^3(-1)^j\binom3j\left[
\binom{m-j(q+1)+3}{3}_+-\binom{m-jq+2}{3}_+\right].
\]

**Step 4 (count splits of the two flags).** If at most one clipped coordinate equals \(q\), the common sum \(m\) uniquely determines the original triple, hence the flags. If all three clipped coordinates equal \(q\), both flags are one because \(2q\ge q+1\). If exactly two coordinates equal \(q\) and the third lies in \(\{1,\ldots,q-1\}\), both flags again equal one. Only the three clipped triples \((q,q,0)\), \((0,q,q)\), and \((q,0,q)\) can split. Each is realizable once \(m\ge2q\). The first two have one possible flag-pair at \(m=2q\), and two from \(m=2q+1\) onward, adding one class each. For \((q,0,q)\), there is one possible pair at \(m=2q\), two at \(m=2q+1\), and three at \(m\ge2q+2\), adding one then two classes. The total correction is \(3\mathbf1_{m\ge2q+1}+\mathbf1_{m\ge2q+2}\), proving the boxed formula.

**Step 5 (sharp stabilization).** For \(m\ge3q\), every clipped triple with at least one coordinate \(q\) is realizable, while no triple with every coordinate below \(q\) is realizable. Their number is \((q+1)^3-q^3=3q^2+3q+1\). For \(q\ge2\), the correction has already reached four at \(m=3q\), giving \(3q^2+3q+5\). At \(m=3q-1\), the clipped triple \((q,q,q)\) is still impossible; for \(q=2\) the correction is also one smaller, so stabilization cannot occur earlier. For \(q=1\), the clipped triples are all present at \(m=3\), but the correction reaches four only at \(m=4\). The depth-two statement follows by recording only whether a zero occurs before both ones and after both ones; for fixed \(m>0\) exactly three flag-pairs occur. Depth one cannot distinguish positions of the two ones at fixed \(m\). This completes the proof.

## Verification
`checker.py` uses a direct left-to-right construction of **all** scattered subsequences, independently of the five-coordinate formula. It checks that direct spectra and claimed invariants define exactly the same partition, and compares the counted classes with the closed expression for \(3\le k\le9\) and \(0\le m\le3(k-2)+5\). It also checks stabilization, sharp threshold values, and the depth-two boundary cases. Execute `python checker.py` using Python 3 and no additional packages. A finite test is not used as proof of the unlimited statement: Steps 1–5 establish all quantifiers.

## Relationship to prior work
Karandikar, Kufleitner, and Schnoebelen (2013) study the unrestricted index of Simon's congruence; their Lemmas 3.1–3.2 show necessary clipped multiplicity and inter-marker gap information for words with few occurrences of one symbol, but do not supply this fixed-length five-coordinate classification or its exact class-count formula. Fleischer and Kufleitner (2018), and Gawrychowski and coauthors (2020), provide general algorithms for determining congruence or normal forms; general algorithmic decidability does not state the present explicit restricted counting law. Fleischmann and coauthors (2026) consider **jumbled** subsequences and embedding counts rather than the ordinary fixed-content index computed here. The formula is for ordinary (multiplicity-free) Simon congruence, not for binomial/Parikh-matrix equivalence or contiguous substring spectra.

## Limitations
No claim is made for alphabet sizes above two, for three or more occurrences of \(1\), for variable \(m\) comparisons, or for the full unrestricted Simon quotient. The classification addresses exact equivalence classes, not the number of words in each class. The literature comparison may have missed an equivalent formula in another notation.

## References
1. P. Karandikar, M. Kufleitner, and P. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, arXiv:1310.1278, first public version 2013-10-03. https://arxiv.org/abs/1310.1278
2. L. Fleischer and M. Kufleitner, *Testing Simon's congruence*, arXiv:1804.10459, first public version 2018-04-27. https://arxiv.org/abs/1804.10459
3. P. Gawrychowski, M. Kosche, T. Koß, F. Manea, and S. Siemer, *Efficiently Testing Simon's Congruence*, arXiv:2005.01112, first public version 2020-05-03. https://arxiv.org/abs/2005.01112
4. P. Fleischmann, A. Huch, S. Kim, T. Koß, and E. Wiards, *Jumbled Simon's Equivalence and Embeddings*, arXiv:2610.17910v1, dated 2026-10-13. https://arxiv.org/html/2610.17910v1
