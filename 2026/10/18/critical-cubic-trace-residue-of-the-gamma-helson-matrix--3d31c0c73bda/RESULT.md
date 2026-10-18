# Critical cubic trace residue of the gamma Helson matrix

## Finding
For every real \(\beta>1\), let the operator \(H_\beta\) on \(\ell^2(\mathbb N)\) have entries
\[
(H_\beta)_{mn}=\frac{1}{\sqrt{mn}(1+\log(mn))^\beta},\qquad m,n\ge1.
\]
This positive Helson operator is trace class. Its cubic Schatten moment has the sharp critical residue
\[
\boxed{\lim_{\beta\downarrow1}(\beta-1)\operatorname{Tr}(H_\beta^3)=\frac{\pi^2}{12}.}
\]
For contrast, the first and second trace moments have residues
\[
\lim_{\beta\downarrow1}(\beta-1)\operatorname{Tr}H_\beta
=\lim_{\beta\downarrow1}(\beta-1)\operatorname{Tr}(H_\beta^2)=\tfrac12.
\]
Thus the third moment captures a nontrivial three-way interaction not specified by trace-class membership or by the first two residues.

## Assumptions and scope
The Hilbert space is the usual \(\ell^2(\mathbb N)\) with \(\mathbb N=\{1,2,\ldots\}\). Natural logarithms are used; \(\beta\) is real and tends to one from above. Set
\[
F_\beta(x,y,z)=\prod_{\mathrm{cyc}}(1+x+y)^{-\beta},\quad x,y,z\ge0,
\]
where the three factors correspond to \((x+y),(y+z),(z+x)\). All traces are the usual positive operator traces. No assertion is made about \(\beta\le1\), individual eigenvalues, or nonpositive measures.

## Proof
**1. Positivity and trace class.** With \(s=\tfrac12+t\), the finite positive gamma measure
\[
\frac{t^{\beta-1}e^{-t}}{\Gamma(\beta)}\,dt,\qquad t>0,
\]
has moment \(\int_0^\infty (mn)^{-1/2-t}t^{\beta-1}e^{-t}\,dt/\Gamma(\beta)=(H_\beta)_{mn}\). Therefore the matrix is positive. Its diagonal sum is
\[
\sum_{n\ge1}\frac1{n(1+2\log n)^\beta}<\infty\qquad(\beta>1),
\]
which makes its Gram synthesis map Hilbert--Schmidt and \(H_\beta\) trace class. Positivity permits monotone finite truncation in trace identities, giving
\[
S_\beta:=\operatorname{Tr}(H_\beta^3)=
\sum_{m,n,k\ge1}\frac{F_\beta(\log m,\log n,\log k)}{mnk}.
\]

**2. Sum-to-integral comparison with a bounded error.** Let \(\nu=\sum_{n\ge1}n^{-1}\delta_{\log n}\) and let \(\lambda\) be Lebesgue measure on \([0,\infty)\). For any nonnegative decreasing function \(f\), partition \([0,\infty)\) into intervals \([\log n,\log(n+1))\). Since \(\log(1+1/n)\le1/n\), the left sum dominates the integral. Moreover
\[
0\le\int f\,d\nu-\int f\,d\lambda\le2f(0).
\]
Indeed the excess weights sum to at most \(\sum_{n\ge1}(2n^2)^{-1}<1\), and the within-interval monotonicity error is bounded by \((\log2)f(0)<f(0)\) via telescoping endpoint differences. Applying this inequality successively to the three separately decreasing variables yields
\[
0\le S_\beta-I_\beta\le
\int_{[0,\infty)^3}F_\beta(x,y,z)\,d(\lambda+2\delta_0)^{\otimes3}
-I_\beta,
\quad I_\beta=\int_{[0,\infty)^3}F_\beta\,dx\,dy\,dz.
\]
The right side contains only proper coordinate faces. It is bounded uniformly for \(\beta\ge1\): at \(\beta=1\), each two-dimensional face is dominated, after splitting \(y\ge z\) and its transpose, by an integral of \((1+y)^{-2}\log(1+y)\); one-dimensional faces decay as \((1+t)^{-2}\); the zero-dimensional face is finite. Thus \(S_\beta=I_\beta+O(1)\) as \(\beta\downarrow1\).

**3. Exact cubic integral residue.** Write \(R=x+y+z\) and \(u_i=x_i/R\) for \(R>0\), with \(u_1+u_2+u_3=1\), \(u_i\ge0\). In the coordinates \((R,u_1,u_2)\) the Jacobian is \(R^2\). Putting \(a_i=1-u_i\), one obtains
\[
I_{1+\varepsilon}=\int_{\Delta}\int_0^\infty
\frac{R^2\,dR\,du_1\,du_2}{\prod_{i=1}^3(1+Ra_i)^{1+\varepsilon}},
\qquad \varepsilon>0.
\]
The range \(0<R<1\) contributes \(O(1)\). For \(R\ge1\), the remaining integral is
\[
\int_1^\infty R^{-1-3\varepsilon}
G_\varepsilon(R)\,dR,
\qquad G_\varepsilon(R)=\int_\Delta\prod_{i=1}^3(a_i+R^{-1})^{-1-\varepsilon}\,du_1\,du_2.
\]
For \(0<\varepsilon\le1/2\), these integrands are dominated on the simplex by \(\prod a_i^{-3/2}\), which is integrable: near any simplex vertex the only singular factor has order below two in two local variables. Consequently \(G_\varepsilon(R)\to A\) as \(\varepsilon\to0\) and \(R\to\infty\), where
\[
A=\int_\Delta\frac{du_1\,du_2}{(1-u_1)(1-u_2)(1-u_3)}.
\]
Since \(3\varepsilon R^{-1-3\varepsilon}dR\) is a probability measure on \([1,\infty)\) whose mass escapes to infinity as \(\varepsilon\downarrow0\), dominated convergence gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon I_{1+\varepsilon}=\frac A3.
\]
Set \(t=u_1+u_2\), integrate first in \(u_1\in[0,t]\), and then put \(t=1-e^{-v}\). Direct partial fractions give
\[
A=\int_0^1\frac{-2\log(1-t)}{t(2-t)}\,dt
=\int_0^\infty\frac{v}{\sinh v}\,dv
=2\sum_{j\ge0}\frac1{(2j+1)^2}=\frac{\pi^2}{4}.
\]
The last identity follows by expanding \(1/\sinh v=2\sum_{j\ge0}e^{-(2j+1)v}\) and integrating termwise. Therefore \(\lim_{\varepsilon\downarrow0}\varepsilon S_{1+\varepsilon}=A/3=\pi^2/12\), as claimed.

**4. First and second moments for comparison.** The trace is the one-dimensional diagonal sum, whose integral comparison yields \(\lim_{\varepsilon\downarrow0}\varepsilon\operatorname{Tr}H_{1+\varepsilon}=1/2\). The second trace moment is the two-dimensional sum associated with \((1+x+y)^{-2(1+\varepsilon)}\). Its integral over the quadrant equals \(\int_0^\infty R(1+R)^{-2(1+\varepsilon)}dR\), which has residue \(1/2\); the two-dimensional quadrature error is uniformly bounded. This proves both supplementary limits.

## Verification
The standalone script `CHECK.py` numerically verifies the simplex angular coefficient by an independent convergent series and a controlled quadrature, checks the elementary cell-length inequalities and tests positive finite-section cubic trace sums. These finite checks corroborate the calculation but do not constitute the infinite-dimensional proof. The argument above establishes the exact universal limiting statement.

## Relationship to prior work
Ma, Lu and Zu (2026), Example 3.6, consider exactly this gamma-measure Helson family and give the trace-class threshold at \(\beta=1\), while their Theorem 3.4 identifies its trace. Their results do not provide the third trace-moment residue. Brevig, Perfekt, Seip, Siskakis and Vukotić (2014/2016) establish the spectrum and norm of the critical multiplicative Hilbert matrix, and Miheisi and Pushnitski (2017) establish individual eigenvalue asymptotics for a different logarithm-of-logarithm perturbation. The present result computes the cubic interaction coefficient along the gamma regularization; it does not assert that the classical spectral theory or the trace-class criterion is new.

## Limitations
The calculation concerns a concrete positive scalar gamma family, not arbitrary Helson measures. No full spectral distribution, individual eigenvalue asymptotics, or stronger independent-priority claim is established. A general trace-asymptotic theorem under different notation might imply this coefficient and remains a publication-priority risk. The accompanying computational checks are finite diagnostics only.

## References
1. T. Ma, Y. Lu and C. Zu, *Unbounded Helson Forms with a Moment Representation*, arXiv:2610.12252v1 (first posted October 8, 2026), especially Theorem 3.4 and Example 3.6.
2. N. Miheisi and A. Pushnitski, *A Helson matrix with explicit eigenvalue asymptotics*, arXiv:1709.06326 (2017).
3. O. F. Brevig, K.-M. Perfekt, K. Seip, A. G. Siskakis and D. Vukotić, *The multiplicative Hilbert matrix*, arXiv:1411.7294 (2014), published 2016.
