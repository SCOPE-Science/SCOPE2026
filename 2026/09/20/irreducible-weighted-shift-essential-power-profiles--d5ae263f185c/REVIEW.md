# Review: Exact norm and essential-norm power profiles for irreducible weighted shifts

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The theorem was checked against the main failure modes in weighted-shift realization arguments.

For a strictly positive submultiplicative sequence \((a_n)\) with \(a_0=1\), the ratios \(\beta_k=a_{k+1}/a_k\) are well defined and satisfy \(\beta_k\le a_1\). Every contiguous product inside the ratio sequence telescopes to \(a_{j+n}/a_j\le a_n\). Thus every finite prefix block already respects all required sliding-product bounds.

The bridge induction is genuinely global rather than levelwise. When a new positive bridge and a new prefix block are appended, every new window that is not wholly contained in the old word or the new prefix contains the new bridge exactly once. Only finitely many such windows exist at that stage. Since all \(a_n\) and all pre-existing weights are positive, one can choose the bridge strictly positive and small enough to satisfy every one of those inequalities simultaneously. Each finite window of the limiting sequence appears at some finite stage, so no later extension can invalidate its bound. Imposing the length-one bound also keeps every weight at most \(a_1\), hence the shift is bounded.

For each fixed \(n\), arbitrarily far-out prefix blocks begin with the product \(\beta_0\cdots\beta_{n-1}=a_n\). This proves \(\|W^n\|=a_n\), not merely an upper estimate. It also supplies a sequence of pairwise orthogonal basis vectors on which \(W^n\) has norm exactly \(a_n\). Compact operators send this weakly null orthonormal sequence to zero in norm, so no compact perturbation can lower the norm below \(a_n\). Hence \(\|W^n\|_e=a_n\).

Irreducibility was checked separately. Because every weight is nonzero, \(\ker W^*=\operatorname{span}\{e_0\}\). A reducing projection commutes with \(W\) and \(W^*\), so it sends \(e_0\) either to \(0\) or to \(e_0\). Since repeated applications of \(W\) to \(e_0\) generate every basis vector up to nonzero scalar multiples, the projection is respectively \(0\) or \(I\).

For the rate corollary, if \((\rho_n)\) is positive and nonincreasing then \(a_n=\rho_n^n\) is submultiplicative because \(\rho_{m+n}\le\rho_m,\rho_n\). The two Gelfand formulas therefore give the same prescribed root sequence and limiting ordinary/essential spectral radius. When the limit is zero, the Calkin spectral radius is zero, so the operator is Riesz; positivity of every essential power norm simultaneously rules out power compactness.

## Originality

The underlying ordinary-norm characterization is known and was explicitly separated from the proposed contribution. Halmos, Solution 92, attributes to L. J. Wallen the result that a sequence \((p_n)\) with \(p_0=1\) is a power-norm sequence exactly when it is submultiplicative, and records a weighted-shift realization via ratio weights. The present theorem does not claim this part as new.

The proposed strengthening asks for the same prescribed sequence to survive unchanged in the Calkin norm while the realizing shift remains irreducible. Targeted searches combined terminology for power norms, essential norms, Calkin norms, submultiplicative sequences, prescribed power profiles, irreducible weighted shifts, spectral-radius rates and Riesz weighted shifts. No source stating the simultaneous equality \(\|W^n\|=\|W^n\|_e=a_n\) for every strictly positive submultiplicative sequence, or the exact-rate corollary, was located.

Shields's 1974 survey is a particularly relevant classical source and was identified bibliographically, but it was not exhaustively inspected page by page. Wallen's original source was not identified beyond Halmos's explicit attribution. Because the recurrent-prefix bridge argument is elementary, an equivalent statement may have been recorded using different language for essential norms, limit behavior of sliding products, or recurrent weighted shifts. Originality is therefore assessed only to the best of our knowledge.

Young's 1980 note explicitly observes that the spectral-radius formula can converge arbitrarily slowly in general. The present corollary is more structured: it realizes every positive nonincreasing rate exactly, simultaneously in operator and essential norm, by an irreducible unilateral weighted shift. Bourdon and Shapiro provide a standard Calkin-algebra characterization of Riesz operators that verifies the final specialization when the prescribed rate tends to zero.

## Value

The theorem gives a sharp positive-profile characterization within a restrictive operator class: strict positivity is exactly what is needed for the ratio construction and is also necessary for an injective irreducible weighted shift to have nonzero power norms. The conclusion upgrades a classical operator-norm realization to an exact essential-norm realization without resorting to an infinite direct sum, which would destroy irreducibility.

The rate corollary supplies a reusable family of examples with exact control over both spectral-radius formulas. In the zero-limit case, it separates Rieszness sharply from power compactness inside irreducible weighted shifts: every positive power remains noncompact even though its essential norm decays at any prescribed positive nonincreasing root rate.

## Verdict

Correctness: PASS.  
Originality: PASS, to the best of our knowledge.  
Value: PASS.

Same-model review: passed. Independent audit: not yet performed.
