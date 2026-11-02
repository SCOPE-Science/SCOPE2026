# Review of three-task transient capacity

## Correctness — PASS

The four physical transition rates in the cited switch sum to \(u=2k\cosh(\theta+fx/2)\) and \(v=2k\cosh(\theta-fx/2)\). Solving the forward equation with a common initial occupation yields a memory term \(\delta e^{-\lambda T}\) and an input-antisymmetric response. Their exact minima at the control interval endpoints and origin give the four-labeling count. Optimizing the minimum of the constant and copy margins over the preparation imbalance gives a two-branch envelope. Strict monotonicity of the branches proves uniqueness of the finite optimal readout; the root equation proves the weak-driving expansion. All hypotheses, strict versus weak inequalities, deterministic endpoints and the positive-time restriction were checked. The independent rate-construction checker passes 12,931 finite assertions; finite tests are not used as proofs of the universal claims.

## Originality — PASS, qualified

Aslyamov and Esposito, *Physical limits to stochastic classifiers*, arXiv:2610.20481v1, § Application and Appendix C, derive the same switch for **uniform** initial preparation; their resulting terminal occupations are exactly input-antisymmetric, so the constant labelings do not occur and their optimized margin concerns copying or inversion at fixed time. The present nonuniform-preparation model breaks this antisymmetry, adds a natural third labeling and solves a distinct joint preparation/time minimax problem. Floyd et al., arXiv:2409.05827v1, analyze steady-state network expressivity, which cannot produce this decaying initial-memory term or its optimal readout. The standard two-state relaxation formula is not claimed as novel. Related mathematical-record searches did not return an equivalent task-count/optimal-time theorem; the remaining possibility of an older implicit transient-classification specialization is a priority risk, not a proven absence.

## Value — PASS

For the recent physical-classifier question, the result specifies exactly how a finite preparation resource changes the number of binary tasks from two to three, gives a sharp positive-margin design limit for all preparations and positive readout times, proves the deterministic-preparation boundary and unique finite optimum, and supplies a generally noninteger weak-drive correction to its optimal performance. The count, optimization and singular boundary law are natural constraints in the stated physical system, not arbitrary data slices.

## Limitations and comparison boundary

The result does not classify arbitrary stochastic networks, initializations dependent on the input, feedback, other threshold choices, single-shot errors or energetic preparation costs. The primary model and uniform-preparation result are established prior art. General Markov relaxation is elementary. The finite verification script does not certify universal mathematics, and literature-wide priority remains unverified.

Self-review: passed. Independent audit: not yet performed.
