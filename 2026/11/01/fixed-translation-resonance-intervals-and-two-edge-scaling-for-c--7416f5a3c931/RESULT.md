# Fixed-translation resonance intervals and two-edge scaling for contracted rotations

## Finding
Let \(R_{\lambda,b}(x)=\{\lambda x+b\}\) on \([0,1)\), with \(0<\lambda,b<1\). Let \(p,q\) be coprime integers satisfying \(1\le p<q\). Put
\[
Q_q(t)=\sum_{j=0}^{q-1}t^j,\qquad
S_{p,q}(t)=1+\sum_{j=1}^{q-2}\left(\left\lfloor\frac{(j+1)p}{q}\right\rfloor-\left\lfloor\frac{jp}{q}\right\rfloor\right)t^j,
\]
where the sum is empty when \(q=2\), and define
\[
L_{p,q}(t)=\frac{S_{p,q}(t)}{Q_q(t)},\qquad
U_{p,q}(t)=\frac{S_{p,q}(t)+t^{q-1}-t^q}{Q_q(t)}.
\]
Both boundary functions are strictly decreasing on \((0,1)\), with limits \(1\) at \(t\downarrow0\) and \(p/q\) at \(t\uparrow1\). Thus, for each fixed \(b\in(0,1)\):

* If \(b\le p/q\), the rotation number of \(R_{\lambda,b}\) never equals \(p/q\) for \(0<\lambda<1\).
* If \(p/q<b<1\), it equals \(p/q\) precisely for the **single closed interval** \(\alpha_{p,q}(b)\le\lambda\le\beta_{p,q}(b)\), where \(0<\alpha_{p,q}(b)<\beta_{p,q}(b)<1\) are the unique roots in \((0,1)\) of
\[
S_{p,q}(\alpha)-bQ_q(\alpha)=0,\qquad
S_{p,q}(\beta)+\beta^{q-1}-\beta^q-bQ_q(\beta)=0.
\]
In particular, rational \(b\) yields exact algebraic endpoints determined by explicit integer-coefficient polynomials after clearing denominators.

These resonance intervals have the following **sharp asymptotic geometry**. As \(b\downarrow p/q\), writing \(\delta=b-p/q\),
\[
\alpha_{p,q}(b)=1-\frac{2q}{q-1}\delta+O(\delta^2),\qquad
\beta_{p,q}(b)=1-\frac{2q}{q+1}\delta+O(\delta^2),
\]
so that
\[
\beta_{p,q}(b)-\alpha_{p,q}(b)=\frac{4q}{q^2-1}\delta+O(\delta^2).
\]
The leading opening coefficient depends **only on the denominator** \(q\), not on the numerator \(p\).

At the opposite edge \(b\uparrow1\), let \(\varepsilon=1-b\), and define
\[
m=\left\lceil\frac{q}{q-p}\right\rceil-1.
\]
If \(p\le q-2\), then \(1\le m\le q-2\), and
\[
\alpha_{p,q}(b)\sim\varepsilon^{1/m},\qquad
\beta_{p,q}(b)\sim\varepsilon^{1/m},\qquad
\beta_{p,q}(b)-\alpha_{p,q}(b)\sim\frac1m\varepsilon^{(q-m)/m}.
\]
If \(p=q-1\), the scaling changes discontinuously:
\[
\alpha_{q-1,q}(b)\sim\varepsilon^{1/(q-1)},\qquad
\beta_{q-1,q}(b)\sim\varepsilon^{1/q},\qquad
\beta_{q-1,q}(b)-\alpha_{q-1,q}(b)\sim\varepsilon^{1/q}.
\]
All asymptotics fix the reduced rational \(p/q\); their constants are not asserted uniform as \(q\to\infty\).

## Assumptions and scope
The map acts on the half-open unit interval, with fractional-part convention and nondecreasing degree-one lift \(F_{\lambda,b}(x)=\lfloor x\rfloor+\lambda\{x\}+b\). The rotation number is \(\rho(\lambda,b)=\lim_{n\to\infty}(F_{\lambda,b}^n(x)-x)/n\), independent of \(x\). The claim concerns the rotation number, including tongue boundary points; it does not require the boundary attractor to be an interior periodic orbit. Only coprime \(1\le p<q\), \(q\ge2\), and real \(0<b<1\) are covered.

## Proof
**1. Exact known plateau criterion.** Laurent–Nogueira's rational-rotation criterion (Theorem 3(ii), arXiv:1704.05130v3; also Proposition 7 of Gaivão–Nogueira, arXiv:2007.08014v2) states that for every \(0<t<1\),
\[
\rho(t,b)=p/q\quad\Longleftrightarrow\quad L_{p,q}(t)\le b\le U_{p,q}(t).
\]
This is an established premise, not claimed as new. The positive width \(U-L=t^{q-1}(1-t)/Q_q(t)>0\) follows directly.

**2. Monotonicity and inversion.** For \(0<t_1<t_2<1\), the degree-one lifts satisfy \(F_{t_1,b}(x)\le F_{t_2,b}(x)\) for every real \(x\). Every such lift is nondecreasing in \(x\); induction compares all iterates and hence the rotation numbers: \(\rho(t_1,b)\le\rho(t_2,b)\). The known plateau criterion and monotonicity in \(b\) imply both \(L_{p,q}\) and \(U_{p,q}\) are nonincreasing in \(t\). Indeed, \(b<L_{p,q}(t)\) is equivalent to \(\rho(t,b)<p/q\), and \(b>U_{p,q}(t)\) is equivalent to \(\rho(t,b)>p/q\). Taking these strict sublevel and superlevel sets at two values of \(t\) gives the claimed order of both edges. They are rational functions analytic on a neighborhood of \([0,1]\), with different endpoint values \(L(0)=U(0)=1\) and \(L(1)=U(1)=p/q\). A nonconstant analytic nonincreasing function is strictly decreasing, since equality at two distinct arguments would force constancy on an interval and then everywhere. Each equation \(L(t)=b\), \(U(t)=b\) therefore has exactly one solution in \((0,1)\) if and only if \(p/q<b<1\). Since \(L<U\) inside, its roots satisfy \(\alpha<\beta\); the rational-rotation criterion gives precisely the intervening interval. This interval automatically lies in the nontrivial two-branch range \(t>1-b\), since rotation number zero holds for \(b\le1-t\).

**3. Universal endpoint derivatives.** Extend coefficients by \(c_0=1\), \(c_{q-1}=0\), and for \(1\le j\le q-2\), \(c_j=\lfloor (j+1)p/q\rfloor-\lfloor jp/q\rfloor\). The nonzero indices other than zero are \(\lfloor kq/p\rfloor\), for \(1\le k\le p-1\). Coprimality gives the classical elementary floor-sum identity \(\sum_{k=1}^{p-1}\lfloor kq/p\rfloor=(p-1)(q-1)/2\) (pair the summands for \(k\) and \(p-k\)). Hence \(S(1)=p\), \(S'(1)=(p-1)(q-1)/2\), \(Q(1)=q\), and \(Q'(1)=q(q-1)/2\). Quotient differentiation yields \(L'(1)=-(q-1)/(2q)\). Since \(U-L=t^{q-1}(1-t)/Q(t)\), its derivative at one is \(-1/q\), hence \(U'(1)=-(q+1)/(2q)\). Both derivatives are nonzero. Taylor's theorem and local inversion at \(t=1\) give the first two endpoint expansions and their difference.

**4. Strong-contraction edge.** Write \(r=q-p\). For \(1\le j\le q-2\), the coefficients obey
\[
c_j=1-\left(\left\lceil\frac{(j+1)r}{q}\right\rceil-\left\lceil\frac{jr}{q}\right\rceil\right).
\]
If \(r>1\), then \(q/r\) is nonintegral by coprimality, and the first zero among \(c_1,\ldots,c_{q-2}\) occurs exactly at \(m=\lfloor q/r\rfloor=\lceil q/r\rceil-1\). Therefore both deficits \(1-L(t)\) and \(1-U(t)\) equal \(t^m(1+O(t))\) as \(t\downarrow0\), while \(U(t)-L(t)=t^{q-1}(1+O(t))\). Inverting their deficits gives \(\alpha,\beta\sim\varepsilon^{1/m}\). By the mean value theorem applied to \(U\) between \(\alpha\) and \(\beta\),
\[
\beta-\alpha=\frac{U(\alpha)-L(\alpha)}{-U'(\xi)}
\quad\text{for some }\xi\in(\alpha,\beta).
\]
Here \(-U'(\xi)\sim m\xi^{m-1}\) and \(\xi\sim\varepsilon^{1/m}\). This gives the asserted \(m^{-1}\varepsilon^{(q-m)/m}\) width.

If \(r=1\), the first missing coefficient of \(S\) occurs instead at \(q-1\); in fact \(S(t)=Q_q(t)-t^{q-1}\). Thus exactly \(1-L(t)=t^{q-1}/Q_q(t)\) and \(1-U(t)=t^q/Q_q(t)\). Their inverse leading powers are \(\varepsilon^{1/(q-1)}\) and \(\varepsilon^{1/q}\); the latter dominates their separation. The case \(q=2\) is included. This finishes the proof.

## Verification
A standalone Python checker (`check.py`) verifies exact coefficient sums, first missing indices and derivative identities for 1,493 coprime pairs with \(2\le q\le70\), and uses 90-digit Decimal arithmetic to check sample tongue endpoints at both edges for nine distinct reduced rationals. These finite tests are supplementary; Steps 1–4 establish the conclusions for every admissible rational parameter. Run: `python check.py` with Python 3 standard library only.

## Relationship to prior work
The rational-plateau polynomial criterion is **not** new: it comes from the contracted-rotation theory of Ding–Hemmer and Bugeaud and is stated explicitly in Laurent–Nogueira (2017/2018), Theorem 3, and Gaivão–Nogueira (2020/2022), Proposition 7. The latter paper observes that, for fixed translation, a precise description of the contraction-rate interval endpoints was unavailable (Introduction after Proposition 7). The present contribution inverts those tongues with unique explicit polynomial roots for every reduced rational rotation number and establishes both endpoint scaling regimes and the numerator-independent first-order opening coefficient. A 2025 three-interval generalization by Guiraud–Hernández–Meyroneinc–Nogueira treats varying translation and break parameters at fixed contraction, not these fixed-translation edge laws.

## Limitations
This is a precise refinement of an existing exact rational tongue formula, not a new classification of rotation numbers or irrational attractors. No quantitative uniformity in the denominator, irrational rotation parameter, basin measure, or boundary periodic-orbit selection is established. Full independent publication-priority assessment is not performed; older specialized Farey-tree literature may contain equivalent geometric observations not found in the inspected texts.

## References
1. M. Laurent and A. Nogueira, *Rotation number of interval contracted rotations*, arXiv:1704.05130v3 (first posted 2017-04-17), Theorem 3 and Section 3. https://arxiv.org/html/1704.05130v3
2. J. P. Gaivão and A. Nogueira, *Dynamics of piecewise increasing contractions*, arXiv:2007.08014v2 (first posted 2020-07-15), Proposition 7 and the following fixed-translation observation. https://arxiv.org/html/2007.08014v2
3. P. Guiraud, M. Hernández, A. Meyroneinc and A. Nogueira, *Rotation number and dynamics of 3-interval piecewise affine contractions*, arXiv:2501.16263v1 (2025), Introduction and parameter-dependent rotation criteria. https://arxiv.org/abs/2501.16263
