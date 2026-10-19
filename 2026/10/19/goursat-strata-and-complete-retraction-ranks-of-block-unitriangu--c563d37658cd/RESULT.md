# Goursat strata and complete retraction ranks of block-unitriangular radical braces

## Finding

For every prime power \(q\) and integer \(n\geq 1\), let \(A_{n,q}\) be the \((2n+1)\)-dimensional, nonunital associative \(\mathbb F_q\)-algebra of strictly upper triangular block matrices of sizes \((1,n,1)\):

\[
A_{n,q}=\left\{\begin{pmatrix}0&u&s\\0&0&w\\0&0&0\end{pmatrix}:u\in\mathbb F_q^{1\times n},\ w\in\mathbb F_q^{n\times1},\ s\in\mathbb F_q\right\}.
\]

Equivalently write its elements as \((u,w,s)\), with multiplication
\[
(u,w,s)(u',w',s')=(0,0,uw').
\]
Endow it also with its radical-ring brace operation \(x\circ y=x+y+xy\). **The endomorphisms counted here are \(\mathbb F_q\)-linear and preserve multiplication** (equivalently, they are \(\mathbb F_q\)-linear homomorphisms of both brace operations). A *retraction* is such an endomorphism \(F\) satisfying \(F^2=F\), where the square means composition.

Let \({a\brack b}_q\) denote the Gaussian coefficient and \(G_t(q)=|\mathrm{GL}_t(\mathbb F_q)|=\prod_{j=0}^{t-1}(q^t-q^j)\), with \(G_0(q)=1\). For \(0\le r\le n\) set
\[
H_{n,r}(q)=\sum_{\substack{a,b,t\geq 0\\a+b\le n,\ t\le\min(a,b)\\a+b-t=r}}
{n\brack a}_q{n-a\brack b}_q
{a\brack t}_q{b\brack t}_q G_t(q).
\]
Then **the complete composition-idempotent endomorphism rank polynomial** is
\[
\boxed{P_{n,q}(z)=z^{2n+1}+\sum_{r=0}^{n}H_{n,r}(q)q^{r(2n-r+1)}z^r.}
\]
The coefficients count actual maps, not isomorphism classes. All ranks \(0,1,\ldots,n,2n+1\) occur, and no rank between \(n+1\) and \(2n\) occurs.

For each \(0\le r\le n\), there are exactly \(q^rH_{n,r}(q)\) *specified retraction images* of dimension \(r\), and each such image supports exactly \(q^{r(2n-r)}\) retractions. These images, except for the whole algebra (whose only retraction is the identity), are precisely the product-zero subspaces
\[
Y_{S,\eta}=\{v+\eta(v)z:v\in S\},
\]
where \(V=\mathbb F_q^n\oplus\mathbb F_q^n\), \(z=(0,0,1)\), \(S\le V\), \(\dim S=r\), \(S\cdot S=0\), and \(\eta:S\to\mathbb F_q\) is linear. The zero-product condition on \(S\) is equivalently
\[
\pi_U(S)\perp\pi_W(S)
\]
under the standard perfect pairing of the two coordinate spaces.

The largest proper rank is \(n\), with exact multiplicity
\[
\boxed{q^{n(n+1)}\sum_{a=0}^{n}{n\brack a}_q.}
\]
In particular \(H_{n,1}(q)=(q^{n-1}+1)(q^n-1)/(q-1)\). The first two nontrivial examples are
\[
P_{1,q}(z)=1+2q^2z+z^3,
\]
\[
P_{2,q}(z)=1+(q+1)^2q^4z+(q+3)q^6z^2+z^5.
\]
Thus \(P_{2,2}(z)=1+144z+320z^2+z^5\), with \(18\) distinct rank-one images and \(20\) distinct rank-two images.

## Assumptions and scope

All vector spaces, endomorphisms, projections, products, dimensions, and rank calculations are over the specified field \(\mathbb F_q\), with arbitrary prime-power \(q\) and integer \(n\geq1\). Homomorphisms are not required to be unital, since the algebra has no unit. The additive group of the brace is the additive group of the algebra, and \(\circ\) is associative as a group operation because the algebra is nilpotent. For nonprime \(q\), arbitrary brace homomorphisms need only be prime-field-linear; those extra homomorphisms are *not* counted by this theorem. The standard pairing \(U\times W\to\mathbb F_q\) is \((u,w)\mapsto uw\), with \(U=\mathbb F_q^{1\times n}\) and \(W=\mathbb F_q^{n\times1}\).

## Proof

**1. Quotient normal form.** Put \(V=U\oplus W\), \(Z=A_{n,q}^2=\mathbb F_qz\), and let \(B:V\times V\to\mathbb F_q\) be \(B((u,w),(u',w'))=uw'\). Multiplication is \(xy=B(\bar x,\bar y)z\). Every algebra endomorphism carries the characteristic subspace \(Z\) into itself, so it has a unique decomposition
\[
F(v+sz)=Tv+(\phi(v)+cs)z
\]
with \(T\in\operatorname{End}_{\mathbb F_q}(V)\), \(\phi\in V^*\), and \(c\in\mathbb F_q\). It preserves multiplication exactly when
\[
B(Tv,Tw)=cB(v,w)\quad\text{for all }v,w\in V.
\]
Idempotence under composition is exactly \(T^2=T\), \(c^2=c\), and \(\phi T+c\phi=\phi\).

**2. The center-surviving case is the identity.** If \(c\ne0\), write \(T(u,w)=(Au+Cw,Du+Ew)\). Comparing the coefficient of \(u\cdot w'\) in the bilinear identity gives \(A^{\mathsf T}E=cI_n\). Thus \(A,E\) are invertible. Comparing the \(u\cdot u'\) and \(w\cdot w'\) terms then gives \(D=0\) and \(C=0\). Thus \(T\) is invertible; from \(T^2=T\) we get \(T=I_V\). The identity \(A^{\mathsf T}E=cI_n\) now gives \(c=1\), and \(\phi T+c\phi=\phi\) gives \(\phi=0\). Hence \(F\) is the identity. (The symbols \(C,D,E\) in this paragraph are the four block matrices of \(T\), not source labels.)

**3. All proper retractions.** Therefore every other retraction has \(c=0\). Its induced map \(T\) is a projection onto some \(r\)-space \(S\le V\), and multiplicativity reduces to \(B(S,S)=0\). Moreover \(\phi T=\phi\), so \(\phi=\eta\circ T\) for a unique \(\eta\in S^*\). This produces exactly the image graph \(Y_{S,\eta}\). Conversely every such \(S\), \(\eta\), and projection \(T:V\to S\) give a multiplicative idempotent map. With \(S\) fixed, the projection kernels range over all complements of \(S\) in \(V\), of which there are \(q^{r(2n-r)}\), and the functional \(\eta\) has \(q^r\) choices. Thus the count attached to each \(S\) is \(q^{r(2n-r+1)}\), and that attached to each specific image is \(q^{r(2n-r)}\).

**4. Counting product-zero subspaces (Goursat strata).** Write \(U_0=\pi_U(S)\) and \(W_0=\pi_W(S)\), with dimensions \(a,b\). Since \(B(S,S)=0\), every vector of \(U_0\) pairs to zero with every vector of \(W_0\). Conversely this orthogonality implies \(B(S,S)=0\). Choose \(U_0\) in \({n\brack a}_q\) ways, and then \(W_0\le U_0^\perp\) in \({n-a\brack b}_q\) ways, necessarily \(a+b\le n\).

For fixed \(U_0,W_0\), a subspace \(S\le U_0\oplus W_0\) surjecting onto both coordinates is classified by the Goursat data \(L=S\cap U_0\), \(M=S\cap W_0\), and an isomorphism \(U_0/L\cong W_0/M\). Both quotients have the same dimension \(t\). Choosing the two kernel subspaces and the isomorphism gives
\[
{a\brack t}_q{b\brack t}_q G_t(q)
\]
possibilities, each with \(\dim S=a+b-t\). Every \(S\) determines the data uniquely. Summing proves exactly the expression \(H_{n,r}(q)\) above, with no overcounting.

**5. Rank support and boundary coefficients.** The condition \(a+b\le n\) forces \(r=a+b-t\le n\), while every \(0\le r\le n\) occurs by taking any \(r\)-space in \(U\) alone. The only remaining retraction is the identity of rank \(2n+1\). If \(r=n\), necessarily \(a+b=n\) and \(t=0\), so \(H_{n,n}(q)=\sum_{a=0}^n{n\brack a}_q\). For \(r=1\), \(S\) is a line spanned by a nonzero pair \((u,w)\) with \(uw=0\). There are \((q^n-1)(q^{n-1}+1)\) such nonzero vectors, and division by \(q-1\) yields the stated \(H_{n,1}(q)\). Directly substituting \(n=1,2\) into \(H\) gives the displayed examples. This completes the proof.

## Verification

The standalone standard-library program `check.py` constructs finite fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), enumerates all matrices representing endomorphisms in the three-dimensional case, and directly tests every multiplication-table identity, composition-idempotence and matrix rank (no structural ansatz imposed). It separately enumerates reduced-row-echelon subspaces in dimensions \(2,4,6\) over \(\mathbb F_2\), checking the ordered product-zero condition, and enumerates all binary four-dimensional quotient projections directly. These independently motivated finite checks give:

```
RAW_MATRIX_CHECK 2 1 [(0, 1), (1, 8), (3, 1)]
RAW_MATRIX_CHECK 3 1 [(0, 1), (1, 18), (3, 1)]
RAW_MATRIX_CHECK 4 1 [(0, 1), (1, 32), (3, 1)]
SUBSPACE_RREF_CHECK 1 [(0, 1), (1, 2)]
SUBSPACE_RREF_CHECK 2 [(0, 1), (1, 9), (2, 5)]
SUBSPACE_RREF_CHECK 3 [(0, 1), (1, 35), (2, 77), (3, 16)]
DIRECT_PROJECTION_CHECK 2 2 [(0, 1), (1, 144), (2, 320), (5, 1)]
ALL_EXACT_CHECKS_PASSED
```

Reproduce using `python3 check.py` with Python's standard library. The infinite family is proved by the algebraic argument above, not by these finite tests.

## Relationship to prior work

The radical-ring construction of braces, left/right nilpotent brace series, and brace factorization results are standard and are not claimed as discoveries here. The 2018 work of Cedó, Smoktunowicz, and Vendramin supplies relevant structural context for nilpotent braces, while the 2019 paper of Jespers, Kubat, Van Antwerpen, and Vendramin treats factorizations and *solution retractions* (the latter quotient solutions of a Yang–Baxter system), not enumeration of composition-idempotent homomorphisms of this block-matrix algebra. Caranti and Stefanello treat group endomorphisms used to build bi-skew braces; their construction likewise does not supply the rank polynomial here. Research into upper-triangular **additively idempotent semirings** concerns different algebraic coefficients and multiplication constraints.

The commutator Lie algebra of \(A_{n,q}\) is a Heisenberg Lie algebra; its isotropic-image condition is weaker than the ordered product-zero condition \(B(S,S)=0\). Consequently a Lie-endomorphism retraction census does not give the Gaussian–Goursat factor \(H_{n,r}(q)\): for example, already at \(n=1\), the ordered zero-product subspaces comprise exactly two lines, rather than all \(q+1\) symplectic-isotropic lines. The calculation here isolates the genuinely multiplicative constraint.

## Limitations

The theorem counts \(\mathbb F_q\)-linear algebra/brace endomorphisms, not every additive-group or multiplicative-group endomorphism, and not all brace endomorphisms over extension fields without an imposed \(\mathbb F_q\)-linearity condition. It treats only the indicated three-block radical algebra, not arbitrary nilpotent algebras or all finite braces. The finite checks are illustrative, not proofs for unbounded parameters. An equivalent rank-refined formulation in older literature on nilpotent radical rings, bilinear spaces, or braces has not been definitively excluded; the asserted novelty is limited to the combined explicit image classification and Gaussian–Goursat rank enumeration, not its classical ingredients.

## References

1. F. Cedó, A. Smoktunowicz, L. Vendramin, *Skew left braces of nilpotent type*, arXiv:1806.01127 (first submitted 2018-06-04), https://arxiv.org/abs/1806.01127.
2. E. Jespers, Ł. Kubat, A. Van Antwerpen, L. Vendramin, *Factorizations of skew braces*, arXiv:1905.05886 (first submitted 2019-05-14), https://arxiv.org/abs/1905.05886.
3. A. Caranti, L. Stefanello, *From endomorphisms to bi-skew braces, regular subgroups, the Yang–Baxter equation, and Hopf–Galois structures*, arXiv:2104.01582 (first submitted 2021-04-04), https://arxiv.org/abs/2104.01582.
4. D. I. Vladeva, *Endomorphisms of upper triangular matrix semirings*, Communications in Algebra (online 2021-09-03), doi:10.1080/00927872.2021.1972306. The additive structures differ from those of field algebras.
