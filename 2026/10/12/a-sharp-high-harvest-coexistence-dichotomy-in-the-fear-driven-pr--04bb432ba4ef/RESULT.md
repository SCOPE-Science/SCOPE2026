# A sharp high-harvest coexistence dichotomy in the fear-driven predator–prey model

## Finding

Consider
\[
\dot u=\frac{au}{1+kv}-bu^2-cu^pv^m,
\qquad
\dot v=-dv-qv^r+eu^pv^m,
\]
with
\[
a,b,c,d,e,k>0,\qquad
0<p\le1,\qquad
0<m\le r\le1.
\]
Write
\[
K=\frac ab.
\]

The exponent comparison between harvesting and predator interference determines the high-harvest equilibrium geometry.

If
\[
r>m,
\]
then for every sufficiently large finite harvesting effort \(q\) there is a positive coexistence equilibrium
\[
(u_q,v_q)
\]
with
\[
u_q\to K
\]
and
\[
v_q\sim
\left(\frac{eK^p}{q}\right)^{1/(r-m)}.
\]
This high-harvest branch is locally asymptotically stable for all sufficiently large \(q\).

At the boundary
\[
r=m<1,
\]
positive coexistence exists exactly when
\[
q<eK^p.
\]
At
\[
r=m=1,
\]
positive coexistence exists exactly when
\[
d+q<eK^p.
\]

Thus the model has a sharp distinction. When the harvesting exponent exceeds the interference exponent, arbitrarily large finite harvesting leaves a stable positive equilibrium, although its predator density tends to zero. When the two exponents coincide, coexistence ends at a finite harvesting threshold.

For the paper's Example 1,
\[
m=0.6,\qquad
r=1,\qquad
a=3,\qquad
b=0.2,\qquad
p=0.5,\qquad
e=1.1,
\]
so
\[
K=15
\]
and
\[
v_q\sim37.4624163930\,q^{-5/2}.
\]

## Assumptions and scope

The result concerns the harvesting model printed in Section 6 of the motivating article.

All rate parameters are positive. The result is restricted to the source's analytically emphasized regime
\[
r\ge m.
\]

The high-harvest conclusion is an equilibrium and local-stability theorem. It does not say that every positive initial condition converges to the coexistence branch. In particular, the nonsmooth boundary dynamics can retain extinction basins.

The theorem also does not assert a global bifurcation diagram for intermediate harvesting effort. It classifies the existence boundary when
\[
r=m
\]
and the asymptotic branch when
\[
r>m.
\]

## Proof

At a positive equilibrium, divide the prey equation by \(u\) and the predator equation by \(v^m\). This gives
\[
\frac{a}{1+kv}-bu-cu^{p-1}v^m=0
\]
and
\[
eu^p=dv^{1-m}+qv^{r-m}.
\]

The first equation immediately implies
\[
bu<\frac{a}{1+kv}<a,
\]
hence every positive equilibrium satisfies
\[
0<u<K.
\]

Assume first that
\[
r>m.
\]
Then \(m<1\). For each fixed \(u>0\), the function
\[
v\mapsto dv^{1-m}+qv^{r-m}
\]
is continuous, strictly increasing from zero to infinity. Therefore the predator equation defines a unique positive
\[
v=V_q(u).
\]
For
\[
0<u\le K,
\]
\[
qV_q(u)^{r-m}
\le eK^p,
\]
so
\[
V_q(u)
\le
\left(\frac{eK^p}{q}\right)^{1/(r-m)}.
\]
Thus \(V_q(u)\to0\) uniformly on
\[
[K/2,K].
\]

Define the undivided prey residual
\[
P_q(u)
=
\frac{au}{1+kV_q(u)}
-bu^2
-cu^pV_q(u)^m.
\]
At
\[
u=K,
\]
one has
\[
P_q(K)<aK-bK^2=0.
\]
At
\[
u=\frac K2,
\]
uniform convergence \(V_q\to0\) gives
\[
P_q(K/2)
\to
\frac{aK}{2}-\frac{bK^2}{4}
=
\frac{a^2}{4b}>0.
\]
Therefore, for all sufficiently large \(q\), continuity gives a root
\[
u_q\in(K/2,K).
\]

For any sequence of such roots with \(q\to\infty\), the bound above gives
\[
v_q\to0.
\]
Taking limits in the prey equilibrium equation yields
\[
u_\infty(a-bu_\infty)=0.
\]
Since
\[
u_q\ge K/2,
\]
the only possible limit is
\[
u_\infty=K.
\]
The predator equation then gives
\[
qv_q^{r-m}
=
eu_q^p-dv_q^{1-m}
\to
eK^p.
\]
Hence
\[
v_q\sim
\left(\frac{eK^p}{q}\right)^{1/(r-m)}.
\]

For local stability, let \(F\) and \(G\) denote the two right-hand sides. At a positive equilibrium,
\[
F_u
=
-bu+c(1-p)u^{p-1}v^m,
\]
so on the high-harvest branch
\[
F_u\to-bK=-a<0.
\]
Also,
\[
F_v
=
-\frac{aku}{(1+kv)^2}
-cmu^pv^{m-1}<0,
\]
\[
G_u=epu^{p-1}v^m>0.
\]
Using the predator equilibrium equation,
\[
G_v
=
-(1-m)d-(r-m)qv^{r-1}<0.
\]
Thus for sufficiently large \(q\),
\[
\operatorname{tr}J=F_u+G_v<0,
\]
while
\[
\det J
=
F_uG_v-F_vG_u>0.
\]
The equilibrium is therefore locally asymptotically stable.

Now let
\[
r=m<1.
\]
The predator equation is
\[
eu^p=q+dv^{1-m}.
\]
If
\[
q\ge eK^p,
\]
then every positive solution of this equation would have
\[
u>K,
\]
contradicting the prey bound.

Conversely, suppose
\[
q<eK^p.
\]
Set
\[
u(v)=
\left(\frac{q+dv^{1-m}}e\right)^{1/p}.
\]
Then
\[
u(0)=\left(\frac qe\right)^{1/p}<K,
\]
and \(u(v)\) reaches \(K\) at some finite positive \(v\). Substitution in the divided prey residual gives a positive value at \(v=0\),
\[
a-bu(0)>0,
\]
and a strictly negative value when \(u(v)=K\). Continuity therefore supplies a positive coexistence equilibrium. This proves the exact threshold
\[
q_c=eK^p.
\]

Finally, when
\[
r=m=1,
\]
the predator equation becomes
\[
eu^p=d+q.
\]
A positive equilibrium can exist only when the resulting fixed \(u\) satisfies
\[
u<K,
\]
which is equivalent to
\[
d+q<eK^p.
\]
Under this strict inequality, the divided prey residual is positive at \(v=0\) and tends to a negative value as \(v\to\infty\), so a positive root exists.

## Verification

The bundled `verify.py` reconstructs the equilibrium identities, the Jacobian sign formulas, and the source's Example 1.

For the Example 1 parameters it verifies
\[
K=15
\]
and the asymptotic coefficient
\[
(eK^p)^{1/(r-m)}
=
37.4624163930\ldots.
\]

It numerically solves the exact equilibrium equations at
\[
q=10,\quad100,\quad1000
\]
only as a replay of the analytic theorem. The computed predator coordinates approach the predicted
\[
q^{-5/2}
\]
law, and the exact Jacobian formulas give negative trace and positive determinant at each checked high-harvest equilibrium.

No finite numerical sample is used to prove the infinite-\(q\) statement.

## Relationship to prior work

Antwi-Fordjour, Parshad, Thompson, and Westaway introduce the harvested system and state their local-stability guideline under
\[
r\ge m.
\]
They formulate harvesting-induced recovery from prey finite-time extinction as a conjecture, show stable coexistence numerically at finite \(q\), and state that very high harvesting drives prey toward carrying capacity while predator density becomes close to extinction. They leave a full dynamical analysis of the harvested model as future work.

The result above turns the high-harvest equilibrium picture into a theorem and exposes the exponent boundary that is not visible from a finite parameter scan. In the paper's own
\[
r=1,\qquad m=0.6
\]
example, the positive stable branch persists to arbitrarily large finite \(q\), with an explicit algebraic decay rate for its predator coordinate.

Caraballo, Colucci, and Guerrini analyze nonlinear predator harvesting in a different delayed Holling-type model. Their work establishes persistence and positive-equilibrium bifurcation theory for another harvesting law, but it does not contain the present
\[
qv^r
\]
versus
\[
v^m
\]
exponent competition or imply the threshold and asymptotic formulas above.

Searches by the motivating DOI, exact title, harvesting-exponent aliases, the pair of powers
\[
v^r,\qquad v^m,
\]
and high-harvest coexistence terminology did not locate a published statement of this source-specific dichotomy.

## Limitations

The theorem is local around the high-harvest coexistence branch and does not prove global persistence from every positive initial condition.

It does not rule out additional coexistence equilibria or boundary attractors at intermediate harvesting effort.

When
\[
r>m,
\]
the statement that the positive branch persists for arbitrarily large finite \(q\) is compatible with predator density becoming arbitrarily small. Mathematical positivity at equilibrium is not the same as ecological detectability.

The regime
\[
r<m
\]
is outside the accepted claim.

## References

1. K. Antwi-Fordjour, R. D. Parshad, H. E. Thompson, S. B. Westaway, “Fear-driven extinction and (de)stabilization in a predator-prey model incorporating prey herd behavior and mutual interference,” AIMS Mathematics 8 (2023), 3353–3377. DOI: 10.3934/math.2023173. Preprint: arXiv:2108.00546.
2. T. Caraballo, R. Colucci, L. Guerrini, “On a predator prey model with nonlinear harvesting and distributed delay,” Communications on Pure and Applied Analysis 17 (2018), 2703–2727. DOI: 10.3934/cpaa.2018128.
