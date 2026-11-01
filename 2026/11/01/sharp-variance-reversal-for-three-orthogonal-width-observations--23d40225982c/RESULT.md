# Sharp variance reversal for three orthogonal width observations of rectangular boxes

## Finding

Let \(K=[0,a]\times[0,b]\times[0,c]\subset\mathbb R^3\), where \(a,b,c>0\). Choose a uniformly distributed orthonormal frame \((U_1,U_2,U_3)\in SO(3)\), and let \(W_j\) be the Euclidean length of the orthogonal projection of \(K\) onto the line with direction \(U_j\). Put \(s=a+b+c\), \(q=a^2+b^2+c^2\), and
\[
A=\frac{8}{3\pi^2}-\frac14,\qquad B=\frac{8}{3\pi^2}-\frac{2}{3\pi},\qquad T=\frac BA=2.87190393517865\ldots.
\]
For **any distinct** \(i,j\in\{1,2,3\}\), the complete first- and second-order joint statistics are
\[
\begin{aligned}
\mathbb E W_i&=s/2,\\
\operatorname{Var}(W_i)&=\left(\frac13-\frac{2}{3\pi}\right)q+\left(\frac{2}{3\pi}-\frac14\right)s^2,\\
\operatorname{Cov}(W_i,W_j)&=A s^2-Bq.
\end{aligned}
\]
Consequently the covariance is strictly positive, zero, or strictly negative according as \(s^2/q\) is greater than, equal to, or less than \(T\). In particular, it is **strictly positive for a cube**, while sufficiently elongated boxes have negative covariance. For \(a=b=1,c=t\) the sign changes at the two positive roots of
\[
(1-T)t^2+4t+4-2T=0,
\]
namely \(t=0.61020008\ldots\) and \(t=1.52666171\ldots\); it is positive precisely between them.

The orthogonal-frame average \(\bar W_o=(W_1+W_2+W_3)/3\) and the average \(\bar W_{\mathrm{iid}}\) of three independent uniformly directed widths are both unbiased for the mean width \(s/2\). Their **exact variance-efficiency ratio** obeys the universal sharp bounds
\[
\boxed{\ \frac{16}{\pi}-5\ <\ \frac{\operatorname{Var}(\bar W_o)}{\operatorname{Var}(\bar W_{\mathrm{iid}})}\ \le\ 1+\frac{2(16/\pi^2+2/\pi-9/4)}{4/\pi-5/4}.\ }
\]
The left endpoint \(16/\pi-5=0.09295817894065\ldots\) is approached by boxes with two side lengths tending to zero relative to the third, but is not attained by any full-dimensional box. The upper endpoint \(1.66771623397995\ldots\) is attained **exactly by cubes** (up to common scaling and permutation). At the same transition \(s^2/q=T\), orthogonal and independent three-view averaging have equal variance. Thus orthogonality substantially improves the efficiency for needle-shaped boxes but can make it approximately \(66.8\%\) worse for cubes.

## Assumptions and scope

The widths are full projection lengths, not radii or chord lengths. The frame is sampled from normalized Haar probability on \(SO(3)\); columns are pairwise perpendicular and dependent, unlike three independent Haar directions. All three side lengths are strictly positive. The ratio compares two designs using three total directional measurements each, on the same fixed box; it does not optimize over arbitrary nonorthogonal sampling schemes. Rotations, translations, or permutations of the box's principal axes do not affect the law. No claim is made for a general nonorthogonal parallelotope or arbitrary convex body.

## Proof

**1. Geometric width identity.** The width of a rectangular box along any unit vector \(u\) is
\[
W_K(u)=a|u_1|+b|u_2|+c|u_3|.
\]
This follows by separately maximizing and minimizing the linear coordinate function over the three intervals.

**2. Four Haar absolute moments.** Write the matrix of the random frame as \(O=(O_{ij})\). By spherical uniformity,
\[
\mathbb E|O_{11}|=\frac12,\quad \mathbb E O_{11}^2=\frac13,\quad
\mathbb E|O_{11}O_{21}|=\mathbb E|O_{11}O_{12}|=\frac{2}{3\pi}.
\]
For example the last identities follow because \((O_{11}^2,O_{21}^2,O_{31}^2)\) has the Dirichlet distribution with parameters \((1/2,1/2,1/2)\), and the rows have the same spherical law as the columns.

The crucial genuinely orthogonal two-coordinate moment is
\[
\boxed{\mathbb E|O_{11}O_{22}|=\frac{8}{3\pi^2}.}
\]
Here is a direct derivation: condition on the first column \(u\), which is uniform on \(S^2\). The second column is uniform on the unit circle in \(u^\perp\), so \(\mathbb E(|O_{22}|\mid u)=(2/\pi)\sqrt{1-u_2^2}\). Conditional on \(u_2=x\), the other two coordinates are uniform on the circle of radius \(\sqrt{1-x^2}\), so \(\mathbb E(|u_1|\mid u_2=x)=(2/\pi)\sqrt{1-x^2}\). Since \(\mathbb E(1-u_2^2)=2/3\), iterated expectation gives \((4/\pi^2)(2/3)\). Symmetry gives the same value for every pair of matrix entries lying in different rows and different columns.

**3. Covariance and phase boundary.** Summing these moments with the three edge-length weights yields
\[
\begin{aligned}
\mathbb E W_1^2&=\left(\frac13-\frac{2}{3\pi}\right)q+\frac{2}{3\pi}s^2,\\
\mathbb E(W_1W_2)&=\left(\frac{2}{3\pi}-\frac{8}{3\pi^2}\right)q+\frac{8}{3\pi^2}s^2.
\end{aligned}
\]
Subtract the squared common mean \(s^2/4\) to obtain the displayed variance and covariance. Note \(A>0\), \(B>0\), by the elementary bounds \(3<\pi<22/7\). Since \(q<s^2\le3q\), with the second equality precisely for cubes by Cauchy--Schwarz, \(A s^2-Bq=Aq(s^2/q-T)\) proves the sign classification. Moreover \(1<T<3\): the first inequality is equivalent to \(2/(3\pi)<1/4\), and the second to \(16/\pi^2+2/\pi>9/4\); the latter is equivalent to \(64+8\pi-9\pi^2>0\), which holds for \(3<\pi<22/7\) because the quadratic is decreasing on that interval and equals \(12/49>0\) at \(22/7\). For two equal sides, substituting \(s=2+t\), \(q=2+t^2\) gives the quadratic and its two simple positive roots.

**4. Sharp comparison of orthogonal and independent direction sampling.** Exchangeability of the three columns yields
\[
\operatorname{Var}(\bar W_o)=\frac{V+2C}{3},\qquad
\operatorname{Var}(\bar W_{\mathrm{iid}})=\frac{V}{3},
\]
where \(V=\operatorname{Var}(W_1)>0\) and \(C=\operatorname{Cov}(W_1,W_2)\). Put \(r=s^2/q\), and define
\[
C_0=\frac13-\frac{2}{3\pi},\qquad D_0=\frac{2}{3\pi}-\frac14.
\]
Their ratio is the one-variable function
\[
R(r)=1+\frac{2(Ar-B)}{C_0+D_0r},\qquad 1<r\le3.
\]
A direct derivative calculation gives
\[
R'(r)=\frac{2(AC_0+BD_0)}{(C_0+D_0r)^2},\qquad
AC_0+BD_0=-\frac{3\pi^2-12\pi+8}{36\pi^2}>0.
\]
The inequality holds because \(3(\pi-2)^2<4\), implied by \(3<\pi<22/7<2+2/\sqrt3\). Thus \(R\) is **strictly increasing** throughout the attainable shape range; the variance is positive since the projected width is nonconstant for every full-dimensional box. At \(r\downarrow1\), \(R\to16/\pi-5\); at \(r=3\), direct substitution gives the upper expression. The equation \(s^2=3q\) is equivalent to \(a=b=c\), establishing the unique upper equality class. The lower limit follows by taking \((a,b,c)=(\varepsilon,\varepsilon,1)\) as \(\varepsilon\downarrow0\); strict positivity forbids \(r=1\) for an actual box. The strict monotonicity simultaneously establishes the unique efficiency transition \(r=T\).

## Verification

The standalone script `check_frame.py` independently integrates the cross-column moment over the sphere, constructs Haar rotations by normalized quaternion sampling, checks exact means and covariances against 400,000 simulated frames at several box shapes including both transition locations, and compares the frame-average variance with the formula. Run `python3 check_frame.py` with the dependencies in `requirements.txt`. The successful execution prints `ALL_ORTHOGONAL_WIDTH_TESTS_PASSED`. The finite numerical experiments test the calculation; the unrestricted sharp inequalities and phase classification follow from the analytical proof.

## Relationship to prior work

Ivanov's *Tight frames and related geometric problems* (2018, arXiv:1804.10055) studies the geometry of orthogonal and projected frames as a tool for polytopal optimization, notably zonotope projection volumes. It motivates the use of an orthogonal directional design but does not contain the present variance comparison for random width observations. Kabluchko, Litvak, and Zaporozhets (2015, arXiv:1511.08479) give a rich exact and asymptotic theory of **single-direction** cube widths; those marginal formulas yield the cube's one-view variance but not its paired orthogonal-frame covariance. Recent work on same-direction width–brightness covariance of orthotopes (public manuscript, October 2026) gives a different joint statistic and does not imply the paired-perpendicular width formula. A separate three-view Cauchy cubature result concerns worst-case estimation of **surface area from projection areas**, rather than statistical variance of mean-width observations. Orthogonal-frame sampling, ordinary independent spherical sampling, and the direction-dependent coupling are distinguished throughout.

The formulas for absolute moments of a Haar orthogonal matrix are familiar harmonic/probabilistic building blocks and are not asserted to be new in isolation. The assessed mathematical contribution is their use to obtain the **complete sharp shape-dependent phase transition and variance-efficiency interval**, including the uniquely worst cubic shape and the limiting needle-shaped optimum. A previously unindexed equivalent formula for orthogonal directional sampling remains possible; full text for two later weighted-width manuscripts was unavailable and only their abstracts could be compared.

## Limitations

This is a three-dimensional, axis-orthogonal rectangular-box result. It characterizes the covariance and mean-estimator variance, not the joint distribution of all three widths or variance-optimal designs among arbitrary direction triples. The lower extremal ratio is an infimum over full-dimensional boxes, not an attained minimum. Numerical checks are not universal proofs, and the work has not undergone an independent mathematical audit. Historical priority is provisional, particularly for literature framed in sampling or design terminology rather than convex geometry.

## References

1. G. Ivanov, *Tight frames and related geometric problems*, arXiv:1804.10055v1 (first public 2018-04-25), https://arxiv.org/abs/1804.10055 .
2. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1 (first public 2015-11-26), https://arxiv.org/abs/1511.08479 .
3. O. Abas, *Width distributions for rectangular boxes*, arXiv:2608.03305 (abstract accessible; complete text not inspected), https://arxiv.org/abs/2608.03305 .
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (abstract accessible; complete text not inspected), https://arxiv.org/abs/2609.26202 .
5. *Sharp aspect-ratio phase diagram for width–brightness covariance of orthotopes*, published-finding corpus, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-aspect-ratio-phase-diagram-for-width-brightness-covariance--ef50d44d3e36 .
6. *Unique minimax three-view Cauchy cubature with quantitative frame rigidity*, published-finding corpus, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-unique-minimax-three-view-cauchy-cubature-with-quantitative-fram--91f8ebdcfbbc .
7. *Exact directional width law of the cube and its first spherical-cap transition*, published-finding corpus, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2 .
