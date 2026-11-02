# Six pure ground-state phases and a flat-band correlation law for ternary Hamming Blume–Capel models

## Finding

Let \(d\ge2\) and \(G=H(d,3)=K_3^{\square d}\). For positive field, the spin-one antiferromagnetic Blume–Capel model on \(G\) has exactly six attainable open-region ground-state phases. Their complete ground-state multiplicities and the two-point covariance in the uniform ground-state ensemble are given by a six-row local table and one universal distance law. Both the exact phase envelope and the correlation law hold for arbitrary \(d\), not just for the enumerated small graphs.

For \(x=D/(dJ)\) and \(y=h/(dJ)>0\), let \(f_T(x,y)\) denote the local energy associated to an unordered triple \(T\):

| Local spin multiset \(T\) | \(f_T(x,y)\) | Strict-phase multiplicity | Witness \((x,y)\) |
|---|---|---|---|
| \((0,0,0)\) | \(0\) | \(1\) | \((3,1)\) |
| \((0,0,+1)\) | \(x-y\) | \(3\cdot2^{d-1}\) | \((1,3/2)\) |
| \((-1,0,+1)\) | \(-1+2x\) | \(3\cdot2^d\) | \((1/10,1/50)\) |
| \((-1,+1,+1)\) | \(-1+3x-y\) | \(3\cdot2^{d-1}\) | \((-2,1)\) |
| \((0,+1,+1)\) | \(1+2x-2y\) | \(3\cdot2^{d-1}\) | \((1/5,2)\) |
| \((+1,+1,+1)\) | \(3+3x-3y\) | \(1\) | \((0,5)\) |

The exact energy is
\[
E_0=d3^{d-1}J\min_T f_T(x,y),\qquad h>0.
\]

Each table witness makes its indicated row the unique minimizer. At a strict minimum the allowed ground states are exactly the maps described below, with the displayed labeled counts. The statements for negative field follow by global spin reversal.

For such a strict phase, put \(\mu=(t_0+t_1+t_2)/3\) and \(v=(t_0^2+t_1^2+t_2^2)/3-\mu^2\). For vertices at Hamming distance \(r\), the uniform mixture over all ground states satisfies
\[
\mathbb E[(s_u-\mu)(s_v-\mu)]=v(-1/2)^r.
\]
The corresponding unnormalized Fourier transform on \(\mathbb F_3^d\), with character \(\omega^{k\cdot z}\) and \(\omega=e^{2\pi i/3}\), is exactly
\[
\widehat C(k)=\begin{cases}v(3/2)^d,& k_i\ne0\text{ for each }i,\\0,&\text{otherwise.}\end{cases}
\]
Thus, when \(v>0\), the structure factor is flat on the \(2^d\)-dimensional bottom adjacency-eigenvalue band \(-d\), and zero elsewhere. This is a collective, parameter-independent correlation signature of the four nonuniform phases.

## Assumptions and scope

All vertices \(z\in\mathbb F_3^d\) carry classical spins \(s_z\in\{-1,0,+1\}\); edges join vertices differing in exactly one coordinate. The Hamiltonian is
\[
\mathcal H(s)=J\sum_{\{u,v\}\in E(G)}s_us_v+D\sum_{z}s_z^2-h\sum_zs_z,
\quad J>0,\quad D,h\in\mathbb R.
\]
The graph has \(3^d\) sites, \(d3^{d-1}\) coordinate triangles and \(d3^d\) edges. A strict phase means that one listed local-spin multiset has strictly smaller energy than the other five for \(h>0\). The ground-state ensemble is the uniform measure on all labeled minimizing spin assignments, not a zero-temperature limit with symmetry-breaking boundary conditions.

At arbitrary \(h\), including coexistence boundaries, the exact energy and complete *configuration criterion* remain valid: minimize
\[
F(t_0,t_1,t_2)=t_0t_1+t_1t_2+t_0t_2+\frac{D}{dJ}\sum_jt_j^2-\frac{h}{dJ}\sum_jt_j
\]
over the ten multisets of three elements from \(\{-1,0,1\}\). Every global ground state, and only a ground state, has a minimizing multiset on **each** coordinate triangle. No closed formula for the total ground-state count at mixed-multiset coexistence boundaries is asserted.

## Proof

**1. Local decomposition and exact lower envelope.** Each graph edge belongs to one and only one coordinate triangle, while each site lies in exactly \(d\) coordinate triangles. Distributing each onsite term evenly gives the identity
\[
\mathcal H(s)=J\sum_{\ell\text{ coordinate triangle}}F((s_z)_{z\in\ell}).
\]
Consequently \(\mathcal H(s)\ge d3^{d-1}J\min F\). This lower bound is always attained: for any minimizing unordered triple \(T=(t_0,t_1,t_2)\), choose arbitrary signs \(a_1,\ldots,a_d\in\{+1,-1\}\subset\mathbb F_3^*\) and \(c\in\mathbb F_3\), and put
\[
s_z=t_{\,c+\sum_i a_iz_i\pmod3}.
\]
Every coordinate line then contains each residue exactly once and hence the triple \(T\). This proves the energy formula *and* the necessary-and-sufficient local condition for any parameter, including all boundaries.

**2. Six distinct positive-field candidates.** The ten unordered triples comprise three constant spins, six double-and-single types and one all-distinct type. Direct evaluation of \(F\) and pairwise spin inversion show that, for \(h>0\), the negative-magnetization partner of every nonzero-magnetization multiset is strictly worse. The six surviving triples are exactly the six table rows. Their evaluated energies are the six affine functions in the table. Substitution of each listed rational witness gives a strict minimum, proving that none of the six branches is redundant.

**3. Rigidity and ground-state counts.** If the unique minimum is an all-distinct triple, every coordinate line must contain each of three spins exactly once, making \(s\) an order-three Latin hypercube. Its values, identified with \(\mathbb F_3\) by a fixed bijection, necessarily have the affine form \(c+\sum_i a_i z_i\), with \(a_i\in\{1,-1\}\). Here is a direct induction. Every one-variable permutation of \(\mathbb F_3\) is affine. If the last-coordinate sections of a \(d\)-variable Latin function are affine, their pairwise differences are affine functions that never vanish; any nonconstant affine form on \(\mathbb F_3^{d-1}\) has a zero, so each difference is a nonzero constant. The three sections are therefore \(L\), \(L+1\), \(L-1\) in some order, establishing the asserted affine form. This yields exactly \(3\cdot2^d\) distinct assignments.

If the minimizing triple has one singleton value and two equal values, the singleton sites form a set meeting every coordinate line in exactly one point. Such a set is an affine hyperplane \(c+\sum_i a_i z_i=0\) with every \(a_i\ne0\). To prove this independently, induct on \(d\). Its three sections at fixed last coordinate are each singleton-line sets in \(\mathbb F_3^{d-1}\), hence affine hyperplanes by induction. They partition \(\mathbb F_3^{d-1}\); disjoint hyperplanes must be parallel, giving one affine equation with nonzero last coefficient. The base case \(d=1\) is immediate. There are \(3\cdot2^d/2=3\cdot2^{d-1}\) distinct such hyperplanes, since simultaneous negation of coefficients and constant does not change the zero set. Constant-spin phases have one assignment each. This proves all six degeneracies.

**4. Correlation and Fourier support.** Sample a uniform affine ground state by choosing independent signs \(a_i\in\{1,-1\}\) and a uniform offset \(c\in\mathbb F_3\); for a two-valued triple each labeled state has precisely two such representations, so the induced law is still uniform. Let \(r\) be the number of differing coordinates of two vertices. The probability that their affine residues agree is
\[
P_r=\frac{1+2(-1/2)^r}{3},
\]
since \(\mathbb E[\omega^{\pm1}]=-1/2\). Conditionally on equal residues, the covariance contribution is \(v\); for unequal residues it is \(-v/2\), by averaging the three cyclic pairs of distinct symbols. Hence \(C_r=v[P_r-(1-P_r)/2]=v(-1/2)^r\). Fourier transformation factors over coordinates: each coordinate sum is zero when \(k_i=0\), and \(3/2\) otherwise. This proves the flat structure factor and its exact support. Since the adjacency eigenvalue of a ternary character is \(\sum_i(2\mathbf1_{k_i=0}-\mathbf1_{k_i\ne0})\), the supported characters all have eigenvalue \(-d\).

## Verification

The standalone standard-library script `verification.py` enumerates the exact six parameter witnesses and all \(3^9=19683\) spin assignments on \(H(2,3)\), checks their ground energies and degeneracies, constructs every affine ground state for dimensions \(1\) through \(4\), checks each coordinate-triangle constraint, and verifies centered correlations exactly using rational arithmetic for dimensions \(1,2,3\). See `verification_output.txt` for actual output; execution reported 233 affine configurations, 6 complete field witnesses, and 4914 exact covariance comparisons. These finite checks support but do not replace the arbitrary-dimension proof above.

## Relationship to prior work

McKay and Wanless, *A Census of Small Latin Hypercubes* (2008), Section 4, explicitly proves the all-order-three Latin-hypercube affineness and the count \(3\cdot2^d\); these are used and independently explained, not claimed novel. Varma's 2013 paper develops exact saturation-field entropy methods for Ising ladders and kagome geometry, not this ternary Cartesian-power spin-one model. Park and Kwak (2016) study an antiferromagnetic Blume–Capel model on the triangular lattice, which differs from \(K_3^{\square d}\); only their accessible article information, not a complete primary text, was available for comparison. An already established zero-field local calculation on line graphs of cubic edge-three-colorable graphs includes the special case \(H(2,3)=L(K_{3,3})\) at \(h=0\). That special case and the Latin-hypercube census are not the novelty claim. The assessed contribution is the coupled all-dimensional six-branch field/anisotropy classification and its ground-state correlation/structure-factor theorem, particularly in \(d\ge3\).

## Limitations

All spins are classical, exchange is uniform and positive, graph factors all have exactly three vertices, and the calculated measure is the finite-size zero-temperature uniform ground-state mixture. The entropy and phase-boundary degeneracies are not completely enumerated when several distinct local multisets coexist; the local-minimizer condition is a complete characterization but not a closed count in that case. No positive-temperature free energy, thermodynamic symmetry breaking, or physical realization of a \(d\)-dimensional Hamming graph is established. The work does not claim the known Latin-hypercube count as new. Independent audit and historical-priority certification have not occurred.

## References

1. B. D. McKay and I. M. Wanless, *A Census of Small Latin Hypercubes*, SIAM J. Discrete Math. 22 (2008), 719–736; DOI: [10.1137/070693874](https://doi.org/10.1137/070693874). Author's lawful full text: https://users.cecs.anu.edu.au/~bdm/papers/hypercubes.pdf . Particularly Section 4, pages 10–11.
2. V. K. Varma, *Saturation field entropies of antiferromagnetic Ising model: Ladders and the kagome lattice*, arXiv:1305.4606 (initial submission 2013-05-20), https://arxiv.org/abs/1305.4606 .
3. S. Park and W. Kwak, *Phase Diagram of the Antiferromagnetic Blume-Capel Model on Triangular Lattice*, J. Phys. Conf. Ser. 738 (2016), 012126; DOI: [10.1088/1742-6596/738/1/012126](https://doi.org/10.1088/1742-6596/738/1/012126).
