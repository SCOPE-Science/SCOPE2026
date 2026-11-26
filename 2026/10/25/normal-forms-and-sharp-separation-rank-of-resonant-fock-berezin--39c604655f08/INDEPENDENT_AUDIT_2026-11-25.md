# Independent mathematical audit

## correctness

PASS

With A=ā and w independent, the Gaussian moment generator is ∫exp(s t+q t̄)dμ(t)=exp(sq), as follows from the moments ∫t^i t̄^j dμ=δ_ij i!. On the polynomial amplitude the shifted generator gives e^κ exp(D), D=∂z∂w+b∂z+A∂w. At resonance, exp(D)−I=D times a polynomial in D with invertible constant term on each degree filtration. Thus fixedness is exactly DR=0. A polynomial or entire identity on w=z̄ can be treated as a two-variable identity: substitute z=x+iy, w=x−iy and apply the identity theorem in each variable successively. For u=Az−bw and v=z/b, the derivatives give D=(1−∂u)∂v−κ∂u². Inverting the first factor terminates on each polynomial. Coefficient comparison in v gives the unique solution with initial data h, exp(vQ)h, and v^j Q^j lowers total degree by at least j when j≥1. The coefficient matrix in z,w is therefore supported on and below the total degree cutoff, with anti-diagonal c binom(d,j)A^j(−b)^(d−j), nowhere zero since κ≠0. Reversing columns gives full rank d+1. Multiplication by the separable exponential does not change rank; truncating the Taylor-coefficient matrix of any entire product expansion makes the rank lower bound apply beyond polynomials. Grouping rows realizes the bound. The degree and rank filtrations follow, with the zero element included; rank zero gives the zero subspace. Independent bounded replay uses h=u^d for d=0,…,8, builds the finite sum ∑v^j Q^j h/j! through j=⌊d/2⌋, substitutes the coordinates, differentiates by D and checks the determinant. In particular A=1, b=2πi, d=2 gives (z−2πi w)^2+2z with D=0 and determinant −16iπ³. The cited checks and the inspected SymPy script are finite; the proof establishes all degrees only at the stated one nonzero mixed frequency.

## originality

PASS

The earlier Berezin identity and anti-diagonal obstruction are substantive prior coverage of ingredients; the rank consequence follows by extending that coefficient argument and is not independently treated as a new method. The supported distinct contribution is an explicit all-degree polynomial parametrization and degree/rank filtration for one resonant frequency, not the qualitative Laplacian characterization or the earlier two-product rigidity theorem. The 2015 full text remains an access and priority risk, not negative evidence.

## value

PASS

The constructive classification solves a natural resonant kernel, gives an explicit degree-preserving basis, and tells exactly which fixed symbols can be represented with a prescribed number of entire products. This goes beyond the prior use of the coefficient obstruction to exclude higher degrees from a specific two-product construction. No operator-boundedness or multi-frequency applications are inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
