# Valuative ceiling diagnostic for Li–Miao Question 4.20

## Context

Li–Miao (arXiv:2506.17420v3) leave Question 4.20 open: if a K-semistable Fano manifold of dimension n contains a minimal rational curve of anticanonical degree 3 <= d <= n-1, must its volume be at most the volume of P^{d-1} x P^{n-d+1}? Their Section 4 constructs globally defined valuations v1 and v2 and, via Corollary 2.5, converts an explicit lower bound for vol(-K_X-xE) into an upper ceiling phi(T) for (-K_X)^n.

## Definitions

For v_l, l in {1,2}, the leading H0 estimate of Li–Miao gives the piecewise function phi and primitive Phi in equations (25), (29), and (30). The discrepancy is

A(v_l)=(d-2)+l(n-d+1),

and Corollary 2.5 gives V:=(-K_X)^n <= phi(T), where T>A is the unique solution of

(T-A)phi(T)=Phi(T).

Write

B(n,d)=vol(P^{d-1} x P^{n-d+1})=binom(n,d-1)d^{d-1}(n-d+2)^{n-d+1}.

## Result

For the specific Corollary-2.5 ceilings obtained from the displayed Li–Miao v2 estimate, direct computation for every pair 4 <= n <= 10 and 3 <= d <= n-1 gives

phi_2(T)/B(n,d) in [1.0402228914, 1.1338599191].

Thus these explicit v2 ceilings do not by themselves imply the stratified bound in Question 4.20 on any of those 28 tested pairs. The corresponding v1 ceilings are larger on all 28 pairs.

At (n,d)=(4,3) this failure has a completely exact certificate. Put y=x-3. Then

phi(y)=(243+216y+54y^2)/4,
Phi(y)=(972/5+243y+108y^2+18y^3)/4,
A=5,

so Psi(y)=(y-2)phi(y)-Phi(y). Exact arithmetic gives

Psi(4)=-261/10 < 0,
Psi(41/10)=7389/1000 > 0.

Since Psi'(x)=(x-A)phi'(x)>0 beyond A, the root satisfies y_T in (4,4.1), equivalently T in (7,7.1). As phi is increasing,

phi(T)>phi(7)=1971/4=492.75>486=B(4,3).

Numerical bisection gives T approximately 7.0784886356 and phi(T) approximately 505.5483252606.

## Interpretation

This is a limitation of one specific quantitative route: applying Corollary 2.5 to the published H0 lower estimates for v1 or v2. It does **not** show that Question 4.20 is false, does not rule out sharper information about these same valuations, and does not prove that every argument involving v1 or v2 must fail. A proof of Question 4.20 could still use these valuations together with stronger geometric input, sharper volume estimates, other valuations, or classification arguments.

## Reproducibility

Run `python3 artifacts/valuation_ceiling.py` (stdlib only). It enumerates all 28 pairs 4 <= n <= 10, 3 <= d <= n-1, prints the v2 ceiling, B(n,d), their ratio, and the v1 control. The (4,3) certificate above is exact rational arithmetic and can be checked by hand.

## Limitations

Only the (4,3) comparison is presented as an exact interval certificate here. The complete 28-pair table uses floating-point bisection, although the formulas are explicit polynomials with rational coefficients and can be interval-certified if desired. The result is a diagnostic about the published Corollary-2.5 ceilings, not a resolution of Question 4.20.

## References

- C. Li, M. Miao, *On the volume of K-semistable Fano manifolds*, arXiv:2506.17420v3, especially Corollary 2.5, equations (25), (29)–(31), Remark 4.4, and Question 4.20.
- C. Li, M. Miao, K. Zhang, *The sharp volume gap for Kähler manifolds with positive Ricci curvature*, arXiv:2608.08193.
