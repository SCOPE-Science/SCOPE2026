# Scientific review

## Correctness

PASS. The sampled intensity of a degree-at-most-\(d\) polynomial is an angular trigonometric polynomial of degree at most \(d\). Its \(2d\)-point DFT has one and only one alias, at harmonic \(d\). The highest Fourier coefficient has the common radial factor \(t^d\); the two rings supply two real projections with determinant \(-\sin(d\delta)\). Inverting these recovers both continuous-circle intensity functions, and a rational quotient invariant under nontrivial dilation proves global phase agreement. At resonance, the pair \(1\pm iz^d\) is a counterexample. Exact Gram eigenvalues prove the optimal offset. The standalone checker passed 9,639 deterministic assertions. Finite checks are not used as an infinite proof.

## Originality

PASS, subject to historical-priority risk. Pohl--Li--Boche's Theorem 7 uses an unbalanced \(2d+1\)/\(2d-1\) two-circle allocation. Chalendar--Partington's Theorem 2.16 uses complete-circle intensity information. Bodmann--Hammen's Theorem 2.3 uses intersecting rather than nested concentric circles. The balanced two-concentric-circle Nyquist alias creates an angular-rank obstruction absent from those exact hypotheses, and the displayed inversion resolves it with a complete iff criterion. Research-record searches for balanced \(2d\)-point rings, rotated Nyquist retrieval, and aliases revealed related but no implication-equivalent result. This does not certify literature completeness.

## Mathematical value

PASS. The result supplies a sharp deterministic geometric design criterion at a \(4d\)-sample budget known to be meaningful in complex polynomial phase retrieval. Both the failure set and the best angular displacement are exact; the latter minimizes the condition number of the only Fourier alias removal step. It is a natural completion of the comparison between full-circle rigidity and low-redundancy finite constructions, rather than a numerical or unmotivated special case.

## Scope and residual risks

Equal radii, irregular grids, analytic nonpolynomials and whole-reconstruction stability are not included. Priority is provisional. The reference comparison is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
