# Sharp anisotropic rectangle constants in free \(1/2\)-spaces

## Finding
Let \(s,t>0\). Endow \(Q_{s,t}=[0,s]\times[0,t]\) with Manhattan distance and its four-vertex set \(V\) with the restricted metric. Let \(\mathcal F_{1/2}(V)\) be the real Lipschitz-free \(1/2\)-space over \(V\), with any vertex as base point, and let \(R_{s,t}\) be the canonical bilinear vertex-interpolation map. Set \(\lambda=\max\{s,t\}/\min\{s,t\}\). Then **for every positive pair of side lengths**,
\[
\boxed{\operatorname{Lip}(R_{s,t})=L(\lambda):=\frac{\left(2\sqrt\lambda+\sqrt{1+\lambda}\right)^2}{3\lambda+1}.}
\]
The function \(L(\lambda)\) is strictly increasing for \(\lambda\ge1\), equals \(3/2+\sqrt2\) at \(\lambda=1\), and tends to \(3\) as \(\lambda\to\infty\). Every finite-aspect maximum is attained by two distinct interior points, not merely approached by derivatives. In particular, the previously known sharp *uniform* constant \(3\) is never attained by any finite rectangle at this exponent.

## Assumptions and scope
The scalar field is real. The free-space exponent is **exactly** \(p=1/2\). The domain and the vertex metric are the same Manhattan metric; the norm on \(\mathcal F_{1/2}(V)\) is defined by the infimum of molecular costs, with
\[
\left\|\sum_v m_v\delta_v\right\|_{\mathcal F_{1/2}}^{1/2}
=\inf\left\{\sum_j\sqrt{|c_j|d(u_j,v_j)}:\sum_v m_v\delta_v=\sum_jc_j(\delta_{u_j}-\delta_{v_j})\right\}.
\]
All displayed measures have total mass zero, so the base point is immaterial. By a common rescaling and optional interchange of axes, write the problem on \([0,1]^2\) with the weighted Manhattan metric \(d_r((x,y),(x',y'))=|x-x'|+r|y-y'|\), where \(r=\lambda\ge1\). Vertices are ordered \(00,10,01,11\), and
\[
R(x,y)=(1-x)(1-y)\delta_{00}+x(1-y)\delta_{10}+(1-x)y\delta_{01}+xy\delta_{11}.
\]

## Proof
**1. Exact finite-flow formula.** For a zero-mass load \(m\) on four metric vertices,
\[
\|m\|_{\mathcal F_{1/2}}^{1/2}
=\min_{T}\sum_{e\in T}\sqrt{d(e)|f_e(T,m)|},
\]
where \(T\) ranges over all 16 spanning trees of the complete four-vertex graph, and the signed tree flow \(f_e\) is the sum of the loads in either cut component on deleting \(e\). Every molecular decomposition is an edge flow. Combining parallel edges cannot increase the cost because the square-root function is subadditive. Along a nonzero flow cycle, adding circulation leaves divergence unchanged, and the cost is concave on each interval before an edge becomes zero. Passing to an endpoint never raises cost and eliminates an edge. Repeating produces a forest; augment by zero-flow edges to a tree. Conversely every tree gives a molecular representation. Thus the 16-tree minimum is **exact**, with no reliance on numerical sampling.

**2. Midpoint and tangent reduction.** Bilinearity gives the exact secant identity \(R(z)-R(z')=DR((z+z')/2)(z-z')\). Conversely each interior derivative is realized by sufficiently short symmetric secants. Reflections in the two axes induce metric isometries of the target vertex set, so it suffices to use nonnegative directional speeds \(a,b\) with \(a+rb=1\). At midpoint \((x,y)\), let \(q=ay+bx\), so \(0\le q\le a+b\). The tangent load in order \(00,10,01,11\) is
\[
m=(-a-b+q,\ a-q,\ b-q,\ q).
\]
We show \(\|m\|_{\mathcal F_{1/2}}^{1/2}\le F_r\), where \(F_r=(2\sqrt r+\sqrt{r+1})/\sqrt{3r+1}\). The four sign regions below exhaust this interval; boundary overlaps are harmless.

**3. Source-only and target-only regions.** For \(0\le q\le\min\{a,b\}\), two explicit path-tree flows give
\[
U=\sqrt a+\sqrt{r(b-q)}+\sqrt{rq},\quad
V=\sqrt{rb}+\sqrt{a-q}+\sqrt q.
\]
The tree formula and Cauchy–Schwarz imply
\[
\|m\|_{\mathcal F_{1/2}}^{1/2}\le\min\{U,V\}\le \frac{U+V}{2}
\le \frac1{\sqrt2}+\sqrt{\frac{1-(r+1)q}{2}}+\frac{\sqrt r+1}{2}\sqrt q.
\]
Set \(z=(r+1)q\in[0,1]\). Maximizing the last two terms by Cauchy–Schwarz and using \((\sqrt r+1)^2\le2(r+1)\) gives \(\|m\|_{\mathcal F_{1/2}}^{1/2}\le1+1/\sqrt2=F_1\le F_r\). Rotating the rectangle by half a turn reduces the target-only region \(\max\{a,b\}\le q\le a+b\) to this one.

**4. Mixed vertical region.** When \(a\le q\le b\), two path-tree flows give
\[
U=\sqrt a+\sqrt{r(b-q)}+\sqrt{rq},\quad
V=\sqrt a+\sqrt{r(a+b-q)}+\sqrt{r(q-a)}.
\]
Put \(A=a\), \(B=rb=1-A\), \(t=rq\), and \(g_B(u)=\sqrt u+\sqrt{B-u}\). Then \(U=\sqrt A+g_B(t)\) and \(V=\sqrt A+g_B(t-rA)\), with \(t\in[rA,B]\). Since \(g_B\) decreases strictly with distance from \(B/2\), the maximum of \(\min(U,V)\) occurs when the two arguments are symmetrically placed about \(B/2\), namely \(t=(B+rA)/2\). Its value is
\[
H_r(A)=\sqrt A+\frac1{\sqrt2}\left(\sqrt{1+(r-1)A}+\sqrt{1-(r+1)A}\right).
\]
Here \(A\le1/(r+1)\). Differentiating the last two square roots with respect to \(r\), at fixed \(A\), shows \(H_r(A)\le H_1(A)\). Elementary differentiation gives \(\max_{0\le A\le1/2}H_1(A)=H_1(1/4)=1+1/\sqrt2\). Thus the mixed vertical region also has cost at most \(F_r\).

**5. Mixed horizontal region and the sharp concavity certificate.** When \(b\le q\le a\), three explicitly feasible spanning trees supply
\[
\begin{aligned}
F_1(b,q)&=\sqrt{a-q}+\sqrt{rb}+\sqrt q,\\
F_2(b,q)&=\sqrt{a-q}+\sqrt{(r+1)b}+\sqrt{q-b},\\
F_3(b,q)&=\sqrt{a+b-q}+\sqrt{rb}+\sqrt{q-b},\qquad a=1-rb.
\end{aligned}
\]
Each is concave on the convex domain \(b\ge0\), \(b\le q\le1-rb\). Let
\[
\gamma=\frac{r+1}{3r+1},\qquad\eta=\frac{r-1}{3r+1},\qquad G=\gamma F_1+\eta F_2+\gamma F_3.
\]
The weights are nonnegative and sum to one. At
\[
b_* =\frac1{3r+1},\quad a_* =\frac{2r+1}{3r+1},\quad q_* =\frac{r+1}{3r+1},
\]
all three candidate costs equal \(F_r\). Their gradients with respect to \((b,q)\) are respectively \((0,-d)\), \((-(r+1)d,0)\), \(((r-1)d,d)\), with \(d=1/(2\sqrt{r/(3r+1)})-1/(2\sqrt{(r+1)/(3r+1)})\). The weighted gradient of \(G\) vanishes. Since \(G\) is concave, its global maximum is \(F_r\). Hence
\[
\|m\|_{\mathcal F_{1/2}}^{1/2}\le\min\{F_1,F_2,F_3\}\le G(b,q)\le F_r.
\]
Together the four regions prove the global upper bound.

**6. Exact 16-tree lower certificate.** Choose the interior midpoint \((x,y)=(1/2,1/2)\) and the normalized displacement direction \((a_*,b_*)\). Its load is
\[
m_* =\frac1{3r+1}(-r-1,\ r,\ -r,\ r+1).
\]
Computing the edge-length-times-cut-flow triples for **all 16 trees**, multiplied by \(3r+1\), yields precisely these eight multisets and multiplicities:

| Triple \(\{d(e)|f_e|(3r+1)\}\) | Trees |
| --- | ---: |
| \(\{r,r,r+1\}\) | 3 |
| \(\{0,(r+1)^2,r(r+1)\}\) | 4 |
| \(\{(r+1)^2,r,r^2\}\) | 2 |
| \(\{2r+1,r(r+1),r^2\}\) | 2 |
| \(\{r+1,r(r+1),r(r+1)\}\) | 2 |
| \(\{r+1,r+1,r+1\}\) | 1 |
| \(\{(r+1)(2r+1),r^2,r^2\}\) | 1 |
| \(\{(r+1)(2r+1),r(r+1),r(r+1)\}\) | 1 |

The seven nonzero-flow patterns, after sorting, dominate \(\{r,r,r+1\}\) coordinatewise for every \(r\ge1\). The zero-flow pattern instead has radical cost \(r+1+\sqrt{r(r+1)}\), at least \(2\sqrt r+\sqrt{r+1}\): writing \(u=\sqrt r\ge1\), \(v=\sqrt{r+1}\), the difference equals \(v(v+u-1)-2u\ge v^2-2u=(u-1)^2\ge0\). Therefore the exact tree minimum is
\[
\|m_*\|_{\mathcal F_{1/2}}^{1/2}=\frac{2\sqrt r+\sqrt{r+1}}{\sqrt{3r+1}}=F_r.
\]
For any sufficiently small \(\varepsilon>0\), both points \((1/2,1/2)\pm(\varepsilon/2)(a_*,b_*)\) remain interior; the exact bilinear midpoint identity gives a secant with ratio \(F_r^2\). Thus the upper bound is attained and equals \(L(r)=F_r^2\).

**7. Strict aspect dependence.** Direct differentiation yields
\[
F_r' =\frac{1/\sqrt r-1/\sqrt{r+1}}{(3r+1)^{3/2}}>0,\qquad r\ge1.
\]
Hence \(L(r)\) is strictly increasing, \(L(1)=3/2+\sqrt2\), and \(\lim_{r\to\infty}L(r)=3\). Interchanging axes gives the formula for arbitrary positive side lengths.

## Verification
The standalone Python 3 standard-library script `verify_rectangle.py` builds all 16 labeled spanning trees, computes cut flows independently of the analytical expressions, and checks the sharp load and all tree-cost inequalities using **exact fractions** at seven rational aspect ratios. It tests exact interior secants and 3,080 additional randomized and boundary tangent configurations over eleven aspect ratios, for **3,192 total tree-cost comparisons**. Run `python3 verify_rectangle.py`. The code supplies finite reproducibility; the proof above establishes the continuum statement. The mathematical proof of global sharpness is the concavity certificate and exhaustive 16-tree classification, not a numerical optimizer or simulation.

## Relationship to prior work
Albiac–Ansorena–Cúth–Doucha (arXiv:2006.08018v1, first posted 2020-06-14), Theorem 3.5, construct the canonical coordinatewise-affine map and obtain dimension-dependent bounds for cubes. Bíma (arXiv:2303.03265v1, first posted 2023-03-06), Theorem 3.2 and its proof, refine bounds for unions of equal-sided cubes; neither determines exact values for all unequal-sided rectangles. The published *Sharp square-cell constant for Lipschitz-free \(p\)-interpolation* (2026-10-11) gives the exact equal-sided value \((2+2^p)^{1/p}/4\); at \(p=1/2\), this is precisely \(L(1)\). That equal-sided statement neither implies constancy nor determines the new strictly varying finite-aspect profile. The already-known uniform-aspect upper bound and limiting value \(3\) are not claimed as new; the contribution is the **exact finite-aspect parameter law, its sharp interior witnesses, and its strict monotonicity**.

## Limitations
The analysis is for exactly four vertices, real scalars, one bilinear cell, Manhattan distance, and free exponent \(1/2\). It neither gives the full aspect profile for other free exponents nor determines best constants over all possible extensions. Priority outside the inspected primary texts and semantic searches cannot be excluded. The self-review are not independent validation.

## References
1. F. Albiac, J. L. Ansorena, M. Cúth and M. Doucha, *Structure of the Lipschitz free \(p\)-spaces \(\mathcal F_p(\mathbb Z^d)\) and \(\mathcal F_p(\mathbb R^d)\) for \(0<p\le1\)*, arXiv:2006.08018v1, 2020-06-14, Theorem 3.5 and Section 3. https://arxiv.org/html/2006.08018v1
2. J. Bíma, *Lipschitz Free Spaces and Subsets of Finite-Dimensional Spaces*, arXiv:2303.03265v1, 2023-03-06, Theorem 3.2 and Section 3 proof. https://arxiv.org/html/2303.03265v1
3. *The sharp square-cell constant for Lipschitz-free \(p\)-interpolation*, published-finding corpus published result, 2026-10-11, full `RESULT.md`: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-sharp-square-cell-constant-for-lipschitz-free-p-interpolatio--23ae4bb01450
