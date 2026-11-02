# Joint large deviations of image ranks for mutually annihilating full transformations

## Finding

Let \(T_n\) be the monoid of all selfmaps of \([n]\), with composition as multiplication. Let \(E_n\) be the set of ordered pairs \((f,g)\) for which both compositions equal one and the same constant transformation \(e_a\) for some \(a\in[n]\):
\[
 f\circ g=g\circ f=e_a,\qquad e_a(x)=a\quad(x\in[n]).
\]
Define, for integers \(N\ge0\) and \(k\ge0\),
\[
 F_N(k)=\sum_{j=0}^k(-1)^j\binom kj(k+1-j)^N,
\]
with \(F_N(k)=0\) when \(N<0\), and \(0^0=1\). For every \(n\ge1\) and \(0\le r,s\le n-1\), the exact number of pairs in \(E_n\) with \(|\operatorname{im} f|=r+1\), \(|\operatorname{im} g|=s+1\) is
\[
 \boxed{Z_n(r,s)=n\binom{n-1}{r}\binom{n-1}{s}F_{n-s-1}(r)F_{n-r-1}(s).}
\]
Thus \(|E_n|=\sum_{r,s=0}^{n-1}Z_n(r,s)\); the formula includes the boundary \(n=1\) and vanishes when \(r+s>n-1\).

Choose a pair uniformly from \(E_n\). Let \(L_n=\log n\), using natural logarithms, and for \(n\ge3\) put
\[
 X_n=\frac{L_n}{n}|\operatorname{im} f|,\qquad
 Y_n=\frac{L_n}{n}|\operatorname{im} g|.
\]
The laws of \((X_n,Y_n)\) obey a **good large-deviation principle** on \([0,\infty)^2\) with speed \(n\) and rate
\[
 \boxed{I(x,y)=\begin{cases}x-1-\log x+y-1-\log y,&x>0,\ y>0,\\+\infty,&\text{otherwise}.\end{cases}}
\]
Explicitly, for every open \(U\subseteq[0,\infty)^2\) and closed \(F\subseteq[0,\infty)^2\),
\[
 \liminf_{n\to\infty}\frac1n\log\Pr((X_n,Y_n)\in U)\ge-\inf_U I,
 \quad
 \limsup_{n\to\infty}\frac1n\log\Pr((X_n,Y_n)\in F)\le-\inf_F I.
\]
In particular \((X_n,Y_n)\to(1,1)\) in probability. The two rare-event rank penalties are **additive at exponential speed**, even though the defining equations couple both transformations. More locally, for every fixed \(x,y>0\), putting \(r_n=\lfloor xn/\log n\rfloor\) and \(s_n=\lfloor yn/\log n\rfloor\),
\[
 \lim_{n\to\infty}\frac1n\log\Pr\bigl(|\operatorname{im} f|=r_n+1,|\operatorname{im} g|=s_n+1\bigr)=-I(x,y).
\]
The scalar normalization obeys
\[
 \log|E_n|=2n(\log n-\log\log n-1)+o(n).
\]
**The typical \(n/\log n\) rank scale and the leading scalar exponent are earlier observations and are not presented as the novel part; the claim is the exact finite joint rank census together with the full two-dimensional large-deviation rate.**

## Assumptions and scope

There are no restrictions on \(n\) beyond positivity, and no assumptions on independence or injectivity of the selfmaps before conditioning. The constant \(e_a\) may depend on the pair; there is exactly one such \(a\). The probability distribution is uniform over ordered pairs in \(E_n\), not over all commuting transformations. Rates and logarithms use base \(e\). The probability statements are asymptotic as \(n\to\infty\) through positive integers. The rate is not asserted for the full set of commuting pairs outside \(E_n\).

## Proof

**1. The unique common root.** Fix \((f,g)\in E_n\) and its common constant \(e_a\). Since \(f\circ g=g\circ f\), associativity gives \(f\circ e_a=e_a\circ f\) and \(g\circ e_a=e_a\circ g\). Therefore \(f(a)=g(a)=a\). Write \(R=\operatorname{im}f\setminus\{a\}\) and \(S=\operatorname{im}g\setminus\{a\}\), with sizes \(r,s\). The two zero-composition conditions are equivalent to \(f\) being identically \(a\) on \(S\cup\{a\}\) and \(g\) being identically \(a\) on \(R\cup\{a\}\). The sets \(R,S\) need not be disjoint. Once they are chosen, the remaining \(n-s-1\) inputs of \(f\) may take any value in \(R\cup\{a\}\) but must hit every member of \(R\); by inclusion–exclusion there are \(F_{n-s-1}(r)\) choices. Similarly there are \(F_{n-r-1}(s)\) choices for \(g\). Choose \(a,R,S\) in \(n\binom{n-1}{r}\binom{n-1}{s}\) ways. The resulting functions are uniquely recovered, proving the count. Since \(F_N(k)=0\) for \(k>N\), nonzero terms have \(r+s\le n-1\).

**2. Uniform occupancy bounds.** For \(0\le k\le N\),
\[
 k!(k+1)^{N-k}\le F_N(k)\le(k+1)^N.
\]
The lower bound assigns a permutation of the \(k\) nonroot colors to \(k\) specified inputs and permits the remaining inputs arbitrary colors; the upper bound drops surjectivity. Stirling's bound therefore shows \(\log F_N(k)=N\log(k+1)+O(k)\), with the error uniform for \(k\le N\). Set \(W_n(r,s)=Z_n(r,s)/n\) and \(L=\log n\), and rescale \(x=rL/n\), \(y=sL/n\). On the expanding square
\[
 B_n=\bigl\{(r,s):n/L^2\le r,s\le n/\sqrt L\bigr\},
\]
we have \(r+s<n-1\) for all sufficiently large \(n\). Applying the occupancy bounds and \(\log\binom{n-1}{r}=O(r\log(en/r))\), uniformly for \((r,s)\in B_n\), gives
\[
 \log W_n(r,s)=2n(L-\log L)+n(\log x-x+\log y-y)+o(n).
\]
Indeed \(\log(r+1)=L-\log L+\log x+o(1)\) uniformly there; \(s\log(r+1)=ny+o(n)\), and the analogous relation holds with \(r,s\) interchanged. The binomial contributions are \(O(n\log L/\sqrt L)=o(n)\), and both occupancy errors are \(O(n/\sqrt L)=o(n)\).

**3. Negligible complementary region.** The elementary upper bound
\[
 W_n(r,s)\le4^n(r+1)^{n-s-1}(s+1)^{n-r-1}
\]
holds for every pair of indices. By symmetry it suffices to bound indices \(r\) outside \([n/L^2,n/\sqrt L]\). If \(r\le n^{9/10}\), use \(r+1\le2n^{9/10}\) and \(s+1\le n\): then \(\log W_n(r,s)\le(19/10)nL+O(n)\). If \(n^{9/10}<r<n/L^2\), put \(a=\log(r+1)\), \(b=n-r-1\), and \(t=s+1\). Optimizing \((n-t)a+b\log t\) over positive real \(t\) gives its maximum \(na+b(\log b-\log a-1)\); here \(a\le L-2\log L+o(1)\) and \(b=n-o(n)\), so \(\log W_n(r,s)\le2nL-3n\log L+O(n)\). If \(r>n/\sqrt L\) and \(b\ge1\), the same optimized upper bound with \(a\le L\), \(\log a=\log L+o(1)\), and \(b\le n-r\) gives
\[
 \log W_n(r,s)\le2nL-n\log L-r(L-\log L)+O(n).
\]
This lies at least \(n\sqrt L-O(n\log L)\) below \(2n(L-\log L)\). If \(b=0\), the upper bound is at most \(nL+O(n)\), still smaller. There are only \(n^2\) index pairs, hence the total weight outside \(B_n\) is superexponentially negligible at speed \(n\) relative to any central term.

**4. Normalization, local law, full principle.** The function \(\phi(u)=\log u-u\) has unique maximum \(-1\) at \(u=1\), and tends to \(-\infty\) both as \(u\downarrow0\) and as \(u\uparrow\infty\). The uniform estimate on \(B_n\), the negligible tails, and the \(n^2\) bound on the number of summands yield
\[
 \log\sum_{r,s}W_n(r,s)=2n(L-\log L-1)+o(n).
\]
Multiplying by \(n\) for the root choice changes its logarithm by only \(\log n=o(n)\). Dividing the weight estimate by this normalization gives uniform local logarithmic probability \(-I(x,y)+o(1)\) on \(B_n\). To obtain the LDP lower bound for an open set, choose any point \((x,y)\) of finite rate in that set and choose the nearest lattice pair of rescaled image sizes. For the upper bound on a closed set, first restrict to a compact square \([\delta,M]^2\), where the uniform local bound and the polynomial number of lattice sites suffice. Outside this square, \(\phi(x)+\phi(y)\to-\infty\) as \(\delta\downarrow0\) and \(M\to\infty\); the uniform band bound and the already negligible complementary region establish exponential tightness. This gives both bounds on the closed and open sets. Finally \(I\) is lower semicontinuous, nonnegative, uniquely minimized at \((1,1)\), and has compact sublevel sets, hence is good. The local formula and convergence in probability follow directly.

## Verification

Run `python3 verify.py` with the standard Python library. It computes the rank-refined formula, independently enumerates every pair of selfmaps for \(n=1,2,3,4\), confirms the equality and composition conditions directly, checks the independent occupancy recurrence for \(n\le35\), and verifies the exact support and symmetry. The exhaustive totals for these four dimensions are respectively \(1,6,63,976\). These finite computations check the identity but **do not prove** the infinite large-deviation bounds; those are proved analytically above.

## Relationship to prior work

Cain, Malheiro and Paulista (2023, arXiv:2310.08481, primary MSC 20M20) prove that maximal finite commutative nilpotent transformation subsemigroups are null and cite Cameron et al.'s structural classification of maximal null subsemigroups; their statements concern sizes of entire subsemigroups, not joint rank laws for uniformly selected ordered pairs. Cameron et al. (2021, arXiv:2110.09701, Section 4.1–4.2, particularly Theorem 4.4) classify and optimize null subsemigroups; their structural bounds do not directly imply the present exact image-pair census or rate function.

A July 2022 answer by Dmytro Taranovsky to Benjamin Steinberg's MathOverflow question on commuting random maps **already discusses the mutual-annihilation lower-bound mechanism**, the typical image-size scale \(n/\log n\), and the leading probability exponent. These facts are not claimed new. That answer treats the scalar commuting probability and its dominant heuristic mechanism; the inspected text does not state or establish an exact two-rank count or a full two-dimensional good large-deviation principle for the conditional mutual-annihilation ensemble. The present theorem supplies those rank-resolved statements. Earlier counts of all commuting pairs, such as OEIS A181162 and the literature on commuting functions, refer to a strictly larger ensemble and do not settle this conditional joint law.

## Limitations

This is a theorem for **mutual constant compositions** only. It does not give the distribution of ranks among every commuting pair, nor an exact subexponential prefactor for \(|E_n|\). The large-deviation principle controls probabilities at exponential speed \(n\), not a central-limit scale or an independence assertion in total variation. An equivalent older two-variable occupancy or semigroup enumeration under different terminology cannot be ruled out; publication priority warrants further specialist examination. Self-review does not constitute independent mathematical audit.

## References

1. A. J. Cain, A. Malheiro and T. Paulista, *Commutative nilpotent transformation semigroups*, arXiv:2310.08481, first public 2023-10-12. https://arxiv.org/abs/2310.08481
2. P. J. Cameron, J. East, D. FitzGerald, J. D. Mitchell, L. Pebody and T. Quinn-Gregson, *Minimum degrees of finite rectangular bands, null semigroups, and variants of full transformation semigroups*, arXiv:2110.09701, first public 2021-10-19. https://arxiv.org/abs/2110.09701
3. D. Taranovsky, answer of 2022-07-01 (edited 2022-07-06), to B. Steinberg, *What is the probability two random maps on n symbols commute?*, MathOverflow. https://mathoverflow.net/questions/143058/what-is-the-probability-two-random-maps-on-n-symbols-commute
4. OEIS A181162, counts of ordered commuting pairs of finite selfmaps. https://oeis.org/A181162
5. M. Holloway and M. Shattuck, *Commuting pairs of functions on a finite set*, PU.M.A. Pure Math. Appl. 24(1) (2013), 9–18. https://www.researchgate.net/publication/272492907_Commuting_pairs_of_functions_on_a_finite_set
