# Mobility-controlled reversal of encounter hazards on complete bipartite networks

## Finding
For any integers \(m,n\ge 2\), let two independent continuous-time random walkers move on the complete bipartite graph \(K_{m,n}\). Each walker located in the part \(A\) of size \(m\) jumps at total rate \(\alpha>0\), choosing a uniformly random neighbor in the other part. In part \(B\) of size \(n\), the jump rate is \(\beta>0\). Stop both walkers at their first meeting time \(T\).

For two distinct starting vertices in \(A\), write \(h_A(t)\) for the meeting-time hazard; similarly use \(h_B(t)\) for distinct starting vertices in \(B\) and \(h_D(t)\) for walkers initially in different parts. For every \(t\ge 0\), the three hazards are well defined and satisfy the complete classification:

- \(h_D\) is strictly decreasing for all positive rates and all \(m,n\ge2\).
- \(h_A\) is strictly increasing if \(\alpha\le\beta\); if \(\alpha>\beta\), it is strictly increasing up to one finite positive time and strictly decreasing thereafter.
- \(h_B\) is strictly increasing if \(\beta\le\alpha\); if \(\beta>\alpha\), it is strictly increasing up to one finite positive time and strictly decreasing thereafter.

Thus the unique mobility threshold is equality of jump rates, **independently of the two part sizes**. Initial placement in the faster part creates exactly one peak in the encounter hazard, whereas placement in the slower part creates a monotonically increasing hazard. All claims concern the entire hazard curve, not just its mean or asymptotic rate.

The exact meeting-time Laplace transforms are given in the Proof section. With \(\kappa=\beta/m+\alpha/n\), the initial hazards obey \(h_A(0)=h_B(0)=0\), \(h_D(0)=\kappa\), and the initial slopes are \(h_A'(0)=2\alpha\kappa>0\), \(h_B'(0)=2\beta\kappa>0\). Every hazard tends to the same positive limiting decay rate \(\lambda_1\), the smallest eigenvalue of the finite transient generator defined below.

## Assumptions and scope
The graph is simple, undirected, complete bipartite, and has both part sizes at least two. Each walker changes its exponential waiting-time parameter whenever its current vertex changes part: these are **location-dependent**, not permanently walker-specific, jump rates. Each jump chooses a vertex in the opposite part uniformly. The walkers move independently until they coincide, at which instant the process is killed. There are no holding moves, simultaneous jump events, edge-dependent rates within a part, or additional walkers. Every initial pair consists of distinct vertices, so \(T>0\) almost surely. The survival function is \(S_X(t)=\Pr(T>t\mid X)\) for \(X\in\{A,B,D\}\), and \(h_X(t)=-S_X'(t)/S_X(t)\). Because absorption is almost sure in finite time and all transient states communicate, \(S_X(t)>0\) for every finite \(t\).

## Proof
**Lumping by relative placement.** The ordered two-walker process before first collision is exactly lumpable into three transient classes: \(A\), when both are at distinct sites in the first part; \(B\), when both are at distinct sites in the second part; and \(D\), when they are in different parts. Set
\[
 p=\beta\frac{m-1}{m},\quad q=\alpha\frac{n-1}{n},\quad
 \kappa=\frac{\beta}{m}+\frac{\alpha}{n},\quad u=\alpha+\beta.
\]
In state \(A\), either walker jumps at rate \(\alpha\) into the other part, so \(A\to D\) occurs at rate \(2\alpha\). Likewise, \(B\to D\) has rate \(2\beta\). From \(D\), the walker in \(B\) jumps into an unoccupied \(A\)-vertex at rate \(p\), creating class \(A\); the walker in \(A\) similarly creates class \(B\) at rate \(q\). The remaining jumps meet the other walker, at total rate \(\kappa\). The transient generator is therefore
\[
 Q=\begin{pmatrix}
 -2\alpha&0&2\alpha\\
 0&-2\beta&2\beta\\
 p&q&-u
 \end{pmatrix},\qquad -Q\boldsymbol{1}=(0,0,\kappa)^{\mathsf T}.
\]
This derivation is valid for every individual ordered pair in the indicated classes; no averaging over starting vertices is used.

**Exact transforms.** For \(s\ge0\), let \(F_X(s)=\mathbb E[e^{-sT}\mid X]\). First-step conditioning gives
\[
 (s+2\alpha)F_A=2\alpha F_D,\qquad
 (s+2\beta)F_B=2\beta F_D,\qquad
 (s+u)F_D=\kappa+pF_A+qF_B.
\]
Define the cubic
\[
 \Delta(s)=(s+u)(s+2\alpha)(s+2\beta)
 -2\alpha p(s+2\beta)-2\beta q(s+2\alpha).
\]
Since \(\Delta(0)=4\alpha\beta\kappa>0\), solving the equations yields
\[
 F_A(s)=\frac{2\alpha\kappa(s+2\beta)}{\Delta(s)},\qquad
 F_B(s)=\frac{2\beta\kappa(s+2\alpha)}{\Delta(s)},\qquad
 F_D(s)=\frac{\kappa(s+2\alpha)(s+2\beta)}{\Delta(s)}.
\]
These rational identities provide the full meeting-time laws, not merely their first moments.

**Real poles and their order.** The matrix \(Q\) is diagonally symmetrizable: the positive edges of its state graph form the path \(A-D-B\). The symmetrized matrix has a positive killing rate at \(D\), so \(-Q\) is positive definite with three simple positive eigenvalues \(\lambda_1<\lambda_2<\lambda_3\). When \(\alpha\ne\beta\), strict eigenvalue interlacing for the two-by-two principal diagonal submatrix, or equivalently the strictly decreasing secular function
\[
 u-\lambda-\frac{2\alpha p}{2\alpha-\lambda}
 -\frac{2\beta q}{2\beta-\lambda},
\]
shows
\[
 0<\lambda_1<2\min(\alpha,\beta)<\lambda_2
 <2\max(\alpha,\beta)<\lambda_3.
\]
When \(\alpha=\beta\), one eigenvalue equals \(2\alpha\), while the other two strictly straddle it.

**Signs of the survival modes.** Write \(S_X(t)=\sum_{j=1}^3 c_{Xj}e^{-\lambda_jt}\), allowing a zero coefficient in the equal-rate case. Let \(N_X(s)\) be the numerator of \(F_X(s)\) above. Since \(F_X(s)\) is the transform of \(-S_X'(t)\), partial fractions give
\[
 c_{Xj}=\frac{N_X(-\lambda_j)}{\lambda_j\Delta'(-\lambda_j)}.
\]
The signs of \(\Delta'(-\lambda_j)\) are respectively \((+,-,+)\). For \(D\), the signs of \((2\alpha-\lambda_j)(2\beta-\lambda_j)\) are also \((+,-,+)\). Hence every nonzero \(c_{Dj}\) is positive, with at least two positive coefficients. For \(A\), the signs are
\[
 c_{A1}>0,\qquad c_{A3}<0,\qquad
 \operatorname{sgn}(c_{A2})=\operatorname{sgn}(\alpha-\beta)
 \quad(\alpha\ne\beta).
\]
Similarly, \(c_{B1}>0\), \(c_{B3}<0\), and \(\operatorname{sgn}(c_{B2})=\operatorname{sgn}(\beta-\alpha)\). At equal rates, the middle coefficients vanish by cancellation. These signs do not depend on \(m\) or \(n\) except through the strict positivity of \(p,q\).

**Hazard-shape classification.** For any exponential sum \(S(t)=\sum_j c_je^{-\lambda_jt}>0\), direct differentiation gives
\[
 h'(t)=-\frac{\sum_{i<j}c_ic_j(\lambda_i-\lambda_j)^2
 e^{-(\lambda_i+\lambda_j)t}}{S(t)^2}.
\]
For \(D\), all contributing pairs have positive coefficients, so \(h_D'(t)<0\).

Suppose \(\alpha<\beta\) and start in \(A\). The three signs are \((+,-,-)\), so
\[
 S_A(t)=e^{-\lambda_1t}\big[c_{A1}
 -|c_{A2}|e^{-(\lambda_2-\lambda_1)t}
 -|c_{A3}|e^{-(\lambda_3-\lambda_1)t}\big].
\]
The bracket is positive and strictly increasing, with strictly negative second derivative. Therefore \(h_A=\lambda_1-(\log\text{bracket})'\) is strictly increasing. The same argument applies at equal rates, when the middle term vanishes.

Now suppose \(\alpha>\beta\), giving signs \((+,+,-)\). Multiplying the numerator of the displayed derivative identity by \(e^{(\lambda_1+\lambda_2)t}\) changes its negative into
\[
 -c_{A1}c_{A2}(\lambda_2-\lambda_1)^2
 +c_{A1}|c_{A3}|(\lambda_3-\lambda_1)^2
 e^{-(\lambda_3-\lambda_2)t}
 +c_{A2}|c_{A3}|(\lambda_3-\lambda_2)^2
 e^{-(\lambda_3-\lambda_1)t}.
\]
This expression is strictly decreasing from a positive value at \(t=0\): positivity follows from \(h_A'(0)=2\alpha\kappa>0\). Its limit is strictly negative. Thus it has one and only one zero in \((0,\infty)\), proving the unique peak. Interchanging the parts completes the proof for \(B\). All hazards tend to \(\lambda_1\), since each slowest-mode coefficient is positive. \(\square\)

## Verification
The included program `verify.py` builds the full ordered-pair Markov generator directly from the graph, without using the three-state reduction, and solves rational backward equations for transforms at several nonnegative arguments. It compares these full-state transforms with the displayed rational functions exactly, using Python standard-library rational arithmetic. It also checks predicted spectral signs and hazard-shape changes numerically in separate sample configurations. Run `python verify.py` using Python 3; no external packages are required. In the recorded run, 426 exact-rational transform comparisons and 18 separate spectral-hazard classifications passed. These finite checks corroborate, but do not replace, the general proof above.

## Relationship to prior work
Zhang, Tan, and Krishnamachari (2014, arXiv:1408.2005v1) analyze expected meeting times on regular graphs for discrete-time walkers, particularly circles and tori. Ohwa (2015, DOI:10.1186/s40736-015-0016-2) provides backward-transform methods for multiple walkers and explicitly analyzes continuous-time meeting times on stars, cycles, and complete graphs, allowing rates that differ **between walkers**. Neither evaluated treatment establishes the present **location-dependent bipartite mobility threshold** or the complete monotone/unimodal hazard classification for arbitrary part sizes. General finite-state phase-type methods explain why rational transforms and exponential sums arise; the specific coefficient-sign change and its topology-independent kinetic threshold are the additional conclusions.

Equal location rates recover the familiar separation between initially same-part increasing hazards and initially different-part decreasing hazards in balanced multipartite models. The new strictly unimodal branch for a faster starting part is absent under that equality condition and cannot be inferred by merely substituting graph size into an equal-rate formula.

## Limitations
The result is restricted to independent walkers before their first meeting, two complete bipartite classes of size at least two, uniform neighbor choice, exponential holding times, and class-constant (location-dependent) jump rates. It does not classify general heterogeneous graphs, additional walkers, walker-intrinsic speeds, or the subsequent dynamics after the first encounter. General first-passage phase-type theory may provide alternative derivations; the bibliographic comparison is not an absolute proof of priority. The unique peak is established analytically, while no elementary closed formula for its time is asserted for arbitrary parameters.

## References
1. Y. Zhang, Z. Tan, and B. Krishnamachari, *On the Meeting Time for Two Random Walks on a Regular Graph*, arXiv:1408.2005v1 (first posted 2014-08-09), https://arxiv.org/abs/1408.2005.
2. T. Ohwa, *Exact computation for meeting times and infection times of random walks on graphs*, Pacific Journal of Mathematics for Industry 7 (2015), article 5, published 2015-07-22, DOI:10.1186/s40736-015-0016-2, https://link.springer.com/article/10.1186/s40736-015-0016-2.
