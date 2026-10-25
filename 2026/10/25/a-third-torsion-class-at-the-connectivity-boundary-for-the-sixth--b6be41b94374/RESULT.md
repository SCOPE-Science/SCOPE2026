# A third-torsion class at the connectivity boundary for the sixth finite subset space of the two-sphere

## Finding

Let \(\operatorname{exp}_6(S^2)\) be the space of nonempty subsets of \(S^2\) of cardinality at most six, with the quotient topology from \((S^2)^6\). Then
\[
H_6(\operatorname{exp}_6(S^2);\mathbb Z)\cong\mathbb Z/3\mathbb Z.
\]

## Assumptions and scope

For a Hausdorff space \(X\), \(\operatorname{exp}_k(X)\) denotes the space of nonempty finite subsets \(\Lambda\subseteq X\) with \(1\leq |\Lambda|\leq k\), topologized as the quotient of \(X^k\) under the map sending a \(k\)-tuple to its underlying set. Homology is singular homology with integer coefficients. The sphere \(S^2\) is given its standard CW structure with one \(0\)-cell and one \(2\)-cell. The claim concerns only the single group \(H_6(\operatorname{exp}_6(S^2);\mathbb Z)\); it does not classify the homotopy type of the full finite subset space.

## Proof

Tuffley's lexicographic cell structure for finite subset spaces of connected finite \(2\)-complexes applies to this CW structure. For each composition \(S=(s_1,\ldots,s_\ell)\) of an integer \(j\geq1\), there is a cell \(\tau^S\) in the based finite subset space when \(j\leq5\), and a cell \(\widetilde{\tau}^{S}\) in the unbased space when \(j\leq6\). Both cells have dimension \(j+\ell\). The unbased cellular chain complex has one \(0\)-cell and these cells in positive dimensions.

Write \(p_a=\sum_{i<a}s_i\). Let \(S\downarrow a\) decrease the even entry \(s_a\) by one, and let \(\mu_a(S)\) merge the adjacent entries \(s_a,s_{a+1}\). The cellular boundary formula in the one-\(2\)-cell case has the following form:
\[
\begin{aligned}
\partial\tau^S
&=\sum_{\substack{1\leq a\leq\ell\\s_a\ {\rm even}}}
(-1)^{p_a+1}\tau^{S\downarrow a}\\
&\quad+\sum_{a=1}^{\ell-1}(-1)^{j+a-1}
\left[\begin{matrix}s_a+s_{a+1}\\s_a\end{matrix}\right]_{-1}
\tau^{\mu_a(S)},\\[4pt]
\partial\widetilde{\tau}^{S}
&=\sum_{\substack{1\leq a\leq\ell\\s_a\ {\rm even}}}
\left(2(-1)^{p_a+1}\tau^{S\downarrow a}
+(-1)^{p_a}\widetilde{\tau}^{S\downarrow a}\right)\\
&\quad+\sum_{a=1}^{\ell-1}(-1)^{j+a-1}
\left[\begin{matrix}s_a+s_{a+1}\\s_a\end{matrix}\right]_{-1}
\widetilde{\tau}^{\mu_a(S)}.
\end{aligned}
\]
Here the signed shuffle number \(\left[\begin{smallmatrix}n\\r\end{smallmatrix}\right]_{-1}\) equals \(0\) if \(n\) is even and \(r\) is odd; it equals \(\binom{n/2}{r/2}\) if both \(n,r\) are even; and it equals \(\binom{\lfloor n/2\rfloor}{\lfloor r/2\rfloor}\) if \(n\) is odd. The attaching map of the \(2\)-cell of \(S^2\) is constant, so there are no additional graph-edge terms.

In dimensions \(5,6,7\), the cellular groups have ranks \(6,10,15\), respectively. Using the ordered bases recorded in `artifacts/cellular_certificate.json`, let \(D_6:C_6\to C_5\) and \(D_7:C_7\to C_6\) be the resulting integer boundary matrices. The certificate gives unimodular matrices \(U_6,V_6\) with
\[
U_6D_6V_6=\operatorname{diag}(1,1,0,0,0,0),
\]
so \(\ker D_6\) has rank \(8\). In the integral kernel basis given by the last eight columns of \(V_6\), the image of \(D_7\) is represented by the last eight rows \(B\) of \(V_6^{-1}D_7\); its first two rows are zero. The certificate supplies unimodular matrices \(U_B,V_B\) with
\[
U_BBV_B=\operatorname{diag}(1,1,1,1,1,1,1,3).
\]
Therefore
\[
H_6(\operatorname{exp}_6(S^2);\mathbb Z)
=\ker D_6/\operatorname{im}D_7
\cong\mathbb Z^8/\operatorname{im}B
\cong\mathbb Z/3\mathbb Z.
\]
The exact integer matrices and all transformation matrices are included in the certificate. The dependency-free script `artifacts/verify_cellular_certificate.py` reconstructs the boundary matrices from the stated formula and checks the chain identity, the unimodular transformations, the Smith diagonals, and modular-rank cross-checks.

## Verification

The computation uses integer arithmetic only. The verifier confirms \(D_6D_7=0\), \(\operatorname{rank}D_6=2\), and that the image lattice in the rank-eight kernel has index \(3\). As a consistency check, the same boundary construction reproduces the published top integral homology groups \(H_{2k}(\operatorname{exp}_k(S^2);\mathbb Z)\cong\mathbb Z\) and \(H_{2k-2}(\operatorname{exp}_k(S^2);\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/(k-1)\mathbb Z\) for \(k=3,4,5,6\). Tuffley's connectivity result also implies that \(\operatorname{exp}_6(S^2)\) is \(5\)-connected, so degree six is the first possible nonzero integral homology degree. No independent audit is claimed.

## Relationship to prior work

Tuffley's paper provides the cell structure and boundary method used here, computes the unbased integral homology through \(k=5\), and gives general top-degree integral homology for every \(k\). The group computed here is in degree \(6\) for the first unbased case beyond that full integral computation. Mostovoy's 2026 paper states that it determines complete rational homology of finite subset spaces of spheres and integral homology in the top \(d\) degrees, with a partial description in codimension \(d\); its abstract does not state this lower integral group. The full text of that paper could not be obtained in this run, so this comparison is limited to the accessible abstract and the possibility of further coverage remains a stated risk.

## Limitations

Only \(H_6(\operatorname{exp}_6(S^2);\mathbb Z)\) is asserted. The result does not determine all lower integral homology groups for \(\operatorname{exp}_6(S^2)\), nor does it give a homotopy classification. The cellular boundary convention is the one in Tuffley's lexicographic cell structure. The later sphere paper's full text was inaccessible; its abstract was read, and the possible relevance of details outside that abstract remains a residual literature risk.

## References

1. C. Tuffley, “Finite subset spaces of closed surfaces,” arXiv:math/0311371 (first public version 2003-11-21), especially §§1.2 and 2.2–2.3 and Theorems 1, 2, 6, and 7.
2. J. Mostovoy, “Finite subset spaces of spheres,” arXiv:2603.01439 (first public version 2026-03-02). Abstract consulted; full text not obtained.
