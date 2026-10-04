# Same-model review

## Correctness
PASS. The proof reconstructs the complete spectrum from the edge ODE and both continuity–Kirchhoff conditions. The only positive wave numbers are \(m\pi/\ell\). For each positive level, the eigenspace is exactly the direct sum of one symmetric cosine direction and the \(N-1\)-dimensional sine coefficient hyperplane. The edgewise squared-supremum sum over an orthonormal basis is shown to be basis independent and equal to \(2/\ell\) by a projector-trace calculation. The zero mode is handled separately. `verify.py` independently replays the finite linear-algebra identities and truncated heat-sum equalities and prints `VERIFY_OK`.

## Originality
PASS. Harrell–Maltsev define the relevant envelope and conjecture the strict domination, but their inspected Section 2 gives only a coarse general bound and a regular-tetrahedron example; targeted full-text searches show no pumpkin/parallel-edge specialization. Kennedy–Rohleder treat equilateral pumpkins and explicitly describe the first positive eigenspace, but their inspected full PDF is about hot spots, contains no heat-kernel discussion, and does not sum the all-level edgewise \(L^\infty\) weights. Published-record searches under pumpkin/dipole/parallel-edge and heat-envelope/theta/spectral-function aliases found no equivalent or stronger claim. Residual risk remains that an equivalent identity is hidden under unrelated terminology.

## Value
PASS. The exact identity resolves a specific conjectural heat-envelope comparison on a natural infinite family and identifies the sharp slack, rather than merely bounding it. The cancellation of all positive-frequency terms despite high eigenspace multiplicity is structurally informative and provides a clean benchmark for less symmetric metric graphs.

## Closest literature and limitations
The closest source by mathematical implication is Harrell–Maltsev, arXiv:1803.01186v2, equations (5)–(6) and Remark 2.1; it poses the inequality that is proved here only for equilateral pumpkins. The closest same-object source is Kennedy–Rohleder, arXiv:2003.14335v4, Example 3.3 and Proposition 4.2; it supplies first-eigenspace structure for a different question. The present theorem does not cover unequal pumpkins, potentials, nonstandard vertex conditions, full pointwise heat kernels, or infinite graphs.

Same-model review: passed. Independent audit: not yet performed.
