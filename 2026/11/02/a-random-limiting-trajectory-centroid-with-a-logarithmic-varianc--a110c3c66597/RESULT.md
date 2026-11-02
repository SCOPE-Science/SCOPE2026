# A random limiting trajectory centroid with a logarithmic variance correction for uniform-history relocation walks

## Finding

For the discrete-time uniform-history preferential-relocation walk defined below, with exploration probability \(0<p<1\), centered independent steps of finite nonzero variance \(\sigma^2\), and empirical trajectory centroid \(A_n=(n+1)^{-1}\sum_{j=0}^n X_j\), there is a centered nondegenerate random variable \(A_\infty\) such that

\[
 A_n\longrightarrow A_\infty\quad\text{almost surely and in }L^2,
 \qquad
 \operatorname{Var}(A_\infty)=\sigma^2\frac{p(2+p)}{2(1-p)}.
\]

Moreover, the finite-sample centroid variance has the sharp deterministic expansion

\[
 \operatorname{Var}(A_n)=\sigma^2\left[\frac{p(2+p)}{2(1-p)}-\frac{p(1+p)}{(1-p)^2}\frac{\log n}{n}+O_p(n^{-1})\right],\qquad n\to\infty.
\]

Here the subscript \(p\) on the error means its deterministic implied constant may depend on the fixed probability \(p\); it does not denote stochastic boundedness. This is distinct from the previously known divergence of the endpoint mean square displacement: 

\[
 \mathbb E X_n^2=\frac{p\sigma^2}{1-p}\sum_{k=1}^n\frac{1-p^k}{k}
 =\frac{p\sigma^2}{1-p}\log n+O_p(1).
\]

Thus the time-averaged *position* stabilizes at a genuinely random center even while the position at a late single time spreads on the square-root-logarithmic spatial scale.

## Assumptions and scope

Fix \(p\in(0,1)\) and \(\sigma^2\in(0,\infty)\). Let \((\eta_j)_{j\ge1}\) be independent identically distributed real random variables, independent of all other random choices, with \(\mathbb E\eta_1=0\) and \(\mathbb E\eta_1^2=\sigma^2\). Begin at \(X_0=0\). Independently at each time \(n\ge0\), choose a Bernoulli decision: with probability \(p\), put \(X_{n+1}=X_n+\eta_{n+1}\); with probability \(1-p\), put \(X_{n+1}=X_{U_n}\) for a fresh uniform index \(U_n\in\{0,\ldots,n\}\). The unused increment at a relocation time has no effect. The random choices at different times are mutually independent, except through the already observed path. There is no fading-memory weighting or reset-to-origin preference.

The result is an annealed, real-valued claim over the walk and its exploration and relocation randomness, with no assumption of a lattice step law or higher moments. All asymptotics fix \(p\) and \(\sigma^2\) before sending \(n\) to infinity. The boundary cases \(p=0\) and \(p=1\) are excluded from the theorem: the former walk stays fixed, and the latter is an ordinary random walk with an unbounded centroid variance.

## Proof

**Step 1: Exact conditional moments and the endpoint second moment.** Put \(S_n=\sum_{j=0}^n X_j\), \(A_n=S_n/(n+1)\), \(v_n=\mathbb E X_n^2\), and \(Q_n=\sum_{j=0}^n v_j\). Centeredness and conditioning on the new decision give \(\mathbb E X_n=0\) and

\[
 v_{n+1}=p(v_n+\sigma^2)+\frac{1-p}{n+1}Q_n,\qquad v_0=Q_0=0.
\]

Let \(V(z)=\sum_{n\ge0}v_nz^n\). Multiplying this recurrence by \(z^{n+1}\) and summing gives

\[
 V(z)=pzV(z)+(1-p)\int_0^z\frac{V(t)}{1-t}\,dt+\frac{p\sigma^2z}{1-z}.
\]

Differentiating, multiplying the resulting equation by \(1-z\), and using \(V(0)=0\) yields

\[
 V(z)=\frac{p\sigma^2}{1-p}\frac{\log\big((1-pz)/(1-z)\big)}{1-z}.
\]

The coefficient formula is the endpoint expression in the Finding section, and \(v_n=O_p(\sigma^2\log(n+1))\).

**Step 2: A convergent martingale representation of the centroid.** Let \(\mathcal F_n\) contain all decisions and increments used through time \(n\), and set

\[
 \xi_j=X_j-\mathbb E[X_j\mid\mathcal F_{j-1}],\quad D_j=X_j-A_j,\quad B_j=(j+1)D_j.
\]

Because \(\mathbb E[X_j\mid\mathcal F_{j-1}]=pX_{j-1}+(1-p)A_{j-1}\), we have, for every \(j\ge1\),

\[
 B_j=pB_{j-1}+j\xi_j,\qquad A_j-A_{j-1}=\frac{B_j}{j(j+1)},\qquad B_0=0.
\]

Define positive deterministic weights

\[
 h_k=k\sum_{j=k}^{\infty}\frac{p^{j-k}}{j(j+1)},\qquad
 0<h_k\le\frac{1}{(1-p)(k+1)}.
\]

The second inequality follows from \(j\ge k\) in the denominator, giving \(k/[j(j+1)]\le1/(k+1)\). More precisely \(h_k\le1/[(1-p)(k+1)]\). In particular \(\sum_kh_k^2\mathbb E\xi_k^2<\infty\), because conditional variance decomposition gives \(\mathbb E\xi_k^2\le v_k=O(\log(k+1))\). The martingale \(M_n=\sum_{k=1}^nh_k\xi_k\) therefore converges almost surely and in \(L^2\) to some \(M_\infty\). Unwinding the recursion for \(B_j\) shows exactly

\[
 M_n-A_n=c_n B_n,
 \qquad c_n=\sum_{r=1}^{\infty}\frac{p^r}{(n+r)(n+r+1)}=O_p(n^{-2}).
\]

By Jensen, \(\mathbb E A_n^2\le(n+1)^{-1}\sum_{j=0}^nv_j=O(\log(n+1))\), so \(\mathbb E B_n^2=(n+1)^2\mathbb E(X_n-A_n)^2=O(n^2\log(n+1))\). It follows that

\[
 \mathbb E\lvert M_n-A_n\rvert^2=O_p\!\left(\frac{\log(n+1)}{n^2}\right).
\]

The right side is summable in \(n\); Markov's inequality and Borel--Cantelli yield \(M_n-A_n\to0\) almost surely, as well as in \(L^2\). Therefore \(A_n\to M_\infty=:A_\infty\) in both senses. The exact positive limiting variance below establishes nondegeneracy.

**Step 3: Closed second-moment equations.** Put \(s_n=\mathbb E S_n^2\) and \(t_n=\mathbb E(S_nX_n)\). With \(s_0=t_0=0\), another direct conditioning gives

\[
 t_{n+1}=pt_n+\frac{1-p}{n+1}s_n+v_{n+1},\qquad
 s_{n+1}=s_n+2t_{n+1}-v_{n+1}.
\]

Let \(\mathcal S(z)=\sum_{n\ge0}s_nz^n\), \(\mathcal T(z)=\sum_{n\ge0}t_nz^n\), and \(F(z)=\int_0^z\mathcal S(t)\,dt=\sum_{n\ge0}s_nz^{n+1}/(n+1)\). The previous two recurrences imply

\[
 (1-pz)\mathcal T(z)=(1-p)F(z)+V(z),\qquad
 (1-z)\mathcal S(z)=2\mathcal T(z)-V(z).
\]

Solving the first-order equation for \(F\) gives the explicit representation

\[
 \boxed{F(z)=\left(\frac{1-pz}{1-z}\right)^2 I(z)},\qquad
 I(z)=\frac{p\sigma^2}{1-p}\int_0^z\frac{1+pt}{(1-pt)^3}\log\frac{1-pt}{1-t}\,dt.
\]

All identities here are initially identities of analytic functions near \(z=0\). They continue to a slit neighborhood of \(z=1\); the other finite branch point is \(1/p>1\).

**Step 4: Evaluation and finite-size asymptotics.** Since

\[
 \frac{d}{dt}\frac{t}{(1-pt)^2}=\frac{1+pt}{(1-pt)^3},
\]

integration by parts using the antiderivative \(t/(1-pt)^2-1/(1-p)^2\) (which vanishes at \(t=1\)) and elementary partial fractions establishes

\[
 \int_0^1\frac{1+pt}{(1-pt)^3}\log\frac{1-pt}{1-t}\,dt=\frac{2+p}{2(1-p)^2}.
\]

Consequently \(I(1)=p\sigma^2(2+p)/(2(1-p)^3)\), and the coefficient of the double pole of \(F\) at \(1\) is

\[
 L=(1-p)^2I(1)=\sigma^2\frac{p(2+p)}{2(1-p)}.
\]

For the next term, the integrand defining \(I\) has near \(t=1\) the expansion

\[
 \frac{p\sigma^2}{1-p}\frac{1+pt}{(1-pt)^3}\log\frac{1-pt}{1-t}
 =\frac{p\sigma^2(1+p)}{(1-p)^4}\log\frac1{1-t}+O_{p,\sigma^2}(1),
\]

with a further error of order \(O_{p,\sigma^2}((1-t)\log(1/(1-t)))\) after subtracting its constant term. Integrating to \(1\) and substituting into \(F\) gives, in a complex dented neighborhood of the unit singularity,

\[
 F(z)=\frac{L}{(1-z)^2}
 -\frac{B\log(1/(1-z))}{1-z}
 +\frac{C}{1-z}+O_{p,\sigma^2}\!\left(\log\frac1{1-z}\right),
 \quad B=\sigma^2\frac{p(1+p)}{(1-p)^2},
\]

for a finite constant \(C\) depending on the fixed parameters. The integrand is analytic away from the positive-real cuts starting at \(1\) and \(1/p\), which permits ordinary singularity coefficient transfer, including the stated remainder. The exact coefficient identities

\[
 [z^{n+1}](1-z)^{-2}=n+2,\qquad
 [z^{n+1}]\frac{\log(1/(1-z))}{1-z}=H_{n+1}
\]

(where \(H_m=\sum_{k=1}^m1/k\)) then yield

\[
 \frac{s_n}{n+1}=L(n+2)-BH_{n+1}+C+O_{p,\sigma^2}(\log(n+1)/n).
\]

Divide by \(n+1\), recall \(\mathbb E A_n=0\), and use \(H_{n+1}=\log n+O(1)\). This proves the finite-size formula and, by the already proved \(L^2\) convergence, \(\operatorname{Var}(A_\infty)=L\). Since \(L>0\), the limit is not deterministic.

## Verification

The accompanying standalone Python program `checker.py` uses only standard-library exact fractions and independent direct enumeration of trajectory histories. It checks the unconditional moment recurrences, the published endpoint moment formula, both first and second moments for two distinct centered increment laws of variance one, and the rate and leading coefficient of the logarithmic finite-size correction. Running `python3 checker.py` produced 177 passed assertions. Finite enumeration and a numerical asymptotic-rate comparison do not certify an infinite asymptotic; the infinite statements are established by Steps 1–4 above.

For direct reproduction, choose an exploration probability such as \(p=1/2\), form the path-law recursion for each finite \(n\), or use the two scalar second-moment recursions, and compare \(\operatorname{Var}(A_n)\) to \(5\sigma^2/4-3\sigma^2\log(n)/n\). The numerical remainder multiplied by \(n\) approaches a bounded value. The proof applies without any Gaussian or fourth-moment hypothesis on the increments.

## Relationship to prior work

The walk's uniform relocation-to-previously-visited-time rule and the exact endpoint MSD were established by Boyer and Solis-Salas, *Random Walks with Preferential Relocations to Places Visited in the Past and their Application to Biology* (public preprint March 24, 2014, arXiv:1403.6069). Those ingredients are known; they are not asserted as novel here.

Mailler and Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees* (first public October 5, 2018, arXiv:1810.02735), proved endpoint scaling limits and normalized occupation-measure convergence for broad families of such walks. Their scaled occupation law does not supply the unscaled random empirical centroid, its explicit limiting variance, or the \((\log n)/n\) finite-size correction; passing to unbounded coordinate moments from weak convergence of scaled occupation measures is not automatic.

Rafler, *Hoppe trees, random recursive sets and their barycentre* (July 6, 2012, arXiv:1207.1636), obtained a nondegenerate limiting barycenter for a different random recursive spatial set. That model selects each preceding vertex uniformly (apart from a fixed root weight) and adds a spatial increment every time; in the present walk the newest vertex receives an additional probability \(p\) of being selected as parent, and relocation produces exactly zero spatial increment. Neither the parent-selection law nor the edge-increment law is an instance of Rafler's stated fixed-kernel Hoppe-tree assumptions. Thus the similarity of barycenter observables does not alone imply this formula.

Campos and Méndez, *Recurrence time correlations in random walks with preferential relocation to visited places* (public preprint August 31, 2018, arXiv:1808.10673), study dispersal and return-time correlations for a continuous-time extension rather than an unscaled empirical-coordinate centroid. Broader analyses of history-dependent walk barycenters might still contain a general theorem implying these results; historical priority has not been independently certified.

## Limitations

The almost-sure result depends on independent uniform history selection, stationary independent exploration decisions and finite second moment of centered steps. No convergence in distribution of the *unscaled endpoint* is claimed, no Gaussian law for \(A_\infty\) is asserted, and no assertion is made for general fading-memory kernels, reset-to-origin schemes, nonzero drift, or heavy-tailed increments without a second moment. The constants diverge as \(p\uparrow1\), so the estimate is not uniform at the ordinary-random-walk boundary. The remaining historical-priority risk is that a more general result on dependent recursive spatial trees or reinforced walk averages could imply this theorem without matching its wording. Independent validation has not been performed.

## References

1. D. Boyer and C. Solis-Salas, *Random Walks with Preferential Relocations to Places Visited in the Past and their Application to Biology*, arXiv:1403.6069, first public March 24, 2014. https://arxiv.org/html/1403.6069v3
2. C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735, first public October 5, 2018. https://arxiv.org/abs/1810.02735
3. M. Rafler, *Hoppe trees, random recursive sets and their barycentre*, arXiv:1207.1636, first public July 6, 2012. https://arxiv.org/abs/1207.1636
4. D. Campos and V. Méndez, *Recurrence time correlations in random walks with preferential relocation to visited places*, arXiv:1808.10673, first public August 31, 2018. https://arxiv.org/html/1808.10673v2
