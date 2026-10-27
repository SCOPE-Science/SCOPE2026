# Exact matrix-size threshold for even-cycle trace-norm embeddings

## Finding
Let \(k\ge 2\) and \(d\ge 1\) be integers, and equip \(M_d(\mathbb C)\) with its Schatten trace norm \(\|A\|_1=\operatorname{Tr}\sqrt{A^*A}\). Give the graph cycle \(C_{2k}=\mathbb Z/(2k)\mathbb Z\) its shortest-path metric. There is an isometric embedding of \(C_{2k}\) into \((M_d(\mathbb C),\|\cdot\|_1)\) **if and only if \(d\ge k\)**. Arbitrary non-Hermitian matrices and nonlinear embeddings are allowed.

Equivalently, for nonconstant \(f:C_{2k}\to M_d(\mathbb C)\) define
\[
\mathcal R_{k,d}(f)=
\frac{\bigl(\mathbb E_x\|f(x+k)-f(x)\|_1^2\bigr)^{1/2}}
{\bigl(\mathbb E_{x,\varepsilon}\|f(x+\varepsilon)-f(x)\|_1^2\bigr)^{1/2}},
\qquad \varepsilon\in\{-1,0,1\}\ \text{uniformly}.
\]
Then \(\mathcal R_{k,d}(f)\le k\sqrt{3/2}\), with equality for some nonconstant \(f\) **if and only if \(d\ge k\)**. Every equality map, after translation and positive rescaling, is a metric-isometric embedding of the cycle. For \(d<k\) the sharp finite-dimensional supremum is strictly smaller than \(k\sqrt{3/2}\), but its exact numerical value is not determined here.

## Assumptions and scope
The underlying matrices are all complex \(d\times d\) matrices, not necessarily normal or self-adjoint. The graph cycle has \(2k\) vertices and unit edge lengths. All expectations are uniform over their stated finite sets; addition of indices is modulo \(2k\). The denominator is positive for every nonconstant map. Isometric means preserving every pairwise graph distance exactly; the scale in the equality characterization is the common positive edge norm.

## Proof
**Universal bound and equality geometry.** Put \(A_j=f(j+1)-f(j)\), with indices modulo \(2k\), so that \(\sum_jA_j=0\), and \(a_j=\|A_j\|_1\). For each \(x\), the opposite-vertex difference equals \(\sum_{h=0}^{k-1}A_{x+h}\). Pointwise trace-norm triangle inequality followed by Minkowski's inequality in the scalar Hilbert space \(\ell_2(C_{2k})\) gives
\[
\Bigl(\mathbb E_x\Bigl\|\sum_{h=0}^{k-1}A_{x+h}\Bigr\|_1^2\Bigr)^{1/2}
\le \Bigl(\mathbb E_x\bigl(\sum_{h=0}^{k-1}a_{x+h}\bigr)^2\Bigr)^{1/2}
\le k\bigl(\mathbb E_xa_x^2\bigr)^{1/2}.
\]
The denominator of \(\mathcal R_{k,d}\) is \(\sqrt{(2/3)\mathbb E_xa_x^2}\). This proves the bound. Equality in scalar Minkowski for the \(k\) cyclic translates of \((a_j)_j\), all having the same positive \(\ell_2\)-norm, forces these translates to coincide; because \(k\ge2\), \(a_j=c>0\) for every \(j\). Equality in the first inequality then forces
\[\Bigl\|\sum_{h=0}^{k-1}A_{x+h}\Bigr\|_1=kc\quad\text{for every }x.\]
Every shorter contiguous arc lies in an arc of \(k\) edges. Trace-norm equality along a \(k\)-edge arc implies equality on each of its subarcs (otherwise triangle inequality would be strict on the whole arc). Hence \(\|f(x+t)-f(x)\|_1=tc\) for every \(0\le t\le k\), proving that \(f/c\) is isometric after translation. Conversely, any scaled isometric embedding makes both inequalities equalities.

**A trace-norm support lemma.** Suppose \(A,B\in M_d(\mathbb C)\) are nonzero, \(\|A+B\|_1=\|A\|_1+\|B\|_1\), and a contraction \(H\) satisfies
\[\operatorname{Re}\operatorname{Tr}(H^*A)=\|A\|_1,\qquad\operatorname{Re}\operatorname{Tr}(H^*B)=-\|B\|_1.\]
Then the right supports of \(|A|\) and \(|B|\) are orthogonal. Indeed, for polar decompositions \(A=U_A|A|\) and \(B=U_B|B|\), equality in trace-norm duality forces \(H\) to act on the right polar supports as \(U_A\) and \(-U_B\), respectively. Since \(A+B\) attains the sum of the two trace norms, another contraction \(G\) acts on those supports as \(U_A\) and \(+U_B\). A contraction preserving the norm of a vector preserves its inner products with all other vectors on which it is also norm-preserving: if \(\|Hv\|=\|v\|\), then \((I-H^*H)v=0\). Therefore for any vectors \(u,v\) in the respective right supports,
\[\langle u,v\rangle=\langle U_Au,-U_Bv\rangle=\langle U_Au,U_Bv\rangle,\]
so \(\langle u,v\rangle=0\), as asserted.

**Necessary matrix size.** Let \(f\) be a scaled isometric embedding with edge length \(c>0\). Set \(P=\sum_{i=0}^{k-1}A_i\), so \(\|P\|_1=kc\). Choose a contraction \(H\) norming \(P\). Equality along this half-cycle and along the opposite half-cycle (whose total increment is \(-P\)) implies
\[B_i:=H^*A_i=|A_i|\ge0,\quad C_i:=-H^*A_{i+k}=|A_{i+k}|\ge0\qquad(0\le i<k).\]
All \(B_i,C_i\) are nonzero and
\[S:=\sum_{i=0}^{k-1}B_i=\sum_{i=0}^{k-1}C_i,\]
because \(\sum_jA_j=0\). For \(i\ne j\), the two edges numbered \(i\) and \(k+j\) lie in a common contiguous arc containing at most \(k\) edges. Consequently \(\|A_i+A_{k+j}\|_1=2c\); the support lemma, applied to these two increments and \(H\), implies \(\operatorname{ran}B_i\perp\operatorname{ran}C_j\). In particular, \(\operatorname{Tr}(B_iC_j)=0\) when \(i\ne j\).

For each \(i\), however,
\[
\operatorname{Tr}(B_iC_i)=\operatorname{Tr}(B_iS)
=\operatorname{Tr}(B_i^2)+\sum_{j\ne i}\operatorname{Tr}(B_iB_j)
\ge\operatorname{Tr}(B_i^2)>0.
\]
The cross traces \(\operatorname{Tr}(B_iB_j)\) are nonnegative because both factors are positive semidefinite. Choose \(u_i\in\operatorname{ran}B_i\), \(v_i\in\operatorname{ran}C_i\) with \(\langle u_i,v_i\rangle\ne0\). All off-diagonal pairings \(\langle u_i,v_j\rangle\) vanish. Thus the \(k\times k\) pairing matrix has rank \(k\), requiring \(d\ge k\). This argument uses no commutativity, self-adjointness, or linearity of \(f\).

**Sufficiency.** If \(d\ge k\), let \(E_{ii}\) be the first \(k\) diagonal matrix units. Put \(A_i=E_{i+1,i+1}\) for \(0\le i<k\), and \(A_{k+i}=-E_{i+1,i+1}\). Define \(f(0)=0\) and \(f(j)=\sum_{h<j}A_h\). Every arc of at most \(k\) consecutive edges uses distinct diagonal coordinates, so its total increment has trace norm equal to its length. Hence \(f\) is an isometric embedding of the cycle, which also saturates \(\mathcal R_{k,d}\).

**Strictness in smaller matrix size.** If \(d<k\), the preceding necessity rules out equality. Normalize \(f(0)=0\) and the denominator to equal \(1\). Then all edge norms and all values \(f(j)\) lie in a bounded subset of a fixed finite-dimensional space, and the normalization constraint is closed. The resulting family is compact; the continuous ratio attains its maximum there. As it cannot attain \(k\sqrt{3/2}\), its maximum is strictly smaller.

## Verification
For every \(k=2,3,\ldots,8\), direct singular-value computations on the stated diagonal construction gave ratio \(k\sqrt{3/2}\) up to floating-point precision. The accompanying `checker.py` independently repeats these finite checks, evaluates a scalar Fourier-mode comparison, and tests the upper bound on sampled complex matrices. These calculations support the construction only; the general matrix-size obstruction, compactness argument, and all universal bounds are proved above.

## Relationship to prior work
Jiao, Luo, and Wu establish the metric-cotype inequality for arbitrary-dimensional trace class with sharp **scale order**; they do not give this exact one-dimensional saturation constant or the necessary and sufficient size of the matrix realizing it. The present result uses their metric-cotype setup but asks a finite-matrix **equality-dimension** question rather than their asymptotic scaling question. Mendel and Naor introduce the discrete-torus cotype formulation and qualitative nonlinear geometry; their general metric-cotype theorem does not imply a sharp trace-class matrix-rank obstruction. Rigobert and Laurent determine exact binary-Cayley host dimensions for even cycles; their host restriction does not imply a lower bound for arbitrary noncommutative matrices carrying the trace norm. A broad prior-terminology and priority risk remains for the isometric-cycle interpretation.

## Limitations
This does not compute the sharp subthreshold ratio in dimensions \(d<k\), nor assert a quantitative gap uniform in \(k\). It does not address odd cycles, higher-dimensional tori, infinite Schatten-rank constraints, or a classification of all trace-class equality embeddings. All empirical checks are finite diagnostics, not proofs of universal statements. Independent evaluation of the proof and historical priority has not been performed.

## References
1. Y. Jiao, S. Luo and L. Wu, *The Sharp Scale Inequality for the Schatten Trace Class*, arXiv:2610.21445v1, first submitted 2026-10-15, https://arxiv.org/html/2610.21445v1.
2. M. Mendel and A. Naor, *Metric Cotype*, Annals of Mathematics 168 (2008), https://annals.math.princeton.edu/2008/168-1/p07.
3. F. S. Rigobert and B. Laurent, *Dimension and Order Bounds for Isometric Embeddings of Graphs into Abelian Cayley Graphs, and the Abelian Dividend*, arXiv:2607.07939, https://arxiv.org/abs/2607.07939.
