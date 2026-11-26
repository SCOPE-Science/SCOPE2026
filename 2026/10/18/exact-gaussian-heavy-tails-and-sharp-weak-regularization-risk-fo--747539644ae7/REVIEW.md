# Independent mathematical audit

## correctness

PASS

For R=r1 and D=r0−r1 the two actual oracle calls give y1=1+D+2R and y0−y1=−R; the unrestricted minimizer yields Z=y1+R²/D. The affine noise transform has determinant one in absolute value. Its D variance is σ²B and regression gives R|D=0 with mean −δ(δ+2)/B and variance σ²/B. Independently, T P(|R²/D|>T) integrates T times the joint density over |d|<r²/T; domination follows from 2r² sup_d f(d,r)≤C r² f_R(r) by nondegenerate conditional Gaussianity. The linear Gaussian y1 is negligible by the tail sandwich at (1±ε)T. This gives 2hM₂ and the positive-moment cutoff from the tail integral. The two ridge minimizers give the singular terms R²D/(D²+aλ), a=1 or 2; squaring and setting d=√(aλ)u gives (π/2)hM₄/√a on the √λ scale since f_D(d)E[R⁴|D=d] is bounded and continuous. The rest has uniformly bounded L² norm, so mixed terms vanish by Cauchy–Schwarz. Both outputs are polynomially bounded for fixed λ>0. The σ=0 affine check gives Z=q²−q²=0. The frozen verifier was read, not run: it checks rational substitutions and finite quadrature, not the limiting claims, which follow analytically.

## originality

PASS

Credit the existing Gaussian-pole mechanism, the centered ridge, and the closely related exact fixed-site tail and weak-ridge laws. The surviving distinction is the actual two-call Anderson trajectory (the second site is the first noisy image), with explicit conditional-square and conditional-fourth-moment constants for that adaptive trajectory and the two specified penalties. The strongest inspected fixed-site exact laws do not specialize to this setup.

## value

PASS

The first genuinely accelerated iterate of a strict affine contraction is a natural stability baseline, not a chosen rare path. Arbitrarily small fixed fresh noise changes exact deterministic recovery into a nonintegrable output, and explicit weak-ridge risks quantify how preservation of finite moments fails as ridge is removed. The constants are useful to compare precise penalty conventions; they are not an optimal tuning rule, joint zero-noise asymptotic, or long-run stability guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
