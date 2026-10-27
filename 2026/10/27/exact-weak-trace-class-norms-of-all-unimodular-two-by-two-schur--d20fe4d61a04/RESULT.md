# Exact weak trace-class norms of all unimodular two-by-two Schur multipliers

## Finding
Let \(m=(m_{ij})_{i,j=1}^2\) be a complex matrix with \(|m_{ij}|=1\) for every entry, and let \(S_m X=m\circ X\) denote entrywise multiplication on complex \(2\times 2\) matrices. Write \(s_1(Y)\ge s_2(Y)\ge0\) for singular values, with \(\|Y\|_{1,\infty}=\max\{s_1(Y),2s_2(Y)\}\) and \(\|X\|_1=s_1(X)+s_2(X)\). Define the gauge-invariant angle \(\delta\in[0,\pi]\) by
\[
\delta=\left|\operatorname{Arg}\!\left(\frac{m_{11}m_{22}}{m_{12}m_{21}}\right)\right|.
\]
Then the exact weak trace-class multiplier norm is
\[
\boxed{\sup_{X\ne0}\frac{\|S_mX\|_{1,\infty}}{\|X\|_1}=\sec(\delta/4).}
\]
The constant is attained for every \(\delta\); it equals one precisely when the phase symbol factors as a row phase times a column phase. In canonical gauge \(m=\begin{psmallmatrix}1&1\\1&e^{i\delta}\end{psmallmatrix}\), one extremizer is \(X=\begin{psmallmatrix}1&1\\1&-e^{-i\delta}\end{psmallmatrix}\). The endpoint has quadratic infinitesimal phase loss: \(\sec(\delta/4)=1+\delta^2/32+O(\delta^4)\) as \(\delta\downarrow0\).

## Assumptions and scope
All matrices are complex \(2\times2\); the domain norm is the ordinary Schatten trace norm and the target is the specific weak Schatten quasi-norm \(\sup_{j=1,2}j s_j\), without logarithmic renormalization. The formula is not asserted for amplified multipliers, larger dimensions, nonunimodular symbols or other target quasi-norm conventions. Because multiplying a symbol by unit-modulus row and column factors conjugates its Schur map by diagonal unitaries on the left and right, only its one invariant cross-ratio phase matters. Complex conjugation exchanges the two signs of this angle, so it suffices to assume \(0\le\delta\le\pi\).

## Proof
Put \(\theta=\delta\). Gauge reduction gives \(m=\begin{psmallmatrix}1&1\\1&e^{i\theta}\end{psmallmatrix}\). If \(\theta=0\), the Schur map is multiplication by diagonal unitaries and hence is an isometry on both norms; its operator norm is exactly one. Assume \(0<\theta\le\pi\), and abbreviate \(c=\cos(\theta/2)\), \(h=\sin(\theta/2)\).

Fix nonzero \(X=\begin{psmallmatrix}a&b\\c_0&d\end{psmallmatrix}\), and put \(Y=S_mX\) and \(F=|a|^2+|b|^2+|c_0|^2+|d|^2>0\). (The entry \(c_0\) is distinct from the trigonometric number \(c\).) Define
\[
\alpha=2ad/F,\quad \beta=2bc_0/F,\quad u=|\alpha-\beta|,\quad v=|e^{i\theta}\alpha-\beta|.
\]
By the arithmetic-geometric mean inequality, \(|\alpha|+|\beta|\le1\), so \(0\le u,v\le1\). The determinant identities \(2|\det X|=Fu\) and \(2|\det Y|=Fv\), together with the exact \(2\times2\) singular-value identities, imply
\[
\|X\|_1=\sqrt F\sqrt{1+u},\qquad
2s_2(Y)=\sqrt F\big(\sqrt{1+v}-\sqrt{1-v}\big).
\tag{1}
\]
We next maximize \(v\) subject to a fixed \(u\), allowing all \(\alpha,\beta\) with \(|\alpha|+|\beta|\le1\). Set \(r=\alpha-\beta\) and \(z=e^{i\theta}\alpha-\beta\). Solving these equations shows that the constraint is precisely
\[
|z-r|+|z-e^{i\theta}r|\le 2h.
\tag{2}
\]
For \(|r|=u\), rotate the plane by the phase of \(r e^{i\theta/2}\). The two foci of this ellipse are \(uc\pm iuh\); its semiaxes are \(h\sqrt{1-u^2}\) in the real direction and \(h\) in the imaginary direction. Hence its boundary is parametrized by
\[
z=uc+h\sqrt{1-u^2}\cos\phi+ih\sin\phi.
\tag{3}
\]
The squared modulus in (3), written as a quadratic in \(q=\cos\phi\in[-1,1]\), is
\[
|z|^2=u^2c^2+h^2+2uch\sqrt{1-u^2}\,q-h^2u^2q^2.
\]
Its maximum occurs at \(q=1\) when \(0\le u\le c\); for \(c\le u\le1\) the interior optimum \(q=c\sqrt{1-u^2}/(hu)\) is feasible. The largest admissible \(v\) therefore satisfies
\[
v_{\max}(u)=\begin{cases}uc+h\sqrt{1-u^2},&0\le u\le c,\\1,&c\le u\le1.\end{cases}
\tag{4}
\]
(The cases \(u=0\), \(\theta=\pi\) and boundary points follow by continuity.) Because the ratio in (1) is increasing in \(v\), its square is at most
\[
R(u)^2=\frac{2\big(1-\sqrt{1-v_{\max}(u)^2}\big)}{1+u}.
\tag{5}
\]
If \(u\le c\), the square root in (5) equals \(c\sqrt{1-u^2}-hu\), and the numerator becomes \(2(1-c\sqrt{1-u^2}+hu)\). The derivative of the expression without the factor two is
\[
\frac{c(1+u)/\sqrt{1-u^2}+h-1}{(1+u)^2}\ge0,
\]
since \(c+h\ge1\) and \((1+u)/\sqrt{1-u^2}\ge1\). Thus the bound increases on \([0,c]\). On \([c,1]\), equation (4) gives \(R(u)^2=2/(1+u)\), which decreases. Consequently the global bound is attained at \(u=c\), and
\[
\frac{2s_2(Y)}{\|X\|_1}\le\sqrt{\frac{2}{1+c}}=\sec(\theta/4).
\]
For the first singular value, \(s_1(Y)\le\|Y\|_2=\|X\|_2\le\|X\|_1\), because every symbol entry has modulus one. Combining the two inequalities proves the upper bound for the weak norm.

Finally take \(X=\begin{psmallmatrix}1&1\\1&-e^{-i\theta}\end{psmallmatrix}\). Then \(Y=\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}\) has both singular values \(\sqrt2\), while \(\|X\|_1=2\sqrt{1+\cos(\theta/2)}\). Its ratio is exactly \(\sec(\theta/4)\), establishing sharpness. Taylor expansion yields the quadratic phase loss, and the gauge-invariant statement follows.

## Verification
The proof is exact and covers every real angle \(\theta\in[0,\pi]\) and every nonzero complex \(2\times2\) input. A standalone deterministic script tests the spectral identities, random complex matrices against the proposed constant at eight angles, and the explicit sharp witnesses. Numerical testing only supports the algebra; it is not an exhaustive proof. The exceptional \(\theta=0\) case and the endpoint \(\theta=\pi\) are handled analytically.

## Relationship to prior work
Tian (2026) proves that weak \((1,1)\) Schur multiplier boundedness is equivalent, within universal multiplicative factors, to a weighted-column approximation criterion and establishes endpoint Hörmander–Mikhlin–Schur estimates. The present calculation is an exact finite-dimensional sharp norm problem not supplied by those comparisons. Davidson and Donsig (2005) investigate Schur multiplier norms on bounded operators and symmetrically structured symbols; that operator-norm target is not the weak trace-class target. Banks and Harcharras (2004) treat idempotent multipliers on Schatten \(S_p\), \(1<p<\infty\), rather than the nonidempotent unimodular phase family with a weak \(S_1\) target.

In particular the small-phase weak norm grows quadratically, whereas on the rank-one input with four equal positive entries the ordinary trace norm of the output is \(\cos(\theta/4)+\sin(\theta/4)=1+\theta/4+O(\theta^2)\). Thus the weak endpoint has a genuinely different local phase response from the strong trace-norm problem.

## Limitations
No claim is made for infinite Schur symbols, entrywise moduli other than one, amplification, the full trace-class target norm, or general classification of all equality inputs. This self-review does not replace independent verification. The possibility of older equivalent formulas for two-dimensional weak Schatten multiplier constants remains a priority risk.

## References
- Yongqiang Tian, *Weak (1,1) Shur multipliers and the Hörmander–Mikhlin–Schur theorem*, arXiv:2610.20339, first submitted 2026-10-14, particularly Definition (1.3), Theorem 1.2 and its proof.
- Kenneth R. Davidson and Allan P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073 (2005), especially Sections 1 and 4.
- William D. Banks and Asma Harcharras, *On the norm of an idempotent Schur multiplier on the Schatten class*, Proceedings of the American Mathematical Society 132 (2004), 2121–2125.
