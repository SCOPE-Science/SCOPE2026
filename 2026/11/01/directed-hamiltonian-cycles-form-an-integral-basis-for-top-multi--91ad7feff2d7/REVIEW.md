# Scientific review

## Correctness — PASS

For a digraph on \(n\) vertices, maximal \((n-2)\)-faces of its multipath complex are directed Hamiltonian paths. Their \((n-3)\)-dimensional ridges have at most two top completions. Two completions exist exactly when the two joining arcs close a unique directed Hamiltonian cycle. As a result, the top boundary matrix splits into singleton columns (whose coefficients must vanish in the kernel) and disjoint blocks each equal to the top boundary of a formal \((n-1)\)-simplex's boundary sphere. Every block has one primitive integral boundary generator, and no degree \(n-1\) chains exist. Equivariance follows from simplicial orientation signs; the bidirected-wheel dihedral action is free and transitive on its \(2m\) cycles. A dependency-free checker separately corroborates signed boundaries, ridge completions, exact finite-field ranks, and symmetry on exhaustive small digraphs. The argument is integral and applies to disconnected and cyclic inputs.

## Originality — PASS on inspected evidence

The earliest selected motivating primary paper is the 2022 multipath-homotopy work (arXiv:2208.04656), which computes special graph families rather than this all-digraph top-chain decomposition. The prior cycle-free chessboard paper (arXiv:0710.5252) proves connectivity and related results; its inspected parts do not state this Hamiltonian-cycle integral top basis. The 2026 polygon study (arXiv:2601.05670) computes full homology only for bidirected polygonal graphs and therefore cannot imply the theorem for arbitrary digraphs. Previously recorded complete-bidirected-graph and bidirected-cycle cases are specializations, not a general implication. Searches for the Hamiltonian-cycle formulation, cycle-free chessboard aliases, the top-homology criterion, and the signed equivariant generalization disclosed no covering statement. Residual risk: equivalent results might occur unindexed or implicitly in older chain-complex work; originality is a best-knowledge assessment, not independently certified.

## Mathematical value — PASS

The theorem gives a canonical primitive **integral** basis of a natural topological invariant for *every* finite directed graph and characterizes directed Hamiltonicity by its nonvanishing. Unlike a mere Euler-characteristic identity, it identifies generators, quantifies exactly which top chains survive, and resolves arbitrary automorphism actions over the integers. The bidirected-wheel example yields a regular dihedral representation, not just an unspecified rank. This does not yield a polynomial-time way to compute Hamiltonicity or settle any lower-dimensional homology.

## Scope and independent status

Only top reduced homology and its automorphism module are established; the complex need not be pure or shellable, and lower homology is unrestricted. The finite checker corroborates but cannot replace the proof, and bibliography can have omissions.

Self-review: passed. Independent audit: not yet performed.
