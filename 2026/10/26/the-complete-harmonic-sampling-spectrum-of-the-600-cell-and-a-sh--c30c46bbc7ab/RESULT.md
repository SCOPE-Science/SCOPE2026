# The complete harmonic sampling spectrum of the 600-cell and a sharp recovery threshold

## Finding

Let \(X\subset S^3\) be the \(120\) unit-quaternion vertices of the regular \(600\)-cell, and let \(E_\ell:\mathcal H_\ell(S^3)\to\mathbb C^X\) be exact-degree spherical-harmonic evaluation, divided by \(\ell+1\) after choosing an orthonormal harmonic basis for normalized sphere area. Its output Gram matrix \(G_\ell=E_\ell E_\ell^*\) has diagonal entries \(1\). The following recurrence gives its **complete spectrum at every degree**, including zero eigenvalues.

Put \(d=(1,2,3,4,5,6,4,2,3)\) and define a symmetric \(9\)-by-\(9\) adjacency matrix \(A\) with edge set
\[
\{(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8)\}.
\]
Set \(m_0=(1,0,\ldots,0)^t\), \(m_1=Am_0\), and \(m_{\ell+1}=Am_\ell-m_{\ell-1}\) for \(\ell\ge1\). Every coordinate is a nonnegative integer. For each \(j=0,\ldots,8\), the matrix \(G_\ell\) has the eigenvalue
\[
\boxed{\lambda_{\ell,j}=\frac{120m_{\ell,j}}{(\ell+1)d_j}}
\]
with multiplicity exactly \(d_j^2\). In particular,
\[
\operatorname{rank}E_\ell=\sum_{j:m_{\ell,j}>0}d_j^2,
\quad \sum_{j=0}^{8}d_j^2=120.
\]

The image always belongs to the \(60\)-dimensional antipodal parity subspace \(\mathcal P_\ell=\{y:X\to\mathbb C:y(-x)=(-1)^\ell y(x)\}\). The **sharp eventual surjectivity threshold is degree \(59\)**:
\[
\boxed{\operatorname{im}E_\ell=\mathcal P_\ell\quad\text{for all integers }\ell\ge59,}
\]
while at degree \(58\) the image has dimension \(59\), missing exactly the constant parity character. Surjectivity is nonmonotone below that threshold; it first occurs at odd degree \(13\) and even degree \(20\). There is also an infinite family of **exact perfectly conditioned samplers**:
\[
\boxed{G_\ell=I+(-1)^\ell P\quad\Longleftrightarrow\quad30\mid(\ell+1),}
\]
where \(P\) is the permutation matrix of vertex negation. In this family the \(60\) nonzero eigenvalues all equal \(2\), and degree \(29\) is the first such case. Finally, for every integer \(q\ge0\) and \(0\le r<60\),
\[
m_{60q+r,j}=m_{r,j}+q d_j\,\mathbf1_{\{j\equiv r\pmod2\}}.
\]
Consequently the positive Gram eigenvalues tend to \(2\) along every residue class, with an explicit \(O(\ell^{-1})\) deviation.

## Assumptions and scope

Identify \(S^3\) with the unit quaternions \(SU(2)\), and identify the regular \(600\)-cell vertices with its binary icosahedral subgroup \(\Gamma\) of order \(120\). The normalized surface measure on \(S^3\) has total mass \(1\); \(\mathcal H_\ell\) means restrictions of complex harmonic homogeneous polynomials on \(\mathbb R^4\) of **exact** degree \(\ell\), so \(\dim\mathcal H_\ell=(\ell+1)^2\). All eigenvalue multiplicities are complex linear algebra multiplicities, counting zeros. The labels \(j\) are the irreducible representation vertices of the affine \(E_8\) McKay graph, rooted at the trivial representation \(j=0\). Its central parity is \((-1)^j\). No claim concerns arbitrary subconfigurations or unions of harmonic degrees.

## Proof

**1. Harmonic addition and group convolution.** If \(Y_\alpha\) is a basis orthonormal in normalized area and \(E_\ell(x,\alpha)=Y_\alpha(x)/(\ell+1)\), the addition theorem on \(S^3\) gives
\[
G_\ell(g,h)=\frac{U_\ell(\operatorname{Re}(g^{-1}h))}{\ell+1}
=\frac{\chi_\ell(g^{-1}h)}{\ell+1},
\]
where \(U_\ell\) is the Chebyshev polynomial of the second kind and \(\chi_\ell\) is the character of the \((\ell+1)\)-dimensional \(SU(2)\) representation \(V_\ell=\operatorname{Sym}^\ell(\mathbb C^2)\). This is convolution on \(\Gamma\) by a real central class function.

**2. Exact eigenvalues.** Write the restricted representation \(V_\ell|_\Gamma=\bigoplus_j m_{\ell,j}\rho_j\) with \(\dim\rho_j=d_j\). Classical \(SU(2)\) Clebsch--Gordan gives \(V_1\otimes V_\ell\cong V_{\ell+1}\oplus V_{\ell-1}\); its restriction and the affine \(E_8\) tensor-product adjacency yield the displayed recurrence from \(m_0=e_0\) and \(m_1=e_1\). These are multiplicities of genuine representations and therefore nonnegative. Finite-group matrix-coefficient orthogonality says \(\chi_{\rho_j}*f\) acts on the \(j\)-th regular representation block by \(|\Gamma|/d_j\). Thus the displayed Gram eigenvalue is \(120m_{\ell,j}/((\ell+1)d_j)\), repeated \(d_j^2\) times. Sum of block dimensions is \(120\), proving completeness, not merely a rank bound.

**3. The exact sixty-step identity.** For \(g\ne\pm1\) in the binary icosahedral group, write its eigenvalues as \(e^{\pm i\theta}\). The possible angles are contained in
\[
\{\pi/5,2\pi/5,3\pi/5,4\pi/5,\pi/3,2\pi/3,\pi/2\}.
\]
The character formula \(\chi_\ell(g)=\sin((\ell+1)\theta)/\sin\theta\) shows \(\chi_{\ell+60}(g)=\chi_\ell(g)\). Their difference is \(60\) at \(g=1\) and \(60(-1)^\ell\) at \(g=-1\). For an irreducible \(\rho_j\), the central element \(-1\) acts by \((-1)^j\). Taking character inner products therefore yields
\[
 m_{\ell+60,j}-m_{\ell,j}=\frac{60d_j+60(-1)^{\ell+j}d_j}{120}
=d_j\mathbf1_{\{j\equiv\ell\pmod2\}}.
\]
This is an exact group-character identity for every nonnegative \(\ell\), not an extrapolation from finite computations.

**4. Exact eventual threshold.** Parity implies all opposite-parity \(m_{\ell,j}\) vanish. Since the sixty-step identity adds \(d_j>0\) to *each* allowed-parity multiplicity at \(\ell+60\), all allowed blocks occur for every \(\ell\ge60\). The recurrence yields
\[
m_{58}=(0,0,3,0,5,0,4,0,3),\qquad
m_{59}=(0,2,0,4,0,6,0,2,0).
\]
The first has rank \(120-(60+1)=59\), because the forbidden parity has dimension \(60\) and the allowed trivial block contributes one more missing dimension. The latter contains all odd blocks and hence has rank \(60\). This establishes the sharp **eventual** threshold \(59\). Direct iteration through degree \(20\) gives the stated first odd and even full-rank degrees.

**5. Perfect antipodal sampling and converse.** Whenever \(30\mid(\ell+1)\), the character vanishes on every noncentral element, because \(\ell+1\) is a multiple of \(2,3,5\). The only nonzero Gram entries are at \(g^{-1}h=\pm1\), where they equal \(1\) and \((-1)^\ell\), respectively. Hence \(G_\ell=I+(-1)^\ell P\), with \(60\) eigenvalues \(2\) and \(60\) zeros. Conversely, if this matrix identity holds, then \(U_\ell(\cos\theta)=0\) for a noncentral group element with each of the angles \(\pi/2,\pi/3,\pi/5\). Since \(\sin\theta\ne0\), this requires \(2,3,5\mid(\ell+1)\), hence \(30\mid(\ell+1)\). Finally the sixty-step formula and \(60q+r+1\) normalization show \(\lambda_{60q+r,j}=2+O_r((60q+r+1)^{-1})\) in each permitted block.

## Verification

The included standalone `CHECK.py` verifies the affine graph dimensions, integer recurrence, parities, sixty-step identity for a substantial finite range, special ranks, and perfect tightness. Independently, it constructs all \(120\) 600-cell vertices from three coordinate families and compares direct \(120\)-by-\(120\) Gegenbauer/Chebyshev Gram-matrix eigenvalues with the predicted representation-theoretic spectrum for sample degrees up through \(60\). The exact group-character proof above handles all degrees; finite checks are not substituted for an infinite argument. `CHECK_OUTPUT.txt` records a successful run.

## Relationship to prior work

Weeks (2005) explicitly constructs the invariant polynomial Laplace eigenmodes for the Poincaré dodecahedral quotient \(S^3/\Gamma\), which addresses the **trivial isotypic block** of the restriction. In particular, the missing degree-\(58\) invariant is compatible with those known invariant degrees. Dechant (2013) identifies the 600-cell spinors with \(\Gamma\) and discusses its affine \(E_8\) McKay correspondence; the group and graph are prior mathematics. The present claim concerns the **whole evaluation Gram spectrum, all nontrivial blocks, full parity sampling threshold and exact tight-degree classification**, rather than rediscovery of that underlying graph or known invariants. Standard finite-group Schur orthogonality and Peter--Weyl theory supply the bridge. The spherical-code treatment of Boyvalenkov and collaborators concerns designs and energy bounds for 600-cell configurations, not the full exact-degree harmonic sampling spectrum. Older representation tables or finite-group sampling work could conceivably imply the combined result; publication priority requires independent specialist verification.

## Limitations

The Gram matrix has unavoidable antipodal-parity nullity \(60\); "surjective" refers only to the matching \(60\)-dimensional parity subspace, not all \(120\) unrestricted samples. Numerical tests check finite degrees and floating-point eigenvalues, not the entire spectrum. The article derives exact rank and singular-value expressions but does not identify an optimal interpolation constant over every degree or classify proper vertex subsets. The representation-theoretic ingredients are classical and their use alone is not claimed as original. Independent mathematical verification and publication-priority assessment have not been performed.

## References

1. J. R. Weeks, *Exact Polynomial Eigenmodes for Homogeneous Spherical 3-Manifolds*, arXiv:math/0502566, first posted 2005-02-27, especially Section 10.
2. P.-P. Dechant, *Platonic solids generate their four-dimensional analogues*, arXiv:1307.6768, first posted 2013-07-25, especially the spinor and McKay discussion.
3. P. Boyvalenkov et al., *Universal bounds for spherical codes: the Levenshtein framework lifted*, arXiv:1906.03062, especially the 600-cell discussion.
4. OEIS A087866, binary icosahedral symmetric-power constituent counts, https://oeis.org/A087866.
