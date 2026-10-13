# The zero-inflow avoidance face invalidates full uniform persistence
## Finding
Poulton and Ellner study a learned-avoidance epidemic model with nonnegative state variables \(S,A,I,P\) and permit \(0\le p\le1\) and \(v\ge0\). They state that when \(R_0>1\), not only the disease variables but all state variables are uniformly persistent. On the allowed endpoint \(p=v=0\), however, the avoidance equation becomes
\[
A'=-[\beta\alpha(P)P+w+\mu+c(P)]A.
\]
Because \(\alpha(P)\ge0\), \(P\ge0\), \(w\ge0\), \(\mu>0\), and \(c(P)\ge0\), every solution with \(A(0)>0\) obeys
\[
0<A(t)\le A(0)e^{-\mu t}\longrightarrow0.
\]
Therefore an interior trajectory approaches the boundary face \(A=0\), so the full state cannot be uniformly persistent. The same endpoint also makes \(A=0\) an invariant face. For any \(R_0>1\), this face contains the endemic equilibrium
\[
A^*=0,\qquad S^*=R_0^{-1},\qquad
I^*=\frac{\mu(1-R_0^{-1})}{\mu+\phi},\qquad
P^*=\frac{\theta}{\lambda}I^*.
\]
Thus the disease-free equilibrium is not the maximal invariant boundary set under the paper's full stated parameter range.

## Assumptions and scope
The learned-avoidance model is
\[
S'=\mu-\beta SP+(1-p)\gamma I+wA-vS-\mu S,
\]
\[
A'=-\beta\alpha(P)AP+p\gamma I-wA+vS-[\mu+c(P)]A,
\]
\[
I'=\beta SP+\beta\alpha(P)AP-(\gamma+\mu+\phi)I,
\]
\[
P'=\theta I-\lambda P.
\]
The source assumes \(\mu,\beta,\gamma,\theta,\lambda>0\), \(\phi,w,v\ge0\), \(0\le p\le1\), \(\alpha(P)\ge0\), and \(c(P)\ge0\). The finding uses only the allowed endpoint \(p=v=0\) and otherwise keeps these assumptions.

The claim concerns the stronger statement that all four state variables are uniformly persistent and the associated boundary argument. It does not claim that the disease pair \(I,P\) fails to persist when \(R_0>1\). It also does not prove that imposing \(p+v>0\) is sufficient for every other step of the published persistence theorem; it shows only that excluding \(p=v=0\) is necessary for the strict avoidance-inflow step used there.

## Proof
Set \(p=v=0\). Then
\[
A'=-q(t)A,\qquad q(t)=\beta\alpha(P(t))P(t)+w+\mu+c(P(t)).
\]
All terms in \(q(t)\) are nonnegative and \(q(t)\ge\mu\). Hence the scalar equation is explicit:
\[
A(t)=A(0)\exp\left(-\int_0^t q(s)\,ds\right),
\]
so
\[
0<A(t)\le A(0)e^{-\mu t}
\]
for every interior initial condition with \(A(0)>0\). In the Euclidean state-space metric, the distance from \((S(t),A(t),I(t),P(t))\) to the boundary is at most \(A(t)\), and therefore tends to zero. No positive uniform lower bound on distance from the full boundary can exist.

When \(A(0)=0\), the same equation gives \(A(t)=0\) for all \(t\), so \(A=0\) is invariant. On this face the model reduces to
\[
S'=\mu-\beta SP+\gamma I-\mu S,\qquad
I'=\beta SP-(\gamma+\mu+\phi)I,\qquad
P'=\theta I-\lambda P.
\]
For this endpoint the disease-free equilibrium has \(S=1\), and
\[
R_0=\frac{\beta\theta}{\lambda(\gamma+\mu+\phi)}.
\]
If \(R_0>1\), define
\[
S^*=R_0^{-1},\qquad
I^*=\frac{\mu(1-R_0^{-1})}{\mu+\phi},\qquad
P^*=\frac{\theta}{\lambda}I^*.
\]
These quantities are positive. The \(P\)-equation vanishes by construction. The \(I\)-equation vanishes because \(\beta\theta S^*/\lambda=\gamma+\mu+\phi\). Finally, after using this identity in the \(S\)-equation,
\[
S'=\mu(1-S^*)-(\mu+\phi)I^*=0.
\]
Thus \((S^*,0,I^*,P^*)\) is a non-disease-free invariant boundary equilibrium. This directly contradicts the supplementary proof's assertion that the disease-free equilibrium is the maximal invariant set on the boundary for the full allowed parameter range.

## Verification
The algebra above is independently reproducible from `verify.py`. It verifies both the symbolic residuals of the boundary endemic equilibrium and an exact numerical witness. For
\[
\mu=\gamma=\theta=\lambda=1,\qquad \phi=w=p=v=0,\qquad \beta=4,
\]
one has \(R_0=2\) and
\[
(S^*,A^*,I^*,P^*)=(1/2,0,1/2,1/2).
\]
Substitution gives zero in all four right-hand sides for any admissible \(\alpha\) and \(c\), because both terms multiplying those functions contain \(A^*=0\). For an interior trajectory at the same parameters, \(A(t)\le A(0)e^{-t}\), so the distance to \(A=0\) vanishes.

## Relationship to prior work
The primary article explicitly permits \(p=0\) and \(v=0\), states that all state variables are uniformly persistent for \(R_0>1\), and refers the proof to Supplementary Section S1.5. That supplementary proof attempts to show strict entrance from the face \(A=0\) using \(p\gamma I+vS>0\). At \(p=v=0\) the expression is identically zero instead, so the proof's boundary-accessibility step fails exactly where the counterexample lies.

Targeted searches using the source title, the parameter endpoint \(p=v=0\), the phrase “uniform persistence,” and the boundary inflow expression did not locate a published correction or a stronger result covering this endpoint. The article page notes a revision to the funding section, not a scientific correction. Generic uniform-persistence theorems do not imply the source's conclusion once the modeled boundary contains an additional invariant set; the obstruction here is model-specific and follows directly from the published equations.

## Limitations
The finding does not re-prove or disprove persistence of the disease variables \(I\) and \(P\). It does not analyze all cases with \(p+v>0\), and it does not assert that \(p+v>0\) alone repairs every hypothesis of the persistence theorem. The counterexample is an endpoint of the stated parameter domain, not a claim about the parameter choices used in the paper's numerical simulations, which typically set \(p=1\).

## References
Poulton, A. J. and Ellner, S. P. (2025). “Learned behavioral avoidance can alter outbreak dynamics in a model for waterborne infectious diseases.” *Journal of Mathematical Biology* 91, 28. DOI: 10.1007/s00285-025-02252-7. Published 2025-08-18. Supplementary Section S1.5 contains the uniform-persistence proof discussed here.
