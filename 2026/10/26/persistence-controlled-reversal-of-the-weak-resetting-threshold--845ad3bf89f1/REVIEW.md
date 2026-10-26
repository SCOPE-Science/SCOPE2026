# Scientific review

## Correctness

**PASS.** The claim concerns the one-sided reset-rate derivative at zero and the first-order active-amplitude displacement of its simple passive zero. The renewal formula reduces the reset response to unreset first and second moments. Two explicit inhomogeneous Dirichlet–Neumann resolvent problems follow by differentiating the killed OU–Brownian backward generator. Their Green solution, exact passive factorization, and sequential persistence/fast-relaxation limits establish both the coefficient and its sign reversal. Girsanov with exponentially controlled killed survival justifies local moment differentiation; no finite experiment is substituted for an infinite-limit proof. `verify.py` independently checks 905 deterministic identities and numerical consistency conditions.

## Originality

**PASS under self-review, with residual priority risk.** The directly motivating 2026 Georgiou–Bressloff–Bertrand article explicitly treats fixed-velocity resetting through simulations (Section 3.4 and Figure 9), whereas its analytic expansion uses a Gaussian reset-velocity law. Approximate linear activity dependence, general renewal formulas, and the passive critical starting location are already known. The new scientific assertion is the exact deterministic-velocity first-order coefficient for the reflecting–absorbing active OU model and its analytically forced sign reversal as relaxation varies. The 2016 Pal–Reuveni general restart result does not compute this model-specific coefficient; Baouche–Kurzthaler study a 2D active Brownian wall problem, and Shankari–Sahoo study free OU transport rather than absorbing interval search. Broader perturbative Green-function theory might implicitly yield this specialization, so independent priority assessment is still needed.

## Value

**PASS.** A directly identified analytical gap is the dependence of optimal-reset onset on a fixed reinitialized propulsion direction. The sign reversal reveals that initial outward propulsion can either enlarge or shrink the helpful-resetting region depending on persistence; it makes a falsifiable prediction that is not captured by the general coefficient-of-variation restart criterion. The exact coefficient permits parameter calibration without re-running rare first-passage simulations. It does not claim global finite-reset optimality or finite-activity control.

## Closest literature and limits

Primary comparison: Georgiou–Bressloff–Bertrand, arXiv:2609.21124v1, Sections 2, 3.2, 3.4 and Appendix; general restart: Pal–Reuveni, arXiv:1607.06048; orientation-dependent active Brownian resetting: Baouche–Kurzthaler, DOI:10.1039/D5SM00340G; unconstrained active OU transport: Shankari–Sahoo, arXiv:2509.18515. The finite-interval absorbing–reflecting boundary conditions, complete velocity reinitialization, weak active amplitude, and only locally identified resetting threshold are essential. Numerical root location does not establish uniqueness in relaxation rate.

Self-review: passed. Independent audit: not yet performed.
