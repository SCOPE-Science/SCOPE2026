# Arithmetic–geometric bracketing of uniform linear-FEM Laplace eigenvalues
## Finding
For the homogeneous Dirichlet problem \(-u''=\lambda u\) on \((0,1)\), use the standard continuous piecewise-linear finite-element space on the uniform mesh \(h=1/N\), with \(N\ge2\). For mode \(1\le k\le N-1\), put \(\theta=k\pi/N\) and \(x=\theta/2\). The exact eigenvalue and the two standard discrete eigenvalues are
\[
\lambda_k=(k\pi)^2=4N^2x^2,
\]
\[
\lambda^L_{k,N}=2N^2(1-\cos\theta)=4N^2\sin^2x,
\]
\[
\lambda^C_{k,N}=\frac{{6N^2(1-\cos\theta)}}{{2+\cos\theta}}
=\frac{{12N^2\sin^2x}}{{3-2\sin^2x}}.
\]
For every lower-half mode \(1\le k\le\lfloor N/2\rfloor\),
\[
\boxed{{\sqrt{{\lambda^L_{{k,N}}\lambda^C_{{k,N}}}}<\lambda_k<\frac{{\lambda^L_{{k,N}}+\lambda^C_{{k,N}}}}2}}.
\]
Thus two familiar second-order eigenvalue approximations yield, by two parameter-free scalar postprocessings, a strict fourth-order two-sided bracket.

## Assumptions and scope
The problem is one-dimensional, the coefficient is constant, the interval is \((0,1)\), the boundary condition is homogeneous Dirichlet, the mesh is uniform, the trial space is the usual \(P_1\) conforming space, and lumping means row-sum lumping. The theorem covers exactly the modes \(1\le k\le\lfloor N/2\rfloor\). It does not assert the arithmetic upper inequality for higher modes or for nonuniform meshes.

## Proof
The sine vectors diagonalize the stiffness, consistent mass, and lumped mass matrices simultaneously, giving the three formulas above. Write \(z=x^2\), \(y=\sin^2x\), and
\[
g(y)=\frac{{y(3-y)}}{{3-2y}}.
\]
The arithmetic mean equals \(4N^2g(y)\), so its being above the exact eigenvalue is equivalent to \(g(y)>z\). Since \(k\le N/2\), one has \(0<x\le\pi/4\), hence \(0<z<5/8\). The alternating sine series gives \(\sin x>x-x^3/6\), and therefore
\[
y>y_-:=z(1-z/6)^2.
\]
Moreover
\[
g'(y)=\frac{{2y^2-6y+9}}{{(3-2y)^2}}>0.
\]
A direct exact factorization is
\[
y_-(3-y_-)-z(3-2y_-)
=-\frac{{z^3}}{{1296}}\left(z^3-24z^2+144z-108\right).
\]
The cubic in parentheses is increasing on \([0,5/8]\) and its value at \(5/8\) is \(-13891/512<0\). Hence \(g(y)>z\), proving the arithmetic upper bound.

For the geometric mean, after squaring and cancelling positive factors the desired inequality is
\[
3y^2<z^2(3-2y).
\]
Set \(H_z(y)=z^2(3-2y)-3y^2\), which is strictly decreasing for \(y\ge0\). The alternating sine series also gives
\[
\sin x<x-x^3/6+x^5/120,
\]
so
\[
y<y_+:=z(1-z/6+z^2/120)^2.
\]
Exact algebra gives
\[
H_z(y_+)=-\frac{{z^4}}{{69120000}}Q(z),
\]
where
\[
Q(z)=z^6-80z^5+2880z^4-51200z^3+438400z^2-1152000z-4608000.
\]
For \(0\le z\le5/8\), dropping the negative terms yields
\[
Q(z)\le z^6+2880z^4+438400z^2-4608000<1+450+171250-4608000<0.
\]
Thus \(H_z(y_+)>0\), and monotonicity gives \(H_z(y)>0\). This proves the geometric lower bound.

Finally, expanding the exact formulas at \(\theta=0\) gives
\[
\frac{\lambda^L_{k,N}+\lambda^C_{k,N}}2-(k\pi)^2
=\frac{{(k\pi)^6}}{{360N^4}}-\frac{{(k\pi)^8}}{{6048N^6}}+O(N^{{-8}}),
\]
\[
\sqrt{{\lambda^L_{k,N}\lambda^C_{k,N}}}-(k\pi)^2
=-\frac{{(k\pi)^6}}{{1440N^4}}-\frac{{(k\pi)^8}}{{6048N^6}}+O(N^{{-8}}),
\]
and subtraction shows that the \(N^{{-6}}\) terms cancel in the bracket width:
\[
\frac{{\lambda^L_{k,N}+\lambda^C_{k,N}}}2-\sqrt{{\lambda^L_{k,N}\lambda^C_{k,N}}}
=\frac{{(k\pi)^6}}{{288N^4}}+O(N^{{-8}}).
\]

## Verification
`verify.py` checks the two polynomial factorizations in exact rational arithmetic, the endpoint sign estimates used in the proof, and the inequalities numerically over all lower-half modes for \(2\le N\le400\). The computation is supplementary: the infinite statement follows from the inequalities above, not from enumeration.

## Relationship to prior work
Hu, Huang, and Shen proved that lumped-mass finite-element eigenvalues lie below standard finite-element eigenvalues and, for model uniform-mesh problems, below the exact eigenvalues; their article lists primary MSC 65N30. Fried and Leong discuss the older strategy of interpolating between consistent and lumped mass matrices and applying a Rayleigh-quotient correction to obtain superaccurate eigenvalues. Luo, Lin, and Xie develop certified lower/upper Laplace-eigenvalue bounds by combining nonconforming and conforming finite-element calculations. Those results establish the relevance of opposite-sided mass effects, superaccurate combinations, and certified eigenvalue intervals. The present statement concerns a different postprocessing: the geometric and arithmetic means of the two separately defined standard \(P_1\) spectra, with an explicit strict lower-half bracket and its cancellation orders.

## Limitations
The proof exploits simultaneous sine diagonalization on a uniform one-dimensional grid. It does not establish analogous mean inequalities on nonuniform meshes, variable-coefficient problems, higher dimensions, or for modes above half the discrete spectrum. Earlier superaccurate mass-matrix literature is close conceptually; the accessible Fried–Leong source states an optimal intermediate mass/Rayleigh correction, not the geometric/arithmetic postprocessed bracket proved here. The earlier Fried–Chavez article is an additional residual originality risk because only its abstract was accessible during comparison.

## References
1. J. Hu, Y. Huang, H. Shen, “The Lower Approximation of Eigenvalue by Lumped Mass Finite Element Method,” *Journal of Computational Mathematics* 22 (2004), 545–556.
2. I. Fried, K. Leong, “Superaccurate finite element eigenvalues via a Rayleigh quotient correction,” *Journal of Sound and Vibration* 288 (2005), 375–386, DOI 10.1016/j.jsv.2005.03.027.
3. F. Luo, Q. Lin, H. Xie, “Computing the lower and upper bounds of Laplace eigenvalue problem: by combining conforming and nonconforming finite element methods,” arXiv:1109.5977v1.
