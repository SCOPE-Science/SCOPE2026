# Exact-degree spherical sampling on a doubly wound Clifford circle

## Finding

Write the unit three-sphere as \(S^3=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^2=1\}\). For every integer \(N\ge2\), put \(\zeta_N=e^{2\pi i/N}\) and
\[
X_N=\left\{2^{-1/2}(\zeta_N^j,\zeta_N^{2j}):0\le j<N\right\}.
\]
These are \(N\) distinct points on the equal-radius Clifford torus; they lie on its circle of winding numbers \((1,2)\). Let \(E_{N,\ell}:\mathcal H_\ell(S^3)\to\mathbb C^{X_N}\) evaluate every complex spherical harmonic of **exactly** degree \(\ell\ge0\), not all harmonics up to that degree.

Define the following finite integer-frequency sets:
\[
\begin{aligned}
S_0&=\{0\},\\
S_1&=\{-2,-1,1,2\},\\
S_2&=\{-4,-3,-2,-1,1,2,3,4\},\\
S_4&=\{-8,-7,-6,-5,-4,-2,-1,0,1,2,4,5,6,7,8\},\\
S_\ell&=\{-2\ell,-2\ell+1,\ldots,2\ell\}\quad(\ell=3\text{ or }\ell\ge5).
\end{aligned}
\]
**The exact all-degree sampling rank is**
\[
\boxed{\operatorname{rank}_{\mathbb C}E_{N,\ell}
=\#\{k\bmod N:k\in S_\ell\}.}
\]
In particular, for \(\ell=3\) or \(\ell\ge5\),
\[
\boxed{\operatorname{rank}E_{N,\ell}=\min\{N,4\ell+1\}.}
\]
The only exceptional continuous Fourier frequencies are the missing zero frequency in degrees one and two, and the missing frequencies \(\pm3\) in degree four. Degree four can have **lower rank than degree three**: at \(N=6\) the exact-degree ranks for degrees three, four, five are \(6,5,6\), while at \(N=12\) they are \(12,10,12\). Thus surjective interpolation need not persist from one degree to the next.

For completeness, the exceptional ranks can also be written without modular set notation. Degree zero has rank one. In degree one the rank is two for \(N=2,3\), three for \(N=4\), and four for \(N\ge5\). In degree two it is \(N\) for \(2\le N\le4\), \(N-1\) for \(5\le N\le8\), and eight for \(N\ge9\). In degree four it is \(N\) for \(2\le N\le5\), five for \(N=6\), \(N\) for \(7\le N\le11\), \(N-2\) for \(12\le N\le17\), and fifteen for \(N\ge18\).

## Assumptions and scope

The sphere has unit Euclidean radius and the two complex coordinates have equal modulus \(1/\sqrt2\) on the sampled circle. Harmonic degree means the eigenvalue \(\ell(\ell+2)\) of the positive scalar Laplace–Beltrami operator on \(S^3\). Evaluation is complex linear. The assertion is for every integer pair \(N\ge2\), \(\ell\ge0\), including small cyclic orders where continuous Fourier frequencies alias modulo \(N\). No generic-position or random-sampling assumption is made. The statement is about rank only; it does not assert frame bounds or numerical conditioning.

## Proof

**1. Scalar harmonic weights.** In Hopf coordinates \(z_1=\cos\alpha\,e^{i\phi_1}\), \(z_2=\sin\alpha\,e^{i\phi_2}\), a scalar harmonic of degree \(\ell\) and torus weight \((a,b)\in\mathbb Z^2\) exists if and only if
\[
|a|+|b|\le\ell,\qquad \ell-|a|-|b|=2s\quad(s\in\mathbb Z_{\ge0}).
\]
Each allowed weight space is one-dimensional. Up to a nonzero normalization, its restriction to \(\alpha=\pi/4\) is the circle character
\[
e^{i(a+2b)t}\,P_s^{(|a|,|b|)}(0),
\]
where \(P_s^{(A,B)}\) denotes the Jacobi polynomial. Interchanging \(A,B\) changes this value only by a sign \((-1)^s\), so the zero criterion is independent of Hopf-coordinate convention. Consequently, the continuous restriction image is spanned by exactly the characters indexed by
\[
T_\ell=\left\{a+2b: |a|+|b|\le\ell,\ \ell-|a|-|b|=2s\ge0,\ P_s^{(|a|,|b|)}(0)\ne0\right\}.
\]
The Jacobi identity used throughout is
\[
2^s P_s^{(A,B)}(0)
=\sum_{j=0}^s(-1)^{s-j}\binom{s+A}{j}\binom{s+B}{s-j}.
\]
In particular \(P_0^{(A,B)}(0)=1\), \(P_1^{(A,B)}(0)=(A-B)/2\), and
\[
P_2^{(A,B)}(0)=\big((A-B)^2-A-B-4\big)/8.
\]

**2. Frequencies outside the central band.** Every integer \(k\) with \(\ell\le k\le2\ell\) occurs at the boundary weight \((a,b)=(2\ell-k,k-\ell)\), which has \(a,b\ge0\), \(a+b=\ell\), and \(s=0\). Negative frequencies follow by conjugation. Hence the only question is \(0\le k<\ell\). No frequency has absolute value greater than \(2\ell\), by \(|a+2b|\le2(|a|+|b|)\).

**3. The central band.** For any \(m=\ell-2s\ge0\), the weight \((a,b)=(m-j,-j)\) for integer \(0\le j\le m\) has frequency \(k=m-3j\), while \((a,b)=(-(m-j),j)\) has frequency \(k=-m+3j\). For \(s=0\) all such weights survive. For \(s=1\) the first choice has nonzero Jacobi value \((m+2k)/6\) whenever \(m>0\) and \(k\ge0\), while the second has value \((m-2k)/6\) and can vanish only at \(k=m/2\). For \(s=2\) the first choice, with \(m=3h\) and \(k=3r\), has Jacobi numerator \((h+2r)^2-3h-4\).

If \(\ell\equiv2\pmod3\), all central residues \(k\equiv\pm1\pmod3\) occur already at \(s=0\). The remaining multiples of three occur at \(s=1\), with \(m=\ell-2\) and the nonvanishing first choice. The exception \(\ell=2,k=0\) vanishes because then \(m=0\) and \(P_1^{(0,0)}(0)=0\). For \(\ell\ge5\) this argument has no gap.

If \(\ell\equiv0\pmod3\), the residue-zero central frequencies occur at \(s=0\). Put \(m=\ell-2\equiv1\pmod3\). Frequencies in the other two residue classes occur at \(s=1\), using respectively the first and second mixed-sign choices. The second choice can vanish only at \(k=m/2\), which is integral exactly when \(\ell=6t\) for positive integer \(t\). That exceptional frequency is restored at \(s=2\), where \(m'=\ell-4=6t-4\), \(k=3t-1\), and the first choice has
\[
8P_2^{(A,B)}(0)=(4t-2)^2-6t
=16t^2-22t+4\ne0.
\]
The quadratic has discriminant \(228\), which is not a square, hence no positive integral zero. Frequencies \(k=m\) and \(k=m+1=\ell-1\) at the top edge of this central range are covered by the same-sign \(s=1\) weights, with nonzero values (also for \(\ell=3\)). Thus no central frequencies are missing.

If \(\ell\equiv1\pmod3\), the residue classes \(\pm1\) occur at \(s=0\). For central multiples \(k=3r\) put \(m=\ell-4=3h\). When \(0\le k\le m\), the \(s=2\) first mixed-sign choice vanishes only if
\[
(h+2r)^2=3h+4,\qquad0\le r\le h.
\]
For \(h\ge5\) the left side exceeds the right; for \(0\le h\le4\), direct substitution leaves only \((h,r)=(4,0)\). This is \(\ell=16,k=0\), which is restored at \(s=5\) by \((a,b)=(-4,2)\), since \(2^5P_5^{(4,2)}(0)=42\ne0\). The sole remaining possible multiple of three within \(k<\ell\) is \(k=m+3=\ell-1\). For \(h\ge1\) it occurs at same-sign \(s=2\) weight \((a,b)=(m-3,3)\) and does not vanish: its Jacobi numerator is \(9h^2-39h+32\), whose discriminant \(369\) is not a square. When \(h=0\) (degree four), the frequency three cannot occur. Direct examination of degrees zero and one completes the finite initial cases.

These cases prove \(T_\ell=S_\ell\) for every \(\ell\ge0\), with exactly the announced holes.

**4. Cyclic sampling.** At \(t_j=2\pi j/N\), two continuous characters \(e^{ikt}\) and \(e^{ik't}\) have identical sample vectors exactly when \(k\equiv k'\pmod N\). The distinct residue-class vectors are orthogonal and nonzero. Hence the evaluation image has dimension \(\#(T_\ell\bmod N)\), proving the main rank formula. In full-interval degrees this equals \(\min\{N,4\ell+1\}\). Direct counting of the three finite exceptional sets gives the displayed piecewise ranks.

## Verification

A separate arithmetic route uses the \(S^3\) addition theorem: up to a strictly positive degree-dependent factor, the evaluation Gram kernel is
\[
U_\ell\left(\frac{\cos t+\cos2t}{2}\right),
\]
where \(U_\ell\) is the Chebyshev polynomial of the second kind. Its exact Laurent coefficients satisfy
\[
Q_0(z)=1,\quad Q_1(z)=z^2+z+z^{-1}+z^{-2},\quad
Q_\ell(z)=(z^2+z+z^{-1}+z^{-2})Q_{\ell-1}(z)-4Q_{\ell-2}(z),
\]
with \(Q_\ell=2^\ell U_\ell((\cos t+\cos2t)/2)\), \(z=e^{it}\). They are nonnegative because the kernel is a sum of squared harmonic matrix coefficients. The standalone standard-library checker `check.py` compares the exact positive Laurent support to independently evaluated Jacobi weight support and to \(S_\ell\) for degrees zero through sixty, and checks cyclic ranks for orders two through sixty-four. The checker is finite corroboration, not the proof of the infinite classification.

## Relationship to prior work

Explicit scalar \(S^3\) harmonics in Hopf coordinates and their Jacobi-polynomial factors are reviewed in Ben Achour, Huguet, Queva and Renaud, *Explicit vector spherical harmonics on the 3-sphere*, Section II, arXiv:1505.03426 (first posted 13 May 2015). McEwen and Wiaux, *A novel sampling theorem on the sphere*, arXiv:1110.6298 (posted 28 October 2011), analyze full bandlimited transforms on \(S^2\) via a toroidal periodic extension. Neither work presents the exact-degree evaluation ranks of this fixed, doubly wound circle on \(S^3\). In particular, the Jacobi separation formula alone does not list the degree-four missing frequencies or derive the all-degree support completeness. The present calculation uses those standard harmonic bases but addresses a distinct rank/interpolation question.

## Limitations

This is a rank theorem, not a stable-reconstruction theorem: singular values, conditioning, noise robustness, and optimality among other sampling curves are not determined. It concerns the fixed \((1,2)\) winding and equal-radius Clifford torus only; other winding numbers and radii can have different Fourier holes. Literature comparison was bounded and cannot exclude an equivalent older formulation, especially in representation-theoretic accounts of \(S^3\) harmonics. No independent mathematical validation is claimed.

## References

1. J. Ben Achour, E. Huguet, J. Queva, J. Renaud, *Explicit vector spherical harmonics on the 3-sphere*, arXiv:1505.03426, version first publicly posted 2015-05-13, Section II (scalar Hopf/Jacobi basis). https://arxiv.org/abs/1505.03426
2. J. D. McEwen, Y. Wiaux, *A novel sampling theorem on the sphere*, arXiv:1110.6298, first publicly posted 2011-10-28, Sections III–IV (harmonic sampling and toroidal periodic extension on the two-sphere). https://arxiv.org/abs/1110.6298
