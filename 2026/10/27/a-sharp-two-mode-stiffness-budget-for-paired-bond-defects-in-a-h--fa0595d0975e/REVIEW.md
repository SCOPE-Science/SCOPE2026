# Independent mathematical audit

## correctness

PASS

For H=L+αg₀g₀*+βg_dg_d*, applying the two differences to the free resolvent at λ=2+e^t+e^(−t) gives diagonal B=2q/(1−q), off-diagonal magnitude C=q^d(1+q)/(1−q), q=e^(−t), including the adjacent case d=1. Resolvent monotonicity is strict on the independent bond vectors. The larger Birman–Schwinger eigenvalue diverges at λ↓4, while dividing the determinant αβ(B+C)(B−C) by the larger eigenvalue gives smaller edge limit 2αβ(2d−1)/(α+β). The eigenvalues both tend to zero at infinity and cross 1 with the stated count, excluding equality. The band-edge resonance can be explicitly constructed: after staggering u_j=(−1)^j v_j, L v=c₀(e₀+e₁)+c_d(e_d+e_{d+1}). Bounded tails require c_d=−c₀. Set c₀=1; the slopes are 0 on the tails, −1 at bonds 0 and d, and −2 on the bonds strictly between. Then (v₀+v₁)−(v_d+v_{d+1})=2(2d−1); choosing the additive constant imposes v₀+v₁=1/α and v_d+v_{d+1}=−1/β exactly on the stated equality. The tails differ by 2d, so the solution is not square summable. Positivity and the free-tail recurrence exclude all other eigenmodes at or below the band top. At fixed S the square root in the 2×2 eigenvalue formula strictly decreases in P=αβ; ordering the crossings proves both opposite unique frequency extrema and the strict budget threshold. For equal strengths, B−C=2Σ_{j=1}^{d−1}q^j+q^d=(2d−1)−d²t+O_d(t²); the implicit root and λ−4=t²+O(t⁴) give precisely the coefficient (2d−1)^4/d^4. The frozen checker was inspected, not run; independently shot the displacement recurrence in eight representative cases including equality using /workspace/branches/independent_replay.py. These sign scans are corroboration, not completeness certificates.

## originality

PASS

Best-of-knowledge pass for the original joint count, fixed summed excess stiffness design and edge-law result, subject to significant named historical risk. The later arbitrary-bond theorem demonstrably covers the count and gives a secular matrix from which the remaining pair formulas are recoverable, but explicitly identifies the very same pair count as earlier work rather than a new result of its own. The later lighter-mass paper is spectrally equivalent under a nonlinear parameter map, not an unrelated example; its stated fixed mass-deficit constraint is different. The comparison separates demonstrable mathematical coverage from evidence of historical priority. The exact historical sources that could supply an independent antecedent are unconfirmed, not ruled out.

## value

PASS

Fixed total excess stiffness is a concrete physical constraint and differs from holding a summed mass deficit fixed. A strict and globally sharp design threshold, the opposite allocation extrema for the two branches, and the explicit detuning law together answer a natural two-defect question, including the adjacent case, without approximating the interaction. The claim is not valuable merely because it evaluates a known count for one parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
