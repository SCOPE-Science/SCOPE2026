# Independent mathematical audit

## correctness

PASS

For any a,b>0, every V:C²→C⁴ isometry defines four rank-one effects E_st whose Bloch weights w_st sum to 1 and vectors sum to 0. The compressed numerical range is a translated ellipse with smaller singular value τ of real rows a h,b k. Grouping opposite effect pairs gives ||h+k||+||h−k||≤2. If τ is the smaller semiaxis then the Gram matrix G≽τ² diag(a^−2,b^−2); test on (1,±1) yields 2≥2τ√(a^−2+b^−2), hence τ≤ab/√(a²+b²). Explicit E_st=(I+s(b/r)σx+t(a/r)σz)/4 are rank one, sum to I, and give compressed (ab/r)(σx+iσz), square-zero with centered disk of radius ab/r. At equality the PSD slack G−τ²diag vanishes on spanning (1,±1), forcing h⊥k and norms b/r,a/r. Triangle-equality vectors then force opposite Bloch pairs and all weights 1/4; a qubit rotation fixes them, and row-Gram equality leaves only ambient independent diagonal phases. This proves all maximizers and the same centered disk. Finite rational checks are illustrative, not proof for continuum.

## originality

PASS

PASS best of knowledge after implication-level comparison. Busch–Heinosaari already prove the binary-qubit compatibility inequality ||h+k||+||h−k||≤2 used for the universal upper bound, and Sababheh Theorem 3.2 already identifies the positive-block defect with elliptical width. Neither gives the numerical optimization for FOUR rectangular spectral corners or the equality rigidity for all optimizing two-planes. The complete published Resultary three-spectral-point normal-compression incircle theorem was read and requires at most three distinct spectral points, a genuinely different case. The new mathematical content is exact δ2(D_ab)=2ab/√(a²+b²), centered disk uniqueness and diagonal-phase classification of all maximizers, not the borrowed compatibility or block-norm identity.

## value

PASS

The rectangular four-point normal spectrum is a minimal natural step beyond triangular three-point spectral compression. Knowing the exact largest minor ellipse semiaxis, its unique optimizing disk, and the full diagonal-phase orbit of attaining planes answers a concrete operator-geometric extremal and rigidity question; the positive-block defect is a useful computed corollary, explicitly credited to Sababheh. It is more than restating qubit compatibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
