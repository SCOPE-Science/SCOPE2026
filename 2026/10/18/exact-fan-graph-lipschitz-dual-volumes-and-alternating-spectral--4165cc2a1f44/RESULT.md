# Exact fan-graph Lipschitz-dual volumes and alternating spectral growth

## Finding
For each integer \(n\ge2\), consider the unit-edge fan graph \(F_n=K_1\vee P_n\) with one hub \(h\) and path vertices \(v_1,\ldots,v_n\). Write \(M_n\) for its shortest-path metric and anchor real-valued functions at \(h\). The unit ball of \(\operatorname{Lip}_0(M_n)=\mathcal F(M_n)^*\) is
\[
Q_n=\bigl\{x\in[-1,1]^n:\ |x_i-x_{i+1}|\le1\text{ for }1\le i<n\bigr\}.
\]
Let \(V_n=\operatorname{vol}_n(Q_n)\) be **anchored-coordinate Lebesgue volume**, not intrinsic Euclidean volume in the zero-sum hyperplane. Include the natural auxiliary value \(Q_1=[-1,1]\) and \(V_1=2\). Then for \(|z|<\alpha\), where \(\alpha=2\arctan(1/3)\), the complete volume generating function is
\[
\boxed{\sum_{n\ge1}V_nz^{n-1}=
\frac{4\sin(z/2)}{z\bigl(\cos(z/2)-3\sin(z/2)\bigr)}.}
\]
It has a globally absolutely convergent exact pole expansion for every integer \(n\ge1\):
\[
\boxed{V_n=\frac45\sum_{j\in\mathbb Z}\frac1{\bigl(\alpha+2\pi j\bigr)^{n+1}}.}
\]
In particular, \(V_1=2\), \(V_2=3\), \(V_3=14/3\), \(V_4=29/4\), and \(V_5=169/15\). All volumes are positive rational numbers.

The spectral formula implies an exact oscillation of successive-volume ratios around their limiting growth constant:
\[
\boxed{(-1)^n\left(\frac{V_{n+1}}{V_n}-\frac1\alpha\right)>0\quad(n\ge1),\qquad
\lim_{n\to\infty}\frac{V_{n+1}}{V_n}=\frac1{2\arctan(1/3)}=1.5539988763581694\ldots.}
\]
Thus odd-indexed ratios are below the limit and even-indexed ratios are above it, **in every dimension**, rather than merely asymptotically. More precisely,
\[
V_n=\frac4{5\alpha^{n+1}}\left[1+(-1)^{n+1}\left(\frac{\alpha}{2\pi-\alpha}\right)^{n+1}
+O\left(\left(\frac{\alpha}{2\pi+\alpha}\right)^{n+1}\right)\right].
\]

## Assumptions and scope
All edges of \(F_n\) have length one, and distances are shortest-path distances. Every hub edge gives \(|x_i|\le1\). Every path edge gives \(|x_i-x_{i+1}|\le1\); other pairwise Lipschitz inequalities follow from paths of edges and the triangle inequality. We use the coordinate basis \((\delta(v_1),\ldots,\delta(v_n))\) of the free space and its dual evaluation coordinates \(x_i=f(v_i)\), with \(f(h)=0\). The lattice and Lebesgue measure are those of \(\mathbb Z^n\subset\mathbb R^n\); no assertion of Euclidean-coordinate or Banach-isometry invariance of unnormalized volume is made. The case \(n=1\) is included only to seed the generating function and the transfer recursion.

## Proof
**1. Graph identification and transfer operator.** By the preceding constraints, \(Q_n\) is precisely the Lipschitz unit ball. Put \(H=L^2([-1,1])\), let \(\mathbf1\) be the constant-one function, and define the bounded, self-adjoint compact operator
\[
(Tf)(x)=\int_{-1}^{1}\mathbf1_{\{|x-y|\le1\}}f(y)\,dy.
\]
Fubini's theorem, applied to the chain of adjacent constraints, gives
\[
V_n=\langle\mathbf1,T^{n-1}\mathbf1\rangle_H\quad(n\ge1).
\]
For \(|z|<\|T\|^{-1}\), set \(u=(I-zT)^{-1}\mathbf1\), so \(u=1+zTu\) and
\[
\sum_{n\ge1}V_nz^{n-1}=\int_{-1}^{1}u(x)\,dx.
\]
Reflection invariance makes \(u\) even. For \(0\le x\le1\), the kernel condition is \(x-1\le y\le1\), giving
\[
u(x)=1+z\int_0^1u(y)\,dy+z\int_0^{1-x}u(y)\,dy.
\]
Consequently \(u'(x)=-zu(1-x)\) and \(u''(x)=-z^2u(x)\). Also the two endpoint identities are
\[
u(0)=2u(1)-1,\qquad u'(0)=-zu(1).
\]
For nonzero small \(z\), write \(u(x)=A\cos(zx)+B\sin(zx)\). The derivative identity gives \(B=-u(1)\), and the first endpoint identity gives \(A=2u(1)-1\). Substituting into \(u(1)\) yields
\[
A=\frac{1+\sin z}{2\cos z-1-\sin z}
=\frac{1+\tan(z/2)}{1-3\tan(z/2)}.
\]
At \(x=0\), the resolvent equation says \(A=u(0)=1+z\int_{-1}^{1}u\). Hence
\[
\sum_{n\ge1}V_nz^{n-1}=\frac{A-1}{z}
=\frac{4\tan(z/2)}{z(1-3\tan(z/2))}
=\frac{4\sin(z/2)}{z(\cos(z/2)-3\sin(z/2))}.
\]
The singularity at \(z=0\) is removable, with value \(2\). Analytic continuation extends this identity through its maximal disk about zero, whose closest nonremovable singularity is at \(z=\alpha\).

**2. Exact pole expansion.** Put \(\alpha=2\arctan(1/3)\in(0,\pi)\), and define \(a_j=\alpha+2\pi j\) for every \(j\in\mathbb Z\). The elementary cotangent subtraction identity gives
\[
\cot\left(\frac{\alpha-z}{2}\right)-3
=\frac{10\tan(z/2)}{1-3\tan(z/2)}.
\]
Use the classical symmetric partial-fraction expansion of the cotangent, with its value at \(z=0\) subtracted:
\[
\cot\left(\frac{\alpha-z}{2}\right)-\cot\left(\frac\alpha2\right)
=2\sum_{j\in\mathbb Z}\left(\frac1{a_j-z}-\frac1{a_j}\right).
\]
The differences in this series converge absolutely and locally uniformly away from the poles: their terms are \(O(j^{-2})\). Since \(\cot(\alpha/2)=3\), the previously derived generating function becomes
\[
G(z)=\frac45\sum_{j\in\mathbb Z}\frac1{a_j(a_j-z)}
=\frac45\sum_{j\in\mathbb Z}\frac1{a_j^2}\frac1{1-z/a_j},\quad |z|<\alpha.
\]
Uniform convergence in compact subdisks allows coefficient extraction term by term, giving the claimed formula \(V_n=(4/5)\sum_j a_j^{-(n+1)}\). Absolute convergence is immediate since the exponent \(n+1\ge2\). Rationality of every \(V_n\) also follows independently by repeated integration of rational-coefficient polynomials in the recursion described under Verification.

**3. Strict alternating ratio inequalities.** Since \(0<\alpha<\pi\), \(a_0=\alpha\) is the unique pole of smallest absolute modulus, and the next is \(a_{-1}=\alpha-2\pi<0\). Write
\[
V_n=\frac4{5\alpha^{n+1}}(1+\varepsilon_n),\qquad
\varepsilon_n=\sum_{j\ne0}\left(\frac\alpha{a_j}\right)^{n+1}.
\]
When \(n\) is odd, the exponent \(n+1\) is even and every summand is strictly positive, so \(\varepsilon_n>0\). When \(n\) is even, the exponent is odd; pairing the terms for \(j=k\) and \(j=-k\), \(k\ge1\), gives
\[
\left(\frac\alpha{\alpha+2\pi k}\right)^{n+1}
-\left(\frac\alpha{2\pi k-\alpha}\right)^{n+1}<0,
\]
so \(\varepsilon_n<0\). Every factor \(1+\varepsilon_n\) is positive because \(V_n\) is the strictly positive volume of a full-dimensional convex body. Thus
\[
\frac{V_{n+1}}{V_n}=\frac1\alpha\frac{1+\varepsilon_{n+1}}{1+\varepsilon_n}.
\]
The numerator correction and denominator correction have opposite strict signs, which proves \((-1)^n(V_{n+1}/V_n-1/\alpha)>0\) for every \(n\ge1\). Absolute convergence and uniqueness of the smallest-modulus pole imply \(\varepsilon_n\to0\). Isolating the \(j=-1\) term, and bounding the remaining paired tails geometrically uniformly in \(n\ge1\), gives the stated exponential correction with sign \((-1)^{n+1}\).

## Verification
The included standalone Python 3 program `verify.py` uses only the standard library. It computes \(V_n\) in two independent exact ways: (a) successive integration of a polynomial on \([0,1]\) via the reflection-symmetric transfer recursion, and (b) finite differences of integer lattice-point counts for the integral polytopes \(Q_n\) via Ehrhart's leading-coefficient theorem. Every vertex of \(Q_n\) is integral: at a vertex the graph of constraints tight at equality must connect all vertices to the anchored hub (otherwise a component can vary); therefore a tight spanning tree of unit edges makes every anchored potential an integer. Equivalently, the rooted edge-incidence constraint matrix is totally unimodular. The two computations agree exactly for \(1\le n\le12\), and all polynomial integrals were computed exactly through \(n=16\). The code also checks 14 strict alternating-ratio inequalities and 10 numerical evaluations of the absolutely convergent spectral sum. The infinite statements rest on the analytic proof, not on finite computation.

## Relationship to prior work
Aliaga (arXiv:2102.01219, first publicly available 2021-02-01; primary MSC 46B20) gives the Lipschitz-free space framework and establishes extreme-point results for compact metric spaces, but does not calculate this fan-graph anchored volume sequence. Alexander, Fradelizi, García-Lirola, and Zvavitch (arXiv:1911.10642) study geometry and volume products of finite-dimensional Lipschitz-free spaces, including equilateral benchmarks, but their inspected results do not determine the present fan family. Sanyal and Stump (arXiv:1703.10586) analyze oriented Lipschitz polytopes of partially ordered sets; their cover inequalities are \(0\le f(b)-f(a)\le1\), whereas the present metric constraints are symmetric absolute differences around triangular fan cycles. Their poset volume formulas do not yield this generating function as a stated special case. A general toric-volume algorithm for polytropes (arXiv:2006.01920) could in principle evaluate individual finite cases but supplies neither this all-dimensional meromorphic generating function nor the strict alternating-ratio law. Published fan-graph symmetric-edge facet-distance results concern the same graph and its polar geometry but evaluate facet normals and inball radii, not anchored-coordinate volume. The cotangent partial fractions themselves are classical; the new content is their exact occurrence in this family and its all-index spectral sign consequences.

## Limitations
The result concerns unit-edge fans and their anchored-coordinate volumes; it does not calculate Euclidean intrinsic volumes in the zero-sum hyperplane, volume products, weighted fans, or higher-order random potentials. The strict ratio alternation applies to the specific indexed fan family and its normalization. The partial-fraction identity is an exact mathematical derivation and not an assertion of publication priority. Despite comparison with selected primary works and indexed records, an unindexed equivalent fan-volume calculation remains a bibliographic risk. The standalone finite checks cannot establish the infinite theorem without the proof above.

## References
- R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, first public 2021-02-01, https://arxiv.org/abs/2102.01219.
- M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public 2019-11-24, https://arxiv.org/abs/1911.10642.
- R. Sanyal and C. Stump, *Lipschitz polytopes of posets and permutation statistics*, arXiv:1703.10586, https://arxiv.org/abs/1703.10586.
- *Multivariate volume, Ehrhart, and \(h^*\)-polynomials of polytropes*, arXiv:2006.01920, https://arxiv.org/abs/2006.01920.
- *Sharp Euclidean facet-distance spectrum and inball-center parity for fan-graph symmetric edge polytopes*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-euclidean-facet-distance-spectrum-and-inball-center-parity--50ae21474872.
