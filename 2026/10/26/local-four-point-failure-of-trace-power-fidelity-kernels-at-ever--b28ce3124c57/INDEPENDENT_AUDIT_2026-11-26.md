# Independent mathematical audit

## correctness

PASS

The Finding itself is correct. Independently, write c=1−q² and F(x)=cosh(r arcosh x). The two-dimensional product spectra, after extracting their common geometric mean, give x=1, 1/c, (1+q²)/c for opposite, adjacent, and identical states. These x are equally spaced. The alternating eigenvalue is the corresponding second difference of F times 2(c/d²)^r. F is strictly concave for 0<r<1: at x=cosh t, F′=r sinh(rt)/sinh t decreases because z coth z is strictly increasing. Its expansion F(1+v)=1+r²v+r²(r²−1)v²/6+O(v³) gives exactly the claimed quartic term. The other nonconstant eigenvalues are strictly positive by strict AM–GM; the inactive block affects only the positive constant eigenvalue. The frozen resolvent proof also checks: writing V=s²+2s+c², the product polynomials have quotient (V²−4q⁴s²)/V², giving the stated logarithmic derivative and single crossing. Fresh matrix spectra (18 cases, replay: python3 /workspace/evidence/review_checks.py 4) agreed to 1.0e−15; finite corroboration only. The frozen RESULT.md line 87 overclaims every strictly positive common spectrum, which includes the all-scalar spectrum where the only state is I/d and the Gram matrix is constant. repairs/4/RESULT.md corrects the quantifier to the stated Pauli-corner spectra and clarifies the pure-state overlap; the proof and Finding are unchanged and the three axes are assessed for that corrected text.

## originality

PASS

Pure-state nonpositivity, including the pure Pauli square, is already known; the supported contribution is the strict faithful-square obstruction for every interior q and every fractional r, with exact inertia and a quartic small-q law. The strongest compared statements do not give those features.

## value

PASS

This determines whether the three-point positivity phenomenon survives locally at four points even with full rank and a common spectrum. Exact inertia for the entire faithful square family and the first nonzero q⁴ defect are substantive stability information beyond a numerical example or continuation near pure states. The repair removes an unsupported generalization without diluting that contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
