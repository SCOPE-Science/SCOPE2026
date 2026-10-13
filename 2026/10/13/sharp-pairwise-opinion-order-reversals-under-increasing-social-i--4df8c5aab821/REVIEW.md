# Scientific review

## Correctness — PASS

The equilibrium equation is obtained from the symmetric fixed-intrinsic-opinion averaging rule; connectedness makes the Laplacian's zero eigenvalue simple. Removing the constant spectral mode yields a proper rational function with at most \(n-1\) distinct positive-eigenvalue poles and therefore a numerator of degree at most \(n-2\). Distinct simple eigenvalues on the unweighted path and nonzero first-edge eigenmode differences yield an invertible residue assignment; any prescribed positive roots are realized through proper partial fractions and positive affine rescaling of intrinsic opinions. Finally, the spectral expansion of centered expressed opinions proves strictly negative variance derivative for each nonconstant initial vector. An exact SymPy checker independently verifies rational identities on paths with three through six vertices, including the explicit five-vertex formula. Computations are not used to prove the arbitrary-order assertion. The statement excludes identically tied comparisons as a degenerate case, and all parameter and boundary restrictions are explicit.

## Originality — PASS, with residual risk

The closest underlying model source, Bindel–Kleinberg–Oren (arXiv:1203.2973), was inspected in its mathematical model, theorem statements, price-of-anarchy analysis and network-design discussion; no all-order pairwise reversal bound or arbitrary prescribed-reversal construction appeared. Dandekar–Goel–Lee (arXiv:1209.5998) analyze a global edgewise squared-disagreement index under opinion updates, not reversals of **pairwise ordering over a parameterized equilibrium family**. Boudourides (arXiv:2602.08704) studies response-based broadcaster/receiver ranking across susceptibility profiles and network families, not the sharp crossing count of two coordinates as one common edge strength varies. Direct searches of published mathematical findings and relevant social-influence literature found no logically dominating result. No claim of novelty follows merely from missing search hits: a general positive-definite resolvent or spectral interpolation theorem could encompass this specific sharp statement, and independent evaluation remains outstanding.

## Value — PASS

The precise \(n-2\) limit and its attainable arbitrary crossing schedule provide an exact complexity benchmark for comparative statics of stubborn-opinion equilibria. The same construction proves that any fixed pair can change signed ordering repeatedly even while a standard population-level disagreement measure contracts strictly. This is a substantive distinction between a globally monotone stability metric and local pairwise order statistics, not an arbitrary single-network numeric observation. The result makes no empirical claim about actual populations or agents.

## Relationship to prior work and limitations

The rational Laplacian-resolvent representation and spectral decay are established analytical tools. Novelty is restricted to the stated sharp universal pairwise-order crossing bound with path attainability at freely prescribed strengths and the simultaneous global-variance law. Relevant reviewed sources and remaining literature coverage risks are in the structured audit. Scope excludes directed networks, heterogeneous susceptibility changes, nonlinear influence, binary-only opinions, and real-time evolution.

Self-review: passed. Independent audit: not yet performed.
