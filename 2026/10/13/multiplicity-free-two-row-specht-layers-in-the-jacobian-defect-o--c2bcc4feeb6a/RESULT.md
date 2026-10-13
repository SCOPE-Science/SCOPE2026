# Multiplicity-free two-row Specht layers in the Jacobian defect of symmetric cubics

## Finding
Fix an integer \(m\geq4\). Let \(S=\mathbb C[x_1,\ldots,x_m]\), let \(f=e_3(x_1,\ldots,x_m)\) be the third elementary symmetric polynomial, and let \(J=(\partial f/\partial x_1,\ldots,\partial f/\partial x_m)\). Write \(I=J:(x_1,\ldots,x_m)^\infty\) and \(N=I/J\). The symmetric group \(\mathfrak S_m\) acts by permuting the variables, preserving all these objects. For a partition \(\lambda\vdash m\), let \(S^\lambda\) denote its irreducible complex Specht representation.

**Equivariant saturation-defect theorem.** In every homogeneous degree \(d\), the complete irreducible decomposition of the defect is
\[
N_d\cong\begin{cases}
\displaystyle\bigoplus_{j=2}^{\min(d,m-d)}S^{(m-j,j)},&2\leq d\leq m-2,\\
0,&\text{otherwise}.
\end{cases}
\]
Each displayed constituent occurs exactly once. Thus no trivial or standard representation occurs in the saturation defect, and the degrees and representations of every nonzero layer are specified uniformly in \(m\).

In particular, \(I=(x_ix_j:1\leq i<j\leq m)\). Taking dimensions yields
\[
\dim_\mathbb C N_d=\binom md-m\quad(2\leq d\leq m-2),\qquad
\operatorname{length}_\mathbb C N=2^m-m^2+m-2.
\]
The supporting Hilbert function of the graded Milnor algebra \(M=S/J\) is
\[
\dim_\mathbb C M_d=\begin{cases}\binom md,&0\leq d\leq m-1,\\m,&d\geq m.\end{cases}
\]
The numerical Hilbert function, especially the four-variable Cayley-cubic case, is not presented as an independent originality claim: prior general nodal-hypersurface results already imply a substantial part of it. The new assertion assessed here is the **uniform equivariant decomposition of the saturation-defect layers**.

## Assumptions and scope
All rings, group representations, points, and schemes are over \(\mathbb C\), and every grading is the ordinary total degree. The assertion applies to each integer \(m\geq4\) with no genericity assumption. Saturation is with respect to the full homogeneous irrelevant ideal; \(N\) is an honest graded finite-length module, not the coordinate ring of the projective singular subscheme. The Specht notation refers to the ordinary characteristic-zero irreducible representations and partitions with two rows. Isomorphisms of representations are asserted degree by degree; no canonical choice of splitting is implied.

## Proof
**1. Quadratic Jacobian presentation.** Put \(s=\sum_i x_i\) and \(e_2=\sum_{i<j}x_ix_j\). The derivatives satisfy
\[
\frac{\partial f}{\partial x_i}=e_2-sx_i+x_i^2,
\qquad \sum_i\frac{\partial f}{\partial x_i}=(m-2)e_2.
\]
Therefore \(J=(x_i^2-sx_i:1\leq i\leq m)\), since \(m-2\ne0\) and \(\sum_i(x_i^2-sx_i)=-2e_2\). These identities are equivariant under variable permutations.

**2. Reduction to Boolean functions and the full graded representation.** Introduce an independent homogeneous variable \(s\), set
\[
B=\mathbb C[s,x_1,\ldots,x_m]/(x_i^2-sx_i:1\leq i\leq m),
\qquad L=\sum_i x_i-s.
\]
Then \(M\cong B/LB\). Since the defining polynomials are monic in the respective variables, \(B\) is free over \(\mathbb C[s]\) with basis the \(2^m\) squarefree monomials \(x_A=\prod_{i\in A}x_i\). Consequently \(B_d\) is, as a \(\mathfrak S_m\)-representation, the direct sum \(\bigoplus_{r=0}^{\min(d,m)}V_r\), where \(V_r\) is the permutation representation on \(r\)-subsets of \(\{1,\ldots,m\}\).

Specializing \(s=1\) identifies \(B_d\) (as a vector space, compatibly with permutations) with the multilinear polynomial functions of degree at most \(d\) on the Boolean cube \(\{0,1\}^m\). Multiplication by \(L\) is multiplication by \(\sum_i z_i-1\), whose value at a Boolean vector of support \(A\) is \(|A|-1\). Its kernel therefore consists of functions supported on the singleton vertices, subject to the degree bound. Any such function, with singleton values \(c_i\), has the unique multilinear expansion
\[
P(z)=\sum_{i=1}^m c_i z_i\prod_{j\ne i}(1-z_j).
\]
For \(d\leq m-2\), cancellation of the degree-\(m\) coefficient gives \(\sum_i c_i=0\), and cancellation of every degree-\((m-1)\) coefficient gives \(\sum_i c_i-c_j=0\) for each \(j\); hence all \(c_i=0\). For \(d=m-1\), only \(\sum_i c_i=0\) is needed. For \(d\geq m\), there is no constraint. Thus the kernel \(K_d=\ker(L:B_d\to B_{d+1})\) is zero for \(d\leq m-2\), the standard \((m-1)\)-dimensional representation for \(d=m-1\), and the full singleton-permutation representation \(V_1\) for \(d\geq m\).

The exact sequence \(B_{d-1}\xrightarrow{L}B_d\to M_d\to0\) is equivariant. For \(0\leq d\leq m-1\), its first arrow is injective. Semisimplicity over \(\mathbb C\) therefore gives
\[
M_d\cong B_d\ominus B_{d-1}\cong V_d
\qquad(0\leq d\leq m-1),
\]
where the difference is in the representation ring and the final equality is realized by an actual representation isomorphism. In degree \(m\), the kernel contributes the standard representation and \(B_m\ominus B_{m-1}=V_m\), the trivial representation; hence \(M_m\cong V_1\). In all greater degrees, \(B_d=B_{d-1}\) as graded representations and the kernel is \(V_1\), giving \(M_d\cong V_1\). The Hilbert function in the finding follows.

**3. Exact saturated ideal.** On the projective chart \(x_i\ne0\), scale \(x_i=1\). The equation \(x_i^2-sx_i=0\) forces \(s=1\), and every remaining equation reads \(x_j^2-x_j=0\). Together with \(s=1+\sum_{j\ne i}x_j\), this gives \(\sum_{j\ne i}x_j=0\). The algebra defined by the idempotent equations is reduced and decomposes into Boolean points; in characteristic zero the sum condition retains only the all-zero Boolean point. Thus the projective gradient scheme consists scheme-theoretically of the \(m\) reduced coordinate points. Its homogeneous saturated ideal is \(I=(x_ix_j:i<j)\), and \((S/I)_d\cong V_1\) for \(d\geq1\).

**4. Specht decomposition.** The exact equivariant sequence
\[
0\longrightarrow N_d\longrightarrow M_d\longrightarrow (S/I)_d\longrightarrow0
\]
shows, for \(2\leq d\leq m-2\), that \([N_d]=[V_d]-[V_1]\) in the Grothendieck ring of \(\mathfrak S_m\)-representations. Young's rule for the two-row subset-permutation representations states
\[
V_d\cong\bigoplus_{j=0}^{\min(d,m-d)}S^{(m-j,j)}.
\]
Since \(V_1=S^{(m)}\oplus S^{(m-1,1)}\), subtracting gives precisely the displayed direct sum for \(N_d\). For \(d\leq1\), \(M_d\to(S/I)_d\) is an isomorphism, while for \(d\geq m-1\) both spaces are \(m\)-dimensional and the map is surjective, so \(N_d=0\). Taking dimensions and summing over \(d\) yields the numerical formulas.

## Verification
The included standalone `checker.py` performs independent exact modular linear algebra over the prime field of size \(1000003\): it verifies the Boolean multiplication kernels for \(3\leq m\leq8\), calculates graded Jacobian quotient dimensions directly for \(3\leq m\leq5\), and checks the resulting total defect lengths for \(3\leq m\leq8\). It also checks the predicted character identity on every conjugacy-cycle type in degrees of interest for \(4\leq m\leq9\). Its expected output is included as `checker_output.txt`; reproduce with `python3 checker.py`. An exact character identity for the subset-permutation modules, \(\chi_{V_d}-\chi_{V_1}=\sum_{j=2}^{\min(d,m-d)}\chi_{S^{(m-j,j)}}\), also follows from the displayed Young-rule formula, with no numerical fitting. All sizes are proved by the symbolic argument above; finite checks do not certify untested sizes or novelty.

## Relationship to prior work
Dimca and Sticlaru, *Koszul complexes and pole order filtrations* (arXiv:1108.3976, publicly available in 2011), study the Milnor algebra, Jacobian syzygies, and defects of nodal hypersurfaces. Their nodal-hypersurface theorem relates non-equivariant Hilbert-function information to defects of point systems, and consequently implies much of the present numerical profile. Their *On the syzygies and Alexander polynomials of nodal hypersurfaces* (arXiv:1111.1533, 2011) develops related degree bounds. A later example by Dimca and Sticlaru, *Syzygies of Jacobian ideals and weighted homogeneous singularities* (Journal of Symbolic Computation, 2016, Example 3.2), explicitly gives the Hilbert series of the four-variable Cayley cubic. These scalar dimension statements are acknowledged as prior work and not claimed as original.

The distinction is that a scalar Hilbert series cannot determine the irreducible \(\mathfrak S_m\)-characters. The claim here identifies every irreducible symmetry type in every layer of the **saturation defect** for the full infinite family; the inspected sections of those nodal-hypersurface papers do not provide this equivariant classification. This comparison is evidence rather than a guarantee against an equivalent unindexed calculation.

## Limitations
No characteristic-positive generalization is asserted: the proof uses characteristic-zero reduced Boolean evaluation, division by \(m-2\), and semisimplicity of \(\mathfrak S_m\). The theorem gives the graded representation of each layer, not a canonical splitting or the multiplication matrices connecting layers, and it does not furnish a minimal graded free resolution. The result should not be read as a new proof that the cubic has coordinate singularities, as that underlying fact is previously accessible; likewise neither the four-variable numerical Hilbert series nor general nodal Hilbert-function identities are new claims. Published equivalences not located by the literature comparison remain a residual priority risk.

## References
1. A. Dimca and G. Sticlaru, *Koszul complexes and pole order filtrations*, arXiv:1108.3976 (first public version 2011-08-19), https://arxiv.org/abs/1108.3976.
2. A. Dimca and G. Sticlaru, *On the syzygies and Alexander polynomials of nodal hypersurfaces*, arXiv:1111.1533 (first public version 2011-11-07), https://arxiv.org/abs/1111.1533.
3. A. Dimca and G. Sticlaru, *Syzygies of Jacobian ideals and weighted homogeneous singularities*, Journal of Symbolic Computation 74 (2016), 627–634, Example 3.2, https://doi.org/10.1016/j.jsc.2015.11.003.
4. B. Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions*, second edition, Springer, 2001 (Young's rule for subset-permutation representations).
