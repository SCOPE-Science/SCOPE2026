# Sharp fourth-moment extension and antipodal phase geometry for finite-field cubic graphs

## Finding
For a finite field \(F=\mathbb F_q\) of characteristic \(p\ge5\), a nontrivial additive character \(\psi\), and the cubic graph \(C=\{(t,t^3):t\in F\}\), put
\[
\mathcal E f(u,v)=\frac1q\sum_{t\in F}f(t)\psi(ut+vt^3).
\]
The sharp complex-valued fourth-moment extension inequality is
\[
\boxed{\sum_{u,v\in F}|\mathcal E f(u,v)|^4\le
\left(3-\frac6{2q+1}\right)
\left(\frac1q\sum_{t\in F}|f(t)|^2\right)^2.}
\]
Every nonzero equality case, and no other input, satisfies
\[
 f(0)\ne0,\qquad |f(t)|^2=\frac23|f(0)|^2,\qquad
 f(t)f(-t)=\frac23f(0)^2\quad(t\ne0).
\]
After division by the nonzero complex scalar \(f(0)\), opposite nonzero pairs may be assigned arbitrary inverse phases; the maximizing family is therefore a torus of real dimension \((q-1)/2\). In particular, optimizers need not be additive characters.

## Assumptions and scope
All sums use counting measure on \(F\) and \(F^2\), and the input \(L^2\) norm is \(\left(q^{-1}\sum_t|f(t)|^2\right)^{1/2}\). The extension normalization is exactly \(q^{-1}\). The field may be any prime-power extension of characteristic greater than three, and the additive character may be arbitrary and nontrivial. The zero input has equality trivially but is not included in the extremizer classification.

## Proof
Write \(S=\sum_{t\in F}|f(t)|^2\), \(Q=\sum_{t\in F}|f(t)|^4\),
\(R=\sum_{t\in F}|f(t)|^2|f(-t)|^2\), and
\(B=\sum_{t\in F}f(t)f(-t)\). For a pair of field elements let \(s=x+y\) and \(w=x^3+y^3\). Since
\[
 w=s^3-3sxy,
\]
if \(s\ne0\), the pair-sum \((s,w)\) determines \(xy\), hence the unordered pair \(\{x,y\}\) uniquely as the roots of a quadratic. If \(s=0\), then \(w=0\) for every pair, and the unique exceptional fiber consists of all antipodal pairs, including \(\{0,0\}\).

Define \(T(s,w)=\sum_{x+y=s,\;x^3+y^3=w}f(x)f(y)\), with ordered summation. Character orthogonality gives
\[
\sum_{u,v\in F}|\mathcal E f(u,v)|^4
 =q^{-2}\sum_{s,w\in F}|T(s,w)|^2.
\]
Without the exceptional fiber, the usual unordered-pair decomposition would contribute \(2S^2-Q\). The contribution of this fiber if all pairs were separated is \(2R-|f(0)|^4\), whereas its actual contribution is \(|B|^2\). Consequently the following **exact identity** holds for every complex input:
\[
\sum_{s,w}|T(s,w)|^2
=2S^2-Q-2R+|f(0)|^4+|B|^2.\tag{1}
\]

For \(S>0\), normalize \(S=1\) by dividing the input by \(\sqrt S\). Set \(m=(q-1)/2\) and \(a=|f(0)|^2\). Choose one representative \(x_j\) from each nonzero pair \(\{t,-t\}\), and write
\[
 u_j=|f(x_j)|^2+|f(-x_j)|^2,\qquad
 v_j=2|f(x_j)f(-x_j)|,\qquad U=\sum_j u_j=1-a,\qquad V=\sum_jv_j.
\]
Here \(0\le v_j\le u_j\), so \(0\le V\le U\). With \(b=|B|\), equation (1) becomes the exact quotient
\[
 \mathcal R(f):=\frac{\sum_{s,w}|T(s,w)|^2}{S^2}
 =2-2a^2-\sum_{j=1}^m\left(u_j^2+\frac12v_j^2\right)+b^2.\tag{2}
\]
By the triangle inequality \(b\le a+V\), and by Cauchy--Schwarz
\(\sum_j u_j^2\ge U^2/m\) and \(\sum_jv_j^2\ge V^2/m\). Therefore
\[
 \mathcal R(f)\le 2-2a^2-\frac{U^2}{m}-\frac{V^2}{2m}+(a+V)^2=:F(a,V).
\]
For fixed \(a\), the derivative with respect to \(V\) is \(2a+(2-1/m)V\ge0\), hence \(F(a,V)\le F(a,U)\). As \(a+U=1\),
\[
\mathcal R(f)\le3-2a^2-\frac3{2m}(1-a)^2.
\]
This strictly concave quadratic attains its maximum at \(a_*=3/(4m+3)=3/(2q+1)\), where the maximum is \(K_q=3-6/(2q+1)\). This proves the inequality and its sharp value once the equality cases below are supplied.

For clarity, the argument proves a quantitative **exact deficit decomposition**, not merely a chain of estimates. Using the normalized quantities above, with \(b=|B|/S\) if working before normalization, one has
\[
\begin{aligned}
K_q-\mathcal R(f)={}&(a+V)^2-b^2
+\sum_j(u_j-U/m)^2
+\frac12\sum_j(v_j-V/m)^2\\
&+(U-V)\left[2a+\left(1-\frac1{2m}\right)(U+V)\right]
+\left(2+\frac3{2m}\right)(a-a_*)^2.
\end{aligned}\tag{3}
\]
Every term on the right is nonnegative, and direct expansion of (2) proves equality of the two sides. In particular an optimizer has \(a=a_*>0\); since the fourth term then vanishes only when \(U=V\), every opposite pair has equal entry moduli. Equality in the other terms gives \(u_j=U/m\) for each \(j\) and alignment of all complex summands in \(B=f(0)^2+2\sum_jf(x_j)f(-x_j)\). Therefore the pair products all have the phase of \(f(0)^2\), and elementary normalization yields
\[
|f(t)|^2=\frac23|f(0)|^2,\qquad
f(t)f(-t)=\frac23 f(0)^2\quad(t\ne0).
\]
Conversely these identities make every term in (3) vanish. An explicit extremizer is \(f(0)=\sqrt3\) and \(f(t)=\sqrt2\) at all nonzero \(t\). Fixing \(f(0)=\sqrt3\), every pair is \(f(x_j)=\sqrt2 e^{i\theta_j}\) and \(f(-x_j)=\sqrt2e^{-i\theta_j}\), with arbitrary \(\theta_j\). This parametrizes all projective maximizers and finishes the proof.

## Verification
The attached standalone `checker.py` uses only the Python standard library and may be run with `python3 checker.py`. It builds prime fields of orders \(5,7,11,13,17\) and extension fields of orders \(25,49\), verifies the pair-sum fiber structure and the convolution identity, tests random complex data, checks arbitrary opposite-pair phases at equality, and independently calculates the original Fourier transform for three field sizes. It reports `PASS 1588 checks; direct Fourier checks for q=5,7,25`. The exact identities (1)--(3), not finite tests, prove the theorem for every eligible finite field.

## Relationship to prior work
Hughes and Wooley, *Discrete restriction for \((x,x^3)\) and related topics*, arXiv:1911.12262v1, studies the analogous integer cubic curve with a tenth-moment estimate. Its two-sum identity motivates the present exceptional-pair analysis, but its integer-range estimates do not state this finite-field sharp fourth-moment constant or equality geometry. Koh and Shen, arXiv:1003.4240v3, establish finite-field algebraic-curve extension estimates in exponent ranges under geometric hypotheses; those estimates do not specify the present finite-size optimal coefficient and opposite-pair equality classification. Higher-dimensional finite-field moment-curve endpoint results, including arXiv:2508.08377v1, use a different curve and moment. The present result is not implied by a constant-coefficient fourth-moment calculation: the best input has nonuniform modulus. No claim of independent external verification is made.

## Limitations
The proof requires the invertibility of \(2\) and \(3\) in the field; it makes no assertion in characteristic two or three. It concerns precisely the fourth moment and the cubic graph; it does not yield a complete range of extension estimates at other exponents. The literature comparison is not an exhaustive uniqueness certificate: an equivalent earlier theorem under different language may exist. Numerical checks are finite corroborations, not a substitute for the algebraic proof.

## References
Hughes, K., and Wooley, T. *Discrete restriction for \((x,x^3)\) and related topics*. arXiv:1911.12262v1 (first posted 2019-11-27), https://arxiv.org/abs/1911.12262.

Koh, D., and Shen, C.-Y. *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*. arXiv:1003.4240v3, https://arxiv.org/abs/1003.4240.

Biswas et al. *Sharp endpoint extension inequalities for the moment curve on finite fields*. arXiv:2508.08377v1, https://arxiv.org/abs/2508.08377.
