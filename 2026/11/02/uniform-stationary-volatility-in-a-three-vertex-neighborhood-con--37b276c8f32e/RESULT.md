# Uniform stationary volatility in a three-vertex neighborhood-confidence path

## Finding

For the non-adaptive neighborhood Deffuant--Weisbuch (NDW) model of Krishnagopal and Porter, consider the undirected path of three agents, with endpoints of opinions \(a<b\) and a center of initial opinion \(y\in[a,b]\), all in \([0,1]\). Let \(d=b-a\), let \(\sigma\) be the neighborhood-tuning parameter, let \(\epsilon\) be the strict confidence bound, and let \(\rho\) be the compromise fraction. Select one of the two edges independently and uniformly at every step. Suppose
\[
0\le\sigma<\frac13,\qquad
\sigma d<\epsilon\le\frac{1-\sigma}{2}d,
\qquad 0<\rho\le\frac12.
\]
Then the following conclusions hold for every admissible \(a,b,y,\sigma,\epsilon,\rho\).

1. The endpoints never change opinions. The center opinion \(Y_t\) obeys exactly
   \[
   Y_{t+1}=(1-\rho)Y_t+\rho Z_t,
   \qquad\Pr(Z_t=a)=\Pr(Z_t=b)=\frac12,
   \]
   with independent draws \(Z_t\). Almost surely, \(\liminf_{t\to\infty}Y_t=a\) and \(\limsup_{t\to\infty}Y_t=b\); hence the center opinion does not converge along any almost-sure trajectory.
2. The center chain has a unique stationary law \(\mu_\rho\), described explicitly by
   \[
   a+\rho d\sum_{j=0}^{\infty}(1-\rho)^j B_j,
   \qquad B_j\stackrel{\mathrm{iid}}{\sim}\operatorname{Bernoulli}\left(\frac12\right).
   \]
   Its mean and variance are \(\frac{a+b}{2}\) and \(\frac{\rho d^2}{4(2-\rho)}\), respectively. The law of \(Y_t\) converges to \(\mu_\rho\) in Wasserstein distance at a geometric rate, and the empirical occupation measures of each trajectory converge weakly to \(\mu_\rho\) almost surely.
3. At exact compromise, \(\rho=1/2\), the stationary law is **uniform on the whole interval \([a,b]\)**. For each integer \(t\ge0\), \(Y_t\) is uniformly distributed over the \(2^t\) equally spaced points
   \[
   \left\{a+\frac{y-a+kd}{2^t}: k=0,\ldots,2^t-1\right\},
   \]
   and the exact first Wasserstein distance is
   \[
   \boxed{W_1(\mathcal L(Y_t),\operatorname{Unif}[a,b])
   =\frac{(y-a)^2+(b-y)^2}{2d\,2^t}.}
   \]
   Nevertheless the finite-time law and the stationary uniform law have total-variation distance one at every finite time.
4. The parameter inequalities describe exactly the **all-center-state, two-way receptive / endpoint-frozen regime**: for every possible center opinion in \([a,b]\), the center responds to either chosen endpoint and neither endpoint responds to the center if and only if \(\sigma d<\epsilon\le(1-\sigma)d/2\). This regime has nonempty interior precisely for \(\sigma<1/3\). Among connected graphs, three vertices are minimal for this nonconvergence mechanism: on two vertices, NDW is symmetric and every trajectory converges.

For example, \(a=0\), \(b=1\), \(y=1/2\), \(\sigma=1/4\), \(\epsilon=3/10\), and \(\rho=1/2\) satisfy the strict interior of the regime. With the same initial opinions and confidence radius, ordinary direct-distance DW makes no update at all, whereas neighborhood-aware DW exhibits perpetual sample-path motion and uniform long-run occupation.

## Assumptions and scope

There are exactly three vertices \(L,C,R\) and two fixed undirected edges \(LC,CR\). The network does not rewire, each vertex has weight one, and every time step samples precisely one edge independently and uniformly. Each endpoint of a sampled edge updates toward the other using the **pre-update** opinions, but only when its own directional mixed confidence distance is strictly less than \(\epsilon\). For distinct adjacent \(i,j\), that distance is
\[
\sigma |x_i-x_j|+(1-\sigma)
\left|x_i-\frac1{\deg(j)}\sum_{k\sim j}x_k\right|.
\]
The numerical parameter \(\rho\) lies in \((0,1/2]\) as in the original NDW compromise model. The result concerns the update model, not an imposed group of externally stubborn agents, not an adaptive or synchronous variant, and not the behavior for all values of the confidence parameters.

## Proof

**Step 1 (exact reduction).** Suppose the endpoint opinions are \(a,b\), and the center opinion is \(z\in[a,b]\). If edge \(LC\) is sampled, the center sees its donor \(L\) having the sole neighbor \(C\), so its neighborhood distance is \(|z-z|=0\). Its total confidence distance is therefore \(\sigma|z-a|\le\sigma d<\epsilon\); it always updates. The leaf \(L\), in contrast, sees the center's mean-neighbor opinion \((a+b)/2\), hence its confidence distance is
\[
\sigma|a-z|+(1-\sigma)d/2\ge(1-\sigma)d/2\ge\epsilon.
\]
Because the model uses a strict inequality, \(L\) never updates. Exactly the same argument applies to edge \(CR\). Thus both leaves remain fixed, and the center updates toward \(a\) or \(b\), each with probability \(1/2\). Convexity keeps \(Y_t\in[a,b]\) for all \(t\), closing the induction.

Conversely, if both directional center updates must be enabled for **all** \(z\in[a,b]\), the cases \(z=b\) on edge \(LC\) and \(z=a\) on edge \(CR\) force \(\sigma d<\epsilon\). For both leaves to be unreceptive for **all** center states, the cases \(z=a\) and \(z=b\) force \(\epsilon\le(1-\sigma)d/2\). The two inequalities are compatible exactly when \(\sigma<1/3\).

**Step 2 (almost-sure nonconvergence and full oscillation).** Independent fair edge selections contain arbitrarily long blocks of the \(L\)-edge and arbitrarily long blocks of the \(R\)-edge almost surely: for each fixed block length, apply independence to disjoint blocks and then intersect over positive integer lengths. After \(k\) successive selections of edge \(LC\), the center is at most \(a+(1-\rho)^kd\), regardless of its state before that block. After \(k\) successive selections of edge \(CR\), it is at least \(b-(1-\rho)^kd\). Together with \(Y_t\in[a,b]\), these inequalities give \(\liminf Y_t=a\) and \(\limsup Y_t=b\) almost surely. Since \(a<b\), no pathwise limit exists.

**Step 3 (stationary law and occupation).** Put \(q=1-\rho\), and take a doubly infinite sequence of iid fair endpoint samples \((Z_t)_{t\in\mathbb Z}\). The convergent series
\[
\overline Y_t=\rho\sum_{j\ge0}q^j Z_{t-1-j}
\]
defines a stationary ergodic chain satisfying \(\overline Y_{t+1}=q\overline Y_t+\rho Z_t\). This yields the asserted distribution after writing \(Z_t=a+dB_t\) and summing the deterministic \(a\)-part. Any two solutions driven by the same future endpoint choices differ by exactly \(q^t\) times their initial difference. Thus the stationary law is unique, and for any initial deterministic state \(y\),
\[
W_1(\mathcal L(Y_t),\mu_\rho)\le q^t d.
\]
The mean equation gives \(\mathbb E\overline Y=(a+b)/2\). Independence of the fresh sample and \(\overline Y_t\) gives \(\operatorname{Var}(\overline Y)=q^2\operatorname{Var}(\overline Y)+\rho^2d^2/4\), yielding the stated variance. Birkhoff's ergodic theorem for the doubly infinite iid sample shift gives occupation convergence for the stationary chain. Since \(|Y_t-\overline Y_t|\le q^td\), the same convergence holds for every initial \(y\) by uniform continuity of continuous test functions on the compact interval.

**Step 4 (uniform law and exact distance).** For \(\rho=1/2\), the stationary series is a binary expansion with independent fair digits, hence uniform on \([a,b]\). Iterating the recursion from \(y\) gives
\[
Y_t=a+\frac{y-a}{2^t}+\frac{dK_t}{2^t},
\qquad K_t\sim\operatorname{Unif}\{0,1,\ldots,2^t-1\}.
\]
Its atoms are one per interval of the regular \(2^t\)-partition of \([a,b]\). Quantile coupling to the continuous uniform law is optimal for the real-line \(W_1\) metric. Within each interval, integrating the absolute difference between its uniform coordinate and the atom at position \((y-a)/2^t\) produces the exact formula stated above. The finite law has finite support while uniform Lebesgue measure assigns that support zero mass, so their total-variation distance is one.

**Step 5 (minimal connected graph).** A connected two-vertex graph has only one edge, and each endpoint is the other's sole neighbor. Both neighborhood distances are identically zero. Thus the two directional confidence tests are identical, so either neither updates or both move symmetrically toward each other, contracting their gap by \(1-2\rho\). Once enabled, the interaction stays enabled; either way both opinions converge. A single vertex is trivially constant.

## Verification

The standalone standard-library Python program `verify.py` directly implements the two directional mixed-distance tests with exact fractions, without assuming the scalar reduction. Its checks include 808 direct edge-update comparisons across four rational admissible parameter configurations, 27 exact finite-time laws with independently integrated quantile Wasserstein distances, and eight stationary moment identities. All tests passed. These computations test representative rational cases; the quantified statements for arbitrary admissible real parameters follow from the proof, not from enumeration.

Run `python verify.py` with Python 3.9 or later. No external packages, files, network connections, or random number generation are required.

## Relationship to prior work

Krishnagopal and Porter (arXiv:2402.05368, first posted 2024-02-08) define the neighborhood-aware directional confidence rule and demonstrate nonstandard and sometimes nonconvergent behavior in numerical experiments. Their inspected model and simulation sections do not identify this exact minimal connected path, its parameter wedge, or its invariant and finite-time laws. The present theorem gives a concrete analytic explanation for persistent motion despite identical confidence parameters and unchanged network structure.

Weisbuch, Deffuant, Amblard and Nadal (arXiv:cond-mat/0111494) study symmetric direct-distance compromises; their convergence and clustering mechanism is different. Chen, Su, Mei and Bullo (arXiv:2409.01593) prove almost-sure convergence for a heterogeneous direct-distance DW rule. Their confidence tests use pairwise opinion distances rather than the donor's neighbor mean, and therefore do not apply to the directional mixed-neighborhood rule here.

The affine recursion, random binary-expansion stationary law, and Bernoulli-convolution representation are classical probability constructions; **they are not claimed as new general results**. For example, Cao and Cortez (arXiv:2601.21023) analyze related Bernoulli-convolution laws in a distinct large-population opinion model. What is asserted here is their exact emergence, together with the sharp directional receptivity region and persistent full-range oscillation, in the finite neighborhood-DW model of the first paper.

## Limitations

This theorem is specific to the fixed three-vertex path, independent fair single-edge sampling, and the displayed confidence parameter wedge. It does not classify behavior outside that wedge, arbitrary networks, adaptive edge rewiring, nonuniform edge selection, or the synchronous neighborhood-HK model. The stationary convergence is in distribution and in ergodic occupation, **not** pathwise or total variation at finite times. No claim of an independent external proof check or exhaustive literature priority is made; specialized equivalent results not surfaced by the inspected literature remain a residual priority risk.

## References

1. S. Krishnagopal and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Neighborhood Effects*, arXiv:2402.05368, first version posted 2024-02-08, https://arxiv.org/abs/2402.05368 ; model equations and simulations: https://arxiv.org/html/2402.05368.
2. G. Weisbuch, G. Deffuant, F. Amblard and J.-P. Nadal, *Interacting Agents and Continuous Opinions Dynamics*, arXiv:cond-mat/0111494, 2001, https://arxiv.org/abs/cond-mat/0111494.
3. G. Chen, W. Su, W. Mei and F. Bullo, *Convergence of the Heterogeneous Deffuant-Weisbuch Model: A Complete Proof and Some Extensions*, arXiv:2409.01593, 2024, https://arxiv.org/abs/2409.01593.
4. F. Cao and R. Cortez, *The fractal geometry of opinion formation*, arXiv:2601.21023, 2026, https://arxiv.org/abs/2601.21023.
