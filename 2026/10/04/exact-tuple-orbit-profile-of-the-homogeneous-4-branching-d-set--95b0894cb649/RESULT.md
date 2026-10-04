# Exact tuple-orbit profile of the homogeneous 4-branching D-set

## Finding
Let \((N,D)\) be the unique countable dense proper homogeneous 4-branching \(D\)-set, and let \(N_4\) be the set-homogeneous 4-hypergraph of Assari–Hosseinzadeh–Macpherson built from it. Their Proposition 4.2.3 proves \(\operatorname{Aut}(N_4)=\operatorname{Aut}(N,D)\). If \(a_4(n)\) is the number of automorphism orbits on injective ordered \(n\)-tuples, then \(a_4(1)=1\), and for \(n\ge2\)
\[
a_4(n)=r_{n-1},
\]
where \(R(x)=\sum_{m\ge1}r_m x^m/m!\) is the unique formal power series satisfying
\[
R=x+\frac{R^2}{2}+\frac{R^3}{6}.
\]
Equivalently,
\[
a_4(n)=(n-2)!\,[u^{n-2}]\left(1-\frac u2-\frac{u^2}{6}\right)^{-(n-1)}.
\]
The profile starts
\[
1,1,1,4,25,220,2485,34300,559405,10525900,\ldots.
\]
For arbitrary ordered tuples, with repetitions allowed,
\[
b_4(n)=\sum_{k=1}^n {n\brace k}\,a_4(k).
\]

## Assumptions and scope
The source paper states that for every branching number \(k\ge3\) there is a unique countable dense proper homogeneous \(k\)-branching \(D\)-set, gives the unrooted-tree interpretation of \(D\), and specializes to the 4-branching structure in constructing \(N_4\). The statement here concerns the 4-branching case and the full automorphism group preserving \(D\), equivalently \(\operatorname{Aut}(N_4)\). The tuple entries in \(a_4(n)\) are pairwise distinct.

## Proof
For a finite set of distinct points in a \(D\)-set, use the standard unrooted-tree picture: take their finite connecting hull and suppress degree-2 vertices. Its leaves are the selected points, and the relation \(D(x,y;z,w)\) records that the \(x\)-to-\(y\) path and the \(z\)-to-\(w\) path are disjoint. In a 4-branching \(D\)-set every internal vertex of this reduced finite hull has degree 3 or 4. Conversely, density and 4-branching allow every finite leaf-labelled tree with internal degrees in \(\{3,4\}\) to occur. The quartet relation determines such a reduced tree, and homogeneity extends every isomorphism of the resulting finite \(D\)-substructures. Hence injective ordered \(n\)-tuple orbits are exactly reduced unrooted trees with leaves labelled \(1,\ldots,n\) and internal degrees 3 or 4.

Fix the leaf labelled \(n\), delete it and its incident edge, and root the remaining tree at the former neighbour of that leaf. An internal vertex of unrooted degree 3 or 4 then has respectively 2 or 3 children. This gives a bijection, for \(n\ge2\), with rooted non-plane trees on the remaining \(n-1\) labelled leaves in which every internal vertex has 2 or 3 children. If \(R\) is the exponential generating function for these rooted trees, the root is either a leaf, an unordered pair of rooted trees, or an unordered triple, giving
\[
R=x+R^2/2!+R^3/3!.
\]
Thus \(a_4(n)=r_{n-1}\). Rewriting as
\[
R=x\left(1-R/2-R^2/6\right)^{-1}
\]
and applying Lagrange inversion yields the coefficient formula above. A tuple with repetitions is classified first by its equality kernel, a set partition into \(k\) blocks, and then by an injective \(k\)-tuple orbit, which gives the Stirling transform for \(b_4(n)\).

## Verification
The bundled verifier independently generates every rooted non-plane tree on a fixed labelled leaf set by enumerating all set partitions of the labels into 2 or 3 nonempty child blocks and recursively combining canonical child trees. Through seven leaves, those exhaustive counts agree with the coefficient recurrence from \(R=x+R^2/2+R^3/6\). It separately evaluates the Lagrange-inversion coefficient formula and checks the displayed 4-branching orbit values through arity 10. It also checks the four-point anchor: three binary quartet splits plus the degree-4 star give exactly four injective ordered 4-tuple orbits. Running `python3 verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Assari, Hosseinzadeh and Macpherson supply the model-theoretic structure: the unique homogeneous 4-branching \(D\)-set, its tree interpretation, and the equality \(\operatorname{Aut}(N_4)=\operatorname{Aut}(N,D)\). Classical phylogenetic-tree literature treats leaf-labelled reduced trees and, in particular, the binary degree-3 specialization. The existing ledger already contains that 3-branching specialization, where the same rooting argument gives \((2n-5)!!\). The present result is the first ledger item for branching number 4 and identifies its exact algebraic orbit generating function, coefficient formula, and initial profile. Targeted published-finding corpus and web searches for the 4-branching \(D\)-set profile, the initial sequence, and the algebraic equation found no statement connecting this exact enumeration to \(N_4\) or to its automorphism group. The constrained phylogenetic-tree enumeration itself is not claimed to be new; the claimed contribution is the exact identification with this homogeneous/set-homogeneous model-theoretic orbit profile.

## Limitations
The literature search cannot exclude an unindexed or differently phrased prior observation. The tree representation used here is the standard finite-hull interpretation of \(D\)-relations; the source paper sketches that interpretation rather than presenting this orbit enumeration. No claim is made that the numerical constrained-tree sequence is new outside model theory. Independent external audit has not been performed.

## References
1. Amir Assari, Narges Hosseinzadeh, Dugald Macpherson, “Set-homogeneous hypergraphs,” *Journal of the London Mathematical Society* 108 (2023), 1852–1885, DOI 10.1112/jlms.12796; arXiv:2202.09613. First public arXiv date: 2022-02-19. Primary MSC 03C15.
2. Charles Semple and Mike Steel, *Phylogenetics*, Oxford University Press, 2003, for standard leaf-labelled reduced phylogenetic trees and quartet encodings.
