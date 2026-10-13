# \(A_4\) separates strong sync-maximality from primitivity
## Finding
For the natural action on
\[
Q=\{0,1,2,3\},
\]
the alternating group \(A_4\) is primitive but is not strongly sync-maximal.

Consequently, the class of strongly sync-maximal permutation groups is a proper subclass of the class of primitive permutation groups.

An explicit witness is the rank-\(2\) transformation
\[
f=(0,0,1,1),
\]
meaning
\[
f(0)=f(1)=0,\qquad f(2)=f(3)=1.
\]
In the transformation monoid
\[
M=\langle A_4\cup\{f\}\rangle,
\]
the distinct two-subsets
\[
X=\{0,1\},\qquad Y=\{2,3\}
\]
are not distinguishable: every \(h\in M\) satisfies
\[
|h(X)|=|h(Y)|.
\]
Hence no \(h\in M\) maps precisely one of \(X,Y\) to a singleton.

## Assumptions and scope
A permutation group \(G\le S_n\) is strongly sync-maximal in the sense introduced by Hoffmann if, for every transformation \(f:[n]\to[n]\) of rank \(r\) with
\[
2\le r\le n-1,
\]
all two-subsets are distinguishable in \(\langle G\cup\{f\}\rangle\). Two distinct two-subsets are distinguishable when some transformation in the generated monoid maps precisely one of them to a singleton.

The source proves that every strongly sync-maximal group is primitive and asks whether the containment inside the primitive groups is proper. The present claim concerns that upper containment. It does not determine whether every \(4\)-transitive group exhausts the strongly sync-maximal class.

## Proof
First, \(A_4\) is primitive. In fact, it is \(2\)-transitive in its natural action on four points: it is transitive, and the stabilizer of \(0\) contains the three-cycle on \(\{1,2,3\}\), so that stabilizer is transitive on the remaining three points. Every \(2\)-transitive permutation group is primitive.

Now take
\[
f=(0,0,1,1),
\qquad
X=\{0,1\},
\qquad
Y=\{2,3\}.
\]

Consider ordered pairs \((U,V)\) of nonempty subsets of \(Q\) belonging to one of the following three types:

1. \(U\) and \(V\) are both singletons;
2. \(U=V\) and \(|U|=2\);
3. \(U\) and \(V\) are complementary two-subsets of \(Q\).

The initial pair \((X,Y)\) has type 3.

Every permutation preserves these three types: singletons stay singletons, equal two-subsets remain equal, and complementary two-subsets remain complementary. Hence every element of \(A_4\) preserves the union of the three types.

It remains to check \(f\). On singletons, both images are singletons. Equal two-subsets have equal images, which are either a singleton or a two-subset. For complementary two-subsets there are only the three partitions of \(Q\) into two pairs:
\[
\{0,1\}\mid\{2,3\},\qquad
\{0,2\}\mid\{1,3\},\qquad
\{0,3\}\mid\{1,2\}.
\]
Under \(f\), the first pair of blocks maps to the two singletons \(\{0\},\{1\}\), while in each of the other two partitions both blocks map to the same set \(\{0,1\}\).

Therefore the three-type union is invariant under every generator of
\[
M=\langle A_4\cup\{f\}\rangle.
\]
Starting from \((X,Y)\), every pair \((h(X),h(Y))\) has equal component cardinalities. In particular it is impossible for exactly one of \(h(X)\) and \(h(Y)\) to be a singleton.

Thus \(X\) and \(Y\) are not distinguishable, so \(A_4\) is not strongly sync-maximal. Since Hoffmann proved that every strongly sync-maximal group is primitive, while \(A_4\) is primitive, the containment is strict.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently constructs \(A_4\), confirms its two-transitivity, generates the full monoid
\[
\langle A_4\cup\{f\}\rangle,
\]
and checks directly that \(X=\{0,1\}\) and \(Y=\{2,3\}\) always have equal image cardinality.

A second implementation propagates the three-type invariant on ordered pairs of subsets and checks that every generator preserves it.

As a finite stress test beyond the proof, the verifier exhausts all \(84\) rank-\(2\) and all \(144\) rank-\(3\) transformations on four points. It finds \(36\) rank-\(2\) transformations for which \(A_4\) fails the strong condition and no rank-\(3\) failures. These counts support the witness but are not needed for the infinite logical implication that the containment is proper.

## Relationship to prior work
Hoffmann introduced strong sync-maximality as a strengthening of sync-maximality after proving that ordinary sync-maximal groups are exactly the primitive permutation groups. The paper proves
\[
\text{\(4\)-transitive}\Longrightarrow
\text{strongly sync-maximal}\Longrightarrow
\text{primitive}
\]
and explicitly asks whether the strongly sync-maximal groups are properly contained between the two surrounding classes.

The present witness answers the upper-containment part of that question: \(A_4\) is primitive but not strongly sync-maximal. Thus strong sync-maximality is genuinely stronger than primitivity.

A later paper of Rystsov and Szykuła studies when primitive automata are synchronizing and cites Hoffmann's sync-maximal work, but addresses a different implication for transformation monoids rather than the strong sync-maximal distinction between permutation groups.

Targeted searches for the phrases “strongly sync-maximal”, “\(A_4\)”, “primitive but not strongly sync-maximal”, and rank-\(2\) witnesses located the defining paper but no published statement of this separation.

## Limitations
The result settles only the strictness of
\[
\text{strongly sync-maximal}\subseteq\text{primitive}.
\]
It does not settle whether the inclusion
\[
\text{\(4\)-transitive}\subseteq\text{strongly sync-maximal}
\]
is also strict, nor does it classify strongly sync-maximal groups in higher degrees.

The finite exhaustive counts for rank-\(2\) and rank-\(3\) maps are supplementary. The proof of non-strong-sync-maximality uses only the displayed rank-\(2\) map and the invariant above.

An unindexed note or unpublished computation could have observed the same \(A_4\) witness.

## References
1. S. Hoffmann, “Sync-Maximal Permutation Groups Equal Primitive Permutation Groups,” arXiv:2111.13527v1, first public version 2021-11-26; Descriptional Complexity of Formal Systems, DCFS 2021, pp. 38–50, DOI 10.1007/978-3-030-93489-7_4.
2. I. Rystsov and M. Szykuła, “Primitive Automata that are Synchronizing,” arXiv:2307.01302v1, first public version 2023-07-03.
