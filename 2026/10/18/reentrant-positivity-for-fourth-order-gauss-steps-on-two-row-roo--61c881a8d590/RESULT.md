# Reentrant positivity for fourth-order Gauss steps on two-row rook graphs

## Finding
For each integer \(n\ge 2\), take the unweighted Cartesian-product graph \(G_n=K_2\square K_n\) and let \(L_n\) be its combinatorial Laplacian. The two-stage, fourth-order Gauss–Legendre end-step for diffusion \(u'=-L_nu\) is
\[
T_n(h)=(12I-6hL_n+h^2L_n^2)(12I+6hL_n+h^2L_n^2)^{-1},\qquad h\ge0.
\]
Define two quartics
\[
\begin{aligned}
A_n(h)&=(n^3+8)h^4+24(n+2)h^3-12(n^2-4n-16)h^2+288h+144,\\
B_n(h)&=-(n^3-8n-8)h^4+24(n+2)h^3+12(n^2+4n+8)h^2+72(n+2)h+144.
\end{aligned}
\]
The **exact set of positivity-preserving timesteps**, where positivity means entrywise nonnegativity of the entire update matrix, has the following complete classification.

1. If \(2\le n\le3\), then \(T_n(h)\ge0\) entrywise for every \(h\ge0\).
2. If \(4\le n\le17\), the polynomial \(B_n\) has a unique positive root \(\gamma_n\), and \(T_n(h)\ge0\) precisely for \(0\le h\le\gamma_n\).
3. If \(n\ge18\), the polynomial \(A_n\) has exactly two positive roots \(\alpha_n<\beta_n\), while \(B_n\) has exactly one positive root \(\gamma_n\). These roots obey \(0<\alpha_n<\beta_n<\gamma_n\), and
\[
\boxed{\ T_n(h)\ge0\quad\Longleftrightarrow\quad
h\in[0,\alpha_n]\cup[\beta_n,\gamma_n].\ }
\]

Thus \(n=18\), a graph with \(36\) vertices, is the **sharp onset of two separated positive-length positivity windows** in this entire family. The method conserves mass for every timestep even outside the positivity windows. At \(n=18\), the three endpoints are approximately \(0.3624244418\), \(0.4927362529\), and \(1.0948732395\), respectively; these decimals are illustrations, not the definitions of the endpoints.

## Assumptions and scope
The graphs are simple, unweighted, connected, and undirected; each \(K_n\) contains \(n\) vertices. For each fixed integer \(n\ge2\), the numerical step is a nonnegative real \(h\) without any stability-related restriction. All comparisons concern exact real arithmetic and entrywise, one-step nonnegativity, including boundary equality; no positivity of internal Runge–Kutta stages is assumed. The result does not cover other graph families, arbitrary weights, nonlinear equations, or repeated-step sign patterns.

## Proof
**1. Four orbit entries.** Put \(D(t)=t^2+6t+12\), \(g(t)=t/D(t)\), and \(r(t)=1-12g(t)=(t^2-6t+12)/D(t)\). Both the numerator \((t-3)^2+3\) and the denominator of \(r(t)\) are strictly positive for \(t\ge0\). The Laplacian of \(K_2\square K_n\) is a Kronecker sum, and its four eigenvalues are \(0,2,n,n+2\). Using the constant and mean-zero projectors in the two coordinates, the four distinct matrix-entry values, for a fixed vertex \((x,y)\), are
\[
\begin{aligned}
t_{00}&=\frac{1+(n-1)r(nh)+r(2h)+(n-1)r((n+2)h)}{2n},\\
t_{10}&=\frac{6}{n}\bigl[g(2h)+(n-1)(g((n+2)h)-g(nh))\bigr],\\
t_{01}&=\frac{6}{n}\bigl[g(nh)+g((n+2)h)-g(2h)\bigr],\\
t_{11}&=\frac{6}{n}\bigl[g(2h)+g(nh)-g((n+2)h)\bigr].
\end{aligned}
\]
The subscripts indicate whether the respective \(K_2\) and \(K_n\) coordinates are changed. In particular, \(t_{00}>0\) for all \(h\ge0\). For \(h>0\), \(t_{11}>0\): since \(g(t)/t=1/D(t)\) strictly decreases on positive arguments, \(g(a)+g(b)>g(a+b)\) for \(a,b>0\) (apply the inequality separately to \(a\) and \(b\)). At \(h=0\), \(T_n(0)=I\).

**2. Exact entry signs.** Clearing the three positive denominators gives the identities
\[
\boxed{\quad t_{10}=\frac{12hA_n(h)}{D(2h)D(nh)D((n+2)h)},\qquad
t_{01}=\frac{12hB_n(h)}{D(2h)D(nh)D((n+2)h)}.\quad}
\]
Both identities follow by direct expansion and can also be reconstructed symbolically with the included verification program. Consequently, for every \(h>0\), entrywise positivity is equivalent to **both** \(A_n(h)\ge0\) and \(B_n(h)\ge0\).

**3. The \(B\)-threshold.** For \(n=2,3\), all coefficients of \(B_n\) are strictly positive. For \(n\ge4\), its leading coefficient is negative and every lower coefficient is strictly positive. Descartes' rule of signs gives at most one positive root, and the opposite signs at zero and at infinity give exactly one positive root \(\gamma_n\). Thus \(B_n\) is positive before \(\gamma_n\) and negative afterward.

**4. Absence of \(A\)-roots below \(18\).** For \(2\le n\le6\), every coefficient of \(A_n\) is strictly positive. For the **exhaustive finite integer range** \(7\le n\le17\), the exact rational Sturm sequences of the displayed quartics have signs \((+,+,-,-,-)\) at zero for every \(n\); at positive infinity the signs are \((+,+,+,-,-)\) for \(7\le n\le14\) and \((+,+,+,+,-)\) for \(15\le n\le17\). Each endpoint has exactly one sign variation, so Sturm's theorem gives **zero** strictly positive roots for each of these eleven integer values. Since \(A_n(0)=144>0\), \(A_n\) is positive throughout \((0,\infty)\). All eleven Sturm sign patterns are reproduced with exact integers/rationals by the standalone verification program; there is no numerical-root or extrapolation step in this finite exhaustive argument.

**5. Two \(A\)-roots from \(18\) onward.** For every integer \(n\ge18\), the coefficient signs of \(A_n\), in decreasing order, are \((+,+,-,+,+)\), allowing **at most two** positive roots by Descartes' rule. Direct substitution gives
\[
A_n(8/n)=-\frac{16}{n^4}(39n^4-592n^3-1536n^2-1536n-2048).
\]
Writing \(n=18+t\) with integer \(t\ge0\), the expression in parentheses equals
\[
39t^4+2216t^3+42312t^2+277536t+114160>0.
\]
Thus \(A_n(8/n)<0\). Since \(A_n(0)>0\) and \(A_n(h)\to+\infty\) as \(h\to\infty\), the polynomial has exactly two positive roots, with \(\alpha_n<8/n<\beta_n\). Both crossings are strict; positivity of \(A_n\) returns after \(\beta_n\).

**6. The recovered interval is nonempty.** Set \(h_*=\sqrt{12/n}\). For \(n\ge18\), \(h_*>8/n\). Reducing the two quartics modulo \(h^2-12/n\) produces
\[
\begin{aligned}
A_n(h_*)&=(576+576/n)h_*+720+2304/n+1152/n^2>0,\\
B_n(h_*)&=(72n+432+576/n)h_*+720+2304/n+1152/n^2>0.
\end{aligned}
\]
Because \(A_n(h_*)>0\) on the far side of \(8/n\), necessarily \(h_*>\beta_n\). Because \(B_n(h_*)>0\) and \(B_n\) has exactly one positive root, \(h_*<\gamma_n\). Hence \(\alpha_n<\beta_n<h_*<\gamma_n\), and both stated positivity windows follow, including their endpoints. The classification is complete.

## Verification
The embedded `artifacts/verify_rook_pade.py` independently assembles the rational Padé map for selected complete small matrices and verifies the entry-orbit formulas; it also verifies both symbolic quartic identities, the exact Sturm endpoint sign patterns, the test-value and recovery identities, and algebraic root counts for a finite collection of larger sizes. Its completed execution printed `VERIFY_OK exact checks: 255`. The proof for **every** integer \(n\ge18\) uses analytic coefficient signs, Descartes' rule, and explicit witnesses—not finite numerical sampling. The proof for \(7\le n\le17\) uses exact exhaustive finite Sturm computations, whose endpoint data are supplied above.

For \(n=18\), exact rational steps \(1/3,2/5,4/5,6/5\) exhibit, respectively, a positive, negative, positive, negative update (entrywise); these illustrate the two-window phenomenon with no reliance on rounded root locations.

## Relationship to prior work
The classical two-stage Gauss–Legendre method has the diagonal \([2/2]\) Padé stability function. Zappavigna, Colaneri, Kirkland, and Shorten (2012) exhibit limitations of diagonal Padé discretizations for positive linear systems, including nonconservative examples; their results do not supply the precise two-row rook-graph phase diagram here. Lóczi and Ketcheson (2013/2014) study rational-function absolute monotonicity and uniform positivity guarantees. Such **uniform-over-generators** bounds cannot determine the graph-specific two disjoint positive-length windows proved above. Related studies of nonnegative time stepping on paths, hypercubes, and finite Markov chains concern different state graphs or distinct extremal questions. The small case \(n=2\) is the four-cycle, also the two-dimensional binary hypercube, and is not claimed as a new isolated case. The sharp \(n=18\) transition and complete polynomial root-order classification are additional results beyond those general tools.

## Limitations
This is a graph-family-specific mathematical statement, not a claim of unconditional positivity of the Gauss–Legendre method. The map is row-stochastic in the sense that its rows sum to one for every \(h\), but it is a **stochastic transition matrix only at the stated nonnegative timesteps**. No floating-point roundoff bounds, internal-stage positivity, multi-step strong-stability property, or efficiency comparison are established. Equivalent results in less accessible or unindexed literature remain possible. Independent review has not been conducted.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Maynooth University public working-paper deposit, 19 June 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/ . See the publicly available full working paper, especially the Padé positivity examples.
2. L. Lóczi, D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, first made public 26 March 2013, https://arxiv.org/abs/1303.6651 .
3. J. A. van de Griend, J. F. B. M. Kraaijevanger, *Absolute monotonicity of rational functions occurring in the numerical solution of initial value problems*, Numerische Mathematik 49 (1986), 413–424, https://doi.org/10.1007/BF01389539 .
4. T. Schatz, V. Thomée, L. Wahlbin, *On positivity and maximum-norm contractivity in time stepping methods for parabolic equations*, Computational Methods in Applied Mathematics 10 (2010), https://doi.org/10.2478/cmam-2010-0025 .
