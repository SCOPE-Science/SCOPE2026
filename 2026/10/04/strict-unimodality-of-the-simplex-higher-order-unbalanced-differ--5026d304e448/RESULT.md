# Strict unimodality of the simplex higher-order unbalanced-difference profile
## Finding
For every pair of integers \(n\ge 2\) and \(p\ge 1\), let \(S_n\) be an \(n\)-simplex and let \(D_p^t\) be the higher-order unbalanced difference body introduced by Fryš and Kotrbatý. Define
\[
F_{n,p}(t)=\frac{|D_p^t S_n|}{|S_n|^p},\qquad 0\le t\le1.
\]
Their simplex-volume formula gives
\[
F_{n,p}(t)=\sum_{j=0}^{n}\binom{np}{j}\binom{n}{j}t^j(1-t)^{np-j}.
\]
Then \(F_{n,p}\) has exactly one critical point in \((0,1)\), and that point is its strict global maximum. If \(x=t/(1-t)\), the maximizing parameter \(t_{n,p}\) is characterized by the unique positive zero \(x_{n,p}\) of
\[
Q_{n,p}(x)=\sum_{j=0}^{n}\left(\binom{n}{j+1}-\binom{n}{j}\right)\binom{np-1}{j}x^j,
\]
with the conventions \(\binom{n}{n+1}=0\) and \(\binom{np-1}{j}=0\) when \(j>np-1\), through \(t_{n,p}=x_{n,p}/(1+x_{n,p})\).

Because Fryš--Kotrbatý prove the corresponding pointwise higher-order Godbersen inequality in dimensions \(n\le3\), this immediately gives a sharp uniform-in-parameter consequence in those dimensions:
\[
\max_{0\le t\le1}\frac{|D_p^tK|}{|K|^p}\le F_{n,p}(t_{n,p})\qquad(n\le3),
\]
for every full-dimensional convex body \(K\subset\mathbb R^n\); simplices attain equality at \(t=t_{n,p}\).

For \(n=2\), the unique maximizer and the maximum are explicit:
\[
t_{2,p}=\frac{2}{2p+1+\sqrt{(2p-1)(6p-5)}},
\]
\[
F_{2,p}(t_{2,p})=\bigl(2+(2p-3)t_{2,p}\bigr)(1-t_{2,p})^{2p-2}.
\]
The large-order limits are
\[
p\,t_{2,p}\longrightarrow\frac{\sqrt3-1}{2},\qquad
F_{2,p}(t_{2,p})\longrightarrow(1+\sqrt3)e^{1-\sqrt3}.
\]

## Assumptions and scope
The order \(p\) and dimension \(n\) are positive integers with \(p\ge1\) and \(n\ge2\). The body \(S_n\) is any nondegenerate \(n\)-simplex. The profile statement for simplices is unconditional in every dimension. The uniform sharp inequality for arbitrary convex bodies uses the pointwise theorem proved in the cited source and is asserted here only for \(n\le3\), where that theorem is established. No claim is made that the pointwise inequality is known in dimensions \(n\ge4\).

## Proof
Set \(m=np\). The displayed simplex formula can be written in Bernstein form of degree \(m\):
\[
F_{n,p}(t)=\sum_{j=0}^{m}a_j\binom{m}{j}t^j(1-t)^{m-j},
\]
where \(a_j=\binom nj\) for \(0\le j\le n\) and \(a_j=0\) for \(j>n\). Differentiating the Bernstein basis gives
\[
F'_{n,p}(t)=m\sum_{j=0}^{m-1}(a_{j+1}-a_j)\binom{m-1}{j}t^j(1-t)^{m-1-j}.
\]
For \(0<t<1\), factor out the positive quantity \(m(1-t)^{m-1}\) and put \(x=t/(1-t)>0\). The sign of the derivative is therefore the sign of
\[
Q_{n,p}(x)=\sum_{j=0}^{n}(a_{j+1}-a_j)\binom{m-1}{j}x^j.
\]
The consecutive differences of the binomial row satisfy
\[
a_{j+1}-a_j>0\quad\text{before the middle},\qquad
a_{j+1}-a_j<0\quad\text{after the middle},
\]
with one possible zero at the middle when \(n\) is odd. Thus the nonzero coefficient sequence of \(Q_{n,p}\) has exactly one sign change. Multiplication by the positive factors \(\binom{m-1}{j}\) cannot introduce another sign change. Descartes' rule of signs therefore gives at most one positive zero.

At \(x=0\),
\[
Q_{n,p}(0)=\binom n1-\binom n0=n-1>0.
\]
The last nonzero coefficient is negative: for \(p>1\) the coefficient of \(x^n\) is \(-\binom{np-1}{n}<0\), while for \(p=1\) the coefficient of \(x^{n-1}\) is \(1-n<0\). Hence \(Q_{n,p}(x)\to-\infty\) as \(x\to\infty\). There is therefore exactly one positive zero. The derivative is positive before it and negative after it, proving strict unimodality and uniqueness of the global maximum.

For \(n=2\), the derivative polynomial becomes
\[
Q_{2,p}(x)=1-(2p-1)x-(2p-1)(p-1)x^2.
\]
Its positive zero is
\[
x_{2,p}=\frac{2}{(2p-1)+\sqrt{(2p-1)(6p-5)}},
\]
which gives the stated formula for \(t_{2,p}\). Substitution into the simplex profile, using the critical-point identity, yields
\[
F_{2,p}(t_{2,p})=\bigl(2+(2p-3)t_{2,p}\bigr)(1-t_{2,p})^{2p-2}.
\]
The two limits follow directly after dividing the denominator of \(t_{2,p}\) by \(p\) and using \((1-c/p)^{2p}\to e^{-2c}\).

## Verification
The proof is analytic and does not depend on finite experimentation. The accompanying `verify.py` independently checks the Bernstein-difference coefficient pattern over a broad finite grid, verifies the exact planar derivative coefficients, checks the closed-form planar critical point against its quadratic equation, checks the maximum-value simplification, and numerically sanity-checks the stated asymptotic limits. Running `python3 verify.py` from the package directory returns `VERIFY_OK`.

## Relationship to prior work
Fryš and Kotrbatý introduce the higher-order unbalanced body \(D_p^t\), formulate its simplex extremal problem, prove the relevant higher-order Godbersen statements in low dimensions, and compute the exact simplex profile used above. Their paper provides the formula that is the starting point here, but the parameter dependence of the simplex profile is not optimized there: the unique maximizing imbalance, the all-dimensional strict-unimodality statement, the planar radical formula, and the resulting sharp uniform-in-\(t\) low-dimensional bound are not stated in the inspected source.

Artstein-Avidan and Putterman study the order-one unbalanced difference body and prove several pointwise extremal statements, including the unbalanced Rogers--Shephard inequality through dimension five. Their work supplies the immediate order-one predecessor but does not contain the higher-order profile analyzed here.

The proof above uses the classical variation property encoded by Descartes' rule of signs for a Bernstein derivative. That general algebraic tool is not itself a statement about higher-order difference bodies; the new content is identifying the source's simplex volume as a Bernstein polynomial whose coefficient differences have one sign change, then extracting the exact geometric optimizer and uniform extremal consequence.

## Limitations
For \(n\ge4\), only the strict-unimodality and optimizer characterization of the simplex benchmark are proved here; the corresponding comparison with every convex body remains conditional on the open higher-order Godbersen-type conjecture. For \(n\ge3\), the unique maximizer is characterized as the positive zero of \(Q_{n,p}\), not by a general radical formula. The originality search covered the lead preprint, its order-one predecessor, targeted web queries, the available published-result database and targeted literature searches; an unindexed treatment applying Bernstein variation-diminishing arguments to the identical profile remains a residual literature risk.

## References
1. Filip Fryš and Jan Kotrbatý, *Around higher-order Godbersen conjectures*, arXiv:2609.08612v1, first public 2026-09-08. Primary MSC 52A40. In particular, the definitions of the higher-order unbalanced difference body, the low-dimensional higher-order Godbersen result, and the simplex-volume formula in the later part of the paper are used.
2. Shiri Artstein-Avidan and Eli Putterman, *On unbalanced difference bodies and Godbersen's conjecture*, arXiv:2412.05308, first public 2024-11-27.
