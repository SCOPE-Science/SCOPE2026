# A 48-state local factorization for ternary L-hypertournaments

## Finding

For the irreflexive ternary specialization of the \(L\)-hypertournaments defined by Huang, Pawliuk, Sabok and Wise, a single unordered triple has \(48\), not merely two or six, admissible local relation states. More precisely, if \(z\) records the number of true ordered instances of \(R\) on that triple, then the local polynomial is
\[
Q(z)=6z+15z^2+18z^3+9z^4=(1+3z+3z^2)^2-1.
\]
Consequently the labeled \(n\)-vertex relation-size enumerator is \(Q(z)^{\binom n3}\), and the number of labeled structures is \(48^{\binom n3}\).

Let \(M_3\) be the Fraisse limit of this finite irreflexive class. Then the injective ordered-tuple orbit profile is
\[
a_n=48^{\binom n3},
\]
while the unrestricted ordered-tuple profile is
\[
b_n=\sum_{k=0}^n {n\brace k}48^{\binom k3}.
\]
For any finite \(A\subseteq M_3\) with \(|A|=m\), the pointwise stabilizer has exactly \(48^{\binom m2}\) orbits on points outside \(A\), and therefore
\[
|S_1(A)|=m+48^{\binom m2}.
\]

## Assumptions and scope

The source's Definition 7.2 is used literally on tuples of distinct elements. To remove an otherwise irrelevant ambiguity about repeated coordinates, the class here is explicitly **irreflexive**: \(R(x_1,x_2,x_3)\) is false whenever two coordinates agree. This is a natural finite-relational specialization of the source definition, but the irreflexive convention is an added assumption and is part of the claim.

The term "3-hypertournament" is not uniform in the literature. Cherlin, Hubicka, Konecny and Nesetril use a different convention in which one chooses one of two cyclic orientations on each triple. The \(48\)-state result concerns the Huang--Pawliuk--Sabok--Wise \(L\)-hypertournament axiom, not that two-state convention and not the older convention choosing exactly one of \(3!\) ordered arcs.

## Proof

Fix an unordered triple and a reference ordering. Identify its six ordered enumerations with \(S_3\), and let \(C=\langle(123)angle=A_3\). Let \(T\subseteq S_3\) be the ordered enumerations on which \(R\) is true.

The first clause of Definition 7.2 says that, for every ordered enumeration, some coordinate permutation makes \(R\) true. Since coordinate permutations act transitively on the six enumerations, this is equivalent to \(T
e\varnothing\).

The second clause forbids a cyclic sequence of three tuples all satisfying the same \(R_\sigma\). Rotating coordinates runs through a coset of \(C\). Because \(C=A_3\) is normal in \(S_3\), allowing an arbitrary coordinate permutation \(\sigma\) does not create any other kind of three-set: it only permutes the two cosets of \(C\). Thus the second clause is equivalent to saying that neither of the two three-element cosets is contained in \(T\).

On each coset one may therefore choose a subset of size \(0\), \(1\), or \(2\), giving generating polynomial \(1+3z+3z^2\). The two cosets are independent, except that the global empty choice is forbidden. Hence
\[
Q(z)=(1+3z+3z^2)^2-1=6z+15z^2+18z^3+9z^4,
\]
and \(Q(1)=48\).

All axioms just analyzed are local to a single unordered triple. Therefore choices on distinct triples are independent. Hereditary closure and joint embedding are immediate. For amalgamation, retain the local states already present on the two sides and choose any of the \(48\) states on every triple meeting both sides outside the common substructure. This is free amalgamation, so the class has a countable homogeneous Fraisse limit \(M_3\).

Homogeneity identifies injective ordered \(n\)-tuple orbits with labeled members of the age, giving \(a_n=48^{\binom n3}\). A general ordered tuple first chooses an equality partition with \(k\) blocks and then an injective orbit on those \(k\) distinct values, giving the Stirling transform for \(b_n\).

Finally, over an \(m\)-element finite parameter set \(A\), adding one new point creates one new unordered triple for each pair from \(A\), and each such triple independently has \(48\) states. Free amalgamation realizes every such pattern and realizes it infinitely often. Thus the pointwise stabilizer has \(48^{\binom m2}\) nonalgebraic point orbits; the \(m\) named elements contribute the algebraic types.

## Verification

`artifacts/verify.py` exhaustively enumerates all \(2^6=64\) truth sets on the six orderings of one triple and tests Definition 7.2 directly, for every coordinate permutation and every cyclic rotation. It obtains exactly \(48\) valid states and relation-size distribution \((6,15,18,9)\) in sizes \(1,2,3,4\). Independently, it classifies the six orderings by permutation parity and verifies that the direct axiom test is equivalent to "nonempty and neither parity class is full." It also checks the first unrestricted tuple-orbit values through arity five by explicit restricted-growth-string enumeration of equality partitions.

## Relationship to prior work

Huang, Pawliuk, Sabok and Wise introduce \(L\)-hypertournaments and give the two defining clauses used above, but their paper is about extending partial automorphisms and profinite topology; the inspected full text contains no local-state count, no \(48\), and no age/orbit enumerator. Their arXiv version first appeared on 17 September 2018, and the journal metadata lists primary MSC 03C13.

Cherlin, Hubicka, Konecny and Nesetril explicitly warn that "hypertournament" has multiple conventions. Their 2021 preprint uses the cyclic-orientation convention: on each triple exactly half of the six orderings lie in the relation, with the alternating group as the local automorphism group. That convention has two local orientations and does not imply the \(48\)-state factorization here.

Targeted published-finding corpus and web searches for the source authors together with "48", local-state counting, Fraisse orbit profiles, and one-point extension counts found no statement equivalent to this factorization. The closest indexed published-finding corpus records concern tuple-orbit profiles of unrelated homogeneous structures.

## Limitations

The theorem is for arity three and for the explicitly irreflexive specialization. For larger prime arities, the forbidden cyclic sets come from cosets of multiple conjugate cyclic subgroups and the local counting problem is substantially less trivial; no formula for those arities is claimed. No EPPA conclusion beyond the source paper is derived. Novelty is supported by targeted searches and full-text inspection, not by a proof that the observation has never circulated informally.

## References

1. J. Huang, M. Pawliuk, M. Sabok, D. T. Wise, *The Hrushovski property for hypertournaments and profinite topologies*, arXiv:1809.06435 (first submitted 17 September 2018); Journal of the London Mathematical Society 100 (2019), 757--774, DOI 10.1112/jlms.12244.
2. G. Cherlin, J. Hubicka, M. Konecny, J. Nesetril, *Ramsey expansions of 3-hypertournaments*, arXiv:2105.12368 (2021).
