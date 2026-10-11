# Exact fish-mean ceiling and zooplankton variance defect on Crowley–Martin cycles
## Finding
Consider the spatially homogeneous delayed phytoplankton–zooplankton–fish system studied by Gao and Meng. Its fish equation is
\[
\dot F=\frac{\gamma_2 ZF}{(a+Z)(b+F)}-g_2F,
\]
with positive parameters and a strictly positive periodic solution \((P,Z,F)\) of period \(T\). Write \(\bar H=T^{-1}\int_0^T H(t)\,dt\). Every non-equilibrium periodic solution satisfies
\[
\frac{\bar Z}{a+\bar Z}-\frac{g_2}{\gamma_2}(b+\bar F)
=\frac{a}{(a+\bar Z)^2}\,\overline{\frac{(Z-\bar Z)^2}{a+Z}}>0.
\]
Hence
\[
0<\bar F<\frac{\gamma_2}{g_2}-b,
\qquad
\bar Z>\frac{a g_2(b+\bar F)}{\gamma_2-g_2(b+\bar F)}.
\]
For the numerical coefficients used in the paper, \(a=1/2\), \(b=1/4\), \(\gamma_2=3/40\), and \(g_2=1/5\), these constraints reduce to
\[
0<\bar F<\frac18,
\qquad
\bar Z>\frac{1+4\bar F}{1-8\bar F}.
\]

## Assumptions and scope
All model parameters are positive. The claim concerns strictly positive, non-equilibrium, spatially homogeneous periodic solutions of the delayed model. No small-amplitude, near-Hopf, or small-delay assumption is used. The statement is a necessary constraint on any such periodic orbit; it does not assert existence, uniqueness, orbital stability, or a period bound.

## Proof
Set
\[
q(t)=\frac{Z(t)}{(a+Z(t))(b+F(t))}.
\]
Because \(F(t)>0\), division of the fish equation by \(F\) gives
\[
(\log F)'=\gamma_2 q-g_2.
\]
Integration over one period yields
\[
\bar q=\frac{g_2}{\gamma_2}.
\]
Integrating the undivided fish equation over a period gives
\[
\overline{Fq}=\frac{g_2}{\gamma_2}\bar F.
\]
Since
\[
\frac{Z}{a+Z}=(b+F)q,
\]
the two period balances combine to the exact identity
\[
\overline{\frac{Z}{a+Z}}=\frac{g_2}{\gamma_2}(b+\bar F).
\]
Now put \(A=a+\bar Z\) and \(x=Z-\bar Z\). The pointwise algebraic identity
\[
\frac1{A+x}=\frac1A-\frac{x}{A^2}+\frac{x^2}{A^2(A+x)}
\]
and \(\bar x=0\) imply
\[
\overline{\frac1{a+Z}}=\frac1{a+\bar Z}
+\frac1{(a+\bar Z)^2}\overline{\frac{(Z-\bar Z)^2}{a+Z}}.
\]
Using \(Z/(a+Z)=1-a/(a+Z)\) and the preceding period balance yields
\[
\frac{\bar Z}{a+\bar Z}-\frac{g_2}{\gamma_2}(b+\bar F)
=\frac{a}{(a+\bar Z)^2}\overline{\frac{(Z-\bar Z)^2}{a+Z}}.
\]
The right-hand side is nonnegative. Equality would force \(Z\) to be constant. With constant \(Z\), the fish equation is a scalar autonomous equation for \(F\), so a positive periodic solution has constant \(F\). With constant \(Z\), the phytoplankton equation is likewise scalar autonomous in \(P\), so periodicity forces constant \(P\). Equality therefore occurs only at an equilibrium, and the displayed defect is strictly positive on every non-equilibrium periodic orbit.

Because \(0<Z/(a+Z)<1\), the exact period balance gives
\[
0<\frac{g_2}{\gamma_2}(b+\bar F)<1.
\]
This proves \(0<\bar F<\gamma_2/g_2-b\). Solving the strict defect inequality for \(\bar Z\) proves the stated lower bound. Substitution of the paper's numerical coefficients gives the final specialized inequalities.

## Verification
The bundled checker verifies the reciprocal algebraic identity symbolically and checks the specialized rational coefficients exactly. The proof itself is analytic and does not depend on numerical experimentation. The source paper reports Hopf bifurcation and stable periodic solutions for its spatially homogeneous delayed system, so the identities constrain the finite-amplitude cycles studied there.

## Relationship to prior work
Gao and Meng analyze equilibria, stability switches, Hopf bifurcation, and diffusion-driven effects in the same model. Inspection of the full available text found no theorem giving the exact period-mean relation, the weighted zooplankton variance defect, or the fish-mean ceiling above. A full-text comparison with Lu and Xia's periodic Crowley–Martin model found a different stage-structured, nonautonomous system with density-dependent predator mortality; their period integrations are used for existence bounds rather than this constant-turnover mean identity. Tripathi's nonautonomous Crowley–Martin study likewise concerns persistence, periodic solutions, and attractivity in a structurally different system.

## Limitations
The theorem is specific to positive periodic solutions of the spatially homogeneous Gao–Meng model and uses the constant per-capita fish loss term. It does not characterize delayed spatial patterns, invariant measures that are not supported on a periodic orbit, or the stability and existence of cycles. Two related Crowley–Martin articles were available only at abstract/bibliographic level during comparison, so a residual literature risk remains that an equivalent identity could occur in inaccessible full text; no available evidence indicated such coverage.

## References
T. Gao and X. Meng, “Stability and Hopf bifurcation of a delayed diffusive phytoplankton-zooplankton-fish model with refuge and two functional responses,” *AIMS Mathematics* 8 (2023), 8867–8901. DOI: 10.3934/math.2023445.

W. Lu and Y. Xia, “Periodic solution of a stage-structured predator-prey model with Crowley-Martin type functional response,” *AIMS Mathematics* 7 (2022), 8691–8704. DOI: 10.3934/math.2022454.

J. P. Tripathi, “A predator–prey model with Crowley–Martin functional response: A nonautonomous study,” *Natural Resource Modeling* (2020). DOI: 10.1111/nrm.12287.
