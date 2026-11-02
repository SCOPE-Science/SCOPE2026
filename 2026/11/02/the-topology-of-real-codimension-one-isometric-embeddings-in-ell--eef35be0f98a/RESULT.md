# The topology of real codimension-one isometric embeddings in \(\ell^p\)

## Finding

**Theorem.** Let \(n\ge 2\) be an integer and \(1\le p<\infty\) with \(p\ne 2\). Let \(\mathcal I_{n,p}\) be the set of real-linear isometric embeddings
\[
T:\ell_{n-1}^{p}(\mathbb R)\longrightarrow\ell_n^{p}(\mathbb R),
\]
with the operator-norm topology. Then \(\mathcal I_{n,p}\) is homeomorphic to a finite, connected, \(2(n-1)\)-regular graph whose vertex and edge counts are
\[
V_n=2^{n-1}n!,\qquad E_n=2^{n-1}(n-1)n!.
\]
Consequently,
\[
\mathcal I_{n,p}\simeq \bigvee^{\,1+2^{n-1}(n-2)n!}S^1,
\]
with the convention that a wedge of one circle is a circle. In particular,
\[
\pi_1(\mathcal I_{n,p})\cong F_{1+2^{n-1}(n-2)n!},\quad
H_1(\mathcal I_{n,p};\mathbb Z)\cong\mathbb Z^{1+2^{n-1}(n-2)n!},
\]
and \(\widetilde H_j(\mathcal I_{n,p};\mathbb Z)=0\) for \(j\ne1\). The homeomorphism type is independent of the allowed exponent \(p\).

The first Betti numbers for \(n=2,3,4,5,6\) are, respectively, \(1,25,385,5761,92161\). In contrast, real surjective isometries of \(\ell_{n-1}^p\) form a discrete space of \(2^{n-1}(n-1)!\) points. A single extra output coordinate therefore changes the topology from discrete to connected with nontrivial first homology.

## Assumptions and scope

All vector spaces and linear maps are **real**. The domain has dimension exactly \(n-1\), the codomain has dimension exactly \(n\), and \(p\in[1,\infty)\setminus\{2\}\). An isometric embedding preserves the \(\ell^p\)-norm of **every** input vector. The topology on matrices is the operator-norm topology, equivalent to entrywise convergence in this finite-dimensional setting.

No claim is made for complex-linear isometries, for the Hilbert-space exponent \(p=2\), for \(p=\infty\), or for other dimension gaps. The graph is a genuine finite topological realization, not merely a combinatorial deformation model.

## Proof

**1. Complete disjoint-support characterization.** Write the matrix columns as \(v_1,\ldots,v_{n-1}\). Isometry implies \(\|v_j\|_p=1\) and, for distinct \(i,j\),
\[
\|v_i+v_j\|_p^p+\|v_i-v_j\|_p^p
=2\|v_i\|_p^p+2\|v_j\|_p^p.
\]
For real scalars \(a,b\), the difference
\[
\delta_p(a,b)=|a+b|^p+|a-b|^p-2|a|^p-2|b|^p
\]
has the strict sign of \(p-2\) when \(ab\ne0\), and is zero when \(ab=0\). To verify this directly for \(1\le p<2\), put \(r=p/2<1\). Concavity and strict subadditivity yield
\[
|a+b|^p+|a-b|^p\le2(a^2+b^2)^r
<2(|a|^p+|b|^p)
\]
for \(ab\ne0\). For \(p>2\), convexity and strict superadditivity reverse these inequalities. Summing \(\delta_p\) over rows forces every pair of columns to have disjoint supports. Conversely, nonzero pairwise disjoint columns of unit \(\ell^p\)-norm visibly define an isometry, since the \(p\)-th powers of their coordinatewise contributions add.

**2. Only vertices and open edges exist.** There are \(n-1\) disjoint nonempty column supports among only \(n\) rows. If one row is unused, every column has exactly one entry, necessarily equal to \(+1\) or \(-1\). These matrices are the vertices. They are indexed by an injection assigning a distinct row to each labelled column, together with one sign per column. Hence
\[
V_n=\underbrace{n!}_{\text{ordered columns and unused row}}
\underbrace{2^{n-1}}_{\text{signs}}.
\]

If all rows are occupied, exactly one column has two nonzero entries and every other column has one. Fix the doubled column, its two rows, the bijection between remaining columns and remaining rows, and all signs. The two absolute values in the doubled column satisfy
\[
|a|^p+|b|^p=1,
\]
so \(t=|b|^p\in(0,1)\) continuously parametrizes an **open edge**. Its endpoints at \(t=0\) and \(t=1\) are signed-injection vertices, with the unused row switching between the two row positions. The number of these open edges is exactly
\[
E_n=(n-1)\binom n2(n-2)!\,2^n
=2^{n-1}(n-1)n!.
\]
No two different open-edge descriptions overlap, because the unique doubled column and its signs and row supports can be recovered from the matrix. Each vertex is incident to exactly \(2(n-1)\) edges: one chooses a column to transfer toward the single unused row and independently chooses the sign of the new entry.

Attaching the finitely many closed parameter intervals to the finitely many vertices using these endpoints yields a finite abstract graph \(G_n\) and a continuous bijection \(G_n\to\mathcal I_{n,p}\). Since \(G_n\) is compact and the finite-dimensional matrix space is Hausdorff, this map is a homeomorphism. This step handles all support degenerations and is not implied merely by knowing the topology of each fixed-support stratum.

**3. Connectivity.** Represent a vertex by an ordered list of the \(n-1\) occupied rows and the one blank row, together with column signs. Crossing any incident edge swaps the blank row with the row occupied by a chosen labelled column. Ignoring signs, such blank--occupied swaps generate every permutation of the \(n\) row positions. Thus the underlying unsigned configurations form one connected class.

Signs are also adjustable. Starting with a vertex, move a chosen column to the blank row (cross one edge), then move it back (cross another edge), choosing the opposite sign for the returning entry. All row assignments return to their original locations while that one column sign changes. Repeating independently for each column reaches any sign pattern. Thus \(G_n\) is connected.

**4. Homotopy and exponent invariance.** A connected finite graph deformation-retracts onto a wedge of \(E_n-V_n+1\) circles by collapsing a spanning tree. Therefore
\[
E_n-V_n+1=1+2^{n-1}(n-2)n!.
\]
The fundamental-group and integral-homology assertions follow from the standard cellular chain complex of a connected graph.

For any other allowed exponent \(q\), apply the entrywise homeomorphism \(a\mapsto\operatorname{sgn}(a)|a|^{p/q}\) to every matrix. Unit \(\ell^p\) columns map to unit \(\ell^q\) columns, disjoint supports remain disjoint, and the inverse uses exponent \(q/p\). This gives a homeomorphism \(\mathcal I_{n,p}\to\mathcal I_{n,q}\). Finally, in equal source and target dimension, all columns must be singletons, leaving precisely the isolated signed permutations described above.

## Verification

The accompanying standalone `check_graph.py` enumerates signed-injection vertices and all blank--occupied elementary moves for \(2\le n\le6\). It independently checks the vertex and edge formulas, regularity, connectedness, and graph cycle rank. It also performs 45,280 finite norm-preservation assertions for explicitly parametrized edge interiors with \(p\in\{1,1.5,3,4\}\). The script prints the complete small-parameter count table. These checks are finite corroboration; the general statement follows from the proof above.

To reproduce: run `python3 check_graph.py` with Python 3 standard library. No third-party packages or external files are needed.

## Relationship to prior work

Dalfollo-Daley, Delfín, Fernández, Mars, and Xia, *Restricted isometries in finite-dimensional \(\ell^p\)-spaces*, arXiv:2610.32615v1 (first public 23 October 2026), Theorem 3.18, provide the underlying disjoint-support characterization for restricted isometries. Their Proposition 4.5 determines products of open simplices (and real sign components) **with each support transformation fixed**. The present result concerns only full real isometric embeddings with exactly one spare codomain coordinate. Its new content is the global *gluing of all such strata across vanishing entries*, explicit connectivity, and exact topology and homology of the resulting graph.

Phillips, *Analogs of Cuntz algebras on \(L^p\) spaces*, arXiv:1201.4196v1, Section 6 (including Lemma 6.22), studies spatial/semispatial isometries and proves path rigidity of the underlying set transformation for **surjective** isometries. That does not imply the present connected topology of nonsurjective embeddings, where coordinates can split and collapse. The proof here does not depend on Phillips's representation theorem.

## Limitations

The proof does not classify the higher-dimensional cell attachments that appear with two or more spare coordinates. Over complex scalars, circle phases create qualitatively different strata and homotopy. At \(p=2\), ordinary real Stiefel manifolds replace the disjoint-support graph; \(p=\infty\) also lies outside the characterization. No assertion of external independent validation or comprehensive historical priority is made. Earlier work could formulate the same graph using signed partial injections rather than isometries.

## References

1. O. Dalfollo-Daley, A. Delfín, C. Fernández, C. Mars, X. Xia, *Restricted isometries in finite-dimensional \(\ell^p\)-spaces*, arXiv:2610.32615v1, 23 October 2026, https://arxiv.org/html/2610.32615v1.
2. N. C. Phillips, *Analogs of Cuntz algebras on \(L^p\) spaces*, arXiv:1201.4196v1, 20 January 2012, Section 6, https://arxiv.org/html/1201.4196v1.
