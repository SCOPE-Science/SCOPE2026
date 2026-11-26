# An exact nonnegative fourth-moment deficit for two finite-group coordinate axes

## Finding

Let \(A\) be a finite abelian group of order \(N\ge4\), let \(S=(A\times\{0\})\cup(\{0\}\times A)\), and extend an arbitrary \(f:S\to\mathbb C\) by zero to \(A^2\). Put \(M=\sum_{s\in S}|f(s)|^2\) and \(Q=\sum_{z\in A^2}|(f*f)(z)|^2\), with counting convolution. The contribution is an **exact eight-term nonnegative decomposition** of \(NM^2-Q\), valid also at order four. The terms separate axis convolution Cauchy–Schwarz deficits, fluctuations of antipodal products, an origin-versus-antipodal balance square, mixed-axis mass, and phase cancellation at the origin.

Write \(a=f(0,0)\), \(u(x)=f(x,0)\), \(v(x)=f(0,x)\), \(\lambda=|a|^2\), \(G=\sum_{x\ne0}|u(x)|^2\), and \(H=\sum_{x\ne0}|v(x)|^2\), so that \(M=\lambda+G+H\). For \(w\in\{u,v\}\) define
\[
B_w=\sum_{x\ne0}w(x)w(-x),\qquad R_w=\sum_{x\ne0}|w(x)w(-x)|^2,
\qquad
\Delta_w=\sum_{s\ne0}\left(N\sum_{t\in A}|w(t)w(s-t)|^2-|(w*w)(s)|^2\right).
\]
Set \(b=|B_u|\), \(c=|B_v|\), and \(\theta_N=2N-6-2/(N-1)\). Then
\[
\begin{aligned}
NM^2-Q={}&\Delta_u+\Delta_v
+N\left(R_u-\frac{b^2}{N-1}\right)+N\left(R_v-\frac{c^2}{N-1}\right)\\
&+\frac{((N-1)\lambda-b-c)^2}{N-1}
+\theta_Nbc+(2N-4)(GH-bc)\\
&+\left[(\lambda+b+c)^2-|a^2+B_u+B_v|^2\right]. \tag{1}
\end{aligned}
\]
In particular, \(NM^2-Q\ge\theta_N GH\). This estimate controls the product of the energies off the common origin, with coefficient \(4/3\) even at \(N=4\); no optimality is asserted for the coefficient \(\theta_N\). For a small deficit, (1) also controls each axis's convolution and antipodal-product deficits separately.

## Proof

The off-axis convolution fiber at \((s,t)\) with \(s,t\ne0\) consists of the two ordered pairs \((s,0),(0,t)\) and their reversal, giving \(2u(s)v(t)\). At \((s,0)\) with \(s\ne0\) all contributing pairs are on the horizontal axis and give \((u*u)(s)\), and likewise on the vertical axis. At \((0,0)\) the value is \(a^2+B_u+B_v\), counting the origin pair only once. Hence
\[
Q=|a^2+B_u+B_v|^2+4GH+\sum_{s\ne0}\left(|(u*u)(s)|^2+|(v*v)(s)|^2\right).
\]
For the horizontal convolution, the total double sum of squared products is \((\lambda+G)^2\); the portion with sum zero is \(\lambda^2+R_u\), including terms from involutions without any change in counting. The definition of \(\Delta_u\) therefore gives
\[
\sum_{s\ne0}|(u*u)(s)|^2=N(2\lambda G+G^2-R_u)-\Delta_u.
\]
Using the corresponding identity for \(v\) gives
\[
NM^2-Q=\Delta_u+\Delta_v+N(R_u+R_v)+(2N-4)GH+N\lambda^2-|a^2+B_u+B_v|^2. \tag{2}
\]
To recover (2) from (1), expand the balance square. Its \(-2\lambda(b+c)\) cancels with the origin term, leaving \(N\lambda^2\). The \(b^2,c^2\) terms cancel because \(-N/(N-1)+1/(N-1)+1=0\), and the remaining coefficient of \(bc\) is \(2/(N-1)+2+\theta_N-(2N-4)=0\).

Each \(\Delta_w\) is nonnegative by Cauchy–Schwarz in its convolution fiber; Cauchy–Schwarz also gives \(|B_w|^2\le(N-1)R_w\). Since inversion permutes the nonzero elements, \(b\le G\) and \(c\le H\) by the triangle inequality and Cauchy–Schwarz. The bracket on the last line of (1) is nonnegative by the triangle inequality. Thus all eight terms are nonnegative, using \(\theta_N>0\) and \(2N-4>0\). Their two mixed-axis terms sum to \(\theta_N GH+(2N-4-\theta_N)(GH-bc)\), which proves the displayed product bound.

## Relation to the sharp inequality

With unnormalized Fourier synthesis \(F(\chi,\eta)=\sum_{(x,y)\in S} f(x,y)\chi(x)\eta(y)\), character orthogonality gives \(\mathbb E_{\chi,\eta}|F|^4=Q\). For normalized source counting measure on \(S\), unnormalized dual counting measure, and extension \(\mathcal E f=F/(2N-1)\), the same deficit in extension variables is
\[
\frac{N^3}{(2N-1)^2}\|f\|_{L^2(S)}^4-\|\mathcal E f\|_{\ell^4(\widehat A^2)}^4
=\frac{N^2}{(2N-1)^4}(NM^2-Q).
\]
If the deficit vanishes then \(GH=0\). On a single axis Plancherel reduces the equality to \(\sum_\chi|\widehat u(\chi)|^4=(\sum_\chi|\widehat u(\chi)|^2)^2\) or the analogous equation for \(v\). A nonzero solution has exactly one nonzero Fourier entry, so it is a multiple of a character on that complete axis and zero off it. These data give zero deficit. Thus (1) is also an alternative proof of the sharp bound and its equality classification, which are not claimed as new here.

The result *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* ([record 5b31463115dc](https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc/RESULT.md)) gives the sharp theorem for two axes at \(N\ge5\) after normalization; its scalar factorization in equation (5) is applied to a majorant and is not a termwise identity for the original deficit. *The order-four endpoint for sharp fourth moments on finite abelian coordinate crosses* ([record a9c611ea59b6](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-the-order-four-endpoint-for-sharp-fourth-moments-on-finite-abeli--a9c611ea59b6/RESULT.md)) covers the constant and equality for all \(N\ge4\) and any number of coordinate axes, and for \(N\ge5\) gives a mixed-mass remainder with coefficient \(2(N-5+1/(N-1))\). For two axes the coefficient \(\theta_N\) above exceeds that coefficient by \(4-4/(N-1)\). These results use centered independent moments; the nonzero-fiber and antipodal-product deficits in (1) give additional separate information. The comparison does not assert historical priority. The order-three failure of the sharp inequality is also previously known (for instance, the all-ones cross has ratio \(77/25>3\)), and is not part of the contribution.

## Verification and scope

Equation (1) follows from the exact convolution fibers and the algebraic cancellations in (2); the proof applies to every finite abelian group of the stated orders and every complex coefficient array. The supplied `verify_axes.py` evaluates the exact identity on finitely many examples using numerical tolerances, including both types of order-four group. These checks corroborate rather than replace the proof. The identity concerns two coordinate axes, not higher moments or arbitrary intersections of subgroups.
