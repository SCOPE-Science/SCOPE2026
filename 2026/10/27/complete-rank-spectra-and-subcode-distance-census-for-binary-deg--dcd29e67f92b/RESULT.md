# Complete rank spectra and subcode-distance census for binary degree-two Gabidulin codes

## Finding

For every integer \(m\ge 2\), let \(K=\mathbb F_{2^m}\) and let \(C\) be the binary matrix Gabidulin code comprising all \(\mathbb F_2\)-linear endomorphisms
\[
L_{a,b}:K\longrightarrow K,\qquad L_{a,b}(x)=ax+bx^2,\qquad (a,b)\in K^2.
\]
After choosing any binary basis of \(K\), this is a linear \([m\times m,2m,m-1]_2\) rank-metric code. Write \(A=\{L_{a,0}:a\in K\}\) and \(B=\{L_{0,b}:b\in K\}\). For any \(d\)-dimensional binary subcode \(U\le C\), \(0\le d\le2m\), put
\[
r=\dim_{\mathbb F_2}(U\cap A),\qquad s=\dim_{\mathbb F_2}(U\cap B),\qquad t=d-r-s.
\]

**Complete rank enumerator.** With \(W_U(z)=\sum_{L\in U}z^{\operatorname{rk}_{\mathbb F_2}L}\),
\[
\boxed{W_U(z)=1+(2^r+2^s-2)z^m+(2^d-2^r-2^s+1)z^{m-1}.}
\]
In particular, the number of rank-\(m\) elements of \(U\), the number of rank-\((m-1)\) elements, and the complete subcode-distance profile depend only on \((d,r,s)\). For every \(1\le i\le d\), defining \(\alpha_i(U)\) to be the largest minimum rank distance of an \(i\)-dimensional binary subcode of \(U\),
\[
\boxed{\alpha_i(U)=\begin{cases}m,&1\le i\le\max(r,s),\\m-1,&\max(r,s)<i\le d.\end{cases}}
\]

**Exact joint population.** The number of labeled \(d\)-dimensional binary subcodes \(U\le C\) with the indicated intersection dimensions is
\[
\boxed{
N_{m,d}(r,s)=
{m\brack r}_2{m\brack s}_2
{m-r\brack t}_2{m-s\brack t}_2\,|\mathrm{GL}_t(\mathbb F_2)|,
\qquad t=d-r-s.
}
\]
Here \({n\brack k}_2=\prod_{j=0}^{k-1}(2^{n-j}-1)/(2^{k-j}-1)\) for \(0\le k\le n\) (zero otherwise), and \(|\mathrm{GL}_t(\mathbb F_2)|=\prod_{j=0}^{t-1}(2^t-2^j)\), including the empty product at \(t=0\). This formula applies precisely when \(0\le r,s\le m\) and \(0\le t\le\min(m-r,m-s)\), and gives zero for infeasible parameters. The sum of all populations at fixed \(d\) equals \({2m\brack d}_2\).

**Sharp deletion-of-dimensions probability.** If \(U\) is uniform among all binary subcodes of codimension \(c\), with \(1\le c\le m\), then
\[
\boxed{\Pr\bigl[\alpha_m(U)=m\bigr]
=\frac{2{m\brack c}_2}{{2m\brack c}_2},\qquad
\Pr\bigl[\alpha_m(U)=m-1\bigr]
=1-\frac{2{m\brack c}_2}{{2m\brack c}_2}.}
\]
In particular, a uniform hyperplane preserves the exceptional best distance \(\alpha_m=m\) with exact probability \(2/(2^m+1)\), and lowers it to \(m-1\) with probability \((2^m-1)/(2^m+1)\). There are exactly \(2(2^m-1)\) preserving hyperplanes and \((2^m-1)^2\) lowering hyperplanes.

## Assumptions and scope

All vector spaces, subspaces, matrix ranks, and code dimensions are over \(\mathbb F_2\), except the field \(K\) used to parameterize linearized maps. A binary basis identifies \(\operatorname{End}_{\mathbb F_2}(K)\) with \(m\times m\) matrices; the conclusions do not depend on the chosen basis. Two subcodes are counted separately whenever they are distinct as subsets of \(C\), without quotienting by any code automorphism. The subcode-distance definition optimizes over *linear subcodes*, not arbitrary subsets. The zero subcode is included in the population identity, but has no \(\alpha_i\) values.

## Proof

**1. Rank dichotomy and faithful parameterization.** If exactly one of \(a,b\) is nonzero, multiplication by a nonzero field element, possibly composed with Frobenius, is a binary automorphism of \(K\), so \(\operatorname{rk}(L_{a,b})=m\). If both coefficients are nonzero, the equation \(ax+bx^2=0\) has exactly the two solutions \(x=0\) and \(x=a/b\); its kernel is one-dimensional over \(\mathbb F_2\), so its rank is \(m-1\). The zero coefficient pair is the zero map. Since \(m\ge2\), no nonzero coefficient pair gives the zero map, and the coefficient parameterization is injective. Hence \(C=A\oplus B\) has binary dimension \(2m\), minimum rank distance \(m-1\), and the *only* nonzero rank-\(m\) elements are the nonzero elements of \(A\cup B\).

**2. Rank enumerator.** Let \(R=U\cap A\) and \(S=U\cap B\). Their nonzero sets are disjoint. Thus exactly \((2^r-1)+(2^s-1)\) elements of \(U\) have rank \(m\). Every other nonzero element has rank \(m-1\), giving the displayed polynomial. In particular, there are no other nonzero ranks in any subcode.

**3. Optimal subcode distances.** Any linear subspace in which all nonzero elements have rank \(m\) lies in \(A\cup B\). If such a subspace had an element in \(A\setminus\{0\}\) and another in \(B\setminus\{0\}\), their sum would have both coefficients nonzero, and therefore rank \(m-1\), a contradiction. Consequently every full-rank-only linear subcode is contained in \(A\) or \(B\); the largest one inside \(U\) has dimension exactly \(\max(r,s)\). For smaller indices this supplies rank-\(m\) subcodes. For larger indices every subcode contains a rank-\((m-1)\) nonzero word, while the parent code has minimum rank distance \(m-1\). This proves the entire sequence \(\alpha_i(U)\) without assuming a probabilistic model.

**4. Population formula.** First choose \(R=U\cap A\) of dimension \(r\) and \(S=U\cap B\) of dimension \(s\). There are \({m\brack r}_2{m\brack s}_2\) choices. Quotienting by the direct sum \(R\oplus S\), the residual space \(U/(R\oplus S)\) is a \(t\)-dimensional subspace of \((A/R)\oplus(B/S)\) intersecting either coordinate summand trivially. Its two projections are therefore isomorphisms onto \(t\)-dimensional subspaces of \(A/R\) and \(B/S\). Conversely, choosing those projected subspaces and an invertible map between them determines exactly one such graph, and hence one subcode \(U\). This yields the two remaining Gaussian coefficients times \(|\mathrm{GL}_t(\mathbb F_2)|\). Feasibility and exhaustive coverage of the Grassmannian follow from the same bijection.

**5. Dimension-removal probability.** The full-rank-only dimension-\(m\) subcodes of \(C\) are exactly \(A\) and \(B\), by Step 3. A subcode \(U\) of codimension \(c\ge1\) cannot contain both because they span \(C\). The number of dimension-\((2m-c)\) subspaces containing a prescribed dimension-\(m\) summand equals \({m\brack c}_2\): choose the quotient subspace inside the other \(m\)-dimensional summand. Divide twice that number by the total \({2m\brack c}_2\). For \(c\le m\), the dimension of \(U\) is at least \(m\), so \(\alpha_m(U)\) is defined and, by Step 3, is either \(m\) or \(m-1\). For \(c=1\), evaluate the Gaussian coefficients \({m\brack1}_2=2^m-1\) and \({2m\brack1}_2=2^{2m}-1\) to obtain the stated closed probability and integer counts.

## Verification

The standalone `verify.py` builds binary matrices of the linearized maps directly over polynomial-basis realizations of the extension fields, performs exact binary Gaussian elimination to calculate ranks, and exhaustively checks all coefficient hyperplanes for \(m=2,3,4,5\). In particular it checks the two rank enumerators of hyperplanes in each case, including all \(1023\) hyperplanes at \(m=5\). It separately enumerates *every* binary subspace of the \(2m\)-dimensional coefficient space for \(m=2,3,4\), recovering the population \(N_{m,d}(r,s)\) in every dimension; the total numbers of subspaces are \(67\), \(2825\), and \(417199\), respectively. For \(m\le3\), it additionally checks the rank enumerator of each subcode directly from its nonzero elements and confirms that exactly two dimension-\(m\) subspaces have all nonzero elements of full rank. The run terminates with `VERIFY_OK`; its exact output is supplied as `verification_output.txt`. These finite checks are independent sanity checks, not the proof of the quantified statements for all \(m\).

## Relationship to prior work

Alfarano, Pratihar and Vinçotte [1] establish bounds on subcode-distance changes under Add-and-Remove operations on Gabidulin codes. Their Proposition 4 computes the original Gabidulin subcode distances; Corollary 9 identifies the exceptional indices at which one removed binary dimension can reduce them, and Example 13 exhibits both behaviors for one \(3\times3\) instance. They do not give a dimension-uniform frequency formula, the population of arbitrary binary subcodes by all rank spectra, or their complete subcode-distance profiles. The present theorem studies subcodes *before any added outside space*; it must not be interpreted as an assertion for arbitrary Add-and-Remove outputs with positive addition dimension.

Camps-Moreno, Gorla and López [2] introduce subcode distances and derive their values for parent Gabidulin codes, but do not enumerate ranks or subcode distances of their arbitrary binary subcodes. Gabidulin and Loidreau [3] study *subspace subcodes* formed by restricting each codeword coordinate to a specified alphabet subspace; this is a different restriction from choosing an arbitrary \(\mathbb F_2\)-linear subspace of the Gabidulin code. The Gaussian-binomial graph count in Step 4 uses standard finite linear algebra, but the identification of the only full-rank words and the complete joint coding-theoretic census are not among the results identified in these references.

## Limitations

The classification is restricted to the binary base field, degree-two square Gabidulin codes, and arbitrary linear subcodes of those codes. For larger base fields, coefficient pairs with both entries nonzero can have full rank; the binary rank dichotomy no longer applies. The theorem does not classify codes obtained by adding an external space, quantify any decoding complexity or cryptographic distinguishability, or assert a new construction of MRD codes. A literature search cannot rule out equivalent coverage in unindexed publications or an implicit formulation of this census in older finite-geometry results. Verification here consists of a mathematical proof and reproducible finite sanity checks.

## References

1. G. N. Alfarano, R. Pratihar, A. Vinçotte, *Code distances of matrix rank-metric codes under Add-and-Remove transformations*, first public October 2, 2026, arXiv:2610.03460, especially Proposition 4, Corollary 9 and Example 13.
2. E. Camps-Moreno, E. Gorla, H. H. López, *Code distances: a new family of invariants of linear codes*, first public September 19, 2025, arXiv:2509.16424, especially Section 3.2.
3. E. M. Gabidulin, P. Loidreau, *Properties of subspace subcodes of optimum codes in rank metric*, first public July 25, 2006, arXiv:cs/0607108, especially Sections 1–2 (journal development: *Properties of subspace subcodes of Gabidulin codes*, Advances in Mathematics of Communications 2 (2008), 147–157).
