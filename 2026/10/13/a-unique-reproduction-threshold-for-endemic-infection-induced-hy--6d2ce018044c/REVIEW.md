# Scientific review

## Correctness — PASS

The exact infected-equilibrium identity gives \(S(I)=\delta I/[p(1-e^{-\beta I})]\); it parametrizes all positive fixed points without an unproved branch assumption. Strict monotonicity of \(r(I)\) proves the equilibrium existence and uniqueness range. The identity \(b(S+I-\bar S)=b(1-w)I-L(I)\) and the strictly decreasing derivative of \(L\) prove the unique-crossing classification, including boundary equality cases. The worked example has an exact factored crossing equation and three strictly positive Schur margins; the bundled standard-library checker returned `VERIFY_OK` on fixed-point residuals, identities and example local stability. Numerical checks supplement, not replace, the proof. No claim is made for global dynamics or cycles.

## Originality — PASS

The source [1] was inspected in full at its equations, Theorem 5 and Appendix B.4–B.6. Its published sufficient inequalities do not imply a complete, sharp reproduction-rate threshold, nor the locally stable crossing that violates both sufficient inequalities. Related Jaramillo et al. [2] concern the same underlying modelling tradition; its abstract describes discrete-time existence and simulation, not a once-only \(r\) crossing classification. The closely related article [2] was not available for whole-document comparison, leaving a genuine residual risk rather than proof of absence. Additional epidemic and hydra literature and public semantic-result searches did not identify an equivalent or stronger theorem for these exact equations and varying \(r\).

## Value — PASS

The source defines the infection-induced hydra problem and gives only a sufficient parameter region. Here the sharp complete classification determines when endemic size exceeds disease-free size for every reproductive capacity and identifies a one-way switch, a structural property not readable from simulation or the earlier bound. The explicitly stable crossing shows the threshold matters on a dynamically realizable local equilibrium branch. This is an extension of the motivated biological comparison, not an arbitrary slice or an uninformative sign check.

## Closest literature and limitations

The closest source is [1], especially Theorem 5 and Appendix B.6. A related older study [2] could be inspected only at abstract level, so unrecognized equivalent results remain a risk. A distinct 2025 overcompensation/hormesis treatment studies continuous-time equations. The present result concerns fixed-point sizes, not cycles, global attractors or field prediction. The checker is deterministic and reproducible but not an external certification.

Self-review: passed. Independent audit: not yet performed.
