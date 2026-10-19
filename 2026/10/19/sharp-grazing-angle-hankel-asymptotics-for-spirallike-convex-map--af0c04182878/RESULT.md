# Sharp grazing-angle Hankel asymptotics for spirallike-convex maps

## Finding

Let \(\mathcal C_\beta\) consist of normalized analytic functions
\(f(z)=z+\sum_{n\ge2}a_nz^n\) on the unit disk for which \(f'\) does not
vanish and
\[
 \operatorname{Re}\!\left[e^{i\beta}\left(1+\frac{zf''(z)}{f'(z)}\right)\right]>0,
 \qquad -\frac\pi2<\beta<\frac\pi2.
\]
Define the sharp second-Hankel functional
\[
 M(\beta)=\sup_{f\in\mathcal C_\beta}|a_2a_4-a_3^2|.
\]
Writing \(c=\cos\beta>0\), the full quantitative endpoint estimate is
\[
 \boxed{\left|\frac{M(\beta)}{c^2}-\frac{11}{96}\right|
 \le \frac{c}{18}+\frac{c^2}{9}.}
\]
Consequently the exact, two-sided grazing-angle asymptotic is
\[
 \boxed{\lim_{\beta\to\pm\pi/2}\frac{M(\beta)}{\cos^2\beta}=\frac{11}{96}.}
\]
In particular, the leading constant is genuinely optimal, not merely
an estimate. The endpoint is approached from within the allowed interval;
no nondegenerate class is asserted at \(\beta=\pm\pi/2\).

## Assumptions and scope

All holomorphic functions and derivatives are in the open unit disk
\(\mathbb D\), and the normalization is \(f(0)=0\), \(f'(0)=1\).
The assertion is one-variable and concerns the ordinary Taylor-coefficient
Hankel determinant. It does not assert an exact formula for \(M(\beta)\)
at a fixed interior angle or a full classification of interior extremizers.
The defining strict inequality is equivalent, by the value at the origin
and the maximum principle, to the corresponding non-strict defining
inequality found in the source literature.

## Proof

**Step 1: exact Carathéodory reduction.** For \(f\in\mathcal C_\beta\),
the normalized positive-real function \(p\) and the complex parameter
\(\tau\) are uniquely specified by
\[
 1+\frac{zf''(z)}{f'(z)}
 =1+\tau(p(z)-1),\qquad
 \tau=e^{-i\beta}\cos\beta,\quad p(0)=1,\quad\operatorname{Re}p>0.
\]
Indeed multiplying by \(e^{i\beta}\) gives
\(e^{i\beta}+\cos\beta(p-1)=\cos\beta p+i\sin\beta\).
Conversely every such \(p\) gives an admissible locally univalent normalized
function through the convergent analytic primitive
\[
 f'(z)=\exp\!\left(\tau\int_0^z\frac{p(w)-1}{w}\,dw\right),
 \qquad f(z)=\int_0^z f'(w)\,dw.
\]
Expand \(p(z)=1+c_1z+c_2z^2+c_3z^3+\cdots\).
Integrating and exponentiating the logarithmic derivative yields exactly
\[
 a_2=\frac{\tau c_1}{2},\quad
 a_3=\frac{\tau c_2+\tau^2c_1^2}{6},\quad
 a_4=\frac{\tau c_3}{12}+\frac{\tau^2c_1c_2}{8}
       +\frac{\tau^3c_1^3}{24}.
\]
Thus
\[
 a_2a_4-a_3^2=\tau^2
 \left(\frac{c_1c_3}{24}-\frac{c_2^2}{36}
 +\frac{\tau c_1^2c_2}{144}-\frac{\tau^2c_1^4}{144}\right).\tag{1}
\]

**Step 2: exact extremum of a Herglotz moment functional.**
By Herglotz representation, \(c_j=2m_j\), where
\(m_j=\int_{|\zeta|=1}\zeta^j\,d\mu(\zeta)\) for a probability measure
\(\mu\) on the unit circle. We establish the sharp identity
\[
 \boxed{\sup_\mu|3m_1m_3-2m_2^2|=\frac{33}{16}.}\tag{2}
\]
Rotational covariance allows \(m_1=x\in[0,1]\) real. The first two
Schur steps give \(y,\xi\in\overline{\mathbb D}\), with \(r=|y|\), such that
\[
 m_2=x^2+(1-x^2)y,
\]
\[
 m_3=x^3+2x(1-x^2)y-x(1-x^2)y^2
            +(1-x^2)(1-r^2)\xi.
\]
For completeness, this follows by writing
\(p=(1+zw)/(1-zw)\), then
\(w(z)=(x+zv(z))/(1+xzv(z))\), with \(v(0)=y\) and
\(v'(0)=(1-r^2)\xi\), and comparing coefficients. All these
parameters are realizable, including their limiting boundary values.

Put \(t=x^2\) and
\[
 a=t^2,\quad b=2t(1-t),\quad d=(1-t)(2+t),\quad
 D=3\sqrt t(1-t).
\]
The functional in (2) becomes
\[
 \Phi=a+by-dy^2+D(1-r^2)\xi.
\]
For fixed \(t,r\), optimizing \(\xi\) gives
\[
 F_t(r)=\max_{\theta\in\mathbb R}
 |a+br e^{i\theta}-dr^2e^{2i\theta}|+D(1-r^2).
\]
The cases \(t=0\) and \(t=1\) give maxima \(2\) and \(1\), respectively.
For \(0<t<1\), put \(u=\cos\theta\). Direct expansion gives
\[
 |a+br e^{i\theta}-dr^2e^{2i\theta}|^2
 =(a+dr^2)^2+b^2r^2+2br(a-dr^2)u-4adr^2u^2.
\]
Its unconstrained maximizing cosine is
\[
 u_* =\frac{a-dr^2}{2t(2+t)r},\qquad r>0.
\]
As \(r\) increases, \(u_*\) strictly decreases. Three consecutive
regimes are therefore possible:

- When \(u_*>1\), the angular maximum is \(a+br-dr^2\), so
  \(F_t(r)\le a+b+D\le 2\). For the last inequality, set \(x=\sqrt t\)
  and use the following completely positive degree-ten Bernstein
  certificate for \(h(x)=2-x^4-2x^2(1-x^2)-3x(1-x^2)\):
  \[
  h(x)=\sum_{k=0}^{10}q_k\binom{10}{k}x^k(1-x)^{10-k},
  \]
  where, in increasing \(k\),
  \[
  (q_0,\ldots,q_{10})=
  \left(2,\frac{17}{10},\frac{61}{45},\frac{119}{120},
   \frac{67}{105},\frac{83}{252},\frac{11}{105},
   \frac1{120},\frac4{45},\frac25,1\right).
  \]
  The coefficients are all positive, and the polynomial identity is
  checked in the accompanying exact-arithmetic program.
- When \(-1\le u_*\le1\), the angular maximum equals
  \((a+dr^2)\sqrt{3/(2+t)}\). Hence \(F_t(r)\) is nondecreasing in
  \(r\), because
  \[
  d\sqrt{\frac3{2+t}}-D
   =(1-t)\bigl(\sqrt{3(2+t)}-3\sqrt t\bigr)\ge0.
  \]
- When \(u_*<-1\), the angular maximum is \(-a+br+dr^2\). Here
  \(F_t(r)=-a+br+dr^2+D(1-r^2)\), which is nondecreasing since
  \(d-D=(1-t)(2+t-3\sqrt t)\ge0\).

As the regimes occur in that order, for every \(t,r\) we obtain
\(F_t(r)\le\max\{2,F_t(1)\}\). At \(r=1\), let
\[
 t_0=\frac{\sqrt{57}-5}{8}.
\]
The same cosine maximization gives the explicit envelope
\[
 F_t(1)=
 \begin{cases}
  2+t-4t^2,&0\le t\le t_0,\\
  (2-t)\sqrt{3/(2+t)},&t_0\le t\le1.
 \end{cases}
\]
The first branch has its unique maximum \(33/16\) at \(t=1/8\)
(which lies below \(t_0\)); the second branch strictly decreases and
matches the first at \(t_0\). This proves the upper bound in (2).
For equality take \(x=1/(2\sqrt2)\) and
\[
 p_*(z)=\frac{1+\omega_*(z)}{1-\omega_*(z)},\qquad
 \omega_*(z)=\frac{z(x-z)}{1-xz}.
\]
This is a Carathéodory function, since \(\omega_*\) is a degree-two
Blaschke product with zero at the origin. Its moments are
\(m_1=x\), \(m_2=2x^2-1=-3/4\), and
\(m_3=4x^3-3x\). Therefore
\(3m_1m_3-2m_2^2=-33/16\), proving sharpness of (2).

**Step 3: quantitative endpoint and sharpness.** Substitution of
\(c_j=2m_j\) into the leading term of (1) gives
\[
 \sup_{p\in\mathcal P}\left|
 \frac{c_1c_3}{24}-\frac{c_2^2}{36}\right|
 =\frac1{18}\frac{33}{16}=\frac{11}{96}.
\]
The standard Carathéodory bounds \(|c_j|\le2\), combined with
\(|\tau|=c\), bound the two omitted terms in (1) by
\(c/18+c^2/9\) after division by \(|\tau|^2\).
The resulting upper inequality holds for all \(p\). Evaluating the
corresponding lower reverse-triangle inequality at the explicit
\(p_*\) proves the lower inequality with the same error.
Taking the supremum and letting \(c\downarrow0\) proves the finding.

## Verification

Run `python3 verify.py` using the accompanying standalone file.
It uses only Python's standard library and exact rational arithmetic,
checks the positive degree-ten Bernstein identity, the extremal moments,
the rational value \(11/96\), and 27 independent coefficient
specializations of identity (1). An additional numerical continuous
optimization over \(x,r,\arg y\) found \(33/16\) to machine precision
near \(x=1/(2\sqrt2)\), \(r=1\), \(\arg y=\pi\).
These computations are cross-checks rather than proofs of the universal
moment maximization; the exhaustive analytical case split above is the
proof.

## Relationship to prior work

Ahamed, Sarkar and Das (arXiv:2608.07563v1, 3 August 2026) derive a
second-Hankel upper bound for a broader Banach-space class and explicitly
leave the exact nonzero-angle variational problem open. Its bound has
leading grazing-angle coefficient \(17/144\); the present planar theorem
determines the smaller sharp coefficient \(11/96\), including a uniform
error estimate. Krishna and Reddy (2015) study second-Hankel upper
bounds for related analytic subclasses. Ali and Nurezzaman (2024) give
sharp Hankel bounds for several classes including spirallike functions;
the publisher preview does not identify an equivalent grazing-angle
statement, and their full text was not accessible for direct comparison.

The result concerns a limiting, large-angle regime that is not
settled by fixed-angle coefficient upper bounds. Possible older
equivalences remain a bibliographic uncertainty, not a claim of
independent certification.

## Limitations

The result is for the one-variable coefficient determinant of normalized
spirallike-convex maps, not for arbitrary Banach-space directional
coefficients. It proves a sharp asymptotic at two limiting angles with
an explicit error, but no interior-angle exact closed form. The
limiting Carathéodory extremizer need not maximize the full determinant
for any prescribed non-endpoint angle. The general coefficient-to-
Herglotz representation is classical; only the particular sharp moment
optimization and its endpoint application are claimed here.

## References

1. M. B. Ahamed, N. Sarkar, P. Das, *Second Hankel Determinant for \(\beta\)-Spirallike Convex Mappings in Complex Banach Spaces*, arXiv:2608.07563v1 (3 August 2026), https://arxiv.org/html/2608.07563v1.
2. D. Vamshee Krishna, T. Ram Reddy, *Coefficient inequality for certain subclasses of analytic functions associated with Hankel determinant*, Indian J. Pure Appl. Math. 46 (2015), 91–106, doi:10.1007/s13226-015-0111-1.
3. M. F. Ali, M. Nurezzaman, *The Second Hankel Determinant for Some Classes of Univalent Functions*, Mediterr. J. Math. 21 (2024), article 220, doi:10.1007/s00009-024-02762-6.
4. The classical Herglotz representation and Schur algorithm for positive-real analytic functions (standard tools, with all needed finite-order identities derived above).
