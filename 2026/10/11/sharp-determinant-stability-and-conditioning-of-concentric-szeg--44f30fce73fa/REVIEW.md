# Independent mathematical audit

## correctness

PASS

PASS: The frozen RESULT.md constructs H^2=⊕_{n≥0} B^n K_B for the finite inner Blaschke multiplier and shows d distinct normalized evaluation kernels span K_B by the positive Cauchy determinant. Thus all infinite-orbit Riesz bounds reduce to the finite seed Gram. Expanding the Cauchy double alternant yields log det=Σ_{k=1}^{d-1}Σ_j L_r(θ_{j+k}-θ_j), L_r(t)=log[2r sin(t/2)/|1-r²e^{it}|]. Differentiation gives -L_r''≥c_r=(1-r²)²/(4(1+r²)²); strong Jensen and the exact cyclic identity Σ_{k,j}(ε_{j+k}-ε_j)²=2d Σ_j(ε_j-mean ε)² give the claimed quadratic loss, with equality only for rotated regular polygons. For d=2, the second-order near-antipodal loss tends to c_r h², proving uniform optimality. Fourier diagonalization gives λ_l=d(1-r²)r^{2l}/(1-r^{2d}) and uniform two-sided frame bounds iff sup_d d(1-r_d)<∞. I independently evaluated the d=2 quadratic coefficient at r=0.2,0.5,0.8 and h=0.02,0.01; all ratios tend to the displayed c_r. Script trials alone are not the proof.

## originality

PASS

PASS (best knowledge): The raw unorthogonalized Szegő kernels, precise radial Gram spectrum and the globally optimal all-degree angular determinant-defect coefficient are not provided by the inspected finite-Blaschke orbit existence theorem or general kernel Fekete design results. The Cauchy determinant and strong concavity principle are classical and are explicitly treated as inputs, not novel discoveries. A stronger generalized circular energy stability theorem is a residual coverage risk.

## value

PASS

PASS: This gives a sharp D-optimality stability modulus for a natural nonorthogonal generator family, plus exact optimal infinite-orbit Riesz bounds and a sharp high-degree uniform conditioning threshold. The quantitative penalty is structurally tied to pseudo-hyperbolic separation and has a proven extremal two-node obstruction, not an arbitrary constant recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
