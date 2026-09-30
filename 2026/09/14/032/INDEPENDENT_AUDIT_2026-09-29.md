# Independent audit — 2026-09-29

Record: `2026/09/14/032`  
Audited source tree: `a3bedc576472d683d6673bf1c69202de0fb588b1`  
Disposition: **passed**

## Correctness

The one-point disproof at a=2/5 is correct. In the even/odd periodic and antiperiodic sectors, the stated Ritz values and residual variances follow from direct trigonometric expansion. With ||V||_infty<=4/5, the one-sided Temple bounds give the even-periodic edge at least 5917/1425>83/20 and the even-antiperiodic edge at least 19/20, while the paired odd-sector Ritz bounds are at most 19/5 and 4/5. The resulting second gap above zero has width at least 83/20-19/5=7/20>1/5. The archived Fraction-only checker reproduces all numerical inequalities, and an independent finite Fourier truncation gives a second-gap width about 0.418, consistent with but not used in the proof.

## Originality

Two-term Hill/Whittaker-Hill gap behavior and asymptotics are established subjects. The audited contribution is the specific small-amplitude exact rational certificate at a=2/5 that defeats the proposed interval for a_c. It is not a new general gap theorem, and the audit makes no priority claim from failure to find this exact numerical counterexample in the checked literature.

## Scientific value

A rigorous single-parameter counterexample is sufficient to settle the admitted threshold claim and does so with elementary spectral bounds. It does not determine the actual threshold or the global gap-width function.

## Limitations

- The argument is a single-point disproof and does not compute the exact threshold a_c or establish monotonicity of w_2(a).
- The numerical Fourier diagonalization is only a sanity check; the rigorous conclusion uses the rational Ritz/Temple inequalities.
- The RESULT and METADATA refer to output/artifacts/verify_disproof.py, while the audited repository file is artifacts/verify_disproof.py.
- Originality is assessed conservatively against established two-term Hill-operator literature.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/032
- https://arxiv.org/abs/math-ph/0509034
- https://doi.org/10.1016/j.jat.2005.03.004
- https://arxiv.org/abs/2007.09575
