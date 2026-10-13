# The first full-support failure of the circular Parikh rewriting rules occurs at length six
## Finding
Fix the ordered alphabet \(\Sigma=\{a<b<c\}\). A circular word has full support when each of \(a,b,c\) occurs. Two circular words are \(M\)-equivalent when their averaged circular Parikh matrices are equal.

Consider the two \(M\)-equivalence-preserving rules \(CE_1\) and \(CE_2\) introduced for ternary circular words. Say that these rules are complete on a finite \(M\)-equivalence class when the graph whose edges are single applications of \(CE_1\) or \(CE_2\), applied to arbitrary rotations, is connected.

For full-support ternary circular words, \(CE_1\) and \(CE_2\) are complete through length \(5\), but they first fail at length \(6\).

At length \(5\) there is exactly one nontrivial full-support \(M\)-equivalence class,
\[
\{[\mathtt{aacbc}],[\mathtt{abacc}]\},
\]
and its two members are joined by the published rules.

At length \(6\) there are exactly eight nontrivial full-support \(M\)-equivalence classes. Five are connected by \(CE_1,CE_2\). The remaining three are
\[
\{[\mathtt{aabcbc}],[\mathtt{ababcc}]\},
\]
\[
\{[\mathtt{aacbcb}],[\mathtt{abaccb}]\},
\]
and
\[
\{[\mathtt{abacbc}],[\mathtt{abcacb}],[\mathtt{abcbac}]\}.
\]
Every one of these seven circular words admits no \(CE_1\) or \(CE_2\) move at all.

Their circular Parikh-matrix signatures \((|a|,|b|,|c|,|ab|,|bc|,|abc|)\) are respectively
\[
\left(2,2,2,\frac73,\frac73,\frac{13}6\right),\qquad
\left(2,2,2,\frac53,\frac53,\frac56\right),\qquad
\left(2,2,2,2,2,\frac43\right).
\]

## Assumptions and scope
Circular words are conjugacy classes under cyclic rotation. The circular Parikh matrix is the average of the ordinary Parikh matrices of the conjugates, equivalently the matrix whose relevant upper-triangular entries are the averaged scattered-subword counts for \(a,b,c,ab,bc,abc\).

Rule \(CE_1\) rewrites
\[
xacyca\longleftrightarrow xcayac
\]
when
\[
|y|_b(|x|_a-|x|_c)=|x|_b(|y|_a-|y|_c).
\]
Rule \(CE_2\) rewrites
\[
x\alpha byb\alpha\longleftrightarrow xb\alpha y\alpha b,\qquad \alpha\in\{a,c\},
\]
when, writing \(\bar\alpha\) for the other letter in \(\{a,c\}\),
\[
|x|_{\bar\alpha}(|y|+|y|_b+3)=|y|_{\bar\alpha}(|x|+|x|_b+3).
\]

The claim is deliberately restricted to full-support words. If one of the three letters is absent, binary circular \(M\)-equivalence has a separate simple characterization, and the ternary rewriting rules are not intended to generate all such binary-support coincidences.

## Proof
For each \(1\le n\le6\), enumerate all \(3^n\) linear words and replace each by its lexicographically least rotation. The resulting necklace counts are
\[
3,6,11,24,51,130,
\]
in agreement with the necklace formula
\[
\frac1n\sum_{d\mid n}\varphi(d)3^{n/d}.
\]

Discard necklaces missing at least one letter. The numbers of full-support circular words at lengths \(1,\ldots,6\) are
\[
0,0,2,9,30,91.
\]

For each remaining necklace, compute its circular Parikh matrix by averaging over all cyclic shifts. Group equal matrices. Up through length \(4\) there is no nontrivial full-support \(M\)-equivalence class. At length \(5\) there is one, with two members. At length \(6\) there are eight, containing seventeen circular words in total.

Next build the rule graph. For each circular word, inspect every rotation and every decomposition permitted by \(CE_1\) and \(CE_2\), test the exact numerical side condition, and add the resulting circular-word edge. Every rule edge is independently checked to preserve the circular Parikh matrix.

At length \(5\), the sole nontrivial \(M\)-class is connected. At length \(6\), five of the eight nontrivial classes are connected and three are disconnected. In each disconnected class, every vertex has degree zero, giving exactly the three classes displayed above.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier computes circular Parikh matrices in two independent ways. The first directly counts the scattered subwords \(ab\), \(bc\), and \(abc\) in every cyclic shift and averages. The second multiplies the \(4\times4\) letter Parikh matrices for each distinct conjugate and averages the resulting matrices. The two methods agree on every circular word through length \(6\).

The rule graph is also built twice: once by constructively generating all one-step \(CE_1/CE_2\) rewrites, and once by testing every pair in each \(M\)-class for the existence of a permitted rotation and decomposition. The edge sets agree exactly.

## Relationship to prior work
Poovanandran, Simpson, and Teh introduced averaged Parikh matrices for circular words, posed the ternary \(M\)-equivalence characterization problem, and derived Rules \(CE_1\) and \(CE_2\). They explicitly state that the rules are not complete and give the length-\(8\) pair
\[
[\mathtt{aaaacbbc}],\qquad [\mathtt{aaacbabc}]
\]
as an \(M\)-equivalent pair to which neither rule applies.

The present result sharpens that observation to the minimal full-support boundary. It proves that the rules are complete through length \(5\), identifies length \(6\) as the first failure, and gives the complete list of the three exceptional \(M\)-classes there.

Exact-string searches for the seven length-\(6\) words, searches using the \(CE_1/CE_2\) terminology, and searches phrased in terms of the first or minimal failure located the source article but no published length-\(6\) classification.

## Limitations
This is a finite minimal-boundary classification. It does not characterize ternary circular \(M\)-equivalence in general and does not propose a replacement rule system.

Completeness is with respect to the published \(CE_1,CE_2\) rules and their transitive closure on circular words, allowing application to any rotation. Unindexed computational notes or source-author experiments may contain the same small census even though the inspected publication does not.

## References
1. G. Poovanandran, J. Simpson, and W. C. Teh, “Counting Subwords in Circular Words and Their Parikh Matrices,” arXiv:2110.14858v1, first public version 2021-10-28; Theoretical Computer Science 985 (2024), 114344, DOI 10.1016/j.tcs.2023.114344.
