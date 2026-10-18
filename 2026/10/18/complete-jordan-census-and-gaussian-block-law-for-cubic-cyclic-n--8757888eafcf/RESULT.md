# Complete Jordan census and Gaussian block law for cubic cyclic Nakayama algebras

## Finding
For every prime power \(q\) and integer \(n\geq3\), let \(Q_n\) be the quiver with arrows \(a_i:i\to i+1\), where indices are in \(\mathbb Z/n\mathbb Z\). Let \(A_{n,q}=\mathbb F_q Q_n/J^3\), with \(J\) its arrow ideal. For each \(u\in J\), let \(L_u:A_{n,q}\to A_{n,q}\) be left multiplication, and let \(A(u),B(u),C(u)\) count canonical three-dimensional path-endpoint summands whose Jordan types are \((3)\), \((2,1)\), and \((1,1,1)\), respectively, as described below. In particular, the Jordan form of \(L_u\) is
\[
(3^{A(u)},\,2^{B(u)},\,1^{B(u)+3C(u)}),\qquad A(u)+B(u)+C(u)=n.
\]
The **complete** Jordan census, including the multiplicities of all such partitions, is the coefficient extraction from
\[
\boxed{\displaystyle
\Phi_{n,q}(U,V,W):=\sum_{u\in J}U^{A(u)}V^{B(u)}W^{C(u)}
=\operatorname{tr}\!\left(\begin{array}{cc}
W+(q-1)V&qV\\q(q-1)V&q(q-1)U
\end{array}\right)^n.}
\]
In particular, \(\Phi_{n,q}(1,1,1)=q^{2n}\), and the rank pair of \(L_u\) and its square is \((2A(u)+B(u),A(u))\). The multiplicity \(A(u)=n-1\) never occurs, whereas each of \(0,1,\ldots,n-2,n\) occurs.

There is also a quantitative limit theorem. Put \(r=q^{-1}\) and \(p=1-r\). If \(u\) is uniform on \(J\), then
\[
\mathbb E[A(u)]=np^2,\qquad \mathbb E[C(u)]=nr^3,
\]
and, for fixed \(q\) as \(n\to\infty\),
\[
\frac{1}{\sqrt n}\binom{A(u)-np^2}{C(u)-nr^3}
\ \Longrightarrow\ N_2(0,\Sigma_q),\quad
\Sigma_q=\begin{pmatrix}
p^2r(1+3p)&-3p^2r^3\\
-3p^2r^3&r^3+2r^5-3r^6
\end{pmatrix}.
\]
This covariance matrix is nondegenerate, with \(\det\Sigma_q=p^3r^4(r+4)>0\). The third block statistic is recovered from \(B=n-A-C\), so the bivariate limit determines the full three-component fluctuation law.

Finally, if \(\lambda_\pm=(1\pm\sqrt{4q-3})/2\), then
\[
\Pr(L_u^2=0)=q^{-n}(\lambda_+^n+\lambda_-^n),
\]
which decays exponentially for every fixed \(q\). This is an exact formula for the event that no three-dimensional Jordan block appears.

## Assumptions and scope
The field is any \(\mathbb F_q\), including extension fields and characteristic two. The quiver is **cyclically oriented**, with exactly one arrow at each vertex, and \(n\ge3\). Products of paths are concatenated from left to right when the terminal vertex of the first equals the initial vertex of the second; all paths of length three vanish. Here \(J\) is the Jacobson radical in \(A_{n,q}\), \(\dim_{\mathbb F_q}A_{n,q}=3n\), and \(\dim_{\mathbb F_q}J=2n\). Only multiplication operators \(L_u\) for \(u\in J\) are counted, not arbitrary nilpotent endomorphisms or all elements of the algebra. The central-limit statement takes \(n\to\infty\) with \(q\) fixed.

## Proof
**Endpoint block decomposition.** For every \(i\in\mathbb Z/n\mathbb Z\) set \(b_i=a_i a_{i+1}\). The paths \(e_i,a_i,b_i\) (all \(i\)) form a basis, and the path-endpoint spaces
\[
B_i=\operatorname{span}_{\mathbb F_q}\{e_{i+2},a_{i+1},b_i\}
\]
are pairwise disjoint with direct sum \(A_{n,q}\). Every radical element is uniquely
\[
u=\sum_{i}(x_i a_i+y_i b_i),\qquad x_i,y_i\in\mathbb F_q.
\]
By path concatenation, \(L_u\) preserves every \(B_i\) and, on the ordered basis above, has matrix
\[
M_i=\begin{pmatrix}0&0&0\\x_{i+1}&0&0\\y_i&x_i&0\end{pmatrix},\qquad
M_i^2=\begin{pmatrix}0&0&0\\0&0&0\\x_ix_{i+1}&0&0\end{pmatrix}.
\]
Therefore \(M_i\) is one Jordan block of size three if both \(x_i,x_{i+1}\) are nonzero; it has Jordan type \((1,1,1)\) precisely if \(x_i=x_{i+1}=y_i=0\); and it has Jordan type \((2,1)\) otherwise. The block and rank statements follow immediately. The condition \(A=n-1\) is impossible: one zero among the cyclic \(x_i\) destroys two adjacent nonzero-pair edges, while no zero gives \(A=n\). For every \(0\le a\le n-2\), a run of \(a+1\) consecutive nonzero \(x_i\) with the other \(x_i\) zero realizes \(A=a\).

**Transfer matrix.** Let \(s_i\in\{0,1\}\) indicate whether \(x_i\ne0\). When \((s_i,s_{i+1})=(0,0)\), the \(y_i\) choices contribute \(W+(q-1)V\). For \((0,1)\) they contribute \(qV\), for \((1,0)\) they contribute \(q(q-1)V\), and for \((1,1)\) they contribute \(q(q-1)U\). In each transition, the factor \(q-1\) for a nonzero \(x_i\) is charged once, on its outgoing transition. Multiplying around the labeled cycle and summing all cyclic state sequences is precisely the stated matrix trace. At \(U=V=W=1\) its transfer matrix has eigenvalues \(q^2\) and \(0\), giving \(q^{2n}\) as required.

**Exact absence of size-three blocks.** The condition \(A=0\) means that the support of \((x_i)\) is an independent set in the cycle. There are \(\sum_{S\text{ independent}}(q-1)^{|S|}\) such \(x\)-tuples, and each allows \(q^n\) choices of \(y\). The weighted independence polynomial is the trace of the \(n\)-th power of \(\left(\begin{smallmatrix}1&1\\q-1&0\end{smallmatrix}\right)\), whose eigenvalues are \(\lambda_\pm\). Dividing by \(|J|=q^{2n}\) proves the probability formula. Since \(|\lambda_-|<\lambda_+<q\), its right-hand side decays exponentially.

**Gaussian fluctuations.** For uniform \(u\), let \(S_i=\boldsymbol1_{x_i\ne0}\) and \(Z_i=\boldsymbol1_{y_i=0}\). All coordinates are independent, with \(\Pr(S_i=1)=p\) and \(\Pr(Z_i=1)=r\). Then
\[
A=\sum_i S_iS_{i+1},\quad C=\sum_i(1-S_i)(1-S_{i+1})Z_i.
\]
The centered summands are stationary and depend only on neighboring independent coordinates. All cross-covariances beyond distance one vanish. The variance and covariance calculation gives, for every \(n\ge3\),
\[
\operatorname{Cov}\binom{A}{C}=n\Sigma_q.
\]
For example, adjacent \(A\)-summands have covariance \(p^3(1-p)\), adjacent \(C\)-summands have covariance \(r^5(1-r)\), and each \(A\)-summand has zero product with precisely three overlapping \(C\)-summands, yielding the off-diagonal \(-3p^2r^3\). A finite-range central-limit argument proves the claimed convergence: cut the cycle at one location, partition the remaining centered local summands into blocks of length \(\lfloor n^{1/3}\rfloor\) separated by one discarded location, and apply the independent-block Lindeberg theorem. The discarded terms have variance \(O(n^{2/3})=o(n)\), while each retained block is uniformly \(O(n^{1/3})=o(\sqrt n)\). Cramér–Wold yields the joint limit. Direct algebra simplifies the covariance determinant to \(p^3r^4(r+4)>0\), establishing nondegeneracy.

## Verification
A standalone verifier, `nakayama_jordan_check.py`, constructs the entire truncated cyclic path algebra over prime fields, forms each left-multiplication matrix from path concatenation (rather than from the asserted block formula), calculates the ranks of the first two matrix powers by finite-field Gaussian elimination, and compares the resulting complete Jordan census with independently multiplied polynomial transfer matrices. It exhaustively checks \((q,n)=(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\), comprising \(12{,}730\) radical elements, and tests \(256\) pseudorandom elements each for \((5,3),(5,4),(7,3),(3,7)\). Its final line is `ALL_TRUNCATED_CYCLIC_JORDAN_CHECKS_PASSED`. For example,
\[
\Phi_{3,2}=W^3+3VW^2+15V^2W+13V^3+24UV^2+8U^3.
\]
Independent coefficient checks also verified the exact means and covariances in several small cases. The proof, not finite enumeration, establishes the all-prime-power and infinite-\(n\) assertions. Run the standalone script with a standard Python 3 interpreter; it uses only the standard library.

## Relationship to prior work
Gao and Schiffler [1] study the same radical-power quotients of cyclic Nakayama path algebras and prove recurrences for \(\tau\)-tilting and support \(\tau\)-tilting modules. Their results establish natural motivation for this algebra family, but concern module-class counts rather than Jordan types of left multiplication by individual radical elements. Bergh, Erdmann, and Jorgensen [2] develop constant-Jordan-type representation theory over quantum complete intersections; their algebra family and quantifiers differ and their results do not supply this finite-field elementwise cycle census. Fuchs and Kirillov [3] count Jordan types among **all** strictly triangular matrices over finite fields; their unrestricted matrix counts do not isolate the algebraically constrained left-regular multiplication image considered here. Dequêne [4] studies generic nilpotent endomorphisms of representations of linearly oriented \(A\)-type quivers over algebraically closed fields, not this finite-field census for a cyclic monomial algebra. The transfer-matrix and finite-range-probability principles themselves are standard; the claim is their explicit algebraic application, complete all-element Jordan distribution, and nondegenerate covariance law.

## Limitations
No novelty claim is made for the path-algebra definition, three-dimensional Jordan classification, transfer-matrix technique, independent-set polynomial, or finite-range central-limit theorem in isolation. The theorem applies specifically to length-three cyclic Nakayama algebras and the left-regular multiplication of their radicals. It does not classify similarity or automorphism orbits of the radical, nor does it treat arbitrary nilpotent endomorphisms or all radical truncation orders. Equivalent formulas may occur in unindexed literature on random monomial-algebra elements. The tests concern prime fields, but the proof uses only field cardinality and is valid over all finite fields. Historical priority is not established by these literature comparisons.

## References
1. H. Gao and R. Schiffler, *On the Number of \(\tau\)-Tilting Modules over Nakayama Algebras*, SIGMA 16 (2020), 058; first arXiv version 2020-02-07, arXiv:2002.02990. https://arxiv.org/abs/2002.02990
2. P. A. Bergh, K. Erdmann, and D. A. Jorgensen, *Modules of Constant Jordan Type over Quantum Complete Intersections*, Documenta Mathematica 25 (2020), 1541–1570; arXiv:1910.06714. https://arxiv.org/abs/1910.06714
3. D. Fuchs and A. Kirillov, *Jordan Types of Triangular Matrices over a Finite Field*, Arnold Mathematical Journal 8 (2022), 543–559; arXiv:2204.00066. https://arxiv.org/abs/2204.00066
4. B. Dequêne, *Canonically Jordan Recoverable Categories for Modules over the Path Algebra of \(A_n\) Type Quivers*, arXiv:2308.16626 (2023). https://arxiv.org/abs/2308.16626
