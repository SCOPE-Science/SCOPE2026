# Uniform double-factorial representatives for every admissible consecutive-pattern overlap

## Finding

For **every** pair of integers \(m\ge 3\) and \(K>2m\), define the length-\(K\) permutation
\[
\pi_{m,K}=(1,2,\ldots,m-1,K-1,K,m,m+1,\ldots,K-2).
\]
Set \(d=K-m\). For each integer \(j\ge1\), let \(N_{m,K}(j)\) count permutations of \(K+(j-1)d\) whose consecutive blocks of length \(K\) beginning at positions \(1,1+d,\ldots,1+(j-1)d\) all standardize to \(\pi_{m,K}\). Further pattern occurrences are **allowed**, not excluded. Then
\[
\boxed{N_{m,K}(j)=\prod_{t=1}^{j}(2t-1)=(2j-1)!!.}
\]
Thus one explicit representative exists at *every* length \(K>2m\) for *every* overlap \(m>2\), resolving the construction question posed as item 6 of the open problems of Blitvić–Kammoun–Steingrímsson (2026).

## Assumptions and scope

A length-\(K\) consecutive pattern occurs when the relative order of the relevant contiguous block agrees with the given permutation of \(1,\ldots,K\). Each pair of successive required occurrences overlaps in exactly \(m\) **positions**, since their starting positions differ by \(d=K-m\). The count does not impose avoidance or forbid extra occurrences. Since \(K>2m\), \(d>m\), so the overlap occurs entirely inside the terminal increasing tail of the old occurrence. The restriction \(m\ge3\) is that of the motivating open problem; the same argument works for some smaller overlaps but no additional claim is needed here.

## Proof

Represent all prescribed local relative-order inequalities on the \(K+(j-1)d\) positions by a poset \(P_j\). Every permutation having the required standardized blocks corresponds bijectively to a linear extension of \(P_j\): assigning the ranks \(1,\ldots,K+(j-1)d\) in extension order recovers the permutation uniquely. It suffices to prove that the extension numbers \(e(P_j)\) obey \(e(P_1)=1\) and \(e(P_{j+1})=(2j+1)e(P_j)\).

Within each occurrence, write its positional blocks as an increasing block \(A\) of length \(m-1\), the two special entries \(B_1,B_2\), and an increasing terminal block \(C\) of length \(d-1\). Their **value** order is the chain
\[
 A_1<\cdots<A_{m-1}<C_1<\cdots<C_{d-1}<B_1<B_2.
\]
Because \(d-1\ge m\), the last \(m\) positions of an occurrence are all in its increasing block \(C\). When these are shared with the first \(m\) positions of the next occurrence, the first \(m-1\) of the shared vertices become the new \(A\), while the final shared vertex becomes the new \(B_1\). Therefore the next occurrence introduces exactly \(d-1\) fresh vertices constituting its own \(C\), as well as one fresh vertex constituting its \(B_2\).

We inductively maintain the following stronger property. Let \(q_j\) be the **last positional vertex** of the final occurrence in \(P_j\) and \(u_j\) its penultimate positional vertex. Then \(u_j<q_j\); **every other old vertex is either at most \(u_j\) or strictly above \(q_j\)**; and exactly \(2j\) vertices lie strictly above \(q_j\). At \(j=1\), all vertices are linearly ordered by their values, \(u_1\) and \(q_1\) are the final two vertices of \(C\), and the only elements above \(q_1\) are \(B_1,B_2\), so the assertion holds.

Suppose it holds at \(j\). The new occurrence identifies its \(B_1\) with \(q_j\), and its last \(m-1\) first-block positions with terminal vertices at or below \(u_j\). Its new \(C\) is a chain of \(d-1\) vertices constrained to lie **strictly above** all those overlap vertices (in particular \(u_j\)) and **strictly below** \(q_j\). Since every old vertex is either at most \(u_j\) or strictly above \(q_j\), all those fresh \(C\) vertices have uniquely determined relative order with *every* old vertex. Thus adding the whole new \(C\)-chain creates no new linear-extension choices: it subdivides the interval immediately below \(q_j\).

The other fresh vertex, the new \(B_2\), must lie strictly above \(q_j\) but has no required comparison with any of the \(2j\) old vertices above \(q_j\). For **each** extension of \(P_j\), the new \(B_2\) may be inserted into exactly \(2j+1\) positions after \(q_j\), between or after those \(2j\) higher old vertices; distinct positions yield distinct extensions. There are no further restrictions from the new occurrence, so
\[
e(P_{j+1})=(2j+1)e(P_j).
\]
Finally the last fresh \(C\) vertex is \(q_{j+1}\), and the preceding fresh \(C\) vertex is \(u_{j+1}\) (the chain has at least \(d-1\ge m\ge3\) elements). Every vertex not above \(q_{j+1}\) lies at or below \(u_{j+1}\); the strict upper set of \(q_{j+1}\) consists of the \(2j\) old vertices above \(q_j\), the old \(q_j\) itself, and the new \(B_2\), hence has size \(2(j+1)\). The invariant follows. Iterating the recurrence from \(e(P_1)=1\) proves the boxed expression for all specified integer parameters. \(\square\)

## Verification

The standalone dependency-free `verify.py` constructs the overlap posets in two independent ways: adjacent-rank inequalities followed by deletion of minimal elements, and all within-occurrence pairwise inequalities followed by deletion of maximal elements. It checks all sixty triples with \(3\le m\le6\), \(2m+1\le K\le2m+3\) and \(1\le j\le5\), compares the counts to \((2j-1)!!\), and independently verifies the designated global separator, cover relation, and upper-set size. The recorded run returned `VERIFY_OK` for all sixty triples; these computations supplement the all-parameter proof rather than extrapolate it.

## Relationship to prior work

Blitvić, Kammoun and Steingrímsson, *Permutations, Pattern Covers, Posets and Positivity: Part I: Patterns and Posets* (arXiv:2610.29846v1, publicly submitted 2026-10-21), develop the positional-overlap poset construction and enumeration methods, including double-factorial-type classes in Proposition 5.25. Their Section 7, open problem 6, asks whether one can give uniformly described representatives of the double-factorial class for every overlap \(m>2\) and every length \(K>2m\). The explicit representatives and extension recurrence above supply precisely that missing uniform construction. The original authors' general recurrences already allow individual patterns to be enumerated; those methods and the double-factorial sequence itself are not claimed as new.

The earlier 2023 extended abstract by the same authors supplies a general recurrence for consecutive-pattern specifications. Dwyer and Elizalde's 2018 work develops consecutive-pattern equivalences and cluster-poset comparisons. Neither inspected text states this unrestricted construction. Targeted literal and equivalent-formulation searches did not locate earlier explicit all-parameter representatives; this is not a proof of historical priority.

## Limitations

This is a prescribed-occurrence count, not a count of permutations with **exactly** these occurrences, nor the total number of permutations containing the pattern in unspecified locations. The result does not classify every pattern in the same enumeration class, settle other open problems, or certify exhaustive historical novelty. Independent mathematical audit and broader priority examination have not been performed.

## References

1. N. Blitvić, M. S. Kammoun, E. Steingrímsson, *Permutations, Pattern Covers, Posets and Positivity: Part I: Patterns and Posets*, arXiv:2610.29846v1 (submitted 2026-10-21), especially Propositions 5.24–5.28 and Section 7, item 6. https://arxiv.org/abs/2610.29846
2. N. Blitvić, M. S. Kammoun, E. Steingrímsson, *A new perspective on positivity in (consecutive) permutation patterns*, Séminaire Lotharingien de Combinatoire 89B, article 61 (2023), https://strathprints.strath.ac.uk/85045/
3. T. Dwyer, S. Elizalde, *Wilf equivalence relations for consecutive patterns*, arXiv:1801.08262 (2018), https://arxiv.org/abs/1801.08262
