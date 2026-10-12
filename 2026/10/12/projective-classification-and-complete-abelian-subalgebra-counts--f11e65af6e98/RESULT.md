# Projective classification and complete abelian-subalgebra counts in the minimal class-three CB algebra

## Finding
Let \(K\) be any field of characteristic different from \(2\), \(V\) a three-dimensional \(K\)-vector space, and
\[
A=V\oplus\Lambda^2V\oplus\Lambda^3V.
\]
Define the bilinear multiplication
\[
(v,a,c)\cdot(w,b,d)=(0,\;v\wedge w,\;v\wedge b-w\wedge a).
\]
The maximal abelian subalgebras (vector subspaces on which the product vanishes identically) are precisely
\(M=\Lambda^2V\oplus\Lambda^3V\), and the centralizers \(C_A(x)\) with \(x\) having nonzero \(V\)-component. Every one has dimension \(4\). The centralizers are canonically parametrized by a line \(\ell\in\mathbf P(V)\) and a map
\[
\alpha\in\operatorname{Hom}_K\bigl(\ell,\Lambda^2(V/\ell)\bigr),
\]
so their family is the total space of a line bundle isomorphic, after choosing a volume normalization, to \(\mathcal O_{\mathbf P^2}(2)\). The additional maximal abelian subalgebra is \(M\). Every abelian subalgebra not contained in \(M\) has a **unique** containing maximal abelian subalgebra.

For every odd prime power \(q\) and each integer \(0\le d\le7\), the complete dimension distribution is
\[
\boxed{A_d(q)={4\brack d}_q+q(q^2+q+1)\bigl({4\brack d}_q-{3\brack d}_q\bigr),}
\]
where \({n\brack d}_q\) is the Gaussian binomial coefficient, defined to be zero for \(d<0\) or \(d>n\). There are exactly
\[
\boxed{1+q(q^2+q+1)}
\]
maximal abelian subalgebras. Two distinct centralizers with the same projected line intersect in dimension \(3\); with distinct projected lines they intersect in dimension \(2\). Every centralizer meets \(M\) in dimension \(3\).

## Assumptions and scope
Products are anticommutative in the alternating sense \(x\cdot x=0\). The stated algebra is the seven-dimensional Saha–Towers Example 4.6, with \(e_1e_2=e_4\), \(e_1e_3=e_5\), \(e_2e_3=e_6\), \(e_1e_6=e_7\), \(e_2e_5=-e_7\), and \(e_3e_4=e_7\); the opposite products have negative signs and all other basis products vanish. Its third power is the nonzero one-dimensional \(\Lambda^3V\), and its fourth power vanishes. The finite-field counting statement concerns **labeled embedded subalgebras**, not isomorphism classes or group orbits. No assertion is made for other seven-dimensional algebras.

## Proof
Write \(W=\Lambda^2V\) and \(Z=\Lambda^3V\), both with their natural wedge pairings. For \(x=v+a+c\), \(y=w+b+d\) their product is
\[
x\cdot y=v\wedge w+v\wedge b-w\wedge a\in W\oplus Z.
\]
If \(v\ne0\), the equation \(x\cdot y=0\) first gives \(v\wedge w=0\), hence \(w=\lambda v\). Its degree-three part then gives \(v\wedge(b-\lambda a)=0\). Since the kernel of \(v\wedge(-):W\to Z\) is precisely \(v\wedge V\), a two-dimensional subspace of \(W\),
\[
C_A(x)=\{\lambda v+\lambda a+v\wedge s+d:\lambda\in K,\ s\in V,\ d\in Z\}.
\]
Thus \(\dim C_A(x)=1+2+1=4\). For two such elements the degree-two product vanishes because both \(V\)-parts are multiples of \(v\); their degree-three product is zero by cancellation of the two multiples of \(v\wedge a\), as \(v\wedge(v\wedge s)=0\). Hence \(C_A(x)\) is abelian. Any abelian subalgebra containing \(x\) is contained in its centralizer, so \(C_A(x)\) is maximal abelian.

For \(v=0\), the element is in \(M=W\oplus Z\), which is abelian. No nonzero \(v\in V\) commutes with all of \(W\), since \(v\wedge W=Z\), so \(C_A(M)=M\): this also is maximal abelian. Any abelian \(H\not\subseteq M\) contains an element \(x\) with \(v\ne0\), and is contained in \(C_A(x)\). If \(x'\in C_A(x)\setminus M\), then its \(V\)-component is a nonzero scalar multiple of \(v\), while its \(W\)-component has the corresponding scalar multiple of \(a\) modulo \(v\wedge V\), forcing \(C_A(x')=C_A(x)\). Therefore this containing maximal subalgebra is unique.

The centralizer is determined by the line \(\ell=Kv\) and the induced well-defined linear map \(\alpha:\ell\to W/(\ell\wedge V)\simeq\Lambda^2(V/\ell)\), mapping \(v\) to the class of \(a\). Conversely every \((\ell,\alpha)\) occurs by lifting \(\alpha(v)\) to \(a\). This proves the parametrization. Over \(\mathbf P(V)\), the tautological line is \(\mathcal O(-1)\); since \(\Lambda^2(V/\ell)\simeq\det V\otimes\ell^*\), the parameter line is \(\det V\otimes(\ell^*)^2\), giving \(\mathcal O(2)\) up to the fixed determinant line. Distinct \(\alpha\) give distinct centralizers. Intersections follow by comparing the projected \(V\)-lines and \(W\)-kernels: \(C_A(x)\cap M=(\ell\wedge V)\oplus Z\), and for distinct lines \(\ell,\ell'\), \((\ell\wedge V)\cap(\ell'\wedge V)=\ell\wedge\ell'\) is one-dimensional.

Over \(\mathbf F_q\), the number of lines in \(V\) is \(q^2+q+1\), and each parameter fiber contains \(q\) maps. For each dimension \(d\), there are \({4\brack d}_q\) subspaces contained in \(M\). Each of the \(q(q^2+q+1)\) four-dimensional centralizers contains \({4\brack d}_q-{3\brack d}_q\) \(d\)-subspaces outside \(M\), since its intersection with \(M\) is three-dimensional. Such subspaces are counted exactly once by the proved uniqueness property. Summing gives the formula, including \(d=0\) and \(d>4\). This is a proof for every odd prime power; finite searches below are independent checks, not its justification.

## Verification
The standalone `check.py` independently enumerates all row-reduced-echelon subspaces of \(\mathbf F_2^7\) in every dimension, and of \(\mathbf F_3^7\) in dimensions \(0,1,2\). It tests all pairwise basis products using the original structure constants, compares the abelian counts with the theorem, checks total subspace counts against Gaussian coefficients, and prints `VERIFY_OK` on success. Its observed abelian counts were \((1,127,427,211,15,0,0,0)\) over \(\mathbf F_2\) and \((1,1093,4693)\) in tested dimensions over \(\mathbf F_3\). The binary case is a supplementary boundary check; the theorem assumes characteristic different from \(2\).

## Relationship to prior work
Saha and Towers, *On certain classes of algebras in which centralizers are ideals*, arXiv:2004.12110v1, Theorem 3.9 and Example 4.6, introduce the precise seven-dimensional multiplication and prove a general centralizer-as-ideal property. The present result does **not** claim those results as new. It determines all maximal abelian subalgebras, their incidence geometry, uniqueness of maximal containment off \(M\), and the complete finite-field subalgebra counts; those formulas are not given in the inspected source. Related work of Saffarnia, Moghaddam and Rostamyari treats numbers of centralizers in Lie algebras, potentially overlapping a small part in characteristic three, but does not establish the full statement from its available abstract.

## Limitations
The theorem classifies abelian subalgebras, not arbitrary subalgebras, all ideals, or conjugacy classes. Finite enumeration checks only the stated small fields and dimensions. A full-text comparison with the 2018 centralizer-count article could not be completed; equivalent older results under different terminology remain a residual originality risk. This result has not undergone an independent audit.

## References
1. R. Saha and D. A. Towers, *On certain classes of algebras in which centralizers are ideals*, arXiv:2004.12110v1 (first posted 2020-04-25), especially Theorems 3.7, 3.9, 4.5 and Example 4.6. https://arxiv.org/html/2004.12110v1
2. S. Saffarnia, M. R. R. Moghaddam and M. A. Rostamyari, *Centralizers in Lie Algebras*, Indian Journal of Pure and Applied Mathematics 49 (2018), 39–49, DOI: 10.1007/s13226-018-0252-0 (abstract consulted; full text not inspected).
3. P. Das and R. Saha, *On Leibniz algebras whose centralizers are ideals*, arXiv:1903.09932 (2019; abstract consulted), https://arxiv.org/abs/1903.09932.
