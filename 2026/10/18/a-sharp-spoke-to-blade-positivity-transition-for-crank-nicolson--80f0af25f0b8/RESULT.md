# A sharp spoke-to-blade positivity transition for Crank–Nicolson diffusion on generalized windmills

## Finding

For integers \(r,s\ge 2\), let \(G=K_1\vee(rK_s)\): one hub joined to each vertex of \(r\) disjoint cliques, each containing \(s\) vertices. Give every hub-to-clique edge conductance \(b>0\), and every internal clique edge conductance \(a>0\). Let \(L\) be the symmetric weighted combinatorial Laplacian. For the **completed** Crank–Nicolson update
\[
T(h)=(I+\tfrac h2 L)^{-1}(I-\tfrac h2 L),\qquad h\ge0,
\]
write \(H(r,s;a,b)\) for the largest step at which \(T(h)\) is entrywise nonnegative.

Define the critical ratio
\[
\Xi_{r,s}=\frac{r(rs-1)}{r(s-2)+1}.
\]
Then the sharp positivity horizon obeys the **exact phase law**
\[
H(r,s;a,b)=\frac{2}{(rs-1)b}\quad\text{if and only if}\quad \frac ab\le \Xi_{r,s}.
\]
For \(a/b>\Xi_{r,s}\), the sharp horizon is strictly smaller and is the unique positive solution \(h\) of
\[
\frac{1}{rs+1}+\frac{1}{rs(rs+1)[1+\frac h2(rs+1)b]}
+\frac{r-1}{rs[1+\frac h2 b]}
+\frac{s-1}{s[1+\frac h2(b+sa)]}=\frac12.
\]
In this second regime the horizon is strictly decreasing as \(a\) increases, with \(r,s,b\) fixed; below the critical ratio it is exactly constant as \(a\) varies. Equality at the transition means that hub and clique vertices lose diagonal positivity simultaneously. At any strictly larger step, at least one diagonal entry of \(T(h)\) is negative.

For fixed \(r,s,b\), the large internal-conductance limit distinguishes triangles from larger clique blades:
\[
\begin{aligned}
s=2:\quad&H(r,2;a,b)=\sqrt{\frac{2}{ab}}+\frac1a+O\left(\frac{\sqrt b}{a^{3/2}}\right),\\
s\ge3:\quad&H(r,s;a,b)=\frac{2}{(s-2)a}+O\left(\frac b{a^2}\right),
\end{aligned}\qquad a/b\to\infty.
\]
In particular, generalized friendship graphs (\(s=2\)) have a square-root, rather than reciprocal, positivity-collapse law. The leading constants in both regimes are independent of the number of blades \(r\).

## Assumptions and scope

The graph is finite, connected and undirected. There are \(r\ge2\) cliques of equal size \(s\ge2\), all clique edges have a common strictly positive conductance \(a\), and all spoke edges have a common strictly positive conductance \(b\). The update is applied once to a vector of vertex values; entrywise positivity of the full update matrix is equivalent to preservation of nonnegative initial data for that step. The step length \(h\) has time units reciprocal to conductance. No finite-element mass matrix, boundary condition, nonuniform blade size, or variable stepping is asserted. The scheme is spectrally stable for every \(h\ge0\), but that does not imply entrywise nonnegativity.

## Proof

Set \(M=rs\), \(N=M+1\), and \(t=h/2\). There is an orthogonal four-space decomposition of \(\mathbb R^N\): constants (dimension one, Laplacian eigenvalue zero); the hub-versus-all-leaves contrast (dimension one, eigenvalue \(Nb\)); contrasts of blade-constant vectors summing to zero across blades (dimension \(r-1\), eigenvalue \(b\)); and within-blade zero-sum vectors (dimension \(r(s-1)\), eigenvalue \(b+sa\)). These eigenvalues may coincide for special parameters, but the orthogonal invariant spaces and their projector formulas remain valid.

To see the eigenvalues, a vector summing to zero on a single blade is annihilated by its hub coupling and gains \(sa+b\) from the intra-blade Laplacian and the spoke. A vector constant on every blade with blade amplitudes summing to zero and hub amplitude zero receives only the spoke rate \(b\). The hub-versus-leaf contrast has value \(-M\) at the hub and \(1\) at each leaf; it is an eigenvector of eigenvalue \(Nb\). Constants have eigenvalue zero. The dimensions sum to \(N\).

Let \(R(t)=(I+tL)^{-1}\). Orthogonal projectors give a hub diagonal and the common leaf diagonal
\[
R_{00}(t)=\frac1N+\frac{M}{N(1+tNb)},
\]
\[
R_{vv}(t)=\frac1N+\frac{1}{MN(1+tNb)}+
\frac{r-1}{M(1+tb)}+\frac{s-1}{s[1+t(b+sa)]},\quad v\ne0.
\]
For clarity, the projector diagonal at a leaf in the four spaces, in the same order, equals \(1/N\), \(1/(MN)\), \((r-1)/M\), and \((s-1)/s\). The corresponding hub projector diagonals are \(1/N,M/N,0,0\). These entries sum to one in either vertex orbit.

The resolvent \(R(t)\) has strictly positive entries for \(t>0\), because \(I+tL\) is an irreducible nonsingular symmetric \(M\)-matrix (equivalently, \(R(t)=\int_0^\infty e^{-u}e^{-utL}\,du\)). Since \(T(h)=2R(h/2)-I\), every off-diagonal entry is positive. Consequently, nonnegativity is equivalent **exactly** to the two diagonal tests \(R_{00}(h/2)\ge1/2\) and \(R_{vv}(h/2)\ge1/2\). Each resolvent diagonal decreases strictly and continuously from one to \(1/N<1/2\) with increasing \(h\), giving unique positive individual thresholds.

Solving the hub equation \(R_{00}(t)=1/2\) gives \(t_0=1/[(M-1)b]\). Evaluate the leaf diagonal at this point. Direct substitution and cancellation yield
\[
R_{vv}(t_0)-\frac12=
-\frac{(rs-1)\,[\,(r(s-2)+1)(a/b)-r(rs-1)\,]}{2r^2s^2\,[\,r+a/b\,]}.
\]
All factors outside the displayed affine numerator are positive. Thus the leaf is still nonnegative at the hub threshold exactly when \(a/b\le\Xi_{r,s}\). If this inequality holds, the hub threshold is the global one. Otherwise the leaf reaches \(1/2\) first and gives the unique scalar equation in the finding. Strict decrease of that scalar root with \(a\) follows from \(\partial R_{vv}/\partial a=-(s-1)t/[1+t(b+sa)]^2<0\) for \(t>0\), together with strict decrease in \(t\). This proves the sharp phase law and all boundary inclusions.

For the asymptotics, put \(x=a/b\) and \(z=bt\). At fixed \(r,s\) with \(x\to\infty\), the leaf threshold \(z\to0\), since its diagonal at any fixed \(z>0\) approaches a value below \(1/2\). For \(s\ge3\), setting \(z=y/x+o(x^{-1})\) in the leaf equation gives \(1/s+(s-1)/[s(1+sy)]=1/2\), hence \(y=1/(s-2)\). The analytic implicit-function theorem in \(1/x\) upgrades this to \(z=1/[(s-2)x]+O(x^{-2})\).

For \(s=2\), the three terms not belonging to the within-blade eigenspace sum to \(1/2-z/2+O(z^2)\) as \(z\downarrow0\), whereas the within-blade contribution is \(1/[2(1+z(1+2x))]\). Balancing these terms forces \(z\asymp x^{-1/2}\). Expanding with \(\epsilon=x^{-1/2}\) and \(z=\epsilon/\sqrt2+c\epsilon^2+O(\epsilon^3)\), the coefficient of \(\epsilon^2\) in the exact equation gives \(c=1/2\). Multiplication by \(2/b\) gives the two-term expansion in the finding. Positivity and monotonicity of the relevant scalar root justify choosing the displayed branch; the analytic expansion in \(\epsilon\) follows by rescaling \(z=\epsilon y\) and using a nonvanishing derivative at \(y=1/\sqrt2\).

## Verification

Run `python3 verify.py` from the directory containing this document and the accompanying source file. It uses only the Python standard library. It constructs the full weighted Laplacian, inverts \(I+tL\) over rational numbers for small parameters, checks every resolvent diagonal against the spectral formula, confirms strict positivity of off-diagonal resolvent entries, checks exact stochastic row sums of \(2R-I\), tests the critical sign and equality for rational conductances, and probes both large-ratio asymptotic regimes. Successful execution prints `VERIFY_OK 1290 assertion groups; exact rational matrices and singular-limit probes`. The exhaustive direct-matrix comparisons are finite computational corroboration; the proof above establishes all dimensions, conductances and time steps.

## Relationship to prior work

The general Crank–Nicolson positivity-versus-resolvent-diagonal equivalence is already established for Markov generators, including in prior public work on resolvent-return laws. The present proof uses that principle rather than claiming it as new. General positive time-stepping and maximum-principle work includes Schatz, Thomée and Wahlbin (2010) and Jin, Lazarov, Thomée and Zhou (2015); the latter studies subdiffusive finite-element discretizations, not this weighted graph family. Higueras and Roldán (2023) determine exact positivity thresholds for a one-dimensional Dirichlet heat grid by Chebyshev-style methods. Those matrix geometries and estimates do not give the displayed \((r,s,a/b)\) phase line or the distinct square-root versus inverse-conductance singular laws.

A general sharp theta-method lower bound for graphs of bounded maximum edge conductance is also known. It yields the present hub threshold in some saturated-hub subcases (notably \(a\le b\)) but does not establish the extended flat region \(1<a/b\le\Xi_{r,s}\) or the leaf-controlled regime. The contribution is the explicit two-parameter switch, proof that no other matrix entry can become restrictive, and two different strong-blade asymptotic exponents. Published and prior-result claim searches did not identify an equivalent generalized-windmill phase classification; they do not establish exhaustive novelty.

## Limitations

The result concerns homogeneous edge conductances within each of two edge orbits and ordinary unnormalized graph Laplacians; arbitrary heterogeneous edge weights or general signed discretizations are outside scope. Equality and singular asymptotic errors assume fixed finite \(r,s,b\), with \(b>0\), before taking \(a/b\to\infty\). It does not address accuracy of a discretized spatial PDE, time-varying steps, independent external verification, or originality in unindexed literature. The generic resolvent reduction is pre-existing; this is a graph-specific sharp classification.

## References

- A. H. Schatz, V. Thomée and L. B. Wahlbin, “On positivity and maximum-norm contractivity in time stepping methods for parabolic equations,” *Computational Methods in Applied Mathematics* **10** (2010), 421–443, DOI: 10.2478/cmam-2010-0025.
- B. Jin, R. Lazarov, V. Thomée and Z. Zhou, “On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations,” arXiv:1510.02825v1, publicly posted 9 October 2015; https://arxiv.org/abs/1510.02825.
- I. Higueras and T. Roldán, “A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation,” arXiv:2301.01066v1, publicly posted 3 January 2023; https://arxiv.org/html/2301.01066v1.
- “A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains,” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a (general Markov-resolvent result; its indexed summary was available for comparison, but its linked full record was not readable during this assessment).
