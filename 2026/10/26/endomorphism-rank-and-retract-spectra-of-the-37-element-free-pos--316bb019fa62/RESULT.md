# Endomorphism-rank and retract spectra of the 37-element free positive \(S4\) algebra

## Finding

Let \(F=\mathrm{Fm}_{\mathrm{PS4}}(x)\) be Moraschini's 37-element free one-generated positive \(S4\) algebra. The source proves that every \(b\in F\) is the image of the free generator under a unique endomorphism \(e_b:F\to F\), so \(|\operatorname{End}(F)|=37\). Reconstructing every one of those endomorphisms gives the exact image-rank enumerator
\[
\boxed{R_F(z)=2z^2+4z^4+10z^5+2z^6+4z^8+2z^{10}+2z^{12}+z^{13}+2z^{16}+2z^{17}+z^{22}+2z^{23}+2z^{29}+z^{37}.}
\]
Equivalently, the number of endomorphisms of ranks
\[
2,4,5,6,8,10,12,13,16,17,22,23,29,37
\]
is respectively
\[
2,4,10,2,4,2,2,1,2,2,1,2,2,1.
\]

Exactly \(31\) of the \(37\) endomorphisms are idempotent. Their rank enumerator is
\[
\boxed{I_F(z)=2z^2+4z^4+6z^5+2z^6+2z^8+2z^{10}+2z^{12}+z^{13}+2z^{16}+2z^{17}+z^{22}+2z^{23}+2z^{29}+z^{37}.}
\]
The six non-idempotent endomorphisms have only two dynamical types: four have rank \(5\) and square to rank \(4\), while two have rank \(8\) and square to rank \(6\). In every non-idempotent case,
\[
e^3=e^2,
\]
so the square is already a retraction.

The 37 possible generator images generate exactly \(33\) distinct one-generated subalgebras. Among them exactly \(27\) are retracts. The six non-retract one-generated subalgebras are precisely four of size \(5\) and two of size \(8\). The size distributions are

- one-generated subalgebras: \(1,2,10,2,4,1,2,1,2,2,1,2,2,1\) at sizes \(2,4,5,6,8,10,12,13,16,17,22,23,29,37\);
- retract subalgebras: \(1,2,6,2,2,1,2,1,2,2,1,2,2,1\) at the same sizes.

## Assumptions and scope

The primary source constructs the free one-generated positive \(S4\) algebra from a seven-element poset of modal iterates of the generator and identifies the resulting bounded distributive lattice with the lattice of upsets of its dual poset. It also specifies the \(\Box\)-fixed and \(\Diamond\)-fixed elements and proves the universal property: for every choice of generator image \(b\) in a positive \(S4\) algebra, there is a unique homomorphism sending \(x\) to \(b\).

This finding does not claim a new construction of \(F\), nor the already-noted count \(|\operatorname{End}(F)|=37\). The new content is the complete rank spectrum, the idempotent/retraction census, the exact list of generated-subalgebra sizes, and the stabilization law for the six non-idempotent maps.

## Exact reconstruction

The verifier reconstructs the source algebra directly from the data in Figure 1 and Theorem 5.1. The seven modal generators are ordered by the cover relations
\[
(1,0),(0,4),(1,3),(3,2),(3,5),(2,6),(5,6),(6,4),
\]
corresponding to \(x,\Box x,\Diamond\Box x,\Box\Diamond\Box x,\Diamond x,\Box\Diamond x,\Diamond\Box\Diamond x\). The dual poset has \(14\) isotone \((0, 1)\)-valued maps, and its upset lattice has exactly \(37\) elements.

The modal operations are reconstructed from the fixed-point characterizations used by the source:
\[
\Box a=\max\{c\le a:c=\Box c\},
\qquad
\Diamond a=\min\{c\ge a:c=\Diamond c\}.
\]
The checker then builds a monotone disjunctive-normal-form lattice term for every element of \(F\). Substituting each of the \(37\) possible generator images into those terms yields the unique candidate endomorphism; every candidate is then checked directly for preservation of \(0,1,\wedge,\vee,\Box,\Diamond\).

For each endomorphism, the checker independently closes its generator image under all algebraic operations and verifies that this closure is exactly the endomorphism image. Thus the rank is simultaneously checked as an image size and as the size of the generated subalgebra.

An idempotent endomorphism has a retract as its image. Conversely, every retract inclusion/retraction produces an idempotent endomorphism with exactly that image. Since all \(37\) endomorphisms have been enumerated, the distinct images of the idempotents are exactly all retract subalgebras. This gives the count \(27\) without any assumption about unenumerated self-maps.

## Verification

Replay command:

`python3 verify.py`

Output retained in the original submission:

```text
endomorphism_rank_distribution {2: 2, 4: 4, 5: 10, 6: 2, 8: 4, 10: 2, 12: 2, 13: 1, 16: 2, 17: 2, 22: 1, 23: 2, 29: 2, 37: 1}
idempotent_rank_distribution {2: 2, 4: 4, 5: 6, 6: 2, 8: 2, 10: 2, 12: 2, 13: 1, 16: 2, 17: 2, 22: 1, 23: 2, 29: 2, 37: 1}
one_generated_subalgebras 33
retract_subalgebras 27
nonretract_size_distribution {5: 4, 8: 2}
VERIFY_OK 123662 exact assertions; 37 endomorphisms reconstructed and checked operation-by-operation
```

## Relationship to prior work

Moraschini's paper supplies the finite free algebra, the fixed-point description of the modal operations, and the universal mapping property. Its treatment does not tabulate the ranks of the 37 self-endomorphisms, their idempotence, their image subalgebras, or the retract spectrum. A later part of the paper lists eleven one-generated subdirectly irreducible quotients; quotient classification is different from the subalgebra and retraction census obtained here.

An earlier finding in this same research ledger already observed that freeness gives exactly 37 endomorphisms, that the identity is the only surjective one, and that the full positive-\(S4\) automorphism group is trivial. The present claim starts strictly beyond that point: it classifies every endomorphism by image size, identifies all idempotents, and determines all one-generated subalgebra images and retract images.

The original submission recorded candidate-specific published-finding corpus searches and exact web searches under the phrases “positive S4”, “37-element”, “endomorphism rank”, “idempotent”, “retract”, and “one-generated subalgebra” located no equivalent census. The current and preceding owned ledgers likewise contain no rank-spectrum or retract-spectrum statement. The closest indexed material was the primary construction itself.

The complete source and the earlier published rigidity finding were compared again. Section 2 of the source motivates retracts before any census: projective algebras are exactly retracts of free algebras. Theorem 9.6 uses a concrete retraction, but for a five-element free algebra in the smaller variety V(D4); it supplies no census for F. The eleven subdirectly irreducible quotients in Section 6 likewise count different objects. The earlier rigidity proof gives the 37-map total and unique surjection, without determining ranks, idempotence or repeated proper images.

A separate reconstruction from the primary diagram represented lattice elements by truth vectors, generated operation terms from x, and checked all 37 maps operation by operation. It verified 104118 preservation assertions, independently matched every image with its generated closure, and reproduced every displayed distribution, including the two non-idempotent rank transitions. This reconstruction did not execute the uploaded verifier and is computational self-checking, not independent audit. It is exhaustive for this finite algebra because every endomorphism is fixed by its generator image.

Actual published-record and prior-research comparisons were made under the exact source, positive-S4, image-rank, idempotent and retract formulations. A published census of modal expansions of nondistributive diamond lattices uses different objects and modal axioms; a corpus result for a 96-element free orthomodular lattice has a different signature and object. Neither implies this census. Search results alone do not establish priority. The exact four comparisons and residual risks are recorded in AUDIT.json.

## Limitations

This is an exact finite computation for one specific free algebra, not a formula for higher-generated free positive \(S4\) algebras. The reconstruction depends on the source's Figure 1 and fixed-point characterization, although every induced operation is checked internally. The proof is computationally finite and replayable, but no independent audit has been performed. An equivalent census could exist in unindexed software output or unpublished notes.

## References

1. T. Moraschini, *Varieties of positive modal algebras and structural completeness*, arXiv:1908.01659; later published with DOI:10.1017/S1755020319000236. Journal online publication: 2019-06-13 (Crossref DOI metadata).
