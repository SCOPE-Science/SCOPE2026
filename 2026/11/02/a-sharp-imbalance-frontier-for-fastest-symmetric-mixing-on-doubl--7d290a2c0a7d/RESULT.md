# A sharp imbalance frontier for fastest symmetric mixing on double-star trees

## Finding

Let \(D_{p,q}\) be the double-star tree with two adjacent hubs, with \(p\ge2\) leaves on one hub and \(q>p\) leaves on the other. Among *all* symmetric nonnegative row-stochastic transition matrices supported on its edges and self-loops, minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-\mathbf1\mathbf1^{\mathsf T}/(p+q+2)\|_2\).

Define \(d=q^2+q-p\) and
\[
H_{p,q}=1-\frac{p^2}{(q-p)^2}-\frac{[q(p+1)-p]^2}{q^2(q-p)^2}.
\]
There is exactly one real \(Q_p\in(2p,3p)\) with \(H_{p,Q_p}=0\). **Precisely when \(q\ge Q_p\)**, the global optimum equals
\[
\boxed{\mu_*(D_{p,q})=\frac{q^2}{q^2+q-p}},
\]
and it is attained by giving every left spoke the transition probability
\[
a_* =\frac{q(q-p)}{p(q^2+q-p)},
\]
every right spoke the transition probability
\[
c_* =\frac{q-p}{q^2+q-p},
\]
and the central bridge probability
\[
b_* =\frac{q(p+1)-p}{q^2+q-p}.
\]
Both hubs then have zero holding probability, while leaf holding probabilities are fixed by stochasticity. The displayed optimizer is unique among leaf-permutation-invariant transition matrices whenever \(q>Q_p\). For \(p<q<Q_p\), this particular design is strictly suboptimal and the optimal SLEM is strictly *less* than the displayed rational expression; the theorem does not classify the optimizer in that complementary regime.

The onset obeys \(Q_p/p\to1+\sqrt2\) as \(p\to\infty\). For instance \((p,q)=(2,6)\) lies in the rational phase and gives \((a_*,b_*,c_*,\mu_*)=(3/10,2/5,1/10,9/10)\), while \((2,5)\) does not.

## Assumptions and scope

The graph has \(p+q+2\) vertices, every edge may receive its own nonnegative transition probability, self-loops are allowed, and rows must sum to one. Symmetry means \(P=P^{\mathsf T}\), equivalently uniform stationary distribution. The assertion concerns discrete-time second-largest **absolute** eigenvalue, not only the spectral gap, not continuous-time mixing, and not prescribed nonuniform stationary measures. Feasibility allows zero edge probabilities in general, but the exhibited optimum is strictly positive on every tree edge.

## Proof

**Symmetry reduction.** Conjugating a feasible \(P\) by permutations within each leaf class preserves feasibility and \(\mu(P)\). Since \(\mu(P)=\|P-\mathbf1\mathbf1^{\mathsf T}/N\|_2\) is convex, averaging over these permutations cannot increase it. Thus some global optimum uses three edge weights \((a,b,c)\) with \(pa+b\le1\) and \(qc+b\le1\).

**Spectral certificate.** At the displayed candidate both hub inequalities are equalities. The symmetric four-dimensional orbit quotient of its Laplacian has diagonal \((a_*,1,1,c_*)\) and consecutive off-diagonal entries \((-\sqrt p\,a_*,-b_*,-\sqrt q\,c_*)\). Its characteristic polynomial is
\[
z(z-c_*)\bigl(z^2-(2+a_*)z+(p+q+2)a_*b_*\bigr).
\]
Each left-leaf difference has Laplacian eigenvalue \(a_*\), and each right-leaf difference has eigenvalue \(c_*\). Put \(f(z)=z^2-(2+a_*)z+(p+q+2)a_*b_*\). Direct expansion gives
\[
f(c_*)=\frac{q-p}{pd^2}\bigl[p^2(q^2-q+1)+pq(q^2-2)+q^2(q+1)\bigr]>0,
\]
\[
f(2-c_*)=\frac{q-p}{pd^2}\bigl[p^2(q^2-q+1)+(p-1)q^3-2pq+q^2\bigr]>0.
\]
The latter bracket is positive for \(p\ge2,q>p\), since \((p-1)q^3\ge2pq\). The two real roots of \(f\) have sum \(2+a_*\), which is strictly between \(2c_*\) and \(2(2-c_*)\). They therefore both lie strictly inside \((c_*,2-c_*)\). Also \(c_*<a_*<2-c_*\). Consequently the smallest positive Laplacian eigenvalue is \(c_*\) (of multiplicity \(q\)), and the largest is less than \(2-c_*\). Thus every nonconstant eigenvalue of \(P\) lies in \((-\mu_*,\mu_*]\), proving the candidate has SLEM \(\mu_*=1-c_*\).

**Global lower certificate.** In the ordered quotient coordinates (left leaf mean, left hub, right hub, right leaf mean), an eigenvector of \(P\) with eigenvalue \(\mu_*\) is \(x=(u,1,0,w)\), where
\[
u=\frac{\sqrt p\,q}{q-p},\qquad w=-\frac{q(p+1)-p}{\sqrt q\,(q-p)}.
\]
Let \(D=u^2+1+w^2\) and \(X=(u-\sqrt p)^2=p^3/(q-p)^2\). For the normalized Rayleigh quotient \(R(a,b,c)=x^{\mathsf T}P(a,b,c)x/D\), the gradient is \(- (X,1,w^2)/D\). The right-leaf difference eigenvalue is \(1-c\), with gradient \((0,0,-1)\). Define
\[
\theta=\frac{D}{D+qH_{p,q}},\quad
\lambda_L=\frac{\theta X}{pD},\quad
\lambda_R=\frac{\theta w^2/D+1-\theta}{q}.
\]
If \(H_{p,q}\ge0\), then \(0<\theta\le1\), both multipliers are positive, and a direct substitution verifies
\[
\theta\nabla R+(1-\theta)\nabla(1-c)
=-\lambda_L(p,1,0)-\lambda_R(0,1,q).
\]
The function \(F(a,b,c)=\max\{R(a,b,c),1-c\}\) is affine-maximal and lies below the full SLEM objective at every feasible triple. It equals \(\mu_*\) at the candidate. The displayed supporting gradient and the two feasible inequalities \(pa+b\le1\), \(qc+b\le1\) show \(F(a,b,c)\ge\mu_*\) everywhere: this is a global dual certificate. Symmetrization extends the conclusion to every original transition matrix, including asymmetric allocations of *edge weights* within each star (while the stochastic matrix itself remains symmetric).

When \(H_{p,q}>0\), the certificate has \(0<\theta<1\). Any other invariant optimizer must saturate both hub constraints (as both multipliers are strictly positive); along this one-dimensional segment, decreasing \(b\) increases the fixed quotient Rayleigh score, while increasing \(b\) increases \(1-c\). Thus the displayed invariant optimizer is unique.

**Sharpness of the frontier.** At a candidate with \(H_{p,q}<0\), move \(b\) slightly downward and keep the hubs saturated by setting \(a=(1-b)/p\), \(c=(1-b)/q\). The directional derivative of the quotient eigenvalue is \(-H_{p,q}/D>0\) with respect to increasing \(b\), whereas that of \(1-c\) is \(1/q>0\). Hence both active maximum branches strictly fall as \(b\) is reduced. All other eigenvalue moduli are strictly below \(\mu_*\) at the candidate by the spectral certificate; continuity makes the overall SLEM strictly smaller after a sufficiently small decrease. This proves the claimed failure below the frontier.

Finally, \(H_{p,q}=1-[p/(q-p)]^2-[(p+1-p/q)/(q-p)]^2\) is strictly increasing in real \(q>p\), from negative infinity to one. Direct substitution gives \(H_{p,2p}<0\) and \(H_{p,3p}>0\) for \(p\ge2\), so \(Q_p\) is unique in \((2p,3p)\). Substituting \(q=rp\) and letting \(p\to\infty\) yields \(1-2/(r-1)^2=0\), hence \(Q_p/p\to1+\sqrt2\).

## Verification

The companion `verify.py` uses exact rational arithmetic to test the four-cell characteristic identity at six points for each of 253 integer parameter pairs, and tests the dual-certificate equalities exactly in 145 above-frontier cases. Direct symmetric-eigenvalue computations confirm the displayed SLEM in all 145 cases; 20 below-frontier instances show strict local improvement, and 1120 feasible nonsymmetric edge allocations are sampled as additional checks. Results are reproduced in `verification_output.txt`. These finite tests are not a proof for the unbounded integer domain; the analytic argument above is.

## Relationship to prior work

Boyd, Diaconis, and Xiao [1] formulate the general fastest-mixing problem as semidefinite optimization. Boyd, Diaconis, Parrilo, and Xiao [2] develop automorphism and eigenspace reductions and explicitly solve a *balanced clique-barbell* graph. Neither of those inspected results classifies the present **unbalanced double-star** sharp threshold. Jafarizadeh [3], Section 6.7, gives bistar solutions subject to conditions (59)–(60), including \(\pi_{\mathrm{hub}}\Pi_{\mathrm{leaves}}\le\pi_{\mathrm{hub}}^2\). The uniform distribution with at least two leaves per hub fails that inequality, so its displayed formula and associated hypotheses do not cover the current domain. The claim concerns this previously excluded boundary regime, not the general previously solved interior regime.

## Limitations

No formula is given for the actual optimum below \(Q_p\), only a strict comparison with the candidate rational value. Uniqueness is asserted only among invariant matrices for \(q>Q_p\). The reported prior-work comparison is not a proof of historical publication priority; unlocated specialized formulas remain possible. No independent mathematical review has occurred.

## References

[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689; DOI: 10.1137/S0036144503423264. Accessible text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first public 2007-09-06, https://arxiv.org/abs/0709.0955.

[3] S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, DOI: 10.1109/TSIPN.2020.2964211; full-text version https://arxiv.org/abs/2501.02421, Section 6.7.
