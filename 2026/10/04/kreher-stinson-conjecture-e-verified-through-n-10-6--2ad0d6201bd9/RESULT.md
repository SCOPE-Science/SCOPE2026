# Kreher--Stinson conjecture (e) verified through \(n=10^6\)

## Finding
Let \(b(N)\) be the least integer base greater than \(1\) in which \(N\) has a palindromic digit expansion. Kreher and Stinson conjecture that
\[
b(2^n)=3
\quad\Longleftrightarrow\quad
n\in\{1,2,3,4\}.
\]

Exact integer computation verifies this conjecture for every
\[
1\le n\le10^6.
\]
Thus the only ternary-palindromic powers of two in this range are
\[
2^1=2,\qquad
2^2=(11)_3,\qquad
2^3=(22)_3,\qquad
2^4=(121)_3.
\]

For every \(5\le n\le10^6\), the base-\(3\) expansion of \(2^n\) is not a palindrome.

## Assumptions and scope
For \(n\ge1\), the base-\(2\) expansion of \(2^n\) is a \(1\) followed by \(n\) zeros, so it is not palindromic. Therefore
\[
b(2^n)=3
\]
is equivalent to the base-\(3\) expansion of \(2^n\) being palindromic.

The computation is finite and exact. It does not prove the conjecture for exponents greater than \(10^6\).

## Proof
The verifier stores \(2^n\) in base
\[
B=3^{39}
\]
as a little-endian vector of unsigned integer chunks. Starting from \(1\), each successive value is obtained by exact multiplication by \(2\), with carries reduced modulo \(B\). Because every nonleading chunk represents exactly \(39\) ternary digits, including leading zero digits inside that chunk, this is an exact base-\(3\) representation grouped into blocks.

For each exponent, the program first performs a necessary palindrome filter: it compares the first \(12\) ternary digits with the reverse of the last \(12\) ternary digits. The leading block boundary is handled exactly, including the case where the first \(12\) digits cross a chunk boundary. If the total ternary length is less than \(24\), or if the filter passes, the program reconstructs the complete ternary digit string and compares symmetric digits exactly.

The filter passed beyond the four genuine palindromes only at
\[
n\in
\{41298,41299,41300,62318,377166,877495,918265\}.
\]
A full digit comparison rejects every one of these candidates. The complete scan through \(10^6\) therefore has precisely the four hits
\[
\{1,2,3,4\}.
\]

## Verification
The standalone C++17 file `verify.cpp` implements the exact chunk recurrence and full-palindrome check. It asserts both the complete hit set
\[
\{1,2,3,4\}
\]
and the complete list of exponents that pass the \(12\)-digit necessary filter, and prints `VERIFY_OK` only after scanning all exponents through \(10^6\).

No floating-point arithmetic, probabilistic test, or unbounded inference is used.

## Relationship to prior work
Kreher and Stinson introduced \(b(N)\), reported all palindromic representations of \(2^n\) for \(n<64\), and stated conjecture (e) that \(b(2^n)=3\) exactly for \(n=1,2,3,4\).

OEIS A369233 records the sequence \(b(2^n)\) and describes a linked table for \(1\le n\le10000\). The present calculation extends that stated finite frontier by a factor of \(100\) in the exponent range. Targeted literature and semantic-database searches using the conjecture, the base-\(3\) formulation, and large exponent cutoffs did not locate a stronger published verification.

## Limitations
This is a meaningful finite verification, not an infinite proof. A ternary palindrome could in principle occur for some \(n>10^6\).

The originality comparison is limited by discoverability: an unindexed computation or private calculation may have checked a larger range. The claim here is the exact, reproducible cutoff and certificate described above, not a claim that no one has ever performed a larger unpublished search.

## References
1. D. L. Kreher and D. R. Stinson, “On min-base palindromic representations of powers of 2,” arXiv:2401.07351v1, submitted 14 January 2024; published in *Integers* 24 (2024), Article A69.
2. OEIS A369233, “Smallest base for which the digits expansion of \(2^n\) is palindromic.”
