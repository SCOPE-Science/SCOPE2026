# Inverse-square parabolic accumulation of a first-generation critical-curve pencil

## Finding

For the continuous, area-preserving planar map
\[
F_{a,b}(x,y)=\begin{cases}(ax-y,x),&x\ge0,\\(bx-y,x),&x<0,\end{cases}
\qquad 0<a<1,
\]
consider the first-generation critical-curve pencil whose word is \(w_m=(a^3b^3)^m a^2\), \(m\ge1\). For each fixed \(a\in(0,1)\), Roberts--Saito--Vivaldi, Theorem 18(ii)(1), establishes a unique legal ordinate \(b_m(a)\). Define
\[
 b_*(a)=\frac{-a+\sqrt{a^2+8(2-a^2)^2}}{2(2-a^2)},\qquad
 d(a)=(1-a b_*)\big[2(2-a^2)b_*+a\big],
\]
\[
 c(a)=\frac{a^2\big[b_*-a(2-a^2)\big]}{(2-a^2)^2},\qquad
 \kappa(a)=\frac a{c(a)}.
\]
All are well-defined and \(1<b_*<\sqrt2\), \(d,c,\kappa>0\). As \(m\to\infty\), **at each fixed** \(a\in(0,1)\),
\[
 \boxed{\;b_*(a)-b_m(a)=\frac{\pi^2}{d(a)\,[m+\kappa(a)]^2}+O_a(m^{-4})\;.}
\]
In particular \(\lim_{m\to\infty}m^2[b_*(a)-b_m(a)]=\pi^2/d(a)\). Thus these infinitely many distinct dynamically legal curves accumulate on an explicit parabolic transfer-matrix locus at an inverse-square rate, with a computable first phase shift. The law is not claimed uniformly as \(a\to0\) or \(a\to1\).

## Assumptions and scope

The parameters obey \(0<a<1\); the asymptotic index \(m\) runs through positive integers. Let
\[
 A=\begin{pmatrix}a&-1\\1&0\end{pmatrix},\quad
 B=\begin{pmatrix}b&-1\\1&0\end{pmatrix},\quad C=B^3A^3,\quad E=A^2,
\]
and initialize the critical ray \(v_0=(0,-1)^\mathsf T\). A parameter is *legal* for \(w_m\) if the orbit follows exactly the indicated branch code until it reaches the positive vertical ray after \(6m+2\) steps. The initial zero coordinate uses the positive-branch convention, which agrees with the source's convention at this ray. The source theorem supplies existence and uniqueness of the legal parameter \(b_m(a)\) for each \(m\); the proof below independently constructs and identifies the relevant root for all sufficiently large \(m\).

## Proof

**1. Parabolic limit and its sign.** Direct multiplication yields
\[
 t(a,b):=\operatorname{tr}(C)
 =a^3b^3-2a^3b-2a^2b^2+2a^2-2ab^3+5ab+2b^2-2
\]
and the factorization
\[
 t(a,b)-2=(ab-1)Q(a,b),\quad
 Q(a,b)=(a^2-2)b^2-ab+4-2a^2.
\]
For fixed \(0<a<1\), \(Q(a,b)\) is strictly decreasing for \(b\ge0\). Its values at \(1\) and \(\sqrt2\) are \(2-a-a^2>0\) and \(-a\sqrt2<0\). Thus the displayed \(b_*\) is the unique positive root of \(Q\), and lies strictly between those endpoints. Moreover \(Q(a,1/a)=-2(a-1/a)^2<0\), hence \(ab_*<1\). Differentiation gives \(t(a,b_*)=2\) and
\[
 \partial_b t(a,b_*)=d(a)>0.
\]
Consequently a neighborhood immediately below \(b_*\) has the elliptic trace \(t=2\cos\theta\) with a small \(\theta>0\), and
\[
 b_*-b=\theta^2/d(a)+O_a(\theta^4).
\]

**2. Negative endpoint coefficient.** Write \(P(a,b)=(EC)_{12}\). Multiplication gives
\[
 P=-(a^2b-a-b)(a^2b^2-2a^2-ab-b^2+2).
\]
Polynomial division by \(Q\) verifies the identity \(P+a=C_{12}\) along \(Q=0\). The same division gives
\[
 C_{12}(a,b_*)=\frac{a^2[a(2-a^2)-b_*]}{(2-a^2)^2}=-c(a).
\]
To see positivity, set \(z=a(2-a^2)\): \(Q(a,z)=(1-a^2)^2(2-a^2)^2>0\), so \(z<b_*\). Thus \(c(a)>0\) and \(P(a,b_*)+a=-c(a)\).

**3. A root before the parabolic boundary.** Since \(\det C=1\), Cayley--Hamilton gives
\[
 C^m=\frac{\sin(m\theta)}{\sin\theta}C
 -\frac{\sin((m-1)\theta)}{\sin\theta}I
\]
for \(t=2\cos\theta\). The target zero-coordinate equation is therefore
\[
 H_m(a,b):=(EC^m)_{12}=
 P(a,b)\frac{\sin(m\theta)}{\sin\theta}
 +a\frac{\sin((m-1)\theta)}{\sin\theta}=0.
\]
At \(b=b_*\), interpreted by continuity, \(H_m=-m c(a)-a<0\). For sufficiently large \(m\), there exists a unique nearby \(b_m^0<b_*\) satisfying \(t(a,b_m^0)=2\cos(\pi/m)\); at this point \(H_m=a>0\). Therefore a zero exists with \(b_m^0<b<b_*\), \(0<\theta<\pi/m\). In that interval \(C_{12}<0\).

**4. The root is dynamically legal.** The vector \(v_m=C^m v_0\) has positive first coordinate, since
\[
 (v_m)_1=-C_{12}\,\frac{\sin(m\theta)}{\sin\theta}>0.
\]
The condition \((Ev_m)_1=0\) therefore forces \(v_m=\gamma(a,a^2-1)^\mathsf T\) for some \(\gamma>0\), and \(Ev_m=(0,\gamma)^\mathsf T\). For every \(0\le j\le m\),
\[
 v_j=C^jv_0=\frac{\sin((m-j)\theta)}{\sin(m\theta)}v_0
 +\frac{\sin(j\theta)}{\sin(m\theta)}v_m.
\]
Both coefficients are nonnegative (and strictly positive for interior \(j\)). At the six successive pre-step positions of one \(A^3B^3\) block, the first coordinates starting from \(v_0\) are
\[
 0,\ 1,\ a,\ a^2-1,\ b(a^2-1)-a,\ (a^2-1)(b^2-1)-ab;
\]
the corresponding first coordinates starting from \(v_m/\gamma=(a,a^2-1)\) are
\[
 a,\ 1,\ 0,\ -1,\ -b,\ 1-b^2.
\]
For \(0<a<1<b\), these first-coordinate signs require exactly the code \(a^3b^3\) at every \(j=0,\ldots,m-1\); the intermediate code decisions are strict, except the legitimate initial boundary point. The final \(A^2\) maps \(v_m\) to the positive vertical ray. Hence this is a legal critical orbit. By the uniqueness assertion in the source's Theorem 18(ii)(1), its ordinate is exactly \(b_m(a)\).

**5. Quantitative phase shift.** Rewriting \(H_m=0\) gives
\[
 [P+a\cos\theta]\sin(m\theta)=a\sin\theta\cos(m\theta).
\]
Near the limiting parameter the bracket is negative and the right-hand sine is positive, hence \(m\theta\in(\pi/2,\pi)\). Put \(\delta=\pi-m\theta\in(0,\pi/2)\). The equation yields
\[
 \tan\delta=\frac{-a\sin\theta}{P+a\cos\theta}
 =\frac a{c(a)}\theta+O_a(\theta^3).
\]
Thus \(\delta=\kappa(a)\theta+O_a(\theta^3)\) and
\[
 (m+\kappa(a))\theta=\pi+O_a(\theta^3),\qquad
 \theta=\frac{\pi}{m+\kappa(a)}+O_a(m^{-4}).
\]
Combining this with the trace Taylor expansion from Step 1 proves the claimed formula, including its \(O_a(m^{-4})\) remainder. \(\square\)

## Verification

The standalone script `critical_pencil_check.py` checks both matrix-polynomial identities by exact symbolic arithmetic, verifies the two root-location sign identities, and evaluates the boundary equation with 65-digit arithmetic at \(a=0.15,0.5,0.9\) and \(m=30,75,150,300\). Direct high-precision step-by-step replay also checks the prescribed orbit signs and positive terminal ray. Numerical calculations support, but do not replace, the preceding analytic argument. Execute it with `python critical_pencil_check.py` after installing `sympy` and `mpmath`.

## Relationship to prior work

Roberts, Saito, and Vivaldi (2021), Theorem 18(ii)(1), establish and parametrize the legal pencil, its common endpoint, and its moving endpoint at \(a=1\); their theorem does not state the present fixed-interior-\(a\) parabolic accumulation formula, coefficient, or phase shift. Their Chebyshev identities are used here as an algebraic technique, with an additional dynamical-legality interpolation argument. Their 2023 work analyzes exact symbolic chains in *rigid rotation coordinates*, not this two-matrix trace limit. Lagarias and Rains analyze rotation-number and invariant-curve dynamics of the same planar family, without the displayed first-generation asymptotic. Garcia-Morato and collaborators study resonance lobes of the same canonical map; full text was inaccessible during this comparison, so potential broader coverage is a material residual risk.

## Limitations

This is a pointwise asymptotic in \(a\in(0,1)\), not a uniform assertion at the endpoints; \(c(a)\) vanishes in endpoint limits and the phase-shift formula requires a different scaling there. The proof does not establish the rate for other first-generation pencils or unrelated mode-locking tongues, nor does it establish a global classification of all real zeros of their continuant polynomials.

## References

1. J. A. G. Roberts, A. Saito, F. Vivaldi, *Critical curves of a piecewise linear map*, arXiv:2104.07197 (first submitted 2021-04-15), especially Theorem 18(ii)(1), Corollary 19, and the appendix. https://arxiv.org/abs/2104.07197
2. J. A. G. Roberts, A. Saito, F. Vivaldi, *Critical curves of rotations*, arXiv:2303.17955 (2023). https://arxiv.org/abs/2303.17955
3. J. C. Lagarias, E. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps I. Rational rotation numbers*, arXiv:math/0301294 (2003); J. Difference Equ. Appl. 11 (2005), 1089--1108. https://arxiv.org/abs/math/0301294
4. L. Benadero Garcia-Morato, E. Freire Macias, E. Ponce Nuñez, F. Torres Peral, *Bifurcation Patterns in Homogeneous Area-Preserving Piecewise-Linear Maps*, Qual. Theory Dyn. Syst. 18 (2019), 547--582. https://doi.org/10.1007/s12346-018-0299-7
