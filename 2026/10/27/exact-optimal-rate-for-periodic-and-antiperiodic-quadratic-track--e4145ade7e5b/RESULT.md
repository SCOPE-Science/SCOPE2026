# Exact optimal rate for periodic and antiperiodic quadratic tracking

## Finding

Let \(n\ge 4\), \(\sigma\in\{-1,+1\}\), and \(0<\mu<L\). Let \(A=A^{\mathsf T}\) be real symmetric with \(\mu I\preceq A\preceq LI\), and consider \(f_k(x)=\tfrac12 x^{\mathsf T}Ax+b_k^{\mathsf T}x\). Assume \(b_{k+n}=\sigma b_k\) and that the minimal common denominator of the forcing model is exactly \(m(z)=z^n-\sigma\), so all \(n\) model poles are present. Within the class of real scalar linear time-invariant gradient filters \(c(z)=d(z)/m(z)\), where \(d\) is a polynomial with \(\deg d<n\), the minimum worst-case root convergence factor over \(\lambda\in[\mu,L]\) is

\[
\rho_* = \left(\frac{L-\mu}{L+\mu}\right)^{1/n}.
\]

It is attained by

\[
c_*(z)=-\frac{2\sigma}{(L+\mu)(z^n-\sigma)},
\]

which is equivalent to the causal recurrence

\[
x_{k+n}=\sigma x_k-\frac{2\sigma}{L+\mu}(Ax_k+b_k).
\]

The cases \(\sigma=1\) and \(\sigma=-1\) cover periodic and antiperiodic forcing, respectively. The statement is restricted to the exact order-\(n\) model and to the stated scalar filter class.

## Assumptions and scope

- The Hessian \(A\) is fixed, real symmetric, and positive definite, with known spectral bounds \(0<\mu<L\).
- The linear term satisfies \(b_{k+n}=\sigma b_k\). Its minimal common model denominator is \(z^n-\sigma\), not a proper divisor; this excludes lower-order forcing models with canceled poles.
- The filter is scalar, linear time-invariant, and strictly proper, with denominator \(z^n-\sigma\) and numerator degree less than \(n\). The same filter is used on every eigendirection.
- The rate is the worst-case asymptotic root factor over all Hessians with spectrum in \([\mu,L]\) and all admissible order-\(n\) forcing signals. A fixed Hessian whose spectrum omits both endpoints can have a smaller rate.
- No noise, constraints, time-varying Hessian, nonlinear objective, or non-LTI controller is included.

## Proof

Put \(\alpha=2/(L+\mu)\), \(q=(L-\mu)/(L+\mu)\), and \(x_k^*=-A^{-1}b_k\). The forcing relation gives \(x_{k+n}^*=\sigma x_k^*\). For the proposed recurrence, with \(e_k=x_k-x_k^*\),

\[
e_{k+n}=\sigma(I-\alpha A)e_k.
\]

Because \(A\) is symmetric and its eigenvalues lie in \([\mu,L]\),

\[
\|I-\alpha A\|_2=\max_{\lambda\in[\mu,L]}|1-\alpha\lambda|=q.
\]

Thus each residue-class subsequence contracts by at most \(q\) every \(n\) steps. This gives root factor at most \(q^{1/n}\); equality occurs when an endpoint eigenvalue \(\mu\) or \(L\) is present and the initial error has a nonzero component in its eigenspace.

For optimality, take any admissible numerator \(d\) and define the closed-loop characteristic polynomial

\[
p_\lambda(z)=z^n-\sigma-\lambda d(z).
\]

It is monic of degree \(n\). Let \(\rho\) be the largest root modulus over \(\lambda\in[\mu,L]\). By the product-of-roots identity, \(|p_\mu(0)|\le\rho^n\) and \(|p_L(0)|\le\rho^n\). Since the constant terms satisfy

\[
L p_\mu(0)-\mu p_L(0)=-\sigma(L-\mu),
\]

the triangle inequality yields

\[
L-\mu\le L|p_\mu(0)|+\mu|p_L(0)|\le(L+\mu)\rho^n.
\]

Therefore every admissible filter has \(\rho\ge q^{1/n}\). For the proposed constant numerator \(d(z)=-2\sigma/(L+\mu)\),

\[
p_\lambda(z)=z^n-\sigma\left(1-\frac{2\lambda}{L+\mu}\right).
\]

All its roots have modulus \(\left|1-2\lambda/(L+\mu)\right|^{1/n}\le q^{1/n}\), with equality at \(\lambda=\mu\) or \(\lambda=L\). The lower and upper bounds coincide, proving the exact minimax factor.

## Verification

The proof uses only the recurrence, the spectral norm of a symmetric matrix, and the constant term of a monic characteristic polynomial. The interval inclusion \(1-2\lambda/(L+\mu)\in[-q,q]\) verifies the upper bound for every admissible curvature. The endpoint identity verifies the lower bound for every numerator of degree less than \(n\). No finite experiment is used as a substitute for proof.

## Relationship to prior work

Van Scoy and Bianchin derive the lower bound \(((L-\mu)/(L+\mu))^{1/n}\) for general unit-circle forcing models and explicitly construct optimal filters for low degrees \(n=1,2,3\). The present result gives a closed-form attaining filter for every \(n\ge4\) in the natural regular-polygon models \(z^n-1\) and \(z^n+1\); it does not assert attainment for arbitrary unit-circle pole configurations. Wu, Petersen, and Shames study polynomially varying optimizers with model \((z-1)^n\) and a different, higher-order algorithm class, so their rate result is not an equivalent formulation of this periodic/antiperiodic case. Work on the internal-model principle establishes tracking conditions and design procedures, but the inspected results do not provide this exact minimax rate for the stated scalar LTI filter class.

## Limitations

The result does not settle optimal controller design for general unit-circle pole sets, matrix-valued filters, non-LTI algorithms, noisy gradients, constrained problems, or time-varying Hessians. The exact order assumption matters: if the forcing denominator cancels to a proper divisor of \(z^n-\sigma\), a lower-order model may admit a different optimal rate. Independent validation has not been performed.

## References

1. Bryan Van Scoy and Gianluca Bianchin, “Temporal Variabilities Limit Convergence Rates in Gradient-Based Online Optimization,” arXiv:2510.12512v1 (first submitted 2025-10-14), especially Theorem 1 and Section V.
2. Alex Xinting Wu, Ian R. Petersen, and Iman Shames, “A Fundamental Convergence Rate Bound for Gradient Based Online Optimization Algorithms with Exact Tracking,” arXiv:2508.21335v2 (first submitted 2025-08-29), especially Theorems 1–2 and the polynomial-variation model.
3. Gianluca Bianchin and Bryan Van Scoy, “The Internal Model Principle of Time-Varying Optimization,” arXiv:2407.08037v3 (first submitted 2024-07-10), for exact-tracking conditions.
4. Gianluca Bianchin and Bryan Van Scoy, “The Discrete-time Internal Model Principle of Time-varying Optimization: Limitations and Algorithm Design,” 2025 CDC paper, author-hosted PDF identifier GB-BVS-25-cdc.pdf.
