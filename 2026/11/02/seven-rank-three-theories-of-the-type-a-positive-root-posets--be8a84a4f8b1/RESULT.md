# Seven rank-three theories of the type-A positive-root posets

## Finding

For each integer \(n\ge 1\), let \(\mathcal R_n\) be the poset of the positive roots of type \(A_n\), with *strict* root order and no additional predicates or constants. Equivalently, its elements are the nonempty discrete intervals \([i,j]\) with \(1\le i\le j\le n\), and
\[
[i,j]\prec[k,\ell]\quad\Longleftrightarrow\quad k\le i\le j\le\ell\ \text{ and }\ (i,j)\ne(k,\ell).
\]
Then the complete first-order quantifier-rank-three classification, in the language of equality and \(\prec\), is
\[
\boxed{\mathcal R_m\equiv_3\mathcal R_n\quad\Longleftrightarrow\quad\min(m,7)=\min(n,7)}.
\]
Thus precisely **seven** rank-three theories occur, with minimal representatives \(\mathcal R_1,\ldots,\mathcal R_7\). Every finite type-A positive-root poset is rank-three equivalent to one with at most \(7\cdot8/2=28\) elements. The threshold seven is sharp.

## Assumptions and scope

The parameter is a positive integer; the finite domain contains \(n(n+1)/2\) roots. The signature has one strict binary relation and equality, but does **not** name the ambient linear order, individual simple roots, the unique maximal root, the cover relation, or rank. The symbol \(\equiv_3\) means agreement on all first-order sentences of quantifier rank at most three, without a bound on the number of distinct variable names or Boolean operations. For type \(A_n\), the roots \(\alpha_i+\cdots+\alpha_j\) correspond to \([i,j]\) and the standard positive-root order is interval containment.

## Proof

**1. Separation below the threshold.** A longest strict chain in \(\mathcal R_n\) contains exactly \(n\) elements. Indeed, strict containment increases interval length, and \([1,1]\prec[1,2]\prec\cdots\prec[1,n]\) is such a chain.

For an arbitrary strict partial order, define \(L_0(x)\) to be true, and define the following formulas asserting chains of one, two and three distinct strict predecessors:
\[
\begin{aligned}
L_1(x)&:=\exists y\,(y\prec x),\\
L_2(x)&:=\exists y\,(y\prec x\land\exists u\,(u\prec y)),\\
L_3(x)&:=\exists y\,[y\prec x\land\exists u\,(u\prec y)\land\exists v\,(y\prec v\land v\prec x)].
\end{aligned}
\]
Let \(U_i(x)\) be the order-dual formulas, with \(U_0(x)\) true. Each \(L_i,U_i\), for \(0\le i\le3\), has quantifier rank at most two. For every \(1\le k\le7\), choose \(r,s\in\{0,1,2,3\}\) with \(r+s+1=k\). The sentence \(\exists x\,[L_r(x)\land U_s(x)]\) has rank at most three and holds exactly when a chain with at least \(k\) elements exists. Consequently distinct parameters \(1,\ldots,7\) are separated at rank three; so is every parameter below seven from every larger parameter.

**2. Exact finite calculation through parameter 26.** For any finite structure \(P\) in this signature, write \(A_P(x,y,z)\) for the complete atomic diagram of an ordered triple: all three pairwise equalities and each of the six directed strict-order relations, including cases where variables repeat. Define the sets
\[
\begin{aligned}
F_P(x,y)&=\{A_P(x,y,z):z\in P\},\\
G_P(x)&=\{F_P(x,y):y\in P\},\\
H_P&=\{G_P(x):x\in P\}.
\end{aligned}
\]
These are exactly the zero-, one-, two- and three-round backward extension types: the full rank-three sentence theory is determined by \(H_P\), and \(H_P=H_Q\) if and only if \(P\equiv_3 Q\). This is proved by induction on quantifier rank, since existential quantification reads membership in the next extension-type set, universal quantification is its Boolean dual, and atomic formulas read \(A\). The construction needs *sets* of possibilities rather than multiplicities: equality with previously selected variables is already included in each extension diagram.

The accompanying standalone C++17 program computes \(H_{\mathcal R_n}\) exactly, for **every** \(1\le n\le26\), by enumerating all ordered triples of intervals and interning nested finite sets; it neither samples nor imposes a limit on formula shape. The resulting seven distinct theory identifiers are assigned to parameters \(1,2,3,4,5,6\), and all parameters \(7,\ldots,26\) receive the seventh identifier. The independent Python program implements a separate immutable-tuple and nested-frozenset recursion without integer interning and independently finds the same classification for \(1\le n\le12\). The scripts and exact recorded outputs are supplied as standalone files.

**3. Infinite upper tail.** We prove \(\mathcal R_m\equiv_3\mathcal R_n\) whenever \(m,n\ge26\), independently of the finite computation. View each chosen interval as a move selecting one or two (possibly equal) endpoints in its underlying finite linear order. Duplicator maintains a common weak and strict order pattern of all previously selected endpoints, and the following gap invariant with \(r\) rounds remaining: between corresponding consecutive selected endpoints, including the two exterior gaps, the numbers of unused underlying points are either equal and less than \(t_r\), or both at least \(t_r\), where
\[
t_0=0,\qquad t_{r+1}=3t_r+2,
\qquad (t_1,t_2,t_3)=(2,8,26).
\]
If a move inserts zero, one, or two new endpoints into a small gap, copy their exact positions. In a large gap it divides the unused elements into at most three subgaps. Let \(h=t_{r-1}\). At least one source subgap must have size at least \(h\), since otherwise the original gap would have fewer than \(3h+2=t_r\) unused points. In the matching large target gap, copy the sizes of source subgaps smaller than \(h\), allocate at least \(h\) elements to every remaining subgap, and assign the surplus to one such large subgap. The necessary total is at most \(3h+2\), so the allocation always exists. The same reasoning also covers a move whose endpoints belong to different gaps, repeated endpoints, and endpoints coinciding with selected landmarks. Thus the invariant is maintained after every round. Initially the unique gap has at least \(26\) points on each side. After three rounds, all endpoint order/equality comparisons agree. Hence every interval equality and containment comparison among selected intervals agrees: Duplicator wins the three-round game.

**4. Combine.** The calculation identifies \(\mathcal R_7,\ldots,\mathcal R_{26}\) as one rank-three class, and the gap lemma identifies every parameter at least 26 with \(\mathcal R_{26}\). Part 1 proves that no two distinct classes in the resulting list can merge. This establishes the displayed classification for every positive integer parameter.

## Verification

From the included files, run `sh reproduce.sh` with a C++17 compiler and Python 3. The C++ program enumerates all \(n(n+1)/2\) elements of each poset, all ordered pairs and all third-coordinate extensions for every parameter through 26. Its recorded class labels are \(0,1,2,3,4,5,6\) for parameters one through seven and remain \(6\) for parameters eight through 26. The independent Python program computes the nested immutable types through parameter 12 and returns the same pattern, with thirteen distinct singleton types in the stabilized cases. Replaying both implementations from the standalone files matches the stored output exactly. The threshold-26 game argument, not any finite extrapolation, completes the proof for all larger parameters.

## Relationship to prior work

The type-A root poset is classical, and the root-system interpretation is standard. Panyushev (2005) investigates root-poset Hasse-edge types and associated ideals, while Cuntz and Stump (2012) study enumerative root-poset properties and noncrystallographic realizations. Their relevant texts do not state the present rank-three logical classification. General Ehrenfeucht–Fraïssé techniques provide the theoretical framework but do not directly give the sharp cutoff seven for this interval-containment reduct. Distinct finite-model-theoretic results for linear orders, subspace lattices, rooted trees or strict-coordinate grid relations use different domains/signatures and do not imply this exact statement.

## Limitations

The theorem is solely about positive-root posets of type \(A_n\) with strict root order and quantifier rank three. It does not apply to other root-system types, to richer signatures (including named simple roots or cover relation), to higher ranks, or to the full first-order theories of unbounded finite posets. The upper-tail proof gives a coarse sufficient cutoff of 26; the improvement to the sharp cutoff seven uses an exhaustive finite computation whose code and outputs accompany this result. Historical priority has not been exhaustively established beyond the listed searches and primary sources. No independent mathematical audit has been performed.

## References

1. D. I. Panyushev, *The poset of positive roots and its relatives*, arXiv:math/0502385v1 (public 17 February 2005), https://arxiv.org/pdf/math/0502385 .
2. M. Cuntz and C. Stump, *On root posets for noncrystallographic root systems*, arXiv:1212.2876v1 (public 12 December 2012), https://arxiv.org/pdf/1212.2876 .
3. L. Libkin, *Elements of Finite Model Theory* (2004), Ehrenfeucht–Fraïssé games on finite linear orders, standard reference for bounded-rank game methods.
