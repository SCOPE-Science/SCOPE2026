# Independent mathematical audit

## correctness

PASS

For M even≥6 distinguishable stubs, each potential loop pair occurs with probability (M−1)⁻¹, and each pair of cross edges with probability 2/((M−1)(M−3)). Conditioning on a loop decreases its vertex pair count by 2d_i−3. This yields exact E L=A/(M−1), E P=2B/((M−1)(M−3)), E LP=2(AB−F)/((M−1)(M−3)(M−5)), and covariance 2(4AB−(M−1)F)/((M−1)²(M−3)(M−5)). Rebuilt the pair/triple/leaf decomposition D/2=∑a_i a_j Q_ij+∑T_ijk+ℓ∑a_i a_j(d_i+d_j−3), Q_ij=2d_id_j−3(d_i+d_j)+3. T_ijk≥0 by six-term AM–GM, equality only (2,2,2); each negative (2,2) pair is compensated by a distinct high-degree triple, and degree-one parity resolves the only remaining zero candidates. Thus covariance is positive precisely when B>0 and all positive degrees equal two, negative for all other B>0 sequences, zero at B=0. Independent small-profile direct full-pairing enumeration with exact rational numbers confirmed positive (2,2,2) and negative (3,3),(2,2,1,1),(2,3,1),(3,2,2,1),(4,2,2).

## originality

PASS

Qualified PASS only for uniform finite-size sign classification over all degree sequences and its positive degree-triple compensation identity. The configuration model, defect observables, exact separate means and asymptotic independent Poisson limits are established prior work.

## value

PASS

Self-loops and parallel-edge pairs control simplicity probabilities in the standard configuration model. Asymptotic independent Poisson statements do not identify finite-size dependence; the strict degree-two-only positive sign and universal negative sign otherwise supply a sharp, nontrivial boundary for arbitrary irregular degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
