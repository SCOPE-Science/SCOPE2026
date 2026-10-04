# Sharp two-band high-energy scaling for the phase-rotated square quantum graph
## Finding
For the periodic square quantum graph introduced by Exner and Tater with common edge length \(\ell>0\) and the circulant vertex matrix \(U=e^{i\mu}R\), fix \(0<\mu<\pi/2\) and set
\[
N_n=\frac{n\pi}{\ell}.
\]
There are, for all sufficiently large \(n\), exactly two Bloch bands in an \(O(N_n^{-1})\) momentum neighborhood of \(N_n\). If their ordered energy edges are \(E_{n,1}<E_{n,2}<E_{n,3}<E_{n,4}\), then
\[
\begin{aligned}
E_{n,1}-N_n^2&=-\frac{4}{\ell}(\sec\mu+\tan\mu)+O(n^{-2}),\\
E_{n,2}-N_n^2&=-\frac{4}{\ell}\tan\frac{\mu}{2}+O(n^{-2}),\\
E_{n,3}-N_n^2&=\frac{4}{\ell}(\sec\mu-\tan\mu)+O(n^{-2}),\\
E_{n,4}-N_n^2&=\frac{4}{\ell}\cot\frac{\mu}{2}+O(n^{-2}).
\end{aligned}
\]
Hence the translated local spectrum converges in Hausdorff distance to
\[
I_-(\mu,\ell)\cup I_+(\mu,\ell),
\]
where
\[
I_-(\mu,\ell)=\left[-\frac{4}{\ell}(\sec\mu+\tan\mu),-\frac{4}{\ell}\tan\frac{\mu}{2}\right]
\]
and
\[
I_+(\mu,\ell)=\left[\frac{4}{\ell}(\sec\mu-\tan\mu),\frac{4}{\ell}\cot\frac{\mu}{2}\right].
\]
The limiting set is parity independent. Parity only changes which extremal value of the Bloch parameter \(Q=\cos\theta_1+\cos\theta_2\) realizes a given edge.

## Assumptions and scope
The graph is the equilateral periodic square lattice of arXiv:2108.04708v1, with the source's normalization in which the vertex length scale is one. The parameter is fixed with \(0<\mu<\pi/2\); the endpoint regimes \(\mu=0\) and \(\mu=\pi/2\) are excluded because the high-energy scaling is nonuniform there. The claim concerns only the positive spectrum in the shrinking momentum neighborhood \(k=N_n+O(N_n^{-1})\), equivalently a fixed energy neighborhood of \(N_n^2\). It does not classify remote bands, negative spectrum, or exceptional finite-energy flat bands.

A precise local formulation is the following. Put \(x=N_n(k-N_n)\). For any fixed \(C\) strictly larger than
\[
\frac{2}{\ell}\max\left\{\sec\mu+\tan\mu,\cot\frac{\mu}{2}}\right\},
\]
the spectral set with \(|x|\le C\) consists, for all sufficiently large \(n\), of two closed intervals, and their four endpoints converge to the four \(x\)-values obtained by halving the displayed energy shifts.

## Proof
The source gives the exact Bloch secular condition in the form
\[
\sum_{j=0}^4 c_j k^j=0,
\]
with
\[
c_0=c_4=-\sin(2\mu)\sin^2(k\ell),
\]
\[
c_2=\sin(2\mu)\bigl(1+3\cos(2k\ell)\bigr),
\]
and
\[
\begin{aligned}
c_1&=2\bigl(2\cos(2\mu)\cos(k\ell)-Q\bigr)\sin(k\ell),\\
c_3&=2\bigl(2\cos(2\mu)\cos(k\ell)+Q\bigr)\sin(k\ell),
\end{aligned}
\]
where \(Q=\cos\theta_1+\cos\theta_2\in[-2,2]\). For \(\sin(k\ell)\ne0\), solving this equation for \(Q\) gives
\[
Q(k)=\frac{s\sin^2(k\ell)(1+k^4)-s(1+3\cos(2k\ell))k^2-4c\sin(k\ell)\cos(k\ell)(k+k^3)}{2\sin(k\ell)k(k^2-1)},
\]
where \(s=\sin(2\mu)\) and \(c=\cos(2\mu)\). A momentum \(k\) is in the Bloch spectrum exactly when \(|Q(k)|\le2\), apart from the source's separately treated exceptional points. At \(k=N_n\), the secular expression equals \(4sN_n^2\ne0\), so the center itself is not spectral.

Set
\[
k=N_n+\frac{x}{N_n},\qquad y=\ell x,\qquad \varepsilon_n=(-1)^n.
\]
Uniformly for \(x\) in a compact set bounded away from zero, Taylor expansion of the exact quotient gives
\[
Q\left(N_n+\frac{x}{N_n}\right)
=
\varepsilon_n\left(\frac{s y}{2}-\frac{2s}{y}-2c\right)+O(N_n^{-2}).
\]
The limiting function
\[
q(y)=\frac{s y}{2}-\frac{2s}{y}-2c
\]
has derivative
\[
q'(y)=\frac{s}{2}+\frac{2s}{y^2}>0
\]
on each of the half-lines \(y<0\) and \(y>0\). Therefore the condition \(|q(y)|\le2\) produces exactly one interval on each half-line. Solving \(q(y)=\pm2\) gives the four roots
\[
-2(\sec\mu+\tan\mu),\quad -2\tan\frac{\mu}{2},\quad
2(\sec\mu-\tan\mu),\quad 2\cot\frac{\mu}{2}.
\]
Because all four roots are simple, uniform convergence and the implicit-function theorem give corresponding exact edge parameters with \(O(N_n^{-2})\) errors in \(x\). The factor \(\varepsilon_n\) only interchanges the roles of \(Q=2\) and \(Q=-2\); it does not change the allowed set defined by \(|Q|\le2\).

Finally,
\[
k^2-N_n^2=2x+\frac{x^2}{N_n^2},
\]
so doubling the limiting \(x\)-roots yields the four energy shifts above, with errors \(O(N_n^{-2})=O(n^{-2})\).

## Verification
The accompanying `verify.py` reconstructs the exact quotient \(Q(k)\) from the published secular coefficients, solves the four exact equations \(Q(k)=\pm2\) by bisection near their predicted asymptotic locations, and compares the resulting energy edges with the closed formulas. It tests three parameter values spanning the interval \(0<\mu<\pi/2\) and three increasing indices. The maximum edge error decreases by approximately a factor of four when \(n\) doubles, consistent with the proved \(O(n^{-2})\) remainder. The script also checks that \(k=N_n\) is not spectral and prints `VERIFY_OK` only if every check passes.

## Relationship to prior work
Exner and Tater derive the exact square-lattice secular equation for \(U=e^{i\mu}R\), prove that positive bands concentrate near \(k=n\pi/\ell\), and give a coarse high-energy displacement/width estimate together with the statement that the behavior is nonuniform as \(\mu\) approaches the endpoints. They do not state the two limiting local bands or the four closed-form energy edges above.

Their earlier preferred-orientation paper treats the endpoint coupling \(U=R\), where flat bands at \(k=n\pi/\ell\) and a different high-energy band/gap structure occur. The present claim explicitly excludes that endpoint and concerns the phase-rotated Robin case. Later work on other preferred-orientation lattices and finite-graph eigenvalue optimization concerns different geometries or different spectral questions and does not imply this local square-lattice scaling law.

## Limitations
The constants diverge as \(\mu\) approaches one endpoint on one of the two branches, so the theorem is not uniform in \(\mu\) near \(0\) or \(\pi/2\). No next correction beyond \(O(n^{-2})\) is claimed. The verification is numerical and finite; the infinite-index conclusion rests on the analytic expansion and root simplicity, not on the finite replay.

## References
1. P. Exner and M. Tater, *Quantum graphs: self-adjoint, and yet exhibiting a nontrivial PT-symmetry*, arXiv:2108.04708v1, especially equations (20)--(25). First public 2021-08-10. DOI:10.1016/j.physleta.2021.127669.
2. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664v1, especially the square-lattice spectral condition (11) and its high-energy discussion. DOI:10.1016/j.physleta.2017.11.028.
3. R. Band and G. Berkolaiko, *Universality of the momentum band density of periodic networks*, Phys. Rev. Lett. 111, 130404 (2013). DOI:10.1103/PhysRevLett.111.130404.
