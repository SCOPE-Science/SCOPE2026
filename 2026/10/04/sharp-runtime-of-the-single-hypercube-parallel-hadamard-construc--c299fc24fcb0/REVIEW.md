# Same-model review

## Correctness
PASS. The proof reconstructs the normalized hypercube propagator, forces all diagonally correctable times from entry magnitudes, factors the Hadamard-to-propagator phase ratio using the Hamming-distance identity, proves uniqueness of the diagonal factors up to scalar rotations, and converts any loop-singleton sequence into an accumulated-time arc. The exact shortest arcs through two, three, or four consecutive fourth roots yield the lower bound, and explicit masks attain it. The finite verifier corroborates the phase algebra and schedules but is not used as an infinite proof.

## Originality
PASS. The closest source is Herrman--Wong, arXiv:2106.06015, which supplies the same normalized hypercube interval and loop-singleton phase construction, including the \(5\pi/2\) two-qubit example and the general phase durations. It gives an upper bound, not a lower-bound or optimality theorem. Wong's isolated-vertex work supplies the phase primitive; Adisa--Wong's length-three result concerns a different gate-synthesis architecture; Chan's cube/complex-Hadamard work concerns uniform-mixing existence and classification. Targeted searches found no equivalent piecewise elapsed-time minimum.

Residual risk: an equivalent diagonal phase-synthesis bound may exist under control-theoretic terminology not recovered by the searches. This does not create a decisive unresolved comparison with the inspected sources.

## Value
PASS. Exact optimality is mathematically and operationally motivated by the source's explicit objective of shortening dynamic-walk evolution. The result proves that the known two-qubit timing and the general four-phase correction cost are not artifacts of one phase assignment: within the stated architecture, they are forced. The low-dimensional transition at \(n=1,2,3\) also identifies the precise point at which all four phase classes become unavoidable.

## Closest literature and limitations
The closest literature is Herrman--Wong (arXiv:2106.06015), Wong (arXiv:1908.00507), Adisa--Wong (arXiv:2108.01055), and Chan (DOI 10.5802/alco.112). The claim is not global gate-synthesis optimality. Multiple non-diagonal intervals, mixed loop-and-edge graphs, weighted generators, ancillary vertices, and other normalizations remain outside scope.

Same-model review: passed. Independent audit: not yet performed.
