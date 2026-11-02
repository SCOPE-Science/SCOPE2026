# Scientific review of the exact Gaussian Nyström deterioration probability

## Correctness — PASS

The finding specifies a strictly positive definite \(3\times3\) family, the Gaussian rank-two sketch and the source's unshifted preconditioner exactly. The rank-one Nyström residual gives the eigenpair geometry. Two exact active-plane trace/determinant identities and an indefinite difference show why condition-number comparison is equivalent to the displayed polynomial sign. That polynomial has one positive root, and the Haar-normal coordinate has explicit CDF \(\sqrt{t}\). Endpoints have probability zero. A direct dimensional argument checks minimality. The symbolic proof identities, rational witness and finite numerical regression tests succeeded. The numerical examples alone would not prove the all-parameter theorem.

## Originality — PASS (qualified)

The closest direct source is Frangella–Tropp–Udell, arXiv:2110.02820, where the Nyström preconditioner is defined and larger-rank performance bounds are derived. The analyzed statements do not give the sharp event probability \(\Pr(K_L>L)\) in this minimal spiked setting. Martinsson–Tropp §17.3 motivates approximate spectral preconditioning; Carson–Daužickaitė §3 gives finite-precision condition bounds and examples; Giraud–Gratton investigates sensitivity of spectral preconditioners. Those comparisons do not imply the exact Gaussian orientation threshold. Published-result similarity searches and recoverable prior mathematical finding records did not identify the same theorem, but search incompleteness and uncatalogued specialized preconditioning calculations remain genuine risks. Novelty does not attach to Gaussian rotational invariance, eigenvalue algebra, or the qualitative possibility of a poor approximate eigenspace.

## Value — PASS

The calculation quantifies a natural failure event for a widely used randomized linear-solver preconditioner, not an arbitrary matrix invariant. At the smallest nontrivial sketch rank, it gives a closed-form probability, a sharp large-condition-number tail, and a dimensional impossibility boundary. This sharp risk complements broad expected-case preconditioning results by identifying precisely how a rare, poorly aligned Gaussian sketch can be harmful. It does not claim a general randomized-algorithm performance theorem or worse PCG iteration counts.

## Residual limitations

Only the exact, positive-definite, three-dimensional one-spike problem at zero regularization is covered. Strong coverage in an uninspected specialized treatment would supersede the novelty claim. External independent audit and validation were not performed.

Self-review: passed. Independent audit: not yet performed.
