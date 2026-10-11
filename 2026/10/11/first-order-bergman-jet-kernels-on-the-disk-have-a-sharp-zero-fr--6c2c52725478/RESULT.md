# First-order Bergman jet kernels on the disk have a sharp zero-free dichotomy

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and let \(A^2(\mathbb D)\) be the holomorphic Bergman space with ordinary planar area measure. For complex \(a,b\), not both zero, let \(B_{a,b}(z,w)\) be the Hermitian Gram kernel of the evaluation functionals
\[
\Lambda_z^{a,b}f=a f(z)+b f'(z),\qquad f\in A^2(\mathbb D).
\]
Then the exact first-order Lu Qi-Keng classification is
\[
\boxed{B_{a,b}(z,w)\ne0\text{ for all }z,w\in\mathbb D\quad\Longleftrightarrow\quad b=0.}
\]
In particular, the ordinary disk Bergman kernel loses its zero-free property under *every* nonzero first-derivative perturbation, no matter how small.

For \(a b\ne0\), put \(t=|b/a|>0\). After a simultaneous rotation of the two disk variables, zeros arise as limits from the slice \(w\to-1\). Its exact boundary numerator is
\[
P_t(z)=(1+2t)z^2+(2-4t^2)z+(1-2t+2t^2).
\]
Both roots are in \(\mathbb D\) for \(0<t<\sqrt2\); at \(t=\sqrt2\) one is at \(1\) and the other in \(\mathbb D\); for \(t>\sqrt2\), one lies in \((-1,1)\) and the other in \((1,\infty)\). As \(t\downarrow0\), the two boundary-slice roots satisfy
\[
z_\pm(t)=-1+(2\pm i\sqrt2)t+O(t^2).
\]
These latter statements describe the *boundary-limiting polynomial*; they do not claim that \(w=-1\) belongs to \(\mathbb D\).

## Assumptions and scope
The kernel is defined from the Gram family of the indicated **constant-coefficient** first-order differential functionals, using the usual Bergman inner product \(\langle f,g\rangle=\int_{\mathbb D}f\overline g\,dA\). Thus \(B_{a,b}\) is holomorphic in its first variable and antiholomorphic in its second. The parameter pair is any member of \(\mathbb C^2\setminus\{(0,0)\}\). No assumption of real coefficients or restrictions on the evaluation points beyond membership in \(\mathbb D\) is made. The conclusion concerns zeros *off the diagonal* of a positive-definite Gram kernel, not zeros of its nonnegative diagonal.

## Proof
The classical Bergman kernel is
\[
K(z,w)=\frac1{\pi(1-z\overline w)^2}.
\]
For the first-order jet functional, differentiating its reproducing identity gives, with \(x=z\overline w\),
\[
\begin{aligned}
B_{a,b}(z,w)&=|a|^2K(z,w)+b\overline a\,\partial_zK(z,w)
+a\overline b\,\partial_{\overline w}K(z,w)
+|b|^2\partial_z\partial_{\overline w}K(z,w),\\
\partial_zK&=\frac{2\overline w}{\pi(1-x)^3},\qquad
\partial_{\overline w}K=\frac{2z}{\pi(1-x)^3},\\
\partial_z\partial_{\overline w}K&=\frac{2(1+2x)}{\pi(1-x)^4}.
\end{aligned}
\]
If \(b=0\), this is \(|a|^2K\), which never vanishes. If \(a=0\) and \(b\ne0\), the mixed derivative vanishes whenever \(z\overline w=-1/2\); for instance choose \(z=1/\sqrt2\) and \(w=-1/\sqrt2\), both strictly inside the disk.

Now let \(ab\ne0\). Scalar normalization reduces to \(a=1\), \(b=\tau\). Under \((z,w)\mapsto(e^{i\phi}z,e^{i\phi}w)\), the coefficient \(\tau\) is replaced by \(\tau e^{-i\phi}\). Choosing \(e^{i\phi}=\tau/|\tau|\) therefore reduces zero existence to the real case \(\tau=t>0\). There
\[
B_{1,t}(z,w)=\frac{N_t(z,\overline w)}{\pi(1-z\overline w)^4},\quad
N_t(z,v)=(1-zv)^2+2t(z+v)(1-zv)+2t^2(1+2zv).
\]
For \(v=-1\), a limit of permitted values \(v=-r\) with \(r\uparrow1\), direct expansion yields the quadratic \(P_t\) displayed above. Its leading, middle and constant coefficients are respectively
\[
A=1+2t,\qquad B=2-4t^2,\qquad C=1-2t+2t^2.
\]
They obey
\[
P_t(1)=4-2t^2,\quad P_t(-1)=6t^2,\quad A-C=2t(2-t),\quad C=2(t-1/2)^2+1/2>0.
\]
For \(0<t<\sqrt2\), these give \(A>C>0\) and \(P_t(\pm1)>0\). If its two roots are nonreal, they are conjugate and their common squared modulus is \(C/A<1\). If they are real, a root at least \(1\) would, from \(P_t(1)>0\), force both roots to exceed \(1\), contradicting \(C/A<1\). The same argument with \(P_t(-1)>0\) excludes roots at most \(-1\). Thus both roots are strictly inside \(\mathbb D\). At \(t=\sqrt2\), one root is \(1\) and the other equals \(C/A\in(0,1)\). For \(t>\sqrt2\), the inequalities \(P_t(-1)>0>P_t(1)\) give a real root in \((-1,1)\); since \(A>0\), the other root lies in \((1,\infty)\).

Consequently, for *every* \(t>0\), \(P_t\) has at least one root \(z_0\) strictly inside the disk. At such a root \(z_0\ne-1\), the denominator \((1+z_0)^4\) is nonzero. Since polynomial roots depend continuously on the coefficients, for all \(r<1\) sufficiently near \(1\), the numerator \(N_t(z,-r)\) has a root \(z_r\in\mathbb D\) close to \(z_0\). With \(w=-r\in\mathbb D\), its denominator is nonzero because \(|z_r\overline w|<1\), so \(B_{1,t}(z_r,w)=0\). Undoing normalization and rotation proves the equivalence.

Finally the quadratic discriminant is
\[
B^2-4AC=8t^2(2t^2-2t-1).
\]
Its quadratic formula gives \(z_\pm(t)=-1+(2\pm i\sqrt2)t+O(t^2)\) for small positive \(t\). This establishes the stated boundary-slice mechanism and completes the proof.

## Verification
The standalone standard-library script `verify.py` expands the Gram numerator using exact rational polynomial arithmetic and checks the formulas for \(P_t\), its endpoint values, coefficient difference and discriminant as formal identities. It was executed successfully in the package directory. These checks are supporting reproducibility evidence; the infinite-parameter zero-existence conclusion rests on the preceding analytic root-position and continuity argument, not on finite sampling.

## Relationship to prior work
Gehlawat, Jain and Sarkar (arXiv:2608.13193v1) define the canonical positive-definite kernel for general derivative sequences and study its Lu Qi-Keng behavior mainly on the **upper half-plane**. Their Theorem 4.11 establishes zero-freeness there for pure derivative sequences and a particular infinitely supported sequence, and their general reproducing-kernel formulas provide the framework used here. The present result is instead a *complete classification of all constant-coefficient first-order sequences on the disk*, including the surprising failure for arbitrarily small derivative coefficient and the exact boundary-root transition at \(\sqrt2\). The source does not give this disk classification. The half-plane and disk statements do not reduce by a constant-parameter substitution: the source's biholomorphic transformation formula transports a constant jet sequence to a **point-dependent** jet sequence under the nonlinear Cayley map.

## Limitations
The statement is limited to the unweighted classical Bergman space of the **unit disk** and first-order *constant-coefficient* differential functionals. It does not claim an analogous classification for higher jets, weighted Bergman spaces, arbitrary domains, or transported position-dependent jet coefficients. The boundary-limit roots themselves are not kernel zeros at the excluded point \(w=-1\); actual interior zeros follow by perturbing \(w\) inward. No priority over unindexed or independently obtained equivalent literature is claimed.

## References
1. S. Gehlawat, A. Jain, A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the \(\xi\)-Bergman Kernel*, arXiv:2608.13193v1, publicly posted August 13, 2026, especially the Gram construction, Definition 4.3, Theorem 4.11, and transformation formulas in Section 6. https://arxiv.org/abs/2608.13193
2. B. Bao, Q. Guan and Z. Sun, *On the p-Bergman kernel with respect to a functional \(\xi\)*, arXiv:2510.13144v1 (2025), for the functional Bergman kernel setting. https://arxiv.org/abs/2510.13144
3. N. Aronszajn, *Theory of Reproducing Kernels*, Transactions of the American Mathematical Society **68** (1950), 337–404; classical reproducing-kernel framework. The disk formula used above also follows directly by summing the orthogonal monomial basis.
