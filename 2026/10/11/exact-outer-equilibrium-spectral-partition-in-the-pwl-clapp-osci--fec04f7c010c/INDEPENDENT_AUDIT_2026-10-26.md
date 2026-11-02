# Independent mathematical audit

## correctness

PASS

Reconstructed from actual PWL Case II vector field (Petrzela equations (6),(8),(10),(11)): at an outer equilibrium with C1=C2=C3=L=y11=1, y12=1/10 and transconductance derivative a, Jacobian rows are (-1,-1/10,0,1),(-a,0,0,-1),(0,0,0,1),(-1,1,-1,0). Direct symbolic det(λI−J) gives q_a(λ)=λ^4+λ^3+(3−a/10)λ²+(a+21/10)λ−a/10 exactly. Independent SymPy discriminant agrees identically with P(a)/50000; Δ2=(9−11a)/10>0 and Δ3=−(110a²+131a−189)/100. Thus Routh first column (1,1,Δ2,Δ3/Δ2,−a/10) yields unstable dimension 2 below a_H and 0 above. At a_H, q factors into (λ²+ω²)(λ²+λ+c) with ω²=A3>0, c>0, proving a simple imaginary pair and stable complement. Independent exact rational polynomial root-isolation and Sturm/count_roots computed exactly two simple discriminant zeros inside [-10,-1], alpha∈(-4.871964812,-4.871964811), beta∈(-1.009024345,-1.009024344); root counts of q at -10,-4,-2,-1 respectively (positive,negative)=(2,0),(0,0),(0,0),(0,2). These and no further collisions establish all four regimes; double coalescence sign follows continuous eigenvalues and simple discriminant crossing. Endpoints -10 and -1 included; alpha/a_H/beta boundaries separately described. The polynomial and assumptions concern local linear spectra only, no nonlinear periodic or chaotic claims. Reconstructed full 8-entry Git tree identity exactly, and inspected RESULT.md/verify.py independently of VERIFY_OK log.

## originality

PASS

Qualified best-of-knowledge PASS: Petrzela (Mathematics 2022, DOI 10.3390/math10111868) prints the Case II model and the outer-characteristic substitution and explicitly describes only approximate spectral transitions near a=-2 and a=-1. Its actually inspected Sections 2.1, 2.2, and 3 contain neither the computed discriminant P nor the earlier positive-real to complex collision a≈-4.871965; targeted published Resultary search returned only the audited finding as exact same-claim match. Existing Case I cubic-Clapp work proves invariant-measure moments, not this Case II quartic-root partition. This is a narrow but motivated new explicit calculation, with residual risk of unindexed self-review analysis. No claim of absolute bibliographic priority.

## value

PASS

A piecewise-linear circuit oscillator is a motivated natural system whose local outer-equilibrium spectra were used in its defining article to discuss transitions while trajectories repeatedly visit outer regions. The exact partition gives all three algebraic boundaries, including a previously omitted positive-real to unstable-focus transition at a≈-4.872 well inside the scanned interval, and separates node-focus collisions at alpha/beta from the unique change of unstable dimension at a_H≈-2.035. This corrects/refines a concrete mathematical phase portrait rather than an arbitrary parameter slice or mere extra decimal digits. It is an exact, finite-parameter full classification, although the proof uses standard Routh/Sturm algebra and supplies no new general spectral theorem or nonlinear chaos mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
