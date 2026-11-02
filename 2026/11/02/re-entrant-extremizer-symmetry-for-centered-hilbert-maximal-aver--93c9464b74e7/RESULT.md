# Re-entrant extremizer symmetry for centered Hilbert maximal averages on the first three odd paths

## Finding

Write \(P_n\) for the unit-edge path on vertices \(0,1,\ldots,n-1\). On the counting-measure real Hilbert space \(\ell^2(P_n)\), let
\[
(M_nf)(i)=\max_{0\le r\le \max(i,n-1-i)}\frac{1}{|B(i,r)|}\sum_{j\in B(i,r)}|f(j)|,
\qquad B(i,r)=\{j:|i-j|\le r\}.
\]
For the first three odd path orders \(n\in\{3,5,7\}\), the sharp squared norm \(\|M_n\|_{2\to2}^2=\lambda_n\) and the complete set of nonnegative extremizing rays are as follows.

* For \(n=3\), \(\lambda_3=(7+\sqrt{33})/8\approx1.59307033081725\). The unique nonnegative extremizing ray is proportional to \((u_3,1,u_3)\), with \(u_3=(4\lambda_3-1)^{-1}\). This three-vertex star case is previously known and is included as a baseline, not as a new constant.
* For \(n=5\), \(\lambda_5\approx1.64638067412275\) is the unique root in \((1.6463806,1.6463808)\) of
\[
288z^4-672z^3+359z^2-56z+2=0.
\]
Its nonnegative extremizers form precisely two labeled rays, proportional to \((u_5,1,v_5,v_5,w_5)\) and its reversal.
* For \(n=7\), \(\lambda_7\approx1.69371599507013\) is the unique root in \((1.6937159,1.6937161)\) of
\[
72z^3-149z^2+47z-2=0.
\]
Its nonnegative extremizers form precisely one labeled ray, proportional to \((w_7,v_7,v_7,1,v_7,v_7,w_7)\).

For \(n\in\{5,7\}\), these ratios have the *exact* common algebraic parametrization
\[
 u_n=\frac{1}{4\lambda_n-1},\qquad
 v_n=\frac{17\lambda_n-1}{72\lambda_n^2-43\lambda_n+2},\qquad
 w_n=\frac{9\lambda_n}{72\lambda_n^2-43\lambda_n+2}.
\]
In particular, among these successive odd paths, the location of every extremizer's largest absolute coordinate moves from the central vertex (three vertices) to one of the two vertices adjacent to an endpoint (five vertices), then returns to the central vertex (seven vertices). For arbitrary real inputs, *all* extremizers arise by independently choosing coordinate signs and multiplying one of the displayed absolute-value patterns by a nonzero scalar. The corresponding exact sharp norms are \(\sqrt{\lambda_n}\), numerically \(1.26216889948107\), \(1.28311366375811\), and \(1.30142844408371\).

## Assumptions and scope

The vertex masses are all one, the graph balls are closed and centered in the shortest-path metric, the input and output norm is the counting-measure \(\ell^2\) norm, and all functions are real. Radius zero (a singleton) is included. The result is an exact classification only for \(n\in\{3,5,7\}\), not a claim for every odd path. The three-vertex assertion is context; the five- and seven-vertex formulas and symmetry change are the claimed additional findings.

## Proof

**Finite selection reduction.** For each vertex \(i\), form the averaging row \(a_{i,r}\) whose entries are \(1/|B(i,r)|\) on its radius-\(r\) ball and zero elsewhere. A *selection* \(\rho=(r_0,\ldots,r_{n-1})\) chooses one legal radius at each vertex; let \(A_\rho\) have rows \(a_{i,r_i}\). For every nonnegative input vector \(x\),
\[
 \|M_nx\|_2^2=\max_\rho\|A_\rho x\|_2^2.
\]
Because every \(A_\rho^{\mathsf T}A_\rho\) is symmetric and entrywise nonnegative, a top eigenvector may be chosen nonnegative. Hence, *without exchanging any noncommuting operations*,
\[
 \|M_n\|_{2\to2}^2=\max_\rho\lambda_{\max}(A_\rho^{\mathsf T}A_\rho).
\]
This also proves attainment. The numbers of selections are \(18\), \(1200\), and \(176400\) for the three path orders.

**Exact exhaustive separation.** The embedded standard-library verifier enumerates every selection, multiplies its rows by \(D_n=\mathrm{lcm}(1,\ldots,n)\), and tests positive definiteness of
\[
 p_n D_n^2 I-q_n D_n^2 A_\rho^{\mathsf T}A_\rho,
 \qquad T_n=p_n/q_n,
\]
using integer fraction-free symmetric Sylvester elimination with divisibility assertions. The exact thresholds are \(T_3=199/125\), \(T_5=823/500\), and \(T_7=3387/2000\). Exactly one, two, and one selections, respectively, *fail* the strict below-threshold test. In zero-indexed vertex order their radius tuples are
\[
\begin{array}{c|l}
 n&\text{exceptional radius tuples}\\\hline
 3&(1,0,1)\\
 5&(1,0,1,2,3),\ (3,2,1,0,1)\\
 7&(3,2,1,0,1,2,3).
\end{array}
\]
Thus every nonexceptional selection has squared norm *strictly smaller* than \(T_n\). The two five-vertex exceptions are path reversals, so they have the same singular values.

**Exceptional spectra and root identification.** For the representative exceptional matrices, exact characteristic-polynomial identities are
\[
\begin{aligned}
\det(zI-A_3^{\mathsf T}A_3)&=\frac{(4z-1)(4z^2-7z+1)}{16},\\
\det(zI-A_5^{\mathsf T}A_5)&=\frac{z(288z^4-672z^3+359z^2-56z+2)}{288},\\
\det(zI-A_7^{\mathsf T}A_7)&=\frac{z^2(72z^2-43z+2)(72z^3-149z^2+47z-2)}{5184}.
\end{aligned}
\]
The rational test vectors (normalized to have their peak equal to one) are, respectively,
\[
 (186/1000,1,186/1000),\qquad
 (179/1000,1,214/1000,214/1000,117/1000),
\]
\[
 (1123/10000,2048/10000,2048/10000,1,2048/10000,2048/10000,1123/10000).
\]
Their exact squared Rayleigh quotients are, in the same order, \(851649/534596\), \(14979715/9098576\), and \(7274139377/4294781064\), each strictly greater than its \(T_n\). The traces of the three Gram matrices are exactly \(2\), \(7/3\), and \(8/3\), all less than \(2T_n\). Since Gram eigenvalues are nonnegative, at most one eigenvalue can exceed \(T_n\), and the exhibited Rayleigh quotients show that exactly one does. Exact rational sign changes of the displayed polynomial factors across the claimed root brackets locate this unique top eigenvalue.

**Extremizer formulas.** Substituting the displayed coordinates into \(A_n^{\mathsf T}A_nx=\lambda_nx\), all but one coordinate equation hold identically as rational functions of a formal variable \(z\). For \(n=3\), the remaining central residual equals \(-(4z^2-7z+1)/(4z-1)\). For \(n=5\), it equals \(-(288z^4-672z^3+359z^2-56z+2)/[(4z-1)(72z^2-43z+2)]\). For \(n=7\), it equals \(-(72z^3-149z^2+47z-2)/(72z^2-43z+2)\). Therefore these are exact positive eigenvectors at the specified roots.

The selected Gram matrices are entrywise nonnegative and irreducible: their positive-entry support graphs connect all coordinates via the distinguished input vertex. Perron--Frobenius therefore makes their positive top eigenvectors unique up to positive scaling. Direct interval bounds on \(u_n,v_n,w_n\), using only the rational root brackets, certify that each chosen radius average at each vertex is strictly larger than every alternative; the exact verifier tests \(5\), \(16\), and \(33\) such inequalities, with verified lower margins exceeding \(0.135\), \(0.041\), and \(0.035\). The exhaustive threshold separation excludes every other selection; hence no other nonnegative extremizing rays exist. Taking absolute values commutes with the definition of \(M_n\), so independent input signs give all real equality cases.

## Verification

Run `python3 verify_path_maximal.py` using Python 3 and its standard library. It constructs *all* ball choices, performs exact integer Sylvester tests, compares exact characteristic-polynomial identities at enough integer points to determine each monic polynomial, checks rational Rayleigh witnesses and trace bounds, isolates the distinguished roots by rational signs, and verifies every competing ball average using rational interval enclosures. The observed output was:

```text
CERTIFICATE_OK P3 selections=18 exceptional=1 charpoly=exact root_isolated=exact Rayleigh_above_threshold=exact active=5 min_active_gap_gt=0.1356432
CERTIFICATE_OK P5 selections=1200 exceptional=2 charpoly=exact root_isolated=exact Rayleigh_above_threshold=exact active=16 min_active_gap_gt=0.0414132
CERTIFICATE_OK P7 selections=176400 exceptional=1 charpoly=exact root_isolated=exact Rayleigh_above_threshold=exact active=33 min_active_gap_gt=0.0351368
ALL_EXACT_CERTIFICATES_OK
```

The finite enumeration is exhaustive **because these are finite path orders with explicitly enumerated complete lists of legal radii**, not because a numerical experiment was extrapolated. The verifier uses exact integers and fractions in every mathematical check. The analytical selection reduction, Perron uniqueness, and equality logic above are necessary parts of the proof; a log by itself is not such a proof.

## Relationship to prior work

Soria and Tradacete (2014), particularly Proposition 4.13 and surrounding results, address graph maximal-operator bounds and the asymptotic weak \(\ell^1\) behavior of linear paths, not the sharp strong \(\ell^2\) constants or equality cases here. González-Riquelme and Madrid (2020) compute strong \(\ell^2\) norms for complete graphs and stars, covering the three-vertex baseline but not the nonstar paths \(P_5\) and \(P_7\). González-Riquelme, Kovač and Madrid (2026) formulate a path problem for **edge-variation** sharp constants; it is a different functional from the strong \(\ell^2\) norm here. Existing exact results for graph maximal variation and other finite graph families likewise do not entail the two displayed nonstar path spectra. These comparisons do not establish absolute priority over unindexed calculations.

## Limitations

The classification is proved only for the three odd orders stated; no formula, extremizer trend, or eventual symmetry law for larger odd paths follows. It does not treat weighted vertices, uncentered maximal averages, other exponents, or extremizing stability. The exact certificates depend on finite enumeration, and independently validating the mathematical arguments remains open.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy--Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (first public October 22, 2014), https://arxiv.org/abs/1410.6204 .
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1 (May 6, 2020), https://arxiv.org/abs/2005.03146 .
3. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy--Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (March 12, 2026), https://arxiv.org/abs/2603.12462 .
