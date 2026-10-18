# Exact fixed-size Smith-set asymptotics and the limiting rare-component geometry

## Finding
Fix integers \(\ell\ge2\) and \(s\ge3\), and put \(m=2\ell-1\). Under impartial culture, let \(S_{m,n}\) be the Smith set of \(n\) alternatives ranked independently and uniformly by \(m\) voters. For a nonnegative \(s\times m\) matrix \(y=(y_{ij})\), define the indicator \(H(y)\) to equal one if the majority tournament on the \(s\) rows, where each voter orders rows by increasing \(y_{ij}\), is strongly connected, and zero otherwise. Ties are immaterial null sets.

For each \(\ell\)-subset \(J\subseteq\{1,\ldots,m\}\), let
\[
V_J(y)=\operatorname{Leb}_{\ell}\left(\bigcup_{i=1}^{s}\prod_{j\in J}[0,y_{ij}]\right),\qquad
\Phi_{\ell,s}(y)=\sum_{|J|=\ell}V_J(y).
\]
Then the finite, strictly positive constant
\[
K_{\ell,s}=\frac1{s!}\int_{[0,\infty)^{ms}}H(y)\exp[-\Phi_{\ell,s}(y)]\,dy
\]
satisfies the exact sharp equivalent
\[
\boxed{\displaystyle \lim_{n\to\infty}n^{s(\ell-1)/\ell}\Pr\{|S_{m,n}|=s\}=K_{\ell,s}\in(0,\infty).}
\]
Moreover, represent rankings by independent uniform scores \(U_{ij}\in(0,1)\), smallest scores ranked highest. Conditional on \(|S_{m,n}|=s\), list its alternatives in increasing label order and collect their \(s\times m\) score matrix \(W_n\). Then \(n^{1/\ell}W_n\) converges in total variation to the probability density
\[
\boxed{\displaystyle p_{\ell,s}(y)=\frac{H(y)e^{-\Phi_{\ell,s}(y)}}{s!K_{\ell,s}}\quad\text{on }[0,\infty)^{ms}.}
\]
This is one local limit theorem: the probability constant is the total mass of the limiting unnormalized density, and the conditional geometry is its normalized version.

## Assumptions and scope
Every one of the \(m=2\ell-1\) voters samples a uniform independent strict ranking of the same \(n\) labeled alternatives. The integers \(\ell\ge2\) and \(s\ge3\) remain fixed as \(n\to\infty\). The Smith set is the unique smallest nonempty subset whose members each beat every alternative outside the subset in strict pairwise-majority voting. The case \(s=2\) is impossible in a tournament. The score coordinates are an auxiliary continuous representation of uniformly random rankings; the probability asymptotic is independent of that representation.

The coordinate-box volume can be computed by finite inclusion-exclusion:
\[
V_J(y)=\sum_{\varnothing\ne I\subseteq\{1,\ldots,s\}}(-1)^{|I|+1}\prod_{j\in J}\min_{i\in I}y_{ij}.
\]
Thus the leading coefficient is an explicit nonnegative integrable function on a fixed-dimensional orthant, with no unknown limiting probabilities or hidden normalization.

## Proof
**1. An exact finite-size integral.** Give alternative \(i\) independent scores \(U_{ij}\sim\operatorname{Unif}(0,1)\), and have voter \(j\) rank by increasing score. Fix alternatives \(1,\ldots,s\), with score matrix \(x\). An outside alternative with scores \(u=(u_1,\ldots,u_m)\) majority-beats at least one member of this set exactly when, for some \(i\le s\) and some \(\ell\)-subset \(J\) of voters, \(u_j<x_{ij}\) for every \(j\in J\). Let \(b(x)\) be the \(m\)-dimensional volume of the union of these finitely many cylinder boxes inside \([0,1]^m\). All other alternatives are conditionally independent, so the probability that the selected set dominates every outside alternative is \((1-b(x))^{n-s}\). A subset is the Smith set if and only if it is dominating and its induced majority tournament is strongly connected (the top strong component of a tournament is unique). Thus
\[
\Pr\{|S_{m,n}|=s\}=\binom ns\int_{[0,1]^{ms}}H(x)(1-b(x))^{n-s}\,dx.\tag{1}
\]
This exact identity also gives the joint unnormalized score density on the event \(S_{m,n}=\{1,\ldots,s\}\).

**2. Microscopic limit of the forbidden volume.** Fix a nonnegative matrix \(y\). Substitute \(x_{ij}=n^{-1/\ell}y_{ij}\), whenever all scaled coordinates are at most one. For a fixed voter subset \(J\) of size \(\ell\), the union over \(i\) of corresponding cylinders has probability exactly \(n^{-1}V_J(y)\). If two distinct \(\ell\)-subsets \(J,J'\) are involved, a point lying in both cylinder unions is constrained in at least \(\ell+1\) distinct voter coordinates. On every fixed bounded set of \(y\), this intersection is \(O(n^{-(\ell+1)/\ell})\), uniformly over the finitely many rows and subsets. Finite inclusion-exclusion therefore yields
\[
nb(n^{-1/\ell}y)\longrightarrow\sum_{|J|=\ell}V_J(y)=\Phi_{\ell,s}(y),
\]
pointwise for every fixed \(y\). Consequently,
\[
(1-b(n^{-1/\ell}y))^{n-s}\longrightarrow e^{-\Phi_{\ell,s}(y)}.
\]
Positive common scaling preserves each voter's within-core ordering, hence \(H(n^{-1/\ell}y)=H(y)\) away from ties.

**3. A uniform integrable majorant.** Define \(\sigma_{\ell}(z)=\sum_{|J|=\ell}\prod_{j\in J}z_j\) for \(z\in[0,\infty)^m\), and \(M=\binom m\ell\). Since a union of measurable events has measure at least the average of the measures of its \(sM\) constituent events,
\[
b(x)\ge\frac1{sM}\sum_{i=1}^s\sigma_{\ell}(x_{i1},\ldots,x_{im}).
\]
For \(n\ge2s\), the rescaled integrand extended by zero outside \([0,n^{1/\ell}]^{ms}\) is bounded above by
\[
\exp\left[-\frac1{2sM}\sum_{i=1}^s\sigma_{\ell}(y_{i1},\ldots,y_{im})\right].\tag{2}
\]
To prove this is integrable without an unverified tail assumption, it suffices to show for any \(c>0\) that \(\int_{[0,\infty)^m}e^{-c\sigma_{\ell}(z)}dz<\infty\). Sort coordinates \(z_1\ge\cdots\ge z_m\). Then \(\sigma_{\ell}(z)\ge z_1\cdots z_{\ell}\). Put \(t=z_{\ell}\) and \(z_i=te^{w_i}\) for \(1\le i<\ell\), with \(w_1\ge\cdots\ge w_{\ell-1}\ge0\). Integrating the last \(m-\ell\) ordered coordinates below \(t\) contributes \(t^{m-\ell}/(m-\ell)!\). The remaining Jacobian is \(t^{\ell-1}e^{W}\), where \(W=\sum_{i<\ell}w_i\). The integral in \(t\) is
\[
\int_0^{\infty}t^{m-1}e^{-ct^{\ell}e^W}\,dt
=\frac{\Gamma(m/\ell)}{\ell c^{m/\ell}}e^{-mW/\ell}.
\]
Including the Jacobian leaves \(e^{-(m/\ell-1)W}\), integrable over the ordered nonnegative \(w\)'s because \(m=2\ell-1>\ell\). Multiplying over the finitely many ordering regions proves integrability of (2).

**4. The sharp constant.** Apply dominated convergence to (1), with Jacobian \(n^{-ms/\ell}\). Since \(\binom ns n^{-s}\to1/s!\),
\[
\lim_{n\to\infty}n^{s(m/\ell-1)}\Pr\{|S_{m,n}|=s\}
=\frac1{s!}\int H(y)e^{-\Phi_{\ell,s}(y)}dy.
\]
The exponent reduces to \(s(\ell-1)/\ell\). Finiteness follows from (2). Positivity follows by partitioning the \(s\) candidates into three nonempty blocks and taking three cyclic voter orders over the blocks, with a common internal order in each block. These induce a strongly connected tournament; pair any extra voters in mutually reversed orders so majority results are unchanged. The corresponding score inequalities hold on a positive-volume open subset of a finite box, on which \(e^{-\Phi}>0\). Therefore \(K_{\ell,s}>0\).

**5. Conditional local geometry.** For a bounded measurable test function \(f\) of the \(s\times m\) scaled scores, exchangeability and uniqueness of the Smith set give the numerator
\[
\binom ns n^{-ms/\ell}\int_{[0,n^{1/\ell}]^{ms}}f(y)H(y)(1-b(n^{-1/\ell}y))^{n-s}\,dy.
\]
The \(L^1\) convergence of the nonnegative densities in this expression follows from pointwise convergence and the integrable majorant (2). Divide by the positive probability asymptotic from step 4. The resulting conditional densities converge in \(L^1\), hence in total variation, to \(H(y)e^{-\Phi(y)}/(s!K_{\ell,s})\). This also proves tightness and excludes mass escaping to large scaled scores.

## Verification
A standalone pure-Python check, `verification.py`, enumerates all triples of voters' strict rankings for \(n=3\) and \(n=4\). The exact Smith-set counts by size are \(\{1:204,3:12\}\) out of \(216\) profiles at \(n=3\), and \(\{1:12288,3:816,4:720\}\) out of \(13824\) profiles at \(n=4\). For every nonempty subset in every profile, the checker verifies the equivalence of being the Smith set and being both dominating and internally strongly connected: \(1512+207360=208872\) exact Boolean comparisons. With rational arithmetic, it also checks the finite inclusion-exclusion formula and the \(\ell=2,m=3,s=3\) cylinder-overlap expansion for seven distinct scales. The general asymptotic and tail integrability are justified analytically above rather than inferred from finite computations.

## Relationship to prior work
Berchenko and Liu (2026), Theorem 1.4, established the correct polynomial **order** \(\Theta_{\ell,s}(n^{-s(\ell-1)/\ell})\) for each fixed \(s\ge3\), and their §2.2 supplies explicit two-sided constants. They did not provide the exact leading constant or a limiting law for the appropriately rescaled score geometry. Their analytic score representation and the exact conditional independence of outside alternatives are essential antecedents; neither is claimed as new here. The new term \(\Phi_{\ell,s}\) retains the within-voter-subset overlaps between several core candidates, whereas bounding the union by sums or maxima loses the sharp coefficient. Sauermann (2022), Theorem 1, obtained an exact integral constant for \(s=1\), the single Condorcet-winner event; that theorem does not cover the internally strongly connected multi-candidate core with \(s\ge3\). Liu et al. (2025/2026) formulated the fixed-size behavior as a conjectural scale rather than a sharp multi-candidate coefficient. Known finite-majority-tournament enumerations are finite-rank probabilities and do not themselves imply the \(n\to\infty\) integral or conditional point-cloud limit.

## Limitations
The theorem assumes independent uniformly random voter rankings, a fixed odd number of at least three voters, and a fixed Smith-set size at least three. The constant is represented by a convergent multidimensional integral, not an elementary closed form. No quantitative convergence rate, uniformity in growing \(s\) or \(m\), even-voter tie model, heterogeneous voter distribution, or independent literature priority certification is claimed. Numerical checks cover small configurations only. A general asymptotic theory of random ranking top components might subsume this limit, and independent priority review is still needed.

## References
1. Z. Berchenko and K. Liu, *On the Cardinality of the Smith Set Under Impartial Culture with Many Alternatives*, arXiv:2610.03814v1, first posted 2026-10-01. https://arxiv.org/html/2610.03814v1
2. L. Sauermann, *On the probability of a Condorcet winner among a large number of alternatives*, arXiv:2203.13713v1, first posted 2022-03-25. https://arxiv.org/html/2203.13713v1
3. K. Liu, Q. Long, Z. Shi, W. J. Su, and J. Xiao, *Statistical Impossibility and Possibility of Aligning LLMs with Human Preferences: From Condorcet Paradox to Nash Equilibrium*, arXiv:2503.10990v2, first posted 2025-03-14. https://arxiv.org/html/2503.10990v2
