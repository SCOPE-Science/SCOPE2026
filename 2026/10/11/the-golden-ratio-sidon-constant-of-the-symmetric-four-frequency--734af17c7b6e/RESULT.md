# The golden-ratio Sidon constant of the symmetric four-frequency set
## Finding
For
\[
\Lambda=\{0,1,3,4\}\subset\mathbb Z,
\]
define its Fourier-analytic Sidon constant by
\[
S(\Lambda)=\sup_{(a,b,c,d)\ne0}
\frac{|a|+|b|+|c|+|d|}
{\sup_{|z|=1}|a+bz+cz^3+dz^4|}.
\]
Then
\[
S(\Lambda)=\frac{1+\sqrt{5}}{2}.
\]
The constant is attained by
\[
P_*(z)=1+(\sqrt{5}-1)z+(\sqrt{5}-1)z^3-z^4.
\]
Thus the simplest nonzero symmetric four-frequency spectrum, which becomes \(\{-2,-1,1,2\}\) after centering, has an exact sharp coefficient \(\ell^1\)-to-supremum norm constant equal to the golden ratio.

## Assumptions and scope
All coefficients are arbitrary complex numbers, and the supremum is taken over the full unit circle with normalized frequency convention \(z=e^{it}\). No reality, phase, or equal-modulus restriction is imposed.

Write
\[
M=\sup_{|z|=1}|a+bz+cz^3+dz^4|,
\]
and put \(A=|a|\), \(B=|b|\), \(C=|c|\), \(D=|d|\). The proof uses only the standard Fejér--Riesz factorization theorem for nonnegative trigonometric polynomials of degree two.

## Proof
Multiplication by \(z^{-2}\) does not change the supremum norm. With \(z=e^{it}\), set
\[
Q(t)=ae^{-2it}+be^{-it}+ce^{it}+de^{2it}=E(t)+O(t),
\]
where
\[
E(t)=ae^{-2it}+de^{2it},\qquad O(t)=be^{-it}+ce^{it}.
\]
Since \(Q(t+\pi)=E(t)-O(t)\), the parallelogram identity gives, for every \(t\),
\[
M^2\ge \frac{|Q(t)|^2+|Q(t+\pi)|^2}{2}=|E(t)|^2+|O(t)|^2.
\]
Consequently
\[
M^2\ge A^2+B^2+C^2+D^2+
\max_{|w|=1}2\Re(Uw+Vw^2),
\]
for complex numbers \(U,V\) with \(|U|=BC\) and \(|V|=AD\).

We need the following sharp two-harmonic envelope. If \(|U|=q\) and \(|V|=p\), then
\[
\max_{|w|=1}2\Re(Uw+Vw^2)\ge m(q,p),
\]
where
\[
m(q,p)=
\begin{cases}
2p+\dfrac{q^2}{4p},&0\le q\le4p,\ p>0,\\[6pt]
2q-2p,&q\ge4p,
\end{cases}
\]
with the second formula also covering \(p=0\).

To prove the envelope, let \(H\) denote the maximum on the left. The trigonometric polynomial
\[
H-2\Re(Uw+Vw^2)
\]
is nonnegative and has degree at most two, so Fejér--Riesz factorization writes it as
\[
|r+sw+tw^2|^2.
\]
Put \(x=|r|\), \(y=|s|\), \(z=|t|\). Comparison of the second and first Fourier coefficients yields
\[
xz=p,\qquad q\le y(x+z),
\]
while comparison of the constant coefficient gives
\[
H=x^2+y^2+z^2.
\]
Hence, with \(u=(x+z)^2\ge4p\),
\[
H\ge u-2p+\frac{q^2}{u}.
\]
Minimizing this elementary expression over \(u\ge4p\) gives exactly the two displayed branches of \(m(q,p)\).

Now put
\[
x=A+D,\qquad y=B+C,\qquad p=AD,\qquad q=BC.
\]
If \(q\le4p\), then
\[
M^2\ge x^2+y^2-2q+\frac{q^2}{4p}.
\]
Since \(p\le x^2/4\), this is at least
\[
x^2+y^2-2q+\frac{q^2}{x^2}.
\]
Also \(q\le y^2/4\) and, in this branch, \(q\le x^2\). If \(y\le2x\), the last expression is therefore at least
\[
x^2+\frac{y^2}{2}+\frac{y^4}{16x^2}.
\]
Writing \(r=y/x\in[0,2]\), we obtain
\[
\frac{(x+y)^2}{M^2}\le
\frac{(1+r)^2}{1+r^2/2+r^4/16}.
\]
Its derivative has the sign of \(-(r^2+2r-4)\), so its maximum occurs at \(r=\sqrt{5}-1\) and equals
\[
\frac{3+\sqrt{5}}{2}=\left(\frac{1+\sqrt{5}}{2}\right)^2.
\]
If instead \(y\ge2x\), the same branch gives \(M^2\ge y^2\), and hence
\[
\frac{(x+y)^2}{M^2}\le\frac94<\frac{3+\sqrt{5}}{2}.
\]

If \(q\ge4p\), then
\[
M^2\ge x^2+y^2-4p.
\]
Because \(p\le\min(x^2/4,y^2/16)\), this gives \(M^2\ge y^2\) when \(y\ge2x\), again yielding the bound \(9/4\). When \(y\le2x\), it gives
\[
M^2\ge x^2+\frac{3y^2}{4}.
\]
Thus, for \(r=y/x\in[0,2]\),
\[
\frac{(x+y)^2}{M^2}\le\frac{(1+r)^2}{1+3r^2/4}\le\frac73<\frac{3+\sqrt{5}}{2}.
\]
Combining the cases proves
\[
|a|+|b|+|c|+|d|\le\frac{1+\sqrt{5}}{2}\,M.
\]

It remains to show sharpness. Let \(\rho=\sqrt{5}-1\) and
\[
P_*(z)=1+\rho z+\rho z^3-z^4.
\]
After multiplication by \(e^{-2it}\),
\[
|P_*(e^{it})|^2=4\cos^2t\bigl(\rho^2+4\sin^2t\bigr).
\]
For \(s=\sin^2t\), the right side is \(4(1-s)(\rho^2+4s)\), whose maximum on \([0,1]\) occurs at
\[
s=\frac{\sqrt{5}-1}{4}
\]
and equals \((5-\sqrt{5})^2\). Therefore
\[
\|P_*\|_\infty=5-\sqrt{5},
\qquad
\|\widehat P_*\|_1=2\sqrt{5},
\]
and
\[
\frac{2\sqrt{5}}{5-\sqrt{5}}=\frac{1+\sqrt{5}}{2}.
\]
This attains the upper bound.

## Verification
The accompanying `verify.py` checks the quadratic-field identities in the sharpness calculation, the two one-variable profile maxima used in the upper bound, and a finite random numerical stress test of the final inequality. The numerical stress test is only corroborative; the proof for arbitrary complex coefficients is the analytic argument above.

The critical nonstandard reduction is the two-harmonic envelope. Its proof is included explicitly and depends only on Fejér--Riesz factorization and a one-variable minimization; no numerical optimization is used to certify the theorem.

## Relationship to prior work
Neuwirth's trigonometric-trinomial work gives the exact Sidon constant of every three-frequency integer set and records the classical exact value \(2\) for the five-term consecutive set \(\{0,1,2,3,4\}\). Its four-term methods do not contain the present spectrum or the two-harmonic envelope above. The earlier three-element paper likewise stops at three frequencies.

A recent note of Neuwirth studies the distinct consecutive four-frequency support \(\{0,1,2,3\}\). The present set is not an affine image of that support: after centering, it is the symmetric nonzero spectrum \(\{-2,-1,1,2\}\). Targeted literature searches under the original support, the centered support, Sidon-constant terminology, unconditional-constant terminology, and missing-middle-frequency terminology located no implication-equivalent result.

Finite-cyclic results with four characters are not covering: reducing frequencies modulo a finite group changes the supremum domain and can introduce aliasing. Likewise, previously checked harmonic-frame results involving the set \(\{0,1,3,4\}\) concern full-spark minors, not the coefficient \(\ell^1\)-to-supremum norm.

## Limitations
The theorem determines the constant and gives an explicit attaining polynomial, but it does not classify every extremizing coefficient vector. It is specific to this four-frequency support; no formula for arbitrary four-element subsets of \(\mathbb Z\) is claimed. The originality check cannot exclude an older unindexed occurrence under substantially different notation, and this remains the principal residual literature risk.

## References
S. Neuwirth, “The maximum modulus of a trigonometric trinomial,” arXiv:math/0703236v1, submitted 2007-03-08; Journal d'Analyse Mathématique 104 (2008), 371–396.

S. Neuwirth, “The Sidon constant of sets with three elements,” arXiv:math/0102145v1, submitted 2001-02-19.

S. Neuwirth, “On the (Fourier analytic) Sidon constant of \(\{0,1,2,3\}\),” arXiv:2603.28229v1, submitted 2026-03-30.
