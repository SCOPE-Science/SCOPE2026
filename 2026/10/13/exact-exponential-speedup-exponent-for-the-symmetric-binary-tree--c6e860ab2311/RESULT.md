# Exact exponential speedup exponent for the symmetric binary-tree quantum walk
## Finding
For the symmetric discrete-time quantum walk on the semi-infinite binary tree introduced by Dimcovic, Rockwell, Milligan, Burton, Nguyen and Kovchegov, let \(H_n(t)\) be the amplitude at the root when the walk starts at level \(n\), and let
\[
T_n^{\mathrm q}=\min_{t\ge n}\frac{t}{|H_n(t)|^2}.
\]
Then
\[
\lim_{n\to\infty}\frac1n\log T_n^{\mathrm q}
=\log(12-6\sqrt3)
=\log\!\left(\frac6{2+\sqrt3}\right).
\]
The exponentially optimal times satisfy
\[
\frac{t}{n}\longrightarrow2(\sqrt3-1)=1.464101615\ldots .
\]
For the classical symmetric walk used in the same comparison,
\[
\lim_{n\to\infty}\frac1n\log T_n^{\mathrm c}=\log2.
\]
Consequently the exact exponent relating the quantum and classical run times is
\[
\eta=\frac{\log(12-6\sqrt3)}{\log2}=0.684993873768\ldots,
\]
so the paper's conjectured exponent \(2/3\) is false, while its fitted value \(0.685\) is asymptotically accurate.

## Assumptions and scope
The walk, root amplitude, and run-time proxy are exactly those of arXiv:1107.4201 and Phys. Rev. A 84, 032311 (2011). Write \(a=e^{2\pi i/3}\). The source gives the root-return generating function \(\widehat g(z)\), the one-level first-hit transform \(\widehat h_1(z)\), and
\[
\widehat H_n(z)=\widehat h_1(z)^n\frac1{1-\widehat g(z)}.
\]
Only the large-\(n\), linearly scaled-time regime is asserted here. Polynomial prefactors are not claimed in closed form.

## Proof
Put \(u=(az)^2\). Substitution of the source's equations (15) and (17) gives
\[
\widehat h_1(z)=\frac{az}{\sqrt3}F(u),
\qquad
F(u)=\frac{5u-3+3\sqrt{1-\frac23u+u^2}}{4u},
\]
where the square-root branch is the one analytic at \(u=0\). Set \(q=F-1\). Direct elimination of the square root yields
\[
q=\frac u3(1+q-2q^2),
\qquad
u(q):=u=\frac{3q}{(1-q)(1+2q)}.
\]
For \(|u|=1\), taking moduli in \(3q=u(1-q)(1+2q)\) and writing \(q=x+iy\), \(s=|q|^2\), gives
\[
(-2s+4x+1)(2s+2x-1)=0.
\]
The analytic branch through \(u=1\) lies on \(s+x=1/2\); there \(q\) runs on the circle
\[
\left(x+\frac12\right)^2+y^2=\frac34.
\]
Its rightmost point is
\[
q_*=\frac{\sqrt3-1}{2},
\]
and the other boundary arc has \(x\le0\). Hence
\[
\max_{|z|=1}|\widehat h_1(z)|^2
=\frac{|1+q_*|^2}{3}
=\frac{2+\sqrt3}{6}=:\rho^2,
\]
with a unique nondegenerate maximum modulo the parity symmetry. The renewal factor \((1-\widehat g(z))^{-1}\) is bounded on the unit circle. Indeed the same parametrization gives \(|\widehat g|=|1-2q|/\sqrt3\le1\) on both boundary arcs. Equality occurs only at the two square-root branch points \(q=\pm i/\sqrt2\), where direct substitution gives \(\widehat g\ne1\). At the maximizing point itself, \(|\widehat g|=2/\sqrt3-1<1\). Thus the fixed renewal factor is bounded and nonzero where the local saddle is taken.

For coefficients with \(t=n+2m\), one-dimensional saddle-point extraction of \(F(u)^n\) has phase equation
\[
\alpha:=\frac mn=\frac{uF'(u)}{F(u)}
=\frac{q(1-q)(1+2q)}{(1+q)(1+2q^2)}.
\]
At the boundary-modulus maximizer \(u=1\), equivalently \(q=q_*\),
\[
\alpha_*=\sqrt3-\frac32,
\qquad
1+2\alpha_*=2(\sqrt3-1).
\]
The saddle is nondegenerate: the second derivative of \(\log(1+q)-\alpha_*\log u(q)\) at \(q_*\) equals
\[
-2+\frac{4\sqrt3}{3}>0.
\]
Thus standard local steepest descent gives at the nearest admissible integers \(m=\alpha_*n+O(1)\)
\[
|H_n(n+2m)|=n^{-1/2+o(1)}\rho^n,
\]
while the unit-circle maximum above gives the matching uniform exponential upper bound for all coefficients. Therefore
\[
\lim_{n\to\infty}\frac1n\log\max_t|H_n(t)|^2=\log\rho^2.
\]
Because the renewal factor is bounded on the unit circle, the boundary maximum gives a uniform coefficient bound \(|H_n(t)|\le C\rho^n\) for every \(t\), while the local saddle produces a coefficient \(n^{-1/2+o(1)}\rho^n\) at linear time. Since every admissible \(t\ge n\), these two bounds sandwich the global minimum of \(t/|H_n(t)|^2\) at the same exponential rate. Hence
\[
\lim_{n\to\infty}\frac1n\log T_n^{\mathrm q}=-\log\rho^2
=\log\!\left(\frac6{2+\sqrt3}\right).
\]

For the classical comparison, the one-level first-passage probability transform satisfies
\[
h(z)=\frac13z+\frac23zh(z)^2.
\]
It has nonnegative coefficients, \(h(1)=1/2\), and its tilted mean at \(z=1\) is
\[
\frac{h'(1)}{h(1)}=3.
\]
The same renewal argument therefore gives a peak at \(t/n\to3\) with probability \(2^{-n+o(n)}\), and hence \(n^{-1}\log T_n^{\mathrm c}\to\log2\). Dividing the two exact logarithmic rates proves the claimed exponent \(\eta\).

## Verification
The standalone script `verify.py` checks the algebraic constants, the saddle location, the classical tilted mean, and a dense unit-circle numerical replay of the sharp boundary modulus. Running it prints `VERIFY_OK`. The numerical replay is auxiliary; the proof of the sharp modulus is the exact factored identity above.

The resulting constants agree closely with the source's independent numerical observations: it reports a quantum linear-fit slope \(0.475234\) versus the exact value \(0.4748015723\ldots\), a classical fitted slope \(0.69401\) versus \(\log2=0.69314718\ldots\), a slope ratio about \(0.685\), and quantum peak time about \(1.46n\).

## Relationship to prior work
Dimcovic et al. derive the exact generating functions and perform numerical inversion up to large \(n\). They report the fitted slopes just quoted and explicitly conjecture that the quantum run time is of order \((T_n^{\mathrm c})^{2/3}\). Their Table I and Figure 7 supply the numerical evidence, but the paper does not derive the proportional-\(n\) coefficient saddle or an exact exponent. Searches by the source identifier, conjectured exponent, exact constants, peak-time constant, and equivalent hitting-time language did not locate a later result implying the theorem above. Later work on quantum walks on infinite trees that was inspected concerns spectral localization of Grover-type walks rather than this root-hitting run-time asymptotic.

## Limitations
The theorem concerns this specific symmetric discrete-time walk and the run-time proxy used in its source. It does not assert the same exponent for other coins, other boundary conditions, finite binary trees, measured first-hitting protocols, or Grover walks. The proof determines the exponential rate and asymptotically optimal linear time; it does not supply the complete polynomial prefactor of \(T_n^{\mathrm q}\). A residual literature risk is that the same saddle calculation may exist under different terminology in later work not indexed by the searched source/citation vocabulary.

## References
1. Z. Dimcovic, D. Rockwell, I. Milligan, R. M. Burton, T. Nguyen, Y. Kovchegov, “Framework for discrete-time quantum walks and a symmetric walk on a binary tree,” arXiv:1107.4201, first submitted 2011-07-21; Phys. Rev. A 84, 032311 (2011), DOI: 10.1103/PhysRevA.84.032311.
2. Y. Higuchi and E. Segawa, “Quantum walks induced by Dirichlet random walks on infinite trees,” J. Phys. A 51, 075303 (2018), DOI: 10.1088/1751-8121/aa8fba.
