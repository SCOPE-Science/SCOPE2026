# Uniform right-angle exclusion for orthogonal exponentials on the three-ball

## Finding
Let \(J_{3/2}\) be the Bessel function and let \(\beta_n\), \(n\ge1\), be its positive zeros, numbered increasingly. Set
\[
\Delta=\frac{\pi^2}{4}-2-\frac{2}{\pi^2}>0.
\]
For **every** choice of positive integers \(i,j,k\), including repeated indices,
\[
\boxed{\left|\beta_i^2+\beta_j^2-\beta_k^2\right|>\Delta.}
\]
The positive-zero set is also *Sidon*: if \(\beta_i+\beta_j=\beta_k+\beta_\ell\), the multisets of indices \(\{i,j\}\) and \(\{k,\ell\}\) coincide. No positive zero is the sum of two positive zeros.

Let \(B=\{x\in\mathbb R^3:|x|<1\}\). For any three distinct frequencies \(\lambda_1,\lambda_2,\lambda_3\in\mathbb R^3\) such that \(e^{2\pi i\lambda_j\cdot x}\) are pairwise orthogonal in \(L^2(B)\), put \(u=\lambda_1-\lambda_2\) and \(v=\lambda_3-\lambda_2\). Then
\[
\boxed{|u\cdot v|>\frac{\Delta}{8\pi^2}>0.}
\]
The same estimate holds at any of the three vertices, hence the frequency triple is neither right-angled nor collinear. The lower bound is uniform over all frequencies and all zero indices; no optimality of its numerical constant is asserted.

## Assumptions and scope
Every \(\beta_n\) is the unique root of \(\tan x=x\) in \((n\pi,(n+1/2)\pi)\) for \(n\ge1\); the root \(x=0\) is excluded. Orthogonality is ordinary complex \(L^2\) orthogonality with respect to Lebesgue measure on the *unit* ball, and the exponential convention is \(e^{2\pi i\lambda\cdot x}\). The theorem is specific to three spatial dimensions and the Bessel order \(3/2\).

## Proof
**1. Root location and an exact phase defect.** The elementary half-integer Bessel formula gives
\[
J_{3/2}(x)=\sqrt{\frac{2}{\pi x}}\left(\frac{\sin x}{x}-\cos x\right),\quad x>0.
\]
On \((n\pi,(n+1/2)\pi)\), \(\tan x-x\) increases from a negative value to positive infinity, since its derivative is \(\tan^2x>0\) in the interior. Thus one simple root \(\beta_n\) occurs there. Put \(T_n=(n+1/2)\pi\), \(u_n=T_n-\beta_n\), and \(d_n=T_n^2-\beta_n^2\). Since \(\tan\beta_n=\beta_n\),
\[
u_n=\arctan(1/\beta_n),\qquad
 d_n=2\beta_n u_n+u_n^2=2u_n\cot u_n+u_n^2.
\]
We prove the strict, index-independent bounds
\[
\boxed{2<d_n<2+\frac1{\pi^2}.}\tag{1}
\]
Indeed \(0<u_n<1/\beta_n<1/\pi<1/3\). From \(\cos u>1-u^2/2\) and \(\sin u<u\) for \(0<u<1/3\), with \(1-u^2/2>0\), we obtain \(u\cot u>1-u^2/2\). This gives \(d_n>2\). Also \(u_n=\arctan(1/\beta_n)<1/\beta_n\), so \(d_n<2+\beta_n^{-2}<2+\pi^{-2}\). No asymptotic approximation is used.

**2. Squared-zero nonresonance.** For any positive \(i,j,k\), write
\[
\begin{aligned}
\beta_i^2+\beta_j^2-\beta_k^2
&=\frac{\pi^2}{4}\,N-E,\\
N&=(2i+1)^2+(2j+1)^2-(2k+1)^2,\\
E&=d_i+d_j-d_k.
\end{aligned}
\]
Every odd square is congruent to \(1\pmod 8\); hence \(N\equiv1\pmod8\) and therefore either \(N\ge1\) or \(N\le-7\). By (1),
\[
2-\frac1{\pi^2}<E<2+\frac2{\pi^2}.
\]
If \(N\ge1\), the squared-zero expression exceeds \(\pi^2/4-2-2/\pi^2=\Delta\). If \(N\le-7\), it is less than \(-7\pi^2/4-(2-1/\pi^2)<-\Delta\). Finally \(\Delta>0\), since \(\pi>31/10\) implies \(\pi^2>961/100\), and \(s/4-2-2/s\) is increasing for positive \(s\) and positive at \(s=961/100\). This establishes the uniform inequality for **all** indices.

**3. Pair-sum rigidity.** At any positive root \(a\), \(\sin a=a\cos a\) and \(\cos a\ne0\). Therefore for two positive roots \(a,b\),
\[
\sin(a+b)=(a+b)\cos a\cos b\ne0,\qquad
\cot(a+b)=\frac{1-ab}{a+b}.
\]
If \(a+b=c+d\) for positive roots \(c,d\), the two cotangent formulae force \(ab=cd\). Equality of real sums and products makes the unordered pairs equal. Since the roots are all distinct, the corresponding index multisets are equal. If \(a+b\) were itself a positive root \(c\), the identity \(\cot c=1/c\) would force \(ab=0\), impossible.

**4. Fourier-ball geometry.** The Fourier transform of the indicator of \(B\) satisfies, for \(\xi\ne0\),
\[
\int_B e^{2\pi i\xi\cdot x}\,dx
=4\pi\frac{\sin(2\pi|\xi|)-(2\pi|\xi|)\cos(2\pi|\xi|)}{(2\pi|\xi|)^3}.
\]
Thus two distinct exponentials are orthogonal precisely when their frequency separation is \(\beta_n/(2\pi)\) for some \(n\ge1\). For three pairwise orthogonal exponentials, let \(\|u\|=\beta_i/(2\pi)\), \(\|v\|=\beta_j/(2\pi)\), and \(\|u-v\|=\beta_k/(2\pi)\). The polarization identity gives
\[
2u\cdot v=\|u\|^2+\|v\|^2-\|u-v\|^2
=\frac{\beta_i^2+\beta_j^2-\beta_k^2}{4\pi^2},
\]
and therefore \(|u\cdot v|>\Delta/(8\pi^2)\). This rules out right angles at every vertex. If three frequency points were collinear, their three positive pairwise distances would satisfy one exact additive relation. Scaling by \(2\pi\), this would give a positive Bessel zero equal to the sum of two others, excluded in Step 3.

## Verification
The proof relies on exact identities and inequalities, not root enumerations. The included standalone `check_bounds.py` exercises the trigonometric zero equation, (1), finite examples of the squared-difference bound, and the positive constant as numerical sanity checks; it is **not** an infinite proof or independent mathematical certification. Execute with `python3 check_bounds.py` in the extracted file directory.

## Relationship to prior work
Ortega-Cerdà (2026) proves the nonexistence of Riesz bases of exponentials on balls and discusses known global restrictions on orthogonal exponential frequency sets. Its projection-continuity method does not give the present three-point Bessel arithmetic or a uniform inner-product exclusion. Guo–Jiang–Wang–Yang (2024) investigate Bessel-zero estimates and spectral counting on balls, without an assertion about three squared zeros, pair sums, or right angles in orthogonal frequency sets. Binyamini–Kiro–Kozma–Pila (2026; publicly posted after the qualifying September 2026 motivating source) study general Diophantine counts of Bessel-zero tuples; their reported few-solutions bounds do not by themselves imply exact absence or this uniform separation. Classical Bessel zero tables and large-argument asymptotics, such as DLMF §10.21, are background only.

## Limitations
No claim is made for other Bessel orders, other dimensions, nonlinear combinations beyond the displayed squared three-term relation, a sharp separation constant, or orthogonal sets of more than three frequencies. Historical priority remains subject to scrutiny, especially classical spectral-set and Bessel-zero literature. The self-review does not constitute independent validation.

## References
1. J. Ortega-Cerdà, *There are no Riesz bases of exponentials in balls and triangles*, arXiv:2609.18426, first submitted 2026-09-16, https://arxiv.org/abs/2609.18426.
2. J. Guo, T. Jiang, Z. Wang, X. Yang, *Bessel functions and Weyl's law for balls and spherical shells*, arXiv:2412.14059, first submitted 2024-12-18, https://arxiv.org/abs/2412.14059.
3. G. Binyamini, A. Kiro, G. Kozma, J. Pila, *Counting Bessel zeros and applications*, arXiv:2610.28477, first submitted 2026-10-20, https://arxiv.org/abs/2610.28477 (supporting comparison, not qualifying initiating source).
4. NIST Digital Library of Mathematical Functions, §10.21, *Zeros*, https://dlmf.nist.gov/10.21.
