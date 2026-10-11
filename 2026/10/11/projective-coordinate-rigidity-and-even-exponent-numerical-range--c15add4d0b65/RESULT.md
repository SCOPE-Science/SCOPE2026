# Projective-coordinate rigidity and even-exponent numerical-range phases for finite-dimensional linear relations

## Finding
Let \(1<p<\infty\), let \(X_p=(\mathbb C^n,\|\cdot\|_p)\), let \(D\subseteq\mathbb C^n\) be a nonzero complex subspace, let \(M\subseteq\mathbb C^n\) be a complex subspace, and let \(A:D\to\mathbb C^n\) be complex linear. The closed linear relation \(T_p\) with graph
\[
G(T_p)=\{(x,Ax+m):x\in D,\ m\in M\}
\]
has either numerical range \(\mathbb C\) or a compact numerical range, independently of the selection \(A\). There is an explicit, complete test for which alternative occurs, including an exact formula for the largest possible dimension of \(M\) in the compact alternative.

Write \(L_i:D\to\mathbb C\) for the restriction of the \(i\)-th coordinate functional and let
\[
\Phi_p(z)=|z|^{p-2}\overline z,\qquad \Phi_p(0)=0.
\]
Define the complex linear subspace
\[
\mathcal N_p(D)=\left\{m\in\mathbb C^n:\sum_{i=1}^n m_i\Phi_p(L_i(x))=0\text{ for every }x\in D\right\}.
\]
Then \(W_p(T_p)\) is compact if and only if \(M\subseteq\mathcal N_p(D)\); otherwise \(W_p(T_p)=\mathbb C\). In the compact case it is precisely
\[
W_p(T_p)=\left\{\frac{\sum_{i=1}^n\Phi_p(x_i)(Ax)_i}{\|x\|_p^p}:x\in D\setminus\{0\}\right\}.
\]

**Non-even exponents.** Assume \(p\notin\{2,4,6,\ldots\}\). Partition the nonzero functionals among \(L_1,\ldots,L_n\) into projective classes, two indices belonging to the same class exactly when their restrictions to \(D\) are nonzero proportional complex-linear forms. In each class \(C\), choose a nonzero representative \(\ell_C\) and write \(L_i=a_i\ell_C\) for \(i\in C\). Then
\[
\mathcal N_p(D)=\left\{m:\sum_{i\in C}|a_i|^{p-2}\overline{a_i}m_i=0\ \text{for every class }C\right\}.
\]
Coordinates with identically zero restriction are unconstrained. In particular, if there are \(r\) nonzero projective classes, then
\[
\boxed{\dim_{\mathbb C}\mathcal N_p(D)=n-r.}
\]
Thus the maximal possible dimension of a multivalued part with compact numerical range is exactly \(n-r\).

**Even exponents.** For \(p=2j\), \(j\ge1\), choose a complex basis of \(D\), write \(L_i(z)=\sum_{s=1}^d b_{is}z_s\), and form the finite coefficient matrix \(C_j(D)\) whose row indexed by multiindices \((\alpha,\beta)\) with \(|\alpha|=j-1\), \(|\beta|=j\), and column \(i\), is the coefficient of \(z^\alpha\overline z^\beta\) in
\[
(L_i(z))^{j-1}(\overline{L_i(z)})^{j}.
\]
Then
\[
\boxed{\dim_{\mathbb C}\mathcal N_{2j}(D)=n-\operatorname{rank}_{\mathbb C}C_j(D).}
\]
The rank is basis independent. The matrix has at most
\[
\binom{d+j-2}{j-1}\binom{d+j-1}{j}
\]
rows, even when all nonzero coordinate restrictions are projectively distinct.

**Exact phase examples.** For every integer \(k\ge1\), set \(n=2k+1\),
\[
D_k=\{(z+i w)_{i=0}^{2k}:z,w\in\mathbb C\},\qquad
m^{(k)}_i=(-1)^i\binom{2k}{i},\qquad M_k=\mathbb C m^{(k)},
\]
where the coordinate index \(i\) denotes an integer (not the imaginary unit), and define the zero-selection relation \(R_{k,p}\) by \(G(R_{k,p})=D_k\times M_k\) on \(\ell_p^{2k+1}(\mathbb C)\). Its numerical range is exactly
\[
\boxed{W_p(R_{k,p})=\{0\}\quad\Longleftrightarrow\quad p\in\{2,4,\ldots,2k\};}
\]
for every other real \(1<p<\infty\) it is \(\mathbb C\). For \(k\ge2\), this same closed relation has spectrum \(\mathbb C\) at *all* exponents, including those with numerical range \(\{0\}\); hence the adjoint numerical-range term in the spectral-inclusion theorem for relations cannot generally be discarded.

## Assumptions and scope
The underlying scalars are complex. Numerical range means the normalized-duality-mapping numerical range for linear relations:
\[
W_p(T)=\left\{\frac{x^*(y)}{\|x\|_p^2}:(x,y)\in G(T),\ x\ne0,\ x^*\in J_{X_p}(x)\right\},
\quad J_{X_p}(x)=\{x^*:\|x^*\|=\|x\|_p,\ x^*(x)=\|x\|_p^2\}.
\]
Here \(n\ge1\), \(D\ne\{0\}\), and \(1<p<\infty\). No relation between \(D\), \(M\), or \(A\) is presumed. The coordinate formula is intrinsically tied to the standard \(\ell_p\) norm and does not assert an analogue for arbitrary equivalent norms or endpoints \(p=1,\infty\). A zero coordinate functional means \(L_i=0\) on all of \(D\).

## Proof
**1. Duality reduction and the exhaustive alternatives.** The unique normalized norming functional of nonzero \(x\in X_p\) is
\[
x^*(y)=\|x\|_p^{2-p}\sum_{i=1}^n\Phi_p(x_i)y_i.
\]
It follows that a fixed pair \((x,Ax+m)\) contributes
\[
\frac{\sum_i\Phi_p(x_i)(Ax)_i}{\|x\|_p^p}
+\frac{\sum_i\Phi_p(x_i)m_i}{\|x\|_p^p}.
\]
If some \(x\in D\setminus\{0\}\) and \(m\in M\) make the second numerator nonzero, the admissibility of all \(\mu m\), \(\mu\in\mathbb C\), implies \(W_p(T_p)=\mathbb C\). Otherwise that numerator vanishes identically, exactly when \(M\subseteq\mathcal N_p(D)\), and the stated compact-case formula results. The unit sphere of finite-dimensional \(D\) is compact and the displayed scalar function is continuous on it; hence its range is compact. This also proves that the alternative is independent of \(A\).

**2. Independence of the nonpolynomial duality profiles.** Let \(V\) be a complex vector space of dimension at least two, and let \(\ell_1,\ldots,\ell_r\) be nonzero, pairwise nonproportional complex-linear forms. If \(p>1\) is not an even integer, the functions \(x\mapsto\Phi_p(\ell_s(x))\) are complex-linearly independent. Indeed, suppose \(\sum_s c_s\Phi_p(\ell_s(x))\equiv0\). Fix \(s\). There is a point \(x_0\in\ker\ell_s\) such that \(\ell_t(x_0)\ne0\) for every \(t\ne s\): a finite union of proper complex-linear subspaces cannot cover \(\ker\ell_s\). Choose \(h\in V\) with \(\ell_s(h)=1\), and set \(x=x_0+th\) for real \(t\) near zero. Each \(\Phi_p(\ell_t(x))\), \(t\ne s\), is real analytic in the real parameter near zero because its argument stays nonzero. The remaining term is \(c_s\operatorname{sgn}(t)|t|^{p-1}\), which is not real analytic at zero unless \(p\) is a positive even integer. Thus \(c_s=0\). Repeat for every \(s\). In dimension one all nonzero forms are proportional and the sole profile is nonzero, giving the same conclusion.

Group the nonzero \(L_i\) projectively. Homogeneity gives \(\Phi_p(a_i\ell_C(x))=|a_i|^{p-2}\overline{a_i}\Phi_p(\ell_C(x))\). The independence just proved shows that \(m\in\mathcal N_p(D)\) if and only if all groupwise equations in the finding hold. Those equations have independent supports and nonzero coefficients, so they have rank \(r\). This proves the exact dimension formula, including all zero restrictions.

**3. Polynomial duality at even exponents.** If \(p=2j\), then \(\Phi_{2j}(L_i(z))=(L_i(z))^{j-1}(\overline{L_i(z)})^j\). Expanding into monomials \(z^\alpha\overline z^\beta\) produces the matrix \(C_j(D)\). A complex polynomial in \(z\) and \(\overline z\) that vanishes for all \(z\in\mathbb C^d\) has all coefficients zero (for example, apply independent Wirtinger derivatives at the origin). Therefore \(m\in\mathcal N_{2j}(D)\) exactly when \(C_j(D)m=0\), and rank-nullity proves the formula. The row bound counts the monomials of bidegree \((j-1,j)\). Changing the basis of \(D\) acts invertibly on this polynomial space and hence does not change rank.

**4. Exact exceptional exponent sets.** The coordinate forms \(z+i w\), indexed by \(0\le i\le2k\), are nonzero and pairwise projectively distinct. If \(p\) is not even, Step 2 says \(\mathcal N_p(D_k)=\{0\}\), so \(m^{(k)}\notin\mathcal N_p(D_k)\) and \(W_p(R_{k,p})=\mathbb C\). For \(p=2j\) with \(j\le k\), the expression
\[
(z+i w)^{j-1}(\overline z+i\overline w)^j
\]
is a polynomial in the integer variable \(i\) of degree at most \(2j-1<2k\). Its \(2k\)-th binomial finite difference vanishes, which reads
\[
\sum_{i=0}^{2k}(-1)^i\binom{2k}{i}(z+i w)^{j-1}(\overline z+i\overline w)^j=0.
\]
Thus \(M_k\subseteq\mathcal N_{2j}(D_k)\), and the zero selection gives \(W_{2j}(R_{k,2j})=\{0\}\). Conversely, for \(j>k\), choose \(z=w=1\). The same sum is
\[
\sum_{i=0}^{2k}(-1)^i\binom{2k}{i}(1+i)^{2j-1},
\]
which equals the \(2k\)-th forward finite difference of \(t\mapsto(1+t)^{2j-1}\) at zero. It is strictly positive because the \(2k\)-th derivative is positive for \(t\ge0\). Hence the multivalued part is detected and the numerical range is \(\mathbb C\). This completes the iff statement for every real \(p>1\).

**5. Spectral boundary.** Each \(R_{k,p}\) is closed because its graph is a product of finite-dimensional subspaces. For every scalar \(\lambda\), the range of \(R_{k,p}-\lambda I\) is contained in \(M_k+D_k\), a space of dimension at most three. When \(k\ge2\) the ambient dimension \(2k+1\ge5\), so the relation is never surjective and has spectrum all of \(\mathbb C\). This does not contradict spectral inclusion with the adjoint relation, and precisely illustrates why its adjoint term is necessary.

## Verification
The analytic argument proves the classifications for all allowed dimensions and exponents. The accompanying standalone script `verify_finite_difference.py` checks the symbolic bidegree finite-difference identities for \(1\le k\le6\) and \(1\le j\le k\), exact strict positivity for selected \(j>k\), and diagnostic non-even samples. Execute from the directory containing the script with `python verify_finite_difference.py` (Python 3 with SymPy). Successful output is `FINITE_DIFFERENCE_RELATION_EXACT_TESTS_OK`. These finite checks are consistency tests, not substitutes for the independence or all-order finite-difference proofs.

## Relationship to prior work
Boubaker, Gernandt and Selmi (2026), Definition 3.1 and Theorem 3.3, introduce the Banach-space numerical range of a linear relation and prove the compact-or-full-plane dichotomy for finite-dimensional domains. That dichotomy and the numerical-range definition are prior input, not claimed as new. Their Theorem 3.4 already shows why the adjoint may be needed in spectral inclusion. The new contribution is the complete \(\ell_p\)-coordinate classification of allowable multivalued parts, its dimension formulas for every exponent, and the precise exceptional-exponent family.

Known ridge-function uniqueness theory (Pinkus, 2015, Chapter 3) and earlier \(L_p\) even-exponent phenomena (Randrianantoanina, 1997) are pertinent conceptual precedents. Neither inspected source states the numerical-range coefficient and rank tests above or the exact finite-difference phase family. The elementary independence lemma is not asserted to be new as a stand-alone ridge-function theorem.

## Limitations
The classification is finite-dimensional and complex, with \(1<p<\infty\). The source paper already implies the compact/full-plane dichotomy; no novelty is assigned to that fact. The polynomial matrix may have redundant rows; the rank, not the row bound, is exact. The binomial construction does not classify all possible exceptional-exponent sets for arbitrary relations. Full access to the 2015 ridge-function uniqueness chapter and the 2025 monograph chapter on numerical ranges of linear relations was unavailable; an implicit equivalent connection remains an originality risk. No independent mathematical audit has been conducted.

## References
1. W. Boubaker, H. Gernandt and W. Selmi, *On the Numerical Range of Linear Relations in Banach Spaces*, arXiv:2608.19913v1, first posted 20 August 2026; especially Definition 3.1 and Theorems 3.3–3.4. https://arxiv.org/html/2608.19913v1
2. A. Pinkus, *Ridge Functions*, Cambridge University Press (2015), Chapter 3, “Uniqueness”, DOI:10.1017/CBO9781316408124.005.
3. B. Randrianantoanina, *On isometric stability of complemented subspaces of \(L_p\)*, arXiv:math/9709214v1 (1997), Sections 2–3. https://arxiv.org/html/math/9709214v1
4. A. Ammar and A. Jeribi, *Pseudospectra and Numerical Range of Linear Relations*, in *Spectral Theory of Block Multivalued Operator Matrices*, Springer (2025), DOI:10.1007/978-981-95-0397-1_4.
