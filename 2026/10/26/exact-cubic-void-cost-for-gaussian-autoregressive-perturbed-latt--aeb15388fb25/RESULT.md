# Exact cubic void-cost for Gaussian autoregressive perturbed lattices

## Finding

**Theorem.** Fix \(\sigma>0\) and \(0\leq\rho<1\). Let \((P_j)_{j\in\mathbb Z}\) be the centered stationary Gaussian autoregressive sequence with
\[
\operatorname{Cov}(P_i,P_j)=\sigma^2\rho^{|i-j|}.
\]
Independently choose \(U\) uniformly on \([0,1)\), and form the stationary point process
\[
\Xi=\sum_{j\in\mathbb Z}\delta_{j+P_j+U}.
\]
For \(L>0\), let \(V(L)=\mathbb P\{\Xi([0,L])=0\}\). Then \(0<V(L)<1\) and
\[
\boxed{\displaystyle\lim_{L\to\infty}\frac{-\log V(L)}{L^3}
=\frac{1-\rho}{24\sigma^2(1+\rho)}.}
\]
Equivalently, if \(\Lambda=\sum_{k\in\mathbb Z}\operatorname{Cov}(P_0,P_k)=\sigma^2(1+\rho)/(1-\rho)\), the exact logarithmic void-cost is \(1/(24\Lambda)\). This is a fixed-parameter limit, not a claim uniform as \(\rho\uparrow1\).

## Assumptions and scope

The sequence can be realized by \(P_{j+1}=\rho P_j+\sigma\sqrt{1-\rho^2}\,Z_{j+1}\), with independent standard Gaussian innovations and its stationary initial distribution. The joint law is defined on the entire two-sided integer lattice; the backward Markov transition has the same autoregressive coefficient. Only nonnegative correlations \(0\leq\rho<1\), strictly positive fixed marginal variance, and an interval observation window are considered. The stationary shift \(U\) is independent of every displacement.

The random counting measure is locally finite almost surely: the sum, over integer sites, of the probabilities of landing in a fixed bounded interval is finite by Gaussian tails. Consequently its void probabilities are well defined. In this model every finite interval has strictly positive void probability, as established by the explicit finite-block construction and the summable tails below. The probability is strictly below one since, for example, an interior site has positive probability of landing inside the interval.

## Proof

It suffices first to consider a positive integer length \(N\). Write \(E_N=\{\Xi([0,N])=0\}\), and put
\[
\Lambda=\sigma^2\frac{1+\rho}{1-\rho}.
\]

**1. Necessary quadratic displacement for a hole.** For every \(i\in\{0,\ldots,N\}\), the event \(E_N\) forces
\[
P_i<-i-U\quad\text{or}\quad P_i>N-i-U.
\]
Because \(0\le U<1\), this entails \(|P_i|\ge d_{i,N}\), where
\[
d_{i,N}=\max\{0,\min\{i,N-i-1\}\}.
\]
Consequently \(\sum_{i=0}^N P_i^2\ge S_N:=\sum_{i=0}^N d_{i,N}^2\), and elementary summation (or a Riemann sum) gives
\[
S_N=\frac{N^3}{12}+O(N^2).
\]
Let \(\Gamma_N=(\sigma^2\rho^{|i-j|})_{0\le i,j\le N}\). Its spectral norm is bounded by its maximum absolute row sum, which is at most \(\Lambda\). For each fixed \(0<\varepsilon<1\), the Gaussian quadratic exponential moment therefore satisfies
\[
\mathbb E\exp\left\{\frac{1-\varepsilon}{2\Lambda}\sum_{i=0}^N P_i^2\right\}
=\det\left(I-\frac{1-\varepsilon}{\Lambda}\Gamma_N\right)^{-1/2}
\le\varepsilon^{-(N+1)/2}.
\]
Markov's inequality, applied to the necessary event, yields
\[
V(N)\le\exp\left\{-\frac{1-\varepsilon}{2\Lambda}S_N
+\frac{N+1}{2}\log(\varepsilon^{-1})\right\}.
\]
Dividing the logarithm by \(N^3\), sending \(N\to\infty\), and then \(\varepsilon\downarrow0\), proves
\[
\liminf_{N\to\infty}\frac{-\log V(N)}{N^3}\ge\frac1{24\Lambda}.
\]

**2. Constructing a matching-energy hole.** Define a deterministic displacement profile on \(\{-N,\ldots,2N\}\):
\[
b_{i,N}=\begin{cases}
-(i+2),&0\le i\le\lfloor N/2\rfloor,\\
N-i+2,&\lfloor N/2\rfloor<i\le N,\\
0,&-N\le i<0\ \text{or}\ N<i\le2N.
\end{cases}
\]
Fix \(\eta=1/8\). Let \(A_N\) be the event that \(U\in[1/4,1/2]\) and \(|P_i-b_{i,N}|\le\eta\) simultaneously for all \(-N\le i\le2N\). On this event every point with index in this block lies strictly outside \([0,N]\): the middle sites fall either below \(-1\) or above \(N+1\), while the exterior block sites remain respectively below zero and above \(N\).

Set \(b_i=b_{i,N}\). Direct summation gives
\[
\sum_{i=-N}^{2N}b_i^2=\frac{N^3}{12}+O(N^2),\qquad
\sum_{i=-N}^{2N-1}(b_{i+1}-b_i)^2=O(N^2).
\]
The second estimate allows one jump of order \(N\) where the two evacuation directions meet; all other nonzero increments are bounded. Since \(b_{-N}=b_{2N}=0\), discrete summation by parts gives the **exact identity**
\[
\sum_{i=-N}^{2N-1}(b_{i+1}-\rho b_i)^2
=(1-\rho)^2\sum_{i=-N}^{2N}b_i^2
+\rho\sum_{i=-N}^{2N-1}(b_{i+1}-b_i)^2.
\]
Therefore
\[
\sum_{i=-N}^{2N-1}(b_{i+1}-\rho b_i)^2
=\frac{(1-\rho)^2N^3}{12}+O(N^2).
\]

**3. Probability of the block profile.** By the Gaussian Markov property, the joint density of \((P_{-N},\ldots,P_{2N})\) is a normalizing factor of exponential order \(\exp\{O(N)\}\) multiplied by
\[
\exp\left\{-\frac{P_{-N}^2}{2\sigma^2}
-\frac{1}{2\sigma^2(1-\rho^2)}\sum_{i=-N}^{2N-1}(P_{i+1}-\rho P_i)^2\right\}.
\]
Inside the prescribed box of radius \(\eta\), the deviation of the quadratic energy from its value at \(b\) is at most \(O(N^2)\), because \(\sum |b_{i+1}-\rho b_i|=O(N^2)\) and every coordinate error is bounded. The box has volume \((2\eta)^{3N+1}=\exp\{-O(N)\}\), and the independent shift restriction has probability \(1/4\). Integrating the joint density over it thus proves
\[
\mathbb P(A_N)\ge\exp\left\{-\frac{(1-\rho)^2}{24\sigma^2(1-\rho^2)}N^3-O(N^2)\right\}
=\exp\left\{-\frac{N^3}{24\Lambda}-O(N^2)\right\}.
\]
All constants implicit in the remainder may depend on the fixed parameters but not on \(N\).

**4. All omitted sites are harmless with high conditional probability.** Conditional on the entire finite block of displacements and on \(U\), the two exterior one-sided chains evolve in forward or reverse stationary AR(1) fashion from their respective endpoints. Under \(A_N\), these endpoints satisfy \(|P_{-N}|,|P_{2N}|\le\eta\). At distance \(k\ge1\) outside the block, each conditional displacement is Gaussian with mean of absolute value at most \(\eta\) and variance at most \(\sigma^2\). To enter \([0,N]\), the corresponding outer site must undergo displacement with absolute value at least \(N+k-1\). A Gaussian tail bound and a union bound show, uniformly over the conditioning allowed by \(A_N\), that
\[
\mathbb P\bigl(\exists i\notin[-N,2N]:i+P_i+U\in[0,N]\mid A_N\bigr)
\le C\sum_{k\ge1}e^{-c(N+k)^2}=o(1).
\]
Hence \(V(N)\ge\mathbb P(A_N)(1-o(1))\), and therefore
\[
\limsup_{N\to\infty}\frac{-\log V(N)}{N^3}\le\frac1{24\Lambda}.
\]
Combining with Step 1 proves the integer-length limit.

**5. Arbitrary lengths.** For every real \(L\ge1\), monotonicity of interval holes gives
\[
V(\lceil L\rceil)\le V(L)\le V(\lfloor L\rfloor).
\]
As both integer bounds have the same cubic logarithmic asymptotic and \(\lfloor L\rfloor/L\to1\), the claimed limit follows. \(\square\)

## Verification

The included Python 3 program `check.py` uses only the standard library and exact rational arithmetic. Running `python3 check.py` performed 15,353 finite assertions. It checks exact covariance–precision inversion for multiple autoregressive coefficients and variances, the row-sum eigenvalue bound, the deterministic evacuation profile at all displayed sites and admissible shift/box extremes, and the exact energy identity and finite-size approach to the cubic coefficients. It also prints the coefficients for four rational correlations. These computations validate algebraic test instances; the infinite-volume result is proved by the Gaussian exponential-moment bound and Markov-path construction above.

## Relationship to prior work

Flimmel, *Void probabilities for perturbed lattices under mixing* (arXiv:2610.24650v1, publicly submitted 17 October 2026), studies the same stationary perturbed-lattice framework. Its Theorem 2 and Corollary 1 provide general mixing-based bounds, including stretched-exponential decay for exponentially mixing fields; these do not give a cubic rate or its constant. Its independent-perturbation discussion explicitly distinguishes an earlier order-level Gaussian result.

Elboim, Spinka and Yakir, *Optimal matchings of randomly perturbed lattices* (arXiv:2506.16873v1), Lemma 2.5, establish two-sided logarithmic-order estimates for independent displacement fields. Their bounds neither provide an exact cubic coefficient nor treat correlated autoregressive fields. The independent specialization of the present theorem is not asserted as a fundamentally new mechanism; the dependence-sensitive exact coefficient is the central finding.

Gabrielli, *Point processes and stochastic displacement fields* (arXiv:cond-mat/0409594), studies pair correlations and spectra of correlated displacement fields, not this many-site hole asymptotic. Flimmel, *Fitting regular point patterns with a hyperuniform perturbed lattice* (arXiv:2503.12179), establishes Gaussian models' second-order properties and an explicit \(K\)-function. Such second-order formulas alone do not identify the exponentially rare joint void event.

The coefficient can be rewritten using the displacement field's long-run variance \(\Lambda\), linking the many-site evacuation cost directly to dependence, rather than simply to the marginal Gaussian variance.

## Limitations

The proof requires a fixed AR(1) coefficient in \([0,1)\), positive fixed marginal variance, a one-dimensional lattice, an independent stationarizing shift, and a single growing interval. No uniformity near the perfectly correlated boundary \(\rho=1\), negative correlation formula, higher-dimensional statement, or prefactor beyond the leading logarithmic exponential rate is established. Equivalence to a more general previously available Gaussian obstacle large-deviation principle remains a literature risk; no exhaustive novelty certification is claimed. External independent mathematical validation has not been performed.

## References

1. D. Flimmel, *Void probabilities for perturbed lattices under mixing*, arXiv:2610.24650v1 (first public 17 October 2026), https://arxiv.org/html/2610.24650v1.
2. D. Elboim, Y. Spinka, O. Yakir, *Optimal matchings of randomly perturbed lattices*, arXiv:2506.16873v1 (20 June 2025), https://arxiv.org/pdf/2506.16873.
3. A. Gabrielli, *Point processes and stochastic displacement fields*, arXiv:cond-mat/0409594v1 (22 September 2004), https://arxiv.org/pdf/cond-mat/0409594.
4. D. Flimmel, *Fitting regular point patterns with a hyperuniform perturbed lattice*, arXiv:2503.12179 (15 March 2025), https://arxiv.org/abs/2503.12179.
