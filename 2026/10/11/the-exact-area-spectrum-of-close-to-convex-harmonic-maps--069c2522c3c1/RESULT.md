# The exact area spectrum of close-to-convex harmonic maps

## Finding
Fix \(0\le\alpha<1\) and \(0<r<1\). The set of normalized Euclidean areas \(S_f(r)/\pi\), as \(f\) ranges through the harmonic class \(\mathcal P_{\mathcal H}^0(\alpha)\) defined below, is **exactly**
\[
\boxed{\left[r^2-\frac{(1-\alpha)^2r^4}{2},\quad r^2+4(1-\alpha)^2\bigl(-\log(1-r^2)-r^2\bigr)\right].}
\]
Every value, including both endpoints, is attained by an explicit map in the class. Equality at the **lower** endpoint for one \(r>0\) occurs exactly for the quadratic harmonic shears
\[
 f(z)=z+\overline{\frac{1-\alpha}{2}e^{i\theta}z^2},\qquad\theta\in\mathbb R.
\]
The upper endpoint is attained by an analytic map
\[
 f_+(z)=z+2(1-\alpha)\sum_{n=1}^{\infty}\frac{z^{n+1}}{n+1}
 =\alpha z+(1-\alpha)[-z-2\log(1-z)].
\]
As an additional full-disk consequence, if \(S_f(1)=\lim_{r\uparrow1}S_f(r)\) is allowed to be infinite, the exact set of possible normalized total areas is \([1-(1-\alpha)^2/2,\infty]\). In particular, the least total area is finite and attained, whereas no finite universal upper bound exists.

## Assumptions and scope
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Write \(f=h+\overline g\), where \(h,g\) are holomorphic on \(\mathbb D\), with \(h(0)=g(0)=g'(0)=0\), \(h'(0)=1\), and
\[
 \operatorname{Re}(h'(z)-\alpha)>|g'(z)|\quad\text{for every }z\in\mathbb D.
\]
This is precisely \(\mathcal P_{\mathcal H}^0(\alpha)\). Set \(c=1-\alpha>0\), and put
\[
 S_f(r)=\int_{|z|<r}\left(|h'(z)|^2-|g'(z)|^2\right)\,dx\,dy.
\]
The derivative inequality implies positive Jacobian and injectivity: for distinct points \(w,z\in\mathbb D\), divide their image difference by \(z-w\), integrate the holomorphic derivatives along the line segment, and take real parts. The result is at least the strictly positive segment average of \(\operatorname{Re}h'-|g'|\). Consequently \(S_f(r)\) is the geometric area of \(f(\{|z|<r\})\), with multiplicity one.

## Proof
**Lower bound.** Put \(p=h'-\alpha\) and \(q=g'\). Since \(\operatorname{Re}p>|q|\), the function \(p\) has no zeros, and \(\omega=q/p\) is holomorphic with \(|\omega|<1\) and \(\omega(0)=0\). Schwarz's lemma yields \(|\omega(z)|\le|z|\), hence
\[
 |q(z)|^2\le |z|^2|p(z)|^2.\tag{1}
\]
Write \(h'(z)=1+\sum_{n\ge1}d_nz^n\) and \(p(z)=c+\sum_{n\ge1}d_nz^n\). The angular Parseval identity and (1), for every \(0\le\rho<1\), give
\[
 \frac1{2\pi}\int_0^{2\pi}\!\bigl(|h'(\rho e^{it})|^2-|q(\rho e^{it})|^2\bigr)\,dt
 \ge 1-c^2\rho^2+(1-\rho^2)\sum_{n\ge1}|d_n|^2\rho^{2n}
 \ge1-c^2\rho^2.\tag{2}
\]
Integration against \(2\rho\,d\rho\) from \(0\) to \(r\) proves
\[
 S_f(r)/\pi\ge r^2-c^2r^4/2.\tag{3}
\]
Indeed a coefficient-sensitive refinement follows directly from (2):
\[
 \frac{S_f(r)}\pi-\left(r^2-\frac{c^2r^4}{2}\right)
 \ge\sum_{n\ge1}|d_n|^2\left(\frac{r^{2n+2}}{n+1}-\frac{r^{2n+4}}{n+2}\right).\tag{4}
\]
For \(r>0\), every weight on the right of (4) is strictly positive. Equality in (3) therefore forces every \(d_n=0\), so \(p\equiv c\). Equality in the integrated form of (1) then forces \(|\omega(z)|=|z|\) at a nonzero point, and the equality case of Schwarz's lemma gives \(\omega(z)=e^{i\theta}z\). Thus \(h(z)=z\) and \(g(z)=ce^{i\theta}z^2/2\). Conversely these maps satisfy the strict defining inequality because \(c>c|z|\); their Jacobian is \(1-c^2|z|^2\), giving equality for all radii.

**Upper bound.** For each \(|\lambda|=1\), the holomorphic function \(p+\lambda q\) has positive real part and its value at zero is \(c\). Fourier positivity of its real part (the Carathéodory coefficient estimate) gives \(|d_n+\lambda e_n|\le 2c\), where \(q(z)=\sum_{n\ge1}e_nz^n\). Maximizing over \(\lambda\) gives \(|d_n|+|e_n|\le2c\). Thus \(|d_n|^2-|e_n|^2\le4c^2\). Parseval and radial integration give the exact identity
\[
 \frac{S_f(r)}\pi=r^2+\sum_{n\ge1}\frac{|d_n|^2-|e_n|^2}{n+1}\,r^{2n+2},\tag{5}
\]
which implies
\[
 \frac{S_f(r)}\pi\le r^2+4c^2\sum_{n\ge1}\frac{r^{2n+2}}{n+1}
 =r^2+4c^2[-\log(1-r^2)-r^2].\tag{6}
\]
For the displayed analytic \(f_+\), one has \(g=0\) and \(p(z)=c(1+z)/(1-z)\), so the defining inequality is strict and every coefficient inequality in (6) is an equality. Hence the upper bound is attained.

**No missing area values.** The shear family \(f_t(z)=z+\overline{tc z^2/2}\), \(0\le t\le1\), belongs to the class and realizes every area \(r^2-t^2c^2r^4/2\), filling the interval from the lower endpoint to \(r^2\). Independently, for \(0\le s\le1\) define \(h_s(0)=0\) by
\[
 h_s'(z)=\alpha+c\frac{1+sz}{1-sz},\qquad g_s=0.
\]
These functions belong to the class because the displayed Möbius factor has positive real part on the disk. Their areas are
\[
 \frac{S_{h_s}(r)}\pi=r^2+4c^2\sum_{n\ge1}\frac{s^{2n}r^{2n+2}}{n+1},\tag{7}
\]
continuous and strictly increasing from \(r^2\) at \(s=0\) to the upper endpoint at \(s=1\). Thus the entire closed interval is attained.

**Total area.** The lower bound (3) persists as \(r\uparrow1\). The shear family fills the finite range from \(1-c^2/2\) to \(1\). The analytic family \(h_s\), now with \(0\le s<1\), has finite total area that increases continuously from \(1\) to infinity as \(s\uparrow1\), by the same positive series (7) at \(r=1\). Finally \(h_1=f_+\) has infinite area because its area series is a positive multiple of the harmonic series. This proves the complete extended total-area range.

## Verification
The supplementary standalone checker `verify_area_spectrum.py` performs 120 exact rational coefficient comparisons for quadratic shears and admissible mixed quadratic maps, and numerical comparisons of finite Taylor sums with (7) for several parameters and radii. The all-order theorem and equality classification are proved by (1)–(7); no finite computation substitutes for the proof. Run with a standard Python 3 installation: `python3 verify_area_spectrum.py`.

## Relationship to prior work
Ahamed and Roy, arXiv:2609.08600v1 (first public September 8, 2026), study the identical \(\mathcal P_{\mathcal H}^0(\alpha)\) class. Their equation (2.4) establishes the upper area bound (6), which the present proof reproduces for completeness; their principal theorems are sharp Bohr and Bohr–Rogosinski radius inequalities involving the area. Neither the lower endpoint, the lower equality maps, nor the complete attainable spectrum appears in their inspected text. Li and Ponnusamy (2013, 2016) provide the underlying coefficient and geometric theory of these harmonic classes. Those known coefficient bounds do not, by themselves, yield the exact lower area extremizer: its derivation here uses the analytic quotient \(g'/(h'-\alpha)\), Schwarz's lemma, and the positive Parseval remainder.

## Limitations
Only the indicated normalized class, \(0\le\alpha<1\), and centered disks are covered. The result does not classify areas for arbitrary sense-preserving harmonic univalent maps, unnormalized derivatives, or multiply connected domains. The source's upper bound is not presented as a newly discovered bound. Two earlier relevant original papers were accessible only through summaries or previews, so possible equivalent unindexed prior treatments remain a literature risk. The computational checks are not an infinite proof.

## References
1. M. B. Ahamed and P. P. Roy, *Sharp Bohr and Bohr-Rogosinski inequalities involving area measure for close-to-convex harmonic mappings*, arXiv:2609.08600v1 (September 8, 2026), especially definition (1.5), Lemma A, Theorems 2.1–2.2, equation (2.4) and their proofs. https://arxiv.org/abs/2609.08600
2. L. Li and S. Ponnusamy, *Injectivity of sections of univalent harmonic mappings*, Nonlinear Analysis 89 (2013), 276–283, doi:10.1016/j.na.2013.05.016.
3. L. Li and S. Ponnusamy, *Injectivity of sections of convex harmonic mappings and convolution theorems*, Czechoslovak Mathematical Journal 66 (2016), 331–350, doi:10.1007/s10587-016-0259-9.
