# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS. The proof starts only from the source paper's exact phase parametrization
\[
\tau_{k,n}(M)=\frac{2\pi n-\theta_k(M)}{\omega_k(M)},
\qquad
\mu_{k,n}(M)=\frac{(-\log M)\omega_k(M)}{2\pi n-\theta_k(M)}.
\]
For fixed \((k,M)\), strict decrease in the branch index is immediate because the denominator increases by \(2\pi\). Strict ordering of compact-branch maxima follows by evaluating the earlier envelope at a maximizer of the later one. The \(1/n\) asymptotic is uniform because the phase lifts are bounded on compact intervals. The fixed-small-\(\mu\) proliferation result is an intermediate-value argument between an interior \(M_0<1\), where the branch value is positive, and \(M=1\), where the factor \(-\log M\) vanishes. The count distinguishes labelled imaginary-root branches from distinct parameter values and explicitly allows double-Hopf coincidences.

Adversarial checks were made against the main hidden assumptions: positivity of the phase denominator, compact attainment of the envelope maximum, bounded phase lifts, persistence of frequency branches, and the distinction between a purely imaginary spectral point and a nonlinear Hopf bifurcation. These assumptions are stated in the result rather than silently inferred.

## Originality

PASS, to the best of our knowledge. The source paper, published 12 June 2026, explicitly defines the Hopf branches, introduces \(\mu_{\max}^j\), conjectures their ordering, states Conjecture 1 for the exact number of Hopf points, and describes unbounded growth in the number of Hopf bifurcations as \(\mu\to0\) as a numerical/structural suggestion. Searches by the exact title, DOI 10.1007/s00285-026-02420-3, author combination, “Conjecture 1,” “Hopf points,” “growth rate,” “unbounded,” and equivalent branch-accumulation language found the original article and bibliographic mirrors but no later correction or source-specific proof of the envelope ordering or harmonic asymptotic. A current bibliographic index reports zero citations for the article.

The general phase condition for retarded delay equations, imaginary-axis root calculations, and elementary \(1/n\) expansions are not claimed as new. The originality claim is limited to the theorem extracted for this source model and to separating the automatically provable envelope/accumulation statements from the stronger exact-count conjecture.

No inaccessible paper was identified as especially likely to overturn this source-specific originality claim. The broader delay-bifurcation literature is extensive, so residual risk remains that a general theorem could imply a similar asymptotic after translation; no such result was found in the targeted searches.

## Value

PASS. The source paper's multi-Hopf geometry is one of its principal dynamical conclusions, but the higher-branch ordering and small-growth accumulation are left conjectural/numerical. The result gives a short exact proof of the envelope ordering, identifies the sharp harmonic scale \(\mu_{\max}^n\sim C/n\), and converts the qualitative “unbounded as \(\mu\to0\)” observation into a quantitative lower-bound mechanism. It also prevents overclaiming by showing precisely what remains necessary for the paper's stronger exact \(2k\)-point Conjecture 1.

## Limitations retained

The result is spectral, not a complete nonlinear Hopf theorem. The fixed-small-growth count assumes continuous persistence of the relevant frequency branches to \(M=1\). The source's displayed persistence window is numerical and is not independently interval-certified here. Exact two-intersection geometry of every joined branch is not proved, so the full Conjecture 1 remains open.
