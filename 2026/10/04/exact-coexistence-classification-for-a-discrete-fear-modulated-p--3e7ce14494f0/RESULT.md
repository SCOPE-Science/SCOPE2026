# Exact coexistence classification for a discrete fear-modulated predator-prey map

## Finding
Consider the discrete system
\[
u_{n+1}=u_n\exp\!\left[\frac{r}{1+kv_n}\left(1-\frac{u_n}{K}\right)-\frac{\beta v_n}{u_n+\gamma}\right],
\qquad
v_{n+1}=v_n\exp\!\left[\alpha-\frac{av_n}{bu_n+c}-d\right].
\]
Assume all biological parameters are positive, \(k\ge 0\), and \(\alpha>d\). Put
\[
q=\frac{\alpha-d}{a}>0.
\]
Every strictly positive fixed point satisfies \(v=q(bu+c)\), and its prey coordinate is a positive root of
\[
P(u)=C_0u^2+C_1u+C_2,
\]
with
\[
\begin{aligned}
C_0&=r+Kk\beta q^2b^2,\\
C_1&=2bcKk\beta q^2+bK\beta q+r\gamma-rK,\\
C_2&=Kk\beta q^2c^2+cK\beta q-rK\gamma.
\end{aligned}
\]
Because \(C_0>0\), the number of strictly positive coexistence equilibria is completely classified by the signs of \(C_1,C_2\) and the discriminant \(\Delta=C_1^2-4C_0C_2\):

- If \(C_2<0\), there is exactly one positive equilibrium.
- If \(C_2=0\), there is exactly one strictly positive equilibrium when \(C_1<0\), and none when \(C_1\ge 0\).
- If \(C_2>0\) and \(C_1<0\), there are two distinct positive equilibria when \(\Delta>0\), one double positive equilibrium when \(\Delta=0\), and none when \(\Delta<0\).
- If \(C_2>0\) and \(C_1\ge0\), there is no positive equilibrium.

Thus the condition \(\alpha>d\) does not force a unique positive equilibrium: zero, one, or two can occur.

There is also an exact link to invasion of the predator-only equilibrium \(H_2=(0,qc)\). Its prey multiplier is
\[
\lambda_u=\exp\!\left[\frac{r}{1+kqc}-\frac{\beta qc}{\gamma}\right],
\]
and direct simplification gives
\[
C_2=-K\gamma(1+kqc)\log\lambda_u.
\]
Therefore \(C_2<0\) is exactly \(\lambda_u>1\), while \(C_2>0\) is exactly \(\lambda_u<1\). In particular, a two-coexistence regime can occur even on the no-invasion side of the predator-only state.

For the positive-\(k\) parameter choice
\[
r=1,\ K=10,\ \beta=\tfrac15,\ \gamma=a=1,\ b=\tfrac1{10},\ c=5,\ k=\tfrac1{100},\ \alpha=\tfrac32,\ d=\tfrac12,
\]
one has
\[
P(u)=\frac{5001}{5000}u^2-\frac{439}{50}u+\frac12,
\qquad
\Delta=\frac{9386}{125}>0,
\]
so the two prey coordinates are approximately \(0.0573219202\) and \(8.7209224309\), both below \(K=10\). At the predator-only state, \(\log\lambda_u=-1/21\), hence \(\lambda_u<1\).

A separate counterexample to unconditional existence is
\[
r=K=\gamma=a=b=c=1,\quad \beta=2,\quad k=\tfrac1{10},\quad \alpha=\tfrac32,\quad d=\tfrac12,
\]
for which
\[
P(u)=\frac65(u+1)^2
\]
has no positive root.

## Assumptions and scope
The result concerns fixed points of the autonomous two-dimensional map above. Parameters \(r,K,\beta,\gamma,a,b,c,\alpha,d\) are positive and \(k\ge0\). A strictly positive equilibrium requires \(\alpha>d\); if \(\alpha\le d\), the predator fixed-point equation cannot hold with \(v>0\).

The claim classifies strictly positive equilibria only. It does not classify their local stability, the global dynamics, or the flip and Neimark–Sacker bifurcations analyzed in the source article.

## Proof
At a fixed point with \(u>0\) and \(v>0\), the exponential factors must equal one. The predator equation therefore gives
\[
\alpha-\frac{av}{bu+c}-d=0,
\]
so \(v=q(bu+c)\), where \(q=(\alpha-d)/a\).

Substituting into the prey equation and multiplying by the positive denominator gives the equivalent scalar equation
\[
F(u)=r\left(1-\frac{u}{K}\right)(u+\gamma)-\beta q(bu+c)\bigl(1+kq(bu+c)\bigr)=0.
\]
Expansion yields
\[
P(u)=-KF(u)=C_0u^2+C_1u+C_2,
\]
with the coefficients stated above. Since \(C_0>0\), Vieta's formulas give product \(C_2/C_0\) and sum \(-C_1/C_0\). If \(C_2<0\), the two roots have opposite signs, so exactly one is positive. If \(C_2=0\), the roots are \(0\) and \(-C_1/C_0\). If \(C_2>0\), any two real roots have the same sign; they are positive exactly when their sum is positive, equivalently \(C_1<0\), and their multiplicity is determined by \(\Delta\). These cases give the stated classification.

Every positive root automatically satisfies \(u<K\): for \(u\ge K\), the first term in \(F(u)\) is nonpositive while the second is strictly negative, so \(F(u)<0\).

At \(H_2=(0,qc)\), linearization in the prey direction gives
\[
\lambda_u=\exp\!\left[\frac{r}{1+kqc}-\frac{\beta qc}{\gamma}\right].
\]
Multiplication of its logarithm by \(-K\gamma(1+kqc)\) gives exactly \(C_2\), proving the invasion relation.

## Verification
The bundled `verify.py` checks the coefficient identity \(P(u)=-KF(u)\) with exact rational arithmetic, implements the full quadratic sign classification, verifies the exact discriminant and boundary multiplier in the two-equilibrium example, verifies the no-equilibrium factorization, and numerically substitutes both positive roots back into the original map. It prints `VERIFY_OK` only when all checks pass.

The numerical substitution is a finite consistency check; the root classification and invasion relation are analytic.

## Relationship to prior work
Du, Han, and Lei (2023) define the map above and state in Proposition 1(iii) that, when \(\alpha>d\), there is a unique positive equilibrium whose prey coordinate is the only positive root of the same quadratic. Their conclusion section also states that the system has four equilibrium points. The coefficient signs in the published quadratic do not support that unconditional uniqueness statement.

Lei, Han, and Wang (2022) study a different discrete fear model with additive updates and a different fixed-point polynomial; its positive equilibrium has an explicit unique positive root. Chen, He, and Chen (2021) study another discrete fear model with alternative food and impose an explicit existence condition for its positive equilibrium. Neither result implies uniqueness for the 2023 exponential map.

Targeted searches for the exact title, DOI, coefficient pattern, positive-root condition, predator-only invasion threshold, and equivalent coexistence terminology located the source article and related fear models but no correction or prior statement of the classification above.

## Limitations
The result corrects and refines the equilibrium-existence geometry of this exact model; it does not establish the stability of either coexistence branch in the two-root regime. A later unindexed note could contain the same algebraic observation. The claimed originality is therefore restricted to the explicit classification, the boundary-multiplier identity, and the exhibited counterexamples for the source map.

## References
1. X. Du, X. Han, C. Lei, “Dynamics of a nonlinear discrete predator-prey system with fear effect,” *AIMS Mathematics* 8(10), 23953–23973 (2023), DOI 10.3934/math.20231221.
2. C. Lei, X. Han, W. Wang, “Bifurcation analysis and chaos control of a discrete-time prey-predator model with fear factor,” *Mathematical Biosciences and Engineering* 19(7), 6659–6679 (2022), DOI 10.3934/mbe.2022313.
3. J. Chen, X. He, F. Chen, “The Influence of Fear Effect to a Discrete-Time Predator-Prey System with Predator Has Other Food Resource,” *Mathematics* 9(8), 865 (2021), DOI 10.3390/math9080865.
