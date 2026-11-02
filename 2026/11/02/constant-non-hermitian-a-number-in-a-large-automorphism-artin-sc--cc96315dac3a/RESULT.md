# Constant non-Hermitian \(a\)-number in a large-automorphism Artin–Schreier family

## Finding

Let \(k\) be an algebraically closed field of characteristic an odd prime \(p\ge5\). For \(a\in k\), write \(Y_a\) for the smooth projective curve with function field
\[
k(x,y),\qquad y^p-y=x^{p+1}+ax^2.
\]
Let \(\mathcal C\) be the \(p^{-1}\)-semilinear Cartier operator on \(H^0(Y_a,\Omega^1)\), and let \(a(Y_a)=\dim_k\ker\mathcal C\) denote the Jacobian \(a\)-number. Then
\[
\operatorname{rank}(\mathcal C)=
\begin{cases}
0,&a=0,\\
(p^2-1)/8,&a\ne0,
\end{cases}
\qquad
a(Y_a)=
\begin{cases}
p(p-1)/2,&a=0,\\
(p-1)(3p-1)/8,&a\ne0.
\end{cases}
\]
All members have genus \(p(p-1)/2\) and geometric \(p\)-rank zero. Thus the \(a\)-number is independent of the nonzero parameter, while jumping at the Hermitian member. The nonzero-parameter locus is the large-Heisenberg-automorphism locus described in Arakelian–Kian, Theorem 1.3.

## Assumptions and scope

Throughout, \(p\) is prime, \(p\ge5\), \(k\) is algebraically closed of characteristic \(p\), and \(a\) is arbitrary in \(k\). The formula computes the **one-step** Cartier rank, equivalently the Jacobian \(a\)-number, not all higher Cartier ranks or the full Ekedahl–Oort type. The polynomial \(f(x)=x^{p+1}+ax^2\) has degree \(p+1\), prime to \(p\), and has just one pole on \(\mathbf P^1_x\). This gives a single totally ramified point \(P_\infty\) and genus \(g=p(p-1)/2\) by the Artin–Schreier Riemann–Hurwitz formula. The Deuring–Shafarevich formula gives \(p\)-rank zero independently of \(a\).

## Proof

**1. Complete differential basis.** At the unique point \(P_\infty\),
\[
\operatorname{ord}_{P_\infty}(x)=-p,\quad
\operatorname{ord}_{P_\infty}(y)=-(p+1),\quad
\operatorname{ord}_{P_\infty}(dx)=p(p-1)-2.
\]
The last valuation follows by pulling back the differential \(dx\) from \(\mathbf P^1\) and using the different exponent \((p-1)(p+2)\). Consequently
\[
\mathcal B=\{\omega_{i,j}:=x^iy^j\,dx:\ i,j\in\mathbf Z_{\ge0},\ i+j\le p-2\}
\]
is a holomorphic basis: the valuation inequality is \(pi+(p+1)j\le p(p-1)-2\), which for \(0\le j\le p-2\) is equivalent to \(i+j\le p-2\). Its members have distinct pole orders because \(0\le j<p\), and it has \(p(p-1)/2=g\) elements.

**2. The Cartier action.** Put \(b=a^{1/p}\in k\), so \(b^p=a\). The identity \(y=y^p-(x^{p+1}+ax^2)\), together with \(\mathcal C(h^p\eta)=h\mathcal C(\eta)\) and \(\mathcal C(x^e\,dx)=0\) unless \(e\equiv p-1\pmod p\), gives the following explicit formula. Set \(w=i+2j\). If \(w<p-1\), then \(\mathcal C(\omega_{i,j})=0\). Otherwise put \(t=w-(p-1)\), and obtain
\[
\mathcal C(\omega_{i,j})=
\sum_{k=0}^{\lfloor t/2\rfloor}
(-1)^{j-k}\binom{j}{k}\binom{j-k}{t-2k}
 b^{j+k-t}\,\omega_{t-2k,k},
\]
with the convention that an impossible binomial coefficient contributes zero. In fact each indicated term has \(0\le t-2k\le j-k\); the exponents of \(b\) are nonnegative. To check the formula directly, expand
\[
y^j=\sum_{k=0}^{j}(-1)^{j-k}\binom jk(y^k)^p
(x^{p+1}+ax^2)^{j-k}.
\]
The \(x\)-exponent in the term where \(s\) copies of \(x^{p+1}\) are selected is \(i+ps+2(j-k)-s\). Because it lies in the permitted range, a Cartier contribution requires \(i+2(j-k)-s=p-1\), or \(s=t-2k\); the output exponent is then precisely \(s\). Semilinearity takes the \(p\)-th root of \(a^{j-k-s}\), explaining the power \(b^{j+k-t}\).

**3. Hermitian parameter.** If \(a=0\), then \(b=0\). Every term in the displayed Cartier formula contains the factor \(b^{j+k-t}\), where
\[
j+k-t=p-1-i-j+k\ge1+k>0
\]
by the basis constraint \(i+j\le p-2\). Thus every term vanishes, and \(\operatorname{rank}\mathcal C=0\).

**4. Nonzero parameter and polynomial evaluation blocks.** Assume \(a\ne0\). Write \(p=2r+1\). The Cartier image of a source of weight \(w=p-1+t\), where \(0\le t\le p-3=2r-2\), is spanned by basis vectors of output weight \(t\). Thus the matrix breaks into disjoint weight blocks. Set \(K=\lfloor t/2\rfloor\). The source columns in this block are indexed by
\[
j=t+1,\ldots,r+K,\qquad i=p-1+t-2j,
\]
so their number is \(N=r-\lceil t/2\rceil\); the target rows are indexed by \(k=0,\ldots,K\). All factorials below have arguments less than \(p\). The block entries are
\[
M_{k,j}=(-1)^{j-k}\frac{j!}{k!(t-2k)!(j-t+k)!}\,b^{j+k-t}.
\]
Nonzero row and column scalings reduce this block to \(1/(u+k)!\), where \(u=j-t\) ranges through the distinct integers \(1,\ldots,N\). Multiplying column \(u\) by \((u+K)!\) converts it into evaluation of
\[
P_k(u)=\prod_{h=k+1}^{K}(u+h),\qquad 0\le k\le K.
\]
These are monic polynomials of successive degrees \(K,K-1,\ldots,0\), hence form a basis for the polynomials of degree at most \(K\). Evaluation at the \(N\) distinct points \(1,\ldots,N\in\mathbf F_p\) has rank \(\min(N,K+1)\). Therefore each block has *exactly* the rank
\[
\rho_t=\min\bigl(r-\lceil t/2\rceil,\lfloor t/2\rfloor+1\bigr).
\]
The target weights of distinct blocks are disjoint, so their ranks add. Splitting the sum into even and odd \(t\) gives
\[
\operatorname{rank}(\mathcal C)=
\sum_{t=0}^{2r-2}\rho_t
=\frac{r(r+1)}2=\frac{p^2-1}{8}.
\]
Finally \(a(Y_a)=g-\operatorname{rank}(\mathcal C)\), proving both cases of the formula for every \(a\in k\).

## Verification

The standalone Python 3 checker `verify_cartier.py` builds the complete basis and Cartier matrix independently by binomial expansion and modular arithmetic, then uses row elimination over \(\mathbf F_p\). It returned `VERIFY_OK` for primes \(3,5,7,11,13,17,19\), comparing zero and nonzero coefficients; the known \(p=3\) case is a cross-check outside this theorem's \(p\ge5\) domain. It also verifies the independent block-rank sum. These finite tests are consistency checks; the all-primes and algebraically closed coefficient claims rest on the preceding proof.

## Relationship to prior work

Arakelian and Kian (2026, Theorem 1.3 and Corollary 1.5) identify the large automorphism groups and geometric \(p\)-rank-zero condition for this exact family, but do not state the Cartier ranks or \(a\)-numbers. Zhou (2019, Theorem 1.1) explicitly proves the rank-one, nonzero-parameter case for \(p=3\), which is **prior work**, not a new special case. Zhou also proves some lower bounds on the ranks for higher primes, without the complete uniform formula above. Borges–Niemann–Zini (2026, Example 3.7) give a different two-cover model of the non-Hermitian special case and its automorphisms, genus, and zero \(p\)-rank, but do not state its Cartier rank. Farnell–Pries (2012, Theorem 1.1) proves coefficient-independence under the condition that the characteristic is \(1\) modulo the least common multiple of the pole orders; here that order is \(p+1\), so the condition cannot hold. Booher–Cais (2018/2020, Corollary 6.32 and Section 7) provides general bounds and exact formulas when breaks divide \(p-1\), but not the coefficient-specific rank theorem for the present break \(p+1\). Literature searches did not locate an exact equivalent formula for \(p\ge5\). This is not a proof of historical uniqueness, and earlier computations under isomorphic models remain a residual priority risk.

## Limitations

Only the one-step Cartier rank and the resulting \(a\)-number are computed; no general claim is made about higher Cartier iterates, the Ekedahl–Oort type, Newton polygon, arithmetic Frobenius polynomial, or independence of moduli-isomorphism classes. The \(p=3\) instance is already known from Zhou and is intentionally excluded from the new all-prime claim. The possibility of unindexed prior calculations under alternate equations remains.

## References

1. N. Arakelian and D. Kian, *Algebraic curves admitting automorphism groups of large prime square order*, first posted 2026-08-13, arXiv:2608.13768, Theorem 1.3 and Corollary 1.5. https://arxiv.org/abs/2608.13768
2. Z. Zhou, *On the existence of curves with prescribed a-number*, first posted 2019-01-24, arXiv:1901.08375, Theorem 1.1 and proof, Section 2. https://arxiv.org/abs/1901.08375
3. S. Farnell and R. Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank*, first posted 2012-02-19, arXiv:1202.4183, Theorem 1.1. https://arxiv.org/abs/1202.4183
4. J. Booher and B. Cais, *a-Numbers of Curves in Artin-Schreier Covers*, first posted 2018-07-26, arXiv:1807.10313, Corollary 6.32 and Section 7. https://arxiv.org/abs/1807.10313
5. H. Borges, J. Niemann and G. Zini, *Double Artin-Schreier extensions of rational function fields with many lifted automorphisms*, first posted 2026-02-14, arXiv:2602.13925, Example 3.7. https://arxiv.org/abs/2602.13925
