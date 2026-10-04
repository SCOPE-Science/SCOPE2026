# Cover-transversal obstruction to per-coordinate adaptivity in SM3
## Finding

SM3 compresses coordinatewise second-moment history by assigning one accumulator to each set in a cover of the parameter coordinates. The resulting compression has an exact combinatorial vulnerability.

Let
\[
\mathcal S=\{S_r\}_{r=1}^k
\]
be a cover of
\[
[d].
\]
Fix a target coordinate \(i\). Define the off-target cover-transversal number
\[
\tau_i
=
\min\left\{
|H|:
H\subseteq[d]\setminus\{i\},
\quad
H\cap S_r\neq\varnothing
\text{ for every }r\text{ with }i\in S_r
\right\},
\]
with
\[
\tau_i=\infty
\]
if no such set exists.

For both additive SM3-I and SM3-II, \(\tau_i\) is the exact minimum number of off-target coordinates whose simultaneous activation can contaminate every cover accumulator available to coordinate \(i\) in one gradient round.

More precisely, suppose
\[
\tau_i<\infty.
\]
Choose a minimum transversal \(H\). On one round set
\[
g(j)=
\begin{cases}
M,&j\in H,\\
0,&j\notin H,
\end{cases}
\qquad
M>0.
\]
In particular,
\[
g(i)=0.
\]
On the next round use the target-only gradient
\[
\widetilde g(i)=\delta\neq0,
\qquad
\widetilde g(j)=0
\quad
(j\neq i).
\]
Then both SM3-I and SM3-II assign the target coordinate the exact second-moment statistic
\[
M^2+\delta^2
\]
on that second round. Hence the magnitude of the target update is
\[
\eta
\frac{|\delta|}
{\sqrt{M^2+\delta^2}}.
\]

For singleton-cover AdaGrad, the same target coordinate has seen no previous nonzero gradient, so its accumulated square is
\[
\delta^2
\]
and its update magnitude is
\[
\eta.
\]
Therefore the exact SM3-to-AdaGrad update ratio is
\[
A(M,\delta)
=
\frac{|\delta|}
{\sqrt{M^2+\delta^2}}.
\]
For every requested attenuation level
\[
0<q<1,
\]
choosing
\[
\frac{M}{|\delta|}
>
\sqrt{q^{-2}-1}
\]
gives
\[
A(M,\delta)<q.
\]
Thus the first nonzero update of a coordinate can be suppressed by an arbitrarily large factor even though every earlier gradient at that coordinate was exactly zero.

The support size \(\tau_i\) is sharp. If an off-target support \(H\) misses some cover set \(S_r\) containing \(i\), then the accumulator for that set remains zero after that round. Since SM3 takes the minimum over accumulators covering \(i\), that untouched set prevents one-round off-target poisoning of the target statistic. Hence no support with cardinality less than \(\tau_i\) can produce the construction.

A singleton cover set
\[
\{i\}
\]
makes
\[
\tau_i=\infty.
\]
Its accumulator can only be changed by gradients at \(i\), so that coordinate is fully protected from off-target second-moment contamination.

For the standard matrix row-column cover, take a target entry \((a,b)\) in a matrix with at least two rows and two columns. No single off-target entry lies in both the target row and target column, so
\[
\tau_{(a,b)}\ge2.
\]
Choose
\[
(a,b')
\quad\text{and}\quad
(a',b),
\]
with
\[
a'\neq a,
\qquad
b'\neq b.
\]
These two entries hit the target row and target column respectively, so
\[
\tau_{(a,b)}=2.
\]

The same value holds for the codimension-one slice cover of a tensor whenever at least two axes have length greater than one. For a target multi-index, choose one off-target index differing only in the first nontrivial axis and another differing only in the second. Each misses only one of the target's slice sets, and together they hit every target slice. A single off-target index cannot lie in every target slice, because membership in every one of those slices forces equality with the target index. Therefore
\[
\tau_i=2
\]
independently of tensor rank.

## Assumptions and scope

The theorem concerns the additive accumulators in the original SM3-I and SM3-II algorithms. It does not include optional momentum or later exponential-moving-average adaptations.

The result is a statement about exact optimizer statistics for admissible gradient sequences. Such sequences are compatible with the online convex setting of the defining paper: any prescribed gradient vector can be realized as the gradient of a linear convex loss on that round.

The comparison with AdaGrad is coordinatewise and uses the same learning rate \(\eta\) with the source convention \(0/0=0\). No numerical stabilizer is added to the denominator.

The theorem does not say that the adversarial activation pattern is typical in neural-network training. Its purpose is to quantify the exact structural cost of a cover that is incompatible with the realized activation pattern.

## Proof

For SM3-I,
\[
\mu_t(r)
=
\mu_{t-1}(r)
+
\max_{j\in S_r}g_t(j)^2,
\]
and
\[
\nu_t(i)
=
\min_{r:S_r\ni i}\mu_t(r).
\]
Initially all cover accumulators vanish.

On the poisoning round, every set \(S_r\) containing \(i\) meets \(H\). Therefore
\[
\max_{j\in S_r}g(j)^2=M^2
\]
for every such \(r\), so
\[
\mu_1(r)=M^2.
\]
On the target-only round,
\[
\max_{j\in S_r}\widetilde g(j)^2=\delta^2
\]
for every set containing \(i\), hence
\[
\mu_2(r)=M^2+\delta^2.
\]
Taking the minimum gives
\[
\nu_2(i)=M^2+\delta^2.
\]

For SM3-II,
\[
\nu'_t(j)
=
\min_{r:S_r\ni j}\mu'_{t-1}(r)
+
g_t(j)^2,
\]
and each cover accumulator is then replaced by the maximum of \(\nu'_t(j)\) over its members. Since every initial accumulator is zero, the poisoning round gives
\[
\nu'_1(j)=M^2
\]
on \(H\) and zero off \(H\). Every target-cover set meets \(H\), so each corresponding post-round accumulator is exactly \(M^2\). The target-only round therefore gives
\[
\nu'_2(i)=M^2+\delta^2.
\]

The update formulas immediately give the attenuation ratio.

For sharpness, suppose an off-target support \(H\) fails to intersect some set \(S_r\) containing \(i\). In SM3-I its accumulator receives zero increment. In SM3-II every member of \(S_r\) has zero gradient and therefore zero first-round local statistic, so its cover accumulator also remains zero. Thus a support poisons every available target accumulator in one round if and only if it is a transversal of the family
\[
\{S_r\setminus\{i\}:i\in S_r\}.
\]
The minimum support cardinality is exactly \(\tau_i\).

The matrix and tensor statements follow from the explicit two-element transversals described above and the observation that a single off-target coordinate cannot belong to every target slice.

## Verification

The accompanying `verify.py` implements SM3-I and SM3-II directly from their definitions. It checks the exact two-round statistic and update attenuation on matrix row-column covers, exhaustively confirms that no one-element off-target support poisons a matrix target, and verifies the rank-independent two-element transversal construction on tensor slice covers of several dimensions.

The finite checks verify the concrete constructions and implementation of the formulas. The arbitrary-cover theorem and minimality statement are proved symbolically by the cover-transversal argument above.

## Relationship to prior work

Anil, Gupta, Koren, and Singer introduced SM3 as a memory-efficient adaptive optimizer based on arbitrary parameter covers. Their paper proves that the SM3 statistic for each coordinate upper-bounds its own cumulative squared gradient and explicitly notes that, in the worst case, the convergence bound can be worse than AdaGrad. It then argues informally that SM3 should closely match AdaGrad when a cover is compatible with observed activation patterns.

The same paper recommends row-column covers for matrices and codimension-one slice covers for higher-order tensors. The result here turns the qualitative notion of cover compatibility into an exact local combinatorial invariant: the minimum off-target activation support that can contaminate every statistic available to one coordinate.

The inspected defining paper does not formulate this transversal number, does not state its value \(2\) for the standard matrix and tensor covers, and does not give the exact attenuation factor
\[
\frac{|\delta|}{\sqrt{M^2+\delta^2}}.
\]

The reference implementation contains a related practical warning for sparse gradients: it avoids a column accumulator because that accumulator can substantially overestimate gradient squares. That observation supports the relevance of cross-coordinate contamination, but it does not give the exact cover-transversal characterization or the two-spike sharpness result.

## Limitations

The theorem is adversarial and local in gradient history. It does not quantify how frequently incompatible activation patterns occur in a particular trained network.

The attenuation comparison is for the original additive versions of SM3 and AdaGrad. Momentum, exponential averaging, epsilon regularization, clipping, and learning-rate schedules alter the numerical ratio.

The transversal number measures the minimum simultaneous support needed to contaminate every target-cover statistic from a zero state. Longer histories can create other contamination patterns, and statistical correlations can make the practical effect much smaller.

A cover containing a singleton for every coordinate removes this obstruction but also restores linear second-moment memory, so the protection is not free.

## References

1. Rohan Anil, Vineet Gupta, Tomer Koren, and Yoram Singer, “Memory-Efficient Adaptive Optimization,” arXiv:1901.11150v1, 2019.
2. Google Research, reference SM3 implementation, `google-research/sm3/sm3.py`.
