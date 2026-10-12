# COCOB has an exact balanced-alternation reset law
## Finding

COCOB turns each coordinate of stochastic optimization into a continuous coin-betting process. Its defining paper emphasizes that long runs of equal gradient signs grow the bet rapidly. At the opposite extreme, a perfectly balanced alternating signal has an exact and sharply different law: every second iterate resets to the initialization, the intervening excursion decays as a power law, and the returned average telescopes exactly.

Consider one coordinate of the theoretical COCOB algorithm. Let
\[
L>0
\]
be the known coordinatewise gradient bound and initialize
\[
G_0=L,
\qquad
\operatorname{Reward}_0=0,
\qquad
\theta_0=0.
\]
Use the source notation in which \(g_t\) is a negative stochastic subgradient, and feed
\[
g_{2n-1}=L,
\qquad
g_{2n}=-L.
\]

COCOB updates
\[
G_t=G_{t-1}+|g_t|,
\]
\[
\operatorname{Reward}_t
=
\operatorname{Reward}_{t-1}
+
(w_t-w_1)g_t,
\]
\[
\theta_t=\theta_{t-1}+g_t,
\]
and
\[
\beta_t
=
\frac1L
\tanh\!\left(
\frac{\theta_t}{G_t+L}
\right),
\]
because
\[
2\sigma(2x)-1=\tanh x.
\]
The next iterate is
\[
w_{t+1}
=
w_1
+
\beta_t
\bigl(
L+\operatorname{Reward}_t
\bigr).
\]

Define
\[
a_n
=
\tanh\!\left(
\frac1{2n+1}
\right),
\qquad
P_0=1,
\]
and
\[
P_n
=
\prod_{k=1}^{n}(1-a_k).
\]

Then for every
\[
n\ge1
\]
the wealth and iterates are exactly
\[
\boxed{
\operatorname{Wealth}_{2n-1}
=
LP_{n-1}
},
\]
\[
\boxed{
\operatorname{Wealth}_{2n}
=
LP_n
},
\]
\[
\boxed{
w_{2n+1}=w_1
},
\]
and
\[
\boxed{
w_{2n}-w_1
=
a_nP_{n-1}
=
P_{n-1}-P_n
}.
\]

Thus every odd iterate is exactly the initialization. The only nonzero excursions occur at the even iterates.

The last identity telescopes. If
\[
\bar w_T
=
\frac1T
\sum_{t=1}^{T}w_t
\]
is the convex-average output used by the source theorem and
\[
N=\left\lfloor\frac T2\right\rfloor,
\]
then
\[
\boxed{
\bar w_T-w_1
=
\frac{1-P_N}{T}
}.
\]
In particular,
\[
\bar w_T-w_1
\sim
\frac1T.
\]

The reset law has a sharp excursion asymptotic. Since
\[
1-\tanh x
=
\frac{e^{-x}}{\cosh x},
\]
we have
\[
P_n
=
\frac{
\exp\!\left(
-\sum_{k=1}^{n}\frac1{2k+1}
\right)
}{
\prod_{k=1}^{n}
\cosh\!\left(
\frac1{2k+1}
\right)
}.
\]
Also
\[
\sum_{k=1}^{n}\frac1{2k+1}
=
H_{2n+1}
-
1
-
\frac12H_n,
\]
so
\[
\sum_{k=1}^{n}\frac1{2k+1}
=
\frac12\log n
+
\log2
+
\frac{\gamma_{\mathrm E}}2
-
1
+
o(1).
\]
Because
\[
\sum_{k=1}^{\infty}
\log\cosh\!\left(
\frac1{2k+1}
\right)
\]
converges, it follows that
\[
P_n
\sim
Cn^{-1/2},
\]
where
\[
\boxed{
C
=
\frac{
e^{1-\gamma_{\mathrm E}/2}
}{
2
\prod_{k=1}^{\infty}
\cosh\!\left(
\frac1{2k+1}
\right)
}
=
0.9071810223\ldots
}.
\]

Therefore
\[
\boxed{
w_{2n}-w_1
\sim
\frac C2 n^{-3/2}
=
0.4535905112\ldots\,n^{-3/2}
}.
\]

All of these formulas are independent of the gradient scale \(L\). The source's scale-free property is therefore exact on this canonical zero-drift high-frequency input.

## Assumptions and scope

The theorem concerns Algorithm 1, the theoretical COCOB method with a known coordinatewise gradient bound \(L\).

The input sequence is expressed in the source convention, where \(g_t\) is a negative stochastic subgradient.

The sequence is externally prescribed. It is an input-response theorem for the optimizer state and does not assert that a fixed objective produces this alternating signal.

The theorem does not concern COCOB-Backprop, which changes the gradient-bound state, clips rewards at zero, and replaces the sigmoid betting rule.

The exact average law refers to the source's convex-case output
\[
\bar w_T
=
T^{-1}\sum_{t=1}^{T}w_t.
\]

## Proof

At an odd round
\[
t=2n-1,
\]
the cumulative signed gradient is
\[
\theta_{2n-1}=L,
\]
while
\[
G_{2n-1}+L=(2n+1)L.
\]
Hence
\[
\beta_{2n-1}
=
\frac1L
\tanh\!\left(
\frac1{2n+1}
\right)
=
\frac{a_n}{L}.
\]

At an even round,
\[
\theta_{2n}=0,
\]
so
\[
\beta_{2n}=0.
\]
Consequently every even-round update sets the next iterate exactly to
\[
w_{2n+1}=w_1.
\]

Let
\[
W_{n-1}
=
L+\operatorname{Reward}_{2n-2}
\]
be the wealth entering odd round \(2n-1\). Since
\[
w_{2n-1}=w_1,
\]
the odd-round reward increment is zero. Therefore
\[
w_{2n}-w_1
=
\frac{a_n}{L}W_{n-1}.
\]

The next outcome is
\[
g_{2n}=-L.
\]
Its reward increment is
\[
(w_{2n}-w_1)(-L)
=
-a_nW_{n-1}.
\]
Thus the wealth after the pair is
\[
W_n
=
W_{n-1}(1-a_n).
\]
Starting from
\[
W_0=L
\]
gives
\[
W_n=LP_n.
\]
This proves both wealth identities and
\[
w_{2n}-w_1=a_nP_{n-1}.
\]

Since
\[
P_n=P_{n-1}(1-a_n),
\]
we also have
\[
a_nP_{n-1}
=
P_{n-1}-P_n.
\]
Summing the even-iterate excursions therefore gives
\[
\sum_{n=1}^{N}(w_{2n}-w_1)
=
1-P_N.
\]
All odd iterates equal \(w_1\), which proves the exact average formula.

For the asymptotic law, use
\[
1-\tanh x=e^{-x}/\cosh x.
\]
The harmonic-number identity above gives the complete logarithmic divergence, while
\[
\log\cosh x=O(x^2)
\]
near zero makes the infinite product of coshes converge. The stated constant \(C\) follows.

Finally,
\[
a_n
=
\frac1{2n}
+
O(n^{-2}),
\]
and
\[
P_{n-1}
\sim
Cn^{-1/2},
\]
so
\[
a_nP_{n-1}
\sim
\frac C2n^{-3/2}.
\]

## Verification

The accompanying `verify.py` independently replays Algorithm 1 on balanced alternating outcomes.

It checks the exact cumulative states, wealth product, every-other-step reset, telescoping average, the \(n^{-1/2}\) wealth law, and the \(n^{-3/2}\) excursion law.

The finite calculations are transcription guards. The identities and asymptotic exponent are proved analytically above.

## Relationship to prior work

Orabona and Tommasi introduced COCOB as a learning-rate-free optimizer obtained from continuous coin betting. Their Algorithm 1 uses a data-dependent betting fraction based on cumulative signed and absolute gradients and is proved scale free.

The source explains that a run of equal outcomes increases wealth and bets rapidly. Its one-dimensional illustration focuses on that same-sign regime and contrasts it with fixed-learning-rate gradient descent.

The source theorem gives a generic data-dependent convergence bound and its appendix proves a lower bound on wealth. Those results do not state the exact response to a balanced period-two outcome sequence.

The later ODE coin-betting work of Chen, Langford, and Orabona develops a different parameter-free update to improve empirical behavior. Its abstract and method description concern a new continuous-time construction rather than the discrete COCOB recursion analyzed here.

Focused published-record searches for COCOB under alternating outcomes, periodic gradients, balanced coin sequences, and exact wealth decay did not locate an implication-equivalent result.

## Limitations

The input is an adversarial diagnostic and not tied to a single objective.

The result concerns the theoretical COCOB algorithm rather than COCOB-Backprop.

The exact constant \(C\) contains a convergent infinite product; the decimal value is numerical, while the product formula is exact.

The result describes one balanced period-two sequence and does not classify arbitrary zero-sum or stochastic sign patterns.

## References

1. Francesco Orabona and Tatiana Tommasi, “Training Deep Networks without Learning Rates Through Coin Betting,” arXiv:1705.07795, first submitted 2017-05-22; camera-ready version 2017.
2. Keyi Chen, John Langford, and Francesco Orabona, “Better Parameter-Free Stochastic Optimization with ODE Updates for Coin-Betting,” arXiv:2006.07507, 2020; AAAI 2022.
