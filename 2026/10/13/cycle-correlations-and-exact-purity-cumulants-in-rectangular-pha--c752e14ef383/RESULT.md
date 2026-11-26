# Exact forest independence and cycle correlations of squared phase overlaps

## Finding

Let \(d,m\ge2\) be integers and let \(z_{aj}\), \(1\le a\le d\), \(1\le j\le m\), be independent Haar-uniform unit complex phases. For an unordered pair of distinct rows let
\[
Y_{ab}=\Big|\sum_{j=1}^m z_{aj}\overline{z_{bj}}\Big|^2.
\]
For a simple graph \(G\) on the rows, the family \((Y_{ab}:\{a,b\}\in E(G))\) is mutually independent if and only if \(G\) is a forest. For every simple cycle \(C\) of length at least three,
\[
\mathbb E\prod_{\{a,b\}\in E(C)}(Y_{ab}-m)=m(m-1).
\]
Thus each pair of distinct edges is independent, but the first full product on any simple cycle yields a positive witness involving every edge of the cycle. Indeed, every proper subset of those edges is a forest and its nonempty centered product has zero mean.

The squared overlaps are the off-diagonal intensities of the Gram matrix of the rows. For a bipartite state with equal amplitudes and independent phases, they equal \((dm)^2|\rho_{ab}|^2\), where \(\rho=ZZ^\dagger/(dm)\) is the row-side reduced state and \(Z=(z_{aj})\). The graph result separates exact factorization of families of these intensities from the dependence that cannot be detected in any pairwise statistic.

## Proof

On an oriented edge \(a\to b\) put \(w_{ab,j}=z_{aj}\bar z_{bj}\). In a forest, choose a root in each component. For each column, the transformation from vertex phases to component-root phases and oriented edge ratios is a bijective group homomorphism of tori: vertex phases can be recovered recursively, since each nonroot vertex has a unique parent. It therefore sends Haar measure to the product Haar measure on the new coordinates. Applying this independently in each column shows that the vectors \((w_{ab,j})_{j=1}^m\) for the forest edges are independent. Each \(Y_{ab}\) is a function of its own edge vector, proving sufficiency.

For a row \(a\), form the complex vector \(X_a\) indexed by ordered column pairs \(j\ne k\), with \((X_a)_{jk}=z_{aj}\bar z_{ak}\). Its mean is zero and its second moment matrix is the identity:
\[
\mathbb E[(X_a)_{jk}\overline{(X_a)_{rs}}]=\mathbf1_{(j,k)=(r,s)}.
\]
This follows by integrating each independent column phase; an integer power of one phase has mean zero unless its exponent is zero. Oppositely ordered pairs give conjugate characters, not identical characters, so they are orthogonal in this complex inner product. Expanding the intensity gives \(Y_{ab}=m+X_b^\dagger X_a\); the off-diagonal term is symmetric under reversing the edge because the set of pairs is closed under swapping \(j,k\). In particular \(\mathbb E Y_{ab}=m\).

Orient the simple cycle coherently and write its vertices as \(a_1,\ldots,a_\ell\), with \(a_{\ell+1}=a_1\). In the expansion of \(\prod_{i=1}^\ell X_{a_{i+1}}^\dagger X_{a_i}\), each independent row contributes one component and one conjugate component of its feature vector. Its second moment matrix forces their indices to agree. Therefore a term survives exactly when every edge has the same ordered pair, and each surviving term has expectation one. There are \(m(m-1)\) such pairs. A family containing the cycle cannot be independent, since a product of independent centered variables would have mean zero. This proves necessity for every simple graph, including graphs with isolated vertices or disconnected components.

## Relationship to prior work

The unimodular phase ensemble and mean purity are studied by Nakata, Turner and Murao (arXiv:1111.2747) and Lakshminarayan, Puchała and Życzkowski (arXiv:1407.1169). The first two purity cumulants and the exact third cumulant are not claimed here; see Trotta et al. (arXiv:2605.10314, Section III) and [*Exact third purity cumulants and a cubic-root resonance in random Hadamard states*](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-exact-third-purity-cumulants-and-a-cubic-root-resonance-in-rando--0e21877b6a1a/RESULT.md). The latter includes the rectangular Haar-circle case, and its triangle contributions account for the three-row special case of the balance calculation. The conclusion here concerns the joint law of a graph-indexed family of individual squared overlaps and cycles of arbitrary length, not another purity cumulant.

Garza Vargas (arXiv:1709.01498, Sections 2–3) gives a general balance-count method for moments of graphs built from a square unimodular matrix. The phase orthogonality used here is standard and agrees with that method. The result here evaluates the centered mixed moment explicitly for all simple cycles and combines it with forest sufficiency to classify independence of the squared overlaps, for arbitrary rectangular dimensions. The related [forest criterion for fermionic edge phase differences](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-cycle-controlled-temporal-cumulants-and-a-forest-berry-esseen-th--66fc4902e081/RESULT.md) concerns phase differences before the nonlinear intensity map; their dependence alone does not show dependence of the intensities.

## Limitations and reproducibility

The law assumes independent uniform circle phases and a simple graph. When \(m=1\) the intensities are constant and the necessity of the forest condition does not apply. No statement is made about general amplitude profiles, discrete phase laws, higher purity cumulants or a limit distribution. The proof is all-dimensional. The package's `artifacts/verify.py` additionally contains exact Laurent coefficient checks of the centered product for triangles and four-cycles at \(m=2,3\); its purity checks are background and are not evidence of a new cumulant result.
