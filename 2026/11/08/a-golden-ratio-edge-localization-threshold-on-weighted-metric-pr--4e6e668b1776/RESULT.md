# A golden-ratio edge-localization threshold on weighted metric prisms

## Finding

For every integer \(n\geq 3\) and every real \(h>0\), let \(G_{n,h}\) be the compact metric realization of the prism graph \(C_n\square K_2\): each of its \(2n\) rail (cycle) edges has length \(1\), and each of its \(n\) rungs has length \(h\). All integrals are with respect to **unnormalized arclength**, and \(L=n(h+2)\) is the total length. On real, continuous, edgewise-\(H^1\) functions of zero arclength mean, let
\[
\mathcal K_{n,h}=\sup_{\substack{f\not\equiv 0\\ \int_{G_{n,h}} f\,ds=0}}
 \frac{\|f\|_\infty^2}{\int_{G_{n,h}}|f'|^2\,ds}.
\]
Put
\[
H_n(h)=\frac1n\sum_{k=0}^{n-1}
\frac{1}{1+h(1-\cos(2\pi k/n))},
\quad
A_n(h)=\frac{n^2-1}{24n}+\frac h4H_n(h)+\frac{2+h^3}{12n(h+2)^2},
\]
\[
B_{\mathrm{rail}}=\frac{H_n(h)}2+\frac{h}{2n(h+2)},
\qquad
B_{\mathrm{rung}}=h(1-H_n(h))-\frac{h^2}{n(h+2)}.
\]
Both \(B\)-values are strictly positive. The **exact sharp squared embedding constant** is
\[
\boxed{\mathcal K_{n,h}=A_n(h)+\tfrac14\max\{B_{\mathrm{rail}},B_{\mathrm{rung}}\}.}
\]
There is exactly one threshold \(h_n>0\) solving
\[
\boxed{\Delta_n(h):=h-\left(h+\frac12\right)H_n(h)
 -\frac{h(2h+1)}{2n(h+2)}=0.}
\]
For \(0<h<h_n\), precisely the \(2n\) rail-edge **midpoints** maximize the evaluation norm. At \(h=h_n\), all \(3n\) edge midpoints, and no other points, maximize it. For \(h>h_n\), precisely the \(n\) rung **midpoints** maximize it. In particular,
\[
 h_3>1,\qquad h_4=1,\qquad 0<h_n<1\ (n\ge5).
\]
The thresholds are strictly decreasing and satisfy the **golden-ratio limit and first correction**
\[
\boxed{\ h_n=\frac{1+\sqrt5}{4}
 +\frac{25+12\sqrt5}{95n}+O(n^{-2})\quad(n\to\infty).\ }
\]
At equal edge lengths \(h=1\), the triangular prism has exactly six rail-midpoint maximizers; the cube has all twelve edge midpoints maximizing; and every larger prism has only its \(n\) rung midpoints maximizing, with the rational sharp squared constant
\[
\boxed{\mathcal K_{n,1}=\frac n{24}+\frac14-\frac{7}{72n}\qquad(n\ge5).}
\]
For any edge \(e\), let its type be rail or rung. At the point with fractional coordinate \(t\in[0,1]\) along \(e\), the exact squared evaluation norm is \(A_n(h)+B_e t(1-t)\). Thus the **exact deficit identity** is
\[
\mathcal K_{n,h}-\|\delta_{e,t}\|^2
= B_e(t-\tfrac12)^2+\frac{\max\{B_{\mathrm{rail}},B_{\mathrm{rung}}\}-B_e}{4}.
\]
Every nonzero equality function is a nonzero real multiple of the mean-zero Kirchhoff Green representer for one of the classified maximizing points.

## Assumptions and scope

The graph is connected; \(n\) is an integer at least three; \(h\) is any strictly positive real; every rail has length one and every rung has the common length \(h\). Standard continuity and Kirchhoff matching are used, with no boundary vertices. The function space consists of real continuous edgewise-\(H^1\) functions satisfying the zero **unnormalized arclength** integral. The energy is \(\int|f'|^2\), not its length-normalized version. All operator norms in the statement are squared norms of real point evaluations, and all asymptotic assertions concern integer \(n\to\infty\) with the threshold varying accordingly.

## Proof

**1. The centered evaluation representer and an edgewise diagonal formula.** On any connected compact metric graph of total length \(L\), the energy inner product on zero-mean real \(H^1\) functions is a Hilbert norm. For a point \(x\) there is a unique zero-mean continuous Kirchhoff Green function \(g_x\) satisfying \(-g_x''=\delta_x-L^{-1}ds\) distributionally. Integration by parts yields \(f(x)=\int f'g_x'\,ds\) for every zero-mean \(f\). Consequently \(\|\delta_x\|^2=g_x(x)=\int|g_x'|^2ds\). Equality for any nonzero \(f\) occurs exactly when \(f\) is a scalar multiple of \(g_x\).

Let a finite edge \(e=uv\) have length \(\ell\), and write \(x\) for the point at distance \(t\ell\) from \(u\), \(0\le t\le1\). Put \(p=(1-t)\mathbf e_u+t\mathbf e_v\). On every edge, the Green solution is the linear interpolation of its vertex values, minus \(s(\ell-s)/(2L)\); on the distinguished edge add the elementary Dirichlet point Green function \(\min(s,t\ell)(\ell-\max(s,t\ell))/\ell\). The vertex Kirchhoff equations are therefore
\[
Qb=p-\frac{d_\ell}{2L},
\]
where \(Q\) is the weighted vertex Laplacian with conductance \(1/\ell\) on each edge and \(d_\ell(v)\) is the sum of lengths of edges incident to \(v\). In the present prism, \(d_\ell(v)=h+2\) and the graph has \(2n\) vertices. Hence \(d_\ell/(2L)=\mathbf1/(2n)\), and a solution is \(b=Q^+p+c\mathbf1\), where \(Q^+\) denotes the Moore--Penrose inverse. Since every vertex lies in one automorphism orbit, \((Q^+)_{uu}=D\) is independent of \(u\). Integrating the edgewise expression to enforce zero mean gives
\[
 c=\frac{\sum_e\ell_e^3}{12L^2}-\frac{\ell^2}{2L}t(1-t).
\]
The elementary resistance identity \(R_{uv}=(Q^+)_{uu}+(Q^+)_{vv}-2(Q^+)_{uv}\), combined with the value of the local Dirichlet Green function at its pole, now yields the **exact** continuum diagonal
\[
\boxed{\|\delta_{e,t}\|^2=D+\frac{\sum_e\ell_e^3}{12L^2}
+t(1-t)\left(\ell-R_{uv}-\frac{\ell^2}{L}\right).}
\tag{1}
\]
This derivation remains valid for vertex evaluations by setting \(t=0\) or \(1\).

**2. Weighted spectral decomposition and exact edge coefficients.** Label the two \(n\)-cycles by layers. Set \(a_k=1-\cos(2\pi k/n)\in[0,2]\). Decomposing into layer-symmetric and layer-antisymmetric Fourier modes gives vertex-Laplacian eigenvalues \(2a_k\) and \(2a_k+2/h\), respectively, with only the symmetric zero mode omitted from \(Q^+\). The identity \(\sum_{k=1}^{n-1}(2a_k)^{-1}=(n^2-1)/12\) then shows
\[
 D=\frac{n^2-1}{24n}+\frac h4 H_n(h).
\]
The two edge-endpoint effective resistances, by the same mode decomposition, are
\[
 R_{\mathrm{rung}}=hH_n(h),\qquad
 R_{\mathrm{rail}}=1-\frac{1}{2n}-\frac{H_n(h)}2.
\]
Since \(\sum_e\ell_e^3=n(2+h^3)\), substitution in (1) proves the displayed expressions for \(A_n\), \(B_{\mathrm{rung}}\), and \(B_{\mathrm{rail}}\).

Clearly \(B_{\mathrm{rail}}>0\). For rungs, rewrite
\[
 B_{\mathrm{rung}}=\frac{h^2}{n}\left(
 \sum_{k=1}^{n-1}\frac{a_k}{1+ha_k}-\frac{1}{h+2}\right).
\]
At least one nonzero \(a_k\) is at least one; hence the sum exceeds \(1/(h+1)>1/(h+2)\). So \(B_{\mathrm{rung}}>0\) as well. Consequently the unique maximum on each edge is its midpoint, and the global maxima are decided solely by the two coefficients. Their difference is exactly \(\Delta_n(h)\).

**3. Strict uniqueness of the crossover.** Write \(H=H_n(h)\) and differentiate. Since \(H'=-n^{-1}\sum_{k>0}a_k/(1+ha_k)^2\),
\[
 n\Delta_n'(h)=
\sum_{k=1}^{n-1}\frac{a_k(2h+\tfrac12+h^2a_k)}{(1+ha_k)^2}
-\frac{h^2+4h+1}{(h+2)^2}.
\tag{2}
\]
For fixed \(h>0\), the summand \(F_h(a)=a(2h+\tfrac12+h^2a)/(1+ha)^2\) is strictly increasing for \(0\le a\le2\):
\[
 F_h'(a)=\frac{2h+\tfrac12-\tfrac12 ha}{(1+ha)^3}>0.
\]
At least two of the cycle eigenmode values \(a_k\) are at least one. Therefore the sum in (2) is at least \(2F_h(1)=2-1/(1+h)^2\ge1\), whereas the subtracted fraction equals \(1-3/(h+2)^2<1\). Thus \(\Delta_n'(h)>0\) for all \(h>0\). As \(h\downarrow0\), \(H_n(h)\to1\) and \(\Delta_n(h)\to-1/2\). As \(h\to\infty\), \(H_n(h)\to1/n\) and \(\Delta_n(h)=h(1-2/n)+O(1)\to+\infty\). There is exactly one positive root \(h_n\), and the complete extremizer trichotomy follows.

**4. Rank hierarchy, the cube, and the golden-ratio limit.** Set
\[
 q(h)=\frac{h}{1+h+\sqrt{2h+1}}\in(0,1).
\]
The elementary Fourier series of \((1+h-h\cos\theta)^{-1}\), summed over the \(n\)-th roots of unity, gives
\[
 H_n(h)=\frac1{\sqrt{2h+1}}\frac{1+q(h)^n}{1-q(h)^n}.
\tag{3}
\]
For fixed \(h>0\), this strictly decreases with \(n\). The positive term \(h(2h+1)/(2n(h+2))\) also strictly decreases with \(n\). Therefore \(\Delta_{n+1}(h)>\Delta_n(h)\), forcing \(h_{n+1}<h_n\). Directly, \(H_3(1)=3/5\) and \(H_4(1)=7/12\), so \(\Delta_3(1)=-1/15\) and \(\Delta_4(1)=0\); monotonicity in \(n\) proves the stated regimes at \(h=1\).

As \(n\to\infty\), (3) converges locally uniformly, with derivatives, to \(H_\infty(h)=1/\sqrt{2h+1}\). Thus
\[
\Delta_\infty(h)=h-\frac{h+1/2}{\sqrt{2h+1}}=h-\frac{\sqrt{2h+1}}2,
\]
whose unique positive root is \(s=(1+\sqrt5)/4\). Because \(\Delta_n(h)<\Delta_\infty(h)\), each \(h_n>s\). Taylor expansion at \(s\), using the exponentially small remainder from (3), gives
\[
 h_n-s=\frac{s(2s+1)}{2(s+2)\Delta_\infty'(s)}\frac1n+O(n^{-2})
 =\frac{25+12\sqrt5}{95n}+O(n^{-2}).
\]
For a rung midpoint, the \(H_n\) terms cancel from the sharp evaluation norm:
\[
 A_n(h)+\frac14B_{\mathrm{rung}}
=\frac{n^2-1}{24n}+\frac h4
 +\frac{2+h^3}{12n(h+2)^2}-\frac{h^2}{4n(h+2)}.
\]
Setting \(h=1\) proves the rational formula for \(n\ge5\). Equation (1) proves the quantitative deficit identity. Equality functions follow from the Riesz equality criterion in Step 1.

## Verification

The included separately formulated checker `prism_poisson_checks.py` refines each tested edge at the evaluation point, solves the continuous Kirchhoff Poisson equation exactly over rational data using the refined weighted vertex Laplacian, integrates the edgewise quadratic to impose zero arclength mean, and compares its diagonal evaluation against the closed spectral formula. It checks \(n\in\{3,4,5,6\}\), \(h\in\{1/3,1,5/2\}\), and five evaluation locations (a vertex, both types of midpoint, and two non-midpoint edge locations): 60 exact symbolic/rational cases. Running `python prism_poisson_checks.py` produced `EXACT_REFINED_KIRCHHOFF_POISSON_CHECKS_PASSED 60`. The proof above supplies the all-parameter conclusion; finite checking is not an infinite proof.

For reference, at \(h=1\), the rail and rung midpoint squared evaluation norms are \(97/270\) versus \(37/108\) at \(n=3\), both \(113/288\) at \(n=4\), and \(737/1710\) versus \(79/180\) at \(n=5\). Numerical roots of the exact monotone threshold equation are approximately \(h_3=1.160847734\), \(h_4=1\), and \(h_5=0.944522494\); these numbers illustrate rather than certify the theorem.

## Relationship to prior work

Baker and Faber (2004) develop the metric-graph Laplacian, energy, electrical-resistance, and Green-function framework. Cinkir (2015) computes resistances of open, equilateral ladder graphs, while Cinkir (2017) computes resistances and Kirchhoff indices for **equilateral** prism graphs and gives their Fourier spectral decomposition. These pre-existing ingredients are not claimed as new. Usman (2018) establishes broader Sobolev-type inequalities for compact metric graphs, not the present exact mean-zero point-evaluation constants. The claimed contribution is the **all-positive-rung-length** sharp continuous embedding constant, complete mid-edge extremizer classification, globally unique and strictly rank-monotone crossover, its golden-ratio large-circumference limit and first correction, and the exact deficit identity. The previously studied open ladder and unit-wheel graph families do not imply the variable-rung prism threshold. General Green/resistance identities are tools rather than novelty claims.

## Limitations

The result is for real first-order Sobolev energy on metric prisms with equal unit rail lengths, uniform positive rung length, uniform arclength background, and the exact zero-arclength-mean constraint. It does not cover alternating rungs, variable rail lengths, nonuniform density, point-mass means, other vertex boundary conditions, higher derivatives, or arbitrary prism decorations. The literature comparison establishes originality only to the extent of the inspected and searchable sources; independent bibliographic or mathematical audit has not been carried out.

## References

1. Matthew Baker and Xander Faber, *Metrized graphs, electrical networks, and Fourier analysis*, first arXiv submission July 25, 2004, https://arxiv.org/abs/math/0407428 .
2. Zubeyir Cinkir, *Effective Resistances, Kirchhoff index and Admissible Invariants of Ladder Graphs*, first arXiv submission March 21, 2015, https://arxiv.org/abs/1503.06353 .
3. Zubeyir Cinkir, *Effective Resistances and Kirchhoff index of Prism Graphs*, first arXiv submission April 11, 2017, https://arxiv.org/abs/1704.03429 .
4. Muhammad Usman, *Sobolev type inequalities for compact metric graphs*, *Journal of Inequalities and Applications* **2018**, article 271, published October 5, 2018, https://doi.org/10.1186/s13660-018-1872-y .
