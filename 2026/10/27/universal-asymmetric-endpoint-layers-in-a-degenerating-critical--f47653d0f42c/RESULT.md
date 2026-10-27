# Universal asymmetric endpoint layers in a degenerating critical-cusp full shift

## Finding
For \(1<\vartheta<2\), define \(K=(1-\vartheta/2)/\sqrt2\) and the critical cusp map
\[f_\vartheta(1/2\pm t)=1-\vartheta t-2K\sqrt t,\qquad0\le t\le1/2.\]
Write \(h_\vartheta\) for the unique normalized absolutely continuous invariant density. As \(\vartheta\uparrow2\), \(h_\vartheta\to1\) in \(L^1[0,1]\), uniformly on every compact subinterval of \((0,1)\), whereas \(h_\vartheta(0)=h_\vartheta(1)=0\) for every \(\vartheta<2\). More precisely, for each finite \(S\), uniformly over \(0\le s\le S\),
\[\begin{aligned}
 h_\vartheta(1-K^2s)&\longrightarrow U(s)=1-\frac1{\sqrt{1+2s}},\\
 h_\vartheta(K^2s)&\longrightarrow V(s)=\sum_{j=1}^\infty2^{-j}\left(1-\frac1{\sqrt{1+2s/2^j}}\right).
\end{aligned}\]
Both profiles rise from zero to one; their slopes at zero are respectively \(1\) and \(1/3\). The two boundary layers therefore have the same quadratic width in \(2-\vartheta\), but distinct universal shapes. The derivatives also satisfy exactly
\[h_\vartheta'(1)=-\frac{h_\vartheta(1/2)}{K^2},\qquad h_\vartheta'(0)=-\frac{\lambda_\vartheta^2}{1-\lambda_\vartheta^2}h_\vartheta'(1),\quad \lambda_\vartheta=(1+\vartheta/2)^{-1}.\]

## Assumptions and scope
The map acts on \([0,1]\); the density is the uniquely normalized \(W^{2,1}\) invariant density proved in Oltiboev--Vafoyev, arXiv:2610.23180v1, Proposition 4.2. No random perturbation or regularity in the parameter is assumed. Every asymptotic limit is one-sided as \(\vartheta\uparrow2\), and convergence of the layer profiles is uniform only on finite \(s\)-intervals. The limiting map is the full tent map \(f_2(x)=2\min(x,1-x)\).

## Proof
**1. Exact inverse branches and endpoint identities.** Set \(u(x)=(\sqrt{K^2+\vartheta(1-x)}-K)/\vartheta\), \(g_\pm(x)=1/2\pm u(x)^2\), and \(w(x)=u(x)/(K+\vartheta u(x))\). The Perron--Frobenius operator is
\[(L_\vartheta\phi)(x)=w(x)\big(\phi(g_-(x))+\phi(g_+(x))\big).\]
Here \(w(1)=0\), \(w(0)=\lambda_\vartheta<1\), \(g_-(0)=0\), \(g_+(0)=1\), and \(w(x)=\vartheta^{-1}(1-K/\sqrt{K^2+\vartheta(1-x)})\). The equation \(h_\vartheta=L_\vartheta h_\vartheta\) implies \(h_\vartheta(1)=0\), and then \(h_\vartheta(0)=\lambda_\vartheta h_\vartheta(0)=0\). As \(x\uparrow1\), \(w(x)/(1-x)\to1/(2K^2)\), while both inverse branches tend to \(1/2\); hence \(h_\vartheta'(1)=-h_\vartheta(1/2)/K^2\). At zero, \(g_-'(0)=\lambda_\vartheta\), \(g_+'(0)=-\lambda_\vartheta\); differentiating and using the vanishing endpoints gives \(h_\vartheta'(0)=\lambda_\vartheta^2(h_\vartheta'(0)-h_\vartheta'(1))\). This is the claimed exact relation. The endpoint derivative at the cusp image is also a special case of Proposition 5.1 of the primary paper; it is not claimed as an independent discovery.

**2. Uniform statistical stability.** The two monotonic full branches have the same fixed partition \([0,1/2]\), \([1/2,1]\). Their inverse slopes are bounded above by \(\lambda_\vartheta\), which stays below a constant smaller than one for \(\vartheta\) sufficiently close to two. The reciprocal forward slopes on the two branches have monotone variation bounded by a common constant (each ranges between zero and \(\lambda_\vartheta\)). These are uniform full-branch Rychlik/Lasota--Yorke hypotheses: the standard bounded-variation inequality for an iterate, obtained by partitioning into inverse cylinders, has a contraction coefficient strictly below one and a finite weak-norm coefficient independent of \(\vartheta\) near two. Applying it to \(L_\vartheta h_\vartheta=h_\vartheta\), \(\|h_\vartheta\|_1=1\), bounds \(\|h_\vartheta\|_{BV}\) uniformly. To make the uniformity explicit, each fixed-rank cylinder contracts by at most \(\lambda_\vartheta^n\), the branch weights are products of reciprocals with uniform bounded variation, and fixed-rank branch geometries converge to those of the full tent map. A sufficiently high fixed iterate gives the required strict BV contraction. Compactness of bounded BV sets in \(L^1\) supplies subsequential limits. The inverse-branch formula gives \(L_\vartheta\to L_2\) from \(BV\) to \(L^1\) in weak operator norm: \(g_\pm\to g_\pm^{(2)}\) uniformly and \(w\to1/2\) in \(L^1\). Any limit density is invariant under the full tent map, whose unique normalized invariant density is constant one. Therefore \(\|h_\vartheta-1\|_1\to0\).

For completeness, this strengthens to uniform convergence on compact interior sets without invoking a uniform parameter-differentiability theorem. Fix an integer \(n\) and an interior interval \(J\subset(0,1)\). On each of the \(2^n\) inverse cylinders \(C\), the inverse-iterate weight \(w_C(x)\le\lambda_\vartheta^n\), and for \(x\in J\) the ratios \(w_C(x)/|C|\) are bounded by a constant \(A_{n,J}\) as \(\vartheta\uparrow2\), since finite-rank inverse branches converge smoothly there to affine tent branches and \(|C|\to2^{-n}\). For \(\phi\in BV\), \(|\phi(g_C(x))|\le\operatorname{Var}_C(\phi)+|C|^{-1}\int_C|\phi|\). Summing disjoint cylinders gives
\[\sup_{x\in J}|L_\vartheta^n\phi(x)|\le\lambda_\vartheta^n\operatorname{Var}(\phi)+A_{n,J}\|\phi\|_1.\]
Apply this to \(\phi=h_\vartheta-1\). Since \(h_\vartheta=L_\vartheta^nh_\vartheta\), and \(L_\vartheta^n1\to L_2^n1=1\) uniformly on \(J\) for fixed \(n\), the limsup of \(\sup_J|h_\vartheta-1|\) is bounded by \(C2^{-n}\). Letting \(n\to\infty\) proves uniform interior convergence.

**3. Right layer.** At \(x=1-K^2s\), one has exactly
\[w(x)=\frac1\vartheta\left(1-\frac1{\sqrt{1+\vartheta s}}\right),\quad g_\pm(x)=\frac12\pm\frac{K^2}{\vartheta^2}(\sqrt{1+\vartheta s}-1)^2.\]
For bounded \(s\), both inverse branches converge uniformly to the interior point \(1/2\). The interior result gives \(h_\vartheta(g_\pm(x))\to1\), proving uniform convergence to \(U(s)\).

**4. Left layer.** Define \(V_\vartheta(s)=h_\vartheta(K^2s)\) and \(U_\vartheta(s)=h_\vartheta(1-K^2s)\). Uniformly on compact \(s\)-intervals, \(w(K^2s)\to1/2\), \(g_-(K^2s)/K^2\to s/2\), and \((1-g_+(K^2s))/K^2\to s/2\). Since \(h_\vartheta\) is uniformly bounded in \(BV\), recursively applying the fixed-point equation \(m\) times on the left inverse branch leaves a remainder at most \(C\lambda_\vartheta^m\). The other terms converge by the established right-layer limit, yielding, uniformly for bounded \(s\),
\[V_\vartheta(s)\longrightarrow\sum_{j=1}^m2^{-j}U(s/2^j)+O(2^{-m}).\]
Letting \(m\to\infty\) yields \(V(s)\). Equivalently, \(V(s)=\tfrac12V(s/2)+\tfrac12U(s/2)\) with \(V\) bounded; iterative substitution proves uniqueness. Uniform geometric domination justifies differentiating the limiting *profile* series: \(U'(0)=1\) and \(V'(0)=\sum_{j\ge1}4^{-j}=1/3\). Finally the exact finite-parameter derivative identities in step 1 and \(h_\vartheta(1/2)\to1\), \(\lambda_\vartheta\to1/2\) give the two renormalized derivative limits independently of any exchange of derivative and profile limits.

## Verification
The proof is analytic; no finite experiment is used to infer an infinite limit. Each inverse-branch identity and both endpoint derivative relations can be checked symbolically from the displayed formulas. The included `verify.py` checks the algebraic inverse-branch properties, finite-parameter endpoint slope ratio, and convergence of finite partial profile sums to the recursions for rational sample arguments. It is supporting reproducibility evidence and not a substitute for the uniform BV argument.

## Relationship to prior work
Oltiboev--Vafoyev (2026), arXiv:2610.23180v1, constructs exactly this full-branch critical-cusp map, proves existence, uniqueness, \(W^{2,1}\) regularity and fixed-parameter spectral gap (Proposition 4.2), and derives the general cusp-image derivative trace (Proposition 5.1). Its main perturbation theorem varies Bernoulli mixing probabilities at fixed cusp parameters. The present statement concerns the *singular change of deterministic map parameter* \(\vartheta\uparrow2\) and identifies both spatially resolved endpoint layers. Oltiboev--Rakhimov--Ruziboev, arXiv:2608.26969v1, treats stationary response for a different exponent range \(-1<\beta<-1/2\) and does not give this critical-endpoint profile. General transfer-operator stability results (Keller--Liverani) motivate the statistical limit but do not specify either boundary profile. A separately recorded analytic-continuation result on this same cusp family concerns complex singularity locations, not these real singular-parameter limits.

## Limitations
The claim is limited to this full-branch family and the limit \(\vartheta\uparrow2\); it does not prove a universal theorem for all cusp degenerations. The layer convergence is locally uniform on finite rescaled distances, not a globally uniform approximation over \(s\ge0\). The exact finite-parameter cusp-image derivative is already in the primary work; novelty is assigned to the distinct two-sided profiles and their singular-parameter convergence. No independent mathematical or literature-priority validation has been performed.

## References
1. D. Oltiboev and M. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (first public October 16, 2026), §§3–6. https://arxiv.org/abs/2610.23180
2. D. Oltiboev, K. Rakhimov and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (August 27, 2026), introduction and main theorem. https://arxiv.org/abs/2608.26969
3. G. Keller and C. Liverani, *Stability of the spectrum for transfer operators*, Ann. Scuola Norm. Sup. Pisa 28 (1999), 141–152.
4. M. Rychlik, *Bounded variation and invariant measures*, Studia Math. 76 (1983), 69–80.
