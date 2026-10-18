# Exact radial convexity spectrum of the normalized-arcsine starlike class

## Finding
For \(q(z)=1+\frac{2}{\pi}\arcsin z\), let \(\mathcal S^*_{\arcsin}\) consist of normalized analytic functions \(f(z)=z+O(z^2)\) on the unit disk \(\mathbb D\) such that \(zf'(z)/f(z)=q(\omega(z))\) for a Schwarz function \(\omega(0)=0\) and \(|\omega(z)|<1\). Put \(c=2/\pi\), \(Q(r)=1-c\arcsin r\), \(A(r)=\sqrt{1-r^2}\), and
\[
\Gamma(r)=Q(r)-\frac{cr}{Q(r)A(r)}.
\]
For every \(0<r<1\), the exact (attained) radial order of convexity is
\[
\inf_{f\in\mathcal S^*_{\arcsin}}\ \inf_{|z|=r}\Re\left(1+\frac{zf''(z)}{f'(z)}\right)=\Gamma(r).
\]
The equality cases are exactly the canonical functions defined in the proof, up to rotation of the evaluation point. The function \(\Gamma\) is strictly decreasing from \(1\) to \(-\infty\). Thus, for each real \(\beta<1\), the sharp radius of convexity of order \(\beta\) is the unique \(R_\beta\in(0,1)\) with \(\Gamma(R_\beta)=\beta\). The classical convexity radius is the unique solution
\[
(1-\tfrac2\pi\arcsin R)^2=\frac{2R}{\pi\sqrt{1-R^2}},\qquad R_0=0.538585996535522\ldots.
\]

## Assumptions and scope
The inverse sine is its principal analytic branch on \(\mathbb D\); functions are analytic and normalized at the origin. The real part of \(q\) is strictly positive on \(\mathbb D\), so members are starlike and \(f'\) never vanishes. Convexity order means \(\Re(1+zf''/f')>\beta\) inside the given disk. The statement concerns the entire class, not only its canonical generator, and makes no assertion of convexity for the full unit disk.

## Proof
Write \(w=\omega(z)\), \(|z|=r\), and \(|w|=s\le r\). Because the Maclaurin coefficients of \(\arcsin z\) are nonnegative, \(\Re q(w)\ge Q(s)>0\), \(|q(w)|\ge Q(s)\), and \(|q'(w)|\le c/A(s)\). Schwarz–Pick applied to \(\omega(z)/z\) gives the Dieudonné derivative estimate
\[
|z\omega'(z)|\le s+\frac{r^2-s^2}{1-r^2}=:B_r(s)=\frac{(r^2+s)(1-s)}{1-r^2}.
\]
Differentiating \(zf'/f=q(\omega)\) yields
\[
1+\frac{zf''}{f'}=q(w)+\frac{zq'(w)\omega'(z)}{q(w)}.
\]
Therefore
\[
\Re\left(1+\frac{zf''}{f'}\right)\ge G_r(s):=Q(s)-\frac{cB_r(s)}{Q(s)A(s)}.
\]
We prove the nontrivial monotonicity \(G_r'(s)<0\) for \(0\le s\le r<1\). Set \(q=Q(s)\), \(A=A(s)\), and \(T=c/(qA)+s/A^2\). Direct differentiation gives
\[
G_r'(s)=-\frac{c}{qA}\left(q+B'_r(s)+B_r(s)T\right).
\]
Multiply the bracket by \(1-r^2\) and put \(u=r^2\). The result is affine in \(u\):
\[
H(u)=(1-u)(q+1)-2s+(u+s)(1-s)T,\qquad s^2\le u<1.
\]
The elementary strict inequality \(cA/q>s\) for \(0\le s<1\) follows by differentiating \(h(s)=c(A+s\arcsin s)-s\): \(h(1)=0\) and \(h'(s)=c\arcsin s-1<0\). Hence
\[
H(1)=cA/q-s>0,
\]
and
\[
H(s^2)=A^2(q+1)-2s+scA/q+s^2>(1-s)((1+s)q+1-s)>0.
\]
Affineness implies \(H(u)>0\) throughout the entire interval, proving \(G'_r(s)<0\). Thus the real part is bounded below by \(G_r(r)=\Gamma(r)\).

To attain it at \(z=re^{i\theta}\), choose \(\omega(z)=-e^{-i\theta}z\) and
\[
f_\theta(z)=z\exp\!\left(c\int_0^z\frac{\arcsin(-e^{-i\theta}t)}{t}\,dt\right).
\]
There \(w=-r\), \(q(w)=Q(r)\), \(z\omega'(z)=-r\), and all inequalities are equalities. If equality holds, strict decrease forces \(s=r\), and equality in the Schwarz lemma forces \(\omega(z)=e^{i\phi}z\). The positive-series real-part and derivative bounds, for \(r>0\), then force \(w=-r\), yielding precisely the stated rotations.

Finally \(Q\) and \(A\) decrease strictly, so \(\Gamma\) decreases strictly. As \(r\downarrow0\), \(\Gamma(r)\to1\); as \(r\uparrow1\), \(Q(r)\) tends to zero and \(\Gamma(r)\to-\infty\). The intermediate-value theorem proves the unique radii and sharpness. In fact \(\Gamma(r)\sim-1/[2(1-r)]\) as \(r\uparrow1\), by \(Q(r)\sim (2\sqrt2/\pi)\sqrt{1-r}\).

## Verification
A standalone numerical diagnostic checks the claimed profile against a radial grid and random Dieudonné-admissible complex Schwarz jets; it also computes \(R_0\) by bisection. These finite tests supplement, but do not replace, the analytic proof. Running \(\texttt{python3 check_arcsine.py}\) requires standard Python and SciPy. The full radial result follows from the explicitly proved affine-endpoint monotonicity lemma, not the computation.

## Relationship to prior work
Panja, Banerjee and Majumder introduced the normalized-arcsine starlike class and studied sharp coefficient and Hankel determinant functionals in arXiv:2609.20288. A separate earlier analysis gives the exact convex-leaf image of \(q\) and the associated sharp strong-starlikeness order; those statements alone do not determine the derivative convexity spectrum. Panja, Banerjee, Banerjee and Majumder study a distinct normalized-arcsine **convex class**, defined by subordinating \(1+zf''/f'\) directly, rather than asking for the radius where a starlike-class member becomes convex. Standard Schwarz–Pick/Dieudonné bounds are classical; the specific monotonicity and global sharp radial evaluation above are the claimed additions.

## Limitations
The assertion is confined to this particular class. Historical priority is best-knowledge rather than exhaustive: primary arXiv full texts and some broader radius literature were not obtainable in full, so an earlier general sharp-radius theorem could conceivably imply the result. The numerical approximation is not needed for correctness. No external independent verification is claimed.

## References
1. S. Panja, A. Banerjee, S. Majumder, *Coefficient estimates and Hankel determinant for the class of leaf shaped starlike function*, arXiv:2609.20288v1 (publicly dated 2026-07-29), https://arxiv.org/abs/2609.20288.
2. S. Panja, A. Banerjee, J. Banerjee, S. Majumder, *Coefficient Problems for a Ma-Minda Convex Class Associated with the Normalized Arcsine Mapping*, arXiv:2607.27293, https://arxiv.org/abs/2607.27293.
3. *Exact normalized-arcsine image and sharp strong-starlikeness*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-exact-arcsine-image-sharp-strong-starlikeness--f0dbb9d220ac.
4. B. B. Janani, V. Ravichandran, A. Sebastian, *Ma-Minda convexity and starlikeness for certain subclasses of close-to-starlike functions*, Filomat 40 (2026), https://journal.pmf.ni.ac.rs/filomat/index.php/filomat/article/view/26750.
