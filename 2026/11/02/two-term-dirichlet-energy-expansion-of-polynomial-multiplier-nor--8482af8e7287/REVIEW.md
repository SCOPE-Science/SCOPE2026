# Independent mathematical audit

## correctness

PASS

In canonical orthonormal monomials e_n=sqrt(c_n(a))z^n, c_n=(a)_n/n!, multiplication is a banded weighted forward shift. Splitting e_0 from n>=1 gives block [[p0,0],[a^-1/2 v(a),B(a)]], with v_j=p_j sqrt(a/c_j). Expansion a/c_j=j(1-aH_{j-1}+O(a²)) yields ||v||²=D-a sum jH|p_j|². For any fixed polynomial degree the ratios c_n/c_(n+j) converge uniformly for n>=1, so B(a)->B0 with bounded norm O(a). Schur complement of M_p* M_p above ||B||² shows top eigenvalue λ=D/a+O(1) and λ=D/a+|p0|²-sum jH|p_j|² + ||B0* v0||²/D+O(a). Exact B0* v0 has n-th entry n^-1/2 sum_{m=n}^d m p_m conj(p_{m-n}), yielding C. Independent finite multiplier matrices confirmed C=-2 for p=z², C=0 for p=1+z² and a nontrivial complex polynomial, with residual error decreasing with a. The infinite conclusion follows from uniform band estimates, not finite sections.

## originality

PASS

The degree-one case is already implied by Monsalve-López–Seco 2025 spectral theorem and is expressly disclaimed as new. Inspected primary paper Section 7(b) describes higher degree d>=2 as a prospective extension rather than providing this explicit all-fixed-degree a->0 two-term norm expansion. Fu–Guo–Yan 2024 establish model/context, but not the cited finite correction. An abstract rank-one singular perturbation theorem would provide methodology but not necessarily polynomial coefficient formula; priority risk remains.

## value

PASS

Natural singular degeneration of reproducing kernel analytic Hilbert spaces: exact leading term identifies classical polynomial Dirichlet energy, while harmonic-number/correlation correction distinguishes polynomials sharing energy (z² vs 1+z²). Uniform fixed-degree formula for arbitrary complex coefficients is a meaningful explicit operator-norm invariant, not merely known linear case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
