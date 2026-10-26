# Euclidean hull census for two NMDS twisted Roth–Lempel families

## Finding

Let \(\mathbb F_{37}\) be the prime field, \(\alpha=\{1,2,\ldots,11\}\), and let \(C_{\ell,\eta,\delta}\) be the length-13, dimension-5 twisted Roth–Lempel code defined below. For the two boundary twist positions \(\ell\in\{3,4\}\) and every nonzero pair \((\eta,\delta)\in(\mathbb F_{37}^{*})^2\), the Euclidean hull dimension is always 0 or 1.

Among the pairs that produce NMDS codes, the exact census is:

| Twist position | All nonzero pairs | Hull dimension 0 among all pairs | Hull dimension 1 among all pairs | NMDS pairs | LCD NMDS pairs | NMDS pairs with hull dimension 1 |
|---|---:|---:|---:|---:|---:|---:|
| \(\ell=3\) | 1296 | 1266 | 30 | 593 | 584 | 9 |
| \(\ell=4\) | 1296 | 1258 | 38 | 970 | 943 | 27 |

Thus, among these NMDS instances, the non-LCD cases are exactly the following parameter pairs \((\eta,\delta)\), with field elements represented by their integer residues modulo 37:

- \(\ell=3\): \((9,9),(9,17),(10,5),(11,19),(17,9),(19,34),(23,8),(23,18),(34,26)\).
- \(\ell=4\): \((2,5),(2,31),(6,18),(6,31),(8,9),(10,28),(10,34),(13,19),(13,25),(17,22),(17,35),(18,6),(18,8),(21,11),(21,22),(24,6),(25,12),(25,34),(26,4),(27,35),(27,36),(29,11),(34,12),(35,4),(35,19),(36,7),(36,10)\).

Every other NMDS pair in the respective family is LCD (has zero-dimensional Euclidean hull). The two examples singled out in the source paper, \((\ell,\eta,\delta)=(4,1,1)\) and \((3,3,1)\), are both LCD under this computation.

## Assumptions and scope

For \(\ell\in\{3,4\}\), define
\[
S_{5,\ell,\eta}=\left\{\sum_{\substack{0\le i\le4\\i\ne\ell}}f_i x^i+f_\ell(x^\ell+\eta x^5): f_i\in\mathbb F_{37}\right\}.
\]
For \(f\in S_{5,\ell,\eta}\), the code is
\[
C_{\ell,\eta,\delta}=\{(f(1),f(2),\ldots,f(11),f_4,f_3+\delta f_4): f\in S_{5,\ell,\eta}\}.
\]
Here \(\eta,\delta\) range independently over all 36 nonzero elements of \(\mathbb F_{37}\). The scope is exactly these two twist positions and this fixed evaluation set; no claim is made for other fields, evaluation sets, or twist positions.

For a linear code \(C\), its Euclidean hull is \(\operatorname{Hull}(C)=C\cap C^\perp\). A code is LCD precisely when this hull has dimension zero. Hull dimension is a useful structural parameter for distinguishing classical codes with the same distance parameters and for selecting inputs to quantum-code constructions.

## Proof

The primary source gives necessary-and-sufficient NMDS criteria for the two boundary cases \(\ell=k-2=3\) and \(\ell=k-1=4\) (Theorems 4.3 and 4.2, respectively). The checker implements those criteria using the elementary symmetric sums
\[
S_1(I)=\sum_{a\in I}a,\qquad S_2(I)=\sum_{a<b,\ a,b\in I}ab,
\]
computed modulo 37 for every 4-subset and 5-subset of \(\alpha\). It then tests all \(36^2=1296\) nonzero scalar pairs for each \(\ell\).

For each pair, let \(G\) be the \(5\times13\) generator matrix whose rows correspond to the basis polynomials \(x^i\), with \(x^\ell\) replaced by \(x^\ell+\eta x^5\), and whose last two entries in row \(i\) are \((0,0)\) for \(i\le2\), \((0,1)\) for \(i=3\), and \((1,\delta)\) for \(i=4\). The evaluation columns are at \(1,\ldots,11\). The rows are independent, so \(G\) has rank 5.

A row combination \(uG\) belongs to \(C^\perp\) exactly when \(uGG^{\mathsf T}=0\). Since the map \(u\mapsto uG\) is injective, rank-nullity gives the exact identity
\[
\dim\operatorname{Hull}(C)=5-\operatorname{rank}_{\mathbb F_{37}}(GG^{\mathsf T}).
\]
The checker computes this rank by Gaussian elimination modulo 37 for every parameter pair, counts the NMDS pairs satisfying the source's criteria, and lists all NMDS pairs for which the Gram rank is 4. It asserts the full count tables and the two source-paper examples, then prints `VERIFY_OK`. The exhaustive domain has exactly 2592 family/parameter cases, with no sampling or floating-point arithmetic.

## Verification

The standalone file `verify_hull_census.py` uses only the Python standard library. It enumerates all 330 four-subsets and 462 five-subsets, evaluates the published NMDS criteria, builds each generator matrix, checks its rank, and computes \(\operatorname{rank}(GG^{\mathsf T})\) exactly in \(\mathbb F_{37}\). It reproduces both count tables and both exceptional-pair lists, and verifies that the two explicit NMDS examples in the source have hull dimension zero. The executed checker returned `VERIFY_OK`.

## Relationship to prior work

Lei, Gu, Zhang, and Zhou, *On Twisted Roth-Lempel Codes* (arXiv:2609.17304v1, first posted 15 September 2026), define this TRL family and give the NMDS criteria used here; Example 4.4 provides one instance at \((\ell,\eta,\delta)=(4,1,1)\) and another at \((3,3,1)\). The source establishes their NMDS parameters but does not report the Euclidean Gram ranks or the full nonzero-parameter census above. NMDS distance conditions alone do not determine the rank of \(GG^{\mathsf T}\), so the hull classification requires an additional exact computation.

Related work on generalized Roth–Lempel codes studies Hermitian self-orthogonality and prescribed Galois hulls. The accessible abstracts of arXiv:2604.11350v2 and arXiv:2609.20453v1 establish that broader hull constructions are relevant, but their full texts were not available during this check. They are therefore retained as explicit overlap risks rather than treated as proof that this precise prime-field TRL census is already covered.

## Limitations

This is a complete finite classification for the stated evaluation set and the two boundary twist positions, not a theorem for arbitrary evaluation sets or fields. The NMDS classification relies on the published necessary-and-sufficient criteria in the primary source; this work does not re-prove those general criteria. The hull ranks and parameter counts are independently recomputed from the displayed generator matrices with exact arithmetic. The broader generalized Roth–Lempel hull literature may contain related constructions, and the inaccessible full text of arXiv:2609.20453v1 leaves a residual overlap risk.

## References

1. H. Lei, H. Gu, J. Zhang, and H. Zhou, “On Twisted Roth-Lempel Codes,” arXiv:2609.17304v1, submitted 15 September 2026. https://arxiv.org/html/2609.17304v1
2. Q. Liu, X. Wu, and H. Zhou, “Generalized Roth-Lempel Codes: NMDS Characterization, Hermitian Self-Orthogonality, and Quantum Constructions,” arXiv:2604.11350v2, 25 April 2026. https://arxiv.org/abs/2604.11350
3. X. Wu, Q. Liu, Y. Chen, and H. Zhou, “Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs,” arXiv:2609.20453v1, submitted 17 September 2026. https://arxiv.org/abs/2609.20453
