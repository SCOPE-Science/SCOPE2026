# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/finite-jet-log-subharmonic-mean-inequality--2e6c49bb3292`  
Assigned and audited source tree: `2cccee6830d148077bdde6d527460f4a7d3ab5e3`  
Repository/branch: `SCOPE-Science/SCOPE2026` / `main`  
Current RESULT.md blob: `bc380014ec3d5abf2675ad17045c7313ee08f2ae`  
Disposition: **passed**

## Correctness

**independently_supported**. The finite-jet expansion is correct. Radial integration gives the ball/sphere factor n/(n+d) for a homogeneous term of degree d. If the first nonharmonic Taylor term occurs before degree 2m, it is the first nonzero homogeneous term of the nonnegative function Δv, so its spherical mean is positive and the leading difference A(e^{pv})-M(e^v)^p is strictly negative. If all terms below 2m are harmonic, the only quadratic exponential contribution at degree 2m is P_m^2/2, and the coefficient reduces to the stated sum of a nonpositive P_{2m} term and a strictly negative variance term when p<1+2m/n. The harmonic germ e^{H_m} reverses the sign for p>1+2m/n. Constant analytic germs give equality, so the analytic corollary is also sound.

## Originality

**qualified_supported**. Mochizuki's 2005 paper explicitly leaves the intermediate exponent range open beyond a second-order nondegeneracy condition, and the 2009 Beckenbach–Radó work gives a global exponent n/(n-1) that does not cover the whole upper part of that interval for n≥3. Targeted searches did not locate the finite-order threshold 1+2m/n or the conclusion that a smooth bad positive point must be infinitely flat in log u. Higher-order Pizzetti expansions are classical, so the novelty is only the finite-jet obstruction and its consequences, with residual terminology risk.

## Scientific value

**meaningful_local_resolution**. The result removes Mochizuki's nondegeneracy hypothesis at every finite-order positive point, settles the full intermediate range locally for positive real-analytic log-subharmonic functions, and sharply isolates infinite-order flatness as the remaining smooth obstruction.

## Independent checks

- Re-derived the degree-d normalized ball and sphere means by radial integration.
- Checked separately the first-nonharmonic and all-harmonic-below-2m cases, including the sign of the first nonzero homogeneous term of Δv.
- Verified that no mixed exponential term other than P_m^2 can contribute through degree 2m.
- Checked the harmonic homogeneous sharpness germ and the m=1 reduction against the second-order coefficient.

## Literature and evidence checked

- https://www.jstage.jst.go.jp/article/iis/11/2/11_2_117/_article
- https://doi.org/10.1007/s11587-009-0046-0
- https://doi.org/10.2748/tmj/1178228490
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/finite-jet-log-subharmonic-mean-inequality--2e6c49bb3292
## Limitations

- The theorem is local and assumes positivity near the point.
- Infinite-order-flat smooth germs and the endpoint p=1+2m/n remain unresolved.
- The result does not address zeros of a log-subharmonic function.
- Equivalent higher-order mean-value/Pizzetti formulations remain a residual originality risk.
