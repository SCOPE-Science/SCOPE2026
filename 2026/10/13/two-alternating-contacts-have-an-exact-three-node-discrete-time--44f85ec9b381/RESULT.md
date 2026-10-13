# Two alternating contacts have an exact three-node discrete-time epidemic penalty
## Finding
Consider the discrete-time individual-based approximation to SIS spreading. At each step an infected node recovers with probability
\[
\mu\in(0,1),
\]
and infection transmits independently across an active contact with probability
\[
\lambda.
\]

Take a period-two temporal network in which each snapshot contains exactly one undirected edge and the two edges are distinct.

Three nodes are the minimum possible order for this kind of temporal variation. On three nodes every pair of distinct edges shares one endpoint, so, up to relabeling and reversing the two time steps, the only temporal sequence is
\[
12,\quad 23.
\]

For this unique minimal sequence, the formal mean-field epidemic threshold is
\[
\lambda_{\mathrm{temp}}(\mu)
=
\mu
\sqrt{\frac{2-\mu}{1-\mu}}.
\]

If the same two contacts are replaced by their static time average, the adjacency matrix is half the three-vertex path, whose spectral radius is
\[
\frac{\sqrt2}{2}.
\]
The aggregate threshold is therefore
\[
\lambda_{\mathrm{agg}}(\mu)
=
\mu\sqrt2.
\]

Consequently,
\[
\frac{\lambda_{\mathrm{temp}}(\mu)}
{\lambda_{\mathrm{agg}}(\mu)}
=
\sqrt{
\frac{2-\mu}{2(1-\mu)}
}
>1
\]
for every
\[
0<\mu<1.
\]

Thus even the smallest deterministic temporal contact sequence with two genuinely different single-edge snapshots has a strictly larger discrete-time mean-field epidemic threshold than its static aggregate.

At
\[
\mu=\frac14,
\]
the exact squared thresholds are
\[
\lambda_{\mathrm{temp}}^2
=
\frac7{48},
\qquad
\lambda_{\mathrm{agg}}^2
=
\frac18.
\]

## Assumptions and scope
The SIS model is the discrete-time individual-based approximation in which recovery and transmission are represented by independent per-step probabilities.

The temporal network has period two, each snapshot contains exactly one undirected unweighted edge, and the two edges are distinct.

The threshold is the linear-stability threshold of the disease-free state. This is the same spectral criterion used in the infection-propagator framework.

The formula for \(\lambda_{\mathrm{temp}}\) is algebraically valid for every
\[
0<\mu<1.
\]
Because \(\lambda\) is a probability, if the formal critical value exceeds \(1\), no admissible transmission probability reaches the mean-field threshold. For smaller recovery probabilities the critical value lies in the physical interval.

The static comparator is the time-average adjacency matrix, not the union graph with unit edge weights.

The result does not claim an exact stochastic finite-population extinction threshold; it is a statement about the deterministic individual-based mean-field approximation.

## Proof
Let
\[
a=1-\mu.
\]

For the edge \(12\), the linearized one-step matrix is
\[
M_{12}
=
\begin{pmatrix}
a&\lambda&0\\
\lambda&a&0\\
0&0&a
\end{pmatrix}.
\]

For the edge \(23\),
\[
M_{23}
=
\begin{pmatrix}
a&0&0\\
0&a&\lambda\\
0&\lambda&a
\end{pmatrix}.
\]

Over one two-step period,
\[
P=M_{23}M_{12}
=
\begin{pmatrix}
a^2&a\lambda&0\\
a\lambda&a^2&a\lambda\\
\lambda^2&a\lambda&a^2
\end{pmatrix}.
\]

The disease-free state loses linear stability when
\[
\rho(P)=1.
\]

A direct determinant calculation gives
\[
\det(P-I)
=
\left[
(a-1)^2(a+1)-a\lambda^2
\right]
\left[
(a-1)(a+1)^2-a\lambda^2
\right].
\]

For
\[
0<a<1
\]
and
\[
\lambda\ge0,
\]
the second factor is strictly negative:
\[
(a-1)(a+1)^2-a\lambda^2<0.
\]

The first factor vanishes exactly at
\[
a\lambda^2
=
(a-1)^2(a+1).
\]
Substituting
\[
a=1-\mu
\]
gives
\[
\lambda^2
=
\frac{\mu^2(2-\mu)}{1-\mu}.
\]

At \(\lambda=0\), the propagator is \(a^2I\), so its spectral radius is below one. For positive \(\lambda\), the nonnegative irreducible propagator has a Perron root that increases strictly with its positive entries. Hence the displayed zero is the unique Perron crossing, proving
\[
\lambda_{\mathrm{temp}}
=
\mu
\sqrt{\frac{2-\mu}{1-\mu}}.
\]

For the static time-average network,
\[
A_*=\frac12(A_{12}+A_{23}).
\]
The unweighted path on three vertices has spectral radius \(\sqrt2\), so
\[
\rho(A_*)=\frac{\sqrt2}{2}.
\]
The one-step static linearization is
\[
(1-\mu)I+\lambda A_*,
\]
and its leading eigenvalue reaches one at
\[
\lambda_{\mathrm{agg}}
=
\frac{\mu}{\rho(A_*)}
=
\mu\sqrt2.
\]

Finally,
\[
\frac{\lambda_{\mathrm{temp}}^2}
{\lambda_{\mathrm{agg}}^2}
=
\frac{2-\mu}{2(1-\mu)}
=
1+\frac{\mu}{2(1-\mu)}
>1.
\]

For minimality, a simple graph on two vertices has only one possible edge, so two distinct single-edge snapshots are impossible. Three vertices have three possible edges, and every pair of distinct edges shares exactly one endpoint, making every admissible period-two sequence isomorphic to the one analyzed above.

## Verification
The embedded `verify_two_contact_temporal_sis.py` uses only the Python standard library.

It reconstructs the two step matrices, multiplies them, and verifies the determinant factorization with exact rational arithmetic on
\[
399
\]
parameter pairs.

It verifies the exact temporal threshold identity and its strict aggregate comparison at
\[
99
\]
rational recovery probabilities.

It numerically replays the Perron crossing at three representative recovery probabilities, checks the exact
\[
\mu=\frac14
\]
example, and verifies the two-node impossibility and three-node uniqueness of the distinct-single-edge temporal pattern.

Run:

`python3 verify_two_contact_temporal_sis.py`

The first output line must be `VERIFY_OK`.

The universal formulas are proved algebraically above; the finite script is a reproducibility check rather than the source of the all-parameter proof.

## Relationship to prior work
Valdano, Ferreri, Poletto, and Colizza introduced the infection-propagator formulation for discrete-time SIS spreading on arbitrary temporal networks. Their linearized temporal operator has one factor
\[
(1-\mu)I+\lambda A^{(t)}
\]
per snapshot, and the epidemic threshold is characterized by spectral radius one of the period product.

Their analysis also identifies the static time-average network as the slow-disease or annealed comparator.

Speidel, Klemm, Eguíluz, and Masuda later emphasized that discrete-time and continuous-time temporal SIS models can move epidemic thresholds in opposite directions. In their Appendix I, for snapshots sampled randomly with replacement, the discrete-time threshold is at least the threshold of the aggregate network. They also discuss single-link snapshots separately.

The present result is narrower and deterministic. It solves the smallest possible period-two single-contact case exactly: three nodes are necessary and sufficient for two distinct snapshots, the temporal sequence is unique up to symmetry, and its threshold penalty relative to the aggregate has the closed form
\[
\sqrt{
\frac{2-\mu}{2(1-\mu)}
}.
\]

Targeted searches using alternating-edge, three-node, single-link-snapshot, infection-propagator, exact-threshold, and aggregate-comparison language did not locate this closed-form minimal case.

## Limitations
The result is restricted to a deterministic period of two snapshots, one active edge per snapshot, and the individual-based discrete-time SIS approximation.

It does not imply that every deterministic temporal sequence has a threshold above its aggregate. The direction of temporal effects depends on the model, update convention, and contact sequence.

The formal threshold can exceed the admissible probability range
\[
0\le\lambda\le1
\]
for sufficiently large recovery probability. In that regime the formula means that the disease-free linearization remains stable throughout the physical transmission-probability interval.

For sparse single-link snapshots, stochastic extinction effects can be important and are not represented by the deterministic mean-field threshold.

An unindexed worked example could contain the same three-node matrix calculation even though the exact minimality-and-ratio statement was not located.

## References
1. E. Valdano, L. Ferreri, C. Poletto, and V. Colizza, “Analytical computation of the epidemic threshold on temporal networks,” arXiv:1406.4815, first submitted 18 June 2014; later *Physical Review X* 5, 021005 (2015). DOI: 10.1103/PhysRevX.5.021005.
2. L. Speidel, K. Klemm, V. M. Eguíluz, and N. Masuda, “Temporal interactions facilitate endemicity in the susceptible-infected-susceptible epidemic model,” arXiv:1602.00859, first submitted 2 February 2016; *New Journal of Physics* 18, 073013 (2016). DOI: 10.1088/1367-2630/18/7/073013.
