# Exact endpoint amplification and spoke–rim transition in weighted wheel networks

## Finding
For every integer \(n\ge3\), let \(W_n=K_1\vee C_n\) be the wheel graph with one hub and \(n\) cyclic rim vertices. Give every spoke conductance \(a>0\) and every rim edge conductance \(1\). For an arbitrary orientation, form the edge-incidence operator \(B\), the diagonal conductance matrix \(C\), the Laplacian \(L=B^{\mathsf T}CB\), and the symmetric electrical-gradient projection
\[
\Pi_{n,a}=C^{1/2}BL^+B^{\mathsf T}C^{1/2}.
\]
Set \(m=\lfloor n/2\rfloor\), \(\rho=(a+2-\sqrt{a(a+4)})/2\), and
\[
 g_j=\frac{\rho^j+\rho^{n-j}}{\sqrt{a(a+4)}(1-\rho^n)},\qquad 0\le j\le n.
\]
Then the exact, attained induced maximum norm on real edge signals is
\[
\boxed{\|\Pi_{n,a}\|_{\ell^\infty\to\ell^\infty}=\max\{S_n(a),R_n(a)\}},
\]
where the spoke-row and rim-row absolute sums are, respectively,
\[
 S_n(a)=1+2\sqrt a\,(g_0-g_m),\qquad
 R_n(a)=2-2ag_0+2\sqrt a\,(g_0-g_m).
\]
Every spoke row has norm \(S_n(a)\) and every rim row has norm \(R_n(a)\); a sign input supported on all edges attains either row norm. There is a **unique** \(a_n>0\) satisfying \(a_ng_0(a_n)=1/2\). The rim rows dominate for \(0<a<a_n\), the spoke rows dominate for \(a>a_n\), and the two types tie at \(a=a_n\). The thresholds increase strictly with \(n\) and satisfy
\[
\boxed{a_3=1<a_4<a_5<\cdots<\frac43,\qquad\lim_{n\to\infty}a_n=\frac43.}
\]
For any fixed \(a>0\), the two row norms converge to
\[
\lim_{n\to\infty}S_n(a)=1+\frac2{\sqrt{a+4}},\qquad
\lim_{n\to\infty}R_n(a)=2+\frac{2(1-\sqrt a)}{\sqrt{a+4}}.
\]
These limits exhibit a sharp **noncommutation of vanishing spoke conductance and increasing rim size**:
\[
\boxed{\lim_{a\downarrow0}\lim_{n\to\infty}\|\Pi_{n,a}\|=3,\qquad
\lim_{n\to\infty}\lim_{a\downarrow0}\|\Pi_{n,a}\|=2.}
\]
In particular, for unit conductances \(a=1\), rim rows dominate for every \(n>3\), and
\[
\boxed{\|\Pi_{n,1}\|=2-\frac{2(\rho^m+\rho^{n-m})}{\sqrt5(1-\rho^n)},\quad\rho=(3-\sqrt5)/2,}
\]
which is strictly increasing in \(n\), approaches \(2\) from below, and has an explicit even/odd exponential defect.

## Assumptions and scope
Everything is finite, real, and unweighted on the rim. The spoke conductance \(a\) is constant within the spoke orbit but may be any positive real number. The norm on the \(2n\) symmetrically conductance-scaled edge coordinates is the ordinary \(\ell^\infty\) norm. It is not the norm of unscaled electrical currents when \(a\ne1\). Orientation choices only conjugate the projection by a diagonal sign matrix and leave the induced norm unchanged. The symbol \(L^+\) means the Moore–Penrose inverse of the full graph Laplacian.

## Proof
**1. Grounded inverse and its monotonicity.** Ground the hub, label the rim by \(\mathbb Z/n\mathbb Z\), and let \(D\) be the cyclic forward difference matrix. The grounded Laplacian is
\[
 K_a=aI+D^{\mathsf T}D=(a+2)I-T-T^{-1}.
\]
The symmetric kernel \(g_j\) in the Finding section satisfies \((a+2)g_j-g_{j-1}-g_{j+1}=\mathbf1_{j=0}\) with indices modulo \(n\), because \(\rho+\rho^{-1}=a+2\), and the jump at zero equals one. Therefore \((K_a^{-1})_{ij}=g_{i-j}\). Each entry is strictly positive and \(\sum_{j=0}^{n-1}g_j=1/a\). Moreover, \(g_0>g_1>\cdots>g_m\), with symmetry \(g_{n-j}=g_j\). The sequence \(j\mapsto g_j\), viewed on the full interval \(0\le j\le n\), is strictly convex by its explicit sum of exponentials.

**2. Exact spoke rows.** The grounded incidence row of a spoke is the coordinate vector at its rim endpoint, weighted by \(\sqrt a\). A unit edge input at a spoke gives rim potentials \(\sqrt a\,g_j\). The sum of absolute outputs at all spokes is \(a\sum_jg_j=1\). The total absolute rim difference is \(\sqrt a\sum_j|g_j-g_{j+1}|=2\sqrt a(g_0-g_m)\) by the cyclic monotone rise and fall of the Green sequence. This proves the formula for \(S_n(a)\).

**3. Exact rim rows.** A rim-edge input joining rim vertices \(0\) and \(1\) gives rim potentials \(v_j=g_j-g_{j-1}\) (possibly with an overall sign). The spoke absolute outputs sum to
\[
\sqrt a\sum_j|v_j|=2\sqrt a(g_0-g_m).
\]
The sequence of first differences \(v_1,v_2,\ldots,v_n\), where \(v_n=v_0\), is strictly increasing by convexity of \(g_j\); it runs from \(-A\) to \(+A\), where \(A=g_0-g_1\). Including the closing rim edge from \(v_0=+A\) back to \(v_1=-A\) gives total cyclic variation \(\sum_j|v_j-v_{j+1}|=4A\). Thus
\[
R_n(a)=2\sqrt a(g_0-g_m)+4(g_0-g_1).
\]
The equation at the Green source, \((a+2)g_0-2g_1=1\), implies \(4(g_0-g_1)=2-2ag_0\), proving the displayed simplified formula. These are all rows by wheel symmetry. A sign vector matching a maximizing row attains its absolute sum, hence the induced maximum norm is the maximum of these two expressions (not merely an upper bound).

**4. Unique crossover.** Subtracting gives
\[
R_n(a)-S_n(a)=1-2a g_0(a).
\]
Put \(h_n(a)=a e_0^{\mathsf T}K_a^{-1}e_0\). Differentiating the finite inverse yields
\[
h_n'(a)=e_0^{\mathsf T}K_a^{-1}(D^{\mathsf T}D)K_a^{-1}e_0>0.
\]
Strict positivity holds because \(K_a^{-1}e_0\) is nonconstant for every \(n\ge3\). At \(a\downarrow0\), spectral decomposition into the constant and mean-zero cyclic subspaces gives \(h_n(a)\to1/n<1/2\); at \(a\to\infty\), \(h_n(a)\to1\). The intermediate value theorem and strict derivative give a unique crossover.

From the explicit Green kernel,
\[
h_n(a)=\sqrt{\frac a{a+4}}\frac{1+\rho(a)^n}{1-\rho(a)^n}.
\]
For fixed \(a\), this strictly decreases as \(n\) grows, so the unique roots \(a_n\) strictly increase. At \(n=3\) and \(a=1\), direct substitution gives \(h_3(1)=1/2\); hence \(a_3=1\). For every finite \(n\), \(h_n(a)>\sqrt{a/(a+4)}\), while the latter increasing function equals \(1/2\) exactly at \(a=4/3\). Thus \(a_n<4/3\). Passing to the limit in the defining equation, using uniform convergence of \(h_n(a)\) on compact positive \(a\)-intervals, shows \(a_n\to4/3\).

**5. Asymptotics and singular order of limits.** For fixed \(a>0\), \(0<\rho(a)<1\), hence \(g_m\to0\) and \(g_0\to1/\sqrt{a(a+4)}\) as \(n\to\infty\). Substitution gives the two limiting branch formulas. For fixed \(n\), as \(a\downarrow0\), the Green operator has the expansion \(K_a^{-1}=\frac1{an}\mathbf1\mathbf1^{\mathsf T}+O(1)\); therefore \(ag_0\to1/n\) and \(\sqrt a(g_0-g_m)\to0\). The spoke branch tends to \(1\), while the rim branch tends to \(2-2/n\), which exceeds \(1\) for \(n\ge3\). Hence the inner limit of the whole norm is \(2-2/n\). Reversing the order of limits gives \(\max\{2,3\}=3\), while taking \(n\to\infty\) after the first limit gives \(2\).

Finally, at \(a=1\) the crossover puts \(n>3\) on the rim branch. The source equation gives \(R_n(1)=2-2g_m\). Substitution yields the advertised formula. For \(n=2m\), \(g_m=2\rho^m/[\sqrt5(1-\rho^{2m})]\); for \(n=2m+1\), \(g_m=(1+\rho)\rho^m/[\sqrt5(1-\rho^{2m+1})]\). The even-to-odd and odd-to-even ratios of successive \(g_m\) are both strictly below one because \(0<\rho<1\). This proves strict increase in \(n\), and the two formulas give the claimed parity-dependent exponential defect.

## Verification
The standalone standard-library Python program `verify.py` constructs and exactly inverts grounded weighted Laplacians with rational conductance square roots, independently assembles the full symmetric projection matrix, and compares the actual absolute row sums with both formulas. It checks 78 graph/conductance profiles (all rim sizes from 3 through 15 and spoke conductances \(1/16,1/4,1,9/4,4,16\)); it also checks projection symmetry, trace, and selected exact idempotences. Execution from the directory containing this file and `verify.py` prints `VERIFY_OK`. Direct numeric evaluation of the exponential Green formula corroborates the exact inverse. These finite computations do not certify universal statements; the analytic proof above supplies those.

## Relationship to prior work
Bapat and Gupta (2010; manuscript dated 2009), *Resistance distance in wheels and fans*, explicitly derive the full wheel inverse-Laplacian kernel and the corresponding spoke-to-hub and rim-to-rim effective resistances; those formulas are prior knowledge and **are not claimed as new**. Their available full-text Theorem 5, proof, and Corollary 6 concern pairwise effective resistance. They do not state or evaluate the absolute transfer-current row sums, the edge-projection maximum norm, the spoke–rim crossover, or the noncommuting singular limits. The present proof needs absolute variation and a comparison between the two edge orbits, not only the kernel itself.

Kelner and Maymounkov (2009), *Electric routing and concurrent flow cutting*, give a general electrical-routing operator framework and bounds, not the wheel-specific sharp norm profile. A separate wheel symmetric-edge-polytope result obtains the optimal Löwner ellipsoid through weighted Laplacian determinants; its extremal ellipsoid and shape-design parameters are different from the fixed-conductance \(\ell^\infty\) electrical-gradient projection here. A previously derived exact formula for parallel-path network electrical projections does not cover wheels with at least four rim vertices: wheels contain overlapping cycles and are not internally disjoint two-terminal path unions. The degree-three wheel is the complete graph \(K_4\), but its general-spoke-conductance family is not covered by a formula for one exceptional edge of \(K_4\).

## Limitations
The result requires all spokes to share one conductance and all rim edges to have unit conductance. It does not provide a formula for arbitrary positive edge weights, arbitrary planar networks, or unscaled physical-current norms. The references include one earlier full Green-kernel determination; originality concerns the nonlinear absolute-value aggregation, exact crossover, and singular asymptotics, not the kernel inversion. Older electrical-circuit literature may contain an equivalent transfer-current norm calculation; independent mathematical and historical review remain necessary.

## References
1. R. B. Bapat and S. Gupta, *Resistance distance in wheels and fans*, Indian Journal of Pure and Applied Mathematics 41 (2010), 1–13, DOI `10.1007/s13226-010-0004-2`; full author-manuscript text presented at https://www.researchgate.net/publication/225679174_Resistance_distance_in_wheels_and_fans (original manuscript displays February 24, 2009; that date is not treated as a verified public upload date).
2. J. Kelner and P. Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859v1, publicly submitted 2009-09-15; https://arxiv.org/abs/0909.2859.
3. *The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes*, publicly available full result at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-exact-l-wner-ellipsoid-and-exponential-edge-weight-stabiliza--39d62ea47ea0; a distinct invariant on the same graph family.
