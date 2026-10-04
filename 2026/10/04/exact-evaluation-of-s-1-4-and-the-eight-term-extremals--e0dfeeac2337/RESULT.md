# Exact evaluation of \(s_1(4)\) and the eight-term extremals
## Finding
Let \(s_1(n)\) denote the least positive integer \(k\) such that every sequence of \(k\) integers not divisible by \(n\) contains a subset of exactly \(n\) terms whose sum is divisible by \(n\) but not by \(n^2\). Then
\[
s_1(4)=9.
\]
Among multisets of eight allowed residues modulo \(16\), exactly \(160\) have no four-term witness. Under \(x\mapsto ux+4c\pmod{16}\), with \(u\) odd and \(c\in\mathbb Z/4\mathbb Z\), they form seven orbits, represented by
\[
(1,1,1,2,2,2,10,13),\ (1,1,1,2,2,6,6,13),\ (1,1,1,2,6,7,7,7),
\]
\[
(1,1,1,2,6,10,13,14),\ (1,1,2,2,2,5,9,10),\ (1,1,2,2,5,6,6,9),\ (1,1,2,5,6,9,10,14).
\]

## Assumptions and scope
Only the one-dimensional constant \(s_1(4)\) is considered. Repetitions are allowed. A witness must use exactly four terms. The property depends only on residues modulo \(16\).

## Proof
The admissible residues are
\[
A=\{1,2,3,5,6,7,9,10,11,13,14,15\}.
\]
A four-term submultiset is a witness exactly when its sum modulo \(16\) is in \(\{4,8,12\}\).

The length-eight multiset \((1,1,1,2,2,2,10,13)\) has four-term sums only in \(\{0,1,2,3,5,6,7,9,10,11,13,14,15\}\pmod{16}\), so \(s_1(4)\ge9\).

Permutation is irrelevant, so for the upper bound it suffices to enumerate nondecreasing multisets. There are \(\binom{20}{9}=167960\) length-nine multisets on \(A\); exact enumeration finds a witness in every one, proving \(s_1(4)\le9\).

Likewise, among the \(\binom{19}{8}=75582\) length-eight multisets, exactly \(160\) are witness-free. The stated affine maps preserve admissibility and the witness condition because a four-term sum \(S\) becomes \(uS+16c\), while odd multiplication permutes \(\{4,8,12\}\) modulo \(16\). Their orbit sizes are \(32,32,16,8,32,32,8\), totaling \(160\), with the displayed representatives.

## Verification
`verify.py` checks every length-eight and length-nine multiset twice: by direct enumeration of four positions and by an independent subset-size/residue dynamic program. The methods agree everywhere. The verifier then reconstructs all affine orbits and checks that they cover precisely the \(160\) extremals.

## Relationship to prior work
Gao, Jiang, Lei, Lin, and Yang introduced the prime-modulus precursor \(\mathsf{s}_p^*\), conjectured \(\mathsf{s}_p^*=2p+1\) for odd primes, and proved \(\mathsf{s}_p^*\le3p-2\); their paper has primary MSC 11B30. Sun subsequently defined \(s_1(n)\) for general \(n\), proved \(2n+1\le s_1(n)\le n^2-2n+2\) for \(n\ge4\), and conjectured equality. Thus his stated bounds leave \(9\le s_1(4)\le10\). The present result closes that one-unit gap and classifies every sharp length-eight obstruction.

A later local zero-sum theorem permits some or at most \(n\) selected terms, so it does not imply the exact-\(n\) assertion here. Targeted searches for the exact equality, the equivalent modulo-\(16\) formulation, and the extremal classification found no matching published statement.

## Limitations
This is a finite exact classification for \(n=4\), not a proof of the general conjecture. Direct full-manuscript inspection of the Sun preprint was unavailable; comparison used its indexed abstract and a detailed theorem-level public summary. An unindexed internal small-case computation therefore remains a residual bibliographic risk.

## References
1. W. Gao, X. Jiang, W. Lei, C. Lin, W. Yang, “A new problem from zero-sum theory”, *Acta Arithmetica* 224 (2026), 71–79, DOI 10.4064/aa251115-21-1.
2. Z.-W. Sun, “On zero-sum problems of two new types” / “On zero-sum problems of new types”, arXiv:2606.18234, first public 2026-06-16.
3. W. Gao, X. Jiang, Y. Mu, “Two local zero-sum problems”, arXiv:2607.11313 (2026).
