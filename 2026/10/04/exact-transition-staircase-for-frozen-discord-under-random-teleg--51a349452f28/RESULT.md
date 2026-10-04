# Exact transition staircase for frozen discord under random-telegraph dephasing

## Finding

Consider the Bell-diagonal family
\[
\rho_{AB}
=
\frac14\left(
I\otimes I+
\sum_{j=1}^3 c_j\,\sigma_j\otimes\sigma_j
\right)
\]
under the local random-telegraph phase-flip channel studied by Mazzola, Piilo, and Maniscalco. The source gives
\[
c_1(\nu)=c_1(0)\Lambda(\nu)^2,\qquad
c_2(\nu)=c_2(0)\Lambda(\nu)^2,\qquad
c_3(\nu)=c_3(0),
\]
with dimensionless time
\[
\nu=\frac{t}{2\tau}.
\]

Set
\[
M=\max\{|c_1(0)|,|c_2(0)|\}
\]
and assume the source's third dynamical regime
\[
0<|c_3|<M.
\]
The classical-correlation optimizer is controlled by
\[
\chi(\nu)
=
\max\left\{
M\Lambda(\nu)^2,\ |c_3|
\right\}.
\]
A genuine sudden transition occurs exactly when the two entries of this maximum cross and exchange order.

In the oscillatory colored-noise regime
\[
4a\tau>1,
\]
define
\[
\mu=\sqrt{(4a\tau)^2-1}
\]
and
\[
A=
\frac{\mu}{2\pi}
\log\!\frac{M}{|c_3|}.
\]
Then the exact total number of genuine sudden transitions over the whole time axis is
\[
\boxed{
N_{\mathrm{st}}
=
2\lceil A\rceil-1.
}
\]

Equivalently, the exact staircase boundaries in the memory parameter are
\[
\boxed{
N_{\mathrm{st}}\ge 2n+1
\quad\Longleftrightarrow\quad
4a\tau>
\sqrt{
1+
\left(
\frac{2n\pi}{\log(M/|c_3|)}
\right)^2
}
}
\]
for every integer
\[
n\ge1.
\]

At equality the relevant revival lobe only touches the threshold. Since the ordering of
\[
M\Lambda(\nu)^2
\]
and
\[
|c_3|
\]
does not change, the tangency is not a sudden transition.

For fixed initial-state ratio
\[
M/|c_3|,
\]
the number of transitions grows linearly with the memory parameter:
\[
N_{\mathrm{st}}
=
\frac{\mu}{\pi}
\log\!\frac{M}{|c_3|}
+
O(1),
\]
and hence
\[
N_{\mathrm{st}}
\sim
\frac{4a\tau}{\pi}
\log\!\frac{M}{|c_3|}
\qquad
(a\tau\to\infty).
\]

For the parameters plotted in the source,
\[
a=1\,\mathrm{s}^{-1},
\qquad
\tau=5\,\mathrm{s},
\qquad
\mu=\sqrt{399},
\]
the frozen-discord example
\[
(c_1,c_2,c_3)=(1,-0.6,0.6)
\]
has
\[
A\approx1.6239746791
\]
and therefore exactly
\[
N_{\mathrm{st}}=3
\]
transitions.

The source's sudden-change example
\[
(c_1,c_2,c_3)=(0.35,-0.3,0.1)
\]
has
\[
A\approx3.9826806744
\]
and therefore exactly
\[
N_{\mathrm{st}}=7
\]
transitions over the full time axis. The finite plotting window displays only the early part of this staircase.

## Assumptions and scope

The initial triple
\[
(c_1(0),c_2(0),c_3)
\]
is assumed to define a valid Bell-diagonal density matrix and to satisfy
\[
0<|c_3|<M.
\]
This excludes the source's first regime, where the constant coefficient dominates from the start, and its special
\[
c_3=0
\]
regime.

The count is for the random-telegraph channel with one nonzero noise direction and the damping function used in the source. It counts changes in the identity of the maximizing coefficient in
\[
\chi(\nu),
\]
which are the source's sudden-transition points for classical correlation and quantum discord.

The formula above is stated for
\[
4a\tau>1,
\]
where the telegraph damping is oscillatory. In the nonoscillatory regime the same threshold is crossed at most once, so the multiple-transition staircase does not arise.

For the frozen-discord subclass identified in the source,
\[
c_{1(2)}(0)=k,\qquad
c_{2(1)}(0)=-c_3k,\qquad
|k|>|c_3|,
\]
the same count is exactly the number of alternations between the frozen-discord and decaying-discord dynamical phases.

## Proof

The completely positive random-telegraph dephasing channel has damping function
\[
\Lambda(\nu)
=
e^{-\nu}
\left[
\cos(\mu\nu)
+
\frac{\sin(\mu\nu)}{\mu}
\right],
\qquad
\mu=\sqrt{(4a\tau)^2-1}.
\]
The source dynamics gives
\[
|c_1(\nu)|=|c_1(0)|\,|\Lambda(\nu)|^2,
\qquad
|c_2(\nu)|=|c_2(0)|\,|\Lambda(\nu)|^2,
\]
so
\[
\max\{|c_1(\nu)|,|c_2(\nu)|\}
=
M|\Lambda(\nu)|^2.
\]
A sudden transition therefore occurs precisely at a sign-changing zero of
\[
F(\nu)=M|\Lambda(\nu)|^2-|c_3|.
\]
Define
\[
\rho=\sqrt{\frac{|c_3|}{M}}\in(0,1).
\]
The transition equation becomes
\[
|\Lambda(\nu)|=\rho.
\]

Differentiate:
\[
\Lambda'(\nu)
=
-\left(\mu+\frac1\mu\right)
e^{-\nu}\sin(\mu\nu).
\]
Thus all noninitial stationary points are
\[
\nu_n=\frac{n\pi}{\mu},
\qquad
n=1,2,\ldots.
\]
At them,
\[
\Lambda(\nu_n)
=
(-1)^n e^{-n\pi/\mu},
\]
hence
\[
|\Lambda(\nu_n)|=e^{-n\pi/\mu}.
\]

The zeros of the damping function satisfy
\[
\tan(\mu\nu)=-\mu.
\]
There is exactly one such zero between each consecutive pair of stationary points. Consequently the initial lobe decreases from
\[
|\Lambda(0)|=1
\]
to zero and contributes exactly one threshold crossing because
\[
0<\rho<1.
\]

Every later lobe starts at zero, rises to the unique maximum
\[
e^{-n\pi/\mu},
\]
and returns to zero. It therefore contributes exactly two genuine threshold crossings if
\[
e^{-n\pi/\mu}>\rho,
\]
no crossings if the inequality is reversed, and only a tangency if equality holds.

The number of later lobes producing crossings is
\[
L
=
\#\left\{
n\in\mathbb N:
e^{-n\pi/\mu}>\rho
\right\}.
\]
Taking logarithms,
\[
n
<
\frac{\mu}{\pi}\log\!\frac1\rho
=
\frac{\mu}{2\pi}\log\!\frac{M}{|c_3|}
=
A.
\]
The number of positive integers strictly below
\[
A>0
\]
is
\[
L=\lceil A\rceil-1.
\]
Adding the one initial crossing gives
\[
N_{\mathrm{st}}
=
1+2L
=
2\lceil A\rceil-1.
\]

For an integer
\[
n\ge1,
\]
the condition for the \(n\)-th revival lobe to generate two additional transitions is
\[
A>n.
\]
Using
\[
\mu=\sqrt{(4a\tau)^2-1}
\]
gives the stated sharp staircase boundary.

Finally,
\[
2\lceil A\rceil-1=2A+O(1),
\]
which yields
\[
N_{\mathrm{st}}
=
\frac{\mu}{\pi}\log\!\frac{M}{|c_3|}
+
O(1).
\]
Since
\[
\mu\sim4a\tau
\]
for fixed initial state and
\[
a\tau\to\infty,
\]
the large-memory asymptotic follows.

## Verification

`verify_telegraph_transition_count.py` evaluates the exact damping function, checks its derivative identity, reconstructs the stationary-point envelope, and independently counts sign-changing threshold roots by bisection on every lobe.

The checker tests deterministic grids of
\[
\mu
\]
and
\[
\rho
\]
against the closed count
\[
2\left\lceil
\frac{\mu}{\pi}\log\!\frac1\rho
\right\rceil-1.
\]
It separately tests exact tangency cases, where the lobe touches the threshold but must not be counted as a transition.

The source parameter examples are also replayed. Their full-time counts are
\[
3
\]
and
\[
7,
\]
respectively.

The finite numerical replay is supplementary. The all-time count and staircase boundaries are proved analytically above.

## Relationship to prior work

Daffer, Wódkiewicz, Cresser, and McIver derive the random-telegraph memory channel and the damped-oscillatory function
\[
\Lambda(\nu)
=
e^{-\nu}
\left[
\cos(\mu\nu)+\frac{\sin(\mu\nu)}{\mu}
\right].
\]
Their work establishes the channel dynamics and complete-positivity conditions, but predates the frozen-discord problem.

Mazzola, Piilo, and Maniscalco apply this channel to Bell-diagonal two-qubit correlations. They prove that the dynamical coefficients are multiplied by
\[
\Lambda(\nu)^2
\]
and identify sudden changes when the decaying maximum
\[
\max\{|c_1(\nu)|,|c_2(\nu)|\}
\]
crosses the constant
\[
|c_3|.
\]
They explicitly report multiple sudden transitions and illustrate them numerically, but the inspected full text does not count all transitions or give memory-parameter boundaries for a prescribed number of transitions.

A later review reproduces the same multiple-transition mechanism and the same examples, still describing the repeated changes qualitatively rather than as a closed counting law.

A 2025 paper revisits sudden transitions under random-telegraph and colored noise and shows transition times graphically as environmental parameters vary. Only the publisher preview and figure captions were accessible in this review; they do not expose an exact all-time transition-count formula. This incomplete access is retained as a residual literature risk.

Targeted searches for a transition count, a ceiling/floor formula, the exact revival envelope
\[
e^{-n\pi/\mu},
\]
and a staircase in
\[
a\tau
\]
did not locate an equivalent statement.

## Limitations

The count is tied to the Bell-diagonal phase-flip dynamics in which both nonconstant coefficients share the same factor
\[
\Lambda(\nu)^2.
\]
More general initial states or unequal local channels can produce a different crossing geometry.

Tangencies are excluded from the transition count because they do not exchange the dominant branch of
\[
\chi(\nu).
\]
If one instead chooses to count threshold contacts irrespective of phase exchange, the integer-boundary convention changes.

The formula counts transitions over the entire half-line
\[
\nu\ge0.
\]
A finite experimental or numerical observation window can contain fewer transitions.

The 2025 closely related paper was not available in complete full text through the inspected sources, so an equivalent formula hidden in its inaccessible remainder remains a specific residual originality risk.

## References

1. L. Mazzola, J. Piilo, and S. Maniscalco, “Frozen discord in non-Markovian dephasing channels,” arXiv:1006.1805, first public 9 June 2010; *International Journal of Quantum Information* 9 (2011), 981–991, DOI: 10.1142/S021974991100754X.
2. S. Daffer, K. Wódkiewicz, J. D. Cresser, and J. K. McIver, “Completely positive maps with memory,” arXiv:quant-ph/0309081, first public 9 September 2003; *Physical Review A* 70 (2004), 010304, DOI: 10.1103/PhysRevA.70.010304.
3. G. Karpat, C. Addis, and S. Maniscalco, “Frozen and Invariant Quantum Discord Under Local Dephasing Noise,” in *Lectures on General Quantum Correlations and their Applications* (2017), DOI: 10.1007/978-3-319-53412-1_16.
4. L. H. Wu, A. C. Yang, and W. W. Cheng, “Sudden Transition and Freezing of Quantum Discord in Colored-noise Environments,” *International Journal of Theoretical Physics* 64 (2025), 176, DOI: 10.1007/s10773-025-06047-w.
