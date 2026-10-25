# Exact Wigner sampling spectra on the twelve fivefold icosahedral rotations

## Finding
Let \(X\subset SO(3)\) comprise the twelve distinct rotations through angle \(2\pi/5\), with oriented rotation axes pointing toward the twelve vertices of a regular icosahedron. These rotations form one conjugacy class of the rotational icosahedral group. For each integer \(\ell\ge0\), let \(\mathcal W_\ell\) be the \((2\ell+1)^2\)-dimensional space of matrix coefficients of the degree-\(\ell\) irreducible unitary representation of \(SO(3)\). Equip \(\mathcal W_\ell\) with the Haar-probability \(L^2\) inner product. Its orthonormal basis is \(\sqrt{2\ell+1}\,D^\ell_{mn}\) for \(-\ell\le m,n\le\ell\). Define the evaluation map \(E_\ell:\mathcal W_\ell\to\mathbb C^{12}\) by \((E_\ell f)(R)=f(R)/\sqrt{12}\).

Put \(n=2\ell+1\), \(\varphi=(1+\sqrt5)/2\), and define
\[
 a_\ell=[1,\varphi,0,-\varphi,-1]_{\ell\bmod5},\qquad
 b_\ell=[1,1-\varphi,0,\varphi-1,-1]_{\ell\bmod5},\qquad
 c_\ell=[1,0,-1]_{\ell\bmod3}.
\]
Then the **entire** spectrum of \(E_\ell E_\ell^*\), including zero eigenvalues, is \(n/12\) times the following four numbers with the listed multiplicities:
\[
\begin{aligned}
\eta_0&=n+5a_\ell+5c_\ell+b_\ell &&(1),\\
\eta_5&=n-a_\ell-c_\ell+b_\ell &&(5),\\
\eta_+&=n+\sqrt5(a_\ell-c_\ell)-b_\ell &&(3),\\
\eta_-&=n-\sqrt5(a_\ell-c_\ell)-b_\ell &&(3).
\end{aligned}
\]
This gives the exact rank classification
\[
\operatorname{rank} E_\ell=\begin{cases}1,&\ell=0,\\9,&\ell=1,\\11,&\ell=2,\\12,&\ell\ge3.\end{cases}
\]
At \(\ell=2\) the only sample-value constraint is \(\sum_{R\in X}f(R)=0\). For all \(\ell\ge3\), any twelve assigned complex values are interpolated by an exact-degree Wigner harmonic. The optimal nonzero squared singular-value bounds are exactly \(\frac{n}{12}\min_{\eta_j>0}\eta_j\) and \(\frac{n}{12}\max_j\eta_j\); for \(\ell\ge3\) the condition number is \(\sqrt{\max_j\eta_j/\min_j\eta_j}=1+O(\ell^{-1})\).

## Assumptions and scope
Use the standard, integer-spin irreducible unitary representation of \(SO(3)\); the Haar measure is normalized to probability, and the sampling norm uses equal weights \(1/12\). Reversing all coordinate axes, rotating the entire icosahedron, or relabeling vertices does not change the spectrum. All statements range over every integer \(\ell\ge0\). The assertion is **surjectivity of evaluation**, not injectivity from the \((2\ell+1)^2\)-dimensional harmonic space at large degrees. It concerns one 12-element class of rotations by \(72^\circ\), not sampling all 60 rotations or sampling scalar spherical harmonics at vertices.

## Proof
Write \(\chi_\ell(\theta)=\sin((\ell+\tfrac12)\theta)/\sin(\theta/2)=1+2\sum_{k=1}^\ell\cos(k\theta)\) for the character of the degree-\(\ell\) rotation representation. Orthogonality and unitarity give the exact sample Gram identity
\[
 (E_\ell E_\ell^*)_{uv}=\frac{n}{12}\,\chi_\ell(R_u^{-1}R_v).
\]
Represent the unit icosahedron vertices as the twelve vectors \((0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\), each divided by \(\sqrt{\varphi+2}\), with independently chosen displayed signs. The inner products of distinct vertex vectors are exactly \(-1,1/\sqrt5,-1/\sqrt5\), with valencies \(1,5,5\) respectively. Let \(A\) join pairs with inner product \(1/\sqrt5\), let \(P\) exchange antipodal vertices, and let \(B=PA\) join pairs with inner product \(-1/\sqrt5\). Thus \(A^2=5I+2A+2B\); \(P^2=I\); and \(A\) commutes with \(P\).

For \(u,v\) with angle \(\gamma\) between their axes, the relative rotation is determined by quaternion multiplication:
\[
 \cos\!\left(\frac{\theta(R_u^{-1}R_v)}2\right)=\cos^2(\pi/5)+\sin^2(\pi/5)\cos\gamma.
\]
The right-hand side is positive at all four inner products. It yields relative rotation angles \(0\), \(2\pi/5\), \(2\pi/3\), \(4\pi/5\) for inner products \(1,1/\sqrt5,-1/\sqrt5,-1\), respectively. Hence the unscaled Gram matrix is exactly
\[
 H_\ell=nI+a_\ell A+c_\ell B+b_\ell P.
\]
The finite-angle character formula yields the displayed period-five and period-three tables for \(a_\ell,b_\ell,c_\ell\).

The matrices \(A,P\) are simultaneously diagonalizable. In the \(P=+1\) sector, \(A^2=5I+4A\), so \(A\) has eigenvalues \(5\) (multiplicity one, constants) and \(-1\) (multiplicity five). In the \(P=-1\) sector, \(A^2=5I\), so \(A\) has \(\sqrt5\) and \(-\sqrt5\), each with multiplicity three: both the trace of \(A\) and the trace of \(AP\) vanish. Since \(B=PA\), evaluating \(H_\ell\) on these four invariant sectors proves all four eigenvalue branches with multiplicities \(1,5,3,3\).

At the three low degrees, the unscaled spectra, ordered by the four sectors above, are
\[
\begin{array}{c|cccc}
\ell&\eta_0&\eta_5&\eta_+&\eta_-\\\hline
0&12&0&0&0\\
1&6+2\sqrt5&3-\sqrt5&5+\sqrt5&0\\
2&0&6&5+\sqrt5&5-\sqrt5
\end{array}
\]
which proves the corresponding ranks. In degree two the only null vector is the constant vector, proving the claimed zero-sum condition.

For every \(\ell\ge3\), use \(|a_\ell|\le\varphi\), \(|b_\ell|\le1\), and \(|c_\ell|\le1\). Then \(\eta_5\ge n-(\varphi+2)>0\), and \(\eta_\pm\ge n-\sqrt5(\varphi+1)-1>0\), because already \(n\ge7\) and \(6-\sqrt5(\varphi+1)=(7-3\sqrt5)/2>0\). For \(\ell\ge7\), \(\eta_0\ge n-5\varphi-6\ge9-5\varphi>0\). The remaining degrees \(3,4,5,6\) have \(\eta_0=9-2\sqrt5,3,12,21+2\sqrt5\), respectively, all positive. Hence the Gram has full rank for every \(\ell\ge3\). Finally, all corrections to \(n\) in the four eigenvalue branches are uniformly bounded, giving the stated asymptotic conditioning and sharp finite-degree singular-value formulas.

## Verification
Run \(\texttt{python3 verify_icosahedral_class.py}\) with Python 3 and SymPy installed. It constructs the twelve explicit exact algebraic axis vectors, tests their three pairwise dot products and the icosahedral adjacency/interchange matrices, proves the four fixed eigenspace multiplicities by exact arithmetic, and verifies the predicted four Gram eigenvalue branches for one hundred degrees. The indefinite-degree conclusion is established by the analytic inequalities in the proof, not by the finite checker. No numerical floating-point threshold is used in the argument.

## Relationship to prior work
McEwen, Büttner, Leistedt, Peiris and Wiaux (2015, arXiv:1508.03101) develop an exact Wigner sampling theorem for **equiangular grids** on \(SO(3)\) with a band-limited input. Their equations for Wigner orthogonality provide the normalization used here; they do not classify twelve samples from a finite icosahedral conjugacy class at any individual degree. Fan, Chen and Draayer (1999) construct icosahedral symmetry-adapted spherical harmonics and projection operators; their symmetry decomposition is relevant background, but the inspected abstract and opening text do not state the conjugacy-class Wigner sampling singular spectrum. The previously analyzed scalar spherical-harmonic sampling at icosahedron vertices is different: its Legendre-polynomial Gram kernel has an antipodal parity restriction, whereas the present \(SO(3)\) character Gram kernel attains full rank twelve.

## Limitations
The classification covers exactly this 12-rotation conjugacy class and integer Wigner degrees; it does not assert an optimal sample configuration among all twelve-node designs or characterize arbitrary mixed-degree bands. The 1999 symmetry-adapted-function paper was not available for reliable complete-page comparison here, so possible implicit coverage or earlier equivalent formulas remain originality risks. The presented symbolic checker is corroborating evidence, not an independent proof or external audit.

## References
1. J. D. McEwen, M. Büttner, B. Leistedt, H. V. Peiris, and Y. Wiaux, *A novel sampling theorem on the rotation group*, initial public arXiv posting 2015-08-13, arXiv:1508.03101, https://arxiv.org/abs/1508.03101.
2. P.-D. Fan, J.-Q. Chen, and J. P. Draayer, *Reduced projection operators and algebraic expressions for the symmetry-adapted functions of the icosahedral group*, Acta Crystallographica A55 (1999), 871–883, DOI: 10.1107/S010876739900330X.
3. Standard representation-theoretic character formula for integer-spin irreducible representations of \(SO(3)\); the exact formula used is stated and derived by finite trigonometric summation above.
