# Exact fluctuations and macroscopic budgets for cooperative metastability in open random Ising chains

## Finding

Consider an open ferromagnetic Ising chain on \(N\ge3\) sites, with energy
\[H(\sigma)=-\sum_{j=1}^{N-1}J_j\sigma_j\sigma_{j+1},\qquad J_j>0,\quad\sigma_j\in\{-1,+1\}.\]
For an integer \(r\ge1\), call a configuration \(r\)-stable if flipping any set of at most \(r\) sites cannot lower its energy. Let \(B_{N,r}\) be the number of these configurations. For iid atomless positive couplings and each fixed \(r\),
\[
\frac{\log B_{N,r}}{N}\longrightarrow\frac{\log 2}{2r+1}\quad\text{almost surely},
\qquad
\frac{\log B_{N,r}-N\log 2/(2r+1)}{\sqrt N}
\Longrightarrow \mathcal N(0,(\log 2)^2v_r),
\]
where the variance density for arbitrary fixed radius is
\[
v_r=\frac4{2r+1}\sum_{d=r+1}^{2r}\frac1{2r+1+d}-\frac{2r}{(2r+1)^2}>0.
\]
In particular \(v_1=2/45\) and \(v_2=13/450\), recovering the known variance densities for the first two radii on a ring.

For \(N\le3r+2\), the law of \(B_{N,r}\) is exactly supported on \(\{2,4\}\), with
\[\mathbb P(B_{N,r}=4)=\frac{(N-2r-1)_+}{2r+1}.\]
Thus when \(r/N\to\alpha\in(1/3,1/2)\), the limiting probabilities of four and two configurations are \((1-2\alpha)/(2\alpha)\) and its complement. This regime differs from the extensive entropy and Gaussian fluctuations at fixed \(r\).

## Domain-wall reduction and assumptions

For any pairwise-distinct positive couplings (without a randomness assumption), set
\[\mathcal V_{N,r}=\{j:r<j<N-r,\ J_j<J_k\text{ for all }k\ne j,\ |k-j|\le r\},\qquad M_{N,r}=|\mathcal V_{N,r}|,\]
with bond indices in \(\{1,\ldots,N-1\}\). The wall sets of \(r\)-stable configurations are exactly the subsets of \(\mathcal V_{N,r}\). Given a wall set, a choice of the first spin fixes all other spins. Hence \(B_{N,r}=2^{M_{N,r}+1}\). This is the open-chain, radius-\(r\) form of the weak-bond representation; it is the reduction used below, not a claim to have introduced weak bonds or cooperative stability.

Flips are simultaneous, and energy-neutral moves are allowed. The reduction includes \(r\ge N\). For the almost-sure statement, one can use successive segments of a single iid bond sequence. No dynamics or quench distribution is assumed.

## Proof

Write \(\tau_j=\sigma_j\sigma_{j+1}\). An interior contiguous interval with boundary bonds \(i<j\) has length \(j-i\), and flipping it changes the energy by \(2(J_i\tau_i+J_j\tau_j)\). An interval meeting just one chain end has a single boundary bond \(j\), with change \(2J_j\tau_j\). A flip of the whole chain has zero cost. For a disconnected flip set, the maximal contiguous pieces change disjoint sets of boundary bonds, so their costs add. It therefore suffices to check all contiguous intervals of length at most \(r\).

A stable wall at \(j\) must have \(r<j<N-r\), since a prefix or suffix reaching it would otherwise have negative cost. For \(0<|k-j|\le r\), flipping the interval between \(j,k\) would lower energy if \(k\) were a wall or if \(J_k<J_j\). Distinctness of the couplings makes \(j\) a strict radius-\(r\) minimum. Conversely, any two such minima are more than \(r\) apart. With a subset of them as walls, a prefix or suffix of allowed length has no boundary wall; an interior interval either has no boundary wall or has one, whose coupling is strictly smaller than that of the other boundary. All these moves have nonnegative cost, as required.

For the statistics let \(m=2r+1\) and use a two-sided iid extension, with \(I_j\) the indicator that bond \(j\) is smallest in its full window of size \(m\). The eligible open-chain bond count is \(K=(N-m)_+\) and \(M_{N,r}\) is the sum of \(I_j\) over those bonds. By exchangeability \(p=\mathbb E I_j=1/m\), so \(\mathbb E M_{N,r}=K/m\). The stationary sequence is bounded and \(2r\)-dependent. The ergodic theorem gives the entropy limit.

At separations \(1\le d\le r\) the minimum events exclude one another, while \(d>2r\) gives independent windows. For \(r<d\le2r\), if both are minima, the smallest bond in the union of the windows must be one of the two centers. Each is the smallest with probability \(1/(m+d)\). Conditional on this event for either center, it does not belong to the other center's window, and the relative order of the bonds in that other window is still uniform. Thus \(\mathbb E I_0 I_d=2/[m(m+d)]\). Consequently the asymptotic variance per bond is
\[p(1-p)+2\sum_{d=1}^{2r}(\mathbb E I_0I_d-p^2)=\frac4m\sum_{d=r+1}^{2r}\frac1{m+d}-\frac{2r}{m^2}.\]
All denominators \(m+d\) in the sum are at most \(4r+1\), giving the positive lower bound \(2r/[m^2(4r+1)]\) (equality at \(r=1\)). The central limit theorem for bounded stationary finite-dependent sequences applies at each fixed \(r\). When \(N\ge m\), \(\mathbb E \log B_{N,r}=(K/m+1)\log 2=N\log 2/m\), and \(K/N\to1\). These give the stated normalization.

For \(N\le3r+2\), at most one eligible bond is a radius-\(r\) minimum: their index interval has diameter at most \(r\) whenever nonempty. Thus \(M_{N,r}\) is Bernoulli with parameter \(K/m\), also covering the empty interval with parameter zero. The exact law and proportional-budget limit follow.

## Verification

The accompanying standalone `verify.py` enumerates spin configurations and flip sets through \(N=10\) on selected distinct positive coupling vectors, and enumerates rank orders for representative two-window cases at radii 1 and 2. It is finite corroboration, not a substitute for the proof at arbitrary \(r\) or for the limit theorems.

## Relationship to prior work and limitations

Newman and Stein [1] define stability against any subset of up to \(M\) spin flips (p. 4) and describe the arbitrary satisfied/unsatisfied choice at weak bonds for the one-spin-stable infinite chain (Eq. (6) and discussion, p. 16). The ring calculation [2] gives the radius-1 and radius-2 weak-bond representations with even wall parity, their individual variance densities, and a joint Gaussian limit. These antecedents cover the weak-bond mechanism and the first two variance densities. The distinct content here is the exact one-level variance for arbitrary fixed \(r\) and the finite open-boundary law when the budget is large enough to permit at most one wall. The open-chain wall classification and entropy formula are supplied to make the derivation self-contained. The result does not address intermediate proportional budgets outside the stated regime, interacting/disordered fields, tied bonds, relaxation, or a Gaussian limit with \(r\) increasing with chain length. Priority against every historical treatment of one-dimensional multi-spin stability is not established; Newman and Stein point in particular to T. Li [3].

1. C. M. Newman and D. L. Stein, *Metastable States in Spin Glasses and Disordered Ferromagnets*, Phys. Rev. E **60**, 5244 (1999), [arXiv:cond-mat/9908455](https://arxiv.org/abs/cond-mat/9908455).
2. *Negative covariance across two levels of metastability in a random ferromagnetic ring*, [record 190dc97a4214](https://github.com/Resultary/2026/blob/36a7204b5741b75430355c38bf9bf0ef7468c2a4/2026/10/18/SCOPE-negative-covariance-across-two-levels-of-metastability-in-a-rand--190dc97a4214/RESULT.md).
3. T. Li, Phys. Rev. B **24**, 6579 (1981), [DOI:10.1103/PhysRevB.24.6579](https://doi.org/10.1103/PhysRevB.24.6579).
