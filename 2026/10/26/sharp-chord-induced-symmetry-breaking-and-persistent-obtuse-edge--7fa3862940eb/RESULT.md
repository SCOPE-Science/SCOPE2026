# Sharp chord-induced symmetry breaking and persistent obtuse-edge sinks on even Kuramoto rings

## Finding
Fix an integer \(m\ge4\). Give all edges of the \(2m\)-vertex cycle unit weight and add a single chord joining its antipodal vertices with weight \(\kappa>0\). All natural oscillator frequencies are equal. Put \(\delta=\pi/m\) and \(\kappa_c=2\cos(\delta)/m\). Each of the two unit-winding, equally spaced twisted equilibria is linearly asymptotically stable modulo common phase shifts for \(0<\kappa<\kappa_c\), has exactly one additional neutral direction at \(\kappa=\kappa_c\), and has exactly one unstable direction for \(\kappa>\kappa_c\).

For **every** \(\kappa>\kappa_c\), there is exactly one \(x\in(0,\delta)\) satisfying
\[
\kappa=\frac{2\cos\delta\,\sin x}{\sin(mx)}.
\]
It gives **four pairwise distinct, linearly asymptotically stable phase-locked equilibria** modulo global rotation. For each \(\varepsilon,\sigma\in\{-1,+1\}\), they are
\[
\theta_j^{\varepsilon,\sigma}=\varepsilon\begin{cases}
 j(\delta+\sigma x),&0\le j\le m,\\
 m(\delta+\sigma x)+(j-m)(\delta-\sigma x),&m<j<2m.
\end{cases}\pmod{2\pi}.
\]
Consequently, with the stable synchronous equilibrium, at least five distinct linearly stable phase classes coexist whenever \(\kappa>\kappa_c\).

The new equilibria have an **obtuse phase gap on the added chord** precisely for
\[
\kappa_c<\kappa<\kappa_o:=2\cos(\pi/m)\sin(\pi/(2m)),
\]
with a right-angle chord at \(\kappa_o\), and an acute chord for \(\kappa>\kappa_o\). The ratio \(\kappa_o/\kappa_c=m\sin(\pi/(2m))\) tends to \(\pi/2\). Near onset, the branch amplitude obeys the sharp square-root law
\[
x=\sqrt{\frac{6}{m^2-1}\left(\frac{\kappa}{\kappa_c}-1\right)}+O\!\left(\left(\frac{\kappa}{\kappa_c}-1\right)^{3/2}\right).
\]
All statements include arbitrary positive chord weights and every integer \(m\ge4\); no global classification of other possible equilibria is asserted.

## Assumptions and scope
Vertices are \(j\in\mathbb Z/(2m\mathbb Z)\). For phases \(\theta_j\in\mathbb R/(2\pi\mathbb Z)\), take the attractive identical-frequency Kuramoto gradient flow (in a common rotating frame)
\[
\dot\theta_j=\sum_{k:\{j,k\}\in E}w_{jk}\sin(\theta_k-\theta_j),
\]
with \(w_{j,j+1}=1\), \(w_{0,m}=\kappa>0\), and no other edges. Stability is strict transverse linear stability: the Jacobian has exactly one zero eigenvalue from global rotation and all other eigenvalues negative. An unstable direction refers to a positive eigenvalue. At the critical point the additional zero direction makes the state nonhyperbolic; nonlinear behavior exactly at equality is not claimed.

## Proof
**The twisted branch and its sharp threshold.** For each orientation \(\varepsilon=\pm1\), the equally spaced twist \(\theta_j=\varepsilon j\delta\) is an equilibrium: the opposing unit-cycle forces cancel at each vertex and the chord endpoints differ by \(\pi\). The negative Jacobian is the weighted graph Laplacian, with cycle conductances \(c=\cos\delta>0\) and chord conductance \(-\kappa\). For a real variation \(v\), write \(d=v_m-v_0\). The two length-\(m\) paths have minimal total cycle energy \(2c d^2/m\), with equality when the increment is constant along each path. Therefore the Hessian form has minimum \((2c/m-\kappa)d^2\) at fixed \(d\). Variations with \(d=0\) have strictly positive cycle energy unless constant. The form is positive on the phase quotient precisely when \(\kappa<\kappa_c\); at equality it has exactly one additional zero mode; for larger \(\kappa\), the negative chord term is a rank-one perturbation of a positive quotient Laplacian, giving exactly one negative Hessian direction and hence one unstable flow direction.

**Existence, uniqueness and onset of the broken-symmetry branches.** Let \(a=\delta+x\) and \(b=\delta-x\). Give the first length-\(m\) arm constant phase increment \(a\) and the second constant increment \(b\). The total cycle winding is \(m(a+b)=2\pi\). Every interior vertex has zero net force. At vertex zero, the remaining scalar equilibrium equation is
\[
0=\sin a-\sin b-\kappa\sin(mx)=2\cos\delta\sin x-\kappa\sin(mx),
\]
with the endpoint \(m\) equation the negative. For \(0<x<\delta\), the function \(x\mapsto2\cos\delta\sin x/\sin(mx)\) tends to \(\kappa_c\) at zero and diverges as \(x\uparrow\delta\). Its logarithmic derivative is \(\cot x-m\cot(mx)>0\), because \(t\mapsto t\cot t\) is strictly decreasing on \((0,\pi)\): its derivative is \((\sin t\cos t-t)/\sin^2t<0\). Thus each \(\kappa>\kappa_c\) has exactly one such \(x\). Reversing the winding sign and exchanging the two arms yields the four displayed equilibria; their cycle-increment sign and ordered values distinguish them modulo rotation. Taylor expansion
\[
\frac{\kappa(x)}{\kappa_c}=\frac{m\sin x}{\sin(mx)}=1+\frac{m^2-1}{6}x^2+O(x^4)
\]
proves the amplitude law.

**Strict linear stability of every new branch.** The ring conductances on the two arms are \(c_+=\cos(\delta+x)\) and \(c_-=\cos(\delta-x)\). Both are strictly positive for \(m\ge4\) and \(0<x<\delta\) (including the limit \(\delta+x<\pi/2\)). The chord phase difference is \(\pi+mx\) up to orientation and arm exchange, so its conductance is \(-\kappa\cos(mx)\). The same fixed-endpoint energy minimization gives
\[
Q(v)\ge\left[\frac{c_++c_-}{m}-\kappa\cos(mx)\right](v_m-v_0)^2
\]
with additional positive energy for nonharmonic interior variations. When \(\cos(mx)\le0\), strict stability is immediate. When \(\cos(mx)>0\), use \(c_++c_-=2\cos\delta\cos x\) and the equilibrium equation to obtain
\[
\frac{c_++c_-}{m}-\kappa\cos(mx)
=\frac{2\cos\delta\sin x}{m}\bigl(\cot x-m\cot(mx)\bigr)>0.
\]
Hence every nonconstant variation has \(Q(v)>0\), proving exactly one rotational zero direction and all other Jacobian eigenvalues strictly negative.

**The obtuse-to-acute chord transition.** The principal chord gap of each branch is \(\pi-mx\in(0,\pi)\). It is obtuse exactly for \(x<\pi/(2m)\). Strict monotonicity of \(\kappa(x)\) maps this condition onto \((\kappa_c,\kappa_o)\); substitution gives \(\kappa_o=2\cos\delta\sin(\pi/(2m))\). The elementary sine limit yields \(\kappa_o/\kappa_c\to\pi/2\). The synchronous state has positive edge conductances for all positive weights, so it supplies the fifth stable phase class.

## Verification
Run `python3 verify.py` with Python 3.9 or later. The script uses only the standard library and builds the full \(2m\)-node vector field and Hessian from the edge list, testing eight graph sizes and 232 cases. It verifies the explicit equilibria's residuals, Hessian positivity on the phase quotient, the twisted states' instability test vector, monotone inverse parameters and the obtuse-chord boundary. Output begins `VERIFY_OK`. The finite floating-point tests corroborate but do not replace the all-parameter argument above.

## Relationship to prior work
Bronski, DeVille and Ferguson (arXiv:1508.01507v1, 2015) give graph-homology and signed-Laplacian index tests for oscillator equilibria on graphs with one or two cycles. Their general inertia method applies to these configurations after they are known; it does not by itself provide the explicit nonlinear symmetry-broken branch, its unique all-coupling amplitude, or its obtuse-to-acute transition. Delabays, Coletta and Jacquod (arXiv:1512.04266v1, 2015) develop winding and multistability analysis on a *single* cycle. Delabays, Coletta and Jacquod (arXiv:1609.02359v1, 2016) study winding and stability on *planar multi-loop* graphs and include two loops sharing an edge. In the inspected relevant sections, their general all-acute uniqueness bounds and example flow configurations do not give the present symmetric equal-arm, single-chord exact bifurcation family. The signed effective-conductance proof is a specialization of established network stability machinery; the claimed additional contribution is the complete explicit branch persistence, onset, and chord-angle interval for this natural parameterized family, not the general graph method.

## Limitations
The theorem constructs and distinguishes four stable broken-symmetry branches, plus synchrony, but does **not** count all equilibria, establish that five is the total number of stable phase classes, classify basins, or determine nonlinear dynamics at the nonhyperbolic threshold. It requires identical natural frequencies, positive unit ring weights, one antipodal chord, and an even cycle of length at least eight. Finite-precision checks cannot certify the infinitely many parameter values. Historical priority may be affected by an unlocated exact specialization of older graph-cycle or Kuramoto bifurcation results; scientific novelty is based on the inspected literature and indexed comparisons, not a theorem of exhaustive uniqueness of presentation. Independent external validation has not been performed.

## References
1. J. C. Bronski, L. DeVille, T. Ferguson, *Graph Homology and Stability of Coupled Oscillator Networks*, arXiv:1508.01507v1, submitted 2015-08-06. https://arxiv.org/abs/1508.01507
2. R. Delabays, M. Coletta, P. Jacquod, *Multistability of Phase-Locking and Topological Winding Numbers in Locally Coupled Kuramoto Models on Single-Loop Networks*, arXiv:1512.04266v1, submitted 2015-12-14. https://arxiv.org/abs/1512.04266
3. R. Delabays, M. Coletta, P. Jacquod, *Multistability of Phase-Locking in Equal-Frequency Kuramoto Models on Planar Graphs*, arXiv:1609.02359v1, submitted 2016-09-08. https://arxiv.org/abs/1609.02359
