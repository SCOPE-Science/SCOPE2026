# An exact fourth off-diagonal family of greedy 2-sumfree sequences

## Finding
For every integer \(f\ge8\), let \(S_{f,2f+4}\) be the increasing strict greedy 2-sumfree sequence initialized with \(f\) and \(2f+4\): each subsequent term is the least larger integer not expressible as the sum of two **distinct** earlier terms. For integer endpoints write \([u,v]_{\mathbb Z}=\{u,u+1,\ldots,v\}\). Put \(M=5f+7\) and
\[
\begin{aligned}
P_f={}&\{f\}\cup[2f+4,3f+3]_{\mathbb Z}\cup[4f+4,4f+8]_{\mathbb Z}\\
&\cup[6f+6,6f+7]_{\mathbb Z}\cup[7f+12,8f+8]_{\mathbb Z}\cup[9f+11,9f+15]_{\mathbb Z},\\
Q_f={}&[11f+12,11f+14]_{\mathbb Z}\cup[12f+19,13f+14]_{\mathbb Z}\\
&\cup[14f+18,14f+22]_{\mathbb Z}\cup\{16f+18\}.
\end{aligned}
\]
Then the **complete sequence**, not merely a long numerical prefix, is
\[
\boxed{S_{f,2f+4}=P_f\ \sqcup\ \bigsqcup_{k\ge0}(Q_f+kM).}
\]
Its sequence of successive differences has **minimal preperiod** \(2f+10\) and **minimal period length** \(f+5\). In particular, this supplies an exact unbounded-parameter fourth off-diagonal case of the periodicity problem for strict greedy 2-sumfree sequences.

## Assumptions and scope
The only variable parameter is the integer \(f\ge8\); the second seed is exactly \(g=2f+4\). The sums used for exclusion have two distinct summands, and the algorithm is initialized with the seeds even if a smaller integer could otherwise have been selected. The endpoint intervals are inclusive and nonempty in this range. The claim is an equality of infinite integer sets together with the exact minimal periodicity data of their ordered differences. No statement is made about smaller seeds or arbitrary pairs of seeds.

## Proof
**1. Candidate and interval-sum identity.** Let \(T_f\) be the right-hand side of the boxed formula. For \(f\ge8\), all displayed intervals are nonempty and disjoint in their indicated order (also across consecutive translates), with initial elements \(f\) and \(2f+4\). For any finite, pairwise disjoint integer intervals \(I_i=[a_i,b_i]_{\mathbb Z}\), the set of sums of *distinct* elements is exactly the union of
\[
[a_i+a_j,b_i+b_j]_{\mathbb Z}\quad(i<j),\qquad
[2a_i+1,2b_i-1]_{\mathbb Z}\quad(a_i<b_i).
\]
The first identity is the elementary interval addition law; for the second, consecutive choices of two unequal integers realize every integer from the smallest to the largest possible sum. Neither rule counts a repeated singleton as two distinct elements.

**2. Exact finite affine-endpoint certificate.** Let \(L=3M\) and \(B=5L=15M\). Exactly **57** component intervals of \(T_f\) lie in \([1,B]_{\mathbb Z}\): the six components of \(P_f\), thirteen translates of each of the first three components of \(Q_f\), and twelve translates of its final singleton. The inequalities identifying these components hold for every integer \(f\ge8\). Exactly 44 of the 57 intervals have at least two elements. By step 1, the distinct-pair sumset \(U_f\) of these components has an exact presentation by \(\binom{57}{2}+44=1640\) integer intervals, with all endpoints affine in \(f\). All terms of any representation \(n=x+y\) with \(n\le B\) and positive summands satisfy \(x,y<n\le B\), so no omitted later term can affect this finite test.

The accompanying `verify.py` constructs these **symbolic** affine endpoints, not a numerical approximation, and verifies the following two exact statements:
\[
T_f\cap U_f\cap[2f+5,B]_{\mathbb Z}=\varnothing,
\qquad
(T_f\cup U_f)\cap[2f+5,B]_{\mathbb Z}=[2f+5,B]_{\mathbb Z}.
\]
Here the first intersection restricts to the same interval as the second. The verifier calculates the full family of 3396 affine boundary expressions (the two domain bounds and both endpoints of all 1697 component/sum intervals). For every boundary expression it also considers shifts by \(-1,0,+1\), as needed to determine integer adjacency. Grouping equal slopes and comparing the extreme intercepts of unequal slopes shows **the largest possible positive crossing parameter is exactly 14**. Hence every endpoint ordering and adjacency comparison needed by the two displayed assertions is unchanged for every real \(f\ge15\). The verifier checks exact interval unions and disjointness separately for the eight integers \(f=8,9,\ldots,15\), including \(f=15\). This certifies the assertions for **all** integers \(f\ge8\), since the remaining infinite range has fixed affine endpoint order. In each checked case the 1640 generating sum intervals merge to 44 components, disjoint from the candidate components, and their union with the candidate covers the entire prescribed range. The precise reproducible algorithm, its crossing bound, and all source data are included in `verify.py`.

The greedy rule and the initial seeds therefore force \(S_{f,2f+4}\) and \(T_f\) to agree at every integer through \(B=15M\). This is a finite **symbolic certificate with a proof of infinite parameter stabilization**, not an inference from a bounded list of sampled values.

**3. Extension beyond the checked integer range.** The periodic tail of \(T_f\), viewed modulo \(M\), has residue set
\[
R_f=[f-3,f]_{\mathbb Z}\cup[2f+5,3f]_{\mathbb Z}\cup[4f+4,4f+8]_{\mathbb Z}.
\]
All these residue classes have their first occurrence at or before \(L+r\), so for each \(n\ge L\), membership in \(T_f\) depends only on \(n\bmod M\). Thus its characteristic sequence on \([L,2L)\), \([2L,3L)\), \([3L,4L)\), and \([4L,5L)\) consists of four identical, nonzero blocks of length \(L\), since \(L=3M\). The corresponding four blocks of the actual greedy sequence are identical, by step 2.

The proved four-block continuation theorem for strict greedy 2-sumfree sequences (van Berkel--Bosma, arXiv:2609.18522v1, Theorem 15, including its proof) states that if the second through fifth blocks of a five-block initial characteristic word are identical and nonzero, then those blocks continue indefinitely. Apply it at block width \(L\). The resulting infinite continuation agrees with \(T_f\), because the repeated length-\(L\) block is already periodic with the finer modulus \(M\). Therefore \(S_{f,2f+4}=T_f\) at every positive integer.

**4. Sharp period and preperiod.** Each translated copy of \(Q_f\) has \(3+(f-4)+5+1=f+5\) entries and displacement \(M\). The cyclic gap word has precisely three gaps larger than one, of respective lengths \(f+5\), \(f+4\), and \(2f-4\); all remaining gaps equal one. If its least period were a proper divisor of \(f+5\), the number of repetitions of that shorter word would divide three, and hence equal three. This would force the three exceptional gaps to have equal lengths, contrary to \(f+5\ne f+4\). Thus its minimal period is \(f+5\). The prefix has \(1+f+5+2+(f-3)+5=2f+10\) terms. Its final element is \(9f+15\); the gap to the first tail term \(11f+12\) is \(2f-3\), whereas the corresponding cyclic gap one full period later is one. Therefore the minimal preperiod of the successive-difference word is exactly \(2f+10\).

## Verification
Run `python3 verify.py` using Python's standard library. The independent replay prints `VERIFY_OK`, with 57 candidate intervals, 1640 distinct-pair sum intervals, 3396 affine endpoint expressions, exact crossing maximum 14, all eight parameters from 8 through 15 checked with exact interval unions, and independent termwise greedy comparisons for every parameter from 8 through 40. The **infinite-parameter** step is the affine-crossing argument in the proof, which is explicitly checked by the code; independent finite term comparisons are additional corroboration. The proof also uses the cited, already established four-block continuation theorem and does not assert an external formal proof or independent mathematical audit.

## Relationship to prior work
D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences* (arXiv:2609.18522v1; first posted 2026-09-16), define these greedy sequences, formulate global conjectures for minimal periods and preperiods (Conjectures 5 and 9), establish a continuation theorem (Theorem 15), and report finite-parameter periodicity checks (Theorems 16--17). Their proven uniform families are at or below the diagonal \(g=2f\); they do not state a proof for every \(f\ge8\) on the fourth off-diagonal \(g=2f+4\). Published adjacent-family results prove the first, second, and third off-diagonals \(g=2f+1,2f+2,2f+3\), respectively, but their conclusions do not imply the fourth. The present explicit component decomposition and all-parameter affine-endpoint proof treat a different infinite family. Earlier finite testing and conjectural length predictions are acknowledged and not presented as novel.

## Limitations
Only the family \(f\ge8\), \(g=2f+4\) is covered; smaller parameters have other initial behavior, and arbitrary greedy 2-sumfree sequences are not classified. The proof of infinite periodicity invokes the previously published four-block continuation theorem rather than reproducing its full proof. The affine certificate is reproducible ordinary integer code, not an independently checked formal proof. An independently verified literature-priority assessment has not been performed; a more general unindexed result could subsume this specialization.

## References
1. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1 (2026-09-16), Sections 1--5, particularly Theorem 15.
2. D. van Berkel and W. Bosma, *On \(t\)-sumfree sequences*, arXiv:2609.16843 (2026-09-15), for the earlier confirmed diagonal-range results, as cited in reference 1.
3. *Exact periodicity of the first two off-diagonal greedy 2-sumfree families*, publicly indexed mathematical research finding (2026-09-20), adjacent cases only.
4. *Exact periodicity of the third off-diagonal greedy 2-sumfree family*, publicly indexed mathematical research finding (2026-10-04), adjacent case only.
