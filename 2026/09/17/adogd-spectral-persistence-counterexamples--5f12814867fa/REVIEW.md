# Same-model review

## Verdict

**PASS (same-model review only).** Correctness, originality to the best of our
knowledge, and value were assessed separately. This is not independent
validation or peer review.

## Correctness audit

The algebra was checked directly against equations (9), (10), (30), (35), and
(36) and the hypotheses of Lemma 4 and Theorem 8 in the current arXiv v1.

### Theorem 8 counterexample

For \(\Lambda=\operatorname{diag}(\mu,L)\) and
\(\xi_0=(u,v)^\top\) with \(uv\ne0\),
\[
L_1^2=\frac{\mu^4u^2+L^4v^2}{\mu^2u^2+L^2v^2},
\]
so \(r=L_1\in(\mu,L)\) and \(\alpha_1=1/r\).

If \(\alpha_0=1/L\), the maximal mode is exactly zero from \(\xi_1\) onward.
Every subsequent local curvature is \(\mu\), hence the running estimators become
\((\widehat\mu,\widehat L)=(\mu,r)\) and
\(\alpha_k=2/(\mu+r)\) for \(k\ge2\). The surviving scalar factor
\((r-\mu)/(r+\mu)\) is nonzero and has magnitude below one, so the infinite
trajectory is well-defined. Because \(r<L\), its limiting stepsize is strictly
larger than \(2/(\mu+L)\).

The \(\alpha_0=1/\mu\) construction is symmetric:
\((\widehat\mu,\widehat L)=(r,L)\) for \(k\ge2\), so
\(\alpha_k=2/(r+L)<2/(\mu+L)\). Both constructions satisfy the theorem's stated
initial nonzero-coordinate condition.

### Lemma 4 counterexample

For \(\Lambda=\operatorname{diag}(1,2)\),
\(\xi_0=(1,1)^\top\), and
\(\alpha_k=(k+3)^{-2}\), every spectral coordinate stays nonzero and the
stepsizes lie uniformly below \(\alpha^\star=2/3\) by a fixed margin. However
\(\sum_k\alpha_k<\infty\), so both coordinate products converge to positive
limits. Substitution into the exact local-curvature formula yields an interior
limit in \((1,2)\), not \(\mu=1\). This directly invalidates the lower branch
of Lemma 4 as stated.

### Repair of the varying-stepsize argument

For a higher eigenvalue \(\lambda>\mu\), the relative one-step factor
\[
q_\lambda(\alpha)
=\frac{|1-\alpha\lambda|}{|1-\alpha\mu|}
\]
satisfies \(q_\lambda(\alpha)<1\) below
\(\alpha^\star\). On a fixed upper-margin interval,
\(-\log q_\lambda(\alpha)/\alpha\) has positive infimum after continuously
extending it at zero. Therefore \(\sum_k\alpha_k=\infty\) forces the relative
product to zero. This supplies the missing implication in the source proof.

### Repaired AdOGD theorem

If the endpoint eigenspace projections are initially nonzero and the seed is
not \(1/\mu\) or \(1/L\), then \(L_1\in(\mu,L)\). Since \(L_1\) remains in the
history of the running min and max,
\[
1/L<\alpha_k<1/\mu,\qquad k\ge1.
\]
Endpoint modes therefore persist forever. In either hypothetical case
\(\widehat\alpha<\alpha^\star\) or
\(\widehat\alpha>\alpha^\star\), eventual separation from
\(\alpha^\star\) plus the preceding strict interval gives a uniform geometric
relative-mode contraction. This makes \(L_k\to\mu\) in the first case and
\(L_k\to L\) in the second, producing exactly the contradictions intended by
the source proof. The repaired conclusion follows.

The repeated-eigenvalue case is covered because the entire endpoint eigenspace
is multiplied by the same scalar at each gradient step; nonzero endpoint
projection is the relevant invariant quantity.

### Edge cases checked

- The result assumes the nontrivial condition \(\mu<L\). If \(\mu=L\), there is
  only one spectral value and the endpoint distinction disappears.
- In the exact counterexamples, no denominator defining \(L_k\) vanishes:
  the surviving coordinate remains nonzero and every later stepsize is
  positive.
- Interior eigendirections may be annihilated under the repaired theorem; this
  does not affect the endpoint-dominance argument.
- The finite-horizon near-annihilation statement uses only continuity over a
  fixed finite number of well-defined updates and does not claim failure of
  eventual convergence for generic seeds.

## Originality audit

### Internal overlap

The current SCOPE catalogue and recent default-branch contents were checked by
the source identifier `2608.03546`, `AdOGD`, the paper title, adaptive
curvature estimation, endpoint spectral annihilation, and equivalent
optimal-stepsize terminology. No existing record covering this correction was
located. Repository search can be incomplete or semantically miss equivalent
wording, so this is not treated as a proof of non-overlap.

### External literature checked

- **Wang et al., arXiv:2608.03546v1.** The theorem statements, update equations,
  Lemma 4 proof, Theorem 8 proof, numerical discussion, and current arXiv
  version history were inspected. The record lists only v1, submitted
  4 August 2026.
- **23rd IFAC World Congress public program.** The paper is listed there and
  its abstract repeats the claim that the proposed adaptive rule converges to
  the optimal constant stepsize.
- **Public indexing and review pages for the paper.** Searches by exact title,
  authors, `AdOGD`, Theorem 8, counterexample, correction, and erratum did not
  locate a correction. Available summaries repeat the theorem rather than flag
  the endpoint-annihilation or summable-step issues.
- **Related adaptive-gradient and Barzilai--Borwein literature.** The source
  paper's main local-curvature references and targeted searches under
  spectral/secant-curvature terminology did not reveal the specific two
  counterexamples or the repaired endpoint-persistence theorem.

### Equivalent-formulation check

The counterexample was searched under reciprocal-eigenvalue steps,
eigencomponent/eigenmode annihilation, loss of spectral observability, secant
curvature, running min/max curvature estimates, and adaptive quadratic
stepsizes. No matching correction to this specific theorem was located.

### Uninspected source and residual risk

A theorem-level final IFAC proceedings version, if distinct from the current
arXiv v1, was not located in searchable full text. Only the public conference
program was inspected. Such a version could already contain revised
hypotheses, so the claim is specifically about the current arXiv v1 and
originality remains qualified.

## Value audit

The source paper's main theorem is an asymptotic optimal-stepsize identification
claim. The first counterexample identifies a precise mechanism that invalidates
that claim under its written assumptions: an initial reciprocal-eigenvalue step
removes the very endpoint mode that later curvature estimates need to observe.

The second counterexample isolates an independent mathematical error in the
varying-stepsize lemma: pointwise contraction ratios do not imply decay of their
infinite product. The proposed repairs separate the two missing ingredients:
endpoint spectral persistence for AdOGD and sufficient cumulative step mass for
the lower-side curvature lemma.

The result is useful beyond a single numerical counterexample because it gives
closed-form families, identifies the exact proof failures, and supplies a
strictly weaker corrected AdOGD hypothesis involving only the two endpoint
eigenspaces.
