# Quadratic-time reconstruction of prime cycles from left-right orbit signatures

## Finding
Let \(p\ge2\) be a prime number and let \(x_1<\cdots<x_p\) be a linearly ordered set. Given a permutation \(f\) that consists of one \(p\)-cycle, form its explicit left-right orbit-signature table
\[
 b_i(t)=\mathbf 1_{\{f^t(x_i)\le x_i\}},\qquad 1\le i\le p,\quad 0\le t<p.
\]
The table determines \(f\), and there is a deterministic \(O(p^2)\)-time reconstruction algorithm using \(O(p)\) auxiliary space when the rows can be streamed. This improves the \(O(p^3)\) reconstruction estimate in Remark 2.4 of Fuhrmann--Gröger--Passeggi for the same table-level inverse problem. Exactly \(p-1\) cyclic binary-word searches, each of length \(p\), suffice.

## Assumptions and scope
Here the points are indexed by their increasing order and the complete signature table is the input; the equality at time zero is known. The number \(p\) is prime, and the unknown permutation is promised to be a single cycle. Time complexity counts operations on indices and bits of length \(O(\log p)\); on a bit-operation model an additional index-arithmetic factor can be required. The statement concerns reconstruction **from known signatures**, not the separate and harder problem of inferring signatures from unlabeled orbit sets of interval maps.

## Proof
Identify cyclic orbit times with \(\mathbb Z/p\mathbb Z\). Define \(a_j\) by \(f^{a_j}(x_1)=x_j\); thus \(a_1=0\), and all \(a_j\) are distinct. Suppose \(a_1,\ldots,a_i\) are known for some \(1\le i<p\). Let \(S_i=\{a_1,\ldots,a_i\}\) and define the length-\(p\) binary word
\[
 A_i(t)=\mathbf 1_{\{t\in S_i\}},\qquad t\in\mathbb Z/p\mathbb Z.
\]
From the row belonging to \(x_{i+1}\), construct \(B_{i+1}\) by replacing its entry at \(t=0\) by zero, leaving all positive-time entries unchanged. Since \(f^t(x_{i+1})=x_j\) exactly when \(t+a_{i+1}=a_j\), and the new point \(x_{i+1}\) is the greatest of \(x_1,\ldots,x_{i+1}\), for every time \(t\) (including zero) we obtain
\[
 B_{i+1}(t)=A_i(t+a_{i+1}\bmod p).
\]
Indeed, at positive times, \(f^t(x_{i+1})\le x_{i+1}\) iff that iterate equals one of \(x_1,\ldots,x_i\); at time zero, \(a_{i+1}\notin S_i\), so both sides are zero.

The cyclic rotation matching \(A_i\) to \(B_{i+1}\) is unique. Were two shifts possible, \(S_i\) would be invariant under a nonzero cyclic translation. As \(p\) is prime, a nonzero element generates \(\mathbb Z/p\mathbb Z\), and the only invariant subsets are empty or full. But \(1\le|S_i|=i<p\). Hence the unique shift is exactly \(a_{i+1}\), and the induction recovers all phases.

For each stage, compute the length-\(p\) indicator word \(A_i\) in \(O(p)\) time and search for the pattern \(B_{i+1}\) in the first \(2p-1\) positions of the periodic word \(A_iA_i\). The standard prefix-function string-matching algorithm finds all matches in \(O(p)\) time and uses \(O(p)\) auxiliary space. By uniqueness exactly one starting position lies in \(\{0,\ldots,p-1\}\), and it is \(a_{i+1}\). Updating \(S_i\) takes constant time using a boolean array. After at most \(p-1\) stages, form the inverse phase array and output the unique image \(f(x_i)=x_j\) satisfying
\[
 a_j\equiv a_i+1\pmod p.
\]
Every stage takes \(O(p)\) time, giving total \(O(p^2)\), and all temporary arrays have length \(O(p)\). The complete input consists of \(p^2\) bits, so the reconstruction time is linear in the length of that explicit representation.

## Verification
The supplied `check_prime_cycles.py` constructs valid signature tables and reconstructs every prime cycle for \(p\in\{2,3,5,7\}\), respectively \(1,2,24,720\) cycles. It additionally reconstructs \(200\) reproducibly seeded random prime cycles at each length in \(\{11,13,17,19,23\}\). The program implements prefix-function matching, not brute-force rotation matching. All checks succeeded. They do not constitute a proof for unbounded prime lengths; the preceding group-action and string-matching argument does.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi, *Period spectrum and rigidity of interval maps* (arXiv:2610.07435v1, first public 5 October 2026), prove uniqueness of a prime cycle from its left-right behavior (Lemma 2.1) and in Remark 2.4 give a reconstruction algorithm with complexity of order \(p^3\). The result here preserves their inverse problem but uses a different representation of successive rows as cyclic translations to obtain an \(O(p^2)\) algorithm. Knuth, Morris and Pratt's classical linear-time pattern matching supplies the standard computational subroutine; it does not address ordered orbit signatures. This is not an independent proof of the interval-map rigidity theorems, which require additional dynamical arguments.

## Limitations
Primality is essential to the uniqueness argument as stated. The algorithm accepts guaranteed realizable signature tables; no characterization of nonrealizable tables is asserted. The complexity is in a full explicit-signature model, not an oracle model, and no optimality lower bound for selective-query algorithms is claimed. Unindexed earlier descriptions of the same cyclic-shift reconstruction may exist. Independent review has not been performed.

## References
1. G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (5 October 2026), especially Lemma 2.1 and Remark 2.4. https://arxiv.org/html/2610.07435v1
2. D. E. Knuth, J. H. Morris Jr., V. R. Pratt, *Fast Pattern Matching in Strings*, SIAM Journal on Computing 6 (1977), 323--350, doi:10.1137/0206024.
