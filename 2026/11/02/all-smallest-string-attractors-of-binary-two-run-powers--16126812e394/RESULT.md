# All smallest string attractors of binary two-run powers

## Finding
For positive integers \(a,b\) and \(k\ge2\), let
\[
W_{a,b,k}=(0^a1^b)^k,\qquad p=a+b,\qquad N=kp.
\]
Positions are numbered from \(1\) to \(N\). A *string attractor* is a subset of positions such that every nonempty contiguous factor has an occurrence intersecting this subset. Every \(W_{a,b,k}\) has minimum attractor cardinality exactly two. A pair is an attractor **if and only if** its two positions collectively intersect an occurrence of each of the four factors \(0\), \(1\), \(01\), and \(10\). Thus these four short factors certify full factor coverage for a pair in this family.

The exact number of smallest attractors is
\[
\mathcal A(a,b,k)=
\begin{cases}
(k-1)(k\max(a,b)+1),&\min(a,b)=1,\\
2k(k-1),&a,b\ge2.
\end{cases}
\]
In particular, for positive run lengths at least two, the count depends only on the number of repetitions, not the run lengths.

When \(a,b\ge2\), every smallest attractor belongs to exactly one of two disjoint families: (I) the last \(0\) in any zero-run together with the last \(1\) in any nonterminal one-run; or (II) the first \(1\) in any one-run together with the first \(0\) in any noninitial zero-run. Both families contain \(k(k-1)\) pairs. If \(H_{a,b,k}(z)\) counts smallest attractors by absolute distance between the selected positions, then
\[
H_{a,b,k}(z)=2\sum_{m=2-k}^{k-1}c_{k,m}z^{\lvert mp-a\rvert},\quad
c_{k,m}=\begin{cases}k-1+m,&m\le0,\\k-m,&m\ge1.\end{cases}
\]
The least and greatest distances occurring among smallest attractors are exactly \(\min(a,b)\) and \((k-1)(a+b)-\min(a,b)\).

## Assumptions and scope
The alphabet consists of two different labeled symbols \(0,1\). The parameters \(a,b\) are arbitrary positive integers, and \(k\ge2\). Factors are nonempty contiguous substrings of the finite *linear* word, not cyclic factors or scattered subsequences. The attractor intersects at least one full occurrence interval of each distinct factor. The polynomial \(H\) counts unordered two-element position sets once each. The result does not concern general periods with more than two runs, nor all binary words. The alternating subcase \(a=b=1\) has been enumerated previously; the new contribution is the uniform four-factor characterization and classification over all positive run lengths, including the phase distinction for run lengths at least two.

## Proof
**Minimum size and necessity of the four tests.** Both symbols occur, and a one-position set cannot intersect occurrences of both length-one factors. Thus any attractor has size at least two. A two-element attractor must contain one \(0\)-position and one \(1\)-position and must hit an occurrence of each length-two factor \(01\) and \(10\). The internal \(10\) occurrence boundaries are precisely between positions \(jp\) and \(jp+1\), for \(1\le j\le k-1\). Therefore a two-position set passing the four tests contains a marked position at one of those internal boundaries.

**Sufficiency for long factors.** Consider any factor \(f\) of length \(L\ge p\). All of its occurrence starts are congruent modulo \(p\), since the infinite periodic parent has the specified period (a smaller fundamental period would not affect the argument). Let \(s\) be the earliest start and \(t\) the latest occurrence end. Periodicity gives \(s\le p\) (otherwise shift the earliest occurrence left by one period) and \(t\ge N-p+1\) (otherwise shift the last occurrence right by one period). The successive occurrence intervals under shifts of \(p\) overlap or abut because \(L\ge p\). Their union therefore includes the entire positional interval \([p,N-p+1]\). In particular it contains both positions at every internal \(10\) boundary (the boundary at \(p,p+1\) and the boundary at \((k-1)p,(k-1)p+1\) are included). The marked internal-boundary position thus attracts every long factor.

**Sufficiency for short factors.** Suppose \(1\le L<p\). A pure-symbol factor \(0^u\) or \(1^v\) has length at most the corresponding full run length, and can be realized through the selected position of that symbol within its run: slide the length-\(u\) or length-\(v\) occurrence within the run until it covers the selected position. Any mixed factor containing \(10\) occurs around each internal \(10\) boundary, because its length is shorter than the period and the entire period-local context on either side of every such boundary is identical; hence an occurrence intersects the selected internal-boundary position. A mixed factor containing no \(10\) must be of the form \(0^u1^v\) with positive \(u,v\); it occurs around each \(01\) boundary and thus intersects the selected position witnessing the \(01\) test. These exhaust the possibilities and establish the four-factor certificate.

**Counting and classification.** Let \(Z\) be all zero positions, \(O\) all one positions, \(Z_L\) the \(k\) last-zero positions, \(Z_F\) the \(k-1\) first-zero positions of noninitial zero-runs, \(O_F\) the \(k\) first-one positions, and \(O_L\) the \(k-1\) last-one positions of nonterminal one-runs. With one selected position from each symbol, the \(01\) test says \(z\in Z_L\) or \(o\in O_F\); the \(10\) test says \(z\in Z_F\) or \(o\in O_L\). If \(a,b\ge2\), then \(Z_L\cap Z_F=\varnothing\) and \(O_F\cap O_L=\varnothing\), forcing either \((z,o)\in Z_L\times O_L\) or \((z,o)\in Z_F\times O_F\). These families are disjoint, and each has \(k(k-1)\) members. If \(a=1\), then \(Z_L=Z\) and \(Z_F\subset Z\). The eligible pairs are \(Z_F\times O\) or \(Z\times O_L\), with intersection \(Z_F\times O_L\), yielding \((k-1)bk+k(k-1)-(k-1)^2=(k-1)(bk+1)\). The case \(b=1\) follows by swapping zero and one and reversing the word, yielding \((k-1)(ak+1)\); the two cases agree when \(a=b=1\). At least one candidate pair exists in every case, so minimum size is exactly two.

**Distance enumerator for \(a,b\ge2\).** The two disjoint pair families give identical distance multisets: for instance the first family has positions \((i-1)p+a\) and \(jp\) with \(1\le i\le k\), \(1\le j\le k-1\). Putting \(m=j-i+1\) produces distance \(\lvert mp-a\rvert\); the multiplicity of this integer parameter is \(k-1+m\) when \(m\le0\) and \(k-m\) when \(m\ge1\). The other family yields the same distribution. The shortest distance is achieved for \(m=0\) or \(m=1\), giving \(\min(a,b)\), while the largest is achieved at an endpoint of the range \([2-k,k-1]\), giving \((k-1)p-\min(a,b)\). This proves the announced polynomial and extrema.

## Verification
The accompanying standalone Python 3 program `verify.py` enumerates every distinct factor of the finite word, constructs exact occurrence-coverage bit masks, and checks every unordered two-position set against the complete definition, independently of the four-factor criterion. For all \(a,b\in\{1,2,3,4,5\}\) and \(k\in\{2,3,4,5\}\), it agrees with the stated criterion and cardinality; for \(a,b\ge2\) it also checks every coefficient of the gap enumerator. A separate routine checks occurrences literally, without substring-mask reuse, for \(a,b\in\{1,2,3\}\) and \(k\in\{2,3,4\}\). Recorded successful output: `VERIFY_OK parameter_cases=100 masked_pair_tests=25950 direct_pair_tests=2100 span_spectra=True`. The infinite family is proved by the preceding argument, not by the finite experiment.

## Relationship to prior work
Prezza introduced string attractors as a unifying repetitiveness measure; the definitions used here are standard. Mantaci and coauthors studied periodic powers and proved stabilization of the *minimum size* of string attractors under repeated concatenation, a statement that does not enumerate the minimum position sets. Restivo and coauthors studied string attractors in infinite and recurrent words, with a different scope. Dvořáková and Hendrychová analyzed attractors for Rote and generalized pseudostandard sequences. The released note *All smallest attractors in two exceptional antipalindromic pseudostandard families* explicitly proves that \((01)^k\) has \(k^2-1\) smallest pairs, which is the \(a=b=1\) special case here; it also treats the distinct truncated period-four family \(0(1100)^{k-1}1\). These already established results are **not** claimed as new. The present uniform all-parameter four-factor certificate, two-run-power pair classification, independence of the count from both run lengths when at least two, and corresponding distance enumerator are not supplied by those inspected claims.

## Limitations
The classification holds only for finite binary powers of a single two-run block and \(k\ge2\). It neither classifies general periodic words nor gives new bounds on minimum cardinality of attractors in arbitrary strings. The previously published alternating subfamily must not be interpreted as a novel special case. Novelty remains conditional on the scope of inspected literature; an unknown broader optimal-attractor enumeration could imply these formulas. No independent expert audit or external certification is claimed.

## References
1. N. Prezza, “String Attractors,” arXiv:1709.05314, first publicly posted 2017-09-15, https://arxiv.org/abs/1709.05314.
2. S. Mantaci et al., “A combinatorial view on string attractors,” *Theoretical Computer Science* (2021), open author version https://arpi.unipi.it/retrieve/e0d6c92f-ec13-fcf8-e053-d805fe0aa794/MRRRS_TCS2021.pdf (in particular Proposition 15 on powers).
3. A. Restivo et al., “String Attractors and Infinite Words,” arXiv:2206.00376, https://arxiv.org/abs/2206.00376.
4. L. Dvořáková and V. Hendrychová, “String attractors of Rote sequences,” arXiv:2308.00850, https://arxiv.org/abs/2308.00850.
5. “All smallest attractors in two exceptional antipalindromic pseudostandard families,” publicly accessible result https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-smallest-attractors-in-two-exceptional-antipalindromic-pseud--fe2566e0098c.
6. M. Banbara et al., “The Smallest String Attractors of Fibonacci and Period-Doubling Words,” CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.33.
