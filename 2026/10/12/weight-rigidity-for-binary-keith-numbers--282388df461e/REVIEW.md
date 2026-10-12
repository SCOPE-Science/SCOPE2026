# Review

## Correctness
PASS. For a non-power binary string of weight \(w\ge2\), the recurrence identity
\[
K_{n+k+1}=2K_{n+k}-b_k
\]
gives
\[
K_{n+j}=2^{j-1}w-P_{j-1}.
\]
Strict growth after the first recurrence term and the inequality \(K_{2n+1}>N\) force any occurrence before that point. Comparing
\[
2^{j-1}(w-1)<N\le2^{j-1}w
\]
with the \(n\)-bit interval forces \(j=n-\lceil\log_2w\rceil+1\). Splitting at the corresponding suffix yields exactly one Euclidean quotient-remainder pair. The converse reconstructs an \(n\)-bit string of the prescribed weight and verifies the recurrence hit. The power-of-two branch is handled separately. No finite scan is used to prove the infinite statement.

## Originality
PASS with a stated residual risk. The accessible Klazar–Luca paper proves a much weaker density-zero bound in decimal and bases at least \(4\), and explicitly separates base \(2\), mentioning an unpublished Kenneth Fan construction. The public binary OEIS records give the recurrence shortcut, the \(2n\)-position bound, examples, and powers of two, but not the one-candidate-per-weight theorem or the quadratic logarithmic counting bound. Exact semantic and formula-level searches found no accessible equivalent.

The inaccessible Fan manuscript is the principal risk: because it reportedly “constructs all” binary Keith numbers, it could contain a characterization implying the present result. It was not located in bounded searches, so no noncoverage claim is made for it.

## Value
PASS. The result converts the binary case from an enumerative recurrence into a rigid two-parameter classification. For each bit length and Hamming weight, one Euclidean division either produces the unique Keith number or proves none exists. The immediate bound
\[
B_2(x)=O((\log x)^2)
\]
is qualitatively stronger than a mere density-zero statement and explains the extreme sparsity of the public binary sequence.

Self-review: passed. Independent audit: not yet performed.
