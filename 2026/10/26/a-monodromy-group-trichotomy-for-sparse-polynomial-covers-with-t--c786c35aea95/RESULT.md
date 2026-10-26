# A monodromy-group trichotomy for sparse polynomial covers with two paired simple branch values

## Finding

Let \(d\ge3\) and let \(f\in\mathbb C[x]\) have degree \(d+4\), a unique finite critical value with one ramification point of local degree \(d\), and exactly two other, distinct, finite critical values, each with two distinct simple ramification points; there are no other finite critical points. Up to an affine change of source and a translation of target, \(f\) has exponents only in \(\{d,d+1,d+2,d+3,d+4\}\). Denote by \(G_f\) the geometric monodromy group of \(f:\mathbb P^1\to\mathbb P^1\), equivalently the Galois group of \(f(X)-t\) over \(\mathbb C(t)\).

The complete group classification of the topological classes appearing in Vladimirov's Proposition 4.6 is:

* If \(d\) is odd, its unique class has \(G_f\cong A_{d+4}\) in its natural degree-\(d+4\) action.
* If \(d\) is even, the class with \(f\) affinely equivalent to \(g(x^2)\) has \(G_f\cong C_2\wr S_{(d+4)/2}\) in its natural action on \((d+4)/2\) pairs. This is the class called \(C_1\) in Proposition 4.6.
* If \(d\) is even, the other class \(C_2\) has \(G_f\cong S_{d+4}\).

These are assertions about **geometric** monodromy of the map \(f(x)\) for each polynomial with the specified passport, not coefficient-space monodromy, arithmetic monodromy, or a claim to reprove the underlying orbit classification.

## Assumptions and scope

All covers are over \(\mathbb C\). By Riemann--Hurwitz the branch-cycle passport is \([(d,1^4),(2,2,1^d),(2,2,1^d)]\) over the three finite branch values, and \((d+4)\) at infinity. The four simple critical points are distinct and their values form two distinct nonzero branch values after target normalization. We rely on the previously proved braid-orbit classification of that passport (Vladimirov, Proposition 4.1) and its identification of the even symmetric-polynomial component (Proposition 4.6). Hurwitz moves and simultaneous conjugation preserve the generated group up to permutation isomorphism.

## Proof

**1. A branch-cycle representative for the nonsymmetric component.** Write \(n=d+4\) and take permutations of \(\{1,\ldots,n\}\):
\[
 c=(1\ 2\ \cdots\ d-1\ n),\qquad
 a=(d+1\ d+2)(d\ d+3),\qquad
 b=(d+1\ d+3)(d\ n).
\]
These have cycle types \((d,1^4),(2,2,1^d),(2,2,1^d)\), and \(cab\) is an \(n\)-cycle (the product convention does not affect the generated group). The representative is exactly the first displayed cactus in the proof of Vladimirov's Proposition 4.1. It lies in the single class if \(d\) is odd and in the nonsymmetric class if \(d\) is even.

**2. It generates the alternating group.** Put \(T=\{d,1,2,\ldots,d-1,n\}\), a set of size \(d+1\). For \(0\le j<d\), the conjugate \(b_j=c^jbc^{-j}\) is \((d+1\ d+3)(d\ c^j(n))\). Thus, for distinct \(i,j\), \(b_ib_j\) is a three-cycle supported on \(\{d,c^i(n),c^j(n)\}\). Since the \(d\) points \(c^j(n)\) exhaust the support of \(c\), these three-cycles generate \(A_T\).

Conjugating \(a=(d+1\ d+2)(d\ d+3)\) by \(A_T\), and multiplying two such conjugates, gives every three-cycle \((d+3\ t\ t')\) with distinct \(t,t'\in T\). It follows that the generated group contains \(A_{T\cup\{d+3\}}\). Conjugation by \(b\) transforms this alternating group into \(A_{T\cup\{d+1\}}\), since \(b\) switches \(d+3\) and \(d+1\) while preserving \(T\) setwise. Two alternating groups on sets with at least three common elements generate the alternating group on the union, so \(A_{T\cup\{d+1,d+3\}}\) is contained. Finally, conjugating by \(a\) replaces \(d+1\) in this support with \(d+2\), and the same overlapping-support argument yields \(A_n\). All conjugations and products are in \(\langle a,b,c\rangle\).

When \(d\) is odd, the \(d\)-cycle \(c\) is even, as are the double transpositions \(a,b\), so \(\langle a,b,c\rangle=A_n\). When \(d\) is even, \(c\) is odd and therefore \(\langle a,b,c\rangle=S_n\). This proves the first and third cases by the cited braid-orbit classification.

**3. A representative for the other even class.** Let \(d=2k\) with \(k\ge2\), and \(m=k+2\). Divide \(2m\) letters into pairs \(B_0,\ldots,B_{m-1}\), each labeled with signs \(+,-\). Consider the following signed permutations: \(t\) cyclically permutes \(B_0,\ldots,B_{k-1}\), reversing the sign once on the wraparound, and fixes the other two pairs; \(s\) interchanges \(B_{k-1}\) and \(B_k\) without sign flips; \(u\) interchanges \(B_k\) and \(B_{k+1}\) without sign flips. As permutations of the \(2m\) individual letters, \(t\) is a \(2k\)-cycle, while \(s,u\) are each products of two disjoint transpositions, and \(tsu\) is a \(2m\)-cycle. Thus these permutations define a connected genus-zero polynomial cover with exactly the required passport, by the Riemann existence theorem. All three preserve the pairing into the \(B_i\).

**4. Full signed-permutation monodromy.** The conjugates \(t^{-j}st^j\), for \(j=0,\ldots,k-1\), act as the unsigned block transpositions \((B_{k-1-j}\ B_k)\); none crosses the sign-reversing wraparound. Together with the unsigned block transposition \(u=(B_k\ B_{k+1})\), they generate the copy of \(S_m\) permuting the pairs without sign flips. Multiplying \(t\) by the inverse of the corresponding unsigned \(k\)-cycle leaves a flip of the sign in a single pair. Conjugating this flip by the obtained \(S_m\) supplies all independent sign flips. Therefore
\[
 \langle t,s,u\rangle=C_2^m\rtimes S_m=C_2\wr S_m.
\]
The group is imprimitive on \(2m\) letters, so this cover cannot lie in the nonsymmetric class just shown to have full \(S_{2m}\) monodromy. There are exactly two braid classes for even \(d\), so the new representative belongs to the other, symmetric class. Proposition 4.6 identifies that class with the polynomials affinely equivalent to \(g(x^2)\). Hurwitz invariance gives the claimed group for every member of that class.

## Verification

The accompanying script `verify_monodromy.py` constructs all three permutation generators for the nonsymmetric cactus and for the signed-pair cactus using zero-based indexing. It checks that the product is a full cycle and computes the exact permutation-group orders using SymPy's Schreier--Sims implementation. It checks all \(3\le d\le14\) in the nonsymmetric family and \(2\le k\le9\) in the signed family, obtaining the expected orders \((d+4)!/2\) (odd \(d\)), \((d+4)!\) (even \(d\)) and \(2^{k+2}(k+2)!\) respectively. Run `python verify_monodromy.py` with SymPy installed. The mathematical argument above, not the finite checks, proves the infinite-family statement.

## Relationship to prior work

Vladimirov (arXiv:2610.15550v1), Propositions 4.1, 4.5 and 4.6, already proves the number of topological classes and identifies the even quadratic-composition class. This result supplies **the exact geometric monodromy group in each class**, which is not stated in those propositions or in the paper's tropical-fan theorem. The source's representative cactus is used verbatim rather than credited as new.

Esterov (arXiv:1801.08260v3) proves symmetric monodromy of **generic coefficient systems**, not of this branch-passport-constrained locus; its hypotheses and family do not imply the odd alternating or the even two-component comparison. Behajaina--König--Neftin (arXiv:2603.27609v1) proves broad lower bounds and exception structures for length-two polynomial compositions; it does not state this precise three-class monodromy classification, and its general large-kernel lower bound alone is weaker than the exact signed-wreath conclusion here. General wreath-product embeddings (Barquero-Sanchez--Calvo-Monge, arXiv:2306.14386v1) are bounds, not proofs of equality. An implicit group-theoretic derivation from earlier permutation-cactus theory remains a priority risk.

## Limitations

This is a theorem about the specified three-critical-value passport over \(\mathbb C\). It says nothing about deformations that split the paired simple critical values, arithmetic Galois groups over number fields, or more general fewnomial supports. The referenced braid-class classification is an external mathematical input, though all new group-generation computations are proved explicitly. Historical priority has not been independently certified.

## References

1. L. Vladimirov, *Topological Classification of Univariate Sparse Polynomials via Tropical Geometry*, arXiv:2610.15550v1, 11 October 2026, especially Propositions 4.1 and 4.6 and the displayed cactus representative.
2. A. Behajaina, J. König, D. Neftin, *Monodromy groups of polynomials of composition length 2*, arXiv:2603.27609v1 (2026), Sections 1--3.
3. A. Esterov, *Galois theory for general systems of polynomial equations*, arXiv:1801.08260v3 (2020), Theorem 1.5.
4. A. Barquero-Sanchez, J. Calvo-Monge, *On the embedding of Galois groups into wreath products*, arXiv:2306.14386v1 (2023).
