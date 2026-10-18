# Exponential multiplicity of prescribed odd divisor imbalances on a three-prime ray

## Finding
For an odd integer \(k\) and a positive integer \(n\), let
\[
R_n(k)=\#\bigl\{\varepsilon:D(n)\longrightarrow\{-1,1\}:\ \sum_{d\mid n}\varepsilon(d)d=k\bigr\},
\]
where \(D(n)\) is the set of positive divisors. Thus \(R_n(k)\) counts ordered two-block divisor partitions with signed sum difference \(k\); for \(k>0\), each unordered partition whose difference has absolute value \(k\) is counted exactly once.

For every integer \(a\ge1\), set
\[
n_a=3^2\cdot5^2\cdot7^{2a}=225\cdot49^a,\qquad
L_a=3218\frac{49^a-1}{48},\qquad
K_a=47\cdot49^a+L_a=\frac{5474\cdot49^a-3218}{48}.
\]
Then the following hold.

**Uniform multiplicity:** for all integers \(a\ge b\ge1\) and every odd integer \(k\) with \(|k|\le K_b\),
\[
\boxed{R_{n_a}(k)\ge12^{a-b}.}
\]
Consequently, for every fixed odd \(k\) there is an explicitly computable \(b=b(k)\) such that for every \(a\ge b\),
\[
R_{n_a}(k)\ge12^{a-b}\gg_k n_a^{\log 12/\log49}.
\]
The family has exactly three distinct prime divisors for every \(a\). This support size is the smallest on which a fixed positive odd imbalance can occur for infinitely many different odd integers: with at most two distinct prime factors, every signed divisor imbalance has magnitude greater than \(n/8\).

The lower bound counts representations rather than merely proving existence. Neither an exact formula for \(R_{n_a}(k)\) nor optimality of the base \(12\) is asserted.

## Assumptions and scope
All primes, exponents, divisors, and partitions are integral. In a signed partition every positive divisor occurs once, with either sign. The target \(k\) is odd; indeed \(\sigma(n_a)\) is odd, so a signed sum of its divisors is necessarily odd. A negative signed sum is permitted only for the symmetric counting formulation; usual prescribed positive differences correspond to \(k>0\).

Let
\[
B=3^2\cdot5^2=225,\quad D(B)=\{1,3,5,9,15,25,45,75,225\},\quad \sigma(B)=403,
\]
and define its signed-sum multiset by
\[
C(s)=\#\{\varepsilon\in\{-1,1\}^{D(B)}:\sum_{d\mid B}\varepsilon(d)d=s\}.
\]
Every divisor of \(n_a\) is uniquely \(7^j d\), where \(d\mid B\) and \(0\le j\le2a\); this separation into disjoint levels underlies the proof.

## Proof
**1. A complete two-level interval.** Form the union of the two disjoint lists \(D(B)\) and \(7D(B)\). In increasing order its 18 elements are
\[
1,3,5,7,9,15,21,25,35,45,63,75,105,175,225,315,525,1575.
\]
Their sum is \(3224\). The subset sums of the first four weights \(1,3,5,7\) include every integer from \(3\) through \(13\). Suppose the weights already processed sum to \(W\) and have every subset sum in \([3,W-3]\). Adjoining a weight \(c\) supplies both \([3,W-3]\) and \([c+3,c+W-3]\); these integer intervals meet or are adjacent whenever \(c\le W-5\). For each of the remaining fourteen listed weights this inequality holds, beginning with \(9\le16-5\) and ending with \(1575\le1649-5\). Induction shows that every subset sum from \(3\) through \(3221\) exists. Replacing a chosen subset \(S\) by positive signs on \(S\) and negative signs elsewhere yields \(2\sum S-3224\). Therefore the signed sums of \(D(B)\sqcup7D(B)\) contain **every even integer** in \([-3218,3218]\).

**2. A top-level odd offset.** Choosing sign \(+\) for \(225\) and sign \(-\) for all eight other divisors of \(B\) gives
\[
225-(403-225)=47.
\]
Negating all signs gives \(-47\). Thus the top level \(7^{2a}D(B)\) supplies either \(+47\cdot49^a\) or \(-47\cdot49^a\).

**3. Uniform existence through every exponent.** Group the lower \(2a\) levels into \(a\) disjoint two-level blocks. By step 1 their aggregate signed sums include every even integer in \([-L_a,L_a]\), where \(L_a=3218(49^a-1)/48\). Indeed, if this holds for \(a\), the next two-level block contributes every even multiple \(49^a t\), \(|t|\le3218\), and the resulting intervals of allowed even sums are adjacent or overlapping because \(L_a\ge49^a-1\). The case \(a=1\) is step 1. Adding the two top-level choices of step 2 gives two intervals of odd numbers. They overlap on the odd lattice since
\[
L_a\ge47\cdot49^a-1\qquad(a\ge1).
\]
Their union therefore contains every odd integer in \([-K_a,K_a]\). In particular, \(R_{n_a}(k)\ge1\) for every such \(k\).

**4. Exactly twelve independently reusable zero blocks.** A two-level signed block has total zero precisely when its two signed \(B\)-sums \(s,t\) satisfy \(s+7t=0\). The integer coefficients \(C(s)\) are computed exactly by the exhaustive nine-step recurrence
\[
C_0(u)=\mathbf 1_{\{u=0\}},\qquad
C_i(u)=C_{i-1}(u-d_i)+C_{i-1}(u+d_i),
\]
using the nine displayed \(d_i\in D(B)\). The only values \(s\) for which both \(C(s)\) and \(C(-s/7)\) are positive are
\[
 s\in\{\pm329,\pm343,\pm371,\pm385\}.
\]
For either sign, the four corresponding coefficient pairs \((C(s),C(-s/7))\) are \((1,1),(2,1),(1,1),(2,1)\), respectively. The recurrence is finite and exhaustive; it gives
\[
\boxed{\sum_s C(s)C(-s/7)=2(1+2+1+2)=12,}
\]
with the convention that \(C(x)=0\) for nonintegral \(x\). Equivalently, the constant term of
\[
\prod_{d\mid B}(z^d+z^{-d})(z^{7d}+z^{-7d})
\]
is exactly \(12\). These are 12 distinct signed assignments of the 18 divisors in the two levels.

**5. Multiplicity amplification.** Fix \(a\ge b\ge1\) and odd \(k\) with \(|k|\le K_b\). Step 3 gives a signed assignment at every level \(0\le j\le2b\) summing to \(k\). For each \(h=b,b+1,\ldots,a-1\), assign the new two levels \(j=2h+1,2h+2\) one of the 12 zero-sum configurations in step 4, scaled by \(7^{2h+1}\). The new contribution is zero, and the blocks use distinct divisors, so the choices are independent and injective. This gives \(12^{a-b}\) distinct partitions of \(D(n_a)\) with signed difference \(k\). Since \(K_b\) tends to infinity, each fixed odd \(k\) eventually meets the hypothesis. The polynomial-in-\(n_a\) form follows from \(n_a=225\cdot49^a\).

**6. Minimal distinct-prime support.** If odd \(n>1\) has at most two distinct prime factors, then
\[
\frac{\sigma(n)}n<\frac32\frac54=\frac{15}{8}.
\]
Whichever divisor block contains \(n\) has sum at least \(n\), while its complement has sum at most \(\sigma(n)-n\). Every resulting absolute imbalance is therefore at least \(2n-\sigma(n)>n/8\). For fixed positive \(k\), only \(n<8k\) can have absolute imbalance \(k\) with one or two distinct prime factors. The three-prime ray above has infinitely many members, proving minimality.

## Verification
The accompanying standalone `verify.py` checks the full nine-step signed-sum coefficient recurrence, identifies all eight nonzero zero-block coefficient pairs, independently verifies that their total is exactly 12, checks all fourteen subset-sum interval inequalities, and tests the full two-level even interval and base odd interval. It separately constructs every positive divisor of \(n_1\) and \(n_2\), uses an exact integer subset-sum bitset, and verifies every odd \(k\) in the theorem's claimed interval for those two cases. Running `python3 verify.py` prints `VERIFY_OK`. The finite checker certifies the small combinatorial base calculation; induction and prime-factor inequalities, not experiments, establish the infinite claims.

## Relationship to prior work
Kalita and Saikia (2026) develop several divisor-partition generalizations and explicitly classify their primary subject as MSC 11A25. Their paper treats exponential-divisor and even-divisor variants, not the cardinality of signed ordinary-divisor partitions at fixed nonzero imbalance. Li (2026) defines \(k\)-IGMO numbers and proves infinitude of odd examples for each fixed \(k\). The present theorem concerns quantitatively many distinct partitions for one explicit three-prime ray, not the bare existence statement.

Stewart's classical theory of almost practical numbers, and a recent published classification of odd three-prime-support almost practical numbers, already imply **existence** of most prescribed odd imbalances for \(225\cdot49^a\). Hence the interval coverage and three-prime examples are not asserted as independently new discoveries. The specifically assessed advance is the exact 12-way zero-block structure and the uniform exponential lower bound for every prescribed fixed odd difference, using minimal distinct-prime support. Earlier published exact partition counts for even two-prime Zumkeller families treat different divisor sets and zero imbalance and do not imply this three-prime positive-imbalance bound.

## Limitations
The bound \(12^{a-b}\) is a lower bound and may be far below the true partition count; no exact multiplicity asymptotic is proved. The originality of its explicit 12-way transfer remains contingent on the completeness of searchable literature. The full text of Li's 2026 preprint was not accessible in this review; its accessible abstract describes infinitude rather than multiplicity, but an implicit count in the uninspected body cannot be excluded. The proof of the classical almost-practical criterion is not reproduced because no such theorem is needed for correctness, only for proper attribution of the already-covered existence comparison.

## References
1. J. Kalita and H. K. Saikia, *A note on generalized Zumkeller numbers*, Notes on Number Theory and Discrete Mathematics 32 (2026), 150–161, DOI 10.7546/nntdm.2026.32.1.150-161, online first 2026-03-06, MSC 11A25. https://nntdm.net/papers/nntdm-32/NNTDM-32-1-150-161.pdf
2. T. H. S. Li, *On a Generalization of Zumkeller Numbers: Infinitude of odd k-IGMO numbers for all non-negative integers k*, arXiv:2608.13890, first public 2026-08-14. https://arxiv.org/abs/2608.13890
3. B. M. Stewart, *Sums of Distinct Divisors*, American Journal of Mathematics 76 (1954), 779–785, DOI 10.2307/2372651.
4. F. Jokar, *On k-layered numbers*, arXiv:2207.09053 (2022), §3 (restatement of Stewart's criterion).
5. *Three-prime-support classification of odd almost practical numbers*, published mathematical note (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-three-prime-support-classification-of-odd-almost-practical-numbe--4d74b378e55d
6. *Exact Zumkeller partition multiplicity in the upper two-prime strip*, published mathematical note (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-zumkeller-partition-multiplicity-in-the-upper-two-prime-st--dee79b1d7481
