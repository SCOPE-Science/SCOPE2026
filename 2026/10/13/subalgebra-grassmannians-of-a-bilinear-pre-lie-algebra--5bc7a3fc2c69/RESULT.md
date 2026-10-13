# Subalgebra Grassmannians of a bilinear pre-Lie algebra

## Finding
Let \(K\) be any field, let \(V\) be a finite-dimensional \(K\)-vector space, and let \(B:V\times V\to K\) be symmetric. On \(A=Ke\oplus V\) define the bilinear product
\[
(ae+u)\cdot(be+v)=(2ab+B(u,v))e+av.
\]
Then \(A\) is a pre-Lie algebra. With the orthogonal-sum bilinear form
\[
\widetilde B(ae+u,be+v)=ab+B(u,v),
\]
its linear subalgebras are **exactly** (i) the subspaces containing \(e\), and (ii) the totally isotropic subspaces for \(\widetilde B\). These two families are disjoint; every subspace containing \(e\) is a subalgebra. Here totally isotropic means that \(\widetilde B\) vanishes on the entire Cartesian square of the subspace, rather than merely on a single vector.

Consequently, if \(K=\mathbb F_q\), \(q\) is odd, \(n=\dim V\ge1\), and \(B\) is nondegenerate, the **entire subalgebra-dimension polynomial**
\[
Z_{A}(T)=\sum_{S\le A,\ S\cdot S\subseteq S} T^{\dim_{\mathbb F_q}S}
\]
is
\[
\boxed{Z_A(T)=T\sum_{k=0}^{n}{n\brack k}_q T^k+\sum_{r=0}^{\lfloor(n+1)/2\rfloor} I_rT^r.}
\]
Here \({n\brack k}_q\) is the Gaussian binomial coefficient, \(I_0=1\), and the other \(I_r\) are computed without orbit enumeration as follows. Set \(N=n+1\), \(\Delta=\det B\in\mathbb F_q^\times\) (its square class is basis-independent), and, if \(N\) is even, let
\[
\epsilon=\chi((-1)^{N/2}\Delta),
\]
where \(\chi\) is the quadratic character. For \(0\le r<\lfloor N/2\rfloor\) put \(d=N-2r\) and
\[
C_r=\begin{cases}
q^{d-1},&d\text{ odd},\\
q^{d-1}+(q-1)\epsilon q^{(d-2)/2},&d\text{ even}.
\end{cases}
\qquad
I_{r+1}=I_r\frac{C_r-1}{q^{r+1}-1}.
\]
The recursion always yields nonnegative integers and includes the vanishing maximal-isotropic strata in nonsplit even-dimensional quadratic spaces.

**Discriminant boundary:** if \(n\) is even, \(Z_A(T)\) depends only on \(n\) and \(q\), not on the nondegenerate symmetric form \(B\). If \(n\) is odd, the formula can distinguish the two square classes of \(\det B\). For \(n=3,q=3\), the forms with diagonal entries \((1,1,1)\) and \((1,1,2)\) give respectively
\[
1+17T+21T^2+13T^3+T^4
\quad\text{and}\quad
1+11T+13T^2+13T^3+T^4.
\]
For \(n=4,q=3\), these two discriminant classes both give
\[
1+41T+80T^2+130T^3+40T^4+T^5.
\]

## Assumptions and scope
The structural classification is valid for all fields and all symmetric bilinear forms, including degenerate forms and characteristic two. The displayed numerical recursion and discriminant assertion require \(q\) odd and \(B\) nondegenerate. Subalgebras mean **all** \(K\)-linear subspaces closed under the displayed product; they need not contain \(e\). The zero subspace and the full algebra are counted. Isomorphic subalgebras are counted separately when they are distinct embedded subspaces.

## Proof
**1. Pre-Lie identity.** Write \(\lambda(ae+u)=a\) and \(\beta_x(y)=\widetilde B(x,y)\). The multiplication has the exact form
\[
x\cdot y=\lambda(x)y+\beta_x(y)e.\tag{1}\]
Thus left multiplication is \(L_x=\lambda(x)\operatorname{id}+e\otimes\beta_x\), and symmetry of \(\widetilde B\) gives
\[
[x,y]_{\cdot}:=x\cdot y-y\cdot x=\lambda(x)y-\lambda(y)x.
\]
Direct calculation yields
\[
[L_x,L_y]=e\otimes(\lambda(x)\beta_y-\lambda(y)\beta_x)
=L_{[x,y]_{\cdot}}.
\]
This operator identity is equivalent to the left-symmetric/pre-Lie associator being symmetric in its first two entries. No characteristic restriction is used.

**2. Exact subalgebra criterion.** If \(S\le A\) contains \(e\), then \(S=Ke\oplus(S\cap V)\). Equation (1) shows closure because its two summands lie in \(S\). If \(e\notin S\), then \(S\cap Ke=0\). For all \(x,y\in S\), equation (1) implies
\[
x\cdot y\in S\iff \beta_x(y)e\in S\iff\widetilde B(x,y)=0.
\]
Requiring this for every ordered pair is precisely total isotropy. Conversely total isotropy makes \(x\cdot y=\lambda(x)y\in S\). The criterion is therefore necessary, sufficient, and disjoint.

**3. Grassmann and polar counts.** Every \(k\)-subspace \(W\le V\) corresponds to the unique subalgebra \(Ke\oplus W\) of dimension \(k+1\), giving \({n\brack k}_q\). By step 2, all remaining subalgebras of dimension \(r\) are exactly the \(r\)-dimensional totally isotropic subspaces of the nondegenerate form \(\widetilde B=\langle1\rangle\perp B\) of dimension \(N\). Their number is \(I_r\).

Fix a totally isotropic subspace \(U\) of dimension \(r\). The induced form on \(U^\perp/U\) is nondegenerate, of dimension \(d=N-2r\). Splitting off \(r\) hyperbolic planes shows that its determinant square class is \((-1)^r\Delta\). The number \(C_r\) of vectors of norm zero in this quotient equals \(q^{d-1}\) if \(d\) is odd; for even \(d\ge2\) it is
\[
q^{d-1}+(q-1)\chi((-1)^{d/2+r}\Delta)q^{(d-2)/2}
=q^{d-1}+(q-1)\epsilon q^{(d-2)/2}.
\]
For completeness, these zero counts follow by diagonalizing the quadratic form and using character orthogonality: for a nontrivial additive character \(\psi\), the one-variable sums for nonzero \(s\) are \(\sum_x\psi(sa x^2)=\chi(sa)G\), with \(G^2=\chi(-1)q\). Averaging \(\prod_i\sum_{x_i}\psi(sa_i x_i^2)\) over \(s\) gives the two cases above. This also covers dimension two; no asymptotic approximation is involved.

There are \((C_r-1)/(q-1)\) isotropic one-dimensional subspaces of \(U^\perp/U\), each defining an extension of \(U\) to an \((r+1)\)-dimensional totally isotropic subspace. Count pairs consisting of such an extension and an \(r\)-subspace of it: each \((r+1)\)-space contains \((q^{r+1}-1)/(q-1)\) subspaces of codimension one. Therefore
\[
I_{r+1}\frac{q^{r+1}-1}{q-1}
=I_r\frac{C_r-1}{q-1},
\]
proving the recursion and its integrality. When \(r=\lfloor N/2\rfloor\), the process stops. A nonsplit even-dimensional form has its top coefficient zero automatically.

**4. Discriminant assertion.** When \(n\) is even, \(N\) is odd, and every successive quotient \(U^\perp/U\) has odd dimension. Thus \(C_r=q^{N-2r-1}\) is independent of the determinant, and so are all \(I_r\). When \(n\) is odd, \(N\) is even and \(C_r\) carries the sign \(\epsilon\); the displayed three-dimensional example shows this distinction is genuinely detectable.

## Verification
The standalone script `verify_subalgebra_census.py` constructs **every** subspace in reduced row-echelon form for several small prime fields. For each subspace it independently tests multiplication closure and verifies pointwise that closure is equivalent to containing \(e\) or being totally isotropic. It then compares the entire dimension distribution with the stated recursion. Checked cases include \(q=3\), \(n=1,2,3,4\), and \(q=5\), \(n=2,3\), for both available discriminant classes. Running `python3 verify_subalgebra_census.py` prints `VERIFY_OK` on success. These experiments check finite examples; the unlimited dimension and prime-power claims follow from the proof, not from enumeration.

## Relationship to prior work
The dimension-two multiplication \(e\cdot e=2e\), \(e\cdot v=v\), \(v\cdot e=0\), \(v\cdot v=e\) appears in the pre-Lie examples of Cerqua–Facchini (2023), who cite Nijenhuis for the original example and study idempotent endomorphisms and semidirect decompositions. The present statement concerns the **subalgebra lattice** of the natural symmetric-bilinear-form extension in arbitrary dimension, not the general equivalence between retractions and split decompositions. Facchini–Heidari Zadeh (2022) investigate unital algebra extensions with bilinear forms, but their categorical equivalence does not provide the present nonunital pre-Lie subalgebra criterion. Counts of totally isotropic subspaces of finite quadratic spaces are classical; they are used as standard input after the new explicit algebra-to-polar-space correspondence, and are not claimed as new quadratic-form counts.

## Limitations
The closed finite-field counting recursion is restricted to odd characteristic and nondegenerate symmetric \(B\). The structural subalgebra criterion does not impose those restrictions. The assertion is about embedded subalgebras and their dimensions, not a classification of their isomorphism classes, their automorphism orbits, or the full incidence relation among subalgebras. The finite-field formula does not count automorphisms or idempotent endomorphisms. No claim of novelty is made for classical orthogonal polar-space counts or the previously published dimension-two example.

## References
1. M. Cerqua and A. Facchini, *Pre-Lie algebras, their multiplicative lattice, and idempotent endomorphisms*, arXiv:2301.02627v1 (6 January 2023), especially Examples 1(3) and Section 6. https://arxiv.org/html/2301.02627v1
2. A. Facchini and L. Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms*, arXiv:2210.08230v1 (15 October 2022). https://arxiv.org/html/2210.08230v1
3. M. De Boeck and G. Van de Voorde, *Anzahl theorems for disjoint subspaces generating a non-degenerate subspace II: quadratic forms*, arXiv:2409.12312v1 (18 September 2024), for contemporary orthogonal-subspace counting context. https://arxiv.org/abs/2409.12312
