# Independent mathematical audit

## correctness

PASS

For fixed b>0 the exact clockwise polar equations follow by writing d=z−Sat(z) and the vector field as (aI+bJ)z−((1+a)I+bJ)d. For initial excess η comparable to a^(2/3), bootstrap in a radial band |r−(1+η)|≤η/2: the angular speed is b+O_b(η); the defect is O(η) and vanishes outside four caps of width O(√η); the integrated radial variation is O_b(a+η^(3/2))=O_b(a)=o(η), strictly closing the band for a full turn. Freezing r costs O_b(a√η) in the clipping integral. Each parabolic cap integrates to (4√2/3)η^(3/2), and the skew projections contain an additional factor O(√η), so they contribute at most O_b(η²) to that integral. The displacement is (2πa−(16√2/3)η^(3/2))/b+O_b(a^(4/3)), with opposing signs at the stated section endpoints. At its zero, η=C_*a^(2/3)+O_b(a), and the bootstrap also gives the uniform radial estimate. At each switching root the normal velocity is of order b√η with nonzero sign, since the tangential coordinate is of order √η and the residual normal term at the line is only O(a). Moving cap boundaries cost at most O_b(a/√η), and the first-order time integral gives saturated time 8√(2η)/b+O_b(a^(2/3)). The continuous vector field gives identity saltation; Liouville's determinant uses divergence 2a or a−1 and equals the section derivative because start and return both have normal speed −b. The derivative is strictly between zero and one in the annulus. Any periodic trajectory crossing the positive ray has only one crossing per least period: by uniqueness it is a simple closed curve, and along that ray all transverse crossings have the same orientation since dy/dt=−bS(x)<0. Thus the fixed point proves the claimed local cycle uniqueness and the determinant gives the stated multiplier. The reciprocal angular-speed expansion gives the positive clipping correction (16√2/3b)η^(3/2) in physical time, and the fixed-point relation gives (2π/b)a+O_b(a^(4/3)). At a=0, the origin is an equilibrium and the positive-radius circles up to radius one are periodic; d/dt of Σ∫₀^{z_i} S(u)du equals −Σ(|z_i|−1)_+, so no periodic trajectory can spend time outside the unsaturated square. The frozen verify.py was inspected, not run; its documented replay with NumPy/SciPy checks four finite cases, ratios and integrated divergence, not the uniform remainders.

## originality

PASS

Best of current knowledge: the exact model, critical annulus and qualitative onset are prior, and the fractional exponents occur in other systems. Credit is limited to the quantitative four-cap theorem for this model, including uniform amplitude and the two physical dynamical coefficients. Reasonable retrieval left named source-access risks.

## value

PASS

The system is a standard motivated two-cell saturation oscillator. The result quantifies its singular onset at a finite-radius annulus, distinguishing gain-independent leading radial selection from coupling-dependent relaxation and giving the physical rather than angular-period correction. Those three linked coefficients describe the amplitude, timing and loss of hyperbolicity in a regime where a smooth small-orbit Hopf approximation would give the wrong mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
