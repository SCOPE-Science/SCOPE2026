# Correcting the explicit species table in the D4-triality example

## Finding

The six Galois orbits of positive roots listed in §3 of Januszewski's *Rational quiver representations: tame and wild* have orbit-sum dimension vectors, in the paper's order,
\[
(1,0,0,0),\ (0,1,1,1),\ (3,1,1,1),\ (3,2,2,2),\ (1,1,1,1),\ (2,1,1,1).
\]
The associated species dimensions \((\dim_K V_K,\dim_M V_M)\) are therefore
\[
(1,0),\ (0,1),\ (3,1),\ (3,2),\ (1,1),\ (2,1).
\]
The explicit species table on p. 7 does not match these data. Its item (3), \((K,M)\) with inclusion, belongs to orbit 5; item (4), \((M,M)\) with identity, belongs to orbit 3; and item (5), \((\ker\operatorname{Tr}_{M/K},M)\) with inclusion, belongs to orbit 6. In item (6), the trace \(M\to K\) has the stated direction from the first component to the second. But the second component \(K\) is not an \(M\)-vector space compatible with its given \(K\)-structure. Thus item (6) is not an object of the stated species category. Its printed root vector \((1,1,1,1)\) is the vector of orbit 5, not orbit 6. There is no valid entry of species dimension \((3,2)\) in the printed table.

The corrected orbit correspondence is:

| Orbit | Pair and map |
| --- | --- |
| 1 | \((K,0)\), zero map |
| 2 | \((0,M)\), zero map |
| 3 | \((M,M)\), identity |
| 4 | The indecomposable of dimensions \((3,2)\) |
| 5 | \((K,M)\), inclusion |
| 6 | \((\ker\operatorname{Tr}_{M/K},M)\), inclusion |

This corrects the explicit table, not the general orbit-classification theorem. An explicit representative for orbit 4 over one cubic field is given below.

## Assumptions and scope

Work in characteristic zero with an \(S_3\)-Galois extension \(L/K\), and let \(M=L^H\) for a subgroup \(H\cong S_2\). Thus \([M:K]=3\). Following the stated convention, a species representation is a pair \((V_K,V_M)\) with a \(K\)-linear map \(V_K\to V_M\), where \(V_K\) is a \(K\)-space and \(V_M\) is an \(M\)-space.

## Proof

The singleton central root gives \((1,0,0,0)\); the three leaf roots sum to \((0,1,1,1)\); the three roots with the center and one leaf sum to \((3,1,1,1)\); and the three roots with the center and two leaves sum to \((3,2,2,2)\). The all-ones root and the highest root each form a singleton orbit, with vectors \((1,1,1,1)\) and \((2,1,1,1)\).

After base change to \(L\), the central coordinate is \(\dim_K V_K\). The three embeddings of \(M\) into \(L\) split \(M\otimes_K L\) into three copies of \(L\), giving a leaf coordinate of \(\dim_M V_M\) at each leaf. This gives the six species pairs of dimensions above. The candidate pairs of dimensions \((3,1),(1,1),(2,1)\) with identity or inclusion are indecomposable: the target is one-dimensional over \(M\), so a nontrivial decomposition would give a nonzero source summand with zero target, contradicting injectivity. The other two displayed pairs with one zero component are simple. By the orbit classification, this leaves the indecomposable of dimensions \((3,2)\) for orbit 4. Item (6) of the printed table cannot supply it, because any \(M\)-space has \(K\)-dimension a multiple of three, whereas \(\dim_K K=1\).

For an explicit representative of the missing dimension \((3,2)\), take \(K=\mathbb Q\), \(M=\mathbb Q(\theta)\), \(\theta^3=2\). The Galois closure of \(M\) is \(\mathbb Q(\theta,\zeta_3)\) with group \(S_3\). Take \(V_K=M\), \(V_M=M^2\), and \(f(x)=(x,\alpha(x))\), where \(\alpha\) is \(\mathbb Q\)-linear with matrix on the basis \((1,\theta,\theta^2)\)
\[
A=\begin{pmatrix}0&-1&0\\1&1&-1\\0&1&-1\end{pmatrix}.
\]
An endomorphism consists of a \(\mathbb Q\)-linear source map \(\gamma\) and an \(M\)-linear target map \(\beta=\begin{pmatrix}u&v\\w&z\end{pmatrix}\), satisfying \(\beta f=f\gamma\). Write \(m_c\) for multiplication by \(c\in M\). The first component gives \(\gamma=m_u+m_v\alpha\); the second gives
\[
\alpha m_u+\alpha m_v\alpha-m_w-m_z\alpha=0.
\]
In the basis \((1,\theta,\theta^2)\) this is a rational linear system of rank nine in the twelve coefficients of \((u,v,w,z)\). The three-dimensional endomorphism algebra contains a pair with source matrix
\[
\Gamma_0=\begin{pmatrix}2&36&8\\-1&-26&-8\\1&0&0\end{pmatrix}.
\]
For this pair the coefficient triples for \((u,v,w,z)\) are respectively \((-12,19,-7),(-20,8,7),(-25,4,11),(-4,-13,13)\). The characteristic polynomial of \(\Gamma_0\) is \(p(X)=X^3+24X^2-24X+80\). Modulo seven the values of \(p\) at \(0,\ldots,6\) are \(3,4,3,6,5,6,1\), respectively, so this monic cubic is irreducible over \(\mathbb Q\). The endomorphism pair therefore generates a subalgebra of dimension at least three by looking at its source component. Since the full algebra has dimension three, the projection to the source algebra identifies it with the field \(\mathbb Q[\Gamma_0]\). There are no nontrivial idempotents, proving indecomposability of this representative.

## Verification

The orbit sums and dimensions can be checked directly from §3 of the cited paper. For the example, the multiplication matrix of \(\theta\) is \(T=\begin{pmatrix}0&0&2\\1&0&0\\0&1&0\end{pmatrix}\). Flattening each of \(AB,ABA,-B,-BA\) for \(B=I,T,T^2\), with the four groups ordered as above, gives the nine-by-twelve matrix of the displayed linear system. Its exact rational rank is nine. The displayed coefficient triples verify the intertwining equation for \(\Gamma_0\).

## Relationship to prior work and limitations

The source's Theorem 2.3 states the general classification by Galois orbits of positive roots. The correction reconciles the §3 species table with that theorem and the paper's orbit list. It does not claim a new classification theorem about \(G_2\) species. The explicit \((3,2)\) representative here is for \(M=\mathbb Q(\sqrt[3]{2})\); for general \(M\) the orbit classification supplies existence. A separate prior correction may exist.

## Reference

F. Januszewski, *Rational quiver representations: tame and wild*, [arXiv:2510.00924v1](https://arxiv.org/pdf/2510.00924v1), Theorem 2.3 and §3, pp. 5–7.
