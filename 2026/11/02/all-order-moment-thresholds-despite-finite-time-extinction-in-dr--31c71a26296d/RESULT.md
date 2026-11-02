# All-order moment thresholds despite finite-time extinction in dropout-averaged iterations

## Finding

Consider a two-lag moving-average iteration whose complete update is independently dropped at random. In exact arithmetic, every sample path becomes identically zero after a finite waiting time, but sufficiently large retained multipliers can make its moments grow exponentially. The phenomenon has a sharp threshold for **every positive integer moment order**, and those thresholds approach one as the order grows.

Write \(w=1-r\), where \(0<r<1\). Let independent coefficients \(A_t\) equal \(M>0\) with probability \(w\) and zero with probability \(r\). Start at \(Y_{-1}=Y_0=1\) and iterate
\[
Y_t=\frac{A_t}{2}(Y_{t-1}+Y_{t-2}),\qquad t\ge1.
\]
The first consecutive pair of zero coefficients makes the entire subsequent trajectory identically zero, and no shorter sequence can do so. If \(T\) denotes the index of the **second zero in the first consecutive pair**, then
\[
\mathbb P(T<\infty)=1,\qquad \mathbb E[T]=\frac{1+r}{r^2}.
\]
For an integer \(k\ge1\), let \(B_k(M,w)\) be the \((k+1)\)-by-\((k+1)\) matrix with row and column indices \(0,\ldots,k\), defined by
\[
(B_k)_{i,j}=\begin{cases}
w(M/2)^{k-i}\binom{k-i}{j},&0\le i<k,\quad 0\le j\le k-i,\\
1,&i=k,\quad j=0,\\
0,&\text{otherwise.}
\end{cases}
\]
For every \(k\ge1\) there is exactly one \(M_k(w)>1\) at which the Perron root \(\rho(B_k(M,w))\) is one. The following is an **if-and-only-if classification**:
\[
\begin{array}{c|c}
M<M_k(w)&\mathbb E[Y_t^k]\to0\text{ exponentially}\\
M=M_k(w)&\mathbb E[Y_t^k]\to c_k\in(0,\infty)\\
M>M_k(w)&\mathbb E[Y_t^k]\to\infty\text{ exponentially}.
\end{array}
\]
The first thresholds are explicit:
\[
M_1(w)=\frac1w,\qquad M_2(w)=\frac{\sqrt{1+8/w}-1}{2}<M_1(w).
\]
For every \(k\ge1\), \(M_{k+1}(w)\le M_k(w)\), and
\[
\boxed{\lim_{k\to\infty}M_k(w)=1.}
\]
In particular, choosing \(M_2(w)<M<M_1(w)\) yields a vanishing mean and exploding second moment at exponential rates, although every path reaches zero exactly in finite time.

## Assumptions and scope

Every draw is independent of the past and of all other draws; there are no additive innovations. We take strictly positive deterministic initial values \(Y_{-1}=Y_0=1\). Moments are ordinary, nonnegative integer moments; the matrix formula and critical classifications hold at each fixed integer \(k\). Stability is moment stability, not stationarity of a process with persistent additive noise. A positive Perron root is the spectral radius of a nonnegative matrix.

## Proof

**Finite-time absorption.** Because both initial values are positive and \(M>0\), a single zero coefficient makes precisely one new iterate zero; the following iterate remains positive if the next coefficient is nonzero. Hence the first pair of consecutive zero coefficients is exactly the time when the state pair becomes \((0,0)\). Such a pair occurs almost surely by independent disjoint trials. For the expected number of draws, let \(u\) be the remaining expectation when the previous draw was nonzero, and \(v\) when the previous draw was zero. First-step conditioning gives \(u=1+wu+rv\) and \(v=1+wu\), whence \(u=(1+r)/r^2\). The initial fictitious previous draw is nonzero, so this is \(\mathbb E[T]\). The surviving-state transition matrix \(\bigl(\begin{smallmatrix}w&r\\ w&0\end{smallmatrix}\bigr)\) has Perron root \(\kappa=(w+\sqrt{w^2+4wr})/2<1\), giving a geometric tail for \(T\).

**Closed moment dynamics.** For fixed integer \(k\ge1\) define \(Z_t^{(i)}=\mathbb E[Y_t^{k-i}Y_{t-1}^{i}]\), for \(i=0,\ldots,k\). For \(i<k\), a zero coefficient contributes zero. Conditioning on the positive coefficient and using the binomial theorem yields
\[
Z_t^{(i)}=w(M/2)^{k-i}\sum_{j=0}^{k-i}\binom{k-i}{j}Z_{t-1}^{(j)},\qquad Z_t^{(k)}=Z_{t-1}^{(0)}.
\]
Thus \(Z_t=B_k^t\boldsymbol 1\). All entries of the first row of \(B_k\) are positive, every other row links to column zero, and the first row has a self-loop; therefore \(B_k\) is primitive. Perron–Frobenius theory gives a positive simple dominant eigenvalue and strictly positive left and right eigenvectors. It follows that the first component \(\mathbb E Y_t^k\) has an asymptotic positive constant times \(\rho(B_k)^t\), with convergence to a finite positive limit when \(\rho(B_k)=1\).

**A unique threshold.** At \(M=0\), the matrix \(B_k\) is nilpotent. For fixed \(w\in(0,1)\), increasing \(M>0\) strictly increases at least one entry of the primitive nonnegative matrix, hence strictly increases its Perron root; the dependence is continuous. The first diagonal entry \(w(M/2)^k\) shows that the root tends to infinity as \(M\to\infty\). At \(M=1\), the recursion is an average of nonnegative values not exceeding one. Each mixed moment is at most the probability of a still-unabsorbed state pair, which decays geometrically by the survival matrix. Hence \(\rho(B_k(1,w))<1\). The intermediate value theorem and strict monotonicity give a unique \(M_k(w)>1\).

**First thresholds.** For \(k=1\), the moment map is \(\bigl(\begin{smallmatrix}wM/2&wM/2\\1&0\end{smallmatrix}\bigr)\); the equation \(\det(I-B_1)=0\) is \(wM=1\). For \(k=2\), direct substitution gives \(\det(I-B_2)=1-w(M^2+M)/2\). Its positive zero gives the displayed \(M_2\), strictly below \(M_1\) because \(w(M_1^2+M_1)/2=(1+w)/(2w)>1\).

**All-order threshold hierarchy.** For nonnegative random variables, \(\mathbb E Y_t^k\le(\mathbb E Y_t^{k+1})^{k/(k+1)}\). Therefore if the \((k+1)\)-st moment decays exponentially, the \(k\)-th also decays, and so \(M_{k+1}\le M_k\). To identify the limit, fix any \(M>1\). On the event that the first \(t\) coefficients are all \(M\) (probability \(w^t\)), the deterministic recursion has dominant characteristic root
\[
R_M=\frac{M+\sqrt{M^2+8M}}4>1.
\]
Its positive solution starting from \((1,1)\) is at least \(c_MR_M^t\) for all sufficiently large \(t\), with \(c_M>0\). Consequently \(\mathbb E Y_t^k\ge c_M^k(wR_M^k)^t\) for such \(t\). For all sufficiently large \(k\), \(wR_M^k>1\), so \(M>M_k(w)\). Since this holds for every \(M>1\), while all \(M_k(w)>1\), the monotone threshold sequence converges to one. This concludes the classification.

## Verification

The included standard-library `verify_moments.py` independently enumerates every Bernoulli path for short horizons and compares its exact rational mixed moments with matrix powers for six moment orders and multiple retained multipliers and probabilities. It also checks the displayed first two threshold equations and survival-time formula. The finite enumeration corroborates the recurrences; it is not a proof of the infinite-horizon Perron statements.

Run with `python3 verify_moments.py` in an isolated directory containing the extracted file.

## Relationship to prior work

Epperlein and Wirth (2026) study deterministic moving-average stability for linear maps; their accessible abstract does not establish a randomly dropped update, finite-time absorption, or the all-integer-order moment phase diagram. Classical random-coefficient autoregressive theory, including Feigin and Tweedie (1985), establishes broad stationarity and moment methodologies, and Lu and Skelton (2002) give a general mean-square small-gain framework. The second-moment stability test belongs to this established line of work; it is **not** claimed independently novel. The new contribution claimed here is the complete exact all-integer-order threshold hierarchy, its critical limits, and the coexistence of eventual zero paths with exponential moment growth for this specific natural recurrence. Published general moment criteria might subsume parts of this formulation; see the recorded priority risks.

## Limitations

The multipliers have exactly two atoms, one at zero; the initial pair is strictly positive; and the average has exactly two equally weighted delays. The thresholds for orders beyond two are defined by explicit finite nonnegative matrices, not closed radical formulas. The statement does not provide finite-precision performance, guarantees for nonlinear systems or arbitrary random coefficients, or independent mathematical certification. The 2026 motivating preprint's full text and the complete 1985 primary article could not be inspected, leaving an identifiable historical-priority risk.

## References

1. J. Epperlein and F. Wirth, *Moving-Average Iteration of Linear Maps* (2026), arXiv:2609.21442, https://arxiv.org/abs/2609.21442 (first publicly submitted September 18, 2026).
2. P. D. Feigin and R. L. Tweedie, *Random Coefficient Autoregressive Processes: A Markov Chain Analysis of Stationarity and Finiteness of Moments*, *Journal of Time Series Analysis* **6** (1985), 1–14, https://doi.org/10.1111/j.1467-9892.1985.tb00394.x.
3. J. Lu and R. E. Skelton, *Mean-square small gain theorem for stochastic control: discrete-time case*, *IEEE Transactions on Automatic Control* **47** (2002), 490–494, https://doi.org/10.1109/9.989147.
4. *On moment dynamics of stochastically delayed linear control systems* (2020), https://doi.org/10.1002/rnc.5218.
