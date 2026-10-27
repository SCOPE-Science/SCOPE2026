# Sharp coordinatewise Hodge stability and two thresholds for conductance-weighted wheels

## Finding

Let \(n\ge3\), and form the wheel with \(n\) rim vertices \(0,\ldots,n-1\), a single hub, consecutive rim edges of conductance one, and a spoke from each rim vertex to the hub of conductance \(t>0\). Use conductance-normalized edge coordinates: an original measured edge difference \(y_e\) is represented by \(\sqrt{c_e}\,y_e\). Let \(P_{n,t}\) be orthogonal projection in these Euclidean coordinates onto potential-gradient flows. The norm of interest is the induced \(\ell_\infty\)-operator norm; it controls coordinatewise weighted perturbations of edge measurements.

Define
\[
 r=\frac{t+2-\sqrt{t(t+4)}}2,\qquad a=\sqrt{t(t+4)},\qquad m=\lfloor n/2\rfloor,
 \qquad g_j=\frac{r^j+r^{n-j}}{a(1-r^n)}\quad(0\le j\le n).
\]
Then the **exact sharp norm**, attained by a finite sign vector, is
\[
 \boxed{\|P_{n,t}\|_{\infty\to\infty}=\max\{R_n(t),S_n(t)\}},
 \qquad R_n(t)=2(1-tg_0)+2\sqrt t\,(g_0-g_m),
 \qquad S_n(t)=1+2\sqrt t\,(g_0-g_m).
\]
The two quantities are, respectively, the absolute row sums at a rim edge and a spoke. Every edge of the same type has the same row sum.

There is a unique transition weight \(t_n>0\) satisfying \(t_ng_0(t_n)=1/2\). Rim edges are the unique maximizing type for \(0<t<t_n\), spokes for \(t>t_n\), and the two types tie at \(t=t_n\). These transition weights satisfy
\[
 t_3=1,\qquad t_3<t_4<t_5<\cdots<\frac43,
 \qquad \lim_{n\to\infty}3^n\left(\frac43-t_n\right)=\frac{64}{9}.
\]
There are two distinct amplification thresholds. Every wheel with \(3\le n\le5\) has \(\|P_{n,t}\|_{\infty\to\infty}<2\) for every \(t>0\), but for each \(n\ge6\) some positive weight makes the norm larger than two. The first example is exact:
\[
 n=6,\quad t=\frac14,\quad g_0=\frac{1188}{1105},\quad g_3=\frac{512}{1105},\quad
 \boxed{\|P_{6,1/4}\|_{\infty\to\infty}=\frac{2292}{1105}>2}.
\]
For a fixed positive weight, the bound two holds for every wheel size if and only if \(t\ge1\) (and is strict for each finite size when \(t\ge1\)). Over all sizes and all positive weights, the optimal universal upper bound is three, approached but not attained.

## Assumptions and scope

All graphs are finite and undirected, with the specified positive conductances and no loops or extra edges. The rim has \(n\) distinct vertices; thus the wheel has \(n+1\) vertices and \(2n\) edges. Fix any orientations; changing orientations conjugates the projector by a diagonal sign matrix, preserving the norm. For edge measurements \(y\) the weighted least-squares fit minimizes \(\sum_e c_e(y_e-(\nabla u)_e)^2\); the projector acts on \(x_e=\sqrt{c_e}y_e\), not on raw unscaled \(y_e\). All assertions concern this explicitly normalized norm, not an unweighted \(\ell_\infty\) norm on raw edge differences.

## Proof

**1. Reduction to a massive cycle Green function.** Orient rim edge \(j\) from \(j\) to \(j+1\pmod n\), and spokes from hub to rim. Fix hub potential zero, and let \(R\) be the oriented \(n\)-by-\(n\) cycle-incidence matrix. The reduced conductance-normalized vertex-edge incidence is \(B=[R\ \sqrt t I]\). Its full row rank gives the orthogonal projector
\[
 P_{n,t}=B^T(BB^T)^{-1}B,\qquad A=BB^T=RR^T+tI,
 \qquad G=A^{-1}.
\]
Here \(A\) is the symmetric circulant matrix with diagonal \(t+2\) and nearest-neighbor entries \(-1\). Since \(r+r^{-1}=t+2\) and \(0<r<1\), direct substitution into the recurrence \((t+2)g_j-g_{j-1}-g_{j+1}=\delta_{j0}\), with periodic indexing, proves
\[
 G_{jk}=g_{(j-k)\bmod n},\qquad g_j=\frac{r^j+r^{n-j}}{\sqrt{t(t+4)}(1-r^n)}.
\]
Thus \(g_j>0\), \(\sum_jg_j=1/t\), and \(g_j\) decreases strictly with circular distance from zero until an antipode is reached.

**2. Every row of the projector.** Cycle circulant matrices commute, so \(R^TGR=I-tG\). Hence the three blocks of \(P_{n,t}\) are
\[
 P_{rr}=I-tG,\qquad P_{rs}=\sqrt t\,R^TG,\qquad P_{ss}=tG.
\]
The diagonal entries of \(P_{rr}\) equal \(1-tg_0\ge0\), all its off-diagonal entries are negative, and its absolute row sum is \(2(1-tg_0)\). The positive block \(P_{ss}\) has row sum one. Each row of \(R^TG\) is the first difference of a circular translate of \((g_j)\), whose absolute variation is exactly \(2(g_0-g_m)\). Adding the block contributions yields \(R_n(t)\) and \(S_n(t)\). The maximum absolute row sum is the induced maximum-coordinate norm. For a maximizing row \(i\), choosing the input coordinate signs to match those of row \(i\) attains the row sum exactly with \(\|x\|_\infty=1\).

**3. The rim-versus-spoke transition.** Subtraction gives \(R_n-S_n=1-2tg_0\). The eigenvalues of the cycle Laplacian are \(4\sin^2(\pi j/n)\), hence
\[
 tg_0=\frac1n\sum_{j=0}^{n-1}\frac{t}{t+4\sin^2(\pi j/n)}.
\]
This is continuous and strictly increasing in \(t>0\), from \(1/n<1/2\) to one. Thus there is exactly one \(t_n\). The Green formula also gives
\[
 tg_0=\sqrt{\frac{t}{t+4}}\,\frac{1+r^n}{1-r^n}.
\]
For each fixed \(t\), this expression strictly decreases with \(n\); consequently \(t_n\) strictly increases and converges to the unique solution \(\sqrt{t/(t+4)}=1/2\), namely \(4/3\). In the three-rim case \(tg_0=(t+1)/(t+3)\), giving \(t_3=1\). At \(t_*=4/3\) the corresponding \(r_*=1/3\), while \(\frac{d}{dt}\sqrt{t/(t+4)}\big|_{t=t_*}=9/64\). Expanding the displayed transition equation, with \(r(t_n)^n=3^{-n}(1+o(1))\), proves \(3^n(t_*-t_n)\to64/9\).

**4. The first size with amplification above two.** From the Green formula, \(g_0-g_m<1/\sqrt{t(t+4)}\), so
\[
 S_n(t)<1+\frac2{\sqrt{t+4}}<2.
\]
For fixed \(t\), \(g_0\) strictly decreases as \(n\) increases. Meanwhile \(g_0-g_m\) increases: writing \(r\in(0,1)\), its value multiplied by \(a\) equals \((1-r^k)/(1+r^k)\) when \(n=2k\), and \((1-r^k)(1-r^{k+1})/(1-r^{2k+1})\) when \(n=2k+1\). Direct cross multiplication shows the latter lies strictly between the values for \(2k\) and \(2k+2\); in both comparisons, cancellation leaves a positive factor \(r^k(1-r)\). Thus \(R_n(t)\) is strictly increasing in \(n\).

It suffices to bound \(R_5(t)\). Set \(u=\sqrt r\in(0,1)\). Since \(\sqrt t=(1-u^2)/u\), the condition \(R_n(t)<2\) is equivalent to
\[
 F_n(u):=(1-u^2)(1+u^{2n})-u(1-u^{2m})(1-u^{2(n-m)})>0.
\]
At \(n=5\), exact polynomial factorization yields
\[
 F_5(u)=(1-u^4)p(u),\qquad
 p(u)=1-u-u^2+u^4-u^6+u^7+u^8.
\]
For \(0<u\le1/2\), the positive terms give \(p(u)\ge1-u-u^2-u^6\ge15/64>0\). For \(1/2\le u<1\), put \(v=(2u-1)/(1-u)\ge0\); then
\[
 (v+2)^8p\!\left(\frac{v+1}{v+2}\right)
 =v^8+6v^7+11v^6+v^5+v^4+89v^3+224v^2+219v+79>0.
\]
Therefore every \(n\le5\) has norm strictly less than two. At \(n=6,t=1/4\), exact inversion gives the stated rational \(g_0,g_3\) and \(R_6=2292/1105>2\). Strict monotonicity of \(R_n(1/4)\) supplies a witness at every \(n\ge6\).

**5. Uniform size bound and the sharp universal envelope.** At fixed \(t>0\), letting \(n\to\infty\) gives
\[
 R_\infty(t)=2+\frac{2(1-\sqrt t)}{\sqrt{t+4}},\qquad
 S_\infty(t)=1+\frac2{\sqrt{t+4}}.
\]
The finite quantities are strictly smaller than their corresponding limits. Thus \(t\ge1\) is exactly the regime in which all finite wheels have norm below two. For \(0<t<1\), the limiting rim row exceeds two and sufficiently large wheels inherit this strict inequality. Both limiting branches are below three for every \(t>0\), and \(R_\infty(t)\to3\) as \(t\downarrow0\). Choosing successive sufficiently large finite wheels gives supremum three, unattained.

## Verification

The accompanying `check_weighted_wheel.py` performs exact rational matrix calculations for all rim sizes from three through twelve and the spoke-square-root values \(1/4,1/2,1,2\). It checks incidence-matrix identities, symmetry and idempotence, all rim and spoke row sums, sign-vector attainment, Green positivity/monotonicity, the rational first crossing witness, the positive-polynomial certificate, and the critical derivative and decay ratio. All 486 assertions passed. These finite checks supplement, but do not replace, the all-size analytical proof above. Run `python3 check_weighted_wheel.py` with SymPy installed.

## Relationship to prior work

The weighted least-squares graph-gradient projection is standard in Jiang, Lim, Yao and Ye (first public preprint in 2008). Kassel and Wu (2013) derive the transfer-current/Green-function framework in general weighted networks. Ipsen and Mallik (first preprint 2022) determine oriented-incidence and Laplacian Moore–Penrose inverses for **unweighted** wheel graphs, which can in principle support the \(t=1\) special case after further row-sum calculations. Those general or unweighted results are credited rather than presented as new.

The contribution established here is the **weighted** exact endpoint norm and attainment, the unique spoke-to-rim sensitivity transition and its exponential weight asymptotic, and the separate exact six-rim and weight-one amplification thresholds. A separately published wheel-ellipsoid result concerns a different extremal invariant; its short summary alone was available and does not establish the present claim. Priority against obscure equivalent formulations is not conclusively settled.

## Limitations

Only constant rim conductance one and a common positive spoke conductance are covered. The norm measures errors after multiplication by the square root of conductance. Results are not asserted for individual heterogeneous spokes, nonwheel graphs, raw unscaled errors, or projections in non-Hilbert geometries. No independent mathematical or historical-priority validation is claimed.

## References

1. X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, originally submitted 2008-11-07; *Mathematical Programming* 127 (2011), 203–244. https://arxiv.org/abs/0811.1067
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, first submitted 2013-12-10; *Probability Theory and Related Fields* 163 (2015), 89–121. https://arxiv.org/abs/1312.2946
3. J. Ipsen and S. Mallik, *Incidence and Laplacian matrices of wheel graphs and their inverses*, arXiv:2201.02579, first submitted 2022-01-06; *American Journal of Combinatorics* 2 (2023), 1–19. https://arxiv.org/abs/2201.02579
4. *The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes*, published research record identifier `39d62ea47ea0`, summary available; different convex-geometric invariant.
