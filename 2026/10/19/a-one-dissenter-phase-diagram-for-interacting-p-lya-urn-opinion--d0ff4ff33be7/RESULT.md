# A one-dissenter phase diagram for interacting Pólya-urn opinion dynamics

## Finding

In the interacting Pólya-urn opinion model of Tang, Adler, Ajorlou, and Jadbabaie, take the unweighted complete simple graph on \(n\geq3\) people (no self-loops). One person has a fixed bias \(g>1\) toward declaring opinion \(1\); the other \(n-1\) people all have the same fixed bias \(0<h<1\) toward declaring opinion \(0\). Put
\[
h_0=\frac{n-1}{g+n-2},\qquad
h_1=\frac{g(n-2)+1}{g(n-1)},\qquad
h_{\mathrm{flip}}=\frac{g(n-2)+n}{gn+n-2}.
\]
Then \(0<h_0<h_{\mathrm{flip}}<h_1<1\), and the vector of historical declaration frequencies converges almost surely to a **deterministic** vector as follows:

* For \(h\le h_0\), every coordinate converges to \(0\).
* For \(h\ge h_1\), every coordinate converges to \(1\).
* For \(h_0<h<h_1\), the dissenter coordinate converges to \(x_*\) and each majority coordinate converges to \(y_*\), where
\[
y_* = \frac{h(g+n-2)-(n-1)}{(g-1)(1-h)(n-2)},\qquad
x_* = \frac{g y_*}{1+(g-1)y_*}.
\]
Here \(0<y_*<x_*<1\). This is the unique interior fixed point of the complete expected-dynamics map, and it is locally asymptotically stable for its associated continuous-time drift. Within the nonconsensus interval, the majority's limiting declared probability of opinion \(1\) exceeds \(1/2\) precisely when \(h>h_{\mathrm{flip}}\), even though every majority member has an inherent bias toward \(0\).

The entire nonconsensus window has the exact positive width
\[
h_1-h_0=\frac{(g-1)^2(n-2)}{g(n-1)(g+n-2)}.
\]
For a concrete case, \(n=5\), \(g=4\), and \(h=3/4\) give \((h_0,h_{\mathrm{flip}},h_1)=(4/7,17/23,13/16)\) and \((x_*,y_*)=(5/6,5/9)\).

## Assumptions and scope

The graph is \(K_n\) **without self-loops**, with equal unit edge weights. Every vertex observes the historical binary declarations of its \(n-1\) distinct neighbors. Initialization is by the strictly positive source-model counts: choose \(b_i^1\in(0,1)\), put \(b_i^0=1-b_i^1\), and let each vertex's initial neighbor count equal the sum of the corresponding \(b_j^s\). With \(\psi_{i,t}\in\{0,1\}\) the random declaration at time \(t\), define
\[
\beta_i(t)=\frac{b_i^1+\sum_{s=2}^t\psi_{i,s}}{t},\quad
\mu_i(t)=\frac{1}{n-1}\sum_{j\ne i}\beta_j(t),\quad
f(z,k)=\frac{kz}{1+(k-1)z}.
\]
Conditionally on the past, each agent independently declares \(1\) with probability \(f(\mu_i(t),\gamma_i)\), where \(\gamma_1=g\) and \(\gamma_i=h\) for \(i\geq2\). The expected map is \(F_i(\beta)=f((\sum_{j\ne i}\beta_j)/(n-1),\gamma_i)\). Source theorems for connected, nonbipartite undirected graphs apply because \(n\geq3\). All probabilities, limiting frequencies, and inequalities are over this exact model; no statement concerns a complete graph **with** self-loops, arbitrary topology, adaptive biases, or convergence of every individual binary declaration to a constant.

## Proof

**1. Equilibrium symmetry and completeness.** Suppose \(z=F(z)\). If two majority coordinates satisfy \(z_i>z_j\), then their neighbor means satisfy \(\mu_i<\mu_j\), whereas strict monotonicity of \(f(\cdot,h)\) yields \(z_i=f(\mu_i,h)<f(\mu_j,h)=z_j\), a contradiction. Hence all majority coordinates agree, say at \(y\), and the lone dissenter coordinate \(x\) satisfies \(x=f(y,g)\). The majority condition is
\[
y=f\left(\frac{x+(n-2)y}{n-1},h\right).
\]
Let \(m=(f(y,g)+(n-2)y)/(n-1)\). Clearing the strictly positive denominator
\[
D=(n-1)(1+(g-1)y)(1+(h-1)m)
\]
gives the exact identity
\[
D\,[y-f(m,h)]
=y(y-1)\left[(g-1)(h-1)(n-2)y+h(g+n-2)-(n-1)\right].
\]
Thus the only fixed points are the all-zero point, the all-one point, and, when its coordinates are strictly between zero and one, the stated rational interior point. Indeed its \(y\)-coordinate is positive exactly when \(h>h_0\), and less than one exactly when \(h<h_1\). The formula for \(x\) follows from the first fixed-point equation and obeys \(x>y\) for \(0<y<1\), \(g>1\). At either threshold the extra algebraic root merges with a boundary point, not an additional interior equilibrium.

**2. Boundary spectral thresholds.** Let \(W=(\mathbf 1\mathbf 1^\mathsf T-I)/(n-1)\) and \(\Gamma=\operatorname{diag}(g,h,\ldots,h)\). The source's Jacobians of \(F\) at the zero and one vectors are \(J_0=\Gamma W\) and \(J_1=\Gamma^{-1}W\). On vectors constant over the majority, these restrict respectively to
\[
B_0=\begin{pmatrix}0&g\\h/(n-1)&h(n-2)/(n-1)\end{pmatrix},\quad
B_1=\begin{pmatrix}0&1/g\\1/[h(n-1)]&(n-2)/[h(n-1)]\end{pmatrix}.
\]
Both matrices are irreducible nonnegative; their Perron eigenvalues are those of the full nonnegative Jacobians, since their positive Perron vectors lift to full positive vectors. Each has one positive and one negative eigenvalue, so evaluating its characteristic polynomial at \(1\) shows
\[
\rho(J_0)>1\iff h>h_0,\qquad
\rho(J_1)>1\iff h<h_1.
\]
Tang and collaborators' boundary theorem (Theorem 4) states that for these admissible connected nonbipartite urn dynamics, a boundary vector is the almost-sure limit if its Jacobian Perron eigenvalue is at most one, and cannot be the limit if it exceeds one. This immediately proves the claimed zero and one consensus regimes, **including equality at their thresholds**.

**3. The actual random limit inside the window.** Their equilibrium-approach theorem (Theorem 3) yields \(\operatorname{dist}(\beta(t),\operatorname{Fix}(F))\to0\) almost surely. The fixed-point set here is the finite set \(\{\mathbf0,\mathbf1,(x_*,y_*,\ldots,y_*)\}\). Moreover \(\|\beta(t+1)-\beta(t)\|_\infty\le1/(t+1)\). A sequence with vanishing increments whose distance to a finite separated set tends to zero must converge to one member of that set: after a sufficiently late time it cannot move between disjoint small neighborhoods without leaving their union. Inside the window both boundary Perron eigenvalues exceed one, so Theorem 4 excludes the two boundary limits. The unique possible limit is therefore the stated interior vector, with probability one. Continuity of \(f\) also makes the conditional probability of each forthcoming declaration converge to the corresponding coordinate.

**4. Local deterministic stability.** Write \(a=f'(y_*,g)>0\) and \(b=f'(m_*,h)>0\), where \(m_*=(x_*+(n-2)y_*)/(n-1)\). For the drift \(\dot z=F(z)-z\), majority-difference directions have eigenvalue \(-1-b/(n-1)<0\). The remaining two-dimensional Jacobian of \(F\) is
\[
B_*=\begin{pmatrix}0&a\\ b/(n-1)&b(n-2)/(n-1)\end{pmatrix}.
\]
Direct substitution of the rational fixed point gives
\[
\det(I-B_*)=1-\frac{b(n-2+a)}{n-1}
=\frac{[h(g+n-2)-(n-1)]\,[g(n-2)+1-gh(n-1)]}
{h(g-1)^2(n-2)}>0.
\]
Since \(B_*\) is irreducible nonnegative with a negative second eigenvalue, this proves its Perron eigenvalue is strictly below one. Every eigenvalue of \(B_*-I\) therefore has strictly negative real part. Hence the interior fixed point is locally asymptotically stable for the continuous-time expected drift.

**5. The majority's publicly reversed bias.** Solving \(y_*=1/2\) yields \(h=h_{\mathrm{flip}}\), and \(y_*\) increases strictly from zero to one across the nonconsensus interval. Direct subtraction yields
\[
h_{\mathrm{flip}}-h_0=\frac{(g-1)^2(n-2)}{(g+n-2)(gn+n-2)}>0,\quad
h_1-h_{\mathrm{flip}}=\frac{(g-1)^2(n-2)}{g(n-1)(gn+n-2)}>0.
\]
Consequently a majority biased privately toward \(0\) nonetheless declares \(1\) with limiting probability exceeding one-half in the upper part of the nonconsensus window. The identities also establish the asserted ordering and window width.

## Verification

The standalone `verify.py` uses rational arithmetic to check the denominator-clearing identity for \(4032\) choices of parameters and test inputs, and tests \(288\) interior cases for exact fixed-point equality, Perron sign inequalities, and positivity of the local-stability determinant. It also checks the worked example exactly. Running `python3 verify.py` reports `PASS`. This finite suite is a falsification aid, not a proof for arbitrary \(n,g,h\). The analytical proof above supplies those quantifiers.

## Relationship to prior work

Jadbabaie, Makur, Mossel, and Salhab introduced the interacting-urn model and solved a different homogeneous-honesty complete-graph setting, with equal honesty strength for opposing private-belief groups. Tang, Adler, Ajorlou, and Jadbabaie extended it to heterogeneous biases and general undirected graphs, proving convergence toward the *set* of equilibria and the boundary spectral consensus criterion. They explicitly identify determination, isolation, and uniqueness of interior equilibria as unresolved in their general setting. The result here does not strengthen those theorems globally: it solves the natural one-dissenter heterogeneous-bias **loopless** complete-graph specialization, supplies its unique interior point, and converts convergence-to-a-set into a deterministic almost-sure limit in the nonconsensus regime. The purely boundary threshold statements are applications of their Theorem 4; the fixed-point uniqueness, explicit positive interior law, public-majority reversal threshold, and interior local stability are established separately here.

## Limitations

The result relies on a single distinguished agent, a common second bias for everyone else, complete connectivity without self-loops, strictly positive initial counts, and the particular rational reinforcement function. It does not address unequal majority biases, networks with more than two bias classes, finite-time rates, or universal uniqueness of interior equilibria on arbitrary graphs. The stochastic convergence argument invokes the published convergence and boundary-exclusion theorems for this model; an independent audit of the full package has not been performed. An equivalent special-case calculation elsewhere in reinforced-urn literature is possible.

## References

1. Jennifer Tang, Aviv Adler, Amir Ajorlou, and Ali Jadbabaie, *Stochastic Opinion Dynamics under Social Pressure in Arbitrary Networks*, arXiv:2308.09275, first submitted 18 August 2023; see the public preprint (2024 revision), Sections II–V, particularly Theorems 3–4. https://arxiv.org/abs/2308.09275 ; https://web.mit.edu/jstang/www/papers/opinion_dynamics_convergence_jour_preprint.pdf
2. Ali Jadbabaie, Anuran Makur, Elchanan Mossel, and Rabih Salhab, *Inference in Opinion Dynamics under Social Pressure*, arXiv:2104.11172, first submitted 22 April 2021; see Sections 2 and 4 and the explicit homogeneous-honesty complete-graph equilibria. https://arxiv.org/abs/2104.11172
