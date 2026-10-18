# Exact optimum for binary weight-two single-deletion-correcting codes

## Finding

For each integer \(n\ge2\), let \(A_2(n)\) be the maximum number of pairwise single-deletion-distinguishable binary words of length \(n\) and Hamming weight exactly \(2\). Here two words are distinguishable if no length-\(n-1\) word can be obtained from both by deleting one coordinate. Then

\[
A_2(n)=n-1-\left\lfloor\frac{n+1}{4}\right\rfloor.
\]

An explicit attaining family consists of the words with two one-positions at \((2r,2r+1)\) for every \(r\ge0\) with \(2r+1<n\), together with the words with one-positions at \((4s+1,4s+4)\) for every \(s\ge0\) with \(4s+4<n\). All positions here are zero-based. This construction and an elementary two-shadow obstruction establish the exact optimum for all \(n\ge2\).

## Assumptions and scope

Fix an integer \(n\ge2\). Define \(\mathcal W_{n,2}\) to be the set of binary words \(w=w_0\cdots w_{n-1}\) containing exactly two ones. For \(w\), its one-deletion descendant set is \(D(w)=\{w_0\cdots w_{i-1}w_{i+1}\cdots w_{n-1}:0\le i<n\}\), with duplicate descendants counted only once. A code \(C\subseteq\mathcal W_{n,2}\) is admissible when \(D(u)\cap D(v)=\varnothing\) for all distinct \(u,v\in C\). The claim optimizes \(|C|\) over arbitrary such codes, without a linearity requirement, with exactly one deletion at an arbitrary coordinate. An optimal code need not be unique.

## Proof

Put \(N=n-1\). Write \(w(i,j)\) for the word with ones exactly at \(0\le i<j<n\). Deleting a one from \(w(i,j)\) produces exactly the weight-one descendants with their remaining one at position \(i\) or at position \(j-1\). If \(j=i+1\), these are the same descendant; otherwise they are two distinct descendants. This gives \(N\) possible weight-one descendants, indexed by their sole one-position \(0,1,\ldots,N-1\).

Separate the codewords of an admissible code into \(\ell\) adjacent-one words (\(j=i+1\)) and \(e\) nonadjacent-one words (\(j\ge i+2\)). All weight-one descendant sets are disjoint, so
\[
\ell+2e\le N. \tag{1}
\]

An additional restriction comes from zero deletions. Two adjacent-one words \(w(i,i+1)\) and \(w(i+1,i+2)\), whenever both exist, cannot lie together in an admissible code. Deleting the zero at position \(i+2\) from the first, and the zero at position \(i\) from the second, produces the *same* length-\(n-1\) word with ones at positions \(i,i+1\). Thus the loop-start indices among \(0,\ldots,N-1\) form an independent set of the ordinary path on \(N\) vertices. Consequently,
\[
\ell\le\lceil N/2\rceil. \tag{2}
\]

Combining (1) and (2), every admissible code obeys
\[
|C|=\ell+e\le\left\lfloor\frac{N+\ell}{2}\right\rfloor
\le\left\lfloor\frac{N+\lceil N/2\rceil}{2}\right\rfloor
=n-1-\left\lfloor\frac{n+1}{4}\right\rfloor. \tag{3}
\]

For equality, take the explicit two families described in the finding. Call their words \(U_r=w(2r,2r+1)\) and \(V_s=w(4s+1,4s+4)\), with only valid indices included. The \(U_r\) contribute \(\lceil N/2\rceil\) words; the \(V_s\) contribute \(\lfloor\lfloor N/2\rfloor/2\rfloor\). Their sum is the right-hand side of (3).

It remains to prove disjointness of their full descendant sets, including zero deletions. Their weight-one descendants have positions \(2r\) for \(U_r\), and \(4s+1\) and \(4s+3\) for \(V_s\); these positions are pairwise disjoint across distinct members and across families. Deleting a zero from a \(U_r\) yields a weight-two descendant with *adjacent* ones at \((2r-1,2r)\), if a zero exists before them, or \((2r,2r+1)\), if a zero exists after them. For different \(r\) these possible first-one indices are disjoint. Deleting a zero from \(V_s\) yields weight-two descendants whose ones are among \((4s,4s+3)\), \((4s+1,4s+3)\), and \((4s+1,4s+4)\), subject to existence of the deleted zero. Each such pair has a gap of at least two, hence cannot coincide with a \(U_r\) descendant, and for different \(s\) its first-one position belongs to the disjoint set \(\{4s,4s+1\}\). Weight-one and weight-two descendants cannot coincide. Thus every pair of constructed codewords has disjoint descendant sets. The construction meets the upper bound for every \(n\ge2\), as required. \(\square\)

## Verification

The accompanying self-contained `checker.py` enumerates the complete descendant sets of every constructed word for lengths \(2\le n\le96\), checks their pairwise disjointness, independently computes exact maxima by compatibility-graph recursion for \(2\le n\le8\), and checks the two counting/adjacency ingredients directly through length \(24\). Execute `python3 checker.py`; the accompanying `checker-output.txt` records the execution. The all-length theorem rests on the proof above, not on finite computation.

## Relationship to prior work

Single-deletion correction and the descendant-set formalism are classical; in particular, N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197, discusses maximum unconstrained code sizes and Varshamov–Tenengolts constructions. The weight-two constant-weight metric may be confused with the separate *adjacent-transposition* channel solved by Gómez Soto, Leaños, Ríos-Castro, and Rivera, *The packing number of the double vertex graph of the path graph*, Discrete Applied Mathematics 247 (2018), 327–340, DOI 10.1016/j.dam.2018.03.085. Their polynomial-size transposition packing is not a bound for arbitrary deletion correction. A newer point of comparison, Eyal En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493 (first submitted 2026-09-16), treats asymptotic unrestricted codes correcting at least two deletions, rather than exact single-deletion optimum constrained to weight two. These comparisons do not imply a universal novelty guarantee.

## Limitations

The theorem concerns binary words of **exactly** weight two and one arbitrary deletion only; it does not determine optima for other weights, more deletions, or simultaneous substitution errors. Existence and maximum size are proved, but uniqueness or classification of all optimal codes is not claimed. Computational checks are finite and supplementary. A comprehensive historical priority determination is not asserted; differently indexed literature or inaccessible older theses could contain an equivalent result. Independent validation has not been performed.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197 (2002).
2. J. M. Gómez Soto, J. Leaños, L. M. Ríos-Castro, and L. M. Rivera, *The packing number of the double vertex graph of the path graph*, Discrete Applied Mathematics **247** (2018), 327–340, DOI:10.1016/j.dam.2018.03.085.
3. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, first submitted 2026-09-16.
