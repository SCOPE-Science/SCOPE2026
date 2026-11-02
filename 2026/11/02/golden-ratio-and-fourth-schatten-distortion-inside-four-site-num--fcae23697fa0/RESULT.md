# Golden-ratio and fourth-Schatten distortion inside four-site numerical-shadow fibers

## Finding

Let \(A(a,b,c)\in M_4(\mathbb C)\) be the matrix with the three superdiagonal entries \(a,b,c\) and all other entries zero, with \(a,c>0\) and \(b\geq0\). Let \(\nu_A\) denote the probability law of \(\langle Au,u\rangle\), where \(u\) is Haar-uniform on the complex unit sphere. Define \(x=a^2\), \(y=b^2\), \(z=c^2\), \(S=x+y+z\), \(P=xz\), and \(\rho=\sqrt P\).

**Theorem (exact fibers and two sharp distortion constants).** Two such matrices have identical full numerical shadows if and only if they have the same ordered pair \((S,P)\). A fiber exists precisely when \(P>0\) and \(S\geq2\rho\). In any fixed fiber, all values of the squared operator norm fill precisely \([L,U]\), where

\[
L=\begin{cases}\rho,&2\rho\leq S\leq3\rho,\\
\bigl(S+\sqrt{S^2-8P}\bigr)/4,&S\geq3\rho,\end{cases}
\qquad
U=\frac{S+\sqrt{S^2-4P}}2.
\]

All fourth powers of the Schatten-four norm fill precisely \([Q_-,Q_+]\), where

\[
Q_-=\begin{cases}S^2-4S\rho+6P,&2\rho\leq S\leq4\rho,\\
S^2/2-2P,&S\geq4\rho,\end{cases}
\qquad Q_+=S^2-2P.
\]

Consequently, for **any two matrices \(A,B\) in this class with the same full numerical shadow**, the following universal inequalities hold:

\[
\boxed{\max\{\|A\|,\|B\|\}\leq\frac{1+\sqrt5}{2}\min\{\|A\|,\|B\|\}},
\]

\[
\boxed{\max\{\|A\|_{\mathcal S_4},\|B\|_{\mathcal S_4}\}
\leq(1+\sqrt2)^{1/4}\min\{\|A\|_{\mathcal S_4},\|B\|_{\mathcal S_4}\}}.
\]

Both constants are sharp and attained. The operator-norm ratio attains its unique maximum over nondegenerate shadow fibers when \(S/\rho=3\), whereas the Schatten-four ratio attains its unique maximum when \(S/\rho=2+\sqrt2\). The different maximizing parameters establish two distinct sensitivity scales for the same probabilistic observable.

## Assumptions and scope

The matrices are complex \(4\times4\), with **three consecutive one-step shift weights** \(a,c>0\) and \(b\geq0\); unitary diagonal phase changes permit assuming the weights nonnegative without loss within this class. The numerical shadow means the entire probability distribution, not just the planar numerical range or its numerical radius. The norm \(\|A\|_{\mathcal S_4}=(\operatorname{tr}|A|^4)^{1/4}\). The universal constants above apply to this explicitly defined family, not to arbitrary \(4\times4\) matrices with the same shadow.

A nonempty fiber \(S\geq2\rho\) is parametrized by \(v=x+z\in[2\rho,S]\) and, up to exchanging end weights,

\[
(x,y,z)=\left(\frac{v+\sqrt{v^2-4P}}2,\ S-v,\ \frac{v-\sqrt{v^2-4P}}2\right).
\]

This is a continuous compact parameter interval, including the endpoint \(b=0\); at \(S=2\rho\) it contains only \((x,y,z)=(\rho,0,\rho)\).

## Proof

**1. Exact full-shadow invariant.** Put \(M=A(a,b,c)\). Expansion of the tridiagonal determinant gives

\[
\det(I-sM-tM^*)=1-Sst+P(s t)^2.
\]

Indeed, the sole two-edge matching on a path with four vertices uses the first and third edges, contributing \(xz=P\), whereas the one-edge matchings contribute \(x+y+z=S\). The general numerical-shadow moment identity is

\[
\mathbb E\bigl[(u^*Mu)^j\overline{(u^*Mu)}^{\,k}\bigr]
=\frac{j!k!}{(4)_{j+k}}
[s^jt^k]\det(I-sM-tM^*)^{-1},
\]

where \((4)_m=4\cdot5\cdots(3+m)\) for positive \(m\). It follows, in one direction, that equal \((S,P)\) give every mixed moment equal. The numerical shadow is compactly supported, so equality of these polynomial moments implies equality of probability measures. Conversely,

\[
\mathbb E|u^*Mu|^2=\frac S{20},\qquad
\mathbb E|u^*Mu|^4=\frac{S^2-P}{210}.
\]

Hence equal full shadows force equal \(S\) and \(P\). These moment and determinant facts are standard earlier numerical-shadow theory, not the new optimization contribution.

**2. Sharp operator-norm interval.** Since \(M^*M\) has the nonzero diagonal values \(x,y,z\),

\[
\|M\|^2=\max\{x,y,z\}
=\max\left\{\frac{v+\sqrt{v^2-4P}}2,\ S-v\right\}.
\]

The first entry is strictly increasing in \(v\geq2\rho\), while the second strictly decreases. When \(S\leq3\rho\), the increasing entry is already the larger one at \(v=2\rho\), and the minimum equals \(\rho\). When \(S>3\rho\), the unique crossing determines the minimum \(m=x=y\), \(z=P/m\), giving \(2m^2-Sm+P=0\) and \(m=(S+\sqrt{S^2-8P})/4\). The maximum of the increasing entry is its value at \(v=S\); the maximum of the decreasing entry is \(S-2\rho\), which is no larger than the former value. Thus the interval endpoints are exactly \(L,U\). Continuity proves there are no missing intermediate values.

**3. Sharp Schatten-four interval.** Direct diagonalization of \(M^*M\) yields

\[
\|M\|_{\mathcal S_4}^4=x^2+y^2+z^2
=v^2-2P+(S-v)^2.
\]

This is a strictly convex quadratic in \(v\), minimized at \(v=\max\{2\rho,S/2\}\) subject to \(2\rho\leq v\leq S\). Its maximum is at \(v=S\), since the other endpoint yields a value smaller by \(4\rho(S-2\rho)\). Substitution proves the stated \(Q_-,Q_+\) and continuity supplies the full interval.

**4. Golden-ratio norm distortion.** Set \(r=S/\rho\geq2\). The largest possible ratio of **squared** operator norms within one fiber is \(U/L\). For \(2\leq r\leq3\), this ratio is

\[
\frac{U}{L}=\frac{r+\sqrt{r^2-4}}2,
\]

which increases strictly in \(r\). For \(r\geq3\), the ratio becomes

\[
\frac UL=2\frac{r+\sqrt{r^2-4}}{r+\sqrt{r^2-8}}.
\]

Its logarithmic derivative is \(1/\sqrt{r^2-4}-1/\sqrt{r^2-8}<0\) for \(r>3\). Therefore \(U/L\) has its unique maximum at \(r=3\), where it equals \((3+\sqrt5)/2=((1+\sqrt5)/2)^2\). Taking square roots proves the first sharp constant. It is attained in the same fiber \((S,P)=(3,1)\) by the squared weights \((1,1,1)\) and \(((3+\sqrt5)/2,0,(3-\sqrt5)/2)\).

**5. Fourth-Schatten distortion.** The largest fourth-power Schatten-four ratio in a fiber is \(Q_+/Q_-\). For \(2\leq r\leq4\), it equals

\[
F(r)=\frac{r^2-2}{r^2-4r+6},
\qquad
F'(r)=\frac{-4(r^2-4r+2)}{(r^2-4r+6)^2}.
\]

Thus it increases until \(r=2+\sqrt2\) and then decreases. For \(r\geq4\), it equals \(2(r^2-2)/(r^2-4)\), also strictly decreasing. The unique global maximum is

\[
F(2+\sqrt2)=1+\sqrt2.
\]

The maximum is attained by the squared weights \(((r+\sqrt{r^2-4})/2,0,(r-\sqrt{r^2-4})/2)\) for the upper fourth moment and \((1,r-2,1)\) for the lower fourth moment at \(r=2+\sqrt2\), with \(P=1\). Taking fourth roots proves the second sharp constant.

**6. Distinct extremal fibers and nilpotence.** Since \(3\ne2+\sqrt2\), no fixed shadow fiber simultaneously realizes both universal distortion constants. For every \(S>2\rho\) the endpoint \(v=S\) has \(b=0\), hence \(M^2=0\), while the interior \(v\in(2\rho,S)\) has \(abc>0\), hence \(M^3\ne0\) and \(M^4=0\). This distinct-nilpotency phenomenon is an illustration of the previously known non-rigidity of numerical shadows and is not claimed as a new general discovery.

## Verification

The included dependency-free `verify.py` checks the determinant/moment invariants by exact rational polynomial calculations on representative fibers, verifies exact extremizer identities using algebraic arithmetic where possible, and performs deterministic finite numerical stress tests across the entire allowed parameter region. These tests are supplementary checks; the infinite family of sharp inequalities follows from the above monotonicity and convexity arguments. To replay: `python3 verify.py`.

## Relationship to prior work

Dunkl, Gawron, Holbrook, Puchała and Życzkowski, *Numerical shadows: measures and densities on the numerical range* (arXiv:1010.4189, 2010), develop the general shadow moment/determinant characterization and explicitly identify every rotation-invariant shadow with that of a direct sum of scaled two-dimensional Jordan blocks (their Section VIII, especially Remark 8.7). They already show that shadow equality can hide different ranks; therefore shadow equivalence, rotational invariance, and the nilpotency illustration are **prior input**, not novel claims. Their general results imply the \((S,P)\) shadow-invariant calculation after specialization, but do not state or optimize the two exact norm-distortion ratios reported here.

Johnson, *Numerical Shadow Rigidity for 3x3 Matrices* (arXiv:2610.29675v1, first public October 21, 2026), studies matrix-level rigidity in dimension three, not sharp operator or fourth-Schatten distortion over the indicated four-site fibers. Prior literature on Schatten norms and numerical radii of weighted shifts treats different objectives; the new statement is the **pair of universal sharp within-shadow distortion constants, full per-fiber intervals, and noncoincident extremal fibers**.

## Limitations

The class is restricted to nonnegative three-edge nilpotent shifts of dimension four (up to removable phases). Neither bound is asserted for other \(4\times4\) matrices sharing the same numerical shadow. The fourth Schatten power is a matrix invariant distinct from the fourth moment of the numerical shadow. The theorem determines sharp inequalities within a shadow fiber but not the general inverse problem for arbitrary matrices. General shadow equivalence and the reduction to invariant parameters are already established in 2010; the claimed contribution begins only with the quantitative optimizations. Bibliographic absence of an equivalent stated optimization is a best-knowledge assessment, not proof of publication priority. Independent expert audit has not been performed.

## References

1. C. F. Dunkl, P. Gawron, J. A. Holbrook, Z. Puchała, and K. Życzkowski, *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189v1 (October 20, 2010), Sections V–VI and VIII. https://arxiv.org/abs/1010.4189
2. D. Johnson, *Numerical Shadow Rigidity for 3x3 Matrices*, arXiv:2610.29675v1 (October 21, 2026), MSC 47A12. https://arxiv.org/abs/2610.29675
