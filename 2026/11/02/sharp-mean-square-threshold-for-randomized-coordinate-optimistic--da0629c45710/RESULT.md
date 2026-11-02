# Sharp mean-square threshold for randomized coordinate optimistic gradient on a bilinear saddle

## Finding
For non-accelerated, uniformly sampled two-coordinate RCOG on the bilinear saddle \(\min_x\max_y(-xy)\), with past-gradient ratio \(g=9/10\), the exact mean-square stability frontier is
\[
0<t^2<\frac{800}{1539}.
\]
For every deterministic nonzero starting point initialized with \(x^{-1}=x^0\), equality produces the nonzero limit
\[
\lim_{k\to\infty}\mathbb E\|x^k\|^2=\frac{1089}{3217}\|x^0\|^2.
\]
Above the threshold \(\limsup_{k\to\infty}(\mathbb E\|x^k\|^2)^{1/k}>1\). In particular, at \(t=3/4\) the mean iterate converges geometrically while the mean-square error grows exponentially along a subsequence.

## Assumptions and scope
Define \(J=\begin{psmallmatrix}0&-1\1&0\end{psmallmatrix}\) and \(G(x)=Jx\) on \(\mathbb R^2\), with the unique root zero. Draw independent uniform coordinate indices \(i_k\in\{1,2\}\), writing \(P_i\) for the corresponding orthogonal coordinate projection. Set \(g=9/10\), choose effective step \(t>0\), and iterate
\[
x^{k+1}=x^k-2tP_{i_k}J(x^k-gx^{k-1}),\qquad x^{-1}=x^0\ne0.
\]
This is exactly the source's non-accelerated RCOG specialization with constant \(\omega,\eta,\gamma\), where \(t=\omega\eta\), \(g=\gamma/\eta=9/10\), and selection probabilities \(1/2\). In particular \(\eta>\gamma>0\), as required for the update definition. The theorem is for exact arithmetic and independent sampling across all iterations.

## Proof
Let \(s=t^2\). Introduce \(u_k=\mathbb E\|x^k\|^2\), \(v_k=\mathbb E\langle x^k,x^{k-1}\rangle\), \(w_k=\mathbb E\|x^{k-1}\|^2\), and \(c_k=\mathbb E\langle x^k,Jx^{k-1}\rangle\). Using \(J^\mathsf TJ=I\), \(J^\mathsf T=-J\), \(\mathbb E P_{i_k}=I/2\), and \(\mathbb E\|P_{i_k}z\|^2=\|z\|^2/2\), direct conditional expansion gives the **exact** linear recurrence
\[
\begin{pmatrix}u_{k+1}\v_{k+1}\w_{k+1}\c_{k+1}\end{pmatrix}=
M\begin{pmatrix}u_k\v_k\w_k\c_k\end{pmatrix},\qquad
M=\begin{pmatrix}
1+2s&-4sg&2sg^2&2tg\
1&0&0&tg\
1&0&0&0\
-t&tg&0&0
\end{pmatrix}.
\]
The initial moment state is \(\|x^0\|^2(1,1,1,0)^\mathsf T\), and the characteristic polynomial is
\[
p(\lambda)=\lambda^4-(1+2s)\lambda^3+s(6g-3g^2)\lambda^2-g^2s(1+2s)\lambda+2g^4s^2.
\]
At \(g=9/10\), \(p(1)=2s(g-1)[g^2(1+g)s-2g+1]\), whose positive zero is \(s_0=800/1539\). To prove that all four eigenvalues are strictly inside the disk for \(0<s<s_0\), make the Cayley transform \(\lambda=(1+w)/(1-w)\). For the resulting real quartic \(q(w)=(1-w)^4p((1+w)/(1-w))=\sum_{j=0}^4a_jw^j\), the Routh–Hurwitz criteria reduce to positivity of \(a_0,\ldots,a_4\) and the two determinants \(a_3a_2-a_4a_1\), \(a_3a_2a_1-a_4a_1^2-a_3^2a_0\). Each is a polynomial in \(s\) with rational coefficients. In each case, substituting \(s=s_0r/(1+r)\) and multiplying by a sufficient power of \(1+r\) yields a polynomial with nonnegative rational coefficients and strictly positive value for \(r>0\). The included exact-arithmetic script explicitly verifies all seven certificates. Thus the moment recurrence tends to zero for \(0<s<s_0\).

For a complete necessity argument, the first-moment-coordinate generating function (normalized by \(\|x^0\|^2\)) has the exact form \(U(z)=N(z)/D(z)\), with
\[
\begin{aligned}
D(z)&=1-(1+2s)z+s(6g-3g^2)z^2-g^2s(1+2s)z^3+2g^4s^2z^4,\
N(z)&=1+s(2g^2-4g)z+g^2sz^2-2g^4s^2z^3.
\end{aligned}
\]
At \(g=9/10\), the exact polynomial resultant is
\[
\operatorname{Res}_z(D,N)=-\frac{3486784401}{6250000000000}s^7(4s-1)^2.
\]
It is nonzero for every \(s\ge s_0>1/4\), so no denominator root is canceled. For \(s>s_0\), \(D(0)=1\) and \(D(1)=p(1)<0\), giving an uncanceled pole in \((0,1)\). By the Cauchy–Hadamard formula and nonnegativity of \(u_k\), \(\limsup u_k^{1/k}>1\). At equality, the Cayley inequalities remain strict except for \(a_0=0\), so the only unit-circle eigenvalue is a simple eigenvalue \(1\), with all others strictly inside the disk. Evaluating the simple pole of \(U(z)\) at \(z=1\) gives \(\lim u_k/\|x^0\|^2=1089/3217\).

Finally the mean obeys the deterministic recurrence \(\mathbb E x^{k+1}=(I-tJ)\mathbb E x^k+tgJ\mathbb E x^{k-1}\). Identifying the plane with \(\mathbb C\), its characteristic quadratic is \(\lambda^2+(-1+it)\lambda-itg\). At \(t=3/4\), \(g=9/10\), the exact quadratic Schur–Cohn inequalities are \(|-itg|^2=729/1600<1\) and \(|a-\bar a b|^2=6385/25600<(1-|b|^2)^2=(871/1600)^2\), with \(a=-1+3i/4\), \(b=-27i/40\). Thus the mean converges geometrically although \(t^2=9/16>s_0\) gives exponentially growing mean square along a subsequence.

## Verification
Run `python verification/check.py` with Python 3 and SymPy. The checker independently reconstructs the moment characteristic polynomial, positive-coefficient Routh–Hurwitz certificates, numerator/denominator resultant and critical residue, Schur–Cohn inequalities, and seven levels of exact enumeration of independent coordinate draws. Its output is a finite algebraic certificate corroborating the displayed identities; the proof supplies the infinite-iteration implications.

## Relationship to prior work
Tran-Dinh and Luo introduce the RCOG update and provide Lyapunov-based sufficient convergence rates under coordinate Lipschitz and weak-Minty hypotheses. The present claim specializes their exact update to a bilinear skew saddle but determines its **necessary-and-sufficient** mean-square stability threshold, including a nonvanishing critical limit and a mean-versus-mean-square separation. Existing analyses of full-vector optimistic/reflected gradients or different adaptive coordinate selection do not directly imply this sampled-coordinate numerical threshold. Generic random-matrix second-moment theory explains the recurrence framework and is not claimed as new.

## Limitations
The frontier concerns two coordinates, pure bilinear skew dynamics, independent equiprobable coordinate sampling, the fixed ratio \(g=9/10\), and exact arithmetic. It does not give a universal threshold for other operators, distributions, or ratios, and does not rule out almost-sure convergence in the mean-square-unstable regime. The originality comparison is best-knowledge, not an independent exhaustive priority certification.

## References
1. Tran-Dinh and Luo, Randomized Block-Coordinate Optimistic Gradient Algorithms for Root-Finding Problems, arXiv:2301.03113 (version 3 publicly dated 2023-09-23; version 5 for formula and theorem).
2. Song and Diakonikolas, *Cyclic Coordinate Dual Averaging with Extrapolation*, arXiv:2102.13244 (a different cyclic block method).
3. Asaad, *Momentum Block GDA: A Block Coordinate Algorithm for Solving Bilinear Min-Max Games*, American University of Beirut master's thesis, March 2023 (dynamic rather than iid block selection).
