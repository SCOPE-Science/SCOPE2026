# Independent mathematical audit

## correctness

PASS

The publisher PDF confirms Eq. (3), the cosine in Eq. (4) and in the hazard numerator, the raw-moment kernel, and the log-cosine likelihood term. For α,δ>0 the angle t=θ(y) decreases from π/2 to 0; if z=cos t, then d(ze^(1−z))/dz=e^(1−z)(1−z), and dz/dt=−sin t. This gives exactly the sine factor, with the claimed sign and prefactor. The endpoint CDF values are 0 and 1, and changing variables u=1−cos t gives unit mass ∫₀¹u e^u du. For the printed kernel use s=sin t: its mass is ∫₀¹x(s)e^x(s) ds with x(s)=1−√(1−s²). It is positive and strictly less than e(1−π/4)<1. Independent composite quadrature gives 0.3449927969472616 and 0.3449927969472641 on 4096 and 8192 panels (python /workspace/checks/independent_formula_checks.py); the non-normalization proof does not rely on numerical error estimates. The derivative-based correction does not change an inversion directly from the CDF. The supplied checker was inspected, not executed; reported software and numerical tables were not reconstructed.

## originality

PASS

The general weighted sine-G density mechanically implies the correct specialized factor; deriving a new generator or a new density for the same CDF is not credited as original. The supported distinct claim is the diagnosis of the published specialization and its consequences: the explicit mass of the erroneous formula and the resulting mismatches in the printed statistical procedures. No checked distinct source makes that diagnosis for this model.

## value

PASS

The printed mass deficit is about 65.5%, so this is not a harmless identity or an isolated typographical correction. Renormalizing the kernel by its constant mass would produce a different model: the ratio to the correct density is cot θ(y) before scaling, not a constant. Thus the CDF-based sampler and the printed likelihood/hazard need not describe the same law. The correction identifies which formulas a reproducing analyst needs to change without assuming how the published numerical results were computed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
