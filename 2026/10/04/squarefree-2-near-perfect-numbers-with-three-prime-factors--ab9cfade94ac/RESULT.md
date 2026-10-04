# Squarefree \(2\)-near-perfect numbers with three prime factors

## Finding
Let \(p<q\) be odd primes and put
\[
n=2pq.
\]
Then \(n\) is \(2\)-near-perfect if and only if
\[
n\in\{30,66\}.
\]

Explicitly,
\[
\sigma(30)=72=2\cdot30+2+10
\]
and
\[
\sigma(66)=144=2\cdot66+1+11.
\]

Thus the complete squarefree three-prime-support slice consists of \(30\) and \(66\).

## Assumptions and scope
A positive integer \(n\) is \(2\)-near-perfect when there exist two distinct positive divisors \(d_1,d_2\mid n\) such that
\[
\sigma(n)=2n+d_1+d_2.
\]
The omitted divisors are not assumed proper in the general definition. In the present family, however, the required sum \(d_1+d_2\) is smaller than \(n\), so both omitted divisors are automatically proper.

The theorem treats only squarefree even integers with exactly three distinct prime factors, namely \(n=2pq\) with odd primes \(p<q\). It does not classify nonsquarefree numbers \(2^k p^m q^r\).

## Proof
For
\[
n=2pq
\]
with odd primes \(p<q\),
\[
\sigma(n)=3(p+1)(q+1).
\]
Hence any omitted pair must satisfy
\[
d_1+d_2
=
\sigma(n)-2n
=
-pq+3p+3q+3.
\]
Write this quantity as
\[
D(p,q)=-pq+3p+3q+3.
\]
Necessarily \(D(p,q)>0\).

Suppose first that \(p\ge7\). Then \(q\ge11\), and for fixed \(p>3\) the function \(D(p,q)\) decreases with \(q\). Therefore
\[
D(p,q)
\le
D(p,11)
=
36-8p
\le -20,
\]
a contradiction. Thus
\[
p\in\{3,5\}.
\]

If \(p=3\), then
\[
D(3,q)=12
\]
for every prime \(q>3\). When \(q\ge13\), every divisor of \(6q\) that is less than \(12\) belongs to
\[
\{1,2,3,6\}.
\]
The largest sum of two distinct members of this set is
\[
3+6=9<12,
\]
so no omitted pair is possible. It remains to check
\[
q\in\{5,7,11\}.
\]
For \(q=5\), the pair
\[
2+10=12
\]
works, giving \(n=30\). For \(q=7\), no two distinct divisors of \(42\) sum to \(12\). For \(q=11\), the pair
\[
1+11=12
\]
works, giving \(n=66\).

If \(p=5\), then
\[
D(5,q)=18-2q.
\]
Positivity forces
\[
q<9.
\]
Since \(q>5\) is prime, necessarily \(q=7\), and then
\[
D(5,7)=4.
\]
The only positive divisors of \(70\) below \(4\) are \(1\) and \(2\), whose sum is \(3\), so no pair works.

Thus the only possibilities are \(30\) and \(66\), and the displayed identities prove that both are indeed \(2\)-near-perfect.

## Verification
The accompanying `verify.py` independently checks the algebraic deficiency formula, the exclusion of every prime \(p\ge7\), the complete \(p=3\) and \(p=5\) case split, and the two surviving divisor pairs.

It also performs a bounded regression over all odd prime pairs below \(1000\), directly generates the divisors of \(2pq\), and confirms that the only \(2\)-near-perfect examples in that range are \(30\) and \(66\).

The bounded regression is not used for exhaustiveness. The proof above is exhaustive because positivity forces \(p\in\{3,5\}\), after which only finitely many \(q\) remain except for the uniform \(p=3,\ q\ge13\) exclusion.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery, and Zelinsky define \(2\)-near-perfect numbers and completely describe the forms
\[
2^k p^i,\qquad i\in\{1,2\}.
\]
Their 2023 paper therefore treats numbers with two distinct prime factors rather than the squarefree three-prime form \(2pq\).

A later paper by Fearon, Foushee, Porosoff, Skula, Zelinsky, and Zhang completes the classification of \(2\)-near-perfect numbers with exactly two distinct prime factors. Its companion computational repository includes a file of three-prime-factor search results whose first two rows are \(30\) and \(66\), corroborating the examples here. The stated theorem of that work remains restricted to exactly two distinct prime factors, and the computational file is not an exhaustive proof of the squarefree \(2pq\) classification.

OEIS A341475 lists \(30\) and \(66\) among the \(2\)-near-perfect numbers. The sequence entry gives computational membership data but does not state that these two values exhaust the squarefree family \(2pq\).

Targeted searches for “\(2\)-near-perfect \(2pq\),” “squarefree \(2\)-near-perfect,” the pair \(\{30,66\}\), and three-distinct-prime formulations did not locate a prior complete classification of this slice.

## Limitations
The theorem does not classify nonsquarefree three-prime-support numbers such as \(2^k p^m q^r\) when any exponent exceeds one. It also makes no claim about the total number of \(2\)-near-perfect integers with three distinct prime factors.

Search non-detection is not a proof of novelty. A residual possibility remains that an unindexed or unpublished argument has already isolated the same squarefree subfamily.

## References
1. Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery, and Joshua Zelinsky, “On \(2\)-Near Perfect Numbers,” arXiv:2310.01305v1, first posted 2 October 2023; MSC \(11A25\), \(11N25\).
2. Richard Fearon, Henry Foushee, Benjamin Porosoff, Alexander Skula, Joshua Zelinsky, and Kyle Zhang, “Complete characterization of \(2\)-near perfect numbers with exactly \(2\) prime factors,” arXiv:2508.06651v1 (2025).
3. OEIS A341475, “\(2\)-near-perfect numbers.”
