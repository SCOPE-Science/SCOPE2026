# Exact subalgebra commutativity degree of finite Heisenberg Lie algebras

## Statement

Let \(q\) be a prime power and let
\[
H_m(q)=V\oplus \mathbb F_q z,\qquad \dim_{\mathbb F_q}V=2m,
\]
where \(V\) carries a nondegenerate alternating form \(\omega\) and
\[
[u+az,v+bz]=\omega(u,v)z.
\]
Write \({n\brack r}_q\) for the Gaussian binomial coefficient and define
\[
I_{m,r}(q)={m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1),
\]
the number of totally isotropic \(r\)-subspaces of a \(2m\)-dimensional symplectic space; set \(I_{m,r}=0\) outside \(0\le r\le m\). Define
\[
D_{M,a,k}(q)=\sum_{j=0}^{\min(a,k)}(-1)^j q^{\binom j2}{a\brack j}_q I_{M-j,k-j}(q).
\]
Then the number of Lie subalgebras of \(H_m(q)\) is
\[
N_m(q)=\sum_{d=0}^{2m}{2m\brack d}_q+\sum_{r=0}^{m}q^r I_{m,r}(q),
\]
and the number of ordered nonpermuting pairs of subalgebras is
\[
E_m(q)=\sum_{r,s=0}^{m}\ \sum_{t=0}^{\min(r,s)}
I_{m,r}(q){r\brack t}_q q^{r+s-t}
\left(
D_{m-t,r-t,s-t}(q)-q^{(r-t)(s-t)}I_{m-r,s-t}(q)
\right).
\]
Consequently the subalgebra commutativity degree is exactly
\[
\boxed{\operatorname{sd}(H_m(q))=1-\frac{E_m(q)}{N_m(q)^2}.}
\]

For \(m=1\), this specializes to
\[
N_1=q^2+2q+4,\qquad E_1=q^3(q+1),
\]
so
\[
\operatorname{sd}(H_1(q))=
\frac{3q^3+12q^2+16q+16}{(q^2+2q+4)^2},
\]
recovering the formula of Muhie--Otera--Russo when \(q=p\) is prime.

The first new explicit case is
\[
N_2=q^5+3q^4+5q^3+6q^2+4q+6
\]
and
\[
E_2=q^4(q+1)(q^2+1)(q^3+2q^2+4q+1),
\]
hence
\[
\boxed{
\operatorname{sd}(H_2(q))=
\frac{3q^9+12q^8+34q^7+62q^6+91q^5+111q^4+108q^3+88q^2+48q+36}
{(q^5+3q^4+5q^3+6q^2+4q+6)^2}.}
\]

For fixed \(m\), the large-field limit has a sharp rank transition:
\[
\boxed{
\lim_{q\to\infty}\operatorname{sd}(H_m(q))=
\begin{cases}
0,&m=1,2,\\
5/9,&m=3,\\
1,&m\ge4,
\end{cases}}
\]
where \(q\) ranges over prime powers.

For odd prime \(p\), the Lazard correspondence therefore gives the same exact formula for the subgroup commutativity degree of the exponent-\(p\) extraspecial Heisenberg group of order \(p^{2m+1}\).

## Proof

Let \(Z=\mathbb F_qz\) and let \(\pi:H_m(q)\to V\) be the quotient map.

### 1. Classification and enumeration of subalgebras

If a subalgebra \(A\) contains \(z\), then
\[
A=U\oplus Z
\]
for an arbitrary subspace \(U\le V\); conversely every such space is a subalgebra because all brackets lie in \(Z\). These contribute
\[
\sum_{d=0}^{2m}{2m\brack d}_q.
\]

If \(z\notin A\), then \(A\cap Z=0\), so \(\pi|_A\) is injective. Writing \(U=\pi(A)\), there is a unique linear functional \(f\in U^*\) with
\[
A=\Gamma_f(U):=\{u+f(u)z:u\in U\}.
\]
Closure under brackets is equivalent to \(\omega|_U=0\), since any nonzero bracket lies in \(Z\) while \(A\cap Z=0\). Thus \(U\) must be totally isotropic. There are \(I_{m,r}(q)\) choices for an isotropic \(r\)-space and \(q^r\) choices for \(f\), yielding the stated formula for \(N_m(q)\).

### 2. When two graph subalgebras fail to permute

Take
\[
A=\Gamma_f(U),\qquad B=\Gamma_g(W),\qquad T=U\cap W,
\]
with \(\dim U=r\), \(\dim W=s\), \(\dim T=t\). A direct calculation gives
\[
(A+B)\cap Z=(f-g)(T)z.
\]
Hence \(z\in A+B\) exactly when \(f|_T\ne g|_T\). Since \([A,B]\) is either \(0\) or \(Z\), the pair \((A,B)\) is nonpermuting exactly when
\[
f|_T=g|_T\quad\text{and}\quad \omega(U,W)\ne0.
\]
For fixed \(U,W,T\), the number of pairs \((f,g)\) agreeing on \(T\) is
\[
q^{r+s-t}.
\]

It remains to count the relevant isotropic pairs \((U,W)\).

### 3. A symplectic disjointness count

Fix an isotropic \(a\)-space \(R\) in a \(2M\)-dimensional symplectic space. The number of isotropic \(k\)-spaces \(K\) with \(K\cap R=0\) is
\[
D_{M,a,k}(q).
\]
Indeed, for each \(j\)-space \(J\le R\), the number of isotropic \(k\)-spaces containing \(J\) is \(I_{M-j,k-j}(q)\), because \(J^\perp/J\) is symplectic of dimension \(2(M-j)\). Möbius inversion in the subspace lattice of \(R\), whose Möbius value on a \(j\)-space is \((-1)^j q^{\binom j2}\), gives the displayed formula for \(D_{M,a,k}\).

Now fix \(U\) and a \(t\)-space \(T\le U\). In the symplectic quotient \(T^\perp/T\), the spaces \(U/T\) and \(W/T\) are isotropic, and \(U\cap W=T\) is equivalent to their being disjoint. Therefore the total number of isotropic \(s\)-spaces \(W\) with \(U\cap W=T\) is
\[
D_{m-t,r-t,s-t}(q).
\]
Among them, those satisfying \(W\le U^\perp\) are counted by
\[
q^{(r-t)(s-t)}I_{m-r,s-t}(q).
\]
To see this, choose the isotropic image of \(W/T\) in the symplectic quotient \(U^\perp/U\), which has dimension \(2(m-r)\), and then choose an arbitrary linear lift into \(U/T\). The radical of the alternating form on \(U^\perp\) is \(U\), so every such lift remains isotropic.

There are \({r\brack t}_q\) choices for \(T\le U\), and \(I_{m,r}(q)\) choices for \(U\). Multiplying by the \(q^{r+s-t}\) compatible pairs of functionals and summing gives exactly \(E_m(q)\). Every pair with at least one subalgebra containing \(z\) is automatically permuting, so there are no further nonpermuting pairs. This proves the exact formula.

### 4. The rank transition

The central-containing stratum has size
\[
S_{2m}(q):=\sum_d {2m\brack d}_q=q^{m^2}+O(q^{m^2-1}),
\]
because \({2m\brack d}_q\) has degree \(d(2m-d)\), uniquely maximized at \(d=m\).

The graph stratum in isotropic dimension \(r\) has degree
\[
g_m(r)=\deg(q^r I_{m,r})=2mr-\frac32r(r-1).
\]
For \(m\ge4\), the real quadratic \(g_m(r)\) has maximum \((4m+3)^2/24<m^2\); hence, since \(g_m(r)\) is integral,
\[
\max_r g_m(r)\le m^2-1.
\]
Thus almost all subalgebras contain \(z\), and every pair involving one of them permutes. Therefore \(E_m(q)=o(N_m(q)^2)\) and \(\operatorname{sd}(H_m(q))\to1\).

For \(m=1\) and \(m=2\), the formulas above have respectively
\[
N_1(q)\sim q^2,\qquad N_1(q)^2-E_1(q)\sim3q^3,
\]
and
\[
N_2(q)\sim q^5,\qquad N_2(q)^2-E_2(q)\sim3q^9,
\]
so both limits are zero.

For \(m=3\), the central stratum and the graph strata \(r=2,3\) all have degree \(9\), giving
\[
N_3(q)=3q^9+O(q^8).
\]
In the exact sum for \(E_3\), the four triples
\[
(r,s,t)=(2,2,0),(2,3,0),(3,2,0),(3,3,0)
\]
are precisely the degree-\(18\) contributions, each with leading coefficient \(1\). Hence
\[
E_3(q)=4q^{18}+O(q^{17}),
\]
and the limit is \(1-4/9=5/9\).

## Verification

The accompanying script evaluates the exact finite sums and independently enumerates every vector subspace of \(H_2(2)\). It finds 374 vector subspaces, 158 Lie subalgebras, and 18,964 ordered permuting pairs out of \(158^2=24,964\), exactly agreeing with the formula; hence there are 6,000 nonpermuting ordered pairs.

For \(m=1\), the formula reduces identically to Theorem 1.2 of Muhie--Otera--Russo. Their paper explicitly poses the values of \(\operatorname{sd}(\mathfrak h(m))\) and proves the displayed formula only for \(\mathfrak h(1)\).

## Literature context and limitations

Muhie, Otera and Russo introduced the subalgebra commutativity degree and, in arXiv:2609.19086v1, compute the three-dimensional Heisenberg case \(\mathfrak h(1)\); they also prove that Lazard correspondence preserves this degree for the class-\(<p\) situation. Their paper explicitly defines \(\mathfrak h(m)\) for arbitrary \(m\) and asks for its values, but the Heisenberg theorem and proof treat \(m=1\) only.

Shen and Voll, arXiv:2605.23003, give explicit subalgebra zeta functions for higher Heisenberg Lie lattices over compact discrete valuation rings. That is a different enumeration problem: finite-index lattices over a DVR, not permuting pairs of subalgebras of \(H_m(\mathbb F_q)\). Their symplectic viewpoint is nevertheless closely related background.

The ordinary element commutativity degree of finite Heisenberg Lie algebras is already known and is a different invariant: it samples pairs of elements rather than pairs of subalgebras. The present claim is only about the subalgebra commutativity degree introduced in arXiv:2609.19086.

Originality is asserted only to the best of our knowledge. Searches for the exact invariant together with higher Heisenberg algebras, \(\mathfrak h(m)\), extraspecial groups, and symplectic-subspace formulations found no prior exact formula or the \(0,0,5/9,1\) rank transition. The full text of M. Tărnăuceanu, *Subgroup commutativity degrees of finite groups*, J. Algebra 321 (2009), 2508--2520, DOI 10.1016/j.jalgebra.2009.02.010, was not inspected; its broad title and general relevance make it the most plausible inaccessible source capable of containing an equivalent prime-field group-theoretic special case. Available descriptions state that it gives explicit formulas for selected families, and targeted searches coupling that paper with extraspecial/Heisenberg terminology did not expose such a formula. This leaves a residual originality risk for the odd-prime extraspecial-group corollary, but not evidence of known coverage. The general finite-field Lie-algebra formula and the large-field rank transition were not located in the searched literature.

## References

1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1 (2026), https://arxiv.org/abs/2609.19086.
2. J. Shen, C. Voll, *Symplectic lattice counting and zeta functions of higher Heisenberg groups*, arXiv:2605.23003 (2026), https://arxiv.org/abs/2605.23003.
3. A. Shamsaki, A. Erfanian, M. Parvizi, *On the commutativity degree of a finite-dimensional Lie algebra*, arXiv:2406.10064; related element-level Heisenberg formula, https://arxiv.org/abs/2406.10064.
4. M. Tărnăuceanu, *Subgroup commutativity degrees of finite groups*, J. Algebra 321 (2009), 2508--2520, DOI:10.1016/j.jalgebra.2009.02.010.
