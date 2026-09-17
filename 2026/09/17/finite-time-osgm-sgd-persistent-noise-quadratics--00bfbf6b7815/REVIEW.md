# Same-model review

## Verdict

**PASS (same-model review only).** Correctness, originality to the best of our
knowledge, and value were assessed separately. This is not independent
validation or peer review.

## Correctness audit

The proof was checked against the exact scalar OSGM-SGD update and against
sign, projection, and stopping-time edge cases.

1. **Hypergradient identity.** For \(f(x)=a x^2/2+C\) and stochastic gradient
   \(g=ax+B\),
   \[
   h'_{x,B}(p)=a\left(p-\frac{x}{ax+B}\right).
   \]
   With OSGM learning rate \(\eta=1/a\), projected online gradient descent gives
   \(p^+=\Pi_{[0,1/a]}(x/(ax+B))\). Under
   \(|ax|<b_{\min}\), the denominator is never zero.

2. **Invariant local basin.** The exact objective null step accepts only a point
   with no larger \(f\). Because \(f-f^\star=a x^2/2\), it never increases
   \(|x|\). Therefore \(|ax|<b_{\min}\) remains true until absorption.

3. **Reset step.** If \(x>0\) and \(B<0\), the local-basin condition implies
   \(ax+B<0\); every nonnegative trial stepsize moves weakly away from zero, so
   the null step keeps \(x\) and the scheduler projects to \(p^+=0\).
   The signs reverse for \(x<0\).

4. **Exact hit.** From \(p=0\), drawing an atom \(b\) with the same sign as
   \(x\) leaves the iterate fixed and sets \(p=x/(ax+b)\). Drawing the same
   atom again makes the next trial point exactly zero, which the null step
   accepts.

5. **Geometric tail.** For \(x>0\), the three-draw reset-and-hit event has
   probability \(q_-c_+\); for \(x<0\), it has probability \(q_+c_-\).
   These probabilities are state-independent lower bounds within the invariant
   basin. Conditioning successively on disjoint three-iteration blocks yields
   \(\Pr(T>3m)\le(1-q)^m\), and blockwise tail summation gives
   \(\mathbb ET\le3/q\).

6. **Absorption at zero.** At \(x=0\), the exact null step always retains zero.
   The subsequent scheduler update also sends the stepsize to zero.

7. **Finite-sum specialization.** Grouping equal offsets into atoms gives
   \(c_+\ge m_+/n^2\) and \(c_-\ge m_-/n^2\), hence
   \(q\ge m_+m_-/n^3\) for uniform component sampling.

8. **Fixed-step comparison.** The stated stationary mean-square error follows
   directly from the AR(1) recursion
   \(x_{k+1}=(1-a\alpha)x_k-\alpha B_k\) for \(0<\alpha<2/a\).

### Correctness limitations

The finite-time argument depends essentially on exact full-objective values,
atomic noise, the scalar equal-curvature model, the local basin, and the tuned
hypergradient learning rate. It does not establish finite-time absorption for
continuous noise or general smooth objectives.

## Originality audit

### Internal SCOPE overlap

Searches of the current SCOPE catalogue using combinations of `OSGM`,
`online scaling`, `hypergradient`, `persistent gradient noise`,
`non-vanishing noise`, `finite-time absorption`, and `quadratic` located no
existing record covering this claim. Recent repository changes were also
checked immediately before publication. Repository text search is not a proof
of semantic non-overlap, so the conclusion remains qualified.

### External literature checked

- **Zhang--Gao--Ye--Udell, arXiv:2609.11751v2 (2026).** The current full text
  was inspected. Algorithm 2 gives the OSGM-SGD null-step/hypergradient
  framework; Section 3 treats exact function values as a special case. Its
  gradient-norm condition controls stochastic error relative to the full
  gradient, while the conclusion explicitly leaves convergence with
  non-vanishing gradient noise open.
- **Gao--Chu--Ye--Udell, arXiv:2505.23081 (2025).** This supplies the
  deterministic OSGM foundations. No persistent-noise stochastic absorption
  theorem was located there.
- **Baydin et al., arXiv:1703.04782 / ICLR 2018.** This develops
  hypergradient learning-rate adaptation for stochastic optimizers. No theorem
  matching the reset-and-hit mechanism above was located.
- **Zhou--Mertikopoulos--Bambos--Boyd--Glynn,
  SIAM J. Optim. 30(1), 2020 / arXiv:1706.05681.** This is an important
  stronger-looking precedent: stochastic mirror descent can attain *sharp*
  minima in finite time almost surely even with persistent gradient noise.
  It does not imply the present theorem because a smooth strongly convex
  quadratic minimum is not sharp in their sense, and the mechanism here is
  adaptive hypergradient feedback plus discrete repeated atoms.
- The recent OSGM paper's related-work chain covering adaptive SGD,
  stochastic line searches, Polyak stepsizes, and hypergradient methods was
  followed with targeted searches for finite-time exact convergence,
  persistent/non-vanishing noise, discrete/atomic noise, and quadratic
  objectives. No matching statement was located.

### Equivalent-formulation and stronger-result check

The claim was also checked under the equivalent finite-sum formulation
\(f_i(x)=a x^2/2+b_i x+c_i\), under descriptions such as adaptive stochastic
stepsize, hypergradient descent, null-step stochastic optimization, and exact
finite-time hitting/absorption. The sharp-minimum mirror-descent theorem is
the closest located finite-time persistent-noise result, but its hypotheses do
not cover smooth quadratic minima.

The result is therefore assessed **PASS to the best of our knowledge** as a
special-case positive answer to the non-vanishing-noise question for
OSGM-SGD.

### Uninspected sources and residual risk

No specific inaccessible paper was identified as especially likely to contain
the same OSGM-SGD theorem. Residual risk remains from literature under older
learning-rate adaptation terminology and from unpublished or newly posted work
that search indexes may not yet expose.

## Value audit

The theorem gives an explicit mechanism by which persistent stochastic
gradient noise can help rather than obstruct exact convergence of an adaptive
method: one noise sign resets the learned stepsize, and repetition of an
opposite-sign atom calibrates and executes an exact hit. The geometric
three-step tail bound and finite-sum corollary make the mechanism quantitative.

Its value is primarily structural. It supplies a rigorous positive special
case for an open direction stated in a recent SOSGM paper and sharply
contrasts with the nonzero stationary error of constant-step SGD on the same
quadratic. The result is deliberately not presented as a general
non-vanishing-noise convergence theory.
