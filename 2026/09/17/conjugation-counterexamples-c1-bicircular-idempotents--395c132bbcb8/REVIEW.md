# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The construction was checked after transporting \(C^1[0,1]\) isometrically to
\(\mathbb C\oplus_1 C[0,1]\) by \(f\mapsto(f(0),f')\).

For distinct \(\lambda,\mu\in\mathbb T\), the pointwise maps
\[
Q_\lambda z=\frac{\overline z-\mu z}{\lambda-\mu},\qquad
Q_\mu z=\frac{\lambda z-\overline z}{\lambda-\mu}
\]
satisfy
\[
\overline{Q_\lambda z}=\lambda Q_\lambda z,\qquad
\overline{Q_\mu z}=\mu Q_\mu z.
\]
Hence \(Q_\lambda\) and \(Q_\mu\) are the complementary real-linear
projections onto \(L_\lambda=\{z:\bar z=\lambda z\}\) and
\(L_\mu=\{z:\bar z=\mu z\}\).  This proves idempotence, orthogonality, and
the identity \(C=\lambda Q_\lambda+\mu Q_\mu\) without appealing to a
complex-linear spectral calculus.

The Form III pair
\[
P_1(a,g)=(a,Q_\lambda g),\qquad P_2(a,g)=(0,Q_\mu g)
\]
therefore satisfies all defining hypotheses and has associated surjective
isometry \((a,g)\mapsto(\lambda a,\bar g)\).  Non-bicircularity is not
inferred from a norm estimate: it is witnessed by an explicit nonzero
function annihilated by one allowed phase combination.  If
\(\bar u_\nu=\nu u_\nu\) and \(\rho=u_\lambda/u_\mu\), then for
\(f(t)=t(u_\lambda-u_\mu)\),
\[
(P_1+\rho P_2)f=0.
\]
Thus the counterexample is exact.

The Form IV variant applies the same two projections to both coordinates;
its associated map is \((a,g)\mapsto(\bar a,\bar g)\), and the same
zero-scalar test function proves non-bicircularity.

The phase correction in Forms I and II follows directly from the paper's
own equations (3.4) and (3.6): substituting
\(\phi^2=\mathrm{id}\) and \(\lambda_2=-\lambda_1\) leaves
\((\beta(t)\beta(\phi(t))-\lambda_1^2)f'(t)=0\).
This also passes the common-phase covariance check.

## Adversarial checks

The projections are nonzero and distinct: \(P_1\) acts as the identity on
the scalar coordinate, while \(P_2\) is nonzero on functions with
derivative in \(L_\mu\).  The cancellation witness has zero scalar
coordinate, so no scalar term can mask the failure of isometry.

The construction works for arbitrary distinct unit phases, not merely for
opposite phases.  In particular \((\lambda,\mu)=(1,i)\) has nonzero sum,
so the counterexample cannot be absorbed into the first alternative of the
preprint's abstract dichotomy.

No claim that an unconditional basis implies complementability, or any
other inheritance assertion, is used.

## Originality

Originality is assessed to the best of our knowledge.  Searches by the
preprint title, arXiv identifier, theorem terminology, conjugation,
real-linear generalized bi-circular idempotents, and synonymous
bicircular-projection language located no correction, comment, or
counterexample to arXiv:2609.18967v1.

The full arXiv HTML of v1 was inspected at Theorems 3.1--3.4 and their
proofs.  Theorem 3.3 explicitly concludes that every Form III GBCI family
is bi-circular, and Theorem 3.4 makes the analogous Form IV claim.  The
abstract also states the global alternative that either
\(\lambda_1+\lambda_2=0\) or the family is bi-circular.

The complete publicly available PDF of Kumar--Abu Baker--Botelho's
closely related analytic-space paper was inspected at its real-linearity
discussion and Theorem 3.3.  It contains a scalar real-linear GBCI example
and a similar Form III-to-BCI inference, but no \(C^1[0,1]\) construction
matching the all-phase counterexample above was found.

Botelho--Miura's 2019 corrigendum is highly relevant historical prior art
because it corrects an earlier GBCI classification on continuously
differentiable function spaces.  Its bibliographic record and abstract
were inspected; the publisher full text was not accessible here.  The
2026 preprint itself describes the 2018/2019 results as treating a
different norm determined by a compact connected set \(D\subset[0,1]^2\).
Because the full corrigendum was not inspected, an equivalent
conjugation mechanism there remains the principal residual originality
risk.  Even if such a mechanism appears there, the explicit contradiction
to the stated 2026 \(C^1\) theorem and its arbitrary-phase form would
still be a distinct correction claim.

## Value

The counterexample attacks a central structural conclusion rather than a
peripheral estimate.  It refutes Theorem 3.3, supplies the same obstruction
to Theorem 3.4, and, for nonopposite phases such as \(1\) and \(i\),
refutes the dichotomy stated in the abstract of arXiv:2609.18967v1.

The mechanism is reusable: a real conjugation carries a continuum of
real eigendirections indexed by the unit circle, so phase-adapted real
spectral projections exist for every pair of distinct unit phases.
This explains exactly why a complex-linear intuition about idempotent
spectral decompositions fails.

The independent phase check on Theorems 3.1 and 3.2 identifies a second,
algebraically separate defect and gives the corrected relation
\(\beta(t)\beta(\phi(t))=\lambda_1^2\).

## Source-access limitations

The full arXiv HTML of arXiv:2609.18967v1 and the complete publicly
available PDF of the related analytic-space manuscript were inspected.
For the 2019 Botelho--Miura corrigendum, the abstract and bibliographic
record were available but the publisher full text was not inspected.
That corrigendum is the inaccessible source most plausibly capable of
containing an equivalent older conjugation mechanism.

The current target is explicitly version 1.  A later revision can correct
the statements, so the claim should not be transferred automatically to
future versions.
