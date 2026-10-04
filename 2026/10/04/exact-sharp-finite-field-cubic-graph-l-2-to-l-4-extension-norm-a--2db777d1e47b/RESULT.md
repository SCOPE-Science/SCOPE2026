# Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers
## Finding
Let \(F\) be a finite field of order \(q\) and characteristic different from \(2\) and \(3\). Let
\[
C=\{(t,t^3):t\in F\}\subset F^2.
\]
Give \(F^2\) counting measure and \(C\) normalized counting measure. Fix a nontrivial additive character \(e:F\to\mathbb C^\times\), and define
\[
Eg(x,y)=\frac1q\sum_{t\in F}g(t)e(xt+yt^3).
\]
Then
\[
R_C^*(2\to4)^4=3-\frac{6}{2q+1}=\frac{3(2q-1)}{2q+1},
\qquad
R_C^*(2\to4)=\left(\frac{3(2q-1)}{2q+1}\right)^{1/4}.
\]
The nonzero extremizers are exactly those for which, writing \(S=\sum_t|g(t)|^2\),
\[
|g(0)|^2=\frac{3S}{2q+1},\qquad |g(t)|^2=\frac{2S}{2q+1}\quad(t\ne0),
\]
and all \(g(t)g(-t)\) have the same argument as \(g(0)^2\).

## Assumptions and scope
The characteristic restrictions are used essentially: characteristic \(3\) destroys the cubic separation identity and characteristic \(2\) changes the antipodal involution. The surface has total mass one and the ambient plane has counting measure. No claim is made in characteristics \(2\) or \(3\).

## Proof
Put \(S=\sum_t|g(t)|^2\). Additive-character orthogonality gives
\[
\|Eg\|_4^4=q^{-2}Q(g),
\]
where
\[
Q(g)=\sum_{a+b=c+d,\;a^3+b^3=c^3+d^3}g(a)g(b)\overline{g(c)g(d)},
\]
while \(\|g\|_{L^2(C)}^4=q^{-2}S^2\). Hence the fourth power of the extension ratio is \(Q(g)/S^2\).

Write \(s=a+b=c+d\). The identity
\[
a^3+b^3=s^3-3abs
\]
shows that if \(s\ne0\), equality of cubic sums forces \(ab=cd\), hence \(\{a,b\}=\{c,d\}\). If \(s=0\), every pair \((a,-a)\) has cubic sum zero. Define
\[
P_4=\sum_a|g(a)|^4,\qquad R=\sum_a|g(a)|^2|g(-a)|^2,\qquad B=\sum_a g(a)g(-a).
\]
The ordinary unordered-pair contribution is \(2S^2-P_4\); its zero-sum part is \(2R-|g(0)|^4\), whereas the actual zero-sum fiber contributes \(|B|^2\). Thus
\[
Q=2S^2-P_4-2R+|g(0)|^4+|B|^2.
\]
Normalize \(S=1\). The nonzero elements split into \(m=(q-1)/2\) pairs \(\{t,-t\}\). Put \(\alpha=|g(0)|^2\). For the \(j\)-th pair let the squared moduli be \(u_j,v_j\), set \(r_j=u_j+v_j\), \(t_j=2\sqrt{u_jv_j}\), and put \(w_j=2g(t)g(-t)\), \(w_0=g(0)^2\). Then
\[
Q=2-2\alpha^2-\sum_jr_j^2-\frac12\sum_jt_j^2+\left|w_0+\sum_jw_j\right|^2.
\]
For fixed magnitudes, the last term is maximal exactly when the \(w_j\) align in phase. After alignment the expression is increasing in each \(t_j\in[0,r_j]\), since the partial derivative is
\[
-t_j+2\left(\alpha+\sum_i t_i\right)\ge0.
\]
Thus a maximizer has \(t_j=r_j\), equivalently \(u_j=v_j\). Since \(\alpha+\sum_jr_j=1\),
\[
Q\le3-2\alpha^2-\frac32\sum_jr_j^2
\le3-2\alpha^2-\frac{3}{2m}(1-\alpha)^2.
\]
The final quadratic is maximized at
\[
\alpha=\frac{3}{4m+3}=\frac{3}{2q+1},
\]
where the subtracted penalty is \(6/(2q+1)\). Equality in Cauchy--Schwarz forces every \(r_j\) to equal \(4/(2q+1)\), and the preceding equality conditions then give \(u_j=v_j=2/(2q+1)\) and common phase for all antipodal products. Conversely these conditions make every inequality an equality.

## Verification
The proof is algebraic and valid over every admitted finite field. The bundled verifier checks the collision fibers for eleven prime fields through \(41\) and checks the closed-form extremizer using exact rational arithmetic. Run `python3 artifacts/verify.py`; the expected output is `VERIFY_OK primes=11 max_prime=41`. The finite replay is corroborative only.

## Relationship to prior work
Mockenhaupt--Tao establish the finite-field restriction normalization and an even-exponent representation-count lemma. Their polynomial-curve application is the full moment curve \((t,t^2,\ldots,t^n)\), and their planar fourth-moment discussion treats the parabola. On the cubic graph the general representation-count lemma sees the \(q\)-fold zero-sum fiber and gives only a coarse bound, not the sharp constant or equality cases.

Hughes--Wooley study the same formal curve \((x,x^3)\) for truncated integers with target torus. Their main theorem concerns high moments, notably a tenth-moment estimate. Their proof records the same zero-sum/nonzero-sum pair algebra, but not this finite-field fourth-moment optimum or its extremizers.

## Limitations
The theorem excludes characteristics \(2\) and \(3\). The originality search found no equivalent published sharp-constant theorem, but older unindexed notes or folklore under different terminology remain a residual risk. The verifier covers prime fields only; the proof supplies the all-finite-field statement.

## References
1. G. Mockenhaupt and T. Tao, “Restriction and Kakeya phenomena for finite fields,” arXiv:math/0204234v1, first public 2002-04-18; Duke Math. J. 121 (2004), 35–74.
2. K. Hughes and T. D. Wooley, “Discrete restriction for \((x,x^3)\) and related topics,” arXiv:1911.12262v1; Int. Math. Res. Not. IMRN (2022).
