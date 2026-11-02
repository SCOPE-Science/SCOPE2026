# Tjurina-module flag strata of a fixed-Puiseux-pair plane-branch family

## Finding
For every pair of integers \(m\ge5\) and \(q\ge2\), set \(n=mq+1\) and define the \(q\)-parameter family of complex plane-curve germs
\[
f_{\mathbf a}(x,y)=y^m-x^n+yh_{\mathbf a}(x),\qquad
h_{\mathbf a}(x)=\sum_{i=1}^{q}a_i x^{(m-1)q+i},\quad \mathbf a\in\mathbb C^q.
\]
Every member is an irreducible plane branch with Puiseux pair \((m,n)\), value semigroup \(\langle m,n\rangle\), and Milnor number \(\mu=m(m-1)q\). Let \(R=\mathbb C[[x]]\) and let \(T_{\mathbf a}=\mathbb C[[x,y]]/(f_{\mathbf a},\partial_xf_{\mathbf a},\partial_yf_{\mathbf a})\) be its Tjurina algebra.

At \(\mathbf a=0\), one has \(\tau=\dim_{\mathbb C}T_{\mathbf0}=\mu\). For \(\mathbf a\ne0\), let \(j\) be the first index with \(a_j\ne0\) and put \(v=(m-1)q+j\). Then there are exact algebra and \(R\)-module presentations
\[
T_{\mathbf a}\cong
\frac{\mathbb C[[x,y]]}{\left(x^n,\,y^{m-1}+h_{\mathbf a}(x)/m,\,
 x^{v-1}y-\frac{n}{v a_j}x^{n-1}\right)},
\qquad
T_{\mathbf a}\cong_R R/(x^n)\oplus\left(R/(x^{v-1})\right)^{m-2}.
\]
In particular,
\[
\boxed{\tau(\mathbf a)=n+(m-2)(v-1),\qquad
\mu-\tau(\mathbf a)=(m-2)(q-j)+(m-3).}
\]
The \(q+1\) exact Tjurina-number loci are the origin and the disjoint smooth irreducible locally closed subsets
\[
\{a_1=\cdots=a_{j-1}=0,\ a_j\ne0\}\cong
\mathbb G_m\times\mathbb A^{q-j}\quad (1\le j\le q).
\]
These have codimension \(j-1\) in the parameter affine space, and distinct \(j\) give distinct Tjurina numbers. Relative to the fixed \(x\)-projection, the \(x\)-adic Hilbert function of \(T_{\mathbf a}\) is exactly \(m-1\) for orders \(0\le r<v-1\), exactly \(1\) for \(v-1\le r<n\), and zero thereafter. Every noncentral member is non-quasihomogeneous.

## Assumptions and scope
All rings are complete local \(\mathbb C\)-algebras at \((x,y)=(0,0)\). Coefficients \(a_i\) range over all complex numbers without genericity assumptions. The word *stratum* refers to the Tjurina-number stratification of this specifically defined affine coefficient family; it is not a classification of all branches with the given Puiseux pair, nor an assertion of pairwise analytic inequivalence within a stratum. The displayed module decomposition is over the fixed subring \(R=\mathbb C[[x]]\), not an isomorphism of rings to a direct sum of rings.

## Proof
**Fixed topology and Milnor number.** Give \(x\) weight \(m\) and \(y\) weight \(n\). The leading part \(y^m-x^n\) has weight \(mn\). The perturbing monomial \(x^{(m-1)q+i}y\) has strictly larger weight, by \(m(i-1)+1>0\). The Newton edge has coprime intercepts \(m,n\), since \(n=mq+1\). Newton--Puiseux therefore gives one irreducible branch with Puiseux pair \((m,n)\) and value semigroup \(\langle m,n\rangle\). The weighted initial forms of \(\partial_x f\) and \(\partial_y f\) are the regular sequence \(-n x^{n-1}\), \(m y^{m-1}\). The resulting Milnor algebra has vector-space dimension \((n-1)(m-1)=m(m-1)q\), independent of coefficients. Since the germ has one branch, its delta invariant is \(\mu/2\).

**A three-generator Tjurina ideal.** Suppose \(\mathbf a\ne0\) and write \(h=h_{\mathbf a}=x^v u(x)\), where \(u(0)=a_j\ne0\) and \(v=(m-1)q+j\le n-1\). Write \(f=f_{\mathbf a}\) and \(I=(f,f_x,f_y)\). The exact weighted Euler identity is
\[
mxf_x+nyf_y-mnf=y\{mxh'(x)-n(m-1)h(x)\}.
\]
The bracket equals \(x^v U(x)\) with
\(U(0)=(mv-n(m-1))a_j=(m(j-1)+1)a_j\ne0\). Thus \(x^v y\in I\). Using \(xf_x=-nx^n+xyh'\) and \(xyh'\in(x^v y)\), we get \(x^n\in I\). Conversely \(xf_x=-nx^n+x^v w(x)y\), with \(w(0)=v a_j\ne0\), shows \(x^v y\in(f_x,x^n)\). The identity
\[
f=(y/m)f_y-x^n+((m-1)/m)yh
\]
then proves the equality \(I=(f_x,f_y,x^n)\) in the completed local ring.

**Exact algebra and module.** Reduce modulo \(x^n\), and set \(R_n=R/(x^n)\). Because \(f_y/m=y^{m-1}+h/m\) is monic in \(y\), its quotient is free over \(R_n\), with basis \(1,y,\ldots,y^{m-2}\). In that quotient, \(f_x=x^{v-1}w(x)y-nx^{n-1}\). The factor \(w(x)\) is a unit and \(x^{n-1}w(x)^{-1}=x^{n-1}/(v a_j)\) modulo \(x^n\), giving the asserted algebra presentation with the single remaining relation
\[
x^{v-1}y=c x^{n-1},\qquad c=\frac{n}{v a_j}.
\]
Since \(v\le n-1\), multiplying this relation by \(x^{n-v}\) gives \(x^{n-1}y=0\). Its products with powers \(y^k\) therefore give \(x^{v-1}y^k=0\) for \(2\le k\le m-2\). The last product is compatible with the monic relation for \(y^{m-1}\), because \(x^{v-1}h\) is divisible by \(x^{2v-1}\), and \(2v-1\ge n\). No further \(R_n\)-module relation occurs: multiplication of the displayed single relation by all \(y^k\), reduced using the monic equation, accounts for its full ideal. Replacing the basis vector \(y\) by \(y-cx^{n-v}\) now yields
\[
T_{\mathbf a}\cong_R R/(x^n)\oplus(R/(x^{v-1}))^{m-2}.
\]
Counting \(R\)-lengths proves \(\tau=n+(m-2)(v-1)\). Substitution of \(n=mq+1\) and \(v=(m-1)q+j\) proves the defect formula. The same decomposition gives the stated \(x\)-adic Hilbert function.

**Parameter strata and the central point.** For \(\mathbf a=0\), the Tjurina ideal is \((x^{n-1},y^{m-1})\), so \(\tau=(n-1)(m-1)=\mu\). Otherwise only the first nonzero index \(j\) enters the formula; each such locus is the indicated product of a punctured affine line and an affine space. The defects decrease by \(m-2>0\) as \(j\) increases and end at \(m-3>0\). Saito's \(\mu=\tau\) criterion therefore shows that only the central germ is quasihomogeneous.

## Verification
The standalone script `artifacts/verify_tjurina.py` performs 38 exact rational-coefficient Gröbner-basis computations using SymPy. It independently enumerates the standard monomials of each Tjurina quotient and confirms the leading monomial ideals, dimensions, weighted Euler identity, and central quasihomogeneous cases for \((m,q)=(5,2),(5,3),(6,2),(7,2),(8,2)\). It returned `VERIFY_OK: 38 exact Gröbner quotient checks`. These finitely many examples are checks, not a substitute for the all-parameter proof above.

For instance, \(m=5,q=2\) gives a fixed Milnor number \(\mu=40\), while the three Tjurina strata are \(\tau=35\) when \(a_1\ne0\), \(\tau=38\) when \(a_1=0,a_2\ne0\), and \(\tau=40\) at the origin. Even the highest perturbation \(x^{n-1}y\), which belongs to the Jacobian ideal of the central member, produces positive nonlinear defect \(m-3\) when taken alone.

## Relationship to prior work
He's 2026 criterion characterizes the degeneration of the derived Hodge-to-de Rham spectral sequence of an integral projective lci curve by quasihomogeneity of its local singularities. It gives the motivation to quantify the local Milnor--Tjurina defect but does not supply this explicit module decomposition or parameter census. Greuel--Hertling--Pfister develop general moduli and Tjurina-Hilbert-function strata for semiquasihomogeneous singularities. Hefez--Hernandes give a general analytic-classification algorithm for plane branches. Almirón--Hernandes study a different, two-branch Tjurina-number phenomenon. The result here is a direct exact classification only for the explicitly specified linear-in-\(y\), one-Puiseux-pair slice; it does not claim a new general criterion, a complete analytic classification, or global historical priority. Classical tools (Newton--Puiseux, Saito's criterion, local Gröbner methods) are credited rather than claimed as new.

## Limitations
This is a local analytic theorem over \(\mathbb C\), not a theorem about an arbitrary projective compactification or a global spectral sequence. All defect gaps are asserted **only within this coefficient family**. The \(R\)-module structure depends on the chosen \(x\)-coordinate; the Tjurina number itself is analytic-invariant. No claim is made about abstract isomorphism classes inside a stratum, geometric monodromy, or the locus in the full equisingular deformation space. Historical priority requires independent literature assessment; mathematical validation outside these exact calculations has not been performed.

## References
1. Yunfan He, *Hodge-to-de Rham degeneration and quasihomogeneous singularities of curves*, arXiv:2604.05825 (2026-04-07), https://arxiv.org/html/2604.05825.
2. Gert-Martin Greuel, Claus Hertling, Gerhard Pfister, *Moduli spaces of semiquasihomogeneous singularities with fixed principal part*, arXiv:alg-geom/9503013 (1995-03-22), https://arxiv.org/html/alg-geom/9503013v1.
3. Abramo Hefez and Marcelo E. Hernandes, *The Analytic Classification of Plane Branches*, arXiv:0707.4502 (2007-07-30), https://arxiv.org/html/0707.4502v1.
4. Patricio Almirón and Marcelo E. Hernandes, *The Tjurina number of a plane curve with two branches and high intersection multiplicity*, arXiv:2501.12836 (2025-01-22), https://arxiv.org/html/2501.12836v1.
