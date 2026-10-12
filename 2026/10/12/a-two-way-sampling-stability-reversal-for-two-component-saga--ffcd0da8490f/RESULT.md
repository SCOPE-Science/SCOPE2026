# A two-way sampling-stability reversal for two-component SAGA

## Finding
For the original SAGA gradient-memory update, neither independent sampling with replacement nor random reshuffling has a universal mean-square stability advantage, even for two smooth strongly convex scalar components. The two exact witnesses are:

* Equal curvature: \(a=b=1\), \(\eta=23/20\). Independent uniform sampling is geometrically mean-square convergent, but independently reshuffling the two indices in each epoch produces an exponentially growing subsequence of expected squared position errors from the standard initialization.
* Unequal curvature: \(a=1\), \(b=4\), \(\eta=27/100\). Independent uniform reshuffling is geometrically mean-square convergent, but independent uniform sampling with replacement produces an exponentially growing subsequence of expected squared position errors from the same standard initialization.

Each strict contrast persists on a nonempty open neighborhood of its parameters. The finding therefore gives a two-way obstruction to any unconditional mean-square stability ordering between the two sampling rules. In particular, the first witness shows that the difference is not caused by heterogeneity between component objectives.

## Assumptions and scope
Let \(a,b,\eta>0\) and \(f_1(x)=a x^2/2\), \(f_2(x)=b x^2/2\) for real \(x\), so the common minimizer is zero. At iteration \(k\), write the state as \(z_k=(x_k,y_{1,k},y_{2,k})^\mathsf T\), where \(y_{i,k}\) is a saved component gradient. Choosing index \(i\) uses the OLD table in the update
\[
x_{k+1}=x_k-\eta\bigl(a_i x_k-y_{i,k}+(y_{1,k}+y_{2,k})/2\bigr),\qquad y_{i,k+1}=a_i x_k,
\]
with the other saved gradient unchanged, where \(a_1=a\), \(a_2=b\). This is the pre-update-table recursion of the original SAGA algorithm, not a variant saving a gradient at \(x_{k+1}\). Initially \(x_0=1\), \(y_{1,0}=a\), \(y_{2,0}=b\), as obtained by evaluating both gradients at the initial point.

Under **iid sampling**, every index is an independent fair draw. Under **random reshuffling**, every epoch independently chooses order \((1,2)\) or \((2,1)\) with equal probability; one epoch has exactly two iterations. A regime is *geometrically mean-square convergent for every initial state* if there exist \(C<\infty\), \(0<r<1\) for which \(\mathbb E\|z_k\|_2^2\le Cr^k\|z_0\|_2^2\). Exponential-subsequence divergence means the stated limsup of roots of \(\mathbb E x_k^2\) exceeds one, with the epoch index used for reshuffling. No almost-sure divergence claim is made.

## Proof
A choice of index acts linearly as \(z_{k+1}=M_i z_k\), with
\[
M_1=\begin{pmatrix}1-\eta a&\eta/2&-\eta/2\\ a&0&0\\0&0&1\end{pmatrix},\qquad
M_2=\begin{pmatrix}1-\eta b&-\eta/2&\eta/2\\ 0&1&0\\ b&0&0\end{pmatrix}.
\]
For any \(3\times3\) matrix \(M\), let \(L(M)\) be the uniquely determined \(6\times6\) matrix satisfying \(v(Mz)=L(M)v(z)\), with
\[
v(z)=(x^2,y_1^2,y_2^2,xy_1,xy_2,y_1y_2)^\mathsf T.
\]
The complete second-moment transitions are exactly
\[
K_{\mathrm{iid}}=\tfrac12(L(M_1)+L(M_2)),\qquad
K_{\mathrm{rr}}=\tfrac12(L(M_2M_1)+L(M_1M_2)).
\]
These equalities follow by expanding the six quadratic monomials and using independent fair choices at successive iid steps or independent fair permutations at successive epochs.

**Stable half of the first witness.** For \(a=b=1\), \(\eta=23/20\), the symmetric integer matrix
\[
Q=\begin{pmatrix}253&-53&-53\\-53&230&-114\\-53&-114&230\end{pmatrix}
\]
has leading principal minors \(253\), \(55381\), \(8163120\). Direct rational matrix multiplication gives the leading principal minors of \(R=Q-\tfrac12(M_1^\mathsf TQM_1+M_2^\mathsf TQM_2)\) as
\[
563/400,\qquad 789489/640000,\qquad 5427/5120.
\]
They are strictly positive. Sylvester's criterion makes \(Q\) and \(R\) positive definite, and conditional expectation of \(z_{k+1}^\mathsf TQz_{k+1}\) is \(z_k^\mathsf T(Q-R)z_k\). Hence iid sampling contracts a positive-definite quadratic energy geometrically, uniformly over all initial states.

**Stable half of the second witness.** For \(a=1\), \(b=4\), \(\eta=27/100\), apply the same argument to the two-step epoch matrices \(M_2M_1\) and \(M_1M_2\), now taking
\[
Q=\begin{pmatrix}259&5&-34\\5&3&-3\\-34&-3&9\end{pmatrix}.
\]
Its leading principal minors are \(259\), \(752\), \(1989\). The leading principal minors of the epoch residual \(R=Q-\tfrac12\sum_{P\in\{M_2M_1,M_1M_2\}}P^\mathsf TQP\) are
\[
\frac{192531773}{50000000},\quad
\frac{7694776875239369}{1600000000000000},\quad
\frac{2268049442949819}{640000000000000}.
\]
They are strictly positive. Thus the epoch-start state contracts geometrically in mean square. The intermediate state is bounded by a fixed matrix norm, so convergence also holds at all iterations.

**Unstable half of the first witness.** Start with \(z_0=(1,1,1)^\mathsf T\). Exact inversion of \(I-zK_{\mathrm{rr}}\), where here \(z\) is a scalar generating-function variable, yields
\[
\sum_{m=0}^\infty\mathbb E[x_{2m}^2]z^m
=\frac{20(529z-1600)(206839z^2+1405760z-2560000)}
{328253493z^4-1825585348z^3-11250326720z^2-72110592000z+81920000000}.
\]
The denominator is positive at \(z=0\) and equals \(-2938250575\) at \(z=1\), so it vanishes at some \(z\in(0,1)\). Neither numerator factor vanishes in that interval: both are negative there. The singularity is therefore a genuine pole strictly inside the unit disk.

**Unstable half of the second witness.** Start with \(z_0=(1,1,4)^\mathsf T\). For iid sampling,
\[
\sum_{k=0}^\infty\mathbb E[x_k^2]z^k
=-\frac{2(54347409z^4-173494916z^3-101122080z^2+679180800z-512000000)}
{16342911z^5-123128728z^4+265787536z^3+269193600z^2-1466521600z+1024000000}.
\]
The denominator is positive at \(z=0\) and equals \(-14326281\) at \(z=1\). The quartic numerator factor is strictly negative on \([0,1]\): its degree-four Bernstein coefficients there are
\[
-512000000,\;-342204800,\;-189263280,\;-96549169,\;-53088787.
\]
All Bernstein basis functions are nonnegative and sum to one. Again an uncancelled pole occurs in \((0,1)\). Each generating function has nonnegative coefficients because they are squared-error expectations. The Cauchy-Hadamard formula therefore gives \(\limsup (\mathbb E x_{2m}^2)^{1/m}>1\) in the first case and \(\limsup (\mathbb E x_k^2)^{1/k}>1\) in the second, establishing exponential growth along subsequences, not just failure of a numerical heuristic.

Finally, every displayed positivity inequality is strict, and the poles are separated from the unit-circle boundary and from numerator zeros. The finite-dimensional matrix and rational-function coefficients depend continuously on \((a,b,\eta)\), so both comparisons persist under sufficiently small perturbations. No maximal perturbation neighborhood is asserted.

## Verification
Run `python verify.py` using Python 3 with SymPy. This recomputes the two exact SAGA matrices and their six-dimensional quadratic lifts, validates the composition law, confirms positive definiteness of both Lyapunov matrices and their exact residuals by principal minors, reconstructs the two rational generating functions, verifies an uncancelled pole in \((0,1)\), and checks path enumeration independently for six lengths per unstable sampling scheme. All coefficients and sign tests use exact rational arithmetic; no floating-point spectral calculations enter the proof. The source of `verify.py` is embedded in the same package.

## Relationship to prior work
Defazio, Bach and Lacoste-Julien (2014) define original SAGA with stored gradients evaluated at the **pre-update** point; that is the algorithm used here. Ying, Yuan and Sayed (2017) establish convergence for random-reshuffling variance reduction under sufficiently small steps but their displayed reshuffling algorithm stores the **post-update** point for the selected component. The distinction makes their recursion different from the present one, and their sufficient small-step theorem does not imply either reversal. Qian, Qu and Richtárik (2019) analyze SAGA with iid arbitrary sampling and sufficient step bounds, not the same two-way comparison against independently reshuffled epochs. Nguyen and colleagues' (2021) shuffling convergence bounds address a broader SGD-type family and do not give these exact pre-update SAGA stability contrasts. Exact same-claim coverage was not found in the targeted comparisons; this does not establish priority against unindexed literature.

## Limitations
The examples involve exactly two scalar strongly convex quadratics and a constant, explicitly stated step size. The positive Lyapunov certificates prove all-state mean-square convergence only for the stable half of each example; the generating functions prove an exponentially growing subsequence of position MSE from the standard initialization on the unstable half. No exact general stability frontier, asymptotic wall-clock advantage, almost-sure divergence, or extension to other memory update conventions, nonlinear objectives or larger data sets is asserted. A specialized equivalent calculation in unindexed work remains possible.

## References
1. A. Defazio, F. Bach, S. Lacoste-Julien, *SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives*, arXiv:1407.0202 (first submitted 2014-07-01), https://arxiv.org/abs/1407.0202.
2. B. Ying, K. Yuan, A. H. Sayed, *Variance-Reduced Stochastic Learning under Random Reshuffling*, arXiv:1708.01383 (first submitted 2017-08-04), https://arxiv.org/abs/1708.01383.
3. X. Qian, Z. Qu, P. Richtárik, *SAGA with Arbitrary Sampling*, arXiv:1901.08669 (first submitted 2019-01-24), https://arxiv.org/abs/1901.08669.
4. L. M. Nguyen, Q. Tran-Dinh, D. T. Phan, P. H. Nguyen, M. van Dijk, *A Unified Convergence Analysis for Shuffling-Type Gradient Methods*, JMLR 22(207), 2021, https://www.jmlr.org/papers/v22/20-1238.html.
