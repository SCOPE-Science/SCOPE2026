# Exact fibers of the Lie commutator on three-by-three triangular matrices

## Finding

Let \(k=\mathbb F_q\) be any finite field, with \(q\ge2\), and let \(T_3(k)\) denote its six-dimensional algebra of upper triangular \(3\)-by-\(3\) matrices. For each strictly upper triangular target
\[
Z=\begin{pmatrix}0&u&w\\0&0&v\\0&0&0\end{pmatrix},
\]
write \(F_q(u,v,w)\) for the number of ordered pairs \((X,Y)\in T_3(k)^2\) satisfying the **Lie commutator** equation \(XY-YX=Z\). Put
\[
M_0=q^3+q^2-q,\qquad M_1=q^3-q,\qquad M(u)=\begin{cases}M_0&u=0,\\M_1&u\ne0.\end{cases}
\]
Then **every fiber is nonempty**, and the complete fiber formula is
\[
\boxed{F_q(u,v,w)=q^3M(u)M(v)+\mathbf1_{u=v=0}\bigl(q^8\mathbf1_{w=0}-q^7\bigr).}
\]
There are exactly four fiber values, in the following target strata:

| Target stratum | Fiber size | Number of targets |
| --- | ---: | ---: |
| \(u=v=w=0\) | \(q^3M_0^2+q^8-q^7\) | \(1\) |
| \(u=v=0,\ w\ne0\) | \(q^3M_0^2-q^7\) | \(q-1\) |
| Exactly one of \(u,v\) is nonzero | \(q^3M_0M_1\) | \(2q(q-1)\) |
| \(uv\ne0\) | \(q^3M_1^2\) | \(q(q-1)^2\) |

For uniformly random independent \(X,Y\), the two simple-root commutator entries \(U=[X,Y]_{12}\) and \(V=[X,Y]_{23}\) are **independent**. The central entry \(W=[X,Y]_{13}\) is conditionally uniform whenever \((U,V)\ne(0,0)\). Quantitatively, with \(\operatorname{Unif}(k)\) denoting the uniform law on \(k\),
\[
\boxed{\left\|\mathcal L(U,V,W)-\mathcal L(U)\otimes\mathcal L(V)\otimes\operatorname{Unif}(k)\right\|_{\rm TV}=\frac{q-1}{q^5}.}
\]
Thus the entire defect of central-coordinate uniformity is concentrated over the zero simple-root pair.

## Assumptions and scope

The field \(k\) is any finite field, including characteristic two. The bracket is the additive algebra commutator \(XY-YX\), **not** the multiplicative group commutator \(XYX^{-1}Y^{-1}\). Both matrices \(X,Y\) range over the full upper triangular algebra, and neither is required to be invertible. All strict-upper-triangular targets occur, and no other target can occur because a commutator of upper triangular matrices has zero diagonal. Counts distinguish ordered pairs. The theorem concerns the finite-field cardinalities, not the schemes of these fibers.

## Proof

Write
\[
X=\begin{pmatrix}a&x&z\\0&b&y\\0&0&c\end{pmatrix},\qquad
Y=\begin{pmatrix}d&s&t\\0&e&h\\0&0&f\end{pmatrix}.
\]
Set \(\alpha=a-b\), \(\beta=b-c\), \(\gamma=d-e\), \(\delta=e-f\), and introduce four vectors in \(k^2\):
\[
A=(-\gamma,\alpha),\quad B=(-\delta,\beta),\quad S=(x,s),\quad T=(y,h).
\]
Put \(R=(z,t)\). Matrix multiplication gives exactly
\[
 u=A\cdot S,\qquad v=B\cdot T,\qquad
 w=(A+B)\cdot R+\det(S,T). \tag{1}
\]
For every prescribed \((\alpha,\beta,\gamma,\delta)\), there are exactly \(q^2\) choices of the six diagonal entries \((a,b,c,d,e,f)\), namely the free choices of \(c,f\). Thus the original fiber is \(q^2\) times the number of \((A,B,S,T,R)\) satisfying (1).

For \(A\in k^2\), define \(N_A(t)=\#\{S\in k^2:A\cdot S=t\}\). If \(A\ne0\), then \(N_A(t)=q\) for every \(t\). If \(A=0\), then \(N_0(0)=q^2\) and \(N_0(t)=0\) for nonzero \(t\). Summing over \(A\) shows
\[
\sum_{A\in k^2}N_A(t)=M(t),\qquad
\sum_{A\in k^2}N_A(u)N_{-A}(v)
=q^2(q^2-1)+q^4\mathbf1_{u=v=0}.\tag{2}
\]

Separate \(A+B\ne0\) from \(B=-A\). In the first case, for fixed \(A,B,S,T,w\), the final equation in (1) has exactly \(q\) solutions \(R\); its contribution to the fiber is
\[
q^3\left(M(u)M(v)-\sum_A N_A(u)N_{-A}(v)\right).\tag{3}
\]
In the second case, \(R\) is arbitrary (\(q^2\) choices), and the remaining determinant must equal \(w\). Write
\[
 H(u,v,w)=\#\{(A,S,T)\in(k^2)^3:A\cdot S=u,\ -A\cdot T=v,\ \det(S,T)=w\}.
\]
Its contribution is \(q^4H(u,v,w)\). We compute \(H\) without assuming any characteristic restrictions. When \(A\ne0\), take a coordinate change making \(A\) the first coordinate functional. The two dot-product constraints fix the first coordinates of \(S,T\) to \(u,-v\); the determinant condition is then a nonzero scalar multiple of a single linear equation in the remaining two coordinates with coefficients \((u,v)\). Consequently, for \((u,v)\ne(0,0)\), each nonzero \(A\) contributes exactly \(q\) solutions, while \(A=0\) contributes none:
\[
H(u,v,w)=q(q^2-1)\qquad\bigl((u,v)\ne(0,0)\bigr).\tag{4}
\]
For \(u=v=0\), any nonzero \(A\) forces \(S,T\) to lie on its one-dimensional kernel, hence their determinant is zero; each such \(A\) contributes \(q^2\) solutions at \(w=0\). At \(A=0\), a prescribed nonzero determinant occurs in exactly \(|\operatorname{SL}_2(k)|=q(q^2-1)\) matrices of columns \((S,T)\); determinant zero occurs in \(q^3+q^2-q\) matrices. Therefore
\[
 H(0,0,w)=\begin{cases}
 q^4+q^3-q,&w=0,\\
 q(q^2-1),&w\ne0.
 \end{cases}\tag{5}
\]
Substituting (2), (4), and (5) into (3) plus \(q^4H\) yields the boxed formula. The four strata and their multiplicities follow because \(u,v,w\) range independently over \(k\), and all four displayed values are strictly positive. They are pairwise distinct: in the table order the successive differences are \(q^8\), \(q^5(q^3-q)\), and \(q^5M_1\), each positive.

For the probability statement, summing the fiber formula over \(w\) cancels the correction and gives
\[
 \#\{(X,Y):U=u,V=v\}=q^4M(u)M(v).
\]
Since \(\sum_{t\in k}M(t)=q^4\), division by the sample-space size \(q^{12}\) proves independence and \(\Pr(U=u)=M(u)/q^4\). The product law with an independent uniform \(W\) assigns \(q^3M(u)M(v)\) pairs per target. The deviations of the actual unnormalized fibers from these values are \(q^8-q^7\) at \((0,0,0)\), \(-q^7\) at each \((0,0,w)\) with \(w\ne0\), and zero elsewhere. Half the sum of the absolute deviations divided by \(q^{12}\) is \((q-1)/q^5\), as claimed.

## Verification

The included standalone standard-library program `check_commutator.py` can be run with `python3 check_commutator.py`. It directly enumerates all \(q^{12}\) ordered matrix pairs for \(q=2\) and \(q=3\), with matrix-coordinate arithmetic independent of the proof's counting argument. It additionally exhausts all \(q^8\) choices of the four vectors \(A,B,S,T\) for \(q=4\) and \(q=5\), summing the remaining choices directly; the \(q=4\) test implements the extension field by polynomial arithmetic. For every field it compares every target fiber against the theorem and checks that the fibers sum to \(q^{12}\). Expected success marker: `TRIANGULAR_BRACKET_FIBER_CENSUS_OK q=2,3,4,5`.

As explicit audit examples, the four fiber sizes are \(928,672,480,288\) for \(q=2\), occurring with multiplicities \(1,1,4,2\), and \(33777,27216,21384,15552\) for \(q=3\), occurring with multiplicities \(1,2,12,12\), respectively. These finite tests check implementation and boundary behavior, but the proof above applies to every finite field.

## Relationship to prior work

Britnell and Wildon [1] study *which full-matrix similarity classes contain commuting representatives*, with results based on centralizer classes and nilpotent partitions. This is not the same counting problem: it neither fixes the strict-upper-triangular Lie-bracket target nor counts every fiber of that bracket map on the triangular algebra. Goodwin and Röhrle [2] analyze components of *zero-bracket commuting varieties* in nilradicals over algebraically closed fields; their theorems do not yield these finite-field nonzero-target fiber distributions. Wang, Zhu, and Rou [3] classify commutativity-preserving maps on strictly triangular spaces, rather than distributions of bilinear brackets on the full triangular algebra. Kaur, Sharma, and Singh [4] calculate branching matrices and commuting probabilities of **invertible** triangular and unitriangular *groups* in odd characteristic; these data concern simultaneous commuting tuples and group conjugacy, not the individual nonzero values of the **additive** algebra bracket when singular matrices are admitted.

De Mello [5] proves that the image of every multilinear polynomial on \(3\)-by-\(3\) upper triangular matrices over an infinite field is one of four specified ideals, including the strictly triangular radical for the ordinary commutator. Gargate and de Mello [6] extend image classification to all upper triangular sizes over infinite fields. Consequently **image surjectivity is existing work in the infinite-field setting**, and is not claimed as novel. These image-classification theorems give no finite-field counts of the preimages of individual commutator values or conditional output laws. The present count independently establishes finite-field surjectivity as a by-product.

The novelty claim is therefore specifically the complete four-stratum nonzero/zero Lie-bracket fiber distribution and its localized uniformity defect, not the general existence or structure of commuting pairs, nor the fact that a triangular commutator is strictly upper triangular. The sources below were checked at their accessible primary presentations; an unlocated exact equivalent in commutator-word distribution literature remains possible.

## Limitations

This result is for the \(3\)-by-\(3\) upper triangular algebra, not higher triangular sizes, not full matrix algebras, and not group commutators. It establishes finite-field fiber cardinalities and the resulting probabilities, not geometric irreducibility, nonreduced scheme structure, or fibers over infinite fields. The program only exhausts the stated small fields. Historical priority remains subject to independent, broader literature review.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first public version 2010-01-06; *Journal of the London Mathematical Society* 83 (2011), 470–492. https://arxiv.org/abs/1001.0811
2. S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289, first public version 2012-09-06. https://arxiv.org/abs/1209.1289
3. D. Wang, M. Zhu, and J. Rou, *The group of commutativity preserving maps on strictly upper triangular matrices*, *Czechoslovak Mathematical Journal* 64 (2014), 335–350. https://dml.cz/handle/10338.dmlcz/144002
4. D. Kaur, U. B. Sharma, and A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493, first public version 2020-06-02. https://arxiv.org/abs/2006.01493
5. T. C. de Mello, *The image of multilinear polynomials evaluated on 3 × 3 upper triangular matrices*, arXiv:1910.05469v1, first public version 2019-10-12. https://arxiv.org/abs/1910.05469
6. I. Gonzales Gargate and T. C. de Mello, *Images of multilinear polynomials on n × n upper triangular matrices over infinite fields*, arXiv:2106.12726v1, first public version 2021-06-24. https://arxiv.org/abs/2106.12726
