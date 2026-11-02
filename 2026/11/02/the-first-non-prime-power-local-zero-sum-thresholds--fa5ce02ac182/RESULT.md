# The first non-prime-power local zero-sum thresholds

## Finding

For an integer \(n\ge2\), let \(\mathsf D_n^{\times}\) be the least length \(L\) such that every sequence of \(L\) integers relatively prime to \(n\) contains a nonempty subsequence whose sum \(\sigma\) satisfies \(\gcd(\sigma,n^2)=n\). Let \(\eta_n^{\times}\) be the corresponding least length when the desired subsequence must have at most \(n\) terms. Repeated sequence entries are allowed.

**Theorem.** At the least integer with two distinct prime factors,
\[
\boxed{\mathsf D_6^{\times}=\eta_6^{\times}=13.}
\]
Thus the general lower bound in Gao--Jiang--Mu, Example 6.2, is attained for \(n=6\). The result answers their Problem 6.1 at its first admissible modulus; it does not assert an answer for other composite moduli.

## Assumptions and scope

The entries are arbitrary ordinary integers coprime to \(6\), with multiplicity. A selected subsequence may have any positive length for \(\mathsf D_6^{\times}\), but length from \(1\) through \(6\) for \(\eta_6^{\times}\). The sum criterion depends only on residues modulo \(36\). In that ring the possible entry residues are
\[
U=\{1,5,7,11,13,17,19,23,25,29,31,35\},
\]
and the acceptable sum residues are exactly \(T=\{6,30\}\), since \(\gcd(s,36)=6\) precisely for \(s\equiv6\) or \(30\pmod{36}\).

## Proof

**Lower bound.** Consider the sequence of twelve residue representatives
\[
W=(\underbrace{1,\ldots,1}_{5},\underbrace{35,\ldots,35}_{5},13,23).
\]
All entries are units modulo \(36\). We verify that *no nonempty subsequence of any length* has a sum in \(T\). Writing \(35\equiv-1\) and \(23\equiv-13\pmod{36}\), any subsequence sum takes the form \(d+13e\pmod{36}\), where \(-5\le d\le5\) and \(e\in\{-1,0,1\}\). For \(e=0\), the residues \(6\) and \(30=-6\) are impossible because \(|d|\le5\). For \(e=1\), the equations \(d+13\equiv6,30\pmod{36}\) require \(d\equiv-7,17\pmod{36}\), neither in \([-5,5]\); the case \(e=-1\) is symmetric. Accordingly both thresholds exceed \(12\). This is an explicit specialization of the construction in the source's Example 6.2.

**Reduction for the upper bound.** Multiplication of all entries by any unit \(u\pmod{36}\) preserves the property \(\gcd(\sigma,36)=6\), because \(\gcd(u\sigma,36)=\gcd(\sigma,36)\). Every nonempty sequence of units may therefore be normalized by multiplying by the inverse of one of its entries, so that at least one entry is \(1\). Reorder the resulting multiset nondecreasingly: its first entry is \(1\) because all residue representatives lie in \(U\) and are positive. Hence it suffices to rule out a thirteen-term multiset whose first entry is \(1\).

**Exact finite exhaustion.** For a multiset \(S\) of unit residues define, for each \(0\le j\le6\), the set \(B_j(S)\subseteq\mathbb Z/36\mathbb Z\) of attainable sums of exactly \(j\) entries, with \(B_0(S)=\{0\}\). If a new entry \(x\) is adjoined, the recurrence is
\[
B_j(S\cup\{x\})=B_j(S)\cup\bigl(B_{j-1}(S)+x\bigr),\qquad1\le j\le6.
\]
The old \(B_{j-1}\) must be used on the right. Thus an extension is forbidden as soon as \(B_j\cap T\ne\varnothing\) for any \(1\le j\le6\). Such a forbidden prefix can never become acceptable after adding further entries, since subsequence sums persist.

The included standalone `verify.py` performs a complete recursive enumeration of nondecreasing multisets beginning with \(1\), using exactly this recurrence. At each state it tries *every* next residue at least as large as the last, and prunes only when a forbidden subsequence already exists. There is no prescribed depth cutoff or memoization. Exact Python integer residue sets yield \(3944\) admissible-prefix nodes in total; the numbers at lengths \(1\) through \(12\), respectively, are
\[
1,10,47,141,322,560,638,639,633,566,315,72,
\]
and **there are no admissible prefixes of length \(13\)**. This check is a finite exhaustive proof: every normalized bad thirteen-term multiset would contribute a reachable length-thirteen node, contradicting the exact enumeration. It follows that \(\eta_6^{\times}\le13\). The elementary monotonicity \(\mathsf D_6^{\times}\le\eta_6^{\times}\), together with the explicit twelve-term lower-bound witness, proves the theorem.

## Verification

Run `python3 verify.py` from the directory containing that file. It prints `VERIFY_OK`, the exact admissible-prefix histogram, and two independently valid twelve-term witnesses. The enumerator uses Python's exact finite sets, not floating-point arithmetic or random sampling. It explicitly checks the unit and target residue sets and verifies invariance of \(T\) under multiplication by all units. Its lower-bound witness check evaluates subsequence sums in all lengths \(1\) through \(12\). The enumeration algorithm is completely specified above, making completeness auditable independently of a particular implementation.

An independent unsigned-bit-mask implementation of the same finite recurrence, traversing without memoization, also counted \(3944\) admissible-prefix nodes with maximum depth \(12\). This independent agreement is corroborative; the exhaustive recurrence and its reproducible Python implementation are the stated certificate.

## Relationship to prior work

Gao, Jiang, and Mu, *Two local zero-sum problems*, arXiv:2607.11313v1 (first public date 2026-07-13), introduce the same \(\mathsf D_n^{\times}\) and \(\eta_n^{\times}\), prove their equality to \(2n-1\) for prime powers, and in Problem 6.1 ask for values when \(n\) has at least two prime factors. Their Example 6.2 gives the general lower bound \(2n+2\omega(n)-3\) for such \(n\). The theorem above supplies the previously undetermined matching *upper* bound at \(n=6\); it does not merely restate that example.

Zhi-Wei Sun, *On zero-sum problems of two new types*, arXiv:2606.18234, studies precisely \(n\)-term sums divisible by \(n\) but not \(n^2\); this is a different predicate and a different length restriction. Li, Ling, Sun, and Zhu, *Proofs and disproofs of some conjectures on zero-sum problems of new types*, arXiv:2610.19965, study a related but weaker non-divisibility predicate in vector groups. Neither accessible abstract gives an upper bound for the exact-gcd \(6\), at-most-six-term threshold here. These comparisons do not constitute a proof of novelty against all possible literature.

## Limitations

The result determines only the two exact constants at \(n=6\), not the structure of every twelve-term extremizer and not the general composite case. The upper bound uses an exact, small, complete finite enumeration rather than a hand classification of all bad sequences. An unindexed prior evaluation or a stronger result implying the same value remains a priority risk. There has been no independent scholarly audit of the mathematical claim.

## References

1. Weidong Gao, Xiao Jiang, Yucen Mu, *Two local zero-sum problems*, arXiv:2607.11313v1, 2026-07-13; Theorem 1.4, Problem 6.1, Example 6.2. https://arxiv.org/abs/2607.11313
2. Zhi-Wei Sun, *On zero-sum problems of two new types*, arXiv:2606.18234v1, 2026-06-16. https://arxiv.org/abs/2606.18234
3. Yang Li, San Ling, Zhonghua Sun, Shixin Zhu, *Proofs and disproofs of some conjectures on zero-sum problems of new types*, arXiv:2610.19965v1, 2026-10-14. https://arxiv.org/abs/2610.19965
