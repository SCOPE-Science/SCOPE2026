# Independent mathematical audit

## correctness

PASS

The exact frontier is correct, but the frozen opening is misleading if read as saying the angle provides information beyond the norm at fixed step size. In this family (I−R)^T(I−R)=2(1−cos θ)I, so the norm and the cosine identify one another. The complete repaired RESULT gives the equivalent norm thresholds and clarifies their dependence on the step size. Independently reconstructing the complex two-by-two update gives P=2u−2u²t²z and Q=u²(1−t²z). The determinant modulus is strictly below one. For roots a,b, the Schur difference equals (1−|a|²)(1−|b|²)|1−a conjugate(b)|²; hence its positive, zero or negative sign decides both strict stability and the exact radius-one boundary. Expanding yields the prefactor (1+c) times the sign factor c−H(t), with c=cos θ. At c=−1 the two roots are 1 and (1+t²)/(1+t)², including for t above the matched cutoff. Factoring H±1 and differentiating proves the two transitions and strict monotonicity; substitution gives H(2)=−11/25. Replay: repairs/1/RESULT.md Proof and the frozen verify.py lines 8–59, inspected but not executed. Its finite angle grid cannot establish the equality cases, which are covered by the algebra. Applies only to the exact, constant, equal-step primal-first quadratic iteration with extrapolation one.

## originality

PASS

The distinct supported claim is the full necessary-and-sufficient rotational frontier with its exact neutral cases and two transition steps, equivalently the joint norm/step threshold for this particular family. The overlap with existing mismatched-adjoint Chambolle–Pock convergence theorems concerns the algorithm and sufficient conditions, not this frontier. The assessment is bounded to examined evidence and is not a determination of historical priority.

## value

PASS

For a standard splitting algorithm, the exact model tests what generic sufficient mismatch estimates miss. The frontier identifies a sharp safe region, distinguishes a fixed-point obstruction from an expanding mode, and yields explicit changes in angular tolerance, including convergence at a substantial mismatch beyond familiar matched sufficient step restrictions. The purpose survives the clarification that in this rotation family the norm is already a complete angular parameter at each fixed t.

The dated certificate retains the supplied scientific assessment, sources and limitations.
