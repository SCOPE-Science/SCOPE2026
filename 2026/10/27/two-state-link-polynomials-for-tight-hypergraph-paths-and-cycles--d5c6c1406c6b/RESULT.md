# Two-state link polynomials for tight hypergraph paths and cycles

## Finding
Let \(\mathcal H\) denote the countable homogeneous 3-uniform hypergraph whose age consists of all finite hypergraphs containing no complete 3-uniform hypergraph on four vertices (no tetrahedron). Let \(A\) be a finite induced subhypergraph with every vertex individually named. For a nonalgebraic complete one-point type \(p\) over \(A\), define \(\ell(p)\) as the number of pairs \(\{a,b\}\subseteq A\) for which the new point \(x\) has the hyperedge \(\{x,a,b\}\). Put \(P_A(u)=\sum_{p\text{ nonalgebraic}}u^{\ell(p)}\).

For integers \(n\ge3\), let \(L_n\) be the tight path with vertices \(0,\ldots,n-1\) and triples \(\{i,i+1,i+2\}\) for \(0\le i\le n-3\). For integers \(n\ge5\), let \(C_n^{(3)}\) be the tight cycle with vertex set \(\mathbb Z/n\mathbb Z\) and triples \(\{i,i+1,i+2\}\) modulo \(n\). Define the polynomial matrix and row vector
\[
M(u)=\begin{pmatrix}1+u&u(1+u)\\1+u&u\end{pmatrix},\qquad v(u)=(1,u),\qquad \mathbf1=\begin{pmatrix}1\\1\end{pmatrix}.
\]
Then the entire degree-refined nonalgebraic one-type spectrum is
\[
\boxed{P_{L_n}(u)=(1+u)^{\binom n2-(2n-3)}\,v(u)M(u)^{n-2}\mathbf1}\quad(n\ge3),
\]
\[
\boxed{P_{C_n^{(3)}}(u)=(1+u)^{\binom n2-2n}\,\operatorname{tr}(M(u)^n)}\quad(n\ge5).
\]
In particular, with \(\lambda_{\pm}=(3\pm\sqrt{17})/2\), the exact number of nonalgebraic complete one-point types over the tight cycle is
\[
\boxed{N_n=2^{\binom n2-2n}(\lambda_+^n+\lambda_-^n)}\quad(n\ge5).
\]
The first cycle values for \(n=5,6,7\) are \(573,16328,930432\). The first path values for \(n=3,4,5\) are \(7,50,712\). Including algebraic types over the named base adds exactly \(n\) in each case. The exact asymptotic fraction of admissible one-point link graphs among all labelled graphs on the parameter set is
\[
\frac{N_n}{2^{\binom n2}}=\left(\frac{3+\sqrt{17}}8\right)^n\left(1+\left(\frac{3-\sqrt{17}}{3+\sqrt{17}}\right)^n\right).
\]
Thus this fraction decays with base \((3+\sqrt{17})/8\approx0.890388\), strictly greater than the independent-triple benchmark \(7/8\). The positive correlation of consecutive forbidden triangles is exponentially visible.

## Assumptions and scope
Every hyperedge is an unordered three-element subset; the forbidden tetrahedron has all four three-element subsets of a four-set as hyperedges. The base vertices are individually named, and all types counted by \(P_A\) require the new point to be distinct from them. The cycle formula starts at \(n=5\): the nominal four-cycle is itself a forbidden tetrahedron and is not an admissible parameter structure. Parameters are taken in the standard first-order language containing one symmetric irreflexive ternary relation. This is an exact type spectrum over two specified natural families, not a claim about arbitrary finite bases or about independent verification.

## Proof
The class of tetrahedron-free finite 3-uniform hypergraphs has hereditary, joint-embedding and free-amalgamation properties. In a free amalgam, no new hyperedge meets both disjoint sides outside the common base, so a tetrahedron cannot straddle them. Its Fraïssé limit \(\mathcal H\) is homogeneous, and finite relational homogeneity gives quantifier elimination. A nonalgebraic complete one-point type over finite \(A\) is therefore specified exactly by its link graph \(L\subseteq\binom A2\), whose edge \(ab\) means that \(xab\) is a hyperedge. The one-point extension is tetrahedron-free if and only if, for every triple \(abc\) already an edge of \(A\), not all of \(ab,bc,ac\) lie in \(L\). Necessity and sufficiency follow because any newly formed tetrahedron must contain the new point, and the remaining three vertices must form an existing base hyperedge. Each admissible extension is realized by the Fraïssé extension property.

Both the tight path and tight cycle in the statement are tetrahedron-free. Indeed, if a four-set had all four triples, choose a member \(\{i,i+1,i+2\}\). A fourth vertex completing an edge with \(\{i,i+1\}\) would have to be \(i-1\), whereas one completing an edge with \(\{i+1,i+2\}\) would have to be \(i+3\). For a tight cycle of length at least five these vertices differ modulo \(n\); on the path they are also different, and some may be absent. This contradiction proves the claim.

For a tight cycle of length \(n\ge5\), distinguish the \(n\) consecutive pair variables \(a_i\in\{0,1\}\) attached to \(\{i,i+1\}\) and the \(n\) short-chord variables \(b_i\in\{0,1\}\) attached to \(\{i,i+2\}\), with all indices modulo \(n\). These are \(2n\) different unordered pairs, including at \(n=5\). The local tetrahedron constraint at the base triple \(\{i,i+1,i+2\}\) is precisely \(a_i a_{i+1} b_i=0\). Once \(a_i,a_{i+1}\) are fixed, summing over \(b_i\) contributes the fugacity factor \(1+u\) unless both cycle-edge indicators are one, when only \(b_i=0\) is allowed and the factor is \(1\). Give the arrival edge \(a_{i+1}\) its weight \(u^{a_{i+1}}\). The resulting transition matrix, with rows indexed by \(a_i=0,1\) and columns by \(a_{i+1}=0,1\), is exactly \(M(u)\). Multiplication around the closed cycle counts every cyclic assignment once and gives \(\operatorname{tr}(M(u)^n)\). The other \(\binom n2-2n\) link edges are unconstrained and contribute \((1+u)^{\binom n2-2n}\).

For a tight path, the \(n-1\) consecutive edges and \(n-2\) short chords are distinct, a total of \(2n-3\) link variables. The initial edge supplies \(v(u)=(1,u)\); its \(n-2\) transitions are governed by the same \(M(u)\); the final state is unrestricted, so sum it with \(\mathbf1\). The remaining \(\binom n2-(2n-3)\) pairs are free. This proves both polynomial identities.

At \(u=1\), \(M(1)=\begin{pmatrix}2&2\\2&1\end{pmatrix}\), with characteristic polynomial \(t^2-3t-2\) and distinct eigenvalues \(\lambda_{\pm}\). Therefore \(\operatorname{tr}(M(1)^n)=\lambda_+^n+\lambda_-^n\). Dividing by all \(2^{\binom n2}\) possible link graphs proves the probability identity. Since \(|\lambda_-|<\lambda_+\), the leading rate is \(\lambda_+/4=(3+\sqrt{17})/8\); it exceeds \(7/8\) because \(\sqrt{17}>4\). This is an all-length proof, not an inference from finite tests.

## Verification
The accompanying standalone `verify.py` independently enumerates all link graphs for tight paths of lengths three through six and tight cycles of lengths five and six, comparing full fugacity-polynomial coefficients with the matrix identities. It also directly enumerates all \(2^{21}\) link graphs over the seven-vertex tight cycle and checks its unweighted total. Additional checks establish the tetrahedron-free boundary through cycle length eleven and the characteristic recurrence through length nineteen. Run `python3 verify.py`; the expected output is recorded in `verification_output.txt`. The checker uses only Python's standard library. Exhaustive finite checks support, but do not substitute for, the general proof above.

## Relationship to prior work
The cyclic consecutive-triple object is the standard tight Hamilton-cycle hypergraph considered, for example, by Frieze, Krivelevich and Loh (arXiv:1005.4711, first publicly posted 25 May 2010); that work studies cycle packing, not the finite-parameter one-point type polynomial asserted here. Fraïssé theory supplies the established homogeneous-limit and one-point-extension framework. Literature on set-homogeneous hypergraphs treats homogeneity and examples rather than this transfer spectrum. Results for the generic \(K_4^-\)-free 3-hypergraph impose the stronger restriction excluding a three-edge tetrahedral configuration, distinct from forbidding all four edges; they do not directly give this tetrahedron-free cycle formula. The two-state transfer method itself is classical and is not claimed as new. The assessed contribution is the explicit complete polynomial in both natural boundary conditions and its sharp cycle asymptotic in the specified homogeneous theory.

## Limitations
Originality is best-knowledge rather than established uniqueness: an implicit equivalent in statistical-mechanics transfer literature, hypergraph extension enumerations or unindexed type-counting work remains possible. The cited tight-cycle packing paper was inspected for its definitions and stated research focus, not exhaustively for every passage. No conclusion is made for arbitrary base hypergraphs, finite parameter sets outside the two families, or higher-arity types. No independent scientific audit has been performed.

## References
- Alan Frieze, Michael Krivelevich and Po-Shen Loh, *Packing tight Hamilton cycles in 3-uniform hypergraphs*, arXiv:1005.4711 (first posted 2010-05-25), https://arxiv.org/abs/1005.4711.
- Amir Assari, Narges Hosseinzadeh and Dugald Macpherson, *Set-homogeneous hypergraphs*, Journal of the London Mathematical Society 108 (2023), 1852–1885, https://doi.org/10.1112/jlms.12796.
- The standard Fraïssé amalgamation theorem for finite relational structures; used here only in its conventional free-amalgamation form.
