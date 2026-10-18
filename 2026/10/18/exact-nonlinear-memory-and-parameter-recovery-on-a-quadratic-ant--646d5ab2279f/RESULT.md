# Exact nonlinear memory and parameter recovery on a quadratic anti-integrable hyperbola

## Finding

The hyperbolic anti-integrable quadratic correspondence of Hampton and Meiss has, under fair independent branch selection, an exactly solvable nonlinear dependence signature. For every \(d>0\) and \(|r|<2\sqrt d\), define the two branches

\[
f_s(x)=s\sqrt{\frac{1+d x^2+r x}{1+d}},\qquad s\in\{-1,1\}.
\]

There is a unique stationary two-sided process \((X_t)_{t\in\mathbb Z}\) obtained by applying \(f_{S_t}\), where the \(S_t\) are independent fair signs. The process is bounded and ergodic, its signs are independent fair signs, and it is a martingale difference sequence with

\[
\mathbb E X_t=0,\qquad \mathbb E X_t^2=1,\qquad
\operatorname{Cov}(X_t,X_{t-k})=0\quad(k\ge1).
\]

Nevertheless, setting \(Z_t=X_t^2-1\), its exact nonlinear temporal statistics are, for every integer \(k\ge0\),

\[
\operatorname{Cov}(Z_t,Z_{t-k})
=\frac{r^2}{1+2d}\left(\frac d{1+d}\right)^k,
\]

and, for every integer \(k\ge1\),

\[
\operatorname{Cov}(Z_t,X_{t-k})
=\frac r{1+d}\left(\frac d{1+d}\right)^{k-1},
\qquad
\operatorname{Cov}(X_t,Z_{t-k})=0.
\]

Thus \(\mathbb E X_t^4=1+r^2/(1+2d)\). If \(r\ne0\), the coordinates are pairwise linearly uncorrelated but not independent. More sharply, two mixed lag moments \(B_1=\mathbb E[Z_t X_{t-1}]\) and \(B_2=\mathbb E[Z_t X_{t-2}]\) recover both parameters without ambiguity:

\[
d=\frac{B_2}{B_1-B_2},\qquad
r=\frac{B_1^2}{B_1-B_2}.
\]

The one-time marginal, in contrast, is identical for the parameters \(r\) and \(-r\); it cannot detect the sign of \(r\). If \(r=0\), then \(X_t=S_t\) is an independent fair-sign sequence, and the parameter \(d\) cannot be recovered from any coordinate time-series distribution.

All stationary even moments are also determined by a finite triangular recurrence. With \(M_0=1\), \(M_{2k}=\mathbb E X_t^{2k}\), for \(k\ge1\),

\[
M_{2k}=\frac{1}{(1+d)^k-d^k}
\sum_{j=0}^{k-1}
\sum_{\substack{0\le\ell\le k-j\\ \ell\ \mathrm{even}}}
\frac{k!}{j!\ell!(k-j-\ell)!}\,d^j r^\ell M_{2j+\ell}.
\]

All odd marginal moments vanish. The recurrence gives, for example, \(M_2=1\) and \(M_4=1+r^2/(1+2d)\).

## Assumptions and scope

The parameters are real and satisfy exactly \(d>0\) and \(|r|<2\sqrt d\). The driving branch choices form a bi-infinite product Bernoulli measure with probability \(1/2\) for each sign, independent over all times. The result concerns the limiting quadratic correspondence

\[
(1+d)X_t^2-dX_{t-1}^2=rX_{t-1}+1,
\]

which is the \(c=-d\), \(a=1-c=1+d\), \(b=0\) specialization of the source's equations (9) and (12). It does not assert any stationary-law identity for the finite-parameter three-dimensional diffeomorphism from which the limiting relation arises. The measure is the pushforward of the fair Bernoulli branch measure, not an asserted physical measure of that finite-parameter map.

## Proof

**1. Global contraction and existence.** The radicand obeys

\[
1+d x^2+r x=d\left(x+\frac r{2d}\right)^2+1-\frac{r^2}{4d}>0
\]

for all real \(x\). Put \(g(x)=\sqrt{(1+d x^2+r x)/(1+d)}\). A direct derivative calculation gives

\[
|g'(x)|^2=\frac{(2dx+r)^2}{4(1+d)(1+d x^2+r x)}
\le \frac d{1+d}=:q^2<1,
\]

because \(4d(1+d x^2+r x)-(2dx+r)^2=4d-r^2>0\). Consequently each branch is globally \(q\)-Lipschitz and satisfies \(|f_s(x)|\le (1+d)^{-1/2}+q|x|\). Starting at zero at time \(-n\), iterating the prescribed signs to any fixed time produces a uniformly bounded sequence; the common-tail contraction estimate makes these iterates Cauchy as \(n\to\infty\). The resulting pullback limit is bounded by \(K=[\sqrt{1+d}(1-q)]^{-1}\), is shift-equivariant and solves the correspondence at every integer time. Contraction makes it the only bounded solution for each sign history and yields the unique invariant probability for the fair-branch Markov kernel by a Wasserstein contraction. The stationary process is ergodic as a factor of the Bernoulli shift. Since \(g(x)>0\), its coordinate sign is exactly the fresh fair sign \(S_t\).

**2. Conditional cancellations and the stationary variance.** Let \(\mathcal F_t=\sigma(S_j:j\le t)\). The state \(X_{t-1}\) is measurable with respect to \(\mathcal F_{t-1}\), while \(S_t\) is independent of that sigma field and has mean zero. Thus

\[
\mathbb E[X_t^{2m+1}\mid\mathcal F_{t-1}]=0
\quad(m\ge0),
\]

and \(\mathbb E[X_t\mid\mathcal F_{t-1}]=0\). In particular, all odd moments and every positive-lag linear covariance vanish. Squaring the recurrence and taking stationary expectations gives \((1+d)\mathbb E X_t^2=d\mathbb E X_t^2+1\), hence \(\mathbb E X_t^2=1\).

**3. Complete low-order lag identities.** Set \(a_*=d/(1+d)\), \(b_*=r/(1+d)\). Subtracting the stationary mean square from the defining relation yields the exact pathwise identity

\[
Z_t=a_*Z_{t-1}+b_*X_{t-1}.
\]

Since \(\mathbb E[Z_tX_t]=\mathbb E X_t^3-\mathbb E X_t=0\), taking its variance gives \(V=a_*^2V+b_*^2\), so \(V=r^2/(1+2d)\). Taking covariance with \(Z_{t-k}\) shows \(\operatorname{Cov}(Z_t,Z_{t-k})=a_*^kV\): the cross term with \(X_{t-1}\) is zero even when \(k=1\), by the odd-moment identity, and for \(k>1\), by the martingale-difference identity. Likewise, covariance with \(X_{t-k}\) equals \(b_*\) when \(k=1\), and satisfies the factor-\(a_*\) recursion for \(k>1\). The reversed mixed covariance vanishes by conditional centering of the later \(X_t\). This proves the displayed infinite families, the fourth moment, and the failure of independence when \(r\ne0\), since the lag-one squared covariance is strictly positive.

**4. Identification and sign symmetry.** From the mixed-moment formulas, \(B_1=b_*\), \(B_2=a_*b_*\). For \(r\ne0\), \(B_1-B_2=(1-a_*)b_*\ne0\); elementary elimination gives exactly the two recovery formulas. Each transition kernel is symmetric under output sign reversal, so its stationary marginal is symmetric. Reflecting the input and changing \(r\) to \(-r\) preserves the squared radicand; uniqueness of the stationary law therefore implies that the one-time marginals for opposite \(r\) coincide. When \(r=0\), the constant-magnitude solution \(X_t=S_t\) satisfies the recurrence, and pullback uniqueness proves that it is the entire stationary process for every \(d>0\).

**5. Complete polynomial moments.** In stationarity,

\[
(1+d)^k M_{2k}=\mathbb E(1+dX_{t-1}^2+rX_{t-1})^k.
\]

Expand the right side by the multinomial theorem. Every term with an odd number of factors \(rX_{t-1}\) vanishes by marginal sign symmetry. The sole term involving \(M_{2k}\) is \(d^kM_{2k}\); moving it to the left produces the displayed recurrence, whose denominator is strictly positive. Compact support justifies all moments and implies that this moment sequence uniquely determines the one-time marginal.

## Verification

The accompanying standalone program `verify.py` checks the algebraic moment identities at exact rational parameter points and carries out seeded finite-sample tests of the second/fourth moments and the two mixed correlations. It passed 210 exact rational identities and 20 statistical diagnostics at four admissible parameter pairs. These computations do not certify infinite-time or continuum statements; the proof above supplies those results. To reproduce, run `python3 verify.py` in a standard Python 3 environment without additional dependencies.

## Relationship to prior work

Hampton and Meiss, *Connecting Anti-integrability to Attractors for Three-Dimensional, Quadratic Diffeomorphisms* (arXiv:2305.06302v1, §2 equations (9),(12), §3 and §4.3), introduce exactly this hyperbolic quadratic correspondence, and establish one-to-one correspondence with symbolic sequences in the domain \(c<-r^2/4\). Neither the branch equation nor its symbolic bijection is claimed here. Their preceding paper (arXiv:2107.09776) treats the anti-integrability coding and contraction geometry; Chen (arXiv:2402.10536) studies topological conjugacy and continuation to hyperbolic orbits. The contribution here is a measure-specific, parameter-identifying description of all lagged quadratic and mixed moments of the fair-symbolic state, plus a closed hierarchy of all stationary polynomial moments. General martingale/conditional-variance techniques underlie the calculation; no novelty is claimed for those general techniques.

## Limitations

The complete statements are specific to **fair independent branch symbols** and to the nondegenerate global-contraction hyperbolic wedge. Other shift-invariant symbolic measures generally do not obey these moment identities. The theorem describes the limiting correspondence, not continued three-dimensional map dynamics, and does not determine an SRB measure or physical observability. Parameter recovery uses population expectations and does not quantify statistical estimation error. The exact marginal symmetry hides the sign of \(r\) but does not assert that marginals are identical for different \(|r|\) or different \(d\). An equivalent model-specific statement in unindexed literature cannot be excluded; full independent priority audit remains outstanding.

## References

1. A. E. Hampton and J. D. Meiss, *Connecting Anti-integrability to Attractors for Three-Dimensional, Quadratic Diffeomorphisms*, arXiv:2305.06302v1 (first posted 2023-05-10), SIAM Journal on Applied Dynamical Systems 23 (2024), 616–640; doi:10.1137/23M1571897. https://arxiv.org/html/2305.06302v1
2. A. E. Hampton and J. D. Meiss, *Anti-integrability for Three-Dimensional Quadratic Maps*, arXiv:2107.09776 (2021), SIAM Journal on Applied Dynamical Systems 21 (2022), 650–675. https://arxiv.org/abs/2107.09776
3. Y.-C. Chen, *On a Question of J. D. Meiss Concerning Anti-integrability for Three-Dimensional Quadratic Diffeomorphisms*, arXiv:2402.10536 (2024). https://arxiv.org/abs/2402.10536
