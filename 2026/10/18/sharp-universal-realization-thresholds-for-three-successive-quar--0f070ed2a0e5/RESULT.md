# Sharp universal realization thresholds for three successive quartic-residue cosets

## Finding

Fix a prime \(p\equiv1\pmod4\) and a primitive root \(g\) modulo \(p\). For nonzero \(y\pmod p\), define the quartic-coset label \(c_p(y)\in\mathbb Z/4\mathbb Z\) by \(c_p(g^a)=a\pmod4\). Define the set of three-consecutive-label words
\[
W_p=\{(c_p(x),c_p(x+1),c_p(x+2)):1\le x\le p-3\}.
\]
All \(4^3=64\) words occur **if and only if** \(p\) is not among the following 38 primes:
\[
\begin{gathered}
5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,157,173,193,197,\\
233,241,257,277,281,293,313,337,353,401,409,433,457,509,521,569,709,881,1153.
\end{gathered}
\]
In particular all 64 patterns occur for every eligible prime \(p\ge1181\), and that sharp universal threshold is preceded by the failure at \(p=1153\). At \(p=1153\), the **only** missing word is \((0,0,0)\). There is a distinct earlier threshold for the 63 other words: each of them occurs for every eligible prime \(p\ge733\), but the preceding eligible prime \(p=709\) misses nonzero words.

## Assumptions and scope

Primes are rational primes congruent to one modulo four. Indices \(x\) are ordinary integers in \(1\le x\le p-3\), so each of \(x,x+1,x+2\) is nonzero modulo \(p\). The class \(0\) consists of fourth powers, and the other classes are the three multiplicative cosets of the fourth-power subgroup. Replacing the primitive root by another multiplies **every** class label by \(1\) or \(3\) modulo four; consequently, the assertions about realization of all words, about the zero word, and about all 63 nonzero words do not depend on the chosen primitive root.

## Proof

Let \(\chi\) be the quartic character satisfying \(\chi(g)=i\) on \(\mathbb F_p^\times\). All four characters \(\chi^r\), including \(\chi^0\), are extended to take value zero at zero. For \(e=(e_0,e_1,e_2)\in(\mathbb Z/4\mathbb Z)^3\), let \(N_p(e)\) count the integers \(1\le x\le p-3\) with \(c_p(x+j)=e_j\) for \(j=0,1,2\). Character orthogonality gives the exact identity
\[
64N_p(e)=\sum_{x\in\mathbb F_p}\prod_{j=0}^2
\left(\sum_{r=0}^3 i^{-e_jr}\chi^r(x+j)\right).
\]
The term in which all three exponents are zero contributes \(p-3\). There are nine terms with exactly one nonzero exponent. The complete character sum over \(\mathbb F_p\) of a nontrivial character of a shifted linear polynomial vanishes; excluding the other two forbidden roots changes that sum by at most two, so each such term has absolute value at most two.

There are 27 terms with exactly two nonzero exponents. For these, the Weil bound for a nontrivial multiplicative character evaluated on a polynomial with two distinct roots gives a complete-sum bound of \(\sqrt p\); excluding the remaining forbidden root changes it by at most one. Thus each is bounded by \(\sqrt p+1\). There are another 27 terms with three nonzero exponents. Their polynomial has three distinct roots, every root exponent lies in \(\{1,2,3\}\), and the polynomial cannot be a fourth power. The corresponding complete-sum Weil bound is \(2\sqrt p\). Taking absolute values proves, uniformly in \(e\),
\[
64N_p(e)\ge(p-3)-9\cdot2-27(\sqrt p+1)-27(2\sqrt p)
=p-81\sqrt p-48.
\]
For all real \(p\ge6724=82^2\), this last expression is positive (it equals 34 at 6724 and is increasing thereafter). Therefore every word occurs for every eligible prime at least 6724.

It remains to classify eligible primes below 6724, **not** to extrapolate from a sample. The standalone `verify.py` builds an exact sieve for all integers below 6724, finds a primitive root using the prime factors of \(p-1\), enumerates each of the \(p-1\) nonzero residue classes in primitive-root order, and counts the words over every \(1\le x\le p-3\). It also independently reconstructs each label using \(x^{(p-1)/4}\pmod p\) and the four powers of \(g^{(p-1)/4}\). The algorithm examines **all** 427 eligible primes in this finite interval and verifies that precisely the 38 primes displayed above lack some word. It verifies that the last prime with any missing nonzero word is 709, the last prime with any missing word is 1153, and at 1153 only the zero word is absent. This exhausts the finite range, proving every assertion.

## Verification

Execute `python3 verify.py` with standard-library Python 3. The program has no imports from external packages and no data dependencies. Its exact outputs begin `VERIFY_OK`, include the figures 427, 38, 709, and 1153, and confirm both universal thresholds. The infinite range \(p\ge6724\) follows from the displayed character-sum inequality, not from computation. Finite computation establishes only the explicitly bounded exceptional range, where it is exhaustive.

## Relationship to prior work

Brauer's existence theorem and the classical work of Bierstedt–Mills and Jordan concern consecutive power residues, or consecutive elements of the **same** power-residue coset; they do not classify realization of all ordered triples of four distinct coset labels. Dietzel's 2013 paper establishes the existence of bounded consecutive power-residue **pairs** by a Ramsey-theoretic method; it neither gives these sharp prime thresholds nor the all-64 three-term distribution. Lehmer's 1983 work studies least occurrences and delays of prescribed power-residue patterns; its full text was unavailable for complete exclusion of a stronger implication, a residual priority risk. Su–Zhang (2020) count special quartic configurations involving inverses, rather than the triples \((x,x+1,x+2)\). The standard Weil bound is used as an existing theorem, not claimed as new. A known cubic-coset triple classification does not logically imply the quartic one; the exceptional sets and sharp thresholds require a separate complete calculation.

## Limitations

The theorem asserts occurrence/nonoccurrence of words, not explicit exact counts of every word at each prime, nor a least positive starting index realizing any fixed word. Its finite certificate must be run to establish the precise exception list; the analytic estimate alone is too coarse for the range below 6724. An earlier unindexed sharp quartic triple classification or a stronger published result might imply the statement. No independent audit has been performed.

## References

1. C. Dietzel, *A generalization of Schur's theorem and its application to consecutive power residues*, arXiv:1309.7506v1, submitted 28 September 2013. https://arxiv.org/abs/1309.7506
2. R. G. Bierstedt and W. H. Mills, *On the bound for a pair of consecutive quartic residues of a prime*, Proc. Amer. Math. Soc. 14 (1963), 628–632. https://www.cs.umd.edu/~gasarch/TOPICS/res/resbiemills.pdf
3. J. H. Jordan, *Pairs of consecutive power residues or non-residues*, Canad. J. Math. 16 (1964), 310–314. https://doi.org/10.4153/CJM-1964-030-6
4. E. Lehmer, *Patterns of power residues*, J. Number Theory 17 (1983), 37–46. https://doi.org/10.1016/0022-314X(83)90004-5
5. J. Su and J. Zhang, *On the Quartic Residues and Their New Distribution Properties*, Mathematics 8 (2020), 1337. https://doi.org/10.3390/math8081337
