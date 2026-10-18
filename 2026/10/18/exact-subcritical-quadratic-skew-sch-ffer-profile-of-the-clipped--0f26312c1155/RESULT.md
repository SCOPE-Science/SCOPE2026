# Exact subcritical quadratic skew Schäffer profile of the clipped Euclidean plane

## Finding
Equip the real plane \(X=(\mathbb R^2,N)\) with the Banaś–Frączek norm
\[
N(s,t)=\max\{\sqrt2|s|,\sqrt{s^2+t^2}\}.
\]
For \(0\le r\le1\), let the quadratic skew Schäffer constant be
\[
\mathcal S(r)^2=\min_{N(x)=N(y)=1}
\frac{N(x+ry)^2+N(rx-y)^2}{2}.
\]
Put \(r_c=\sqrt{2-\sqrt3}=(\sqrt3-1)/\sqrt2\). For \(0<r<r_c\) set
\[
U_r=\frac{1-r\sqrt{1-r^2+r^4}}{1+r^4}.
\]
Then the **complete exact profile**, including the previously unevaluated strict regime, is
\[
\boxed{\mathcal S(r)^2=\begin{cases}
\dfrac{(1+r^2)^2}{2}\bigl(1+(1-r^2)U_r^2\bigr),&0<r<r_c,\\[4pt]
\dfrac34(1+r^2),&r_c\le r\le1,
\end{cases}}
\]
with \(\mathcal S(0)=1\). The two branches join continuously at \(r_c\). For the first branch an explicit minimizing pair has one point on the flat face of the unit sphere and the other on its circular arc; **both transformed output vectors are situated on the two diagonal corner rays** of the same norm.

## Assumptions and scope
All vectors are real and the mean exponent is exactly two. The norm is a Euclidean disk clipped by the strip \(|s|\le 1/\sqrt2\); the unit sphere consists of two vertical segments and two circular arcs. No claim is made for different clipping parameters, nonquadratic means, or complex scalars. The scalar parameter satisfies \(0\le r\le1\). The strict regime \(0<r<r_c\) is the principal new contribution.

## Proof
**1. Exact objective identity and reduction to mixed input strata.** Write \(x=(a,b)\), \(y=(c,d)\) and \(q=1+r^2\), \(f=1-r^2\). The identity \(N(s,t)^2=s^2+\max\{s^2,t^2\}\), followed by \(|A|+|B|=\max\{|A+B|,|A-B|\}\), gives
\[
\begin{split}
4F_r(x,y)&:=2\bigl(N(x+ry)^2+N(rx-y)^2\bigr)\\
&=q\bigl[(a^2+b^2+c^2+d^2)+2(a^2+c^2)\bigr]\\
&\quad+\max\bigl\{q|\Delta_x+\Delta_y|,\ |f(\Delta_x-\Delta_y)+4r(ac-bd)|\bigr\},
\end{split}
\]
where \(\Delta_x=a^2-b^2\) and \(\Delta_y=c^2-d^2\). (The notation \(4F_r\) here equals four times the squared objective.) In particular,
\[
F_r(x,y)\ge \frac q2\max\bigl\{\|x\|_2^2+\|y\|_2^2,\ 2(a^2+c^2)\bigr\}.
\]
If both unit inputs lie on circular arcs, the first maximum entry is two; if both lie on flat faces, its second entry is two. Consequently either type gives \(F_r\ge q\). The constructed mixed witnesses below satisfy \(F_r<q\) whenever \(0<r<r_c\). Hence it is enough to minimize over a mixed pair. Using the exact invariance \((x,y)\mapsto(y,-x)\), the simultaneous coordinate reflections, and the possible coordinate signs, we may take the flat input \(x=(1/\sqrt2,u)\) with \(0\le u\le1/\sqrt2\), and the circular input \(y=(c,d)\) with \(|c|=v\in[0,1/\sqrt2]\), \(|d|=\sqrt{1-v^2}=:d_+\). For such input pairs, the identity implies the universally valid lower estimate
\[
4F_r\ge \frac{q}{1}\Big(\frac52+u^2+2v^2\Big)
+\max\Big\{q|2v^2-\frac12-u^2|,\ f(\frac32-u^2-2v^2)-4r(\frac{v}{\sqrt2}+u\sqrt{1-v^2})\Big\}.\tag{1}
\]
Here we used \(ac-bd\ge-(v/\sqrt2+u d_+)\); the second argument of the maximum need not be nonnegative.

**2. Radical witness.** Fix \(0<r<r_c\). Write \(z=r^2\), \(U=U_r\), \(t=1-U\). Direct expansion shows
\[
(1+z^2)U^2-2U+1-z=0,
\qquad t^2=z-U^2z^2.\tag{2}
\]
Since the first polynomial is positive at \(U=1/2\) and negative at \(U=1\) in the stated range, its smaller root satisfies \(1/2<U<1\). Define
\[
u=\frac{2U-1}{\sqrt2},\quad
v=\frac{1-(1+z)U}{\sqrt2 r},\quad
d_+=\frac{1-(1-z)U}{\sqrt2 r}.\tag{3}
\]
Equation (2) implies \(v^2+d_+^2=1\). Moreover \(0<u<1/\sqrt2\), \(0<v<1/\sqrt2\). To check the latter, the polynomial in (2) has negative value at \(1/(1+z)\), so its smaller root satisfies \(U<1/(1+z)\), giving \(v>0\). It has positive value \(2r^3(1-r)(1+r)/(1+r^2)^2\) at \((1-r)/(1+r^2)\), which is below its vertex; hence the smaller root exceeds this test value and \(v<1/\sqrt2\). Thus \(x=(1/\sqrt2,u)\) and \(y=(-v,d_+)\) are unit vectors.

Put \(h=qU/\sqrt2\), \(k=q(1-U)/(\sqrt2 r)\). From (3), direct substitution gives
\[
x+ry=(h,h),\qquad rx-y=(k,-k).\tag{4}
\]
Both outputs lie on corner rays where the two defining branches of \(N\) agree, and their objective is \(h^2+k^2\). Using (2), this simplifies to
\[
F_r(x,y)=\frac{q^2}{2}\left(U^2+\frac{(1-U)^2}{z}\right)
=\frac{q^2}{2}\bigl(1+(1-z)U^2\bigr)=:F_* .\tag{5}
\]
Also \(u,v<1/\sqrt2\) implies \(F_*<q\), as noted in Step 1.

**3. A global two-variable dual certificate.** The remaining task is to show (1) cannot fall below (5). Let \(t=1-U\) and \(z=r^2\), and define exact nonnegative certificate weights
\[
\ell=-\frac{t^2-Uz}{t(t-z)},\qquad
\mu=\frac{(1-2t)(Uz+t)(t-Uz)}{t(t-z)}.\tag{6}
\]
All denominators are positive: from (2), \(t^2=z(1-U^2z)>z^2\) because \(0<z<2-\sqrt3<1/2\), so \(t>z\). Then \(-1<\ell<0\), \(\mu>0\), and
\[
1+\ell-\mu=\frac{2(1-2t)U^2z^2}{t(t-z)}>0.\tag{7}
\]
In particular \(|\ell|+\mu<1\). Therefore the maximum on the right side of (1) is at least \(\ell q(2v^2-1/2-u^2)+\mu[f(3/2-u^2-2v^2)-4r(v/\sqrt2+u\sqrt{1-v^2})]\) for **every** feasible \(u,v\).

Set
\[
A=q(1-\ell)-\mu f,\qquad B=2q(1+\ell)-2\mu f.\tag{8}
\]
It follows that \(4F_r\) is bounded below by the explicit constant
\(K=5q/2-\ell q/2+3\mu f/2\) plus
\[
A u^2+B v^2-4\mu r\left(u\sqrt{1-v^2}+\frac v{\sqrt2}\right).\tag{9}
\]
Denote the witness coordinates in (3) by \(u_*,v_*\), and \(d_*=\sqrt{1-v_*^2}\). A substitution of (2), (3), (6), (8) gives the two exact stationarity identities
\[
2Au_*=4\mu r d_*,\qquad
2Bv_*+4\mu r\frac{u_*v_*}{d_*}=\frac{4\mu r}{\sqrt2}.\tag{10}
\]
These also show \(A=2\mu r d_*/u_*>0\) and \(B=2\mu r(1/(\sqrt2v_*)-u_*/d_*)>0\): the second positivity follows from \(d_*>1/\sqrt2\) and \(u_*,v_*<1/\sqrt2\). Completing squares in (9), its difference from the same expression at \((u_*,v_*)\) is exactly
\[
A\left(u-\frac{2\mu r\sqrt{1-v^2}}A\right)^2
+\left(B+\frac{4\mu^2r^2}A\right)(v-v_*)^2\ge0.\tag{11}
\]
(Equality in (11) means that the explicit quadratic lower certificate has its global minimum at the witness.) At the witness both absolute-value arguments in (1) vanish, by (4), so the lower certificate equals the actual objective \(F_*\). Equations (1)–(11) prove \(\mathcal S(r)^2=F_*\) for every \(0<r<r_c\).

**4. Endpoint and the saturated branch.** At \(r=0\), \(N(x)=N(y)=1\) forces \(\mathcal S(0)=1\). Letting \(r\uparrow r_c\) in (2) gives \(U\downarrow1/2\) and \(F_*\to3(1+r_c^2)/4\). For \(r\in[r_c,1]\), the already established sharp lower-envelope saturation theorem for this plane gives \(\mathcal S(r)^2=3(1+r^2)/4\); this final branch can alternatively be established by its published explicit equality witnesses. Together these arguments prove the displayed complete profile.

## Verification
Every step is algebraic or a compact unit-sphere argument; numerical experiments are not used as infinite proofs. An accompanying standalone Python verifier checks the polynomial, normalized witness, dual-weight inequalities, stationarity, and witness objective on 2,000 interior parameter samples, as well as the transition limit. For a reproducibility check, run `python3 verify_profile.py` from this directory using Python 3 with its standard library. The scripts test examples, not the universal inequalities used in the proof.

## Relationship to prior work
Xu and Liu, *Skew Schäffer Type Constants* (arXiv:2610.03050v1, first public 2026-10-02), define the invariant and prove the saturated formula for \(r\ge1/\sqrt2\) at this clipping parameter. The published note *Exact saturation threshold for quadratic skew Schäffer constants on the Banaś–Frączek plane* (published-finding corpus identifier `2026/10/11/SCOPE-exact-saturation-threshold-for-quadratic-skew-sch-ffer-constants--c3c39dc819be`) establishes the optimal saturation boundary \(r_c\), but explicitly does not evaluate the strict interval. A separate published note, *A sharp small-skew phase transition in the Banaś–Frączek plane* (identifier `2026/10/11/SCOPE-a-sharp-small-skew-phase-transition-in-the-bana-fr-czek-plane--4c730d387d65`), gives only the first-order expansion at zero. The present formula provides the exact **whole subcritical curve**, and its two-variable dual certificate is needed to exclude every mixed input pair—not just exhibit the radical witness. Neither known saturation nor an endpoint derivative entails the exact intervening values.

## Limitations
The formula is only for the real quadratic mean at the intrinsically symmetric clipping parameter \(\lambda=\sqrt2\). Extending the radical certificate to arbitrary \(\lambda\) is open here; the result does not supply a general classification of all minimizing pairs. Priority risk remains from unindexed equivalent minimax formulas.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1 (first posted 2026-10-02), §3, Example 3.5; https://arxiv.org/html/2610.03050v1.
2. *Exact saturation threshold for quadratic skew Schäffer constants on the Banaś–Frączek plane*, published-finding corpus record `2026/10/11/SCOPE-exact-saturation-threshold-for-quadratic-skew-sch-ffer-constants--c3c39dc819be`, complete RESULT.md read at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-saturation-threshold-for-quadratic-skew-sch-ffer-constants--c3c39dc819be.
3. *A sharp small-skew phase transition in the Banaś–Frączek plane*, published-finding corpus record `2026/10/11/SCOPE-a-sharp-small-skew-phase-transition-in-the-bana-fr-czek-plane--4c730d387d65`, complete RESULT.md read at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-small-skew-phase-transition-in-the-bana-fr-czek-plane--4c730d387d65.
4. J. Banaś and K. Frączek, *Deformation of Banach spaces*, Comment. Math. Univ. Carolinae 34 (1993), 47–53.
