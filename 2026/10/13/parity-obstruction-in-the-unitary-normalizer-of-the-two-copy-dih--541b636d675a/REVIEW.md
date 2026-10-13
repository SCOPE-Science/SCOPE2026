# Review

## Correctness
PASS. The quotient is the image of the conjugation homomorphism from the unitary normalizer, not automatically the whole abstract automorphism group. For a finite group, an automorphism is in that image exactly when twisting the represented action by the automorphism preserves the representation character. The natural dihedral permutation character is determined by fixed vertices: nonidentity rotations fix none; for odd \(n\), each reflection fixes one; for even \(n\), reflections with even exponent fix two and those with odd exponent fix none. This yields the stated parity criterion. The affine basis permutation \(P_{a,c}|i\rangle=|ai+c\rangle\) proves sufficiency whenever \(2c\equiv b\pmod n\). Exact enumeration for small \(n\) was replayed successfully, but the proof is independent of enumeration.

## Originality
PASS. The anchor article itself states the full-automorphism quotient and a Fourier-basis implementation using \(2^{-1}\), while also treating even and dyadic \(n\). Focused searches for the exact article identifier, even-dihedral reflection-class obstructions, representation-normalizer aliases, and an index-two correction did not find a published correction or an implication-equivalent result. Standard dihedral parity and fixed-point facts are prior mathematics and are not claimed as new. The original contribution is the exact representation-specific normalizer image and its constructive realization.

## Value
PASS. The result changes a central structural classification from the full automorphism group to an index-two subgroup throughout the even family used for dyadic implementations. It also supplies the exact replacement theorem and implementers rather than merely pointing out that a modular inverse is undefined. This matters for identifying which abstract symmetries are physically realizable by unitary conjugation in the proposed code representation.

## Closest literature and limitations
The closest source is Bradshaw–LaBorde–Montero itself, especially its normalizer discussion around Eqs. (125)–(136). Grech–Kisielewicz records the classical fixed-point distinction between the two reflection types in the natural even-dihedral permutation action, but does not draw the quantum-code normalizer consequence. The claim is representation-specific and does not extend automatically to other faithful representations.

Self-review: passed. Independent audit: not yet performed.
