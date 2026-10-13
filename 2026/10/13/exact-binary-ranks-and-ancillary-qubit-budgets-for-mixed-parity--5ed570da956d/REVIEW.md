# Scientific review

## Correctness — PASS

The asserted domain has at least one even and one odd coordinate. The adjacency operator over \(\mathbb F_2\) is a sum of all-ones coordinate operators plus \((d\bmod2)I\). On odd factors the all-ones operator is diagonalizable with dimensions \(1\) and \(q_i-1\); on even factors it is a rank-one differential plus \(q_i-2\) zero blocks. Contractible tensor summands yield \(\dim\ker D=(Q+H)/2\). Parity extraction with \(\prod_{i\in O}(q_i-1+z)\) produces the other factor. Lemmas 4.1–4.2 of Riera--Parker--Stănică turn the exact binary rank into the minimum quantum append cost for fully oriented edges. The direct adjacency-matrix construction and exact elimination checked 1,034 mixed-parity cases (1,222 cases including comparison boundaries). The infinite result follows from the proof, not the computational range.

## Originality — PASS with specific residual risk

Fish--Key--Mwambene (2009, Proposition 1) already give the exact binary rank for homogeneous Hamming graphs of any alphabet parity; that is not claimed as new. The heterogeneous mixed-parity formula is a different quantified statement and is not implied merely by substituting one common alphabet in the homogeneous formula. Riera--Parker--Stănică supply the general append-rank identity, not the rank of these graphs. The related 2023 Cartesian-product coding paper's indexed page-ten discussion says rank is not provided directly by the Cartesian product, and its visible claims emphasize conditional LCD properties. Its complete text could not be read, so equivalent or more general coverage remains possible; that risk is not presented as resolved. Searches for rectangular Hamming box ranks, modular Cartesian clique ranks, and mixed-graph append parameters did not identify the exact general formula.

## Value — PASS

An exact ancilla budget is a natural finite-dimensional resource invariant for an infinite family of mixed-graph stabilizer networks. The arbitrary combination of even and odd coordinate alphabets forces interaction between diagonalizable and nilpotent mod-two blocks; the dimension of the nilpotent homology contributes a correction not visible from the ordinary eigenvalue list. The theorem completely classifies all mixed-parity Cartesian clique boxes and yields exact resource costs independently of edge orientation, without prescribing arbitrary graph-size cutoffs. It does not claim a gate-count improvement or a solution beyond the stated stabilizer extension model.

## Closest literature and limitations

The 2009 homogeneous rank formula is pre-existing. The 2019 Hamming coding paper reuses that homogeneous framework. The 2021 graph-state theorem is a general conversion from rank to ancillary resources. The 2023 product-code paper is a plausible unexhausted comparison because its author-hosted PDF was not retrievable in this session. Its reported RLCD criteria are not applicable to an even clique factor, whose binary adjacency is invertible but whose reflexive adjacency has rank one. Inaccessible full text is a residual novelty risk, not proof of novelty. Numerical graph tests are finite and only corroborate the analytical identity.

Self-review: passed. Independent audit: not yet performed.
