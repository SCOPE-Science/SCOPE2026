# A unique one-sided superlocalization point for quadratic cardinal spline projection

## Finding
Let \(B\) be the nonnegative cardinal quadratic B-spline with support \([0,3]\), and let \(P\) be the orthogonal projector in \(L^2(\mathbb R)\) onto the closed span of its integer translates. Its continuous kernel is \(K(x,y)\), as defined below. There is **exactly one** \(x_*\in(0,1)\) at which the exponential decay rate of the kernel in remote intervals to the right changes from \(0.430575347099974\ldots\) to \(0.043096288203264\ldots\).

More precisely, let \(r,s\in(-1/2,0)\) be the two roots inside the unit circle of
\[
Q(z)=z^4+26z^3+66z^2+26z+1,
\qquad 0<|s|<|r|<\tfrac12.
\]
Explicitly, putting \(w_{\pm}=-13\pm\sqrt{105}\),
\[
r=\frac{w_++\sqrt{w_+^2-4}}2,\qquad
s=\frac{w_-+\sqrt{w_-^2-4}}2.
\]
For \(0\le x\le1\), set \(T_m(x)=\sup_{0\le t\le1}|K(x,m+t)|\), with integer \(m\ge3\). Then the unique exceptional point is
\[
x_* = \frac{\sqrt{-r}-r}{1-r}=0.759664811179614\ldots.
\]
For each \(x\in[0,1]\setminus\{x_*\}\),
\[
\lim_{m\to\infty}\frac{T_m(x)}{|r|^{m-2}}
=\frac{1+r}{2}\,A|F_r(x)|>0,
\qquad A=\frac{120r}{Q'(r)}>0,
\]
where \(F_z(x)=B(x)+zB(x+1)+z^2B(x+2)\). At the exceptional point there is instead an **exact, all-cells identity**
\[
T_m(x_*)=\frac{1+s}{2}\,|C F_s(x_*)|\,|s|^{m-2}
\quad(m\ge3),\qquad C=\frac{120s}{Q'(s)}<0.
\]
In particular, \(\lim_{m\to\infty}T_m(x)^{1/m}\) equals \(|r|\) everywhere except at \(x_*\), where it equals \(|s|\). The ratio of the two decay bases is about \(9.9910\). Reflection gives a corresponding unique left-hand exceptional site \(1-x_*\) in the same unit cell. This is one-sided superlocalization: no two-sided improvement is asserted.

## Assumptions and scope
The normalized quadratic cardinal spline is
\[
B(u)=\begin{cases}
 u^2/2,&0\le u\le1,\\
-u^2+3u-3/2,&1\le u\le2,\\
(3-u)^2/2,&2\le u\le3,\\
0,&\text{otherwise}.
\end{cases}
\]
Its translates \(B_j(u)=B(u-j)\), \(j\in\mathbb Z\), generate the closed shift-invariant spline space \(V\subset L^2(\mathbb R)\). The Gram convolution has strictly positive Fourier symbol, hence these translates form a Riesz basis of \(V\). Its inverse convolution is denoted \(h_k\), \(k\in\mathbb Z\), and
\[
K(x,y)=\sum_{j,k\in\mathbb Z}B(x-j)h_{j-k}B(y-k).
\]
The series converges absolutely for fixed \(x,y\), and represents \(P\). The theorem concerns the kernel's remote-right *cell suprema*, not the global \(L^\infty\) norm of \(P\). All scalar values, exponents, ranges, and normalization follow these definitions.

## Proof
**Gram inversion.** Direct piecewise integration yields
\[
g_0=\int B^2=\frac{11}{20},\quad
g_{\pm1}=\frac{13}{60},\quad
g_{\pm2}=\frac1{120},\quad g_j=0\ (|j|>2).
\]
On the unit circle its symbol is
\[
g(z)=\frac{z^{-2}}{120}Q(z).
\]
Writing \(c=\cos\theta\in[-1,1]\), its symbol satisfies \(g(e^{i\theta})=(c^2+13c+16)/30\ge2/15\). Thus the Gram operator is boundedly invertible, and its inverse coefficients exist and decay exponentially. For \(k\ge0\), the contour formula and residues at the two simple roots inside the unit circle give
\[
h_k=\frac1{2\pi i}\oint_{|z|=1}\frac{120z^{k+1}}{Q(z)}\,dz
=Ar^k+Cs^k,\quad A=\frac{120r}{Q'(r)},\quad C=\frac{120s}{Q'(s)}.
\]
Symmetry gives \(h_{-k}=h_k\). The quartic becomes \(w^2+26w+64\) after division by \(z^2\) and substitution \(w=z+z^{-1}\), yielding exactly the roots displayed above; in particular \(-1/2<r<s<0\), \(A>0\), and \(C<0\).

**An exact two-mode tail.** For \(x\in[0,1]\), only \(B(x-j)\) with \(j=-2,-1,0\) can be nonzero. For \(y=m+t\) with \(m\ge3\) and \(t\in[0,1]\), only \(B(y-k)\) with \(k=m-2,m-1,m\) can be nonzero. Thus \(k-j\ge1\), and the inverse Gram formula gives the exact identity
\[
K(x,m+t)= A F_r(x)r^{m-2}\Phi_r(t)
+C F_s(x)s^{m-2}\Phi_s(t),
\]
where
\[
\Phi_z(t)=z^2B(t)+zB(t+1)+B(t+2)
=\frac{(1-z)^2t^2}{2}-(1-z)t+\frac{1+z}{2}.
\]
This is an identity on every stated cell, not an asymptotic approximation.

**Unique cancellation and sharp rates.** On \([0,1]\), the spline pieces give
\[
2F_z(x)=(1-z)^2x^2+2z(1-z)x+z(1+z).
\]
Its roots are \((\pm\sqrt{-z}-z)/(1-z)\). For \(-1/2<z<0\), the negative-sign root is strictly negative and the positive-sign root lies strictly in \((0,1)\). Therefore \(F_r\) vanishes on \([0,1]\) only at \(x_*\). The positive root increases strictly with \(\sqrt{-z}\), so \(F_s(x_*)>0\) because \(|s|<|r|\). Both residues are nonzero.

For each \(z\in\{r,s\}\), the quadratic \(\Phi_z\) is strictly convex, with minimum \(z/2\), endpoint values \((1+z)/2\) and \(z(1+z)/2\), and hence
\[
\max_{t\in[0,1]}|\Phi_z(t)|=(1+z)/2.
\]
For \(x\ne x_*\), division of the two-mode identity by \(|r|^{m-2}\), with a possible alternating sign, converges uniformly in \(t\) in absolute value to \(A|F_r(x)\Phi_r(t)|\); taking suprema proves the first limit. At \(x=x_*\) the first term vanishes identically and the same elementary maximum gives the exact formula for every \(m\ge3\). Reflection of the symmetric spline Gram and kernel establishes the left-hand counterpart.

## Verification
The accompanying standalone `checker.py` numerically reconstructs the three Gram entries by independent quadrature, verifies the inverse Gram convolution and an independent finite Toeplitz inverse, and compares the exact two-mode identity against direct kernel sums at multiple evaluation points and cells. It also checks the exceptional-point cell-supremum identity and the generic asymptotic rate. It passed 297 assertions in the recorded run. These finite checks are supplementary; all infinite and uniqueness statements are proved above.

## Relationship to prior work
Shadrin's proof of de Boor's conjecture gives mesh-independent boundedness of spline orthogonal projectors, and Passenbrunner–Shadrin give exponential inverse-Gram/kernel estimates and local convergence for arbitrary knots. Demko gives general exponential inverse-band decay. These theorems supply the operator-theoretic setting and broad localization framework, but the statements inspected do not identify a unique within-cell cancellation of the dominant inverse-Gram mode, nor the resulting strictly faster exact one-sided decay rate. The explicit mode computation here depends on the special cardinal quadratic Gram symbol; it should not be attributed to those general theorems.

## Limitations
This is a special exact directional kernel theorem, not an estimate for every knot mesh, a proof of optimal global spline projection norm, or a new general inverse-band theorem. The exceptional evaluation site improves only the right-hand tail; the reflected left tail still has generic decay. The asymptotic equivalences hold for fixed evaluation point as remote cell index tends to infinity. Historical priority under alternate cardinal-spline terminology remains a risk; some relevant older full texts were inaccessible, and no independent literature audit has been performed.

## References
1. M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824 (first posted 2013-08-22), especially Theorem 1.2 and the kernel estimate (1.8). https://arxiv.org/abs/1308.4824
2. A. Yu. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, Acta Math. 187 (2001), 59–137. https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/spn0.pdf
3. S. Demko, *Inverses of band matrices and local convergence of spline projections*, SIAM J. Numer. Anal. 14 (1977), 616–619. https://doi.org/10.1137/0714041
4. C. de Boor, *On the (bi)infinite case of Shadrin's theorem concerning the \(L^\infty\)-boundedness of the \(L^2\)-spline projector*, Trudy Inst. Mat. Mekh. UrO RAN 17(3) (2011), 24–29. https://geodesic.mathdoc.fr/item/TIMM_2011_17_3_a4/
