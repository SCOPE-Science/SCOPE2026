# Symmetry jump in the minimal 13-line Numerical Terao pair
## Finding
Let \(\mathcal A\) and \(\mathcal B\) be the two explicit arrangements of thirteen lines in Examples 3.1 and 3.2 of Kühne--Luber--Pokora. The source proves that both have weak combinatorics
\[
(13;16,6,4,2),
\]
while \(\mathcal A\) is free with exponents \( (6,6) \) and \(\mathcal B\) is plus-one-generated with exponents \( (5,8,8) \).

Their symmetry groups are sharply different. For \(\mathcal A\), the automorphism group of the full intersection lattice is \(C_2\), but the only projective automorphism preserving the arrangement is the identity. For \(\mathcal B\), the lattice automorphism group is the dihedral group \(D_8\) of order \(8\), whereas the projective stabilizer is its Klein-four subgroup \(V_4\). Hence
\[
|\operatorname{Stab}_{\mathrm{PGL}_3}(\mathcal A)|=1,\qquad
|\operatorname{Stab}_{\mathrm{PGL}_3}(\mathcal B)|=4,
\]
and in both cases the projectively realizable subgroup has index \(2\) in the lattice automorphism group.

## Assumptions and scope
The ground field is \(\mathbb C\). The line factors are exactly those displayed in Examples 3.1 and 3.2 of arXiv:2407.07070v1. The symbol \(D_8\) means the dihedral group of order \(8\). The projective stabilizer is the subgroup of \(\mathrm{PGL}_3(\mathbb C)\) that preserves the union of the thirteen lines setwise.

The result is about these two concrete realizations. It does not assert that freeness is determined by projective symmetry, nor that every arrangement with weak combinatorics \( (13;16,6,4,2) \) has one of these symmetry groups.

## Proof
Encode each line by its coefficient point \([a:b:c]\) in the dual projective plane. Exact algebraic arithmetic over \(\mathbb Q(i)\) for \(\mathcal A\) and \(\mathbb Q(\sqrt 5)\) for \(\mathcal B\) gives, in each case, exactly sixteen double, six triple, four quadruple, and two quintuple intersection points, reproducing the source's weak combinatorics.

The full lattice automorphism group can be obtained from the colored incidence graph between the thirteen lines and all intersection points of multiplicity at least three. This loses no information about double points: a pair of lines meets at a double point exactly when it is not contained together in any higher-multiplicity block. Exact graph automorphism enumeration gives two line permutations for \(\mathcal A\), with element-order profile \(1^1 2^1\), hence \(C_2\). For \(\mathcal B\) it gives eight permutations with order profile \(1^1 2^5 4^2\), which identifies \(D_8\).

Every projective stabilizer element induces one of these lattice automorphisms. Choose four line-coefficient points in general position. For each lattice permutation there is then at most one dual projectivity carrying those four points to their prescribed images. Solving that projectivity exactly and testing it on all thirteen line points exhausts the possibilities. In \(\mathcal A\), only the identity passes. In \(\mathcal B\), exactly four permutations pass; their order profile is \(1^1 2^3\), so the projective group is \(V_4\). This proves fullness rather than merely exhibiting subgroups.

## Verification
The accompanying `verifier.py` reconstructs the two line sets from the source equations, computes all intersection blocks, enumerates the colored incidence-graph automorphisms, reconstructs the unique candidate dual projectivity for every lattice automorphism from a projective frame, and checks all thirteen line images exactly. A fresh replay with SymPy 1.14.0 and NetworkX 3.6.1 returns:

`VERIFY_OK sympy=1.14.0 networkx=3.6.1 weak=(13;16,6,4,2) A:lattice=C2,projective=1 B:lattice=D8(order8),projective=V4`

The finite enumeration is exhaustive because every projective automorphism must permute the finite line set and hence appears among the enumerated lattice automorphisms.

## Relationship to prior work
Kühne--Luber--Pokora introduce \(\mathcal A\) and \(\mathcal B\) as a smallest counterexample to the Numerical Terao Conjecture and determine their homological types. Their inspected v1 full text contains no discussion of automorphisms, stabilizers, or symmetry groups. Searches for the exact equations, the 13-line Numerical Terao pair, projective stabilizers, Klein-four symmetry, and lattice automorphism groups found no source stating or implying the symmetry profile above.

The closest published research-index hits concern projective stabilizers of unrelated curve arrangements. Those results do not cover these thirteen-line configurations or imply their lattice-to-projective symmetry indices.

## Limitations
The computation is over characteristic zero and uses the two displayed complex realizations only. It does not classify the entire realization spaces of their two matroids. The two arrangements have equal weak combinatorics but different intersection lattices, so the symmetry jump is an additional geometric distinction hidden by weak combinatorics, not an invariant separating two realizations of the same matroid. A residual originality risk is that the same finite-group calculation may occur in supplemental data or older arrangement literature under unlabeled matroid notation.

## References
1. L. Kühne, D. Luber, P. Pokora, *On the Numerical Terao's Conjecture and Ziegler pairs for line arrangements*, arXiv:2407.07070v1, 9 July 2024, especially Theorem 1.5 and Examples 3.1--3.2.
