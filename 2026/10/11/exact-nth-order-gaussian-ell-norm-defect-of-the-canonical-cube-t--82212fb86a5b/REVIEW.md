# Independent mathematical audit

## correctness

PASS

Every ±1 sign halfspace reduces exactly to ||x||_1≤n(1−ε), so gauge=max(||x||∞,||x||_1/[n(1−ε)]). For half-normal Y_i=|X_i|, M=maxY_i, S=sumY_i, defect E[(S/[n(1−ε)]−M)_+]. Condition on the unique a.s. maximizing coordinate m, use gaps z_j=m−Y_j for other n−1 coordinates and exact support Σz<nεm. For ε<1/n upper bound z_j<m automatically, so no missed boundary. Change variables z_j=εm w_j gives ε^n m^n times fixed simplex domain; dominated convergence for each fixed n is justified by bounded f and integrable m^n f(m). Simplex integral n^n/n!, half-normal moment (2/π)^(n/2)·(1/2)·(2/n)^((n+1)/2) Γ((n+1)/2), giving c_n=2^(n−1/2)n^((n−1)/2)Γ((n+1)/2)/(n!π^(n/2)), positive. The support geometry, normalization including maximizing-index factor n and gauge denominator n, and fixed-dimension limits were independently checked. Packaged `verify.py` checks moment arithmetic only, not an infinite proof.

## originality

PASS

Böröczky–Fodor–Hug use exactly the same all-sign-vertex truncation as a sharpness witness and prove only upper-order O(ε^n) for the Gaussian ell-norm defect. Their full available treatment does not give an asymptotic equality, positive exact leading coefficient or its Gamma expression. Earlier nonsymmetric simplex stability is a different extremizer. The present exact first response is best-of-knowledge not entailed by a one-sided upper bound.

## value

PASS

A canonical truncation is the motivating explicit witness for sharpness of the stability exponent n in a recent origin-symmetric cube theorem. A positive exact dimension-dependent first variation refines one-sided upper-order behavior into the sharp contact asymptotic and supplies a precise benchmark for comparing other perturbations. The object and invariant are mathematically preselected by the source theorem, not arbitrary small numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
