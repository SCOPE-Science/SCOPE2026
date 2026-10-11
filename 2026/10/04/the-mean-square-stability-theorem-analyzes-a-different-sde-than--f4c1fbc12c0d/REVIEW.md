# Independent mathematical audit

## correctness

PASS

The primary full text prints the original stochastic terms as \(\sigma_i(t,N_i)N_i\,dW_i\) in equations (2.1)--(2.2), with \(\sigma_i\) either constant or inverse-population. Section 4 instead replaces them by \(\sigma_i(t,N_i)(N_i-N_i^*)\,dW_i\) before applying the mean-square theorem. Centering the original equation leaves, respectively, constant terms \(\epsilon N_1^*\) or \(\epsilon\) and \(\delta N_2^*\) or \(\delta\), so the diffusion never vanishes at the deterministic positive equilibrium when both intensities are positive. Consequently that point is not a constant Itô equilibrium of the original model. Itô's formula at the deterministic point gives right derivative \(\|G(P^*)\|^2\) for the mean-square displacement. Fresh exact arithmetic at the source parameters reproduces \(N_1^*=101/150\), \(N_2^*=31/75\), and the four slopes \(0.0307962711\ldots,0.0427361111\ldots,0.0769,0.06496016\).

## originality

PASS

The source itself prints both incompatible equations but presents Section 4 as the mean-square stability analysis of systems (2.1)--(2.2) and later interprets Theorem 4.3 that way numerically. Current exact-title, DOI, correction, and model-switch searches found the source and bibliographic mirrors but no corrigendum or prior published diagnosis of this mismatch. General mean-square stability literature requires diffusion to vanish at a point equilibrium but does not identify this source-specific replacement or its four exact departure rates.

## value

PASS

The model switch invalidates the paper's principal interpretation that sufficiently small random immigration makes the deterministic positive point asymptotically mean-square stable. The exact short-time departure rates quantify the failure at the paper's own benchmark and sharply separate point stability from legitimate stationary-fluctuation questions, making this a substantive correction rather than a notational objection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
