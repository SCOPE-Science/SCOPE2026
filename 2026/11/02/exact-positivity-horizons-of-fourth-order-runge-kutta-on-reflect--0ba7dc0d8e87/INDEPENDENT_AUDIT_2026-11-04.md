# Independent mathematical audit

## correctness

PASS

PASS: For symmetric reflecting path generator Q_n and classical RK4 step T_n(z)=sum_{k=0}^4 z^k Q_n^k/k!, setting P=I+Q_n/2 stochastic yields polynomial coefficients nonnegative for z<=1/2; this proves a uniform all-n positive interval. For distance-three vertices the exact unique-route walk count gives (T_n)_{i,i+3}=z³(4-z sum_{4 vertices} degrees)/24, so sharp ceilings are 2/3 for n4, 4/7 for n5, 1/2 for n≥6, with negative entry thereafter. Small n=2,3 reduce to monotonic cubic root obstructions (1.392646781702..., .928431187802...); n4,n5 remaining entry types have explicitly positive polynomials at the endpoints and monotonic cubic factors. The RK4 scalar polynomial is strictly positive on nonpositive spectrum, securing diagonal positivity. Independently reconstructed exact rational matrices for n=2..10 and checked thresholds and beyond endpoint; no finite-size extrapolation is needed for n≥6.

## originality

PASS

PASS qualified: General SSP and positivity theory (Horváth 1998/2005, Gottlieb et al) has universal bounds and knows classical RK4 is not unconditionally positivity preserving, but does not give the complete reflecting symmetric path endpoint classification in inspected material. Blanes–Iserles–Macnamara 2021/2022 analyze Laplacian integrators and RK4 context, not this exact array. Two-state value is already covered by an earlier directed two-cycle result and is included solely for complete all-size statement. The new all-size degree-sum rigidity plus n3–5 exceptions appear absent from examined sources. Specialized 2026 heat-scheme full text inaccessible, residual priority risk.

## value

PASS

PASS: Complete exact positivity-step classification, including several finite-size exceptions and proof that classical RK4 offers no positivity-step gain over forward Euler from six vertices onward, is a motivated numerical-analysis question with a genuinely sharp graph-geometry mechanism. Not a trivial application of universal SSP coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
