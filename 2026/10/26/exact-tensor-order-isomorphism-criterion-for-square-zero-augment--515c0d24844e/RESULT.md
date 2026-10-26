# Exact tensor-order isomorphism criterion for square-zero augmented Rota–Baxter factors

## Finding

The oriented augmented Rota–Baxter tensor product of Guo–Xie–Zhang admits an exact **reversal-isomorphism classification** when both augmentation ideals have square-zero multiplication. Rank balance is necessary but generally not sufficient. The criterion below decides existence of **any** augmentation-preserving Rota–Baxter algebra isomorphism, not merely whether the ordinary tensor flip works.

**Theorem.** Let \(k\) be a field with \(\operatorname{char}k\ne2\), let \(\lambda\in k\), and let \(V,W\) be nonzero finite-dimensional \(k\)-vector spaces of dimensions \(m,n\ge1\). Form the split local augmented algebras \(A=k\oplus V\), \(B=k\oplus W\), with \(V^2=W^2=0\) and scalar-projection augmentations. Choose maps \(Q\in\operatorname{End}_k(V)\) and \(R\in\operatorname{End}_k(W)\) such that
\[
Q(Q+\lambda\operatorname{id}_V)=0,\qquad R(R+\lambda\operatorname{id}_W)=0.
\]
Extend them to normalized augmented weight-\(\lambda\) Rota–Baxter operators by \(P_A(1)=P_B(1)=0\), \(P_A|_V=Q\), \(P_B|_W=R\). For the oriented monoidal product \(\boxtimes\) defined below,
\[
(A,P_A)\boxtimes(B,P_B)\cong(B,P_B)\boxtimes(A,P_A)
\]
as augmented Rota–Baxter algebras **if and only if** one of the following mutually exclusive dimensional alternatives holds:

1. \(m=n\) and \(\operatorname{rank}Q=\operatorname{rank}R\).
2. \(m\ne n\) and either \(Q=R=0\), or \(Q=-\lambda\operatorname{id}_V\) and \(R=-\lambda\operatorname{id}_W\).

When \(\lambda=0\), the two alternatives within case 2 coincide.

**Sharp rank-balanced counterexample.** At weight zero take \(m=2\), \(n=4\), with \(Q\) one size-two nilpotent Jordan block and \(R\) two such blocks. The two orderings have the same dimension \(15\), the same operator rank \(7\), and their operators are similar as linear maps (both are square-zero), but the augmented Rota–Baxter algebras are **not** isomorphic. This is the minimum tensor-product dimension for such a *positive, strictly intermediate, rank-balanced* counterexample among these square-zero factors at weight zero.

For every rational \(s\) with \(0<s\le1/2\) at weight zero, and every rational \(s\) with \(0<s<1\) at nonzero weight, there exist factors of unequal radical dimensions and rank ratio \(s\) with nonisomorphic reversed products. Thus the full monoidal subcategory of finite-dimensional normalized augmented weight-\(\lambda\) Rota–Baxter algebras having that fixed rank ratio (together with the monoidal unit) cannot be braided. The theorem does not exclude braidings on smaller specially restricted subcategories.

## Assumptions and scope

Throughout, tensor products and dimensions are over a field \(k\) with \(2\ne0\); radical dimensions are positive and finite. The weight \(\lambda\) may vanish. An augmented Rota–Baxter algebra has a unital algebra augmentation \(\varepsilon\) satisfying \(\varepsilon P=0\); normalized means \(P(1)=0\). The weight-\(\lambda\) identity is
\[
P(x)P(y)=P\bigl(P(x)y+xP(y)+\lambda xy\bigr).
\]

For augmented algebras \((A,P_A,\varepsilon_A)\), \((B,P_B,\varepsilon_B)\), define \(e_B(b)=\varepsilon_B(b)1_B\) and, following [1],
\[
P_{A\boxtimes B}=P_A\otimes e_B+\operatorname{id}_A\otimes P_B.
\]
The underlying algebra is the ordinary tensor product and the augmentation is \(\varepsilon_A\otimes\varepsilon_B\). An isomorphism in the theorem must preserve the algebra product, unit, augmentation, and Rota–Baxter operator.

## Proof

**1. The factors satisfy the required identities.** In a square-zero ideal all products of two elements vanish, hence any linear map on the ideal satisfies its internal Rota–Baxter identity. To extend by zero on the unit, apply the weight-\(\lambda\) identity to \((1,v)\): its right side is \(Q(Q(v)+\lambda v)\), and its left side vanishes. Therefore \(Q^2+\lambda Q=0\) is precisely the extension condition; likewise for \(R\). This also agrees with [1, Theorem 2.11].

**2. Identify both tensor orderings inside one algebra.** Apply the ordinary flip to the second ordering and write both on
\[
C=A\otimes B=k1\oplus V\oplus W\oplus(V\otimes W).
\]
The radical \(M=V\oplus W\oplus(V\otimes W)\) satisfies \(M^2=V\otimes W\) and \(M^3=0\); only products between \(V\) and \(W\) contribute to \(M^2\). The two Rota–Baxter operators, denoted \(L\) and \(H\) for the two orders, act as follows:
\[
\begin{array}{c|cccc}
&k1&V&W&V\otimes W\\ \hline
L&0&Q&R&\operatorname{id}_V\otimes R\\
H&0&Q&R&Q\otimes\operatorname{id}_W.
\end{array}
\]
The two operators therefore agree on \(M/M^2\), but differ in general on \(M^2\).

**3. Radical-square rigidity when \(m\ne n\).** In \(M/M^2=V\oplus W\), squaring a lift of \(v+w\) gives exactly \(2v\otimes w\in M^2\). As \(2\ne0\) and a nonzero pure tensor over a field cannot vanish, the set of classes with zero square is precisely \(V\cup W\). This is intrinsic to \(C\), since changing the lift by an element of \(M^2\) does not change its square. Every augmentation-preserving algebra automorphism \(F\) of \(C\) must therefore permute the two maximal linear pieces \(V,W\). If \(m\ne n\), their different dimensions force them to be fixed separately. Thus the induced map on \(M/M^2\) has blocks \(S\in\operatorname{GL}(V)\), \(T\in\operatorname{GL}(W)\). Multiplicativity on products \(vw=v\otimes w\) forces
\[
F|_{M^2}=S\otimes T.
\]
Terms of \(F(v),F(w)\) lying in \(M^2\) cannot affect this identity because \(M^3=0\).

If \(FL=HF\), comparison on \(M/M^2\) gives \(SQ=QS\) and \(TR=RT\). Restricting the same identity to \(M^2\) yields
\[
(S\otimes T)(\operatorname{id}_V\otimes R)
=(Q\otimes\operatorname{id}_W)(S\otimes T).
\]
Using invertibility and the two commutation relations, this reduces to
\[
\operatorname{id}_V\otimes R=Q\otimes\operatorname{id}_W.
\]
Apply a functional \(\ell\in V^*\) with \(\ell(v)=1\) to \((Qv)\otimes w=v\otimes(Rw)\) to obtain \(Rw=\ell(Qv)w\) for all \(w\). Thus \(R=c\operatorname{id}_W\), and the equality then gives \(Q=c\operatorname{id}_V\). The quadratic relations imply \(c(c+\lambda)=0\), i.e. \(c=0\) or \(c=-\lambda\). Conversely both cases intertwine under the ordinary flip (see [1, Proposition 3.7]). This proves case 2.

**4. Equal dimensions.** Let \(r_Q=\operatorname{rank}Q\), \(r_R=\operatorname{rank}R\). By [1, Proposition 3.10], the ranks of the two tensor-order operators are \(r_Q+(m+1)r_R\) and \(r_R+(n+1)r_Q\). If \(m=n\), equality forces \(r_Q=r_R\). Conversely \(Q\) and \(R\) are similar when their dimensions and ranks agree: for \(\lambda=0\) both are square-zero and have the same number of size-two Jordan blocks; for \(\lambda\ne0\), both are diagonalizable with possible eigenvalues \(0,-\lambda\), with their multiplicities fixed by rank. Thus there exists \(f:V\to W\) satisfying \(fQ=Rf\). Extend \(f\) by the identity on scalar units to an augmented Rota–Baxter isomorphism \(A\to B\); its inverse gives an isomorphism \(B\to A\). Their tensor product, by naturality of \(\boxtimes\), is the required isomorphism between opposite orders. This proves case 1.

**5. Exact rank-balanced boundary.** At \(\lambda=0\), take \(m=2,n=4,r_Q=1,r_R=2\), with \(Q^2=R^2=0\). Formula [1, Proposition 3.10] yields \(1+3\cdot2=2+5\cdot1=7\). Both tensor-order maps are square-zero by Step 1 and the monoidal normalization theorem, hence identical rank implies linear similarity. Since \(m\ne n\) and neither map is zero, Step 3 rules out an augmented algebra isomorphism. For any strictly positive rank-balanced weight-zero example, \(0<r_Q/m=r_R/n\le1/2\). The smallest unequal positive dimensions realizing this are \(2,4\), so their tensor dimension \((2+1)(4+1)=15\) is minimal. For arbitrary rational \(s=a/b\in(0,1/2]\), choose \(m=b,n=2b\) and square-zero maps of ranks \(a,2a\). For nonzero weight and rational \(s=a/b\in(0,1)\), choose the same dimensions and projections of ranks \(a,2a\), multiplied by \(-\lambda\). Since \(b\ge2\), these are unequal dimensions and neither pair is a common scalar map, so the products are not isomorphic. The constant-ratio full monoidal subcategories exist by [1, Corollary 3.11], and the exhibited pair rules out a braiding there.

## Verification

The standalone file `verify.py` independently constructs the tensor-product algebra over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), implements both oriented operators, checks the Rota–Baxter identity on every ordered pair of basis elements, tests the quadratic operator relations, and independently computes matrix ranks. Eighteen parameter-field instances test zero and nonzero weights; the 15-dimensional rank-balanced counterexample gives rank \(7\) in both orderings. Run `python3 verify.py` and require the final line `VERIFY_OK`. Finite-field checks are not substitutes for the all-field proof in Steps 1–5.

## Relationship to prior work

Guo–Xie–Zhang [1] define the oriented product (Theorem 3.2), characterize normalized objects (Theorem 2.11), characterize cases where the ordinary flip works (Proposition 3.8), and obtain the necessary rank-ratio condition (Proposition 3.10 and Corollary 3.11). Their Theorem 3.12 rules out a braiding for the entire category using *unequal-rank* examples. Section 3.4 expressly leaves undecided whether a full monoidal subcategory with a fixed intermediate ratio can admit a braiding. The new classification above settles this issue for every positive intermediate ratio realizable in the square-zero-factor family and exhibits equal-rank, linearly similar tensor operators that cannot be conjugate by an augmented algebra isomorphism. It is not a claim that the underlying oriented monoidal product, the rank obstruction, or the extreme-ratio symmetric subcategories are new.

## Limitations

The exact classification is proved only for the two square-zero *factors*, with both radical dimensions positive, finite, and over fields of characteristic different from two. General augmented Rota–Baxter algebras may have nonzero radical products or nonnormalized operators; nothing in this theorem classifies their reversal-isomorphisms. The construction obstructs braidings on the **full** constant-ratio subcategory, not on all possible smaller subcategories. Although direct published coverage was not identified, implicit consequences of other algebra-automorphism classifications remain an originality risk. Independent external validation has not been performed.

## References

[1] L. Guo, Y. Xie, Y. Zhang, *Monoidal structure on Rota-Baxter algebras via augmentation, and free cocycle bialgebras*, arXiv:2610.17525v1, first posted 2026-10-13, https://arxiv.org/html/2610.17525v1 (especially Theorems 2.11, 3.2, 3.9, 3.12; Propositions 3.7, 3.8, 3.10; Corollary 3.11).
