# The first nontrivial odd-prime case of the exact local zero-sum conjecture: \(s_1(5)=11\)

## Finding
For \(n>1\), write \(s_1(n)\) for the smallest integer \(k\) with the following property: every sequence of \(k\) integers not divisible by \(n\) contains **exactly** \(n\) terms whose sum is divisible by \(n\) and not divisible by \(n^2\). Repeated terms are allowed. Then
\[
\boxed{s_1(5)=11.}
\]
Equivalently, the original odd-prime constant of Gao, Jiang, Lei, Lin and Yang has \(\mathsf{s}^{*}_5=11\).

In addition, there are exactly \(3900\) nondecreasing, ten-term residue multisets modulo \(25\), with no term divisible by \(5\), that avoid the required five-term subset. For example,
\[
(1,1,1,1,2,2,2,2,17,21)
\]
is one such multiset.

## Assumptions and scope
The problem is one-dimensional and unrestricted in the magnitudes and signs of the integer terms. Terms are selected by their **positions**, so repetitions count separately. Since both divisibility conditions only depend on residues modulo \(25\), work with the twenty-element allowed residue set
\[
R=\{1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24\}
\]
and the target set \(T=\{5,10,15,20\}\subset\mathbb Z/25\mathbb Z\). The sum of five admissible terms is divisible by \(5\) but not by \(25\) if and only if its residue lies in \(T\).

The result is an **exhaustive finite theorem** for the fixed prime \(5\), not a claim for all primes.

## Proof
**Exact state recurrence.** For each finite ordered multiset prefix \(A=(a_1,\ldots,a_m)\), let \(S_j(A)\subseteq\mathbb Z/25\mathbb Z\), for \(0\le j\le5\), be the set of residues of sums of exactly \(j\) distinct positions of \(A\). Thus \(S_0=\{0\}\) and initially \(S_1=\cdots=S_5=\varnothing\). If a new term \(r\) is appended, direct partition of subsets according to whether they use that position gives the identity
\[
S_j(A\mathbin\Vert r)=S_j(A)\cup\bigl(r+S_{j-1}(A)\bigr)\pmod{25},\quad1\le j\le5,
\]
where all right-hand side states refer to \(A\), and the zeroth state remains \(\{0\}\). This is an identity of finite sets, including when \(r\) repeats an earlier residue.

**Complete traversal and pruning.** Every multiset of allowed residues has a unique nondecreasing order in \(R\). Starting from the empty multiset, recursively append a residue whose index is at least the previously appended index. Retain a child state if and only if \(S_5\cap T=\varnothing\). If a prefix already has a five-term target subset, every extension retains that subset. Thus pruning can never discard a longer witness-free multiset. This proves by induction that the traversal enumerates **all** witness-free multisets at each depth, once each, with no omitted multiplicity patterns.

Two standalone implementations use independently encoded exact state updates: the first represents \(S_j\) by a 25-bit cyclic bitset, and the second by Python sets of residues. Both traverse the entire finite search tree through depth \(11\) and give the same counts, in order of depths \(0,1,\ldots,11\):
\[
(1,20,210,1540,8855,35700,78700,89100,58350,21600,3900,0).
\]
In particular, the last count is exactly **zero**, so no witness-free eleven-term multiset exists. As each sequence can be sorted without changing the existence of a five-position subset, every eleven-term sequence contains the desired subset; hence \(s_1(5)\le11\).

For the opposite inequality, direct application of the recurrence (or enumeration of the \(\binom{10}{5}=252\) five-position subsets) to the displayed ten-term multiset shows \(S_5\cap T=\varnothing\). Consequently \(s_1(5)>10\). Combining the inequalities yields \(s_1(5)=11\). \(\square\)

## Verification
All evidence necessary to reproduce the finite proof is embedded: `artifacts/verify.cpp` and `artifacts/verify.py`, plus `artifacts/replay.txt` containing an actual run of each. For the C++ implementation run `g++ -std=c++17 -O2 artifacts/verify.cpp -o verify && ./verify`. Run `python3 artifacts/verify.py` for the independent set-based implementation. Both check the complete count vector and exhibit the same avoiding ten-term multiset. The proof of exhaustive coverage is the state recurrence and prefix-pruning invariant, not a probabilistic sample or an extrapolation from bounded integers.

## Relationship to prior work
Gao, Jiang, Lei, Lin and Yang [1] defined the prime constant \(\mathsf{s}^{*}_p\), conjectured \(\mathsf{s}^{*}_p=2p+1\) for all odd primes, and established the bound \(\mathsf{s}^{*}_p\le3p-2\). For \(p=5\), this establishes an upper bound of \(13\), which does not itself imply the equality \(11\). Sun [2] defined the composite-modulus version \(s_1(n)\), proved \(2n+1\le s_1(n)\le n^2-2n+2\) for \(n\ge4\), and explicitly conjectured \(s_1(n)=2n+1\). Our result confirms that conjecture for \(n=5\), the first odd-prime case where the available bound \(3p-2\) is strictly weaker than \(2p+1\).

A published finite classification for \(s_1(4)\), with \(160\) witness-free eight-term multisets, concerns a different modulus and does not imply this prime-five case [3]. Gao, Jiang and Mu [4] prove local zero-sum theorems allowing **some** or **at most** \(n\) selected positions; those flexible-cardinality theorems do not imply the exact-five-term statement here.

## Limitations
The conclusion addresses the single prime \(5\). It does not establish the conjecture for primes \(p\ge7\) or composite moduli other than \(5\). Literature searches and the accessible primary abstracts revealed no covering prior theorem, but the complete manuscripts of [1] and [2] were not inspectable; an unpublished or unindexed earlier computation of this specific finite case remains a bibliographic risk. The exhaustive computational certificate is fully reproducible but has not undergone independent external audit.

## References
[1] W. Gao, X. Jiang, W. Lei, C. Lin, W. Yang, “A new problem from zero-sum theory,” *Acta Arithmetica* 224 (2026), 71–79, DOI 10.4064/aa251115-21-1; first verified public online date 31 May 2026; primary MSC 11B30. https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/224/1/116456/a-new-problem-from-zero-sum-theory

[2] Z.-W. Sun, “On zero-sum problems of two new types,” arXiv:2606.18234, first public 16 June 2026. https://arxiv.org/abs/2606.18234

[3] “Exact evaluation of \(s_1(4)\) and the eight-term extremals,” public mathematical record e0dfeeac2337, 2026.

[4] W. Gao, X. Jiang, Y. Mu, “Two local zero-sum problems,” arXiv:2607.11313 (2026). https://arxiv.org/abs/2607.11313
