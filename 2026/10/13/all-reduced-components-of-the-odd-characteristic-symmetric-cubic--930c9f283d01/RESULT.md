# All reduced components of the odd-characteristic symmetric-cubic critical locus

## Finding
Let \(K\) be an algebraically closed field of odd characteristic \(p\), and let \(n\ge3\). Define
\[
e_3(x_1,\ldots,x_n)=\sum_{1\le i<j<k\le n}x_ix_jx_k,
\qquad I=(\partial_1e_3,\ldots,\partial_ne_3)\subset K[x_1,\ldots,x_n].
\]
For every nonempty \(S\subseteq[n]\), denote by \(L_S\) the one-dimensional linear subspace where \(x_i=a\) for \(i\in S\), and \(x_j=0\) otherwise. For every proper nonempty \(S\), denote by \(P_S=P_{S^c}\) the two-dimensional linear subspace where \(x_i=a\) on \(S\), and \(x_j=b\) on \(S^c\).

**Theorem (all minimal primes, arbitrary odd characteristic).** The following are irredundant decompositions into distinct irreducible linear components:

* If \(n\not\equiv2\pmod p\), then
  \[
  V(\sqrt I)=\bigcup_{\substack{\varnothing\ne S\subseteq[n]\\ |S|\equiv1\; (\mathrm{mod}\;p)}}L_S,
  \qquad \#\operatorname{Irr}(V(I))=\sum_{\substack{1\le m\le n\\ m\equiv1\; (\mathrm{mod}\;p)}}\binom nm.
  \]
* If \(n\equiv2\pmod p\), then
  \[
  V(\sqrt I)=\bigcup_{\substack{\{S,S^c\}\\1\le|S|<n\\ |S|\equiv|S^c|\equiv1\; (\mathrm{mod}\;p)}}P_S,
  \qquad \#\operatorname{Irr}(V(I))=\frac12\sum_{\substack{1\le m<n\\m\equiv1\; (\mathrm{mod}\;p)}}\binom nm.
  \]
All components are generically smooth in the original critical scheme. Their affine dimensions are, respectively, \(1\) and \(2\). After projectivization, the reduced homogeneous critical locus has the indicated number of reduced points or projective lines, hence projective degree equal to the respective component count.

Equivalently, the first radical is the intersection of the linear ideals \(I(L_S)\) for the indicated subsets, and the second radical is the intersection of the linear ideals \(I(P_S)\) for the indicated bipartitions.

For example, in characteristic \(3\), there are exactly \(5\) line components when \(n=4\), exactly \(5\) plane components when \(n=5\), and exactly \(21\) line components when \(n=6\). Dimension alone cannot distinguish the last case from a single line.

## Assumptions and scope
The base field is algebraically closed and \(p\) is an odd prime. No assumption on \(n\) beyond \(n\ge3\) is imposed. The scheme under study is the *critical scheme of the polynomial*, defined by its gradient. In characteristic \(3\), this need not be the singular scheme of the hypersurface \(e_3=0\): for example, on the characteristic-\(3\), five-variable critical plane \((a,b,b,b,b)\), one has \(e_3=b^3\).

All statements about irreducible components, radicals and projective degrees concern the underlying reduced scheme. They do not assert a global primary decomposition of \(I\), absence of embedded associated primes, or global reducedness.

## Proof
**1. At most two coordinate values.** Write \(e_1=\sum_i x_i\) and \(e_2=\sum_{i<j}x_ix_j\). For each index \(i\), the deletion identity reads
\[
\partial_i e_3=e_2-x_i e_1+x_i^2.
\]
At a common critical point, every coordinate is a root of the *same monic quadratic* \(u^2-e_1u+e_2\). Hence there are at most two distinct coordinate values. This proof works in every odd characteristic and uses no separability assumption.

**2. Two distinct values.** Suppose a critical point has distinct values \(a\ne b\), occurring on complementary blocks of sizes \(m\ge1\) and \(r=n-m\ge1\). Set \(A=m-1\) and \(B=r-1\), regarded as scalars in \(K\). For an index in the \(a\)-block and one in the \(b\)-block, the corresponding derivatives are
\[
G_a=\binom{m-1}{2}a^2+(m-1)r ab+\binom r2 b^2,
\]
\[
G_b=\binom m2 a^2+m(r-1)ab+\binom{r-1}{2}b^2.
\]
Subtracting gives the exact identity
\[
G_a-G_b=(b-a)(Aa+Bb).
\]
Since the point is critical and \(a\ne b\), necessarily \(Aa+Bb=0\). The sum of coordinates outside any specified \(a\)-block index is then \(Aa+rb=b\). Because \(p\ne2\), the elementary sum-of-squares identity for \(G_a\) gives
\[
2G_a=b^2-\bigl(Aa^2+rb^2\bigr)=-Aa^2-Bb^2.
\]
Thus \(Aa^2+Bb^2=0\) as well. Subtracting \(a(Aa+Bb)=0\) and \(b(Aa+Bb)=0\) yields, respectively, \(Bb(b-a)=0\) and \(Aa(a-b)=0\). Since \(a-b\ne0\),
\[
Aa=0,\qquad Bb=0.
\]
If both \(a\) and \(b\) are nonzero, we obtain \(m\equiv r\equiv1\pmod p\), which forces \(n\equiv2\pmod p\). If exactly one is nonzero, its support has size congruent to \(1\pmod p\). Conversely, these conditions give \(G_a=G_b=0\) directly from the formulas, so every specified line or two-block plane lies in the critical locus.

**3. A single coordinate value.** If all coordinates equal \(a\), the derivatives all equal \(\binom{n-1}{2}a^2\). For \(a\ne0\), this vanishes in an odd characteristic precisely when \(n\equiv1\) or \(2\pmod p\). If \(n\equiv1\), this common diagonal is precisely \(L_{[n]}\); if \(n\equiv2\), it lies in every displayed two-block plane. The origin lies in all components. The cases in Steps 2–3 exhaust the entire critical set, proving the two radical equalities by the Nullstellensatz.

**4. Irredundancy and degrees.** Different nonempty supports give distinct lines \(L_S\); equal two-block planes correspond exactly to the unordered pair \(\{S,S^c\}\). Distinct irreducible linear subspaces of the same dimension cannot contain one another. Hence each displayed subspace is a complete irreducible component. The degree of an equidimensional reduced union of projective linear subspaces of degree one is the number of its components. Counting supports and unordered bipartitions gives the stated formulas.

**5. Generic smoothness.** At a point, the Hessian matrix has diagonal entries zero and off-diagonal entry \(\sum_{k\notin\{i,j\}}x_k\). On a generic point \(a\ne0\) of \(L_S\), with \(m=|S|\equiv1\pmod p\) and \(r=n-m\), the mixed Hessian block vanishes, the \(S\)-block is \((m-2)a(J_m-I_m)\), and the complement block is \(ma(J_r-I_r)\). The first block has rank \(m-1\), and if \(r>0\), then \(r\not\equiv1\pmod p\) in the line case, so the second has rank \(r\). If \(r=0\), only the first block occurs. The total Hessian rank is \(n-1\). At a generic point of \(P_S\) with \(a\ne b\) and both block sizes \(1\pmod p\), the mixed Hessian block is zero and the diagonal blocks are \((b-a)(J_m-I_m)\) and \((a-b)(J_r-I_r)\), respectively. Their ranks are \(m-1\) and \(r-1\), giving total rank \(n-2\). The Jacobian criterion then proves generic smoothness in both cases. Here \(J_s\) denotes the all-ones matrix and \(I_s\) the identity matrix of size \(s\).

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The standalone program enumerates all affine points over the prime fields \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\) in the displayed small variable ranges, checks the direct partial derivatives against the predicted supports/bipartitions, checks all component counts, and recomputes the exact Hessian ranks at a representative generic point of each component. It prints `VERIFY_OK`. These finite prime-field tests are corroborating computations and **not** an exhaustive proof over algebraically closed fields; Steps 1–5 supply the proof for every admissible \(p,n\).

## Relationship to prior work
Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1, Theorems 1.1 and 1.3 and Lemmas 2.1–2.2, determines the dimensions of all derivative loci and the two-dimensional extremal components. Thus **the two-block plane classification when \(n\equiv2\pmod p\) is already covered there** and is included only to give a uniform statement. Section 7 explicitly leaves smaller-dimensional components unclassified. The new contribution is the complete irredundant **line-component/radical classification for every \(n\not\equiv2\pmod p\)**, including all non-coordinate diagonal-support lines, their binomial component counts, degrees and generic smoothness. These conclusions do not follow from Xie's dimension statement or classification of extremal components alone.

Orzel, arXiv:2509.05009v3, studies the dimension of the *zero-and-gradient* locus and its computational consequences, not this reduced gradient-only decomposition. Cafure–Matera–Privitelli, arXiv:1109.2265v1, Theorem 3.1 and Remark 3.2, supplies the general bound on distinct coordinate values and containment in partition spaces, not the exact congruence-wise decomposition of this cubic gradient locus. Those earlier inclusions and methods are acknowledged rather than claimed as new.

## Limitations
The theorem does not classify embedded associated primes, the global nilpotent structure of the Jacobian ideal, or the hypersurface's singular scheme. The latter differs from the gradient critical scheme when the characteristic divides the cubic degree. Published results may contain an implicit equivalent special-case radical decomposition; the original-source comparisons did not identify such a statement. 
## References
1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1, September 24, 2026. https://arxiv.org/html/2610.00259v1
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3, first posted September 5, 2025. https://arxiv.org/html/2509.05009v3
3. A. Cafure, G. Matera and M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265v1, 2011. https://arxiv.org/html/1109.2265v1
