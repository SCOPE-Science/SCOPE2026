# Sharp fourth moments and Euclidean distance of the five-sign quadratic Walsh chaos

## Finding
Let \(\varepsilon_1,\ldots,\varepsilon_5\) be independent uniform signs. The real ten-dimensional Banach space
\[
X_5=\operatorname{span}_{\mathbb R}\{\varepsilon_i\varepsilon_j:1\le i<j\le5\}\subset L^4(\{-1,1\}^5)
\]
uses the normalized probability measure on the cube. For every real coefficient array \(a=(a_{ij})_{i<j}\), put \(Q_a=\sum_{i<j}a_{ij}\varepsilon_i\varepsilon_j\). Then
\[
\boxed{\max_{a\ne0}\frac{\mathbb E Q_a^4}{(\mathbb E Q_a^2)^2}=\frac{32}{5},\qquad
 d_{\mathrm{BM}}(X_5,\ell_2^{10})=\left(\frac{32}{5}\right)^{1/4}.}
\]
The maximizing arrays are precisely \(a_{ij}=\lambda\sigma_i\sigma_j\) with \(\lambda\in\mathbb R\setminus\{0\}\) and \(\sigma_i\in\{-1,1\}\). Thus the sharp five-sign second-chaos \(L^2\)-to-\(L^4\) constant is \((32/5)^{1/4}\), including its complete real extremizer family.

## Assumptions and scope
All scalar coefficients are real. Expectations refer to the uniform measure on the \(32\) points of \(\{-1,1\}^5\). The ten coefficients are indexed by edges \(e\) of the complete graph \(K_5\); write \(S=\sum_e a_e^2\), \(T=\sum_e a_e^4\), and \(\mathcal C\) for the \(15\) undirected simple four-cycles of \(K_5\). The Banach--Mazur distance is multiplicative: the infimum over linear isomorphisms to Euclidean space of the product of their operator norms and inverse operator norms. No assertion is made for other dimensions, exponents, or complex coefficients.

## Proof
Walsh orthogonality gives \(\mathbb E Q_a^2=S\). A monomial survives in \(\mathbb E Q_a^4\) exactly when each vertex appears an even number of times in its four edges (with multiplicities). The surviving possibilities are one edge four times, two distinct edges twice each, and four distinct edges forming a four-cycle. Counting multinomial coefficients yields the exact identity
\[
\mathbb E Q_a^4=3S^2-2T+24\sum_{C\in\mathcal C}\prod_{e\in C}a_e. \tag{1}
\]
Each unordered pair of distinct edges of \(K_5\) occurs together in exactly two four-cycles. For adjacent edges, a fourth vertex can be chosen in two ways; for disjoint edges, their four vertices give exactly two compatible cycles. Hence every pair occurs twice, and there are \(15\) cycles.

For each cycle choose any ordering \(C=(e_1,e_2,e_3,e_4)\), write \(a=a_{e_1}, b=a_{e_2}, c=a_{e_3}, d=a_{e_4}\), and note the nonnegative sum
\[
(ab-cd)^2+(ac-bd)^2+(ad-bc)^2
=\sum_{\{e,f\}\subset C}a_e^2a_f^2-6\prod_{e\in C}a_e.
\]
Combining this with (1) and the twofold edge-pair incidence gives the exact global sum-of-squares certificate
\[
\begin{aligned}
\frac{32}{5}S^2-\mathbb E Q_a^4
={}&\frac35\sum_{e<f}(a_e^2-a_f^2)^2\\
&+4\sum_{C\in\mathcal C}\big[(ab-cd)^2+(ac-bd)^2+(ad-bc)^2\big]\ge0.
\end{aligned}\tag{2}
\]
The bound is attained when every coefficient is \(1\): with \(Z=\sum_i\varepsilon_i\), then \(Q=(Z^2-5)/2\), which takes value \(10\) at two cube points and values \(2\) and \(-2\) at the remaining thirty points. Consequently \(\mathbb E Q^2=10\), \(\mathbb E Q^4=640\), and the ratio is \(640/100=32/5\).

Equality in (2) forces all ten coefficient magnitudes to be a common positive number. The cycle squares then force the product of the four coefficient signs around every four-cycle to be positive. To classify such signings, fix vertex \(1\) and let \(s_{ij}\) be the signs, with \(\tau_i=s_{1i}\) for \(i\ne1\). For distinct \(i,j,k\ne1\), the positive sign product around \((1,i,j,k,1)\) implies \(s_{ij}\tau_i\tau_j=s_{jk}\tau_j\tau_k\). Connectivity of the line graph on the remaining four vertices forces these expressions to equal a common sign \(c\). Therefore \(s_{ij}=c\rho_i\rho_j\) for all edges by taking \(\rho_1=c\), \(\rho_i=\tau_i\) for \(i\ne1\); absorbing \(c\) into the common real scalar yields precisely \(a_{ij}=\lambda\rho_i\rho_j\). Conversely every such array attains equality by sign changes of the variables.

It remains to justify the **optimal Euclidean position**, not merely the ratio of the two displayed norms. Coordinate-sign changes \(\varepsilon_i\mapsto\pm\varepsilon_i\) act diagonally on the ten coefficient axes by distinct sign characters; permutations of the five base coordinates act transitively on these ten axes. Let \(q\) be any positive-definite quadratic form and suppose \(Aq(a)\le\|Q_a\|_4^2\le Bq(a)\) for all \(a\). Averaging these inequalities over the finite symmetry group preserves \(A,B\) and the \(L^4\) norm. Averaging \(q\) first over sign changes kills off-diagonal entries, since distinct edge characters are inequivalent; further averaging over permutations makes all diagonal entries equal. The averaged form is therefore \(cS\) for some \(c>0\). Thus no Euclidean quadratic form improves the distortion for \(\sqrt S\). On the other hand \(\|Q_a\|_4\ge\|Q_a\|_2=\sqrt S\) by probability-space norm monotonicity, with equality for a single Walsh character, while the first part of the proof gives the sharp upper ratio \((32/5)^{1/4}\). The claimed Banach--Mazur distance follows.

## Verification
The companion standard-library program `verify.py` checks all \(715\) degree-four coefficient multisets in (2) using exact rational arithmetic and direct Walsh parity enumeration. It also checks the \(15\) cycles, the twofold incidence of all \(45\) edge pairs, the \(32\) optimal edge-sign patterns, and the exact moments \(10\) and \(640\) of the uniform array. Execute `python3 verify.py`; the required output begins `VERIFY_OK`. The written sum-of-squares and finite-group averaging proofs, not finite random tests, establish the universal assertions.

## Relationship to prior work
The classical Bonami hypercontractive inequality and its proofs give the general dimension-free estimate \(\|Q\|_4\le3\|Q\|_2\) for a second homogeneous Rademacher chaos; they do not determine the sharp five-sign constant. Kauers--O'Donnell--Tan--Zhou give sum-of-squares methods for hypercontractivity, while Blais--Tan give an entropy proof; neither states the ten-dimensional coefficient optimum or its Euclidean distortion. Ivanisvili--Tkocz study dimension-free moment comparisons for Rademacher chaoses, and Döbler--Krokowski study fourth moments for normal approximation; the fixed five-sign extremal problem is different. The pair-balanced four-cycle incidence of \(K_5\) is what permits the exact finite-dimensional certificate (2).

## Limitations
The result concerns only homogeneous degree-two **real** Walsh polynomials in exactly five signs, with exponent \(4\), and the associated Banach--Mazur distance to \(\ell_2^{10}\). It does not determine sharp constants for other sign counts, degree mixtures, or complex coefficients. The full bibliographic universe cannot be exhaustively ruled out; earlier specialized treatments of small homogeneous Walsh chaoses could contain equivalent statements.

## References
1. M. Kauers, R. O'Donnell, L.-Y. Tan, and Y. Zhou, *Hypercontractive inequalities via SOS, and the Frankl--Rödl graph*, arXiv:1212.5324 (first posted 2012-12-21), especially the introduction and its dimension-free \(L^2\)-to-\(L^4\) theorem. https://arxiv.org/abs/1212.5324
2. E. Blais and L.-Y. Tan, *Hypercontractivity via the entropy method*, Theory of Computing 9 (2013), 889--896, doi:10.4086/toc.2013.v009a029, Theorems 1.1 and 3.1. https://doi.org/10.4086/toc.2013.v009a029
3. P. Ivanisvili and T. Tkocz, *Comparison of moments of Rademacher chaoses*, arXiv:1807.04358, Theorems 1--2. https://arxiv.org/abs/1807.04358
4. C. Döbler and K. Krokowski, *On the fourth moment condition for Rademacher chaos*, arXiv:1706.00751, especially equation (10) and the fourth-moment convergence theorems. https://arxiv.org/abs/1706.00751
