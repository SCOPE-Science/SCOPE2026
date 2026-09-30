# Exact ordered-tuple orbit profiles of the five random-poset reduct groups
## Finding
Let \(\mathbb P\) be the countable universal homogeneous partial order. Let \(p_k\) be the number of partial orders on the labeled set \([k]\), with \(p_0=1\). For the five closed groups \(\operatorname{Aut}(\mathbb P)\), \(\operatorname{Rev}\), \(\operatorname{Turn}\), \(\operatorname{Max}\), and \(\operatorname{Sym}(P)\), let \(f_G(k)\) count orbits on ordered injective \(k\)-tuples. Then \(f_G(0)=1\), and for every \(k\ge1\),
\[
f_{\operatorname{Aut}(\mathbb P)}(k)=p_k,\quad
f_{\operatorname{Rev}}(k)=\frac{p_k+1}{2},\quad
f_{\operatorname{Turn}}(k)=p_{k-1},\quad
f_{\operatorname{Max}}(k)=\frac{p_{k-1}+1}{2},\quad
f_{\operatorname{Sym}(P)}(k)=1.
\]
If \(o_G(n)\) counts all ordered \(n\)-tuple orbits, repetitions allowed, then
\[
o_G(n)=\sum_{k=0}^{n}{n\brace k}f_G(k).
\]
Since \(p_0,\ldots,p_4=1,1,3,19,219\), the five injective orbit counts at \(k=3\) are \(19,10,3,2,1\); hence ordered triples distinguish all five groups.

## Assumptions and scope
The groups are the five closed supergroups in the published reduct classification of the random partial order. \(\operatorname{Rev}\) adds order reversal, \(\operatorname{Turn}\) adds rotations, \(\operatorname{Max}\) adds both, and \(\operatorname{Sym}(P)\) is the full symmetric group. The rotation formulas use the published finite rotation-equivalence theorem and homogeneous finite-language presentation of rotating permutations.

## Proof
Homogeneity identifies \(\operatorname{Aut}(\mathbb P)\)-orbits of ordered injective \(k\)-tuples with labeled \(k\)-element partial orders, giving \(p_k\).

For \(\operatorname{Rev}\), duality is an involution on labeled posets. A labeled poset equal to its dual has no strict comparable pair, so the antichain is the unique fixed point. Burnside's lemma gives \((p_k+1)/2\).

For \(\operatorname{Turn}\), finite tuple orbits are precisely rotation-equivalence classes. Fix a label \(r\). The finite rotation theory gives a unique representative of each class whose only maximal element is \(r\). In a finite poset that element is greatest. Deleting it gives an arbitrary labeled poset on the other \(k-1\) labels, and adjoining a greatest element reverses this construction. Thus there are \(p_{k-1}\) rotation classes.

For \(\operatorname{Max}\), quotient the rotation classes by duality. For \(k\ge3\), the finite rotation theorem characterizes rotation equivalence by the three labeled classes \(O_1,O_2,O_3\) on every triple. Duality fixes \(O_1\) and swaps \(O_2,O_3\). Hence a rotation class is dual-fixed exactly when all its triples lie in \(O_1\), equivalently when it is the antichain rotation class. For \(k=1,2\) there is likewise one rotation class. Burnside therefore gives \((p_{k-1}+1)/2\). The full symmetric group has one injective orbit.

Finally, equality patterns of coordinates are invariant. Partitioning \([n]\) into \(k\) equality blocks and then choosing an injective \(k\)-tuple orbit gives the Stirling transform.

## Verification
The accompanying `artifacts/verify.py` enumerates all labeled posets through four labels, reproduces \(1,1,3,19,219\), encodes the three labeled rotation classes on triples, obtains rotation-signature counts \(1,1,1,3,19\), checks one dual-fixed rotation class in every tested size, and recomputes the injective and Stirling-transformed profiles. It terminates with `VERIFY_OK`.

The all-tuple profiles for \(n=0,\ldots,4\), in the group order above, are
\[
(1,1,1,1,1),\ (1,1,1,1,1),\ (4,3,2,2,2),\ (29,17,7,6,5),\ (355,185,45,30,15).
\]

## Relationship to prior work
Pach, Pinsker, Pluhár, Pongrácz, and Szabó classify the five closed supergroups of the random-poset automorphism group. Pach, Pinsker, Pongrácz, and Szabó develop finite rotations, prove the local three-point characterization of rotation equivalence, and prove homogeneity for the rotating structure. Those results supply the structural input. The exact five orbit-profile formulas, their reduction to \(p_k\) and \(p_{k-1}\), and the arity-three separation were not found stated in the checked literature.

## Limitations
Originality is best-of-knowledge rather than a proof of global absence. The finite verifier is a reproducibility check, not an independent audit or formal verification. The general proof depends on the published reduct classification and rotation theorems.

## References
1. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz, C. Szabó, “Reducts of the random partial order,” arXiv:1111.7109; DOI 10.1016/j.aim.2014.08.008.
2. P. P. Pach, M. Pinsker, A. Pongrácz, C. Szabó, “A new operation on partially ordered sets,” arXiv:1208.3504; DOI 10.1016/j.jcta.2013.04.003.
3. M. Kompatscher, T. Van Pham, “A complexity dichotomy for poset constraint satisfaction,” arXiv:1603.00082; zbMATH-indexed MSC includes \(03C35\).
