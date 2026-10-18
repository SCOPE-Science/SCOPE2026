# Exact polynomial-scale volumes of two-row rook-graph Lipschitz dual balls

## Finding
For every integer \(n\ge2\), let \(R_n=K_n\square K_2\) carry the unit-edge shortest-path metric. Label its two complete layers \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), with matching edges \(a_i b_i\). Anchor a real Lipschitz potential by \(a_1=0\). Its dual unit ball is the full-dimensional polytope
\[
Q_n=\{(a_2,\ldots,a_n,b_1,\ldots,b_n)\in\mathbb R^{2n-1}:\ |a_i-a_j|\le1,\ |b_i-b_j|\le1,\ |a_i-b_i|\le1\quad\text{for all admissible indices}\}.
\]
All volumes in this note are ordinary Lebesgue volumes in the displayed anchored coordinate chart, not intrinsic Euclidean volumes in the zero-sum hyperplane. Put
\[
J_m=\int_0^1\left(1-\frac{s^2}{2}\right)^m\,ds
=\sum_{j=0}^m\frac{(-1)^j\binom mj}{2^j(2j+1)}\qquad(m\in\mathbb Z_{\ge0}).
\]
Then the exact volume \(V_n=\operatorname{vol}_{2n-1}(Q_n)\) is
\[
\boxed{V_n=2n\left[(n-1)J_{n-2}+J_{n-1}-1+2^{-(n-1)}\right].}
\]
In particular, \(V_2=16/3\), \(V_3=49/5\), \(V_4=534/35\), and \(V_5=5443/252\). The infinite family has the sharp asymptotic
\[
\boxed{V_n=\sqrt{2\pi}\,n^{3/2}-2n+O(\sqrt n)}\qquad(n\to\infty).
\]
Thus the anchored volumes grow polynomially despite the ambient dimensions increasing linearly.

## Assumptions and scope
The graph has exactly two \(n\)-vertex cliques and one perfect matching joining corresponding vertices. Every graph edge has length one; nonedges between layers have graph distance two. The within-layer and matching Lipschitz inequalities imply every nonedge inequality by the triangle inequality, so they define the full dual unit ball. The anchor determines a lattice coordinate chart: changing the anchor acts unimodularly and does not change \(V_n\). The domain is every integer \(n\ge2\); no assumptions on a limiting proportion or on unproved enumerations are needed.

## Proof
**1. Decompose both clique balls into unit cubes.** For a potential \((a_i)\) whose range is at most one, its minimizing index \(r\) is unique except on a null set. Writing \(a_i=\alpha+u_i\), with \(u_r=0\) and the other \(u_i\in[0,1]\), gives a unit \((n-1)\)-cube. Likewise, \(b_i=\beta+v_i\), where \(v_s=0\) and the other \(v_i\in[0,1]\). When \(a_1=0\), replacing the free anchored coordinates by the \(2n-2\) nonminimum coordinates and \(\delta=\beta-\alpha\) is an affine integral coordinate transformation of determinant \(\pm1\): it is obtained by subtracting the selected minimum within each layer and retaining the difference of their layer offsets. Hence these products of cubes carry standard Lebesgue measure without an extra factor.

**2. Integrate the interlayer translation.** For fixed \(u,v\), the matching inequalities become \(|\delta-(u_i-v_i)|\le1\) for \(1\le i\le n\). The allowable interval of \(\delta\) therefore has length
\[
2-\left(\max_i(u_i-v_i)-\min_i(u_i-v_i)\right).
\]
This number is nonnegative because every difference lies in \([-1,1]\). Denote the bracketed range by \(\mathcal R\). Integrating across all choices of minimizing indices yields
\[
V_n=\sum_{r,s=1}^n\mathbb E_{r,s}[2-\mathcal R],
\]
where the expectation uses independent uniforms on the remaining cube coordinates.

**3. Calculate the two range expectations.** The difference \(T=U-V\) of two independent \(\operatorname{Uniform}[0,1]\) variables has, for \(0\le t\le1\), distribution function
\[
F_T(t)=1-\frac{(1-t)^2}{2}.
\]
If \(r=s\), one coordinate \(u_r-v_r\) is zero and the other \(n-1\) are independent copies of \(T\). Symmetry gives \(\mathbb E\mathcal R=2\mathbb E\max_i(u_i-v_i)\). The maximum is nonnegative and its tail integral gives
\[
\mathbb E_{r,r}\mathcal R
=2\int_0^1\bigl[1-F_T(t)^{n-1}\bigr]\,dt
=2(1-J_{n-1}).
\]
If \(r\ne s\), the differences at \(r,s\) are respectively \(-U\) and \(+U'\), where \(U,U'\) are independent uniforms, and the remaining \(n-2\) differences are independent copies of \(T\). Swapping the two special coordinates and negating all differences preserves the range distribution, so again \(\mathbb E\mathcal R=2\mathbb E\max\). For \(0\le t\le1\), the maximum has distribution function \(tF_T(t)^{n-2}\). Consequently
\[
\begin{aligned}
\mathbb E_{r,s}\mathcal R
&=2\int_0^1\bigl[1-tF_T(t)^{n-2}\bigr]\,dt\\
&=2\left[1-J_{n-2}+\int_0^1w\left(1-\frac{w^2}{2}\right)^{n-2}\,dw\right]\\
&=2\left[1-J_{n-2}+\frac{1-2^{-(n-1)}}{n-1}\right].
\end{aligned}
\]
There are exactly \(n\) choices with \(r=s\) and \(n(n-1)\) with \(r\ne s\). Substitution into Step 2 and direct simplification prove the boxed exact formula. Expanding the integrand by the binomial theorem gives the finite rational formula for every \(J_m\).

**4. Asymptotic evaluation.** The standard Gaussian Laplace estimate, justified by splitting the integral at \(m^{-3/8}\) and using the uniform Taylor expansion of \(m\log(1-s^2/2)\) below that cutoff, yields
\[
J_m=\sqrt{\frac\pi{2m}}+O(m^{-3/2})\qquad(m\to\infty).
\]
Indeed, above the cutoff the integrand is bounded by \(\exp(-ms^2/2)\), whose tail is smaller than any negative power of \(m\), and below the cutoff it differs from \(\exp(-ms^2/2)\) by an integrable error \(O(ms^4\exp(-ms^2/2))\), of order \(m^{-3/2}\). Substituting this estimate for \(J_{n-2}\) and \(J_{n-1}\) into the exact expression gives \(\sqrt{2\pi}\,n^{3/2}-2n+O(\sqrt n)\), as asserted.

## Verification
The accompanying standalone `checker.py` uses integer lattice counts in the scaled anchored polytope, independently of the continuous minimum-cube integration. The edge-difference inequality matrix is totally unimodular, so the lattice-point enumerator of \(Q_n\) is an Ehrhart polynomial of degree \(2n-1\). Its leading coefficient is \(V_n\). For each \(n\in\{2,3,4,5\}\), the program counts the lattice points in every dilation from zero through dimension \(2n-1\), computes the leading coefficient by exact finite differences, and matches the analytic formula using rational arithmetic. All four comparisons passed. These finitely many tests are checks, not a proof of the all-dimensional formula.

## Relationship to prior work
Finite Lipschitz-free spaces and their dual norm balls are standard objects in Banach-space geometry; see Dilworth–Kutzarova–Ostrovskii and Aliaga. Alexander–Fradelizi–García-Lirola–Zvavitch study the general volume product and determine the equilateral reference case. D'Alì–Delucchi–Michałek investigate symmetric edge polytopes and their **primal** normalized volumes, whereas this note measures the anchored **polar** volume of the specific two-row rook family. A previously obtained facet enumeration for the same family counts boundary faces and does not supply these Lebesgue volumes. The present result is not asserted to follow from those results; nor does the absence of a detected exact predecessor establish absolute novelty.

## Limitations
The volume normalization is fixed to anchored vertex-potential coordinates, not the intrinsic orthonormal zero-sum metric. The result does not evaluate the primal volume or the Mahler product, nor does it treat more than two layers or nonunit edge weights. Exact verification covers only four finite dimensions; the proof covers all \(n\ge2\). A differently titled or unindexed equivalent volume calculation may exist; a separate independent scientific assessment has not been conducted.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz-free spaces on finite metric spaces*, arXiv:1807.03814 (first submitted 2018-07-10).
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019).
3. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first submitted 2019-11-24).
4. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first submitted 2021-02-01; primary MSC 46B20).
