# Critical pair-symmetric relaxation for proper four-colourings of the 4-regular tree
## Finding
For the four-state antiferromagnetic Potts recursion at zero temperature on the 4-regular tree, let \(F_0\) denote the projective recursion with branching factor \(d=3\). On the positive projective ray
\[
L=\{[r:r:1:1]:r>0\},
\]
the recursion is invariant and is exactly
\[
F_0([r:r:1:1])=[f(r):f(r):1:1],\qquad
f(r)=\frac{r^3+2}{2r^3+1}.
\]
Every \(r_0>0\) satisfies \(f^{\circ n}(r_0)\to1\). If \(r_0\ne1\), then the orbit alternates across \(1\) and obeys the sharp asymptotic
\[
\lim_{n\to\infty}\sqrt n\,\left|f^{\circ n}(r_0)-1\right|=\frac{\sqrt3}2.
\]
Thus the 2+2 colour-symmetric channel is globally attracted to the uniform message even at the zero-temperature critical point \(q=d+1=4\), where the full proper-colouring Gibbs problem is non-unique.

## Assumptions and scope
The state space is the positive projective cone for four Potts messages. The parameter is zero temperature, \(w=0\), and the tree has branching factor \(d=3\), hence degree \(4\). The statement concerns only the invariant ray \(L\); it does not assert uniqueness of the full Gibbs measure, strong spatial mixing, or convergence from arbitrary projective messages. The initial ratio \(r_0\) is any positive real number. The asymptotic constant is asserted only when \(r_0\ne1\).

## Proof
The source defines, for \(q=4\), the projective map \(F=G\circ P\), where \(P(x_1,x_2,x_3)=(x_1^d,x_2^d,x_3^d)\) and
\[
G_1=\frac{w x_1+x_2+x_3+1}{x_1+x_2+x_3+w},\quad
G_2=\frac{x_1+w x_2+x_3+1}{x_1+x_2+x_3+w},\quad
G_3=\frac{x_1+x_2+w x_3+1}{x_1+x_2+x_3+w}.
\]
Setting \(d=3\), \(w=0\), and \((x_1,x_2,x_3)=(r,r,1)\) gives
\[
F_0(r,r,1)=\left(\frac{r^3+2}{2r^3+1},\frac{r^3+2}{2r^3+1},1\right),
\]
which proves invariance of \(L\) and the formula for \(f\).

The derivative is
\[
f'(r)=-\frac{9r^2}{(2r^3+1)^2}<0,
\]
so \(f\) is strictly decreasing and \(f(1)=1\). Write \(g=f\circ f\). Direct rational simplification gives
\[
g(r)=\frac{17r^9+30r^6+24r^3+10}{10r^9+24r^6+30r^3+17}
\]
and
\[
g(r)-r=-\frac{(r-1)^3(r+1)(2r^2-r+2)(5r^4+4r^3+4r+5)}{10r^9+24r^6+30r^3+17}.
\]
Every factor other than \(-(r-1)^3\) is strictly positive for \(r>0\). Hence \(g(r)<r\) for \(r>1\) and \(g(r)>r\) for \(0<r<1\). Since \(f\) is decreasing and fixes \(1\), one also has \(g(r)>1\) for \(r>1\) and \(g(r)<1\) for \(0<r<1\). Therefore the even iterates are monotone toward a positive fixed point of \(g\). The displayed factorization shows that the only positive fixed point is \(1\), so the even iterates converge to \(1\); continuity of \(f\) gives the same for the odd iterates. Strict decrease of \(f\) also gives the alternation across \(1\).

For the rate, put \(r=1+u\). Taylor expansion of the exact rational function gives
\[
g(1+u)=1+u-\frac43u^3+O(u^4).
\]
Let \(u_m=f^{\circ 2m}(r_0)-1\). For \(r_0\ne1\), \(u_m\) has fixed sign and tends to zero, so
\[
u_{m+1}=u_m-\frac43u_m^3+O(u_m^4).
\]
Consequently
\[
\frac1{u_{m+1}^2}-\frac1{u_m^2}=\frac83+o(1).
\]
Cesaro summation yields \(m u_m^2\to3/8\). Hence
\[
\sqrt{2m}\,|f^{\circ 2m}(r_0)-1|\to\frac{\sqrt3}2.
\]
Finally, \(f'(1)=-1\), so \(f(1+u)-1=-u+O(u^2)\); the odd subsequence has the same absolute asymptotic constant. This proves the claim.

## Verification
The bundled `verify.py` checks, with exact integer polynomial arithmetic, the rational formula for \(g\), the complete factorization of the numerator of \(g(r)-r\), and the cubic Taylor coefficient \(-4/3\) at \(r=1\). These checks replay algebra used in the proof; the infinite-orbit conclusion follows from the sign and asymptotic arguments above, not from finite sampling.

## Relationship to prior work
De Boer, Buys and Regts give the projective Potts tree recursion and discuss the exceptional case \((q,d)=(4,3)\); their paper proves positive-temperature uniqueness only for \(q=4,d\ge4\) and explicitly notes that their method does not handle \(q=4,d=3\). Gu, Wu and Yang subsequently prove the full positive-temperature uniqueness threshold and an exact \(1/2\) critical exponent when the critical Gibbs state is unique, but their theorem excludes the zero-temperature critical case \(q=d+1\), where proper colourings are non-unique. Jonasson's colouring theorem establishes this global non-uniqueness at \(q=d+1\), but does not give the pair-symmetric projective-ray dynamics or its sharp amplitude. The present statement isolates a marginally stable symmetry channel exactly at that non-unique endpoint.

## Limitations
The result is one-dimensional inside the three-dimensional positive projective ratio space and therefore cannot imply full Gibbs uniqueness. It does not classify the frozen or semitranslation-invariant mechanisms responsible for non-uniqueness. The exact amplitude concerns projective message ratio \(r\), not a universal amplitude for every physical observable. A 1983 Bethe-lattice phase-diagram paper is highly relevant background but was available here only through bibliographic/abstract-level material; an equivalent ray calculation there remains a residual originality risk.

## References
1. D. de Boer, P. Buys and G. Regts, *Uniqueness of the Gibbs measure for the 4-state anti-ferromagnetic Potts model on the regular tree*, arXiv:2011.05638v1; DOI:10.1017/S0963548322000207.
2. C. Gu, W. Wu and K. Yang, *Power law decay at criticality for the q-state antiferromagnetic Potts model on regular trees*, arXiv:2112.00573v1.
3. J. Jonasson, *Uniqueness of uniform random colorings of regular trees*, DOI:10.1016/S0167-7152(02)00054-8.
4. F. Peruggi, F. di Liberto and G. Monroy, *The Potts model on Bethe lattices. I. General results*, DOI:10.1088/0305-4470/16/4/018.
