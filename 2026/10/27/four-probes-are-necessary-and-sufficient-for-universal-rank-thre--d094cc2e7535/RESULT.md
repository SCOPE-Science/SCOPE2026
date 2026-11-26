# Four probes are necessary and sufficient for universal rank-three qubit-channel identification

## Finding

For complex square quantum channels on \(M_d(\mathbb C)\), with \(d\ge2\), any fixed probe set that identifies every channel of exact Choi rank \(r\) among all CPTP channels must contain at least
\[
\left\lceil\frac{2d^2r-d^2-r^2}{d^2-1}\right\rceil
\]
input states. In particular, the universal minimum for exact rank-three qubit channels is four: every fixed triple fails for at least one rank-three channel, while four linearly independent qubit density matrices identify every qubit channel. For any fixed probe triple, each connected component of the exact-rank-three channel manifold has an open dense subset on which the same-output fibers within that manifold are locally smooth and at least two-dimensional.

Here “universal” means one fixed set of input density matrices works for every target in the stated exact-rank class; competing channels are not assumed to have the same rank. The general formula is a necessary lower bound, not an asserted exact minimum for every \(d,r\). The rank-three qubit case is exact.

## Assumptions and scope

A channel is a completely positive trace-preserving complex-linear map \(\Phi:M_d(\mathbb C)\to M_d(\mathbb C)\). Its Choi rank equals its minimal Kraus rank. For \(d\ge2\) we consider \(1\le r\le d^2\). At \(d=1\) there is just one channel, of rank one, so zero probes suffice and the displayed quotient does not apply. A probe is a fixed density matrix \(\rho_j\); the observed data are the exact output states \(\Phi(\rho_j)\), with no statistical or measurement noise. A probe set selected separately for each target is not a universal fixed set.

## Proof

Let \(\mathcal M_{d,r}\) be the exact Choi rank \(r\) channel manifold. In a minimal Kraus representation the \(r\) stacked \(d\)-by-\(d\) Kraus operators form an isometry in the complex Stiefel manifold of \(d\)-frames in \(\mathbb C^{rd}\). Minimality is an open linear-independence condition. Unitary mixing of the \(r\) Kraus operators acts freely and represents precisely the channel gauge. Hence the real dimension is the Stiefel dimension minus \(\dim U(r)\):
\[
\dim_{\mathbb R}\mathcal M_{d,r}=2rd^2-d^2-r^2=:p.
\]
For the analytic structure, the rank-\(r\) positive-semidefinite Choi matrices form a real-analytic manifold, as is seen in a chart with an invertible \(r\)-by-\(r\) principal block by writing the remaining diagonal block via the vanishing Schur complement. On this manifold the partial trace over the output is a submersion at the trace-preserving level. Indeed, congruence by \((I+tH/2)\otimes I\) preserves rank and positivity for small \(t\) and gives partial-trace derivative \(H\) at a Choi matrix with partial trace \(I\), for any Hermitian \(H\). This also gives the real-analytic manifold structure of \(\mathcal M_{d,r}\) in Choi coordinates.

For fixed probes \(\rho_1,\ldots,\rho_k\), the evaluation map
\[
E(\Phi)=(\Phi(\rho_1),\ldots,\Phi(\rho_k))
\]
is real analytic in these coordinates. Each output is a trace-one Hermitian matrix, so the real affine data-space dimension is \(q=k(d^2-1)\). If \(p>q\), an injective evaluation map on the rank stratum would yield, by restricting to a coordinate chart and composing with \(\mathbb R^q\hookrightarrow\mathbb R^p\), a continuous injection of an open subset of \(\mathbb R^p\) into a proper linear subspace of \(\mathbb R^p\). Invariance of domain rules this out. Universality requires injectivity even within the exact-rank stratum, so \(q\ge p\).

For rank-three qubit channels, \(p=11\) and three probes give at most nine real output coordinates. Thus a fixed triple cannot distinguish all exact-rank-three channels even from one another. Define \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\) and \(|+i\rangle=(|0\rangle+i|1\rangle)/\sqrt2\). The four density matrices
\[
|0\rangle\langle0|,\quad |1\rangle\langle1|,\quad |+\rangle\langle+|,\quad |+i\rangle\langle+i|
\]
span \(I,\sigma_x,\sigma_y,\sigma_z\). Agreement on them gives agreement on all Hermitian inputs and hence, by complex linearity, on every input. Four probes therefore suffice against arbitrary CPTP competitors.

For a fixed triple, let \(s\le9\) be the maximal differential rank of \(E\) on a connected component of \(\mathcal M_{2,3}\). Its rank-\(s\) locus is open dense: for \(s>0\) the analytic tensor \(\bigwedge^s dE\) is not identically zero and thus cannot vanish on any open set of the component; for \(s=0\) the entire component qualifies. On this locus the constant-rank theorem gives a smooth local fiber of dimension \(11-s\ge2\).

## Verification

This proof uses the fixed-rank channel dimension, invariance of domain, and the constant-rank theorem, rather than numerical experiments. The numerical specialization is \(p(2,3)=11\), compared to the three-probe data dimension \(9\). Linear spanning of all qubit Hermitian matrices is sufficient with no assumptions on the competitor's rank.

## Relationship to prior work

Kuklina, Vasilenko, Volkov and Pechen give a fixed three-state set for the canonical-form rank-two qubit problem (Theorem 2); for a general rank-two target they rotate the inputs by its input unitary (Proposition 1). They also prove a lower bound of \(d^2\) inputs for full-Choi-rank channels, agreeing with the displayed bound when \(r=d^2\). These statements do not settle the universal fixed-probe threshold in the intermediate rank-three qubit stratum. Iten and Colbeck supply the fixed-rank channel-manifold dimension; their parameter-count application concerns circuit representations of extreme channels, not fixed-probe evaluation. Reich, Gualdi and Koch study unitary gate characterization and average-fidelity estimation rather than rank-three nonunitary channel identification.

## Limitations

For general \(d,r\), no matching upper bound is asserted. The generic fiber statement is restricted to an open dense set for each fixed triple, not all individual target channels. The results concern exact outputs and do not quantify robustness to sampling, preparation error, or measurement noise.

## References

1. N. E. Kuklina, V. Iu. Vasilenko, B. O. Volkov and A. N. Pechen, “Unique determination and generation of rank two single-qubit quantum channels,” arXiv:2609.14707v1; J. Phys. A: Math. Theor. 59, 355309 (2026), DOI 10.1088/1751-8121/ae9b4f.
2. R. Iten and R. Colbeck, “Smooth Manifold Structure for Extreme Channels,” arXiv:1610.02513v2; J. Math. Phys. 59, 012202 (2018), DOI 10.1063/1.5019837.
3. D. M. Reich, G. Gualdi and C. P. Koch, “Minimum number of input states required for quantum gate characterization,” arXiv:1305.3222; Phys. Rev. A 88, 042309 (2013).
