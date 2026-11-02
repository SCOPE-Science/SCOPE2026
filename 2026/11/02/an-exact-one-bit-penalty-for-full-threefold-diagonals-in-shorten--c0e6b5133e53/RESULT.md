# An exact one-bit penalty for full threefold diagonals in shortened Hamming lengths

## Finding

Let \(r\ge3\) be **odd**, put \(m=(2^r-2)/3\) and \(n=3m=2^r-2\), and define the linear threefold diagonal map
\[
\iota_3:\mathbb F_2^m\longrightarrow\mathbb F_2^n,\qquad u\longmapsto(u,u,u).
\]
Among binary linear codes \(C\le\mathbb F_2^n\) with minimum Hamming distance at least \(3\) and the entire diagonal \(\iota_3(\mathbb F_2^m)\subseteq C\), the largest dimension is **exactly**
\[
\boxed{\max\dim C=n-r-1.}
\]
In comparison, the largest possible dimension at the same length and distance without the diagonal restriction is \(n-r\). Thus requiring all threefold diagonal words costs **exactly one information bit** for each odd \(r\ge3\); the first lengths are \(6,30,126,510\).

Furthermore, all maximizing codes admit a geometric characterization: after choosing a full-rank parity-check matrix of rank \(r+1\), each coordinate triple \((i,m+i,2m+i)\) consists of the three nonzero vectors of a binary two-dimensional subspace; these \(m\) subspaces are pairwise disjoint outside zero and together span \(\mathbb F_2^{r+1}\). Conversely any such ordered, spanning partial line spread, with ordered nonzero column triples, defines a maximizing code. The statement concerns an exact correspondence of parity-check presentations under row operations, not an enumeration of equivalence classes.

## Assumptions and scope

Throughout \(\mathbb F_2\) is the binary field. A binary \([n,k,\ge3]\) linear code is a \(k\)-dimensional linear subspace of \(\mathbb F_2^n\) with all nonzero words of Hamming weight at least three. Its parity-check matrix has rank \(h=n-k\). Its columns are nonzero and pairwise distinct if and only if the code has minimum distance at least three. A *partial binary line spread* is a family of two-dimensional binary linear subspaces whose pairwise intersections are \(\{0\}\). We require containment of the **whole** \(m\)-dimensional diagonal, not an even-weight subdiagonal.

The oddness assumption on \(r\) makes \(2^r-2\) divisible by three and \(r+1\) even. It is essential to the stated family and the field-reduction construction. No assertion is made for arbitrary block lengths or stronger distance thresholds.

## Proof

**1. Unrestricted reference bound.** Any rank-\(h\) parity-check matrix for distance at least three has \(n\) distinct nonzero columns, so \(n\le2^h-1\). At \(n=2^r-2\) this forces \(h\ge r\). Equality is achievable: list every nonzero vector of \(\mathbb F_2^r\) except one as the \(n\) parity-check columns. Since all but one nonzero vector span \(\mathbb F_2^r\) for \(r\ge3\), the resulting shortened Hamming code has dimension \(n-r\) and distance at least three.

**2. The full-diagonal obstruction.** Suppose \(C\) contains \(\iota_3(\mathbb F_2^m)\) and had dimension \(n-r\). Then a rank-\(r\) parity-check matrix \(H\) for \(C\) has precisely \(2^r-2\) pairwise distinct nonzero columns in \(\mathbb F_2^r\). Thus its column set omits a unique nonzero vector \(v\). The sum of all nonzero vectors in \(\mathbb F_2^r\) is zero (for \(r\ge2\), each coordinate takes value one an even number of times), whence the sum of the columns of \(H\) is \(v\ne0\). But the all-one length-\(n\) word is \(\iota_3(\mathbf1_m)\in C\), so \(H\mathbf1_n=0\), contradicting that sum. Therefore every admissible code has rank at least \(r+1\) and dimension at most \(n-r-1\).

**3. Construction meeting the bound.** Write \(r+1=2t\) with \(t\ge2\), and use the field \(\mathbb F_4=\mathbb F_2[\omega]\), where \(\omega^2+\omega+1=0\). Field reduction identifies the binary space \(\mathbb F_2^{r+1}\) with \(\mathbb F_4^t\). Every one-dimensional \(\mathbb F_4\)-subspace \(L=\mathbb F_4v\) has exactly three nonzero vectors
\[
v,\quad \omega v,\quad\omega^2v,
\]
which are distinct and sum to zero. Different \(\mathbb F_4\)-lines share no nonzero vectors. There are \((4^t-1)/3\) such lines, more than \(m=(2^{2t-1}-2)/3\). Since \(m\ge t\), choose \(m\) distinct lines including the \(t\) coordinate-axis lines; let their representatives be \(v_1,\ldots,v_m\). Form an \((r+1)\times3m\) binary matrix \(H\) by field reduction, with columns in three consecutive blocks:
\[
H=[v_1\;\cdots\;v_m\mid\omega v_1\;\cdots\;\omega v_m\mid\omega^2v_1\;\cdots\;\omega^2v_m].
\]
All columns are distinct and nonzero. The \(t\) coordinate-axis lines contribute a binary spanning set of \(\mathbb F_2^{2t}\), so \(\operatorname{rank}H=r+1\). For every \(u\in\mathbb F_2^m\),
\[
H\iota_3(u)=\sum_{i=1}^m u_i(1+\omega+\omega^2)v_i=0.
\]
Hence \(C=\ker H\) contains the whole threefold diagonal, has dimension \(n-r-1\), and minimum distance at least three. Indeed its minimum distance is exactly three because \(\iota_3(e_i)\) has weight three. This matches the upper bound.

**4. Characterization of equality.** Let \(C\) meet the bound and let \(H\) be any full-rank \((r+1)\times n\) parity-check matrix. The inclusion \(\iota_3(e_i)\in C\) says the three columns \(a_i,b_i,c_i\), located at \(i,m+i,2m+i\), satisfy \(a_i+b_i+c_i=0\). Since they are nonzero and pairwise distinct, the triple is precisely the nonzero part of the two-dimensional subspace \(\langle a_i,b_i\rangle\). Pairwise distinctness of all \(n\) columns forces these binary lines to be disjoint outside zero. Full row rank makes their union span the ambient \(r+1\)-dimensional binary space. Conversely, a spanning family of such lines assembled into consecutive blocks gives a rank-\(r+1\) parity check with the requisite column and diagonal properties, and so a maximizing code. Changing the parity-check row basis acts by \(\mathrm{GL}_{r+1}(\mathbb F_2)\). This proves the asserted correspondence.

## Verification

The accompanying standalone Python file `verify_triple.py` uses exact integer arithmetic to implement \(\mathbb F_4\) multiplication and field reduction; it constructs the full three-block parity-check matrices at \(r=3,5,7,9\), checks column nonzeroness and uniqueness, exact rank \(r+1\), and all \(m\) generators of the contained diagonal. It also tests the seven possible rank-three parity-check column sets of length six: every such set has nonzero total column sum. A successful execution prints `VERIFY_OK`, as reproduced in the finite check. These checks corroborate the explicit construction and obstruction but do not replace the all-integer proof above.

## Relationship to prior work

Kim's 2026 study [1] proves no redundancy penalty for the **twofold** diagonal containing the even-weight subcode (Theorem 6.6), and explicitly poses development of the \(s\)-fold analogue in Problem 6.31. The new result addresses the **threefold full-diagonal** situation at the infinitely many special lengths \(2^r-2\), where the answer is instead a sharp one-bit penalty. The classical shortened Hamming construction [1,2] establishes the *unrestricted* comparison but not containment of the full threefold diagonal. Field reduction and Desarguesian two-spreads [3] supply the classical geometric ingredient of disjoint binary lines; their existence alone does not state the present constrained code-dimension optimum or its all-equality partial-spread characterization. These are explicit distinctions of hypotheses and implications, not claims that standard underlying tools are new.

## Limitations

The dimensional optimum and geometry are proved for odd \(r\ge3\), and for binary linear distance-at-least-three codes containing the **entire** threefold diagonal. The construction is an existence recipe rather than a classification of equivalence orbits or an encoding-implementation analysis. The statement does not give the full all-length or all-multiplicity generalization requested in [1]. Novelty relative to unindexed or unpublished material remains subject to independent literature review. No external independent mathematical validation has been performed.

## References

[1] Jon-Lark Kim, *Extremal diagonal-coherent binary codes: shortened Hamming cores, deep holes, and the 64 I-Ching hexagrams*, arXiv:2610.33676v1, first posted 24 October 2026, Theorem 6.6 and Problem 6.31. https://arxiv.org/abs/2610.33676v1

[2] M. R. Best and A. E. Brouwer, *The triply shortened binary Hamming code is optimal*, Discrete Mathematics **17** (1977), 235–245. https://doi.org/10.1016/0012-365X(77)90158-3

[3] Geertrui Van de Voorde, *Desarguesian spreads and field reduction for elements of the semilinear group*, Linear Algebra and its Applications **507** (2016), 96–120. https://doi.org/10.1016/j.laa.2016.05.038
