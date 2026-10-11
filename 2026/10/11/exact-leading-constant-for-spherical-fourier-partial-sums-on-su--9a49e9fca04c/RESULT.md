# Exact leading constant for spherical Fourier partial sums on \(SU(2)\)
## Finding
Let \(H_r\) be the full matrix-coefficient space of the irreducible unitary representation of \(SU(2)\) with highest weight \(r\), so its dimension as a representation is \(r+1\). Let \(P_r\) be the Peter--Weyl orthogonal projection onto \(H_r\), and for every integer \(L\ge 0\) define the canonical low-pass projection
\[
S_L=\sum_{r=0}^L P_r.
\]
With normalized Haar measure,
\[
\|S_L\|_{L^1\to L^1}=\|S_L\|_{L^\infty\to L^\infty}
=\frac{8}{\pi^2}(L+1)+O(\log(L+2)).
\]
Consequently,
\[
\lim_{L\to\infty}\frac{\|S_L\|_{L^1\to L^1}}{L+1}
=\lim_{L\to\infty}\frac{\|S_L\|_{L^\infty\to L^\infty}}{L+1}
=\frac{8}{\pi^2}.
\]
Thus the canonical spherical Peter--Weyl truncation on \(SU(2)\) has an exact leading endpoint amplification constant.

## Assumptions and scope
The group is \(SU(2)\) with Haar probability measure. The cutoff is by highest weight: all irreducible blocks \(H_r\) with \(0\le r\le L\) are retained and all higher blocks are removed. The statement concerns the convolution-operator norms on \(L^1\) and \(L^\infty\); it does not assert a sharp remainder beyond \(O(\log L)\), nor does it treat other compact Lie groups or other spectral orderings.

## Proof
Write \(M=L+1\). For the irreducible of highest weight \(r\), the dimension is \(r+1\) and the character at conjugacy-class angle \(0\le\theta\le\pi\) is
\[
\chi_r(\theta)=\frac{\sin((r+1)\theta)}{\sin\theta}.
\]
Hence the central convolution kernel of \(S_L\) is
\[
K_L(\theta)=\sum_{m=1}^M m\frac{\sin(m\theta)}{\sin\theta}.
\]
For a convolution kernel, the sharp \(L^1\) and \(L^\infty\) operator norms equal its \(L^1\) mass. The normalized Weyl integration formula on \(SU(2)\) therefore gives
\[
\Lambda_M:=\|S_L\|
=\frac2\pi\int_0^\pi
\left|\sum_{m=1}^M m\sin(m\theta)\right|\sin\theta\,d\theta.
\]
The finite trigonometric sum satisfies the exact identity
\[
\sin\theta\sum_{m=1}^M m\sin(m\theta)
=-M\cos(\theta/2)\cos((M+1/2)\theta)
+\frac12\cot(\theta/2)\sin(M\theta).
\]
Set \(w(\theta)=\cos(\theta/2)\) and
\[
I_M=\int_0^\pi w(\theta)\left|\cos((M+1/2)\theta)\right|\,d\theta,
\qquad
J_M=\int_0^\pi \cot(\theta/2)|\sin(M\theta)|\,d\theta.
\]
The reverse triangle inequality yields
\[
\left|\Lambda_M-\frac{2M}\pi I_M\right|\le\frac1\pi J_M.
\]
Since \(\cot(\theta/2)\le2/\theta\), splitting at \(1/M\) and using \(|\sin(M\theta)|\le M\theta\) on the first interval gives
\[
J_M\le 2+2\log(\pi M)=O(\log M).
\]
It remains to average the main oscillation. The absolutely convergent cosine series of \(|\cos x|\) has mean \(2/\pi\) and coefficients \(O(k^{-2})\). Integrating every nonconstant mode against \(w\) by parts gives a contribution \(O((kM)^{-1})\). Summing the modes therefore gives
\[
I_M=\frac2\pi\int_0^\pi\cos(\theta/2)\,d\theta+O(M^{-1})
=\frac4\pi+O(M^{-1}).
\]
Combining the last three displays,
\[
\Lambda_M=\frac{8}{\pi^2}M+O(\log M),
\]
which is the claimed result after \(M=L+1\).

## Verification
The accompanying `verify.py` checks the exact trigonometric identity over a large deterministic grid and independently evaluates the defining absolute integral by midpoint quadrature for several increasing cutoffs. The numerical ratios converge to \(8/\pi^2\). These finite computations are corroborative only; the infinite asymptotic statement is proved by the analytic estimates above.

## Relationship to prior work
Hare's 1997 paper gives the canonical orthogonal decomposition \(L^2(SU(2))=\bigoplus_{r\ge0}H_r\), explicitly identifies \(H_r\) with the matrix-coefficient space of the irreducible representation of degree \(r+1\), and studies Littlewood--Paley block sums and multipliers for this decomposition. Its published metadata records primary MSC 42B25. The paper does not state the endpoint norm asymptotic above.

Giulini and Travaglini (1986) study spherical Dirichlet kernels on compact connected semisimple Lie groups. Their inspected full text proves sharp two-sided order bounds and, in rank one, identifies \(SU(2)\) as the special case where the known upper and lower powers match. It does not state the normalized limit \(8/\pi^2\) or an exact leading coefficient. Meaney (1981) establishes unboundedness criteria for compact-group Lebesgue constants, which is qualitatively weaker than the present quantitative asymptotic.

## Limitations
No claim is made that \(O(\log L)\) is the optimal remainder. A 1986 paper of Dreseler on asymptotics of Bochner--Riesz kernels on compact Lie groups is a plausible terminology-adjacent source for which a complete text comparison was not available; bibliographic and surrounding literature distinguish its Bochner--Riesz kernel analysis from the unsmoothed endpoint constant proved here, but this remains a specific residual originality risk. The result is restricted to the stated highest-weight cutoff on \(SU(2)\).

## References
1. K. E. Hare, *A General Approach to Littlewood-Paley Theorems for Orthogonal Families*, Canadian Mathematical Bulletin 40 (1997), 296--308, DOI 10.4153/CMB-1997-036-1.
2. S. Giulini and G. Travaglini, *Sharp Estimates for Lebesgue Constants on Compact Lie Groups*, Journal of Functional Analysis 68 (1986), 106--116, DOI 10.1016/0022-1236(86)90059-5.
3. C. Meaney, *Unbounded Lebesgue Constants on Compact Groups*, Monatshefte für Mathematik 91 (1981), 119--129, DOI 10.1007/BF01295142.
4. B. Dreseler, *On the Asymptotic of the Bochner--Riesz Kernel on Compact Lie Groups*, Journal of Functional Analysis 68 (1986), 374--387.
