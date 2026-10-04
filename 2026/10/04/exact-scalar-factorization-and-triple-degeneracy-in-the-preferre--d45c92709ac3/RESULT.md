# Exact scalar factorization and triple degeneracy in the preferred-orientation octahedron spectrum
## Finding
For the unit-edge equilateral octahedron quantum graph with the preferred-orientation vertex coupling, the positive nonexceptional spectrum has an exact two-equation description. Apart from the already exact families \(k=2\pi n\) and \(k=\pm 2\pi/3+2\pi n\), every positive spectral wave number \(k\) satisfies exactly one of
\[
\tan^2(k/2)=2k^2+1,
\]
or
\[
\tan^2(k/2)=1+2/k^2.
\]
Every root of either scalar equation is simple in that equation and yields a graph eigenvalue \(k^2\) of multiplicity exactly three.

Writing \(K_n=(2n+1)\pi\), the first equation has the two high-energy roots
\[
k_{n,\pm}=K_n\pm\frac{\sqrt{2}}{K_n}+O(K_n^{-3}).
\]
Writing \(L_n=\pi/2+n\pi\), the second equation has the high-energy root
\[
\widetilde k_n=L_n+(-1)^nL_n^{-2}+O(L_n^{-4}).
\]
These formulas sharpen the interval bounds in the published octahedron theorem and identify the nonexceptional multiplicity.

## Assumptions and scope
The graph is the equilateral octahedron with every edge identified with \((0,1)\). At every degree-four vertex the preferred-orientation coupling is the cyclic Exner–Tater condition used by Exner and Lipovský. Only positive spectral parameters \(k>0\), with energy \(E=k^2\), are considered. The result does not address unequal edge lengths, phase-distorted couplings, or the negative spectrum.

The source decomposes the Hamiltonian by the four eigenvalues of a quarter-turn symmetry, giving component sectors \(j=0,1,2,3\). Its exact component secular equations are the starting point; no numerical spectral ansatz is used as a premise.

## Proof
Set \(x=\cos^2(k/2)\) and \(y=k^2\). In the \(j=1\) and \(j=3\) sectors, the nontrivial bracket in the published secular determinant is
\[
2y^2(2x-1)x+y\bigl(1+4x(2x-1)\bigr)+2(2x-1)x.
\]
Direct expansion gives the exact factorization
\[
\bigl(2(y+1)x-y\bigr)\bigl(2(y+1)x-1\bigr).
\]
The residual factor in the published \(j=0\) determinant is, up to a nonzero constant, \(2(y+1)x-1\), while the residual factor in the \(j=2\) determinant is, up to a nonzero constant, \(2(y+1)x-y\). Hence every nonexceptional root belongs to either sectors \(0,1,3\) or sectors \(1,2,3\), respectively.

The equation \(2(k^2+1)\cos^2(k/2)=1\) is equivalent to
\[
\tan^2(k/2)=2k^2+1,
\]
and \(2(k^2+1)\cos^2(k/2)=k^2\) is equivalent to
\[
\tan^2(k/2)=1+2/k^2.
\]
The two root sets are disjoint: equality of their right-hand sides would force \(k=1\), but \(k=1\) satisfies neither equation. They also do not meet the exact factors \(\sin(k/2)=0\) or \(4\cos^2(k/2)-1=0\).

For simplicity, put \(t=\tan(k/2)\). For the first equation let \(G_1(k)=t^2-(2k^2+1)\). At a root,
\[
G_1'(k)=2\bigl((k^2+1)t-2k\bigr).
\]
If \(t<0\) this is negative. If \(t>0\), then
\[
(k^2+1)^2t^2-4k^2=2k^6+5k^4+1>0,
\]
so it is positive. Thus every first-family root is simple.

For the second equation let \(G_2(k)=t^2-(1+2/k^2)\). Any positive root has \(k>1\): on \(0<k\le1\), monotonicity of tangent and \(1/2<\pi/4\) give \(t^2<1\), whereas \(1+2/k^2\ge3\). At a root,
\[
G_2'(k)=\frac{2(k^2+1)}{k^2}t+\frac{4}{k^3}.
\]
It is positive when \(t>0\). If \(t<0\) and the derivative vanished, squaring the resulting identity and using the root equation would give
\[
4=(k^2+2)(k^2+1)^2,
\]
which is impossible for \(k>1\). Hence these roots are also simple.

Each of the three sector determinants containing a given scalar factor therefore has a simple zero, so its boundary linear system has one-dimensional kernel. The four symmetry sectors form an orthogonal direct sum; since no fourth sector contains that root, the graph eigenvalue has multiplicity exactly three.

For the asymptotics, write \(k=K_n+\delta\) in the first equation. Since \(K_n\) is an odd multiple of \(\pi\),
\[
\tan^2(k/2)=\cot^2(\delta/2)=\frac{4}{\delta^2}-\frac{2}{3}+O(\delta^2).
\]
Substitution of \(\delta=aK_n^{-1}+bK_n^{-2}+O(K_n^{-3})\) forces \(a=\pm\sqrt2\) and \(b=0\), yielding the stated \(O(K_n^{-3})\) expansion.

For the second equation write \(k=L_n+\delta\) and \(s=(-1)^n\). Around \(L_n\),
\[
\tan^2((L_n+\delta)/2)=1+2s\delta+2\delta^2+O(\delta^3),
\]
while
\[
1+\frac{2}{(L_n+\delta)^2}=1+2L_n^{-2}+O(L_n^{-5}).
\]
Thus \(\delta=sL_n^{-2}+O(L_n^{-4})\).

## Verification
The accompanying verifier checks the polynomial factorization exactly at the coefficient level, checks the \(j=0\) and \(j=2\) reductions, solves representative roots of both scalar equations by bisection, and verifies convergence to the predicted scaled offsets. Its numerical checks corroborate the analytic proof; they are not used to infer the infinite statements.

## Relationship to prior work
Exner and Lipovský derive the four symmetry-sector secular determinants for this octahedron and state exact multiplicities for two elementary spectral families. For the remaining two families, their Theorem 5.1 gives only asymptotic localization in intervals of width \(O(k^{-1})\) around odd multiples of \(\pi\), and \(O(k^{-2})\) around \(\pi/2+n\pi\). The exact quadratic factorization above is not stated there; it turns those interval-localized branches into exact scalar equations and yields the sharper coefficients \(\sqrt2\) and \(1\), together with multiplicity three.

The earlier preferred-orientation paper develops the vertex coupling and periodic square/hexagonal lattice spectra, not the finite octahedron secular problem. A later eigenvalue-optimization paper concerns stars and general variational bounds, while recent preferred-orientation spectral-statistics work studies chiefly incommensurate graphs and form factors. None of those statements implies the exact equilateral-octahedron factorization above.

## Limitations
This is an exact refinement of a specific finite equilateral model, not a result for arbitrary metrics on the octahedral combinatorial graph. The argument assumes precisely the cyclic preferred-orientation coupling and unit edge length. The literature searches found no equivalent factorization or exact triple-degeneracy statement, but an unindexed equivalent derivation under different terminology remains a residual originality risk.

## References
1. P. Exner and J. Lipovský, “Spectral asymptotics of the Laplacian on Platonic solids graphs,” arXiv:1906.09091v1 (2019), later J. Math. Phys. 60, 122101. https://arxiv.org/abs/1906.09091 ; https://doi.org/10.1063/1.5116100
2. P. Exner and M. Tater, “Quantum graphs with vertices of a preferred orientation,” arXiv:1710.02664, Phys. Lett. A 382 (2018), 283–287. https://arxiv.org/abs/1710.02664
3. P. Exner and J. Rohleder, “Optimization of quantum graph eigenvalues with preferred orientation vertex conditions,” arXiv:2410.21820. https://arxiv.org/abs/2410.21820
