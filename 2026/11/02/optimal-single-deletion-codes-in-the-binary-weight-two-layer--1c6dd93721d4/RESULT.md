# Optimal single-deletion codes in the binary weight-two layer

## Finding

For every integer \(n\ge 2\), let \(\mathcal W_{n,2}\) denote the length-\(n\) binary words having exactly two ones. Write \(D_1(w)\) for the set of distinct length-\(n-1\) words obtainable from \(w\) by deleting one position. A code \(C\subseteq\mathcal W_{n,2}\) is single-deletion-correcting if \(D_1(u)\cap D_1(v)=\varnothing\) for every pair of distinct members \(u,v\in C\). Then the maximum possible code size, for **every** \(n\ge2\), is

\[
A_2(n)=\max_C |C|=\left\lfloor\frac{3n-2}{4}\right\rfloor.
\]

A uniform, explicit optimal code is given below. In particular, \(A_2(n)=\tfrac34 n+O(1)\), and the finite-length answer depends only on \(n\bmod4\). This is an exact optimal-code result for the fixed-weight channel; it is not a statement about unrestricted deletion codes.

## Assumptions and scope

Words are binary, have *exactly two ones*, and have a fixed transmitted length \(n\ge2\). Indices begin at zero. The receiver is given any one-deletion output without the deletion position; repeated deletion positions producing the same output are identified. This is zero-error, worst-case decoding. The code need not be linear. All bounds and constructions hold for arbitrary integer block lengths in the stated domain.

For \(N=n-1\), define \(w(a,b)\) for integers \(0\le a\le b<N\) to be the word with ones precisely at original positions \(a\) and \(b+1\). We call \(a=b\) a *loop word*, merely as notation for its adjacent ones; \(a<b\) is a *nonloop word*. This parametrization is bijective onto \(\mathcal W_{n,2}\).

## Proof

**1. One-deletion shadows.** For \(w(a,b)\), the possible outputs obtained by deleting a one have weight one, with their remaining one at position \(a\) or \(b\); these coincide when \(a=b\). The possible outputs obtained by deleting a zero have weight two, with their one-position pairs among

\[
(a-1,b)\quad(a\ge1),\qquad
(a,b)\quad(a<b),\qquad
(a,b+1)\quad(b<N-1).
\]

These are all possibilities: the removed zero lies respectively before both ones, strictly between the ones, or after both ones. A displayed pair is included only under its indicated condition.

**2. Upper bound.** In a correcting code \(C\), the weight-one output positions of distinct codewords are disjoint. Let \(L\) be the number of loop words and \(E\) the number of nonloop words in \(C\). A loop contributes one distinct weight-one output and a nonloop contributes two. There are \(N\) possible weight-one outputs, so

\[
L+2E\le N.\tag{1}
\]

Moreover, loop words at neighboring indices \(a\) and \(a+1\) cannot coexist: they share the weight-two output with adjacent ones at positions \(a,a+1\). Explicitly, delete a zero after the two ones from \(w(a,a)\), and delete a zero before the two ones from \(w(a+1,a+1)\). Both operations are available when the two loop indices exist. Thus the \(L\) loop indices form an independent set of a path on \(N\) vertices, whence

\[
L\le\left\lceil\frac N2\right\rceil.\tag{2}
\]

Using (1) and (2),

\[
2|C|=2L+2E\le N+L\le N+\left\lceil\frac N2\right\rceil.
\]

Since \(|C|\) is an integer,

\[
|C|\le\left\lfloor\frac{N+\lceil N/2\rceil}{2}\right\rfloor
=\left\lfloor\frac{3N+1}{4}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.
\]

**3. Matching construction.** Choose all loop words \(w(a,a)\) whose \(a\) is even, and in addition choose all nonloop words

\[
w(4t+1,4t+3)
\quad\text{for integers }t\ge0\text{ with }4t+3<N.
\]

The loop indices are precisely \(0,2,4,\ldots\) below \(N\), so there are \(\lceil N/2\rceil\) loops. The nonloops pair successive odd indices as \((1,3),(5,7),\ldots\), and their number is \(\lfloor N/4\rfloor\). Their combined number is

\[
\left\lceil\frac N2\right\rceil+
\left\lfloor\frac N4\right\rfloor
=\left\lfloor\frac{3N+1}{4}\right\rfloor.
\]

**4. Deletion shadows are disjoint.** The weight-one outputs of the selected loops are at even positions, while those of the nonloops are at odd positions; all are distinct. A loop at even index \(a\) gives, after deletion of a zero, only adjacent one-position pairs \((a-1,a)\) and \((a,a+1)\), when defined. These pairs do not repeat among different even \(a\). A nonloop \(w(4t+1,4t+3)\) gives only weight-two pairs

\[
(4t,4t+3),\quad(4t+1,4t+3),\quad(4t+1,4t+4),
\]

again omitting an out-of-range endpoint pair. Their gaps are respectively three, two, and three, so none equals a loop's adjacent-one output. Outputs from different \(t\) are distinct because their first coordinates lie in disjoint sets \(\{4t,4t+1\}\). All one-deletion shadows of the construction are therefore pairwise disjoint. The construction attains the upper bound, proving the theorem. \(\square\)

## Verification

The companion standalone program `verify.py` constructs the proposed code and computes its literal one-deletion output sets for all \(2\le n\le200\). In addition, for \(2\le n\le10\), it independently builds the full pairwise deletion-confusability graph on all weight-two words and computes its exact maximum independent set by a branch-and-bound maximum-clique algorithm on the complementary graph. A successful run returned:

`VERIFY_OK constructed_n=2..200 distinct_outputs=54152 exact_MIS_n=2..10 branch_nodes=75`

These finite checks corroborate implementation and boundary cases; **the infinite all-\(n\) claim follows from the upper bound and construction above**, not from exhaustive enumeration.

## Relationship to prior work

A. No (2019) studies exact and bounded maximum independent-set formulations of binary one-deletion codes, including mixed-integer upper bounds for unrestricted block codes. Cullina, Kulkarni and Kiyavash (2012) study the constant-weight deletion-confusability subgraphs and establish optimal **colorings**. That work explicitly distinguishes optimal graph coloring from computing a maximum independent set. The present result supplies the exact all-length **independence number of the weight-two induced subgraph** and an explicit maximum independent family; these statements are not asserted by the cited coloring or unrestricted-code results. In particular, the leading coefficient here is \(3/4\) at fixed weight two, not an asymptotic capacity result for the full binary language.

The sources examined do not establish whether the same special-case formula might appear elsewhere under a different notation (e.g. as a fixed-weight confusability-graph independent-set identity). That is a remaining literature risk, not an assertion that the result has been exhaustively proven novel.

## Limitations

No independent scientific audit has been performed. The theorem concerns one deletion and exactly two ones; no unrestricted, multi-deletion, or higher-weight maximum-code conclusion follows. Related older coding-literature specializations may not have been located. The stand-alone finite verifier is corroboration only; it is not a substitute for the all-length combinatorial argument.

## References

1. A. No, *Nonasymptotic Upper Bounds on Binary Single Deletion Codes via Mixed Integer Linear Programming*, Entropy **21** (2019), 1202. First publicly published 2019-12-06. DOI: https://doi.org/10.3390/e21121202.
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings* (2012), arXiv:1211.4056. https://arxiv.org/abs/1211.4056.
3. D. Cullina, A. A. Kulkarni and N. Kiyavash, *A Coloring Approach to Constructing Deletion Correcting Codes from Constant Weight Subgraphs*, ISIT 2012, pp. 513–517. DOI: https://doi.org/10.1109/ISIT.2012.6284242.
