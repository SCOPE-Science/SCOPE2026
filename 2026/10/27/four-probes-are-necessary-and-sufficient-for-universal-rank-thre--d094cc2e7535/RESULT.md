# Four probes are necessary and sufficient for universal rank-three qubit-channel identification

## Finding

For complex square quantum channels on \(M_d(\mathbb C)\) of exact Choi/Kraus rank \(r\), any fixed probe set that identifies every rank-\(r\) channel among all CPTP channels must contain at least \[\left\lceil\frac{2d^2r-d^2-r^2}{d^2-1}\right\rceil\] input states. In particular, the universal minimum for exact rank-three qubit channels is four: every fixed triple fails for at least one rank-three channel, while four linearly independent qubit density matrices identify every qubit channel. For any fixed triple, the rank-three qubit channels with locally at least two-dimensional same-output fibers form an open dense subset of each connected component of the exact-rank-three channel manifold.

Here “universal” means one fixed set of input density matrices works for every target in the stated exact-rank class; competing channels are not assumed to have the same rank. The general formula is a necessary lower bound, not an asserted exact minimum for every \(d,r\). The rank-three qubit case is exact.

## Assumptions and scope

All spaces are finite-dimensional complex matrix algebras. A channel is a completely positive trace-preserving linear map \(\Phi:M_d(\mathbb C)\to M_d(\mathbb C)\). Its Choi rank equals its minimal Kraus rank. The exact-rank-
\(r\) channel set is considered for \(1\le r\le d^2\). A probe is a fixed density matrix \(\rho_j\); the observed data are the exact output states \(\Phi(\rho_j)\), with no statistical or measurement noise. The claim concerns universal identification by one fixed probe set, not whether a specially chosen set can isolate an individual exceptional target with fewer probes.

## Proof

Let \(\mathcal M_{d,r}\) denote the manifold of channels of exact Choi rank \(r\). In a minimal Kraus representation, stacking the \(r\) Kraus operators gives an isometry in the complex Stiefel manifold of \(d\)-frames in \(\mathbb C^{rd}\). The Stiefel manifold has real dimension \(2rd^2-d^2\); unitary mixing of the \(r\) minimal Kraus operators acts freely, and quotienting by \(U(r)\), of real dimension \(r^2\), gives

\[
\dim_{\mathbb R}\mathcal M_{d,r}=2d^2r-d^2-r^2=:p.
\]

For fixed probes \(\rho_1,\ldots,\rho_k\), define the smooth evaluation map

\[
E(\Phi)=(\Phi(\rho_1),\ldots,\Phi(\rho_k)).
\]

A trace-one Hermitian \(d\times d\) matrix lies in an affine real space of dimension \(d^2-1\), so the data lie in a real affine space of dimension \(q=k(d^2-1)\). If \(p>q\), no continuous map from the whole \(p\)-dimensional channel manifold into this \(q\)-dimensional data space can be injective. Indeed, restrict a hypothetical injection to a coordinate chart in \(\mathbb R^p\) and compose it with the standard embedding \(\mathbb R^q\hookrightarrow\mathbb R^p\). Invariance of domain would force the image to be open in \(\mathbb R^p\), although it lies in a proper linear subspace, a contradiction. Hence \(k(d^2-1)\ge p\), giving the displayed lower bound.

For qubits of exact Choi rank three, \(p=2\cdot 2^2\cdot3-2^2-3^2=11\). Three probes provide at most \(3(2^2-1)=9\) real output coordinates, so no fixed triple can identify every rank-three qubit channel. Define \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\) and \(|+i\rangle=(|0\rangle+i|1\rangle)/\sqrt2\). The four states

\[
|0\rangle\langle0|,\quad |1\rangle\langle1|,\quad |+\rangle\langle+|,\quad |+i\rangle\langle+i|
\]

span the real vector space of Hermitian \(2\times2\) matrices: they span \(I,\sigma_x,\sigma_y,\sigma_z\). Two linear maps agreeing on these four states agree on a basis and are identical. Thus four probes suffice even against competitors of arbitrary Choi rank, proving the exact universal minimum.

For the generic ambiguity statement, the evaluation map is real analytic on each connected component of \(\mathcal M_{2,3}\). Its maximal differential-rank locus is open and dense on each component. There the constant-rank theorem gives local fibers of dimension \(11-s\), where \(s\le9\) is the maximal differential rank. Each such fiber therefore has dimension at least two.

## Verification

The dimension formula is the fixed-Kraus-rank channel-manifold formula from the Stiefel-quotient description. The numerical specialization is \(p(2,3)=11\); the three-probe data-space dimension is \(9\); the four-probe spanning argument is exact and does not depend on positivity being strict. The proof uses invariance of domain and the constant-rank theorem, not finite experiments. The lower bound is necessary for universal identification; it is not claimed sharp for every rank and dimension.

## Relationship to prior work

Kuklina, Vasilenko, Volkov and Pechen prove that three suitably chosen states identify every rank-two qubit channel, and prove a lower bound of \(d^2\) states for full-Choi-rank channels. Their paper explicitly leaves extensions beyond rank two as future work. The argument here treats the exact rank-three qubit stratum, which is neither covered by their full-rank hypothesis nor by their rank-two theorem. Iten and Colbeck supply the smooth fixed-rank channel-manifold dimension, but their application concerns circuit-parameter lower bounds for extreme channels rather than the dimension of probe-output fibers. Reich, Gualdi and Koch study unitary gate characterization and average-fidelity estimation, not rank-three nonunitary channel identification.

## Limitations

The dimension bound is a necessary bound for a universal fixed probe set; for general \(d,r\), no matching upper bound is asserted. The generic fiber statement applies to the open dense maximal-rank locus for a fixed probe triple and does not say every individual rank-three channel has a two-dimensional fiber at every probe set. The results assume exact output states and do not quantify robustness under finite sampling, state-preparation error or measurement noise.

## References

1. N. E. Kuklina, V. Iu. Vasilenko, B. O. Volkov and A. N. Pechen, “Unique determination and generation of rank two single-qubit quantum channels,” arXiv:2609.14707v1 (first public 2026-09-13); J. Phys. A: Math. Theor. 59, 355309 (2026), DOI 10.1088/1751-8121/ae9b4f.
2. R. Iten and R. Colbeck, “Smooth Manifold Structure for Extreme Channels,” arXiv:1610.02513v2 (2019); J. Math. Phys. 59, 012202 (2018), DOI 10.1063/1.5019837.
3. D. M. Reich, G. Gualdi and C. P. Koch, “Minimum number of input states required for quantum gate characterization,” arXiv:1305.3222 (2013); Phys. Rev. A 88, 042309 (2013).
