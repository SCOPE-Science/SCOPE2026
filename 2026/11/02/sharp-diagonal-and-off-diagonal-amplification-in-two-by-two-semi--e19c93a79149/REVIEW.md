# Scientific review

## Correctness

PASS. The spectral formula gives all projector branches. The two three-coordinate derivative rows have been differentiated explicitly, then optimized using inequalities valid for every \(c,s\ge0\), \(c^2+s^2=1\) and \(-1\le t\le1\). Integrating these bounds gives the global Lipschitz modulus. The determinant-zero affine-line case is handled separately for nonattainment. Two explicit rank-one boundary perturbations give the exact limiting lower bounds. `verify.py` passed 407 independent exact-rational and high-precision checks; its finite tests are not treated as the unrestricted proof.

## Originality

PASS, with residual publication-priority risk. Higham's nearest-semidefinite formula and Malick–Sendov's complete generalized-Jacobian framework are strongly relevant, but neither source states the sharp two-coordinate sensitivity split or analyzes nonattainment. The standard Lorentz-cone coordinate maximum norm cannot be substituted for the entrywise matrix maximum norm because the change of variables is not an isometry for those norms. The Šilhavý paper was assessable through its full bibliographic abstract but its full text was inaccessible; earlier unindexed equivalent calculations remain possible. The positive originality judgment is evidence-limited rather than a uniqueness certificate.

## Mathematical value

PASS. This is the complete sharp local-to-global coordinatewise stability classification in the first nontrivial dimension for semidefinite repair: diagonal errors can be magnified by 50%, off-diagonal errors by 12.5%, and both worst cases are unattained finite differences. These are material robustness boundaries for spectral eigenvalue clipping, not a mere restatement of the Hilbert-norm nonexpansiveness theorem. The diagonal phenomenon embeds into all higher dimensions, although exact larger-dimensional constants are not claimed.

## Scope and closest literature

The result concerns real \(2\times2\) symmetric input, Frobenius-nearest PSD output, and maximum absolute entry differences. The closest primary sources are Higham (1988), Malick–Sendov (2006), and Šilhavý (2015); the last presents a material access limitation. Earlier comparable endpoint analyses for the standard Lorentz cone have different coordinate norms.

Self-review: passed. Independent audit: not yet performed.
