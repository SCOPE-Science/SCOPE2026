# Exact valuations preserving Tribonacci abelian complexity
## Finding
Let \(\mathbf{tr}\) be the Tribonacci word, the fixed point beginning in \(0\) of
\[
0\mapsto01,\qquad 1\mapsto02,\qquad 2\mapsto0.
\]
Assign nonnegative integer weights
\[
a_0,a_1,a_2
\]
to the letters \(0,1,2\), respectively, and let weighted additive equivalence mean equality of length and equality of total weight.

Then the weighted additive complexity of \(\mathbf{tr}\) equals its abelian complexity at every length if and only if the three weights are pairwise distinct and no one is the arithmetic mean of the other two. Equivalently, all six relations
\[
a_0=a_1,\quad a_0=a_2,\quad a_1=a_2,
\]
\[
2a_0=a_1+a_2,\quad 2a_1=a_0+a_2,\quad 2a_2=a_0+a_1
\]
must fail.

Thus the exceptional valuations are exactly the three equality hyperplanes and the three midpoint hyperplanes.

## Assumptions and scope
The abelian class of a finite ternary word is determined by its Parikh vector
\[
\Psi(w)=(|w|_0,|w|_1,|w|_2).
\]
For the chosen weights, two same-length factors are weighted-additively equivalent when their Parikh-vector difference \(d=(d_0,d_1,d_2)\) satisfies
\[
a_0d_0+a_1d_1+a_2d_2=0.
\]

A published theorem of Richomme, Saari, and Zamboni states that the Tribonacci word is \(2\)-balanced: for any two equal-length factors and each letter, the corresponding letter counts differ by at most \(2\).

The claim classifies all nonnegative integer valuations on the fixed symbolic Tribonacci word. It concerns equality of additive and abelian complexity functions at every factor length, not equality with factor complexity.

## Proof
Take two equal-length factors \(u,v\) and put
\[
d=\Psi(u)-\Psi(v).
\]
Equal lengths imply
\[
d_0+d_1+d_2=0,
\]
and \(2\)-balance implies
\[
|d_i|\le2\qquad(i=0,1,2).
\]

There are only two kinds of nonzero integer vectors satisfying these constraints, up to permuting coordinates and changing sign. Either
\[
(1,-1,0)\quad\text{or}\quad(2,-2,0),
\]
or
\[
(2,-1,-1).
\]
Indeed, if one coordinate is zero then the other two are opposites of magnitude \(1\) or \(2\). If no coordinate is zero, the zero-sum condition and the bound \(2\) force one coordinate to have magnitude \(2\) and the other two to have magnitude \(1\) with the opposite sign.

Suppose first that the weights are pairwise distinct and no one is the arithmetic mean of the other two. A vector of the first kind cannot have weighted dot product zero, because that would force two weights to be equal. A vector of the second kind cannot have weighted dot product zero, because that would force one weight to be the arithmetic mean of the other two. Hence
\[
a_0d_0+a_1d_1+a_2d_2=0
\]
forces \(d=0\). Therefore two weighted-additively equivalent equal-length factors have the same Parikh vector and are abelian equivalent. The converse implication is automatic, so the two equivalence relations, and hence their complexity functions, coincide at every length.

For necessity, if two weights are equal, the corresponding one-letter factors are additively equivalent but not abelian equivalent, so equality already fails at length \(1\).

It remains to exclude distinct weights in arithmetic progression. Each possible midpoint relation has an explicit pair of Tribonacci factors with different Parikh vectors but the required weighted sum equality:

- If \(2a_1=a_0+a_2\), the factors
  \[
  \mathtt{020},\qquad\mathtt{101}
  \]
  have Parikh-vector difference \((-1,2,-1)\).
- If \(2a_2=a_0+a_1\), the factors
  \[
  \mathtt{01001},\qquad\mathtt{20102}
  \]
  have Parikh-vector difference \((-1,-1,2)\).
- If \(2a_0=a_1+a_2\), the factors
  \[
  \mathtt{102010102},\qquad\mathtt{001020100}
  \]
  have Parikh-vector difference \((2,-1,-1)\) in the appropriate orientation.

Thus every forbidden midpoint relation produces a genuine merging of two distinct abelian classes. The six stated conditions are therefore necessary and sufficient.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier generates the Tribonacci fixed point from its defining morphism, checks occurrence and Parikh vectors of all three midpoint witness pairs, and enumerates all \(18\) nonzero integer vectors with coordinate magnitudes at most \(2\) and coordinate sum zero. It verifies algebraically, for all \(729\) weight triples in \(\{0,\ldots,8\}^3\), that avoiding a weighted kernel on those \(18\) directions is exactly the pairwise-distinct, non-arithmetic-progression condition.

As a supplementary direct check, it scans a prefix of length \(120000\), verifies the \(2\)-balance inequality for observed factor Parikh vectors through length \(120\), and compares weighted additive and abelian class counts for all \(125\) triples in \(\{0,\ldots,4\}^3\).

The finite checks are not used to infer the theorem. The infinite step is the published \(2\)-balance theorem together with the complete bounded difference-vector classification above.

## Relationship to prior work
Popoli, Shallit, and Stipulanti emphasize that additive complexity depends on the valuation of the alphabet and explicitly ask when one can choose a valuation making additive and abelian complexities equal. They prove a general sufficient construction for \(C\)-balanced words and note, specifically for the \(2\)-balanced Tribonacci word, that the valuation \(\{0,1,3\}\) works.

That sufficient construction does not characterize the admissible valuations for the Tribonacci word. The present result gives the complete parameter space: the only obstructions are repeated weights and three-term arithmetic progressions. In particular, many admissible valuations fall outside the rapidly separated sufficient construction.

Richomme, Saari, and Zamboni prove the load-bearing balance fact used here: the Tribonacci word is \(2\)-balanced. Their result controls all possible Parikh-vector differences but does not discuss additive valuations.

Targeted searches for Tribonacci valuations, equality of additive and abelian complexity, arithmetic-progression obstructions, and the specific sufficient valuation \(\{0,1,3\}\) did not locate a published necessary-and-sufficient classification.

## Limitations
The classification is specific to the ordinary Tribonacci word and uses its sharp \(2\)-balance property. It does not classify valuations for arbitrary ternary \(2\)-balanced words unless they also realize the midpoint witness directions needed for necessity.

The theorem concerns integer valuations as used in the motivating literature. No claim is made here about other notions of additive equivalence or about additive powers.

An unindexed note or unpublished computation could contain the same six-hyperplane classification.

## References
1. P. Popoli, J. Shallit, and M. Stipulanti, “Additive Word Complexity and Walnut,” arXiv:2410.02409v1, first public version 2024-10-03; FSTTCS 2024, DOI 10.4230/LIPIcs.FSTTCS.2024.32.
2. G. Richomme, K. Saari, and L. Q. Zamboni, “Balance and Abelian Complexity of the Tribonacci Word,” arXiv:0904.2872v1, 2009; Advances in Applied Mathematics 45 (2010), DOI 10.1016/j.aam.2010.01.006.
