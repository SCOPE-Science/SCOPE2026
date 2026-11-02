# Rank-one Rota–Baxter census for rectangular-band semigroup algebras

## Finding

Fix integers \(m,n\geq1\), a finite field \(k=\mathbb F_q\), and the rectangular-band semigroup \(S_{m,n}=\{(i,j):1\leq i\leq m,\ 1\leq j\leq n\}\) with multiplication \((i,j)(h,\ell)=(i,\ell)\). Let \(A=k[S_{m,n}]\), and let \(B_{m,n}(q)\) denote the number of **nonzero, linear-rank-one**, weight-zero Rota–Baxter operators \(R:A\to A\), meaning

\[
R(x)R(y)=R(R(x)y+xR(y))\quad\text{for every }x,y\in A.
\]

Put \(N=mn\) and \(d=(m-1)(n-1)\). The exact count, valid in every characteristic, is

\[
\boxed{\begin{aligned}
B_{m,n}(q)={}&\frac{(q^d-1)(q^N-1)}{q-1}\\
&+\frac{q^d(q^{n-1}-1)(q^{N-m}-1)}{q-1}\\
&+\frac{q^d(q^{m-1}-1)(q^{N-n}-1)}{q-1}\\
&+q^{m+n-2}(q^{n-1}+q^{m-1}-2).
\end{aligned}}
\]

The first three terms count operators whose nonzero image generator is square-zero. The last term counts operators whose image generator has nonzero square proportional to itself. The formula is symmetric in \(m,n\), including the boundary cases \(m=1\) or \(n=1\). In particular, \(B_{1,1}(q)=0\), \(B_{2,2}(2)=35\), \(B_{2,2}(3)=164\), and \(B_{2,3}(2)=429\).

## Assumptions and scope

The semigroup algebra \(A\) has vector-space dimension \(N\), generally lacks an identity when \(mn>1\), and is not the usual matrix algebra. Identify it with \(m\times n\) coefficient arrays. Let \(\rho(a)\in k^m\) be the row-sum vector, \(\gamma(a)\in k^n\) the column-sum vector, and \(\tau(a)\) their common total sum. Direct use of the semigroup product gives

\[
ab=\rho(a)\gamma(b)^{\mathsf T}.
\]

Here a rank-one operator refers to the vector-space rank of \(R\), not the matrix rank of \(a\). Operators are individually labelled; no conjugation quotient is taken. All formulas apply to every prime power \(q\), including nonprime fields and characteristic two.

## Proof

**1. Universal rank-one reduction.** Every nonzero linear-rank-one map has a presentation \(R(x)=f(x)a\) with \(a\neq0\) and \(f\in A^*\setminus\{0\}\), unique up to \((a,f)\mapsto(ca,c^{-1}f)\) for \(c\in k^\times\). Substituting into the weight-zero identity and taking \(x,y\) with \(f(x)f(y)\neq0\) forces \(a^2=\lambda a\) for some \(\lambda\in k\). The remaining scalar identity is

\[
\lambda f(x)f(y)=f(x)f(ay)+f(y)f(xa).
\]

This is equivalent to \(f\circ L_a=\mu f\), \(f\circ R_a=\nu f\), with \(\mu+\nu=\lambda\), where \(L_a(x)=ax\) and \(R_a(x)=xa\). Necessity follows by restricting first to \(x\in\ker f\); sufficiency follows by substitution. As \(L_a^2=\lambda L_a\) and \(R_a^2=\lambda R_a\), their possible eigenvalues obey \(\mu^2=\lambda\mu\) and \(\nu^2=\lambda\nu\). Thus \(\lambda=0\) forces \(\mu=\nu=0\); for \(\lambda\neq0\), exactly \((\mu,\nu)=(\lambda,0)\) or \((0,\lambda)\) is possible. This statement includes characteristic two.

**2. Classify possible image generators.** Put \(u=\rho(a)\), \(v=\gamma(a)\), \(\alpha=\tau(a)\). The product rule gives \(a^2=uv^{\mathsf T}\), so \(a^2=0\) precisely when \(u=0\) or \(v=0\). In the complementary case, \(a^2=\lambda a\) holds precisely when \(\alpha\neq0\) and

\[
a=\alpha^{-1}uv^{\mathsf T},\qquad \lambda=\alpha.
\]

Indeed, the row sums of \(uv^{\mathsf T}=\lambda a\) give \(\alpha u=\lambda u\), so \(\lambda=\alpha\); conversely the displayed array has row and column sums \(u,v\) and square \(\alpha a\).

**3. Count square-zero generator pairs.** The linear map \(a\mapsto(u,v)\) is onto the subspace \(\{(u,v):\sum_i u_i=\sum_j v_j\}\), with fibers of size \(q^d\). Separate the mutually disjoint cases:

* \(u=v=0\) and \(a\neq0\): there are \(q^d-1\) generators, with \(L_a=R_a=0\), and \(q^N-1\) allowed nonzero functionals.
* \(u=0,v\neq0\): there are \(q^d(q^{n-1}-1)\) generators because \(\sum_jv_j=0\). Now \(L_a=0\), while \(R_a\) has rank \(m\). There are \(q^{N-m}-1\) nonzero functionals annihilating \(\operatorname{im}R_a\).
* \(v=0,u\neq0\): symmetrically \(q^d(q^{m-1}-1)\) generators, and \(q^{N-n}-1\) nonzero functionals annihilating \(\operatorname{im}L_a\).

For all these square-zero generators the rank-one reduction requires \(f(L_a A)=f(R_a A)=0\). Divide the resulting number of pairs \((a,f)\) by \(q-1\) to account for scalar equivalence; this gives exactly the first three terms.

**4. Count non-square-zero generator pairs.** For each \(\alpha\in k^\times\), independently choose \(u\in k^m\), \(v\in k^n\) with total sums \(\alpha\). There are \(q^{m+n-2}\) choices, each specifying a distinct \(a=\alpha^{-1}uv^{\mathsf T}\). Hence there are \((q-1)q^{m+n-2}\) non-square-zero generators. Now \(\alpha^{-1}L_a\) and \(\alpha^{-1}R_a\) are commuting projections of ranks \(n\) and \(m\). Their product has rank one because \(axa=\alpha\tau(x)a\). Their simultaneous \((1,0)\) and \((0,1)\) eigenspaces therefore have dimensions \(n-1\) and \(m-1\). The admissible nonzero dual eigenfunctionals comprise \((q^{n-1}-1)+(q^{m-1}-1)\) choices. Divide by \(q-1\) for the presentation ambiguity to obtain the last term. All cases have been exhausted.

## Verification

The included `verify_rectangular_band.py` uses the original multiplication table \((i,j)(h,\ell)=(i,\ell)\), not the row/column classification, to check the Rota–Baxter identity on every ordered basis pair for every nonzero rank-one linear map in seven small cases. It normalizes image vectors only to avoid scalar double-counting. Its finite fields are \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the latter implemented as \(\mathbb F_2[t]/(t^2+t+1)\)). The checker confirms both square-zero-image and non-square-zero-image contributions separately:

| \((m,n,q)\) | Square-zero image | Non-square-zero image | Total |
| --- | ---: | ---: | ---: |
| \((1,1,2)\) | 0 | 0 | 0 |
| \((1,2,3)\) | 2 | 6 | 8 |
| \((1,3,2)\) | 9 | 12 | 21 |
| \((2,2,2)\) | 27 | 8 | 35 |
| \((2,2,3)\) | 128 | 36 | 164 |
| \((2,2,4)\) | 375 | 96 | 471 |
| \((2,3,2)\) | 397 | 32 | 429 |

Run with `python3 verify_rectangular_band.py`; successful output ends in `RECTANGULAR_BAND_RANK_ONE_RB_OK`. The exhaustive checks do not prove the formula beyond their tested parameters; the preceding symbolic proof does.

## Relationship to prior work

Guo, Rosenkranz and Zheng classified weight-zero Rota–Baxter operators on semigroup algebras for semigroups of orders two and three, principally in characteristic zero [1]. That original article gives a general coefficient-equation setup but no rectangular-band count for arbitrary \(m,n\); the first genuinely two-sided rectangular band has four elements. Jian's construction from quasi-idempotent elements concerns specific left-multiplication operators and does not count rank-one maps on these algebras [2]. Gubarev counts operators on direct sums of fields, concentrating on nonzero weight; those algebras are commutative semisimple and are not the generally nonunital rectangular-band algebra [3]. Benito, Gubarev and Pozhidaev work with quadratic and simple algebras, not rectangular bands [4]. The familiar rank-one tensor reduction is not claimed as an original general principle; the exact rectangular-band stratification and all-characteristic census are the contributions here.

## Limitations

The theorem counts only vector-space-rank-one weight-zero Rota–Baxter operators, not arbitrary-rank maps, orbit classes under automorphisms, or nonzero weights. It does not classify all nonreduced scheme structures of the operator equations. A search and comparison of accessible primary sources found no formula implying this precise census; this does not establish absolute publication priority.

## References

[1] L. Guo, M. Rosenkranz and S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702, first posted 2014-02-15. https://arxiv.org/abs/1402.3702

[2] R.-Q. Jian, *Quasi-idempotent Rota-Baxter operators arising from quasi-idempotent elements*, arXiv:1604.07292, first posted 2016-04-25. https://arxiv.org/abs/1604.07292

[3] V. Gubarev, *Rota-Baxter operators on a sum of fields*, arXiv:1811.08219, first posted 2018-11-20. https://arxiv.org/abs/1811.08219

[4] P. Benito, V. Gubarev and A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037, first posted 2018-01-22. https://arxiv.org/abs/1801.07037
