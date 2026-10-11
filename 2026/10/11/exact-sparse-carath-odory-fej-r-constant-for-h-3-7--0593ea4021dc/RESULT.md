# Exact sparse Carathéodory–Fejér constant for \(H=\{3,7\}\)
## Finding
Consider the sparse Carathéodory–Fejér quantity
\[
M(\{3,7\})=\sup\left\{a:\exists b,c\in\mathbb R,\ 1+a\cos\theta+b\cos(3\theta)+c\cos(7\theta)\ge0\ \text{for every }\theta\in\mathbb R\right\}.
\]
Then
\[
M(\{3,7\})=\frac{5+3\sqrt5}{10}.
\]
The extremizer is unique and is given by
\[
a_*=\frac{5+3\sqrt5}{10},\qquad
b_*=\frac{15-11\sqrt5}{50},\qquad
c_*=\frac{5-2\sqrt5}{25}.
\]

Equivalently, if \(\psi:\mathbb Z\to\mathbb R\) is positive definite, \(\psi(0)=1\), and \(\operatorname{supp}\psi\subseteq\{0,\pm1,\pm3,\pm7\}\), then
\[
\psi(1)\le\frac{5+3\sqrt5}{20},
\]
with equality only for \(2\psi(3)=b_*\) and \(2\psi(7)=c_*\).

## Assumptions and scope
All coefficients are real and nonnegativity is required on the entire circle, not merely on a finite grid. The constant Fourier coefficient is normalized to \(1\), and the distinguished coefficient is that of the first cosine harmonic. The allowed higher harmonics are exactly \(3\) and \(7\).

## Proof
Put
\[
r=\cos\!\left(\frac{\pi}5\right)=\frac{1+\sqrt5}4,
\qquad
s=\cos\!\left(\frac{2\pi}5\right)=\frac{\sqrt5-1}4.
\]
For every feasible \(T\), evaluate at \(\theta=\pi\) and \(\theta=4\pi/5\). Since
\[
(\cos\theta,\cos3\theta,\cos7\theta)=(-1,-1,-1)
\]
at \(\theta=\pi\), while at \(\theta=4\pi/5\) the same triple is \((-r,s,s)\), one has
\[
T(\pi)=1-a-b-c\ge0,
\qquad
T(4\pi/5)=1-ar+s(b+c)\ge0.
\]
Multiplying the first inequality by \(s>0\) and adding gives
\[
0\le sT(\pi)+T(4\pi/5)=1+s-a(r+s).
\]
Therefore
\[
a\le\frac{1+s}{r+s}=\frac{5+3\sqrt5}{10}.
\]

It remains to prove attainment. Write \(x=\cos\theta\), and let \(T_3(x)=4x^3-3x\) and \(T_7(x)=64x^7-112x^5+56x^3-7x\). For the displayed coefficients, direct algebra gives
\[
T_*(x)=\frac{64(5-2\sqrt5)}{25}(x+1)(x+r)^2R(x),
\]
where
\[
R(x)=x^4-\frac{3+\sqrt5}2x^3+\frac{7+7\sqrt5}8x^2-\left(1+\frac{\sqrt5}2\right)x+\frac{25+5\sqrt5}{32}.
\]
To certify \(R(x)>0\) on \([-1,1]\), set \(y=(x+1)/2\). Its degree-five Bernstein representation is
\[
R(2y-1)=\sum_{k=0}^5 q_k\binom5k y^k(1-y)^{5-k},
\]
with
\[
\begin{aligned}
q_0&=\frac{165+65\sqrt5}{32},&
q_1&=\frac{21+17\sqrt5}{32},&
q_2&=\frac{113-3\sqrt5}{160},\\
q_3&=\frac{145-3\sqrt5}{160},&
q_4&=\frac{9+21\sqrt5}{160},&
q_5&=\frac{5+\sqrt5}{32}.
\end{aligned}
\]
Every \(q_k\) is strictly positive. Hence \(R>0\) on \([-1,1]\), so \(T_*\ge0\).

Finally, equality in the upper certificate forces both nonnegative terms \(T(\pi)\) and \(T(4\pi/5)\) to vanish. Thus \(b+c=1-a_*\). The point \(x=-r\) is an interior zero of a nonnegative polynomial, so its derivative also vanishes. Since
\[
T_3'(-r)=\frac32+\frac{3\sqrt5}2,
\qquad
T_7'(-r)=-\frac72-\frac{7\sqrt5}2,
\]
the derivative equation together with \(b+c=1-a_*\) has nonzero determinant \(5+5\sqrt5\), and therefore determines \(b,c\) uniquely as \(b_*,c_*\).

## Verification
The accompanying `artifacts/verify.py` uses only Python's standard library and exact arithmetic in \(\mathbb Q(\sqrt5)\). It checks the two-point upper certificate, the candidate coefficients, the factorization, all six positive Bernstein coefficients, the derivative identities, and uniqueness. A finite numerical scan is neither needed nor used for the universal claim.

## Relationship to prior work
Kolountzakis and Révész formulate the same support-restricted Carathéodory–Fejér problem for arbitrary \(H\subseteq\{2,3,\ldots\}\), and identify its equivalence with pointwise positive-definite extremal problems. Their exact cases include singleton supports, singleton complements, tails, and parity classes, together with a complement duality; none of those stated families evaluates the two-element support \(H=\{3,7\}\). The present result supplies an exact value and equality case for that sparse support.

The sharp certificate is tied to a natural fifth-root resonance: at \(\theta=4\pi/5\), the third and seventh cosine harmonics coincide. This makes the support mathematically distinguished inside the sparse problem rather than an arbitrary numerical slice.

## Limitations
The theorem concerns real even trigonometric polynomials with the specific higher-frequency support \(\{3,7\}\). It does not classify arbitrary two-element supports or complex nonsymmetric coefficient problems. The literature comparison cannot exclude an older equivalent formula hidden under substantially different notation; no such formula was located in the searched support, positive-definite, or dual-extremal formulations.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1, 17 February 2003. Primary MSC 42B10.
2. S. Gy. Révész, *Some trigonometric extremal problems and duality*, Journal of the Australian Mathematical Society 50 (1991), 384–390, DOI:10.1017/S1446788700032985.
