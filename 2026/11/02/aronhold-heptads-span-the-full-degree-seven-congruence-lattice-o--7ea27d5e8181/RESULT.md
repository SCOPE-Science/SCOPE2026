# Aronhold heptads span the full degree-seven congruence lattice of bitangents

## Finding
For a smooth nonhyperelliptic genus-three curve over an algebraically closed field of characteristic different from \(2\), let \(B\) denote its \(28\) geometric bitangents, and \(\mathcal A\) its \(288\) Aronhold heptads. Write \(e_b\) for the standard basis vectors of \(\mathbb Z^B\) and \(h_A=\sum_{b\in A}e_b\). Then
\[
\operatorname{span}_{\mathbb Z}\{h_A:A\in\mathcal A\}=\bigl\{z\in\mathbb Z^B:\sum_{b\in B}z_b\equiv0\pmod 7\bigr\}.
\]
Consequently, the integral incidence matrix has Smith form \(\operatorname{diag}(1^{27},7)\) and cokernel \(\mathbb Z/7\mathbb Z\). All differences \(e_b-e_{b'}\) lie in the heptad span, although none of the individual basis vectors does.

## Assumptions and scope
The curve is smooth, geometrically connected and nonhyperelliptic, of genus \(3\), over an algebraically closed field of characteristic not \(2\). The claim concerns a *formal integral incidence lattice*, not divisor classes, bitangent equations, torsion of a Jacobian or the Neron-Severi group. The classical identification of odd theta characteristics with the bitangents, and of Aronhold heptads with azygetic seven-subsets, is used. The proof depends on no particular model of the curve.

## Proof
Identify the \(64\) theta characteristics with pairs \((a,b)\in\mathbb F_2^3\times\mathbb F_2^3\), using the standard quadratic refinements \(q_{a,b}(x,y)=x\cdot y+a\cdot x+b\cdot y\). The Arf invariant is \(a\cdot b\). Thus the \(28\) odd characteristics are the lexicographically ordered pairs with \(a\cdot b=1\), where each three-bit word is ordered by its ordinary binary integer from \(0\) through \(7\). A triple \(i,j,k\) of odd characteristics is azygetic precisely when \((a_i+a_j+a_k)\cdot(b_i+b_j+b_k)=0\) over \(\mathbb F_2\). Enumerating lexicographically the seven-element subsets of the ordered list of \(28\) odd characteristics for which all \(35\) triples meet this test produces \(288\) distinct heptads. This criterion and the classical total of \(288\) are established in the cited literature.

Every column of the \(28\times288\) incidence matrix \(M\) has exactly seven ones. Therefore its integer column lattice \(L\) lies in \(K=\{z:\sum z_i\equiv0\pmod7}\), which has index \(7\) in \(\mathbb Z^{28}\). The attached standalone integer verifier constructs the entire ordered list and the \(28\times28\) submatrix of columns at zero-based indices

`[85, 76, 79, 86, 4, 172, 107, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 28, 30, 32, 48, 72]`.

Its fraction-free exact determinant calculation gives absolute determinant \(7\). Thus \(\mathbb Z^{28}/L\) is finite of order dividing \(7\). As \(L\subseteq K\) and \(K\) has index \(7\), equality follows. This also forces invariant factors \(1\) repeated \(27\) times and \(7\) once. Finally any difference \(e_i-e_j\) has total coordinate sum zero, hence belongs to \(L\). The converse follows because every heptad sum has coordinate sum seven.

## Verification
Run `python3 verify_aronhold.py` using only the Python standard library. It enumerates all \(28\) odd characteristics and \(288\) heptads, checks the \(2\)-design frequencies (each bitangent in \(72\) heptads and every pair in \(16\)), and recomputes the specified \(28\times28\) determinant exactly using integer Bareiss elimination. The design checks are consistency tests and are not substituted for the determinant certificate. The program was executed from its exact standalone contents with output including `VERIFY_OK`.

## Relationship to prior work
Classical Aronhold theory establishes the seven-sets, the \(288\) count, the symplectic parameterization and their role in recovering plane quartics. Dalla Piazza–Fiorentino–Salvati Manni (2014, especially Section 3) explicitly treat the Aronhold heptads and matrices of bitangents; their results concern geometric reconstruction and determinantal representations, not the presented integer span. Gizatullin (2013) constructs related designs and a partition of the \(288\) heptads; the accessible abstract/excerpts do not establish the integral rank/saturation conclusion, but the full article could not be compared throughout. The new statement is about the complete integral lattice, not the already-known heptad enumeration or design frequencies.

## Limitations
No claim of historical uniqueness is proved. The exact incidence lattice follows from an explicit integer determinant certificate whose construction is reproducible but not replaced by a short conceptual symmetry-only proof. A full historical priority comparison, especially with Gizatullin's block-design article and possible finite-geometry design literature, remains advisable. The statement concerns geometric bitangents only in characteristic unequal to \(2\).

## References
1. F. Dalla Piazza, A. Fiorentino and R. Salvati Manni, *Plane quartics: the matrix of bitangents*, arXiv:1409.5032, first submitted 17 September 2014; especially Section 3, https://arxiv.org/html/1409.5032v2.
2. M. Kh. Gizatullin, *Combinatorics associated with inflections and bitangents of plane quartics*, Izvestiya: Mathematics 77 (2013), 675–695, doi:10.1070/IM2013v077n04ABEH002655.
3. D. Plaumann, B. Sturmfels and C. Vinzant, *Quartic curves and their bitangents*, Journal of Symbolic Computation 46 (2011), 712–733, arXiv:1008.4104.
