# A cusp and complete transverse spectral phase diagram for two touching equilibrium circles

## Finding
For the three-dimensional smooth-away-from-the-axis flow of Sambas et al. (2019), an equilibrium consists of either of two unit-diameter circles touching at the origin. We completely classify, for every \(a,b,c>0\), the number and multiplicities of the points on **each punctured circle** where the two transverse eigenvalues vanish. An explicit universal threshold \(a_*\) and two fold curves enclose a region with four such points per circle, rather than the usual two. The folds coalesce at a cubic cusp. This is a classification of **linear transverse spectra**, not a classification of nonlinear center or attractor stability.

Write
\[
 z_* =\frac{9-\sqrt{33}}4,\qquad u_* =\sqrt{z_*},\qquad
 A(u)=\frac2{\sqrt{1-u^2}}+\frac{6\sqrt{1-u^2}}{u^2},
\]
\[
 a_* = A(u_*)\approx7.816335110265,\qquad
 b_* =\frac{2a_*}{u_*}-\frac{4\sqrt{1-u_*^2}}{u_*^3}
 \approx14.977920882978.
\]
For \(a>a_*\), let \(0<u_-<u_*<u_+<1\) be the two distinct solutions of \(A(u)=a\), and define
\[
 B_a(u)=\frac{2a}{u}-\frac{4\sqrt{1-u^2}}{u^3},\quad
 \beta_{\mathrm{lo}}(a)=B_a(u_+),\qquad
 \beta_{\mathrm{hi}}(a)=B_a(u_-).
\]
Both fold values are strictly positive, and \(\beta_{\mathrm{lo}}(a)<\beta_{\mathrm{hi}}(a)\). The number \(N(a,b)\) of **distinct non-origin equilibrium points** with all three eigenvalues zero on **each** circle is exactly
\[
 N(a,b)=\begin{cases}
 4,&a>a_*,\ \beta_{\mathrm{lo}}(a)<b<\beta_{\mathrm{hi}}(a),\\
 3,&a>a_*,\ b\in\{\beta_{\mathrm{lo}}(a),\beta_{\mathrm{hi}}(a)\},\\
 2,&\text{otherwise}.
 \end{cases}
\]
The ordinary two-point regime has one simple upper-semicircle neutral point and one lower-semicircle neutral point. Inside the four-point regime there are one upper and three lower points. On either fold there is one upper plus two lower points, one lower neutral zero being double along the circle. At \((a,b)=(a_*,b_*)\), the lower point is triple along the circle yet still counts only once; this is the unique cusp. At every such neutral point the smooth Jacobian is a nilpotent \(3\times3\) matrix of index exactly three. Between them, a positive discriminant factor gives one negative and one positive real transverse eigenvalue, and a negative factor gives a purely imaginary transverse pair. The entire diagram is independent of \(c>0\).

For example, \((a,b,c)=(10,20,1)\) lies in the four-point region, while the source's numerical choice \((4,9/2,1)\) lies in the two-point region. No claim is made for the nonsmooth common origin.

## Assumptions and scope
The exact real differential equation is
\[
 \dot x=z,\qquad \dot y=z(-ay-by^2-cxz),\qquad
 \dot z=x^2+y^2-|x|,\qquad a,b,c>0.
\]
An equilibrium has \(z=0\) and \(x^2+y^2=|x|\), hence is on the right circle \((x-1/2)^2+y^2=1/4\) or left circle \((x+1/2)^2+y^2=1/4\). Both include \((0,0,0)\), the nondifferentiable origin, which is **excluded from all Jacobian and counting claims**. Parameterize either circle by
\[
 (x_\pm(\theta),y(\theta),z)=((\pm1+\cos\theta)/2,\sin\theta/2,0),
\]
where \(+\) labels the right circle, \(-\) the left. On the right remove \(\theta=\pi\); on the left remove \(\theta=0\) (equivalently \(2\pi\)). All points counted lie away from these exclusions. An upper/lower point has positive/negative \(y\), respectively. Multiplicity always means the order of the zero of the scalar spectral factor along the \(\theta\) parameter, not the algebraic multiplicity of the Jacobian eigenvalue.

## Proof
**1. Exact transverse factorization.** At any equilibrium with \(x\ne0\), differentiation yields
\[
 J=\begin{pmatrix}
 0&0&1\\0&0&-ay-by^2\\2x-\operatorname{sgn}(x)&2y&0
 \end{pmatrix}.
\]
Direct determinant expansion gives
\[
 \det(\lambda I-J)=\lambda(\lambda^2-Q),\quad
 Q=2x-\operatorname{sgn}(x)-2ay^2-2by^3.
\]
On **both** circles, the identity \(2x-\operatorname{sgn}(x)=\cos\theta\) reduces this to
\[
 Q(\theta)=\cos\theta-\frac a2\sin^2\theta
                 -\frac b4\sin^3\theta.
\]
Thus two real nonzero eigenvalues \(\pm\sqrt Q\) occur when \(Q>0\), while \(Q<0\) gives \(\pm i\sqrt{-Q}\); a zero tangent to the equilibrium curve is always present. At \(Q=0\) the Cayley–Hamilton identity gives \(J^3=0\). Each such point satisfies \(y\ne0\), since any point with \(y=0\) other than the origin is \((\pm1,0,0)\), where \(Q=\pm1\) (with signs interpreted on their respective circles, actually \(Q=-1\) at the outer left end and \(Q=1\) at the outer right end). In either case \(Q\ne0\). The first row of \(J^2\) is \((2x-\operatorname{sgn}(x),2y,0)\), so \(J^2\ne0\). Therefore the nilpotency index is exactly three. The coefficient \(c\) vanishes from the Jacobian at every equilibrium because its contribution is quadratic in \(z\).

**2. Exactly one upper neutral point.** For \(0<\theta<\pi/2\), direct differentiation shows
\[
 Q'(\theta)=-\sin\theta-a\sin\theta\cos\theta
 -\frac{3b}{4}\sin^2\theta\cos\theta<0.
\]
Moreover \(Q(0)=1\) (understood as a one-sided parameter value) and \(Q(\pi/2)=-a/2-b/4<0\). Hence exactly one simple zero occurs in \((0,\pi/2)\). For \(\pi/2<\theta<\pi\), all three terms of \(Q\) are negative, so there are no others above the axis. This proves one upper point per circle for all positive parameters.

**3. Scalar return-to-zero profile below the axis.** On \(\pi<\theta<2\pi\), put \(u=-\sin\theta\in(0,1]\) and \(v=\sqrt{1-u^2}\). Solving \(Q(\theta)=0\) for the positive parameter \(b\) gives
\[
 b=G_a(\theta)=\frac{2a}{u}-\frac{4\cos\theta}{u^3}.
\]
On \(\pi<\theta<3\pi/2\), \(\cos\theta=-v\) and \(G_a=2a/u+4v/u^3\), a strictly decreasing function as \(u\) increases from zero to one. On \(3\pi/2<\theta<2\pi\), \(\cos\theta=+v\), \(u\) decreases from one to zero, and \(G_a=B_a(u)\). The two formulas join smoothly at \(\theta=3\pi/2\), because \(G_a\) is a smooth function of \(\theta\) with \(\sin\theta<0\). Its limits are \(+\infty\) as \(\theta\downarrow\pi\) and \(-\infty\) as \(\theta\uparrow2\pi\); its derivative at \(3\pi/2\) is \(-4\), so \(b=2a\) is not an exceptional counting case.

A direct derivative calculation gives
\[
 B_a'(u)=\frac2{u^2}(A(u)-a),\qquad
 A'(u)=-\frac{2(2u^4-9u^2+6)}{u^3(1-u^2)^{3/2}}.
\]
The quadratic \(2s^2-9s+6\), for \(s=u^2\in(0,1)\), has precisely one root there, \(s=z_*=(9-\sqrt{33})/4\). Therefore \(A\) strictly decreases until \(u_*\), strictly increases thereafter, and tends to \(+\infty\) at both ends. Consequently, if \(a<a_*\) then \(B'_a>0\) everywhere; if \(a=a_*\), its only critical point is a stationary inflection; if \(a>a_*\), there are exactly two nondegenerate critical points \(u_-<u_*<u_+\), with \(B_a\) attaining a local maximum at \(u_-\) and a local minimum at \(u_+\). At any critical point \(a=A(u)\), substitution shows
\[
 B_a(u)=\frac4{u\sqrt{1-u^2}}+\frac{8\sqrt{1-u^2}}{u^3}>0,
\]
so the two fold levels are positive. Their strict order follows from strict decrease of \(B_a\) between its critical points.

As \(\theta\) increases through the lower half-circle, \(G_a\) is strictly decreasing throughout when \(a<a_*\). At equality it is still strictly decreasing but has one cubic-flat inflection. For \(a>a_*\), \(G_a\) decreases from \(+\infty\), reaches the positive local minimum \(\beta_{\mathrm{lo}}\), increases to the positive local maximum \(\beta_{\mathrm{hi}}\), then decreases to \(-\infty\). A horizontal line at height \(b>0\) therefore meets the lower-half profile once, twice (at either fold, with one tangency), or three times (strictly between folds), exactly as stated. Adding the one upper crossing proves \(N(a,b)\) and every endpoint convention.

**4. Multiplicities and cusp.** Since on the lower half \(Q(\theta)=\frac{u^3}{4}(b-G_a(\theta))\) and \(u>0\), a nondegenerate critical point of \(G_a\) produces a **double** zero of \(Q\) along the circle. At \(a=a_*\), \(A'(u_*)=0\) but \(A''(u_*)>0\) because the polynomial above has a simple root and \(A\) changes from decreasing to increasing. Hence \(B_a'\) has a quadratic zero at \(u_*\), \(G_{a_*}(\theta)-b_*\) has a **cubic** zero, and this sole cusp is the point where both fold curves meet. Away from these cases all lower zero crossings are simple. No other degeneracies exist because all derivatives and endpoint behaviors have been exhausted.

**5. Concrete four-point witness.** At \(a=10,b=20\), on the lower-right semicircle the neutral equation is
\[
 \sqrt{1-u^2}-5u^2(1-u)=0.
\]
Its left-hand side equals \(1\) at \(u=0\), is negative at \(u=3/4\) (exactly \(\sqrt7/4-45/64<0\)), and positive at \(u=15/16\) (exactly \(\sqrt{31}/16-1125/4096>0\)). It additionally vanishes at \(u=1\), a simple zero in \(\theta\) because \(Q'(3\pi/2)=1\). Thus there are at least three lower neutral points; Step 3 proves there are at most three. With the upper point there are exactly four, on each circle. The two circles carry distinct neutral points, since their only shared point is the excluded origin.

## Verification
The accompanying `verify.py` is a standalone Python/SymPy checker; run it with `python verify.py` in an environment with SymPy installed. It independently differentiates the vector field, verifies the cubic characteristic polynomial, the identity \(J^3=QJ\), and both derivative factorizations, computes the cusp constants, and counts sign-changing roots for six specified interior parameter examples. It also checks exact rational/sign witnesses for the four-point example. These finite checks are supplementary; exhaustive parameter classifications and the double/cubic multiplicities are proven in Steps 1–4, not inferred from finite sampling.

## Relationship to prior work
Sambas, Vaidyanathan, Tlelo-Cuautle and collaborators introduced this precise vector field and identified its two touching equilibrium circles, using numerical Lyapunov spectra, numerical bifurcation plots and electrical realizations. Their **phase-portrait Lyapunov exponents of trajectories** are not the same object as the **pointwise Jacobian transverse spectra on the equilibrium circles** classified here. The complete positive-parameter fold-cusp and neutral-point count is not stated in that primary paper. Earlier work on single cloud-shaped or single circular equilibrium sets concerns different vector fields; it does not provide this particular two-circle threshold and its parameter-independent simultaneous replication on both circles. Standard nilpotent linear algebra and one-variable saddle-node/cusp calculus are used, not claimed as new. Historical unindexed or equivalent formulations are a residual priority risk.

## Limitations
The common origin is nonsmooth and is expressly excluded. At \(Q<0\), a purely imaginary linear pair **does not prove nonlinear center behavior or Lyapunov stability**; at \(Q=0\), index-three nilpotency **does not by itself establish a nonlinear bifurcation of periodic orbits**. The fold/cusp terms describe the counting diagram of **spectral zero points along a fixed equilibrium manifold**, not creation or destruction of equilibria themselves. We do not establish a global invariant set, basin structure, or the source's reported chaotic windows. No independent mathematical audit has been performed.

## References
Sambas, A.; Vaidyanathan, S.; Tlelo-Cuautle, E.; Zhang, S.; Guillen-Fernandez, O.; Sukono; Hidayat, Y.; Gundara, G. *A Novel Chaotic System with Two Circles of Equilibrium Points: Multistability, Electronic Circuit and FPGA Realization*. Electronics **8** (2019), 1211, published October 23, 2019. DOI: 10.3390/electronics8111211. Open full text: https://www.mdpi.com/2079-9292/8/11/1211 ; archival PDF: https://pdfs.semanticscholar.org/d4f7/68f23a02b4ecae25c86f6f2b7046e7f8e793.pdf . Relevant passages: Sections 1–3, equations (2)–(4), and Section 6.

Vaidyanathan, S.; Sambas, A.; Kaçar, S.; Çavuşoğlu, Ü. *A new three-dimensional chaotic system with a cloud-shaped curve of equilibrium points, its circuit implementation and sound encryption*. International Journal of Modelling, Identification and Control **30** (2018), 184 (identified in the originating paper's reference 10). Different equilibrium curve and vector field.
