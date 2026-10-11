# Antiperiodic cyclic shifts have a sharp numerical-radius gap on real sequence spaces

## Finding

For each fixed real \(1<p<\infty\), let \(U_n\) act on \(\ell_p^n(\mathbb R)\) by shifting consecutive coordinates and negating the coordinate wrapped from the first position to the last. Its spatial numerical radius satisfies
\[
v_p(U_n)=1\quad(n\text{ odd}),\qquad v_p(U_n)<1\quad(n\text{ even}),
\]
and, along even dimensions,
\[
\lim_{\substack{n\to\infty\\n\ \mathrm{even}}}
n^2\bigl(1-v_p(U_n)\bigr)=\frac{2(p-1)\pi^2}{p^2}.
\]
The result is about numerical radius, not the norm of a sum of operators. At \(p=2\), every even-dimensional radius equals \(\cos(\pi/n)\), agreeing with the limit.

## Assumptions and scope

Fix \(1<p<\infty\) and \(n\ge2\). All spaces and functionals are **real**. Explicitly, \((U_nx)_j=x_{j+1}\) for \(1\le j<n\), and \((U_nx)_n=-x_1\). The norming functional at a unit vector is \(J_p(x)=(|x_j|^{p-2}x_j)_j\) (put \(|0|^{p-2}0=0\)); its dual norm is one. The spatial numerical radius is
\[
v_p(U_n)=\max_{\sum_j|x_j|^p=1}\left|\sum_{j=1}^{n-1}|x_j|^{p-2}x_jx_{j+1}-|x_n|^{p-2}x_nx_1\right|.
\]
The assertion is a fixed-exponent large-dimension limit; it does not cover \(p=1\), \(p=\infty\), complex scalars, variable exponents, or arbitrary signed shifts.

## Proof

**1. Parity and a Young-defect variational formula.** For odd \(n\), the alternating-sign vector is an eigenvector of \(U_n\) with eigenvalue \(-1\), hence \(v_p(U_n)=1\) because \(\|U_n\|=1\). For even \(n\), conjugation by the diagonal sign matrix \(\operatorname{diag}(1,-1,1,-1,\ldots,-1)\) sends \(U_n\) to \(-U_n\). Thus the numerical-radius absolute value can be removed by taking the maximum of its signed pairing.

Write \(x_{n+1}=-x_1\), and define the nonnegative Young defect
\[
E_p(a,b)=\frac{p-1}{p}|a|^p+\frac1p|b|^p-|a|^{p-2}ab.
\]
Young's inequality implies \(E_p(a,b)\ge0\), with equality precisely when \(a=b\). Cyclicity of absolute values implies the exact identity
\[
1-v_p(U_n)=\min_{x\ne0}
\frac{\sum_{j=1}^{n}E_p(x_j,x_{j+1})}{\sum_{j=1}^{n}|x_j|^p}
\qquad(n\text{ even}). \tag{1}
\]
Indeed the pairings are homogeneous of degree \(p\), and the sign conjugation removes the negative branch. Equality \(v_p(U_n)=1\) for even \(n\) would make every defect zero and force all coordinates equal, incompatible with \(x_{n+1}=-x_1\) unless \(x=0\). Finite-dimensional compactness gives strict inequality.

**2. The power transform and the crucial local coefficient.** Let \(\Phi_p(t)=\operatorname{sgn}(t)|t|^{p/2}\), so \(\Phi_p(-t)=-\Phi_p(t)\), \(|\Phi_p(t)|^2=|t|^p\), and \(\Phi_p\) is a homeomorphism of the real line. Put
\[
R_p(a,b)=\frac{E_p(a,b)}{|\Phi_p(b)-\Phi_p(a)|^2}\qquad(a\ne b).
\]
The quotient is strictly positive and homogeneous of degree zero under a common positive scaling of \((a,b)\). By the equality case of Young's inequality, it extends continuously across \(a=b\ne0\), with limiting value
\[
c_p=\frac{2(p-1)}{p^2}.\tag{2}
\]
To check the coefficient, expand \(E_p(a,a+h)=(p-1)|a|^{p-2}h^2/2+o(h^2)\) and \((\Phi_p(a+h)-\Phi_p(a))^2=p^2|a|^{p-2}h^2/4+o(h^2)\). Homogeneity and compactness of the normalized circle \(|a|^p+|b|^p=1\) now yield \(0<\kappa_p\le R_p(a,b)\). On the closed same-sign region \(ab\ge0\), the corresponding upper bound \(R_p(a,b)\le K_p<\infty\) also holds. The latter includes zero endpoints by taking limits with the other coordinate nonzero. Consequently
\[
E_p(a,b)\ge\kappa_p|\Phi_p(b)-\Phi_p(a)|^2\qquad(a,b\in\mathbb R).\tag{3}
\]

**3. A universal lower bound for the scaled gap.** Let \(n\) run through even integers, and take a minimizing vector in (1), normalized by \(n^{-1}\sum_j|x_j|^p=1\). Put \(z_j=\Phi_p(x_j)\), including \(z_{n+1}=-z_1\). A recovery family in Step 4 will establish a uniform bound \(n^2(1-v_p(U_n))\le C_p\). From (1) and (3), therefore,
\[
n\sum_{j=1}^n|z_{j+1}-z_j|^2\le C_p/\kappa_p.
\]
Linearly interpolate the values \(z_1,\ldots,z_{n+1}\) at the grid \(t=(j-1)/n\). The resulting functions are bounded in \(H^1(0,1)\). Moreover \(n^{-1}\sum z_j^2=1\), and one-dimensional Sobolev compactness makes their limit \(z\) satisfy \(\int_0^1z^2=1\) and \(z(1)=-z(0)\). On any compact interval where \(|z|>\varepsilon\), adjacent transformed coordinates converge uniformly to the same nonzero value, and the quotient in Step 2 converges uniformly to \(c_p\). Weak lower semicontinuity applied on these intervals yields
\[
\liminf_{n\ \mathrm{even}}n\sum_j E_p(x_j,x_{j+1})
\ge c_p\int_{\{z\ne0\}}|z'(t)|^2\,dt
=c_p\int_0^1|z'(t)|^2\,dt.
\]
The last equality uses the standard Sobolev fact that the derivative vanishes almost everywhere on a function's zero set. This localization avoids assuming uniform quadratic Taylor expansions at zero, which would be false for non-Hilbert exponents. Anti-periodic Poincaré–Wirtinger yields \(\int_0^1|z'|^2\ge\pi^2\int_0^1|z|^2=\pi^2\): extend \(z\) to a mean-zero two-periodic \(H^1\) function by setting \(z(t+1)=-z(t)\). Finally the normalization makes (1) imply \(n^2(1-v_p(U_n))=n\sum_jE_p(x_j,x_{j+1})\). Hence
\[
\liminf_{n\to\infty,\ n\ \mathrm{even}}n^2(1-v_p(U_n))\ge c_p\pi^2.\tag{4}
\]

**4. A matching recovery sequence.** For even \(n\), choose \(z_j=\sin(\pi(j-1)/n)\ge0\) and \(x_j=z_j^{2/p}\) for \(1\le j\le n\). The antiperiodic last value is \(x_{n+1}=-x_1=0\). The exact normalization is \(\sum_j|x_j|^p=\sum_jz_j^2=n/2\). All consecutive coordinate pairs have the same sign (or include zero). Therefore the same-sign upper bound \(K_p\) from Step 2 controls every boundary increment. Away from the two vanishing endpoints, the quotients \(R_p(x_j,x_{j+1})\) converge to \(c_p\) uniformly. Since \(n\sum_j(z_{j+1}-z_j)^2\to\pi^2/2\), and the proportion of its energy near the endpoints tends to zero, dominated decomposition gives
\[
\lim_{n\to\infty,\ n\ \mathrm{even}} n\sum_jE_p(x_j,x_{j+1})=\frac{c_p\pi^2}{2}.
\]
Using (1) and \(\sum|x_j|^p=n/2\), we obtain \(\limsup n^2(1-v_p(U_n))\le c_p\pi^2\). Combine with (4) and (2) to finish.

## Verification

The standalone Python standard-library program `verify_signed_shift.py` checks the Young-defect identity, nonnegativity and normalization, the exact \(p=2\) Hilbert radius, odd-dimensional eigenvectors, and the sine recovery energy for selected real exponents and even dimensions. It is finite numerical corroboration, **not** a proof of the infinite limit, the compactness step, or prior-work originality. Reproduce by running `python3 verify_signed_shift.py` alongside this document.

## Relationship to prior work

Chang and Wang [1] study numerical radii of cyclic weighted matrices and permutations of weights, using the complex Hilbert-space numerical radius. Chien and Sheu [2] compute numerical radii for weighted shift matrices and operators on Hilbert space. Chica and Merí [3] study rank-one numerical indices of particular normed planes. These results provide adjacent spectral/numerical-radius context but do not by themselves imply the fixed-\(p\), real Banach-space antiperiodic asymptotic (including its \(p\)-dependent constant). Operator-norm estimates for \(I+U_n\) address a different extremal quantity and are not transferred here without argument.

## Limitations

The proof handles fixed \(1<p<\infty\), real scalars, the specific antiperiodic signed cyclic shift, and the even-dimensional limit. It does not give the exact numerical radius at each finite even \(n\), any uniformity as \(p\to1\) or \(p\to\infty\), or a classification of general signed or weighted shifts. A historically equivalent formulation in Banach-space numerical-radius literature cannot be ruled out solely by the inspected sources.

## References

[1] Chi-Tung Chang and Kuo-Zhong Wang, “Maximizing numerical radii of weighted shifts under weight permutations,” *Journal of Mathematical Analysis and Applications* 394 (2012), 592–602, DOI:10.1016/j.jmaa.2012.04.039.

[2] Mao-Ting Chien and Hue-An Sheu, “The numerical radii of weighted shift matrices and operators,” *Operators and Matrices* 7 (2013), 197–204, DOI:10.7153/oam-07-11.

[3] Mario Chica and Javier Merí, “Rank-1 numerical index of some families of norms on the plane,” *Linear and Multilinear Algebra*, DOI:10.1080/03081087.2014.975670 (available author manuscript).
