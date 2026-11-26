# Exact bit-step phase diagram for finite-bit stochastic-rounding descent

## Finding

Truncating finite-bit stochastic rounding of scalar quadratic descent on the integer grid has a sharp transition between a deterministic, initial-state-dependent trapping regime and a unique limiting law on the two grid points adjacent to the minimum. The entire lattice, including starts arbitrarily far from the minimum, can be classified.

Let \(c=b\eta\), and let \(N=\max\{0,\lceil 1/c-\tau\rceil\}\). If \(N>0\), the absorbing integers are precisely \([a,0]\cap\mathbb Z\) where \(a=1-N\). From any integer initial state \(j\), the chain almost surely eventually sticks at
\[
L(j)=\max\{a,\min\{0,j\}\}.
\]
In particular the absorption location is deterministic even when a proposal can cross more than one grid spacing. The stationary distributions are exactly all probability measures supported on \([a,0]\cap\mathbb Z\). If \(N=0\), equivalently \(b\eta\tau\ge1\), the chain almost surely enters \(\{0,1\}\) from every integer start. Its law converges to the unique stationary distribution, whose upper mass is the two-state formula given below. The result does not concern multiple arithmetic roundings or changing grid spacing.

## Model

Take integer \(r\ge1\), \(b=2^r\), \(0<\eta<1\), and \(0<\tau<1\). The loss is \(f(x)=(x-\tau)^2/2\). For integer \(j\), evaluate the affine proposal \(T(j)=(1-\eta)j+\eta\tau\) exactly. With a new independent uniform draw \(U\in\{0,\ldots,b-1\}\) at each step, round a proposal \(y\) to
\[
Q_b(y)=\lfloor y\rfloor+\mathbf 1\{U<\lfloor b(y-\lfloor y\rfloor)\rfloor\}.
\]
Thus \(X_{n+1}=Q_b(T(X_n))\), with no other rounding.

## Proof

For \(j\le0\), one has \(j<T(j)<1\), so \(j\le Q_b(T(j))\le1\). A positive increase has probability zero exactly when \(T(j)<j+1/b\); equality gives increase probability \(1/b\). For \(j\ge1\), one has \(0<T(j)<j\), so \(0\le Q_b(T(j))\le j\), with strictly positive chance of a decrease. Consequently the absorbing set is \(\{j\le0:j>\tau-1/c\}\), giving \(N\) and the stated threshold, including its equality case. No such integer solves \(f'(j)=0\).

If \(N>0\) and \(j<a\), the strict increase of \(T\) and the absorption criterion at \(a\) give \(T(j)<T(a)<a+1/b\). Any such proposal rounds to at most \(a\): a proposal above or equal to \(a\) but below \(a+1/b\) rounds deterministically to \(a\), and a proposal below \(a\) cannot round above \(a\). Thus the chain from below \(a\) is nondecreasing, stays in the finite interval between its start and \(a\), and has a strictly positive probability of leaving each occupied state below \(a\) at each trial. The holding time at any such state has an almost surely finite geometric tail. Monotonicity and finiteness therefore give eventual absorption at \(a\). From \(j>0\), the chain is nonincreasing until it reaches \(0\); the same finite-state argument gives eventual absorption there. A start in \([a,0]\) stays put. This proves the clipping law.

If \(N=0\), the same monotonicity and holding-time argument gives almost-sure entry into \(\{0,1\}\). Indeed the chain cannot jump above \(1\) from a state below the pair or below \(0\) from a state above it. The pair is invariant since \(T(0),T(1)\in(0,1)\). Its up and down probabilities are
\[
u=\frac{\lfloor c\tau\rfloor}{b},\qquad d=\frac{\lceil c(1-\tau)\rceil}{b},
\]
where the ceiling comes from subtracting the upper-rounding probability at \(T(1)=1-\eta(1-\tau)\) from one. Hence the stationary upper mass is
\[
\pi_1=\frac{u}{u+d}=\frac{\lfloor c\tau\rfloor}{\lfloor c\tau\rfloor+\lceil c(1-\tau)\rceil}.
\]
The deviation of the upper mass from \(\pi_1\) is multiplied by \(1-u-d\) each step, with \(|1-u-d|<1\) since \(d>0\), \(u<1\), and \(d\le1\). Thus convergence also holds after almost-sure entry: for a fixed cutoff time, the contribution from entries after the cutoff is bounded by their probability, while from earlier entries the pair converges geometrically. The formula holds on the pair even when \(N>0\), when \(u=0\) and \(\pi_1=0\). For any stationary law, integrate the point-start limits against that law by bounded convergence on each singleton. This shows that the stationary laws are exactly those stated in both regimes.

## Examples and comparison with ideal rounding

For \(b=4,\ \eta=1/64,\ \tau=2/5\), there are 16 traps, from \(-15\) to 0. Starting below this interval leads almost surely to \(-15\); starting above it leads almost surely to 0, and starting inside leaves the state unchanged. From 1 the probability of still being at 1 after \(n\) steps is \((3/4)^n\).

The two-state mean satisfies \(\pi_1\le\tau\), since \(u\le\eta\tau\) and \(d\ge\eta(1-\tau)\). In ideal unbiased rounding these inequalities are equalities and the stationary mean is \(\tau\). For integer \(c=m\), the denominator of \(\pi_1\) is \(m\) and the fixed-target mean is the staircase \(\lfloor m\tau\rfloor/m\). For \(b=8\) and \(\tau=2/5\), \(m=3,4,5\) give masses \(1/3,1/4,2/5\), respectively. These compare the adjacent pair, not arbitrary lattice initial states in the trapping regime.

## Relationship to prior work

El Arar, Fasi, Filip and Mikaitis, *Probabilistic error analysis of limited-precision stochastic rounding* ([arXiv:2408.03069](https://arxiv.org/abs/2408.03069), Definition 4 and equations (6)–(7)), analyze the underlying limited-precision kernel and its downward one-step bias. Xia, Massei and Hochstenbach ([arXiv:2301.09511](https://arxiv.org/abs/2301.09511)) analyze stochastic fixed-point gradient descent under PL assumptions with rounding errors in computational operations; Fitzgibbon and Felix ([arXiv:2504.20634](https://arxiv.org/abs/2504.20634)) study few-random-bit implementation bias. These comparisons do not establish priority for the global classification.

The exact adjacent-pair stationary mass is also given in [*A sharp random-bit threshold for invariant bias in two-level quadratic descent*](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-sharp-random-bit-threshold-for-invariant-bias-in-two-level-qua--51e52c9814bf); its threshold count \(K\) is \(b\) here. The formula and its integer-resonance specialization are used as two-state context, not as separate originality claims. A two-state model does not include the lattice trapping paths or determine which absorbing integer an arbitrary initial state reaches. The new classification in this statement rests on the trap boundary and the no-overshoot property of the truncated kernel.

## Reproducibility and limitations

The proof establishes all lattice, parameter and limiting statements. The companion exact-rational checker (`python3 checker.py`) and recorded output (`check_output.txt`) test the two-state transition formulas, absorbing-state counts on test ranges and examples; they do not test the full clipping theorem. The model has an infinite unit grid, independent thresholds, and exactly computed proposals. These conclusions do not classify hardware rounding with intermediate arithmetic, exponent changes or bounded grids, nor do they imply high-dimensional convergence.
