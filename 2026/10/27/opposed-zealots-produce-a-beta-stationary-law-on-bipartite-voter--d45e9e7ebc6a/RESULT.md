# Opposed zealots produce a beta stationary law on bipartite voter networks

## Finding
Let \(a,b\ge 1\). On \(K_{a+1,b+1}\), fix one permanently red vertex in the first part and one permanently blue vertex in the second part. Every other vertex carries a red/blue voter, who at rate one copies a uniformly selected neighbor. Write \(X\) and \(Y\) for the fractions of red *flexible* voters in the first and second parts, respectively, in the unique stationary law. Then
\[
\mathbb E X=\frac{b}{a+b+1},\qquad \mathbb E Y=\frac{b+1}{a+b+1}.
\]
For distinct flexible voters \(A_1,A_2\) in the first part (when \(a\ge2\)), distinct flexible voters \(B_1,B_2\) in the second (when \(b\ge2\)), and a flexible pair \(A_1,B_1\) across parts, their red-indicator covariances are exactly
\[
\begin{aligned}
\operatorname{Cov}(A_1,A_2)&=\frac{b(a+1)(a+b)}{(a+b+1)^2(3a+3b+2)},\\
\operatorname{Cov}(B_1,B_2)&=\frac{a(b+1)(a+b)}{(a+b+1)^2(3a+3b+2)},\\
\operatorname{Cov}(A_1,B_1)&=\frac{(a+1)(b+1)(a+b)}{(a+b+1)^2(3a+3b+2)}.
\end{aligned}
\]
In particular, all existing distinct-pair covariances are strictly positive. More strikingly, if \(a,b\to\infty\) with \(b/(a+b)\to\theta\in(0,1)\), then jointly in distribution
\[
(X,Y)\Longrightarrow(V,V),\qquad V\sim\operatorname{Beta}(2\theta,2(1-\theta)).
\]
At equal asymptotic part sizes, the stationary red fraction is therefore asymptotically **uniform on \([0,1]\)**, not concentrated about \(1/2\). For any two distinct flexible voters, the disagreement probability tends to \(4\theta(1-\theta)/3\), equal to \(1/3\) when \(\theta=1/2\).

## Assumptions and scope
The graph is the complete undirected bipartite graph whose sides have \(a+1\) and \(b+1\) labeled vertices. Only two designated zealots are frozen: the first-part zealot is red (indicator one) and the second-part zealot is blue (indicator zero). The remaining \(a+b\) binary opinions change by independent continuous-time rate-one Poisson clocks; at a clock event the voter copies one uniformly random opposite-part neighbor, possibly a zealot. Each \(a,b\) is a positive integer; the limit assumes both tend to infinity with nondegenerate ratio. The statements concern stationarity, not finite-time mixing rates. The first/second moments refer to **distinct labeled voters**; formulas for same-part pairs are asserted only when that part has at least two flexible voters.

## Proof
**Stationarity and exact first moments.** Let \(I=aX\) and \(J=bY\) count flexible red opinions. The count-chain rates are
\[
\begin{array}{ll}
q_{(i,j),(i+1,j)}=(a-i)j/(b+1),&q_{(i,j),(i-1,j)}=i(b+1-j)/(b+1),\\
q_{(i,j),(i,j+1)}=(b-j)(i+1)/(a+1),&q_{(i,j),(i,j-1)}=j(a-i)/(a+1).
\end{array}
\]
All omitted boundary rates are zero. The finite chain is irreducible: each color is injected by a frozen opposite-part vertex, then can spread across both sides through positive-rate copy events, and the opposite color can likewise spread. Any prescribed flexible coloring can be reached from any other by a finite sequence of allowed copy events, so its stationary distribution is unique. Exchangeability within each part is preserved. Writing \(\mathcal L\) for the generator,
\[
\mathcal LX=\frac{b}{b+1}Y-X,\qquad
\mathcal LY=\frac{1+aX}{a+1}-Y.
\]
Their stationary expectations solve the displayed two linear equations, proving the means.

**Exact pair closure.** Write \(\mu=\mathbb E A_1\), \(\nu=\mathbb E B_1\), \(u=\mathbb E A_1A_2\), \(v=\mathbb E B_1B_2\), \(w=\mathbb E A_1B_1\), with \(u\) or \(v\) used only where a distinct pair exists. Applying the generator to products of distinct indicators yields
\[
u=\frac{bw}{b+1},\qquad v=\frac{\nu+aw}{a+1},\qquad
2w=\frac{\nu+(b-1)v}{b+1}+\frac{2\mu+(a-1)u}{a+1}.
\]
Here the first equality is **\(u=bw/(b+1)\)**; in the second, \(\nu\) denotes the second-part mean. Where \(a=1\) or \(b=1\), the corresponding unused pair equation can be removed: its coefficient in the cross equation is zero. Substituting the means and solving gives
\[
\begin{aligned}
u&=\frac{b(a+3b)}{(a+b+1)(3a+3b+2)},\\
v&=\frac{(b+1)(a+3b+2)}{(a+b+1)(3a+3b+2)},\\
w&=\frac{(a+3b)(b+1)}{(a+b+1)(3a+3b+2)}.
\end{aligned}
\]
In this display the first quantity is \(u\) (the same-part first-side pair probability), not the mean \(\nu\). The equalities are formal when a part has only one flexible voter and are used there only multiplied by the vanishing number of such pairs. Subtracting \(\mu^2\), \(\nu^2\), and \(\mu\nu\), respectively, yields the exact covariances.

**Collapse of the two part averages.** Put \(N=a+b\), \(\Delta=X-Y\), and \(Z=(X+Y)/2\). The displayed drift identities imply
\[
\mathcal L\Delta=-2\Delta-\frac{1-X}{a+1}-\frac{Y}{b+1}.
\]
Every jump changes \(\Delta\) by \(1/a\) or \(1/b\), and total jump rates from each part are at most \(a\) or \(b\). Thus the carré-du-champ satisfies \(\Gamma\Delta\le 1/a+1/b\). Stationarity of \(\Delta^2\), the bound \(|(1-X)/(a+1)+Y/(b+1)|\le1/(a+1)+1/(b+1)\), and Young's inequality give \(\mathbb E\Delta^2=O(1/a+1/b)\). Therefore \(X-Y\to0\) in stationary \(L^2\).

**Limiting stationary moments.** For every polynomial \(f\), Taylor expansion of the count generator at \(Z\) gives
\[
\begin{aligned}
\mathcal LZ&=\tfrac12\left(\frac{1-X}{a+1}-\frac{Y}{b+1}\right),\\
\Gamma Z&=\frac{q_{i+}+q_{i-}}{4a^2}+\frac{q_{j+}+q_{j-}}{4b^2},\\
N\mathcal Lf(Z)&\;\longrightarrow\frac{2(\theta-Z)f'(Z)+Z(1-Z)f''(Z)}{4\theta(1-\theta)}
\end{aligned}
\]
in stationary \(L^1\) after replacing the random \(X,Y\) by \(Z\) in the limiting coefficients. This is justified because both part sizes are proportional to \(N\), the squared part-average difference tends to zero, jump sizes are \(O(N^{-1})\), and the Taylor remainder multiplied by \(N\) is \(O(N^{-1})\). Compactness gives subsequential stationary weak limits. Stationarity \(\mathbb E\mathcal L f(Z)=0\) and \(f(z)=z^k\) force, for every integer \(k\ge1\),
\[
(k+1)\mathbb EV^k=(2\theta+k-1)\mathbb EV^{k-1},\qquad \mathbb EV^0=1.
\]
These are exactly the moments of \(\operatorname{Beta}(2\theta,2(1-\theta))\). Probability laws on \([0,1]\) are determined by their moments; hence every subsequential limit agrees. Since \(X-Y\to0\) in probability, the full joint weak convergence follows.

The limiting covariance between distinct flexible voters is \(\operatorname{Var}(V)=\theta(1-\theta)/3\), either by the exact rational formulas or by exchangeability, boundedness, and the limit. Their limiting disagreement probability is \(2(\mathbb EV-\mathbb EV^2)=4\theta(1-\theta)/3\).

## Verification
Run `python3 verify_stationarity.py` with Python 3 standard library. The script builds the complete generator on the \((a+1)(b+1)\) count states, solves its invariant distribution using exact rational Gaussian elimination, and checks all applicable first- and distinct-second-moment formulas for each \(1\le a,b\le3\) (nine parameter pairs). All nine tests passed. This checks the finite algebra independently of pair-generator closure, but cannot establish the infinite-size theorem, for which the moment proof above is supplied.

## Relationship to prior work
Mori, Hisakado and Nakayama (2018, arXiv:1810.05643) investigate voter networks and multivariate beta distributions using internally interacting groups and innovations; their multigroup setup is different from exclusive opposite-part copying with exactly one frozen zealot per side. Ben-Ari, Panzo, Speegle and VandenBerg (2020, arXiv:2004.10187) study quasi-stationary distributions **without zealots** on complete bipartite graphs with one part fixed in the limit; their conditional-survival regime is not this ergodic stationary model with proportional part growth. Braha and de Aguiar (2026, arXiv:2601.09816) treat a multi-zealot Moran representation and complete-graph stationary counts; the complete-graph result does not directly yield this bipartite generator or its ratio-dependent beta parameters. The finite pair equations and limiting beta law here are direct derivations, not claims of inventing the voter model, zealotry, or beta diffusion methodology. An equivalent special-case treatment under another description remains possible.

## Limitations
No explicit closed-form **full finite stationary joint distribution** is claimed. No spectral-gap or mixing-time bound is claimed. The beta limit is restricted to \(\theta\in(0,1)\); extreme part-size ratios may have different limits. Both frozen agents and the uniform opposite-neighbor copying rule are essential hypotheses.

## References
1. T. Mori, M. Hisakado and K. Nakayama, *A Voter Model on Networks and Multivariate Beta Distribution*, arXiv:1810.05643 (first posted 2018-10-12), https://arxiv.org/abs/1810.05643.
2. I. Ben-Ari, H. Panzo, P. Speegle and R. O. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187 (2020), https://arxiv.org/abs/2004.10187.
3. L. Braha and M. A. M. de Aguiar, *The multi-allelic Moran process as a multi-zealot voter model: exact results and consequences for diversity thresholds*, arXiv:2601.09816 (2026), https://arxiv.org/abs/2601.09816.
4. N. Khalil and T. Galla, *Zealots in multistate noisy voter models*, Physical Review E 103, 012311 (2021), doi:10.1103/PhysRevE.103.012311.
