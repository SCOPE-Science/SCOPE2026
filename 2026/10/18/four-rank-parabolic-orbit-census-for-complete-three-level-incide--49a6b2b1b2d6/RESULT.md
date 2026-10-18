# Four-rank parabolic orbit census for complete three-level incidence algebras

## Finding

Let \(q\) be a prime power and let \(a,b,c\geq1\) be integers. For the vector spaces \(X=\mathbb F_q^a\), \(Y=\mathbb F_q^b\), \(Z=\mathbb F_q^c\), consider the nilpotent radical \(J\) consisting of all matrices
\[
N(A,B,C)=\begin{pmatrix}0&A&C\\0&0&B\\0&0&0\end{pmatrix},\quad
A:Y\to X,\ B:Z\to Y,\ C:Z\to X.
\]
The block upper-triangular parabolic subgroup \(P\leq \operatorname{GL}_{a+b+c}(\mathbb F_q)\) conjugates \(J\) into itself. This is also the radical of the incidence algebra of the ordinal sum of three antichains of sizes \(a,b,c\), respectively; the theorem is for this *complete* three-level poset, not for arbitrary height-three posets.

Define four integers for each \(N\):
\[
u=\operatorname{rank} A,\quad v=\operatorname{rank} B,\quad
t=\operatorname{rank}(AB),\quad
w=\operatorname{rank}\bigl(\overline C:\ker B\to X/\operatorname{im} A\bigr).
\]
Here \(\overline C(z)=Cz+\operatorname{im}A\). The four integers are conjugacy invariants, and two elements of \(J\) are \(P\)-conjugate **if and only if all four coincide**. Precisely the tuples satisfying
\[
0\leq u\leq\min(a,b),\quad0\leq v\leq\min(b,c),\quad
\max(0,u+v-b)\leq t\leq\min(u,v),\quad
0\leq w\leq\min(a-u,c-v)
\]
occur. Every admissible tuple constitutes one orbit.

For integers \(0\leq k\leq n\), put \(G_q(n,k)={n\brack k}_q\), the Gaussian binomial coefficient, and \(I_q(n,k)=\prod_{j=0}^{k-1}(q^n-q^j)\), the number of injections \(\mathbb F_q^k\hookrightarrow\mathbb F_q^n\). Write \(R_q(m,n,k)=G_q(m,k)I_q(n,k)\) for the number of rank-\(k\) linear maps \(\mathbb F_q^n\to\mathbb F_q^m\). Empty products are one. All factors below are defined for admissible tuples.

**Exact orbit cardinality:**
\[
\begin{aligned}
\mathcal O_q(a,b,c;u,v,t,w)={}&G_q(b,u)I_q(a,u)\\
&\cdot G_q(b-u,v-t)G_q(u,t)q^{t(b-u-v+t)} I_q(c,v)\\
&\cdot q^{ac-(a-u)(c-v)}R_q(a-u,c-v,w).
\end{aligned}
\]
Thus the full orbit-size multiset, including multiplicities of equal sizes, follows by enumerating the admissible quadruples; summing all these cardinalities yields \(q^{ab+bc+ac}\).

The number of orbits is independent of \(q\):
\[
K(a,b,c)=\sum_{u=0}^{\min(a,b)}\sum_{v=0}^{\min(b,c)}
\bigl(\min(u,v)-\max(0,u+v-b)+1\bigr)
\bigl(\min(a-u,c-v)+1\bigr).
\]
For equal levels \(a=b=c=n\), this evaluates to
\[
K(n,n,n)=
\begin{cases}
(m+1)^4,&n=2m,\\
\dfrac{(m+1)(m+2)(2m^2+6m+5)}2,&n=2m+1.
\end{cases}
\]
In particular, the first balanced counts for \(n=1,2,3,4,5\) are \(5,16,39,81,150\).

For each orbit, \(\operatorname{rank}N=u+v+w\) and \(\operatorname{rank}N^2=t\), hence its Jordan partition is
\[
\bigl(3^t,\;2^{u+v+w-2t},\;1^{a+b+c-2(u+v+w)+t}\bigr).
\]
A useful factorization is that for uniformly selected \(A,B,C\), conditional on \((u,v)\), the ranks \(t\) and \(w\) are independent; the displayed orbit formula makes their complete joint distribution explicit.

## Assumptions and scope

The coefficient field is any finite field, including characteristic two. The three levels are fully comparable in order, each level individually an antichain, and each block has positive dimension. The term *orbit* means conjugacy by the entire invertible upper-block-triangular parabolic group over \(\mathbb F_q\), not conjugacy by its unipotent radical or by the whole general linear group. The algebraic classification and counting do not require algebraic closedness.

## Proof

**1. Classification of pairs.** Two pairs \((A,B)\) under independent base changes on \(X,Y,Z\) are classified by \((u,v,t)\). Write \(U=\ker A\) (dimension \(b-u\)) and \(W=\operatorname{im}B\) (dimension \(v\)) in \(Y\). The restriction of \(A\) to \(W\) has rank \(t\), so \(\dim(U\cap W)=v-t\). Subspace pairs of these three dimensions form one \(\operatorname{GL}(Y)\)-orbit; then \(A\) is an arbitrary injection \(Y/U\hookrightarrow X\), and \(B\) an arbitrary surjection \(Z\twoheadrightarrow W\). The independent \(\operatorname{GL}(X)\) and \(\operatorname{GL}(Z)\) actions are transitive on these choices. The admissible inequalities for \((u,v,t)\) are precisely the intersection dimension inequalities.

**2. The residual long block.** With \(A,B\) fixed, unipotent upper-block transformations alter \(C\) by arbitrary sums of the form \(SB+AT\) with \(S:Y\to X\), \(T:Z\to Y\) (the signs are immaterial). The kernel of the natural restriction/quotient homomorphism
\[
\operatorname{Hom}(Z,X)\longrightarrow\operatorname{Hom}(\ker B,X/\operatorname{im}A)
\]
is exactly \(\operatorname{Hom}(Y,X)B+A\operatorname{Hom}(Z,Y)\): a map whose restriction to \(\ker B\) has image in \(\operatorname{im}A\) is the sum of a map with image in \(\operatorname{im}A\) and a map factoring through \(Z/\ker B\cong\operatorname{im}B\). Thus the quotient has dimension \((a-u)(c-v)\). The Levi stabilizer of \((A,B)\) induces the **full independent** general linear actions on \(X/\operatorname{im}A\) and \(\ker B\), by extending arbitrary chosen automorphisms of these complementary summands while fixing the injective and surjective parts. Consequently the quotient orbits are classified exactly by the rank \(w\). This proves both necessity and sufficiency, and the \(w\)-range.

**3. Count by subspaces and injections.** There are \(G_q(b,u)\) choices for \(U=\ker A\), followed by \(I_q(a,u)\) choices for \(A\). With \(U\) fixed, count \(v\)-dimensional \(W\) satisfying \(\dim(U\cap W)=v-t\): choose the intersection in \(U\), choose the projected \(t\)-space in \(Y/U\), and choose its graph lift. This gives
\[
G_q(b-u,v-t)G_q(u,t)q^{t(b-u-v+t)}.
\]
For each \(W\), there are \(I_q(c,v)\) surjections \(Z\to W\). Finally \(\overline C\) can be any linear map from the \((c-v)\)-space \(\ker B\) to the \((a-u)\)-space \(X/\operatorname{im}A\). The restriction/quotient map has constant fiber size \(q^{ac-(a-u)(c-v)}\), and the number of its rank-\(w\) targets is \(R_q(a-u,c-v,w)\). Multiplication gives the formula. Because each tuple is one orbit, the count is also the orbit cardinality. Partitioning the whole space yields the total-mass identity.

**4. Rank and Jordan form.** The image of \(N:Y\oplus Z\to X\oplus Y\) projects onto \(\operatorname{im}B\) with dimension \(v\). Its kernel under this projection consists of the sum of \(\operatorname{im}A\) and the image of \(C(\ker B)\), of dimension \(u+w\). Thus \(\operatorname{rank}N=u+v+w\). Direct multiplication gives \(N^2\) with sole nonzero block \(AB\), so \(\operatorname{rank}N^2=t\); the counts of Jordan blocks of sizes three, two and one follow by standard rank differences for index-at-most-three nilpotent operators. For fixed \(A,B\), independent uniform \(C\) induces a uniform quotient map, whose rank distribution depends only on \((u,v)\); hence conditional independence of \(t\) and \(w\) given \((u,v)\).

**5. Balanced orbit polynomial.** For \(a=b=c=n\), set \(m=\max(u,v)\), \(\ell=\min(u,v)\) and \(h=n-m+1\). There are \(\min(\ell+1,h)\) admissible \(t\)-values and exactly \(h\) admissible \(w\)-values. Counting the ordered pairs with maximum \(m\) gives
\[
K(n,n,n)=\sum_{m=0}^n h\left(2\sum_{\ell=0}^{m}\min(\ell+1,h)-\min(m+1,h)\right).
\]
For \(m\le n/2\), the summand simplifies to \((n-m+1)(m+1)^2\); for \(m\ge n/2\), it simplifies to \((n-m+1)^2(3m-n+1)\). At equality these coincide. Summing the two elementary cubic sequences separately for even and odd \(n\) gives the displayed closed forms.

## Verification

The companion file `three_layer_rank_checker.py` is self-contained Python 3. It separately constructs all finite-field block triples for 13 small field/dimension configurations, computes \((u,v,t,w)\) using Gaussian elimination, and compares each resulting histogram with the formula and the total mass. It also explicitly constructs upper-block-triangular conjugacy actions for four small cases and checks that the rank fibers are exactly the parabolic orbits. The successful output terminates with `ALL_THREE_LAYER_RANK_CHECKS_PASSED 13` and `ALL_PARABOLIC_ORBIT_CHECKS_PASSED`. These checks are finite corroborations, not an infinite proof; the general proof is Steps 1–5 above.

## Relationship to prior work

Goodwin, Hille and Röhrle (2007) already give representation-theoretic orbit classifications and finite-orbit criteria for parabolics on metabelian nilradicals. Thus **finiteness of the orbit set is not claimed as new**, nor is the existence of a quiver-theoretic parametrization. Fuchs and Kirillov (2022) study the Jordan-type distribution of strictly upper-triangular finite-field matrices. Karp and Thomas (2022) and Bardestani, Mallahi-Karai, Ram and Salmasian (2025, revised 2026) supply more general formulas for parabolic nilradical Jordan-type *marginals*. The present more finely labelled claim is the explicit four-integer parabolic-orbit partition, Gaussian-product cardinality of each labelled orbit, and equal-level orbit polynomial. Summing its strata by Jordan type recovers a case already covered in principle by the broader Jordan enumeration literature. These results must not be construed as independent discoveries of Jordan marginals or orbit finiteness.

## Limitations

Only three complete levels and full parabolic conjugacy are treated. Higher-level nilradicals may have infinitely many orbits or require different invariants. The orbit-size polynomial is not an enumeration of unipotent-radical conjugacy orbits. A historically equivalent four-rank orbit-size description might exist in older quiver/parabolic matrix literature; the inspected primary papers do not supply this explicit numerical statement, but that absence is not a uniqueness certificate. No independent mathematical audit has been performed.

## References

1. S. M. Goodwin, L. Hille and G. Röhrle, *Orbits of parabolic subgroups on metabelian ideals*, arXiv:0711.3711v1 (2007), https://arxiv.org/html/0711.3711v1.
2. D. Fuchs and A. Kirillov, *Jordan types of triangular matrices over a finite field*, arXiv:2204.00066v1 (2022), https://arxiv.org/html/2204.00066v1.
3. S. N. Karp and H. Thomas, *q-Whittaker functions, finite fields, and Jordan forms*, arXiv:2207.12590 (2022), https://arxiv.org/abs/2207.12590.
4. M. Bardestani, K. Mallahi-Karai, S. Ram and H. Salmasian, *Counting finite-field points of orbital varieties in ad-nilpotent ideals of type A*, arXiv:2503.15440v4 (2026 revision), https://arxiv.org/abs/2503.15440.
