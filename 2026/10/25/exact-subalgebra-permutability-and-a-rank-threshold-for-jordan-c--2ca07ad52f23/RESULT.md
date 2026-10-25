# Exact subalgebra permutability and a rank threshold for Jordan-chain Lie algebras

## Finding

For every prime power \(q\), integer \(r\geq2\), and scalar \(\lambda\in\mathbb F_q\), consider the \((r+1)\)-dimensional Lie algebra \(L_{r,\lambda}\) with basis \(h,e_1,\ldots,e_r\), all brackets between the \(e_i\) zero, and
\[
[h,e_i]=\lambda e_i+e_{i-1}\quad(1\leq i\leq r),\qquad e_0=0.
\]
The subalgebra lattice and the relation of permutability of two subalgebras are **independent of** \(\lambda\), under the canonical identification of their underlying vector spaces. In particular this relates the nilpotent standard filiform model \(\lambda=0\) to nonnilpotent solvable models \(\lambda\ne0\).

Write \(G_q(a,b)\) for the Gaussian binomial coefficient, the number of \(b\)-dimensional subspaces of \(\mathbb F_q^a\), and set
\[
\begin{aligned}
T_r(q)&=\sum_{d=0}^{r}G_q(r,d),\\
S_r(q)&=\sum_{j=0}^{r}q^{r-j},\\
H_{r,j}(q)&=\sum_{\ell=j}^{r}\sum_{k=0}^{j}
G_q(j,k)q^{(\ell-j)(j-k)}\quad(0\leq j\leq r).
\end{aligned}
\]
The exact number of Lie subalgebras, including the zero and whole subalgebras, is
\[
N_r(q)=T_r(q)+S_r(q).
\]
The exact number of **ordered** pairs of Lie subalgebras \((A,B)\) satisfying \([A,B]\subseteq A+B\) is
\[
\boxed{
P_r(q)=T_r(q)^2+2\sum_{j=0}^{r}q^{r-j}H_{r,j}(q)
+\sum_{t=1}^{r}(2t-1)q^{t+1}+2S_r(q)-1.
}
\]
Thus the subalgebra commutativity degree, using independent uniform choices among *all* Lie subalgebras, is \(\operatorname{sd}(L_{r,\lambda})=P_r(q)/N_r(q)^2\).

For fixed \(r\), as \(q\) grows through prime powers,
\[
\boxed{
\lim_{q\to\infty}\operatorname{sd}(L_{r,\lambda})=
\begin{cases}
0,&r=2,3,\\
\tfrac14,&r=4,\\
1,&r\geq5.
\end{cases}}
\]
The rank-one boundary has degree \(1\). In the first new threshold dimension \(r=4\), the exact rational function is
\[
\operatorname{sd}(L_{4,\lambda})=
\frac{q^8+6q^7+21q^6+43q^5+77q^4+87q^3+76q^2+48q+36}
{(2q^4+4q^3+5q^2+4q+6)^2}.
\]

## Assumptions and scope

The field is an arbitrary finite field \(\mathbb F_q\), including nonprime fields and characteristic two. The Lie bracket is the semidirect-product bracket associated with the linear operator \(\lambda I+J\), where \(Je_1=0\) and \(Je_i=e_{i-1}\) for \(i>1\). No invertibility or characteristic assumption is imposed. All subalgebras and vector-space dimensions are over \(\mathbb F_q\). Permutability means the vector-space sum is itself a Lie subalgebra, equivalently \([A,B]\subseteq A+B\); this is not merely the order-theoretic notion of a modular pair.

## Proof

**1. Scalar-shift invariance.** More generally, let \(D\) be any endomorphism of a vector space \(V\). On \(\mathbb F_qh\oplus V\) compare the semidirect-product brackets determined by \(D\) and \(D+cI\), for a scalar \(c\). For \(x=\alpha h+v\) and \(y=\beta h+w\),
\[
[x,y]_{D+cI}-[x,y]_D
=c(\alpha w-\beta v)=c(\alpha y-\beta x).
\]
If \(x,y\) belong to one vector subspace \(A\), the difference belongs to \(A\); consequently the two brackets define the same collections of subalgebras. If \(x\in A\) and \(y\in B\), the difference belongs to \(A+B\); consequently \([A,B]\subseteq A+B\) holds for one bracket precisely when it holds for the other. This proves the asserted independence of \(\lambda\). It suffices henceforth to work with \(D=J\).

**2. Classification of subalgebras.** Put \(V=\langle e_1,\ldots,e_r\rangle\) and \(W_j=\langle e_1,\ldots,e_j\rangle\) for \(0\leq j\leq r\). Every subspace \(U\leq V\) is a subalgebra, because \([V,V]=0\). Every subalgebra \(A\not\subseteq V\) has the uniquely determined form
\[
A=\mathbb F_q(h+a)\oplus W,
\]
where \(W=A\cap V\), \(a\) is determined modulo \(W\), and closure is equivalent to \(JW\subseteq W\). Since \(J\) is one nilpotent Jordan block, its invariant subspaces are exactly the chain \(W_0,\ldots,W_r\): identify \(V\) as the cyclic \(\mathbb F_q[t]\)-module \(\mathbb F_q[t]/(t^r)\) and use its ideals. For \(W=W_j\), there are exactly \(q^{r-j}\) distinct cosets \(a+W_j\). The inside and outside classes are disjoint. Counting the inside subspaces by dimension gives \(T_r(q)\); counting the outside forms gives \(S_r(q)\).

**3. Two subalgebras inside \(V\).** Each such pair permutes because its sum lies in the abelian ideal \(V\). These contribute \(T_r(q)^2\) ordered pairs.

**4. Mixed pairs.** Fix an outside subalgebra \(B=\mathbb F_q(h+a)\oplus W_j\) and an inside subalgebra \(U\leq V\). Their sum is a subalgebra if and only if \(J(U+W_j)\subseteq U+W_j\), hence if and only if \(U+W_j=W_\ell\) for a unique \(\ell\geq j\). For a fixed \(\ell\), put \(K=U\cap W_j\) with dimension \(k\). There are \(G_q(j,k)\) choices of \(K\). The map \(U\to W_\ell/W_j\) must be surjective, with kernel \(K\); after choosing \(K\), the choices of \(U\) are the graphs of arbitrary linear maps
\[
W_\ell/W_j\longrightarrow W_j/K,
\]
which number \(q^{(\ell-j)(j-k)}\). Summing over \(k\) and \(\ell\) yields exactly \(H_{r,j}(q)\) admissible inside subalgebras for any one outside subalgebra of type \(j\). Thus mixed ordered pairs contribute \(2\sum_{j=0}^{r}q^{r-j}H_{r,j}(q)\).

**5. Two outside subalgebras.** Consider \(A=\mathbb F_q(h+a)\oplus W_j\) and \(B=\mathbb F_q(h+b)\oplus W_k\), and set \(m=\max(j,k)\). Their sum equals
\[
A+B=\mathbb F_q(h+a)\oplus\bigl(W_m+\mathbb F_q(b-a)\bigr).
\]
If \(m=r\), the sum is automatically a subalgebra. If \(m<r\), the sum is a subalgebra precisely when the image of \(b-a\) in \(V/W_m\) spans a \(J\)-invariant line or is zero. Because the induced operator is a single nilpotent Jordan block, this is equivalent to
\[
b-a\in W_{m+1}.
\]
For \(j,k<r\), the number of ordered coset choices satisfying this condition is
\[
q^{r-j}\,q^{m+1-k}=q^{r+1-\min(j,k)}.
\]
Grouping the \(r^2\) pairs of indices by \(t=r-\min(j,k)\), the contribution from \(j,k<r\) is \(\sum_{t=1}^r(2t-1)q^{t+1}\). Pairs with at least one index equal to \(r\) contribute \(2(S_r(q)-1)+1\). Adding these pieces proves the formula for \(P_r(q)\).

**6. Limit theorem.** The Gaussian binomial \(G_q(r,d)\) is a polynomial of degree \(d(r-d)\) with leading coefficient \(1\). Therefore
\[
T_r(q)\sim c_rq^{\lfloor r^2/4\rfloor},
\qquad S_r(q)\sim q^r,
\]
where \(c_r=1\) for even \(r\) and \(c_r=2\) for odd \(r\). When \(r=2,3\), outside subalgebras of type \(j=0\) asymptotically dominate all subalgebras; two independent such choices permute with probability \(q^{1-r}\), so the total degree tends to zero. When \(r=4\), inside subalgebras and type-zero outside subalgebras each contribute asymptotically one half of all subalgebras. Inside-inside pairs always permute. Type-zero outside pairs permute with probability \(q^{-3}\); mixed inside/type-zero-outside pairs permute only if the inside subspace is one of the five \(J\)-invariant subspaces, whose proportion among \(T_4(q)\) subspaces tends to zero. Other outside types have negligible density. Thus the limit is \(1/4\). When \(r\geq5\), the inequality \(\lfloor r^2/4\rfloor>r\) makes inside subalgebras asymptotically predominant, so the degree tends to one. For \(r=1\), the operator has no nilpotent part and every pair permutes.

## Verification

Run the self-contained script `python3 verify.py` in the same directory. It enumerates every linear subspace of the small ambient vector spaces in reduced row-echelon form, determines Lie subalgebras by testing basis brackets, and tests every ordered pair directly. It compares counts with the displayed formulas for \((r,q)\) equal to \((1,2)\), \((2,2)\), \((2,3)\), \((2,5)\), \((3,2)\), \((3,3)\), and \((4,2)\), and checks scalar-shift invariance of the entire subalgebra set and permutability relation at ranks two and three. The run reports `VERIFY_OK`. Finite-field tests do not constitute proof for arbitrary \(r\) or \(q\); the general proof is above.

## Relationship to prior work

Muhie, Otera and Russo introduced the quantitative subalgebra commutativity degree for finite-field Lie algebras and gave formulas and bounds for selected families, notably the three-dimensional Heisenberg algebra and \(\mathfrak{sl}_2\). Their definition of *almost abelian* demands scalar action on the codimension-one abelian ideal; the nontrivial Jordan block here does not satisfy that condition. Their scalar-action degree-one result therefore does not cover this family.

The three-dimensional rank-two outcome agrees with the known Heisenberg calculation. The four-dimensional rank-three polynomial agrees with an earlier exact census of the standard filiform Lie algebra; it is a previously obtained low-dimensional case, not a separately novel claim. The new scope is the uniform formula in all ranks, its scalar-shift universality across nilpotent and nonnilpotent models, and the rank-four transition followed by rank-five predominance. The theorem concerns Lie-subalgebra permutability, not the distinct notion of elementwise commuting probability or other graph invariants.

## Limitations

The formula applies to a single full Jordan block, not an arbitrary semidirect-product action with several blocks or distinct eigenvalues. The asymptotics fix \(r\) while \(q\to\infty\); no joint-growth statement is made. Searches did not establish absence of every unindexed or historical equivalent. Older work on projectivizations of solvable Lie algebras may contain the scalar-shift observation; no novelty is claimed for that lemma alone. Independent external mathematical validation has not been performed.

## References

1. S. K. Muhie, D. E. Otera and F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086, first posted September 16, 2026. https://arxiv.org/abs/2609.19086
2. B. Kolman, *Semi-modular Lie algebras*, J. Sci. Hiroshima Univ. Ser. A-I **29** (1965), 149–163, cited for the classical scalar-action notion in the preceding paper.
3. A. A. Lashkhi, *Lattices with modular identity and Lie algebras*, Journal of Soviet Mathematics **38** (1987), 1823–1853, https://doi.org/10.1007/BF01088205. Its abstract concerns modular lattice classifications, not the present quantitative finite-field formulas.
