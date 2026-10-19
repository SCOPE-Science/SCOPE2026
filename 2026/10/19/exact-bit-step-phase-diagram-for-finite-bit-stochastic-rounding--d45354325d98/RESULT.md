# Exact bit-step phase diagram for finite-bit stochastic-rounding descent

## Finding
Consider independent, truncation-based stochastic rounding to the integer grid with \(b=2^r\) equiprobable random thresholds, followed at every step of scalar gradient descent for \(f(x)=\tfrac12(x-\tau)^2\), \(0<\tau<1\). With \(0<\eta<1\) and \(c=b\eta\), all absorbing states and the complete stationary law on the adjacent pair \(\{0,1\}\) have explicit formulas:
\[
\#\{\text{absorbing lattice states}\}=\max\{0,\lceil c^{-1}-\tau\rceil\}, \qquad
\Pr_{\mathrm{stat}}\{X=1\}=\frac{\lfloor c\tau\rfloor}{\lfloor c\tau\rfloor+\lceil c(1-\tau)\rceil}.
\]
The only absorbing points are nonpositive integers, and the sharp threshold for eliminating *all* such nonstationary traps is \(c\tau\geq1\). For every positive integer \(m=b\eta<b\), the stationary mean simplifies to the staircase law \(\lfloor m\tau\rfloor/m\), which can decrease when the stepsize increases. The stationary mean never exceeds \(\tau\), whereas ideal unbiased stochastic rounding has stationary mean exactly \(\tau\). All these conclusions are for the stated fixed-grid and single-rounding model, not arbitrary floating-point computations.

## Assumptions and scope
Let \(r\ge1\) be an integer, \(b=2^r\), \(\tau\in(0,1)\), and \(\eta\in(0,1)\). Represent the working numbers on \(\mathbb Z\) (unit grid); gradients and affine proposals are evaluated exactly and only the final proposed state is rounded. Define independent uniform \(U_n\in\{0,1,\ldots,b-1\}\) and
\[
Q_b(y)=\lfloor y\rfloor+\mathbf1\!\left\{U_n<\lfloor b\{y\}\rfloor\right\},\qquad
X_{n+1}=Q_b\!\left((1-\eta)X_n+\eta\tau\right),\quad X_0\in\mathbb Z.
\]
Here \(\{y\}=y-\lfloor y\rfloor\). All equalities below refer to exact real probabilities and arithmetic. This is a fixed-point / equal-unit-in-last-place specialization of stochastic rounding with the extra bits **truncated** before drawing the random threshold. In a floating-point binade of constant spacing the model applies after a common affine change of coordinates only if the full computational trajectory remains in that binade and only the final conversion is rounded.

## Proof
**1. Every absorbing integer.** Write \(T(j)=j+\eta(\tau-j)\). If \(j\le0\), then \(T(j)>j\). It can round back to \(j\) with probability one precisely if \(T(j)-j<1/b\): below this strict threshold the first \(r\) fractional bits are zero; at equality, the probability of an upward step is \(1/b\). If \(T(j)-j\ge1\), it certainly does not remain at \(j\). If \(j\ge1\), \(T(j)<j\), and the probability of a downward rounded step is strictly positive, even if its magnitude is arbitrarily small. Therefore the complete absorbing set is
\[
\{j\in\mathbb Z:j\le0,\quad j>\tau-1/(b\eta)\},
\]
with the cardinality in the Finding. Since \(f'(j)=j-\tau\neq0\) at every such integer, these are all nonstationary. The set is empty if and only if \(b\eta\tau\ge1\); the endpoint is nonabsorbing.

**2. Invariant pair and its transition matrix.** The affine proposal at \(0\) lies in \((0,1)\), while the proposal at \(1\) lies in \((0,1)\); hence \(\{0,1\}\) is closed. Put
\[
u=\frac{\lfloor c\tau\rfloor}{b},\qquad
 d=\frac{\lceil c(1-\tau)\rceil}{b},\qquad c=b\eta.
\]
The row-stochastic matrix on ordered states \((0,1)\) is
\[
P=\begin{pmatrix}1-u&u\\d&1-d\end{pmatrix}.
\]
One has \(0\le u<1\), \(0<d\le1\), and the unique stationary law on this class has mass \(\pi=u/(u+d)\) at \(1\). If \(u=0\), the class includes an absorbing zero and still has this unique stationary law. For every start within the pair,
\[
\Pr\{X_n=1\}=\pi+\bigl(\Pr\{X_0=1\}-\pi\bigr)(1-u-d)^n.
\]
The right-hand side converges since \(|1-u-d|<1\): this follows from \(u+d>0\), and \(u+d<2\) because \(u<1\); when \(d=1\), necessarily \(u=0\) under \(c<b\), so the eigenvalue is zero. The same stationary law is the unique global limiting law for each fixed integer initial state when \(c\tau\ge1\): outside the closed pair, the chain moves monotonically towards that pair on a finite set between its initial point and the pair, and every non-pair state has a positive chance of making an inward move. If traps exist, no uniqueness for arbitrary starts is asserted.

**3. Bias and integer resonance.** Write \(\alpha=c\tau-\lfloor c\tau\rfloor\in[0,1)\) and \(\beta=\lceil c(1-\tau)\rceil-c(1-\tau)\in[0,1)\). Then
\[
\tau-\pi=\frac{(1-\tau)\alpha+\tau\beta}{c+\beta-\alpha}\ge0.
\]
For integer \(c=m\), one has \(\lfloor m\tau\rfloor+\lceil m(1-\tau)\rceil=m\), proving \(\pi=\lfloor m\tau\rfloor/m\). With \(b=8\) and \(\tau=2/5\), choosing \(\eta=3/8,4/8,5/8\) yields stationary means \(1/3,1/4,2/5\), respectively. Thus increasing \(\eta\) can make the stationary error larger before it improves.

**4. An explicit stagnation example and the infinite-bit comparison.** With \(b=4\), \(\tau=2/5\), \(\eta=1/64\), exactly the \(16\) states \(-15,-14,\ldots,0\) are absorbing, although none solves \(f'(x)=0\). Starting from \(X_0=1\), the probability of remaining at \(1\) after \(n\) steps is \((3/4)^n\), and \(X_n\to0\) almost surely. More generally for each fixed finite \(b\), reducing \(\eta\) sufficiently forces \(u=0\) and \(X_n\to0\) from \(X_0=1\); hence the long-run stationary mean tends to zero in that order of limits. Under *ideal* stochastic rounding the transition probabilities are \(u=\eta\tau\) and \(d=\eta(1-\tau)\), so the stationary mean is always \(\tau\). As \(b\to\infty\) at any fixed \(\eta\in(0,1)\), the finite-bit probabilities converge to those ideal probabilities and \(\pi\to\tau\).

## Verification
Run `python3 checker.py` with the standard Python library (exact `fractions.Fraction` arithmetic). The checker verifies \(6,089\) rational parameter settings covering multiple bit counts, stepsizes and targets, one-step transition probabilities, stationarity and bias, the full absorbing-state classification on finite test ranges, finite-time laws, integer \(b\eta\) resonance, and the explicit \(16\)-trap example. `check_output.txt` records the actual output. These finite checks support implementation accuracy; the infinite-time and all-parameter assertions are derived in the proof.

## Relationship to prior work
El Arar, Fasi, Filip and Mikaitis introduced the relevant limited-precision stochastic-rounding kernel and its one-operation downward bias (arXiv:2408.03069, Definition 4, Sections 3–6). Their article treats error bounds for arithmetic operations, summation and inner products, and illustrates gradient descent numerically, rather than giving this exact recurrence classification. Xia, Massei and Hochstenbach (arXiv:2301.09511) study gradient descent with stochastic fixed-point errors and the ideal unbiased and intentionally biased rounding mechanisms; their general convergence setting does not yield the precise finite-random-bit absorbing-state count or stationary staircase here. Fitzgibbon and Felix (arXiv:2504.20634) discuss stochastic rounding with few random bits and biases of its hardware-oriented kernels; the exact long-run scalar GD law is a different question. The method's one-step downward bias is **not** claimed as new.

## Limitations
The model rounds **only** the final affine update on a uniform infinite grid. It does not claim to represent separate rounding of gradients, intermediate products, dynamic exponent changes, underflow, overflow or arbitrary floating-point hardware. The stationary distribution is unconditional for starts in \(\{0,1\}\); outside it, extra absorbing states may coexist, as explicitly characterized. The analytic result is elementary finite-state mathematics and does not establish a general high-dimensional SGD convergence theorem. Older quantized-Markov or rounding literature could contain equivalent descriptions despite the explicit source comparisons.

## References
1. El-Mehdi El Arar, Massimiliano Fasi, Silviu-Ioan Filip, Mantas Mikaitis, *Probabilistic error analysis of limited-precision stochastic rounding*, arXiv:2408.03069 (first publicly submitted 2024-08-06), https://arxiv.org/abs/2408.03069.
2. Lu Xia, Stefano Massei, Michiel E. Hochstenbach, *On the Convergence of the Gradient Descent Method with Stochastic Fixed-Point Rounding Errors under the Polyak–Łojasiewicz Inequality*, arXiv:2301.09511, https://arxiv.org/abs/2301.09511.
3. Andrew Fitzgibbon, Stephen Felix, *On Stochastic Rounding with Few Random Bits*, arXiv:2504.20634, https://arxiv.org/abs/2504.20634.
