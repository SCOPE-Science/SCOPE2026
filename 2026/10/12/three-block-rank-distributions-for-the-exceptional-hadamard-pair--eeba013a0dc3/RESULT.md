# Three-block rank distributions for the exceptional Hadamard pair
## Finding

Let
\[
A_t=H^{1,1,t-4},
\qquad
B_t=\bar H^{2,0,t-5},
\qquad
t\ge5,
\]
be the exceptional pair of nonlinear Hadamard-code families isolated by Bhunia. Put
\[
m=t-5.
\]
Each code has
\[
4\cdot2^m
\]
kernel blocks, each of size \(8\).

For a code \(C\), write \(P_C(j)\) for the number of unordered pairs of distinct kernel blocks whose union has punctured span rank \(j\), and \(T_C(j)\) for the analogous number of unordered triples.

The complete two-block distributions are
\[
P_{A_t}(5)=5\cdot4^m-2^{m+1},
\qquad
P_{A_t}(6)=3\cdot4^m,
\]
and
\[
P_{B_t}(5)=4\cdot4^m-2^{m+1},
\qquad
P_{B_t}(7)=4^{m+1}.
\]
No other two-block ranks occur.

The complete three-block distributions are
\[
T_{A_t}(6)
=
\frac{14\cdot8^m-15\cdot4^m+4\cdot2^m}{3},
\]
\[
T_{A_t}(7)
=
6\cdot8^m-3\cdot4^m,
\]
and
\[
T_{B_t}(6)
=
\frac{8\cdot8^m-12\cdot4^m+4\cdot2^m}{3},
\]
\[
T_{B_t}(8)
=
8\cdot8^m-4\cdot4^m.
\]
No other three-block ranks occur.

In particular,
\[
\max\{j:T_{A_t}(j)>0\}=7,
\qquad
\max\{j:T_{B_t}(j)>0\}=8
\]
for every \(t\ge5\). Thus the third level of the multi-block hierarchy separates the exceptional pair uniformly.

At the base length \(32\), the pair distributions are
\[
A_5:\ 5:3,\ 6:3,
\qquad
B_5:\ 5:2,\ 7:4,
\]
while the triple distributions are
\[
A_5:\ 6:1,\ 7:3,
\qquad
B_5:\ 8:4.
\]
At length \(64\), they become
\[
A_6:\ P=(5:16,6:12),\quad T=(6:20,7:36),
\]
and
\[
B_6:\ P=(5:12,7:16),\quad T=(6:8,8:48).
\]

## Assumptions and scope

The kernel blocks are those defined by equality of all kernel-word coordinate evaluations. The source proves that both \(A_t\) and \(B_t\) have kernel dimension \(t-2\), rank \(t+3\), exactly
\[
2^{t-3}
\]
kernel blocks of size \(8\), and one-block rank \(4\).

Both families are obtained from their length-\(32\) members by repeated binary Plotkin extension. If \(C^+\) is the Plotkin extension of \(C\), every old block \(B\) produces two child blocks \(B_0,B_1\).

The result concerns only unions of two and three distinct kernel blocks in these two exceptional recursively constructed families. It does not claim a formula for every level of the hierarchy or for arbitrary additive Hadamard codes.

## Proof

The source computes the four local spaces for \(A_5=H^{1,1,1}\):
\[
V_{0,0}=\operatorname{span}\{\epsilon,a_1,b_1,d_1\},
\]
\[
V_{0,1}=\operatorname{span}\{a_1,d_1,\epsilon+e_1,b_1+a_1d_1\},
\]
\[
V_{1,0}=\operatorname{span}\{a_1,d_1,b_1,\epsilon+c_1\},
\]
\[
V_{1,1}=\operatorname{span}\{a_1,d_1,b_1,\epsilon+c_1+e_1+b_1d_1\}.
\]
Taking sums gives the published pair ranks
\[
6,5,5,6,6,5.
\]
Taking the four sums of three local spaces gives ranks
\[
7,7,6,7,
\]
so
\[
T_{A_5}(6)=1,\qquad T_{A_5}(7)=3.
\]

For \(B_5=\bar H^{2,0,0}\), the source writes the additive generator as the \(2\times8\) matrix with columns
\[
(1,j)^{\mathsf T},
\qquad
j\in\mathbb Z_8,
\]
and labels its four kernel blocks by
\[
(j\bmod2,\ h_0+h_1).
\]
A direct Carlet-Gray reconstruction from these formulas gives the published pair ranks
\[
5,5,7,7,7,7
\]
and gives rank \(8\) for every one of the four three-block unions. Hence
\[
T_{B_5}(8)=4.
\]

We now derive the Plotkin recurrences. Let \(b\) be the number of parent blocks. The source proves that a sibling pair
\[
\{B_0,B_1\}
\]
has rank \(5\), because every parent block has local rank \(4\), while every pair with two different parents preserves the parent-pair rank. Therefore
\[
P_{C^+}(j)
=
b\,\mathbf 1_{\{j=5\}}+4P_C(j).
\]

For triples, two parent patterns are possible.

First, a triple may use three distinct parent blocks. For each old triple there are \(2^3=8\) choices of children. The extra Plotkin vector is constant on each selected parent block. Its three constants form a vector of \(\mathbb F_2^3\). These constants are already realized by a kernel word: the three distinct block-evaluation functionals on the kernel are linearly independent. Indeed, each evaluates the all-one kernel word as \(1\); a relation involving three distinct functionals would evaluate to \(1\), while relations of one or two terms are impossible because the functionals are nonzero and distinct. Hence the restriction map from the kernel onto the three block constants is surjective. The Plotkin vector adds no dimension, and the triple rank is the parent-triple rank.

Second, a triple may use both children of one parent and one child of a different parent. For each unordered parent pair there are \(2\) choices of the doubled parent and \(2\) choices of the single child, hence \(4\) child triples. The diagonal part has the parent-pair rank. The extra Plotkin vector takes different values on the two children of the doubled parent, while every diagonal vector takes the same value there, so it adds exactly one dimension.

Thus
\[
T_{C^+}(j)
=
8T_C(j)+4P_C(j-1).
\]

Starting from
\[
P_{A_5}(5)=3,\quad P_{A_5}(6)=3,
\]
\[
P_{B_5}(5)=2,\quad P_{B_5}(7)=4,
\]
and
\[
T_{A_5}(6)=1,\quad T_{A_5}(7)=3,
\qquad
T_{B_5}(8)=4,
\]
the pair recurrence solves to the stated pair formulas. Substituting those solutions into the triple recurrence and summing the resulting geometric progressions gives the stated triple formulas.

As consistency checks, the pair counts sum to
\[
\binom{4\cdot2^m}{2}
\]
and the triple counts sum to
\[
\binom{4\cdot2^m}{3}
\]
for both families.

## Verification

`artifacts/verify.py` uses only the Python standard library.

For \(A_5\), it encodes the four published local function spaces over the monomial basis
\[
\epsilon,a_1,b_1,c_1,d_1,e_1,a_1d_1,b_1d_1
\]
and computes every one-, two-, three-, and four-block sum by exact binary row reduction.

For \(B_5\), it reconstructs all \(64\) codewords of \(\bar H^{2,0,0}\) from
\[
(x_1,x_2)\in\mathbb Z_8^2
\]
and Carlet's Gray map. It verifies length \(32\), Hadamard weight distribution
\[
1+62z^{16}+z^{32},
\]
binary span rank \(8\), the four source kernel blocks, the pair histogram
\[
5:2,\ 7:4,
\]
and the triple histogram
\[
8:4.
\]

The verifier then iterates the pair and triple Plotkin recurrences through ten extensions and checks them against the closed formulas. At every stage it also checks that the histogram totals equal the appropriate binomial numbers of block subsets.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Bhunia's paper introduces the multi-block hierarchy explicitly as an open direction. It computes the one-block rank profile, introduces the maximum two-block rank
\[
\mu(C),
\]
computes all six pair ranks only for the two length-\(32\) base codes, and propagates only the maximum \(\mu\) through the exceptional infinite family. The paper does not give the all-\(t\) pair histograms or any three-block histogram.

An immediately preceding paper by the same author develops the one-block kernel-rank profile for the \(\mathbb Z_2\mathbb Z_4\mathbb Z_8\)-linear family. Its scope is the one-block invariant and internal classification; it does not state the multi-block formulas above.

Focused searches using the source identifier, both exceptional family names, “three-block rank,” “multi-block rank hierarchy,” and the length-\(32\) base types did not locate a prior statement of the pair or triple formulas. The source's own explicit formulation of the higher hierarchy as an open question is particularly strong evidence that the three-block distribution is not contained in that work.

## Limitations

The theorem resolves only hierarchy levels \(2\) and \(3\) for the exceptional pair. It does not determine the full hierarchy for arbitrary \(\ell\), nor does it establish that level \(3\) classifies any broader family.

The proof uses the recursive Plotkin realization of the two families. Other additive Hadamard codes with the same abstract type but not permutation equivalent to these recursive constructions are outside the claim.

The base computation for \(B_5\) is finite and exact; the infinite extension is proved by the recurrence, not by finite experimentation.

An unindexed note could contain the same recurrence refinement, although no such source was found in the searches performed.

## References

1. Dipak K. Bhunia, *The kernel-block rank profiles of the \(\mathbb Z_2\mathbb Z_4\)-linear and the \(\mathbb Z_{2^s}\)-linear Hadamard codes, and a complete classification of the \(\mathbb Z_2\mathbb Z_4\mathbb Z_8\)-linear Hadamard codes*, arXiv:2610.00142v1, 10 September 2026.
2. Dipak K. Bhunia, *The kernel-block rank profile and a complete classification of \(\mathbb Z_2\mathbb Z_4\mathbb Z_8\)-linear Hadamard codes*, arXiv:2609.09969v1, 9 September 2026.
