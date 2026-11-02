# Parity-sharp exact-degree harmonic sampling on the 600-cell

## Finding
Let \(X\subset S^3\) be the 120 unit vertices of the regular 600-cell, identified with the binary icosahedral group \(\Gamma\subset SU(2)\). For each integer \(\ell\ge0\), let \(\mathcal H_\ell(S^3)\) be the complex spherical harmonics of **exact** degree \(\ell\), and define the evaluation map \(E_\ell:\mathcal H_\ell(S^3)\to\mathbb C^X\). Define the real symmetric kernel matrix
\[
K_\ell(x,y)=U_\ell(\langle x,y\rangle),\qquad x,y\in X,
\]
where \(U_0(t)=1\), \(U_1(t)=2t\), and \(U_{\ell+1}(t)=2tU_\ell(t)-U_{\ell-1}(t)\). The matrix \(K_\ell\) is a positive multiple of \(E_\ell E_\ell^*\).

Here is an **all-degree exact spectrum**. Put
\[
(d_0,\ldots,d_8)=(1,2,3,4,5,6,4,2,3),
\]
and let \(A\) be the adjacency matrix of the nine-vertex tree with edges
\[
(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8).
\]
Define integer vectors \(m_0=(1,0,\ldots,0)\), \(m_1=(0,1,0,\ldots,0)\), and
\[
m_{\ell+1}=A m_\ell-m_{\ell-1}\qquad(\ell\ge1).
\]
Then, **for every integer \(\ell\ge0\)**, the full 120-dimensional eigenvalue multiset of \(K_\ell\) consists of
\[
\boxed{\frac{120m_{\ell,i}}{d_i}\ \text{with multiplicity}\ d_i^2,\quad i=0,\ldots,8.}
\]
Coincident entries, including zero, have their multiplicities added. Consequently
\[
\boxed{\operatorname{rank}(E_\ell)=\sum_{i:m_{\ell,i}>0}d_i^2\le60.}
\]
The upper bound is forced by antipodal parity: every exact-degree harmonic satisfies \(h(-x)=(-1)^\ell h(x)\), and \(X\) has 60 antipodal pairs.

**An exact 60-degree spectral translation law** holds on the entire vertex set. Let \(J\) denote the antipodal permutation matrix, so \(J_{x,y}=1\) precisely when \(y=-x\). For every \(\ell\ge0\),
\[
\boxed{K_{\ell+60}=K_\ell+60\bigl(I+(-1)^\ell J\bigr).}
\]
Thus every eigenvalue on the correct antipodal parity space increases by **exactly 120** when the harmonic degree increases by 60. For each fixed residue class modulo 60, the positive-parity-restricted condition number of the Gram operator tends to one (in fact its squared-singular-value condition number is \(1+O(\ell^{-1})\)), so the restrictions become asymptotically tight after rescaling.

**Exact tightness is completely classified.** The operator \(K_\ell\) is a positive scalar multiple of the orthogonal projection onto its full 60-dimensional antipodal parity subspace **if and only if** \(\ell\equiv29\pmod{30}\). More precisely, for every integer \(k\ge1\),
\[
\boxed{K_{30k-1}=30k(I-J).}
\]
Consequently exact-degree sampling is perfectly tight at all and only these degrees, with nonzero Gram eigenvalue \(60k\) of multiplicity \(60\). No even degree is perfectly tight, although both parities become asymptotically tight at high degree.

**The sharp eventual interpolation thresholds** are different for the two parities. Every odd degree \(\ell\ge29\) maps onto the entire 60-dimensional odd antipodal data space, and every even degree \(\ell\ge60\) maps onto the entire 60-dimensional even antipodal data space. These are the smallest eventual bounds in the respective parity classes: degree \(27\) has rank \(56\), while degree \(58\) has rank \(59\). Earlier individual degrees may already reach rank \(60\); hence this is an eventual, not an initial-segment, classification. For instance degree \(13\) has rank \(60\) but degree \(15\) does not.

## Assumptions and scope
The ambient sphere is \(S^3\subset\mathbb R^4\), with the standard round metric and ordinary Euclidean inner product. The 600-cell is scaled to unit radius. Every one of its 120 distinct vertices is sampled once, with **unit (not probability) counting weight** in \(K_\ell\). All harmonic spaces and sampling ranks are over \(\mathbb C\), although the same ranks hold over \(\mathbb R\). The exact degree \(\ell\) is any nonnegative integer; no band-limited cumulative harmonic space or numerical truncation is substituted.

The standard degree-\(\ell\) spherical reproducing kernel with probability-normalized surface measure is \((\ell+1)U_\ell(\langle x,y\rangle)\). Thus the displayed matrix is the reproducing Gram matrix divided by \(\ell+1\); its eigenvalues are not those of a differently normalized frame without applying that factor.

## Proof
**1. Character identity and evaluation rank.** Identify the unit quaternions with \(SU(2)\). For \(x,y\in\Gamma\), \(\langle x,y\rangle=\frac12\operatorname{tr}(xy^{-1})\). If \(V_\ell=\operatorname{Sym}^{\ell}(\mathbb C^2)\), the standard \(SU(2)\) character formula is
\[
\chi_\ell(g)=U_\ell\bigl(\tfrac12\operatorname{tr}g\bigr).
\]
Therefore \(K_\ell(x,y)=\chi_\ell(xy^{-1})\). The degree-\(\ell\) spherical harmonic space on \(S^3\cong SU(2)\) is the \((\ell+1)^2\)-dimensional matrix-coefficient space \(V_\ell\otimes V_\ell^*\); consequently its restriction to \(\Gamma\) has Gram kernel proportional to this character matrix. In particular its evaluation rank equals \(\operatorname{rank}K_\ell\).

**2. Exact diagonalization.** Let \(W_0,\ldots,W_8\) be the nine inequivalent irreducible representations of \(\Gamma\), labelled by the affine \(E_8\) McKay graph in the stated order. Their dimensions are exactly the displayed \(d_i\), with \(\sum_i d_i^2=120\). Write
\[
V_\ell\big|_\Gamma\cong\bigoplus_{i=0}^8m_{\ell,i}W_i.
\]
Because \(K_\ell\) is central convolution by the character \(\chi_\ell\) in the regular representation, orthogonality of irreducible characters makes it a scalar operator on the \(W_i\)-isotypic summand. That scalar is
\[
\frac1{d_i}\sum_{g\in\Gamma}\chi_\ell(g)\overline{\chi_i(g)}
=\frac{|\Gamma|m_{\ell,i}}{d_i}
=\frac{120m_{\ell,i}}{d_i},
\]
and the summand dimension is \(d_i^2\). Thus the entire asserted spectrum and rank follow, including all multiplicities and the zero sector.

**3. Multiplicities from the McKay tree.** The natural two-dimensional \(SU(2)\) representation restricts to the node \(W_1\), and its tensor-product adjacency on irreducible \(\Gamma\)-representations is exactly \(A\). Clebsch–Gordan gives
\[
\mathbb C^2\otimes\operatorname{Sym}^{\ell}(\mathbb C^2)
\cong \operatorname{Sym}^{\ell+1}(\mathbb C^2)
\oplus\operatorname{Sym}^{\ell-1}(\mathbb C^2),\quad\ell\ge1.
\]
Restricting to \(\Gamma\) yields \(A m_\ell=m_{\ell+1}+m_{\ell-1}\), with the displayed initial values. This proves the recurrence for every degree; the integers are nonnegative because they are multiplicities. The check \(\sum_i d_i m_{\ell,i}=\ell+1\) also verifies the representation dimension in every degree.

**4. The exact shift law.** Every element of the binary icosahedral group has order dividing 60; for noncentral \(g\in\Gamma\), its eigenvalues are \(e^{\pm i\theta}\) with \(\sin\theta\ne0\) and \(e^{60i\theta}=1\). Hence the \(SU(2)\) character formula \(\chi_\ell(g)=\sin((\ell+1)\theta)/\sin\theta\) gives \(\chi_{\ell+60}(g)=\chi_\ell(g)\) for \(g\ne\pm I\). At the two central elements, \(\chi_\ell(I)=\ell+1\) and \(\chi_\ell(-I)=(-1)^\ell(\ell+1)\), so the respective differences are \(60\) and \(60(-1)^\ell\). Since \(xy^{-1}=I\) exactly when \(x=y\), and \(xy^{-1}=-I\) exactly when \(x=-y\), this proves the matrix identity. On the \((-1)^\ell\)-antipodal subspace, \(J=(-1)^\ell I\), so the increment is \(120I\); the opposite parity continues to have eigenvalue zero. Iterating gives the asymptotic tightness and the \(1+O(\ell^{-1})\) Gram condition-number law.

**5. Complete classification of exactly tight degrees.** If \(s=\ell+1\) is divisible by 30, then \(\ell\) is odd, and the group element-order list \(1,2,3,4,5,6,10\) implies \(\sin(s\theta)=0\) for every noncentral group eigenangle \(\theta\). Therefore \(\chi_\ell(g)=0\) for all \(g\notin\{\pm I\}\). The two central values are \(\pm s\), giving \(K_\ell=s(I-J)\); its nonzero eigenvalues are all \(2s\). Conversely, if \(K_\ell\) is proportional to the entire appropriate 60-dimensional parity projection, its matrix entries at pairs with \(x\ne\pm y\) must vanish, so \(\chi_\ell(g)=0\) for every noncentral group element. The binary icosahedral group has elements of orders \(4\), \(6\) and \(10\), with primitive eigenangles of respective denominator \(4\), \(6\) and \(10\). Vanishing of \(\sin(s\theta)\) at these three conjugacy types forces \(2\mid s\), \(3\mid s\), and \(5\mid s\). Hence \(30\mid s\), proving necessity as well as sufficiency. In particular no even \(\ell\) is exactly tight.

**6. Why finite exact certificates imply sharp infinite thresholds.** The recurrence gives
\[
m_{12}=(1,0,1,0,1,0,1,0,0).
\]
Hence there exists a nonzero \(\Gamma\)-invariant homogeneous binary form \(F\) of degree 12. Multiplication by \(F\) is an injective, \(\Gamma\)-equivariant map on polynomial representations:
\[
\operatorname{Sym}^{\ell}(\mathbb C^2)^*\hookrightarrow
\operatorname{Sym}^{\ell+12}(\mathbb C^2)^*.
\]
The polynomial ring is an integral domain, so this map really is injective for every \(\ell\). Thus, coordinatewise, \(m_{\ell+12,i}\ge m_{\ell,i}\) for all \(\ell,i\). The sign of central \(-I\) is \((-1)^\ell\); all five even-parity representation nodes are \(i=0,2,4,6,8\), while all four odd-parity nodes are \(i=1,3,5,7\), each side contributing \(60\) to \(\sum d_i^2\).

The following finite list is an **exact recurrence certificate**, not a numerical eigenvalue experiment. Each row is \((m_{\ell,0},\ldots,m_{\ell,8})\), and can be checked using only the nine-node adjacency and the stated recurrence:

| \(\ell\) | Exact multiplicity vector |
|---:|---|
| 27 | \((0,0,0,2,0,3,0,1,0)\) |
| 29 | \((0,1,0,2,0,3,0,1,0)\) |
| 31 | \((0,2,0,2,0,3,0,1,0)\) |
| 33 | \((0,1,0,3,0,3,0,1,0)\) |
| 35 | \((0,1,0,2,0,4,0,1,0)\) |
| 37 | \((0,1,0,2,0,4,0,2,0)\) |
| 39 | \((0,1,0,3,0,4,0,1,0)\) |
| 58 | \((0,0,3,0,5,0,4,0,3)\) |
| 60 | \((2,0,3,0,5,0,4,0,3)\) |
| 62 | \((1,0,4,0,5,0,4,0,3)\) |
| 64 | \((1,0,3,0,6,0,4,0,3)\) |
| 66 | \((1,0,3,0,5,0,5,0,4)\) |
| 68 | \((1,0,3,0,6,0,5,0,3)\) |
| 70 | \((1,0,4,0,6,0,4,0,4)\) |

All four odd nodes occur in each of the **six consecutive odd degrees** \(29,31,33,35,37,39\). Every subsequent odd degree belongs to one of these six residue classes modulo 12; multiplication by powers of \(F\) preserves every already-appearing irreducible component. Thus all odd degrees from 29 onward have rank 60. Degree 27 omits node 1 of dimension 2, and its rank is \(60-2^2=56\); hence no lower eventual odd bound is possible. Similarly all five even nodes occur at each of \(60,62,64,66,68,70\), giving all even degrees from 60 onward. Degree 58 omits only node 0, of dimension 1, so its rank is \(59\), proving the even threshold is sharp.

**7. A further check of the nonmonotone phenomenon.** At degree 13 the recurrence yields \((0,1,0,1,0,1,0,1,0)\), hence rank 60. At degree 15 the recurrence omits some odd nodes, giving rank 52. This shows the eventual thresholds cannot be replaced by a monotonicity claim about all degrees.

## Verification
The included `CHECK.py` constructs \(A\) explicitly, calculates exact integer multiplicities through degree 200, checks representation dimensions, 12-step inclusions and the exact 60-step spectral translation, and checks all six residue-class witnesses for each eventual threshold and the exact tightness criterion in degrees up to 200. It also constructs the 120 distinct unit 600-cell vertices directly using the golden ratio, forms the Chebyshev matrices, and diagonalizes directly them numerically for every \(0\le\ell\le14\). The reproduced output was: `PASS 241 assertion groups; ranks at degrees 27,29,58,60: [56, 60, 59, 60]`. The separately computed numerical spectra agree with the rational McKay eigenvalues to absolute error less than \(10^{-8}\). Python 3 with NumPy is required for the numerical section.

The all-degree theorem is proved by character orthogonality, the order-60 character-shift identity, and multiplication by the invariant degree-12 form. Finite numerical tests are not used to establish any infinite assertion. The finite integer recurrence table is an exact, fully specified certificate for the base degrees used in the separate infinite argument.

## Relationship to prior work
The binary icosahedral realization of the 600-cell and the affine \(E_8\) McKay graph are classical, explicitly treated in Dechant (2013); those identifications and character orthogonality are **not claimed as discoveries**. Teh (2010) studies a different Dirac-spectrum problem on the quotient \(S^3/\Gamma\) and is not a degree-by-degree interpolation classification of 120 point samples. Classical symmetrized icosahedral harmonics and 600-cell geometry are also antecedents. The specific result assessed here is the full sampling Gram spectrum together with the **exact 60-degree spectral translation, complete tight-degree classification, sharp last exceptional degrees, and parity-dependent eventual surjectivity cutoffs**, not a new construction of the 600-cell or the McKay correspondence.

## Limitations
The assertion concerns exactly one homogeneous spherical-harmonic degree, not a cumulative band. Surjectivity means surjectivity onto the appropriate 60-dimensional **antipodally compatible** sample-data subspace, never onto all of \(\mathbb C^{120}\). Only the residue-class-wise asymptotic \(1+O(\ell^{-1})\) Gram condition-number estimate is given, not a sharp all-residue conditioning constant, and the report does not classify exceptional rank values for each degree in a closed piecewise formula beyond the complete recurrence. Older articles on icosahedral symmetrized harmonics and character decomposition may contain equivalent formulations; their inaccessible full texts leave a residual historical originality risk. No independent external mathematical validation is claimed.

## References
- K. Teh, *Nonperturbative Spectral Action of Round Coset Spaces of SU(2)*, first posted 2010-10-09, arXiv:1010.1827v1, https://arxiv.org/abs/1010.1827 (different quotient spectral problem; inspected to compare scope).
- P.-P. Dechant, *Platonic solids generate their four-dimensional analogues*, first posted 2013-07-25, arXiv:1307.6768v1, https://arxiv.org/abs/1307.6768 (600-cell spinor realization and explicit affine \(E_8\) McKay diagram, Figure 1).
- N. B. Backhouse and P. Gard, *The representation theory of the icosahedral group*, Journal of Physics A 7 (1974), 2101–2108, https://doi.org/10.1088/0305-4470/7/17/004 (abstract compared, full text unavailable; possible overlap risk).
- N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Mathematical Proceedings of the Cambridge Philosophical Society 54 (1958), 28–38, https://doi.org/10.1017/S0305004100033156 (accessible extract only; conventional three-dimensional icosahedral symmetry harmonics).
- J. Choi and J.-H. Lee, *Binary Icosahedral Group and 600-Cell*, Symmetry 10 (2018), 326, https://doi.org/10.3390/sym10080326 (geometric construction; full-text access not completed).
