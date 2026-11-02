# Independent mathematical audit

## correctness

PASS

The normalized arclength moments E cos=0, E sin=2/π, E cos²=1/2, Var sin=1/2-4/π² yield the exact symmetric reproducing kernel K=1+2cosθcosφ+((sinθ-m)(sinφ-m))/v. Symmetry yields equal L1 and L∞ norms, each equal to max_θ ∫|K|dφ/π. Reflecting φ about π/2 reduces F(θ) to a max over |1+(t-m)(s-m)/v| and 2√(1-t²)√(1-s²), t=sinθ. For 0≤t≤1/3 the positive branch on s≤m and the negative/b branch on s>m are nonincreasing; the positive s>m branch is dominated by b by concavity, with strict decrease for t>0. For 1/3≤t≤1 the Cauchy bound F²≤K(θ,θ), a strictly convex quadratic with both endpoint values <4, gives F<2, whereas an exact rational interval witness proves F(0)>2. Thus only θ=0,π maximize. At θ=0, the two interior kernel sign roots φ±=π-arctan(2π/D)±arccos(π²/R) allow exact integration to the displayed 2.048099271479... constant, attained by sign(K(0,·)). Independent 45-digit quadrature reproduced the algebraic formula and checked five interior evaluations. Full-circle finite cyclic Fourier projection is not the same Gram kernel.

## originality

PASS

The primary Fourier-extension literature treats half-range trigonometric approximation and projector stability, but its inspected full text does not provide the exact degree-one norm or global endpoint maximizer. Uniform kernel Lp bounds do not imply this sharp value. The published Resultary three-character cyclic full-circle projection has a distinct normalized Dirichlet kernel and norm (1/3+2√3/π); it does not dominate this continuous semicircle problem.

## value

PASS

Sharp worst-case error amplification for least-square affine restriction to a semicircular arc is a natural operator invariant directly relevant to stability of Fourier extension and geometry-induced conditioning. The fact that only boundary evaluation maximizes, and amplification exceeds two against a full-circle value about 1.436, is substantial rather than a routine finite sample norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
