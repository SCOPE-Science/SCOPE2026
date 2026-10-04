# Exact parity-split high-energy offsets for the preferred-orientation dodecahedron

## Finding
For the unit-edge dodecahedral quantum graph with the preferred-orientation coupling, write \(N_n=n\pi\) and use the five rotational sectors \(\omega_j=e^{2\pi i j/5}\). For every nonzero branch in the high-energy cluster \(k=N_n+O(N_n^{-1})\), define \(\xi_n=N_n(k-N_n)\).

The nonzero scaled limits are parity-sensitive and exactly sector-resolved. For even \(n\), sector \(j=0\) has \(\xi=\pm2\sqrt2\), while sectors \(j=1,2,3,4\) have \(\xi=\pm\sqrt5\) and \(\xi=\pm2\sqrt2\). For odd \(n\), sector \(j=0\) has \(\xi=\pm(\sqrt5-1)\), \(\pm2\), and \(\pm(\sqrt5+1)\); sectors \(j=1,4\) have \(\xi=\pm1\), \(\pm2\), and \(\pm(\sqrt5+1)\); sectors \(j=2,3\) have \(\xi=\pm1\), \(\pm(\sqrt5-1)\), and \(\pm2\). Every listed nonzero limit comes from a simple root of the limiting sector equation and hence persists as a nearby eigenvalue branch.

Equivalently, the corresponding energy offsets satisfy \(k^2-N_n^2\to2\xi\). Thus the coarse source envelope \(5.51\) in the momentum scaling can be replaced, for nonzero scaled branches, by the exact parity envelopes \(2\sqrt2\) for even \(n\) and \(\sqrt5+1\) for odd \(n\).

## Assumptions and scope
The graph is the equilateral dodecahedral metric graph with every edge identified with an interval of length one and with the preferred-orientation coupling used in arXiv:1906.09091. The rotation-sector parameter is \(\omega_j=e^{2\pi i j/5}\). The statement concerns the clusters around \(N_n=n\pi\) in the high-energy limit \(n\to\infty\). It classifies only branches with a nonzero limit of \(N_n(k-N_n)\). Even-parity branches at smaller scale are deliberately excluded.

## Proof
The primary source derives, in each sector, a high-energy secular equation whose displayed leading expression is a cubic in \(y=k^2\sin^2 k\), up to a remainder of order \(k^{-2}\). Set \(\varepsilon=(-1)^n\). Inside a cluster with \(k-N_n=O(N_n^{-1})\), one has \(\cos k\to\varepsilon\) and \(\sin^2 k=O(N_n^{-2})\). Keeping the nonvanishing terms in the source equation gives

\[
P_{\varepsilon,j}(y)=\omega_j y^3+A_{\varepsilon,j}y^2+B_{\varepsilon,j}y+C_{\varepsilon,j},
\]
with
\[
A_{\varepsilon,j}=\omega_j^4+\omega_j^3+(2\varepsilon-1)\omega_j^2-12\omega_j+2\varepsilon-1,
\]
\[
B_{\varepsilon,j}=(-2\varepsilon-6)(\omega_j^4+\omega_j^3)+(4-12\varepsilon)\omega_j^2+(36-4\varepsilon)\omega_j+(4-12\varepsilon),
\]
and
\[
C_{\varepsilon,j}=8(\varepsilon-1)(\omega_j+1)^2.
\]

For even \(n\), \(\varepsilon=1\). At \(j=0\),
\[
P_{1,0}(y)=y^2(y-8).
\]
For \(j=1,2,3,4\), the fifth-root identity \(1+\omega_j+\omega_j^2+\omega_j^3+\omega_j^4=0\) yields
\[
P_{1,j}(y)=\omega_j y(y-5)(y-8).
\]
Hence the positive simple roots are \(8\) in sector \(j=0\), and \(5,8\) in the four nontrivial sectors.

For odd \(n\), \(\varepsilon=-1\). In sector \(j=0\),
\[
P_{-1,0}(y)=(y-4)(y-(6-2\sqrt5))(y-(6+2\sqrt5)).
\]
For nontrivial sectors, division by \(\omega_j\) and the substitution \(x_j=\omega_j+\omega_j^{-1}\) give
\[
\frac{P_{-1,j}(y)}{\omega_j}=y^3-(13+4x_j)y^2+4(11+5x_j)y-16(2+x_j).
\]
Now \(x_1=x_4=(\sqrt5-1)/2\) and \(x_2=x_3=-(\sqrt5+1)/2\), so
\[
\frac{P_{-1,1}(y)}{\omega_1}=\frac{P_{-1,4}(y)}{\omega_4}=(y-1)(y-4)(y-(6+2\sqrt5)),
\]
while
\[
\frac{P_{-1,2}(y)}{\omega_2}=\frac{P_{-1,3}(y)}{\omega_3}=(y-1)(y-4)(y-(6-2\sqrt5)).
\]
Since \(6\pm2\sqrt5=(\sqrt5\pm1)^2\), taking square roots of the positive roots gives exactly the listed nonzero scaled offsets.

To pass from the limiting polynomial to eigenvalue branches, substitute \(k=N_n+z/N_n\) in the exact sector secular determinant. On compact \(z\)-sets its normalized form tends to a nonzero sector phase times \(P_{\varepsilon,j}(z^2)\); the omitted terms in the source expansion are uniformly smaller. Every listed nonzero root \(z\) is simple because \(z\ne0\) and the corresponding root of \(P_{\varepsilon,j}\) is simple. Standard simple-zero stability, equivalently Rouché's theorem on a small circle around the root, produces a nearby root for all sufficiently large \(n\). Finally,
\[
k^2-N_n^2=2N_n(k-N_n)+(k-N_n)^2\to2\xi.
\]

## Verification
The accompanying `verify.py` independently reconstructs the limiting coefficients from the displayed secular expression, evaluates the sector polynomials at the claimed roots, checks simplicity of every positive root, and verifies the fifth-root reductions numerically to tight tolerance. It also evaluates the full displayed high-energy secular expression at \(k=N_n+c/N_n\) for increasing \(n\); the residual decays quadratically, as predicted by the \(O(k^{-2})\) remainder. A bisection check on the displayed real-phase equation confirms convergence of finite-index scaled roots to the stated constants.

## Relationship to prior work
Exner and Lipovský derive the dodecahedral sector secular equation and prove only the common enclosure
\[
|k\sin k|\le 5.51+O(k^{-2}),
\]
which yields their Theorem 6.1 interval around \(n\pi\). Their proof explicitly replaces the sector cubics by coefficient bounds before applying a polynomial root bound. The factorization above retains the fivefold-sector phase and therefore resolves the cluster into exact parity-dependent constants. A later overview of preferred-orientation quantum graphs restates only the qualitative \(O(n^{-1})\) clustering for the odd-degree Platonic solids and uses the tetrahedron as its explicit example; it does not give the dodecahedral constants above.

Targeted searches for dodecahedral preferred-orientation quantum-graph offsets, golden-ratio cluster constants, the source's \(5.51\) bound, and the sector cubic produced no publication or indexed result stating these factorizations or their energy-offset consequence. General symmetry-quotient and preferred-orientation results explain the decomposition and the odd-degree decoupling mechanism but do not imply the numerical sector constants without analyzing this dodecahedral cubic.

## Limitations
The result is a first scaled-order statement. It does not resolve even-parity branches for which \(N_n(k-N_n)\to0\), their multiplicities, or any next-order corrections. The originality search cannot exclude an equivalent calculation hidden under substantially different terminology, and no independent audit has been performed.

## References
1. P. Exner and J. Lipovský, *Spectral asymptotics of the Laplacian on Platonic solids graphs*, arXiv:1906.09091v1, first posted 21 June 2019; especially Section 6.2 and Theorem 6.1. https://arxiv.org/abs/1906.09091
2. J. Lipovský, *Quantum Graphs with Preferred-Orientation Coupling*, habilitation lecture text, Section 5.2. https://lide.uhk.cz/prf/ucitel/lipovji1/papers/text_for_habilitation_lecture_lipovsky.pdf
3. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664.
