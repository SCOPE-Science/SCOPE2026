# Image-size variance for the sum of two random permutations detects finite abelian group structure

## Finding

Let \(G\) be a finite abelian group of cardinality \(N\ge2\). Let \(\pi_1,\pi_2:G\to G\) be independent uniform random permutations, and let \(R=|\{\pi_1(x)+\pi_2(x):x\in G\}|\) denote their sum's image cardinality. Put
\[
 d_N=\sum_{j=0}^{N}\frac{(-1)^j}{j!},\qquad
 A_m(t)=\sum_{k=0}^{m}\frac{2m}{2m-k}\binom{2m-k}{k}t^k
\]
for every integer \(m\ge2\). For any divisor \(m\ge2\) of \(N\), put
\[
 Q_N(m)=\frac1{N!}\sum_{k=0}^{N}(-1)^k (N-k)!\,[t^k]A_m(t)^{N/m}.
\]
The exact mean and variance are
\[
 \boxed{\mathbb ER=N(1-d_N),\qquad
 \operatorname{Var}(R)=Nd_N-N^2d_N^2+
 N\sum_{0\ne h\in G}Q_N(\operatorname{ord}(h)).}
\]
Indeed, for any distinct output labels \(y,z\in G\), the probability that **both** labels are absent is exactly \(Q_N(\operatorname{ord}(z-y))\). Thus the variance depends on the counts of nonzero elements of each order in \(G\), even though the mean depends only on \(N\).

For the two nonisomorphic groups of order four, the complete image-size laws differ: on \(\mathbb Z/4\mathbb Z\), the probabilities at cardinalities \(1,2,3\) are \(1/6,1/6,2/3\); on \((\mathbb Z/2\mathbb Z)^2\), the probabilities at cardinalities \(1,2,4\) are \(1/6,1/2,1/3\). Both have mean \(5/2\), but their variances are, respectively, \(7/12\) and \(5/4\).

## Assumptions and scope

The group is abelian, finite and nontrivial. Permutations are sampled independently and uniformly from all bijections of its underlying set. Group addition is the fixed group operation. The exact formula concerns image-size mean, variance and pairwise absent-output probabilities; it is not a formula for the entire image-size distribution in arbitrary group order. The order \(\operatorname{ord}(h)\) is the least positive \(m\) such that \(mh=0\). All sums, polynomials and coefficients are finite. The coefficient of \(t^0\) in \(A_m\) is one.

## Proof

**Step 1 (relabel inputs).** Conditioning on \(\pi_1\), reindex the inputs by \(u=\pi_1(x)\). The permutation \(\sigma=\pi_2\circ\pi_1^{-1}\) is uniform on permutations of \(G\), and the set of outputs has the same distribution as \(\{u+\sigma(u):u\in G\}\). Consequently, for a given \(y\in G\), its absence is the event \(\sigma(u)\ne y-u\) for all \(u\). The map \(u\mapsto y-u\) is a bijection, so this is a usual derangement avoidance event. Inclusion-exclusion gives probability \(d_N\).

**Step 2 (two forbidden perfect matchings).** For distinct \(y,z\in G\), simultaneous absence means avoiding all edges in the union of the two perfect matchings of the bipartite row-column graph,
\[
 M_y=\{(u,y-u):u\in G\},\qquad
 M_z=\{(u,z-u):u\in G\}.
\]
The matchings are disjoint because \(y\ne z\). Alternating a \(M_y\)-edge with a reverse \(M_z\)-edge moves row labels by \(z-y\) or its negative. Each orbit of translation by \(h=z-y\) has \(m=\operatorname{ord}(h)\) elements. Thus the union splits into exactly \(N/m\) disjoint bipartite cycles, each consisting of \(2m\) edges, with no further edges.

**Step 3 (cycle rook polynomial).** For a cycle with \(2m\) edges, a subset of edges is a matching of size \(k\) precisely when no two selected edges are adjacent in cyclic order. The number of such subsets is
\[
 a_{m,k}=\frac{2m}{2m-k}\binom{2m-k}{k},\qquad 0\le k\le m.
\]
To derive this identity, mark one of the \(k\) selected cycle edges and record the \(k\) positive intervening cyclic gaps after reserving one unselected edge after each selection. Counting the resulting weak compositions of \(2m-2k\) into \(k\) gaps yields \((2m/k)\binom{2m-k-1}{k-1}\) for \(k\ge1\), equal to the displayed coefficient. For \(k=0\), the count is one. Because cycles are disjoint, the rook polynomial of the entire forbidden board is \(A_m(t)^{N/m}\), and \([t^k]\) counts the ways to select \(k\) pairwise row- and column-disjoint forbidden positions.

**Step 4 (inclusion-exclusion).** For each selected collection of \(k\) nonattacking forbidden positions, precisely \((N-k)!\) permutations contain all of them. Inclusion-exclusion therefore shows that the number of permutations avoiding the union is
\[
 \sum_{k=0}^{N}(-1)^k(N-k)![t^k]A_m(t)^{N/m}.
\]
Dividing by \(N!\) proves the claimed exact pairwise absence probability \(Q_N(m)\).

**Step 5 (variance).** For each \(y\in G\), let \(I_y\) be its absent-output indicator, and let \(M=\sum_{y\in G}I_y=N-R\). All \(I_y\) have mean \(d_N\), and for \(y\ne z\) their product has expectation \(Q_N(\operatorname{ord}(z-y))\). Hence
\[
 \operatorname{Var}(R)=\operatorname{Var}(M)
 =Nd_N+\sum_{y\ne z}Q_N(\operatorname{ord}(z-y))-N^2d_N^2.
\]
Each nonzero difference \(h=z-y\) occurs for exactly \(N\) ordered pairs \((y,z)\), proving the variance formula.

**Step 6 (order four).** Exhaustively enumerate the \(4!\) uniform permutations \(\sigma\) in the representation \(u+\sigma(u)\). The image-size counts are \((4,4,16)\) at cardinalities \((1,2,3)\) for the cyclic group and \((4,12,8)\) at \((1,2,4)\) for the elementary abelian group. Division by \(24\), direct first and second moments, and the exact general formula yield the stated means and variances.

## Verification

Run `python verify.py` with the Python standard library (version 3.9 or newer). It checks the independent finite-permutation enumeration of image-size moments and forbidden-symbol pair counts for all finite abelian product groups in its explicitly listed bounded test suite (orders two through eight); it also independently enumerates small nonattacking rook placements and compares them against the cycle polynomial. The run reported `PASS: 200 grouped exact identities; zero Monte Carlo estimation.` All checks use integer or rational arithmetic and are reproducible. These finite computations corroborate boundary cases; the proof of the general formula is the preceding exact bijection and inclusion-exclusion.

## Relationship to prior work

Bhaumik, Guo, Guo and Jha introduce and analyze this same sum-of-independent-permutations random map over finite abelian groups (arXiv:2609.35421, publicly submitted September 28, 2026), focusing on distinguishability bounds for classical and quantum queries. Their work supplies the motivating random map but, in the inspected paper, not the global image-size variance as an arithmetic function of the group element-order profile. The general technique of rook-polynomial inclusion-exclusion is classical and is not claimed as new.

Donovan, Johnson and Wanless study the permanent and determinant of Latin squares, showing in particular how cycles between two symbols influence coefficients involving only those two symbols (DOI:10.1002/jcd.21418). This is a close antecedent for the two-symbol cycle structure. The accessible abstract does not explicitly give the present two-symbol **avoidance** probability, image-size covariance formula, or order-four contrast. The full article was not accessible in the present comparison; it could contain a broader result that implies portions of the theorem, which remains a priority risk.

## Limitations

No claim is made for nonabelian groups, more than two permutation summands, asymptotic normality, or a closed full law for arbitrary group order. The exact formula is expressed as a finite coefficient extraction and can be computationally expensive for large groups. Its derivation uses established rook theory, and originality relative to all historical finite Latin-square/permanent literature has not been independently established. The order-four distinction is exact but should not be read as a universal criterion for group-isomorphism identification by variance.

## References

1. R. Bhaumik, C. Guo, X. Guo and A. Jha, *Indistinguishability of Sum of Permutations: A Fourier Analytic Route to Classical and Quantum Security*, arXiv:2609.35421 (first submitted 2026-09-28), https://arxiv.org/abs/2609.35421.
2. D. Donovan, K. Johnson and I. M. Wanless, *Permanents and Determinants of Latin Squares*, Journal of Combinatorial Designs 24 (2016), 132–148; first online 2014, DOI:10.1002/jcd.21418.
