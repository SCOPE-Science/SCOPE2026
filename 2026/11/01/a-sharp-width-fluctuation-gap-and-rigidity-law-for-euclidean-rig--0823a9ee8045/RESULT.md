# A sharp width-fluctuation gap and rigidity law for Euclidean right prisms

## Finding
Let \(d\ge3\), let \(B\subset\mathbb R^{d-1}\) be any full-dimensional compact convex body, and let \(K=B\times[0,H]\subset\mathbb R^d\) with \(H>0\). If \(U\) is uniformly distributed on the Euclidean unit sphere, write \(W=w_K(U)\) for the length of the orthogonal projection of \(K\) onto the line parallel to \(U\). Set \(m=\mathbb E_V w_B(V)>0\), where \(V\) is uniform on \(S^{d-2}\), and put
\[
\eta=\frac{\operatorname{Var}_V(w_B(V))}{m^2},\qquad t=H/m.
\]
Define, with all gamma functions evaluated at positive arguments,
\[
\begin{split}
a&=\frac{\Gamma(d/2)^2}{\Gamma((d-1)/2)\Gamma((d+1)/2)},\\
b&=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\\
p&=\frac{d-1}{d},\quad q=\frac1d,\quad
r=\frac{2\Gamma(d/2)}{d\sqrt\pi\,\Gamma((d-1)/2)},\\
Q&=qa^2-2rab+pb^2,\quad
\tau_d=\frac{pb-ra}{qa-rb},\\
\gamma_d&=\frac{pq-r^2}{Q}-1.
\end{split}
\]
Then \(Q>0\), \(\tau_d>0\), and \(\gamma_d>0\), and the following **exact rigidity identity** holds:
\[
\boxed{\displaystyle
\frac{\operatorname{Var}(W)}{(\mathbb E W)^2}-\gamma_d
=\frac{p\eta+\frac{(qa-rb)^2}{Q}(t-\tau_d)^2}{(a+bt)^2}.}
\tag{1}
\]
Consequently, \(\gamma_d\) is the sharp universal lower bound for the squared coefficient of variation of the random projection width over **all** such right prisms. Equality holds precisely when \(B\) has constant Euclidean width and \(H=\tau_d m\). In particular, noncircular constant-width bases are also extremizers when such bases exist.

In dimension three this becomes
\[
\boxed{\displaystyle
\tau_3=\frac{4-\pi}{\pi-2},\qquad
\gamma_3=\frac{16}{3(\pi^2-4\pi+8)}-1
=0.0056756967189\ldots.}
\tag{2}
\]
Thus every nondegenerate right three-dimensional cylinder or prism has width coefficient of variation at least \(\sqrt{\gamma_3}=0.075337\ldots\), with equality for constant-width planar bases at the displayed height-to-mean-base-width ratio.

The sharp dimension-dependent gap admits the asymptotic laws
\[
\boxed{\displaystyle
\lim_{d\to\infty}\sqrt d\,\tau_d
=\frac{\sqrt{\pi/2}}{\pi-2},\qquad
\lim_{d\to\infty}d^2\gamma_d
=\frac{\pi-3}{2(\pi-2)}.}
\tag{3}
\]

## Assumptions and scope
Widths use Euclidean support functions: \(w_C(u)=h_C(u)+h_C(-u)\), with unit directions sampled using normalized spherical surface measure. The product is orthogonal, not oblique. The base \(B\) need not be symmetric or smooth; even nonsmooth constant-width bases are admitted. The normalization \(m\) is the average base width, *not* its diameter, inradius, or volume radius. Only exact population means and variances are considered. We require \(d\ge3\) and \(H>0\); degenerate height-zero limits are not equality cases.

## Proof
**1. Independent spherical coordinates.** Write \(U=(\sqrt{1-Z^2}\,V,Z)\), where \(Z\in[-1,1]\), \(V\in S^{d-2}\), and \(Z,V\) are independent. The density of \(Z\) is
\[
f_Z(z)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-z^2)^{(d-3)/2}.
\]
Set \(S=\sqrt{1-Z^2}\) and \(T=|Z|\). Additivity of support functions for an orthogonal Cartesian product gives the *exact random-variable identity*
\[
W=S\,w_B(V)+HT.
\tag{4}
\]
Beta integrals yield \(\mathbb ES=a\), \(\mathbb ET=b\), \(\mathbb ES^2=p\), \(\mathbb ET^2=q\), and \(\mathbb EST=r\), with the five explicit constants above. Independence and \(\mathbb E_V w_B^2=m^2(1+\eta)\) imply
\[
\mathbb EW=m(a+bt),\qquad
\mathbb EW^2=m^2\bigl(p(1+\eta)+2rt+qt^2\bigr).
\tag{5}
\]

**2. Unique positive optimizer.** Because \(S\) strictly decreases and \(T\) strictly increases as \(|Z|\) increases, \(\operatorname{Cov}(S,T)=r-ab<0\). Both \(S,T\) have strictly positive variance. Therefore
\[
pb-ra=b\operatorname{Var}(S)-a\operatorname{Cov}(S,T)>0,
\]
\[
qa-rb=a\operatorname{Var}(T)-b\operatorname{Cov}(S,T)>0,
\]
so \(\tau_d>0\). The positive-definite second-moment matrix \(\begin{pmatrix}p&r\\r&q\end{pmatrix}\) has \(pq-r^2>0\), and its adjugate gives \(Q>0\). Exact completion of the square in \(t\) yields
\[
\frac{p+2rt+qt^2}{(a+bt)^2}
=\frac{pq-r^2}{Q}
+\frac{(qa-rb)^2}{Q(a+bt)^2}(t-\tau_d)^2.
\tag{6}
\]
Substituting \(\eta\) in (5) proves (1). For strict positivity of \(\gamma_d\), note that \((pq-r^2)/Q\) equals the reciprocal of the squared \(L^2\)-norm of the orthogonal projection of the constant function \(1\) onto \(\operatorname{span}\{S,T\}\). This squared norm is strictly less than \(1\): the identity \(cS+eT\equiv1\) is impossible on the interval \(0<|Z|<1\). Thus \(\gamma_d>0\). Equation (1) gives the claimed equality cases, and Euclidean-ball bases of any radius realize them. Constant width is equivalent to \(\eta=0\) because the continuous width function on the sphere is almost everywhere constant only when it is everywhere constant.

**3. Dimension three.** For \(d=3\), \(Z\) is uniform on \([-1,1]\), giving \(a=\pi/4\), \(b=1/2\), \(p=2/3\), \(q=r=1/3\). Substitution into (1) gives the exact values in (2).

**4. High-dimensional sharpness.** Let \(Z_d\) be the last coordinate of Haar-uniform \(S^{d-1}\), and \(G\sim N(0,1)\). The moments of \(\sqrt d\,Z_d\) converge to the corresponding Gaussian moments, with uniformly bounded moments of each fixed order. Consequently, in joint moment convergence,
\[
\sqrt d\,T_d\ \longrightarrow\ |G|,\qquad
 d(S_d-1)\ \longrightarrow\ -G^2/2.
\]
The second assertion follows also from \(\sqrt{1-z^2}=1-z^2/2+O(z^4)\), uniformly on \([-1,1]\), together with \(d^2\,\mathbb E Z_d^8=O(d^{-2})\), which controls the squared remainder. It follows from the variance/covariance formulas in step 2 that \(\sqrt d\,\tau_d\) tends to the least-squares regression coefficient of \(G^2/2\) on \(|G|\):
\[
\frac{\operatorname{Cov}(G^2/2,|G|)}{\operatorname{Var}(|G|)}
=\frac{\sqrt{2/\pi}/2}{1-2/\pi}
=\frac{\sqrt{\pi/2}}{\pi-2}.
\]
Since \(\mathbb ES_d+\tau_d\mathbb ET_d\to1\), the normalized minimal variance multiplied by \(d^2\) converges to
\[
\min_{c\in\mathbb R}\operatorname{Var}(c|G|-G^2/2)
=\frac12-\frac{(\sqrt{2/\pi}/2)^2}{1-2/\pi}
=\frac{\pi-3}{2(\pi-2)}.
\]
This proves (3) without assuming an asymptotic normal law for the widths of arbitrary bases.

## Verification
The included standalone `verify.py` performs exact symbolic confirmation of (1) and (2) in dimension three, independent numerical beta-integral evaluations for all dimensions \(3\le d\le30\), tests of (1) away from the optimizer and for positive base-width variance, high-dimensional asymptotic checks, separate one-dimensional integration for an optimal circular cylinder, and a seeded random-direction comparison for a square prism. Execute with `python verify.py` in an environment with NumPy, SciPy, and SymPy. These finite tests corroborate the proof; they do not establish the all-dimensional statements independently of the analytic argument.

## Relationship to prior work
Akiyama and Kamae (2022) systematically study the normalized angular deviation of widths of planar convex polygons and identify sharp polygonal minimizers, including their connection to constant-width bodies. The present theorem uses the same natural fluctuation observable but concerns higher-dimensional **orthogonal products**, allowing arbitrary convex bases and optimizing their height; the dimension-dependent positive gap, complete equality class, exact stability identity, and Gaussian limiting constant are not statements of that work.

An earlier public research note, *Exact mean-square width of every uniform regular prism* (2026), gives a dimension-three second-moment decomposition for a **regular polygonal base at unit height** and a parity-split exact formula. Its elementary product decomposition is compatible with (4). That formula does not alone state or cover the global sharp optimization over all bases and heights or the dimension-asymptotic theorem (3). Dimension-three moments in the present proof are not claimed as new by themselves.

Kabluchko, Litvak, and Zaporozhets (2015) give general Gaussian width-moment identities and study regular cubes, simplices, and crosspolytopes; this is a general computational framework, not the sharp product-prism rigidity theorem. Older stereological and Feret-width terminology could conceal an equivalent sharp inequality; priority is therefore provisional.

## Limitations
The claim does not extend to oblique prisms, arbitrary Minkowski sums, or random two-dimensional shadow areas without new arguments. Exact equality permits all constant-width bases and therefore does not characterize round cylinders. The gap \(\gamma_d\) is dimension dependent and tends to zero; no dimension-independent positive lower bound is asserted. The stability identity is in directional-width \(L^2\) and height normalization, not in Hausdorff distance. Scientific correctness is established by the displayed analytical argument and self-review only; no independent mathematical validation has been performed. Historical priority remains provisional.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, first public 18 January 2022. https://arxiv.org/html/2201.06736v1
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, first public 26 November 2015. https://arxiv.org/html/1511.08479v3
3. *Exact mean-square width of every uniform regular prism*, public note dated 11 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549
