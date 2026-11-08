# A geometric-radius resonance for parity-separated cubic phase retrieval on three four-point circles

## Finding

Theorem. Choose any \(0<r_0<r_1<r_2\) and real \(\delta\) satisfying \(\sin(2\delta)\ne0\). Sample every complex polynomial of degree at most three at the twelve points
\[
\mathcal Z=\{r_0i^k,\ r_1e^{i\delta}i^k,\ r_2i^k:k=0,1,2,3\}.
\]
There are **nonzero** polynomials \(p(z)=a+cz^2\) and \(q(z)=bz+dz^3\) with \(|p(\zeta)|=|q(\zeta)|\) at every \(\zeta\in\mathcal Z\) if and only if
\[
\boxed{r_1^2=r_0r_2.}
\]
In particular, on that geometric progression the twelve intensity measurements **fail phase retrieval** in the full four-dimensional cubic space: the even and odd witnesses are never constant-phase multiples. The converse is specifically for even-versus-odd pairs, **not** for all pairs of cubic polynomials.

Here is a complete description of **every** such pair. Put \(t_j=r_j^2\), and define the elementary symmetric quantities
\[
S_1=t_0+t_1+t_2,\qquad S_2=t_0t_1+t_0t_2+t_1t_2,\qquad S_3=t_0t_1t_2.
\]
At \(t_1^2=t_0t_2\), precisely the pairs
\[
\begin{aligned}
p(z)&=\sqrt C\,u\left(i\sigma\sqrt{S_3}+\sqrt{S_1}\,z^2\right),\\
q(z)&=\sqrt C\,v\left(i\sigma\sqrt{S_2}\,z+z^3\right),
\end{aligned}
\qquad C>0,\quad |u|=|v|=1,\quad\sigma\in\{-1,1\}
\]
share all twelve magnitudes. The independent unit phases \(u,v\) and positive scale \(C\) exhaust the freedom.

A quantitative companion identity holds **without** the geometric-progression assumption. For the displayed canonical polynomials with \(C=1\), \(u=v=1\), and \(\sigma=1\), define
\[
\mathcal E=\sum_{\zeta\in\mathcal Z}\left(|p(\zeta)|^2-|q(\zeta)|^2\right)^2.
\]
Then
\[
\boxed{\mathcal E=16t_1^2\sin^2(2\delta)\left(\sqrt{S_3S_1}-t_1\sqrt{S_2}\right)^2}
\]
and equivalently
\[
\boxed{\mathcal E=\frac{16t_1^4(t_0+t_2)^2\sin^2(2\delta)(t_0t_2-t_1^2)^2}{\left(\sqrt{S_3S_1}+t_1\sqrt{S_2}\right)^2}.}
\]
Thus the squared-intensity discrepancy of this explicit parity pair vanishes **exactly quadratically** in the squared-radius mismatch \(t_0t_2-t_1^2\), with all other parameters held in a nonsingular compact range. This is a witness-specific identity, not a sharp lower or upper singular-value bound for the entire nonlinear measurement map.

## Assumptions and scope

The sample points are complex numbers, \(i^2=-1\), all three radii are strictly positive and distinct in increasing order, and the outer two quadrature grids are aligned. The middle grid is rotated by \(\delta\), and \(\sin(2\delta)\ne0\) rules out the aligned or quarter-turn-degenerate middle grid. Signals are coefficient vectors \((a,b,c,d)\in\mathbb C^4\) identified with degree-at-most-three polynomials. Phaseless data are the twelve real numbers \(|p(\zeta)|^2\). Equivalence means multiplication by one common unit complex scalar; the even and odd subspaces are disjoint except at zero. The theorem classifies parity-crossing witnesses and makes a sufficient noninjectivity claim for the full cubic space at resonance. It does not classify arbitrary non-parity pairs off resonance.

## Proof

For \(p(z)=a+cz^2\), \(q(z)=bz+dz^3\), put \(U=\overline a c\), \(V=\overline b d\), and, for real \(t\),
\[
D(t)=|a|^2-|b|^2t+|c|^2t^2-|d|^2t^3.
\]
At \(z=\sqrt t\,e^{i\theta}\) direct expansion gives the exact identity
\[
|p(z)|^2-|q(z)|^2=D(t)+2t\operatorname{Re}\bigl((U-tV)e^{2i\theta}\bigr). \tag{1}
\]
Each set of four angles \(\theta=\phi+k\pi/2\) changes the sign of the second term in (1) and has mean zero. Equality at all four points therefore forces \(D(t_j)=0\) for each \(j=0,1,2\). If \(D\) vanished identically, its four alternating-sign coefficient squares would all vanish, contradicting the hypothesis that \(p,q\) are nonzero. Since \(t_0,t_1,t_2\) are distinct and \(\deg D\le3\), necessarily
\[
D(t)=C(t_0-t)(t_1-t)(t_2-t),\qquad C>0.
\]
The leading coefficient gives \(|d|^2=C>0\). Equating the other coefficients yields
\[
|a|^2=CS_3,\qquad |b|^2=CS_2,\qquad |c|^2=CS_1,\qquad |d|^2=C. \tag{2}
\]
In particular, \(U,V\ne0\), with \(|U|=C\sqrt{S_3S_1}\) and \(|V|=C\sqrt{S_2}\).

On the two aligned outer grids, the alternating term in (1) vanishes precisely when \(\operatorname{Re}(U-t_0V)=\operatorname{Re}(U-t_2V)=0\). Because \(t_0\ne t_2\), these equations imply \(\operatorname{Re}U=\operatorname{Re}V=0\). On the middle grid the corresponding condition is
\[
\operatorname{Re}\bigl((U-t_1V)e^{2i\delta}\bigr)=0.
\]
Since \(U-t_1V\) is purely imaginary and \(\sin(2\delta)\ne0\), it follows that \(U=t_1V\). Taking magnitudes and using (2) gives \(S_3S_1=t_1^2S_2\). But direct expansion proves
\[
S_3S_1-t_1^2S_2=t_1(t_0+t_2)(t_0t_2-t_1^2). \tag{3}
\]
Every factor outside the last parenthesis is positive, hence \(t_0t_2=t_1^2\), i.e. \(r_1^2=r_0r_2\). This proves necessity.

Conversely suppose \(t_1^2=t_0t_2\). Equation (3) gives \(\sqrt{S_3S_1}=t_1\sqrt{S_2}\). For any \(C>0\), unit phases \(u,v\), and common sign \(\sigma\), the displayed pair has coefficients satisfying (2), so its \(D\) is the cubic \(C\prod_j(t_j-t)\). Its mixed coefficients are \(U=-i\sigma C\sqrt{S_3S_1}\) and \(V=-i\sigma C\sqrt{S_2}\). At the middle radius \(U=t_1V\), and at the two outer radii \(U-t_jV\) is purely imaginary. Hence (1) vanishes at all four sampled angles on each ring. Conversely the phase of \(U\) and \(V\) must be the same choice of \(\pm i\) and (2) fixes all amplitudes, proving the claimed exhaustive parameterization. Because \(p\) has only even and \(q\) only odd powers and both are nonzero, they cannot differ by a unit scalar.

For the quantitative identity, take the canonical pair without imposing (3). Its coefficients still make \(D(t)=\prod_j(t_j-t)\), which vanishes at all three sampled radii. Again \(U=-i\sqrt{S_3S_1}\) and \(V=-i\sqrt{S_2}\). At the outer aligned grids the second term in (1) vanishes; at the middle grid its four values are alternating signs of \(2t_1\sin(2\delta)(\sqrt{S_3S_1}-t_1\sqrt{S_2})\). Squaring and summing gives the first expression for \(\mathcal E\). Rationalizing the difference of square roots and using (3) proves the second expression exactly. No approximation enters.

## Verification

Run the standalone `CHECK.py` with Python 3 and SymPy available: `python CHECK.py`. It checks the factorization and identity (3) symbolically, directly evaluates twelve-point intensities for four representative radius triples at six angular offsets, verifies the exact residual formula, and tests eighty reproducibly seeded random geometric-progression examples. The finite experiments corroborate the elementary universal proof and do not substitute for it. At \((r_0,r_1,r_2)=(1,2,4)\), one exact ambiguity is \(p(z)=8i+\sqrt{21}z^2\), \(q(z)=2i\sqrt{21}z+z^3\) for every eligible middle rotation.

## Relationship to prior work

Finite complex phase retrieval asks whether a collection of intensity measurements identifies an unknown coefficient vector up to global phase. Kim's 2026 explicit polynomial-evaluation design in \(\mathbb C^6\) and Conca–Edidin–Hering–Vinzant's generic \(4d-4\) theorem motivate studying special structured measurement patterns: generic injectivity at twelve measurements in complex dimension four does **not** guarantee injectivity for every concentric sampling design. Chalendar and Partington's two-circle uniqueness concerns complete circles, not these finite quadrature samples. The contribution here is the exact radial resonance, exhaustive parity-crossing witnesses and explicit off-resonance discrepancy for this twelve-point architecture.

## Limitations

Off the geometric progression, this theorem excludes only nonzero ambiguity pairs consisting of one even and one odd cubic. It does **not** establish phase retrieval for the full cubic space there, nor determine the smallest singular value or an optimal stability constant. The quadratic discrepancy is for the specified canonical witness pair, not a globally sharp modulus condition number. A literature search cannot guarantee publication priority, and the same identity may exist in older specialized phaseless polynomial sampling literature. The result covers only the aligned outer quadrature grids with a nondegenerately rotated middle quadrature grid; it does not cover unequal angular grids, more radii or higher polynomial degree.

## References

1. M. Kim, *Nineteen vectors and their phase-retrieval injectivity in* \(\mathbb C^6\), arXiv:2608.06822v1 (first public August 7, 2026), https://arxiv.org/abs/2608.06822.
2. A. Conca, D. Edidin, M. Hering, C. Vinzant, *An Algebraic Characterization of Injectivity in Phase Retrieval*, arXiv:1312.0158v1 (2013), https://arxiv.org/abs/1312.0158.
3. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (2024), https://arxiv.org/abs/2403.16255.
4. M. Huang, *Phase Retrieval in* \(\mathbb C^4\) *Requires Exactly Eleven Measurements*, arXiv:2607.27719 (2026), https://arxiv.org/abs/2607.27719 (abstract consulted only).
