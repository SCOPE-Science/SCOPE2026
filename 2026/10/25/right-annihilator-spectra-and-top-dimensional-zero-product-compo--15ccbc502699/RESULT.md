# Right-annihilator spectra and top-dimensional zero-product components of triangular matrix algebras

## Finding
Let \(\mathbb F_q\) be any finite field and \(T_n(\mathbb F_q)\) the algebra of upper-triangular \(n\times n\) matrices, \(n\ge1\). Put \(m=n(n+1)/2\), and for \(A\in T_n\) let \(h(A)=\dim_{\mathbb F_q}\{B\in T_n:AB=0\}\). The polynomial \(\Phi_{n,q}(T)=\sum_{A\in T_n}T^{h(A)}\) is given for every \(n\) and \(q\) by an explicit positive rank-profile formula and a two-index recurrence below.

For a subset \(P\subseteq\{1,\dots,n\}\), put \(k_0=0\), \(k_j=|P\cap\{1,\dots,j\}|\), and
\[
 w_j(P)=\begin{cases}
 q^{j-1-k_{j-1}},&j\in P,\\
 q^j-q^{j-1-k_{j-1}},&j\notin P.
 \end{cases}
\]
Then the **complete right-annihilator spectrum** is
\[
 \boxed{\Phi_{n,q}(T)=\sum_{P\subseteq[n]}\left(\prod_{j=1}^nw_j(P)\right)T^{\sum_{p\in P}(n-p+1)}.}
\]
Consequently, the exact number of ordered zero-product pairs (including zero factors) is \(Z_n(q)=\Phi_{n,q}(q)\).

Over an algebraically closed field \(K\), the variety
\[
 X_n(K)=\{(A,B)\in T_n(K)^2:AB=0\}
\]
has dimension exactly
\[
 \boxed{\dim X_n=\frac{n(n+1)}2+\left\lfloor\frac{n^2}4\right\rfloor.}
\]
The number of its top-dimensional **geometrically irreducible** components is exactly one for even \(n\) and two for odd \(n\). No assertion is made about the number of lower-dimensional components or the scheme's nilpotent structure.

## Assumptions and scope
The point counts hold over every finite field, including nonprime extension fields and characteristic two. The geometric assertions concern the reduced underlying algebraic set over an algebraic closure of an arbitrary field. Products are literal ordered matrix products \(AB\), not commutators. \(h(A)\) includes the zero annihilator element. The standard zero-divisor digraph, which normally omits zero and may omit loops, is a different normalization from the full zero-product relation counted here.

## Proof
**1. Prefix nullities control right annihilators.** For \(1\le j\le n\), denote by \(A_j\) the leading principal \(j\times j\) submatrix of \(A\), with \(k_j(A)=j-\operatorname{rank}(A_j)\). The \(j\)-th column of any upper-triangular \(B\) is an arbitrary vector supported in its first \(j\) entries. Its column in \(AB\) vanishes exactly when the corresponding vector belongs to \(\ker A_j\). Columns of \(B\) are independent. Hence
\[
 \boxed{h(A)=\sum_{j=1}^n k_j(A).}
\]

**2. Every nullity jump is zero or one, with exact field counts.** Write the next principal block as
\[
 A_j=\begin{pmatrix}A_{j-1}&v\\0&a\end{pmatrix}.
\]
If \(\dim\ker A_{j-1}=k\), then \(\operatorname{rank}(A_{j-1})=j-1-k\). If \(a=0\) and \(v\in\operatorname{im}(A_{j-1})\), the rank stays constant and the nullity increases from \(k\) to \(k+1\). There are exactly \(q^{j-1-k}\) choices of \((v,a)\) realizing this jump. Every other choice increases the rank by one and keeps the nullity at \(k\); there are exactly \(q^j-q^{j-1-k}\) such choices. Induction over columns therefore yields the positive product formula, with \(P\) recording the positions at which nullity increases. Each such increase at position \(p\) contributes one to every subsequent nullity, so \(\sum_jk_j=\sum_{p\in P}(n-p+1)\).

Equivalently, define \(G_{0,0}(T)=1\), \(G_{0,k}(T)=0\) for \(k\ne0\), and set all out-of-range \(G\)'s to zero. For \(j\ge1\) and \(0\le k\le j\),
\[
 \boxed{G_{j,k}(T)=T^k\bigl[(q^j-q^{j-1-k})G_{j-1,k}(T)+q^{j-k}G_{j-1,k-1}(T)\bigr],}
\]
where the first summand is used only for \(k\le j-1\). Then \(\Phi_{n,q}(T)=\sum_{k=0}^nG_{n,k}(T)\). This is an exact dynamic program on \(O(n^2)\) states, with polynomial coefficients (or it can be evaluated numerically at \(T=q\)).

**3. Geometric rank-profile strata.** Over an algebraically closed field \(K\), fix the set \(P\) of jumps. It defines a locally closed stratum \(S_P\) in the affine space of upper-triangular \(A\). Inductively, when nullity increases, the fiber over the preceding stratum is the vector bundle \(a=0\), \(v\in\operatorname{im}(A_{j-1})\), of relative dimension \(j-1-k\). When nullity stays constant, the fiber is the nonempty Zariski-open complement of this subbundle in affine \(j\)-space, of relative dimension \(j\). The image of a constant-rank matrix family is a vector subbundle, so the induction is valid over the whole prior stratum. Thus every \(S_P\) is geometrically irreducible.

Writing \(r=|P|\), the dimension accumulated for \(A\) is
\[
 \sum_{j\notin P}j+\sum_{j\in P}(j-1-k_{j-1})
 =m-\sum_{s=1}^{r}s=m-\frac{r(r+1)}2.
\]
The solutions \(B\) of \(AB=0\) above \(S_P\) form a kernel vector bundle of constant rank \(h_P=\sum_{p\in P}(n-p+1)\). The corresponding stratum \(X_P\subseteq X_n\) is therefore irreducible of dimension
\[
 d_P=m-\frac{r(r+1)}2+\sum_{p\in P}(n-p+1).
\]
For fixed \(r\), this expression is uniquely maximal when \(P=\{1,\dots,r\}\), yielding \(d_P=m+r(n-r)\). The integer \(r(n-r)\) is maximized precisely at \(r=\lfloor n/2\rfloor\) and \(r=\lceil n/2\rceil\), coinciding for even \(n\). Because the \(X_P\) form a finite disjoint stratification by irreducible locally closed subsets, closures of the maximal-dimensional strata are exactly all top-dimensional irreducible components. This proves both geometric assertions.

**4. Leading term of zero-product count.** Each \(w_j(P)\) is a monic polynomial in \(q\) of degree \(j\) for \(j\notin P\), and a monomial of degree \(j-1-k_{j-1}\) for \(j\in P\). Hence the summand of \(Z_n(q)\) indexed by \(P\) is monic of degree \(d_P\). Exactly one (even \(n\)) or two (odd \(n\)) subsets attain the maximum. Thus \(Z_n(q)\) is a polynomial with leading term \(q^{m+\lfloor n^2/4\rfloor}\) for even \(n\), and \(2q^{m+\lfloor n^2/4\rfloor}\) for odd \(n\). This is a direct finite-field check on the geometric count, not the sole proof of it.

## Verification
The accompanying standalone program `verify.py` directly enumerates the upper-triangular matrices and independently computes prefix ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), with literal zero-product pair enumeration in smaller instances. It checks the complete distribution for nine field-and-size instances, including \(n=5\) over \(\mathbb F_2\), and separately checks the predicted leading degree and coefficient for \(1\le n\le40\). Run `python3 verify.py`. Expected final line: `VERIFY_OK_TRIANGULAR_ZERO_PRODUCTS 9_FINITE_CASES 40_TOP_DEGREES`.

For example, \(\Phi_{2,2}(T)=2+2T+3T^2+T^3\), and \(Z_2(2)=26\). For \(n=3\), \(q=2\), \(Z_3(2)=632\); for \(n=4\), \(q=2\), \(Z_4(2)=42560\). Direct symbolic evaluation gives \(Z_2(q)=q(q^3+3q^2-4q+1)\). Finite verification is not used as a proof of the all-dimensional statements.

## Relationship to prior work
Li Bingjun (2011) studies zero-divisor graphs for triangular matrix rings and their diameters and girths; its fully inspected six-page article introduces both left and right annihilators but does not give the present field-dependent, all-size annihilator profile enumerator or the geometry of the zero-product pair variety. Li and Tucci (2013) discuss the same rings' directed zero-divisor graphs and provide bounds on edges, with an exact edge count for size two; only the abstract and publicly visible description of the 2013 article were accessible here, so implicit stronger coverage in its full text remains a priority risk. Wong, Ma and Zhou (2014) investigate automorphisms of the rank-one induced graph; these do not furnish the all-rank zero-product distribution. Lakshmibai (2000) analyzes varieties of unrestricted composable linear maps with zero product, not the simultaneous upper-triangular flag constraints used here. These structural distinctions, not differences of wording, motivate the originality assessment.

## Limitations
This is not a calculation of the standard simple zero-divisor graph's degree sequence: removing zero and removing loops requires accounting for square-zero elements separately. It does not classify lower-dimensional irreducible components, nilpotent scheme structure, or left-and-right annihilator *joint* distributions. The relevant Li–Tucci article was not inspected in full; consequently historical-priority confidence is provisional. The named computational checks cover finite instances and do not establish an infinite theorem independently.

## References
1. Li Bingjun, “Zero-Divisor Graph of Triangular Matrix Rings over Commutative Rings,” *International Journal of Algebra* 5 (2011), 255–260; open-access full text: https://www.m-hikari.com/ija/ija-2011/ija-5-8-2011/libIJA5-8-2011.pdf . The publisher gives publication year, not a day-precise public release date.
2. A. Li and R. P. Tucci, “Zero Divisor Graphs of Upper Triangular Matrix Rings,” *Communications in Algebra* 41 (2013), 4622–4636; published online 2013-09-20; https://doi.org/10.1080/00927872.2012.706841 .
3. D. Wong, X. Ma and J. Zhou, “The group of automorphisms of a zero-divisor graph based on rank one upper triangular matrices,” *Linear Algebra and its Applications* 460 (2014), 242–258; https://doi.org/10.1016/j.laa.2014.07.041 .
4. V. Lakshmibai, “Singular loci of varieties of complexes,” *Journal of Pure and Applied Algebra* 152 (2000), 217–230; https://doi.org/10.1016/S0022-4049(99)00144-9 .
