# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The proof reduces the low-dimensional objective to the active coordinates and evaluates the two Haar moments needed by the smoothness descent inequality exactly. For a Haar rank-d projector Q, the diagonal second moment follows from the classical beta law for the squared length of a fixed vector projected onto a random d-dimensional subspace. Idempotence Q^2=Q then determines the common off-diagonal squared moment. Rotational invariance in the active s-dimensional space forces E[(RQR^T)^2] to be scalar, giving the displayed θ exactly.

Substitution into the L-smooth descent lemma gives a concave quadratic in the constant stepsize. Its maximizer is alpha=1/(Lθ), and telescoping yields the stationarity theorem without concentration events or dimension restrictions on d. The PL corollary follows directly from the same one-step inequality. For s=1 and g(y)=Ly^2/2, the descent calculation becomes an exact equality and the expected objective ratio is a scalar quadratic whose unique minimizer and minimum agree with the claimed alpha and contraction factor.

Exact rational verification checks the closed-form moments, the source-regime comparison at (n,s,d)=(1000,512,32), the full-dimensional consistency cases, and the rank-one sharpness identity.

## Originality

The primary source arXiv:2609.18416v1 was inspected through its sparse-function setup, Theorem 6, and the complete proof of that theorem. Theorem 6 uses a high-probability singular-value event and a bad-event split to control the quadratic term; it assumes max{1,2 log(2n^2/(9s))} <= d <= s/16, takes alpha=n/(18sL), and obtains coefficient 36Ls/d. The exact Haar second-moment identity and the unrestricted optimized coefficient in this record do not appear there.

The original SSD work of Kozak--Becker--Doostan--Tenorio was checked as the principal prior source for Haar stochastic subspace descent. Its generic theory gives ambient-dimension rates and does not state the low-intrinsic-dimension second-moment refinement here. Searches also covered stochastic subspace descent with intrinsic/effective dimension, random-direction optimization for low-dimensional objectives, exact Haar/random-projector moments in optimization, random embeddings, and precise random-projection analyses.

Frankl--Maehara's beta-distribution geometry is relevant to the classical random-projection moment and is not claimed as new. Derezinski--Liang--Liao--Mahoney derive precise random-projection expressions for sketching applications including randomized Newton, but their setting and optimization consequence are different from classical Haar SSD on f(x)=g(Rx). Random-embedding global-optimization literature for low effective dimension was also inspected and addresses solving random embedded subproblems rather than the iterative Haar projected-gradient recursion analyzed here.

No source located in these searches states the exact θ-based sparse-SSD stationarity theorem, the removal of the September 2026 theorem's d restrictions, the >=16x comparison throughout its stated regime, or the rank-one sharpness result. Originality is therefore asserted only to the best of our knowledge.

The 1990 Frankl--Maehara article was identified through bibliographic and DOI records, but its full text was not inspected. This creates little originality risk because the beta-law fact is explicitly treated as prior art rather than a claimed contribution. No inaccessible source was identified as especially likely to contain the paper-specific SSD refinement.

## Value

The source paper presents its sparse classical-SSD theorem as, to its knowledge, the first such theoretical analysis. Replacing its concentration bound by the exact Haar second moment yields a substantially stronger result: no logarithmic lower bound or d<=s/16 restriction, a one-dimensional-subspace guarantee, and at least a factor-16 smaller stationarity coefficient everywhere the source theorem applies. The rank-one quadratic establishes that the resulting constant stepsize and PL contraction are not merely artifacts of a loose proof.

## Scope and limitations

The result does not criticize the correctness of the source theorem; it strictly sharpens it. It does not analyze the source paper's persistence-of-memory method, finite-difference errors, noisy gradients, changing active subspaces, non-Haar sketches, or high-probability trajectories. Its guarantee is in expectation and assumes global L-smoothness and a fixed orthonormal active subspace.
