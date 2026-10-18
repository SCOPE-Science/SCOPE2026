# Exact fixed-translation rational tongues and universal vertex slopes for contracted rotations

## Finding
Consider the contracted circle maps
\[
R_{\lambda,b}(x)=\{\lambda x+b\},\qquad 0<\lambda<1,\quad0<b<1,
\]
where braces mean fractional part. Fix coprime integers \(1\le p<q\), and let \(r=p/q\). Define the integer polynomials
\[
Q_q(t)=\sum_{j=0}^{q-1}t^j,\qquad
S_{p,q}(t)=\sum_{j=0}^{q-1}
 \left(\left\lceil\frac{(j+1)p}{q}\right\rceil-
             \left\lceil\frac{jp}{q}\right\rceil\right)t^j.
\]
The following statements hold.

**Exact vertical section.** If \(0<b\le r\), no \(\lambda\in(0,1)\) gives rotation number \(r\). If \(r<b<1\), the set of slopes with rotation number exactly \(r\) is the single nondegenerate closed interval
\[
\{\lambda\in(0,1):\rho(R_{\lambda,b})=r\}
 =[\lambda_-(b),\lambda_+(b)],
\]
whose endpoints are uniquely determined *inside* \((0,1)\) by
\[
bQ_q(\lambda_-)=S_{p,q}(\lambda_-),\qquad
bQ_q(\lambda_+)=S_{p,q}(\lambda_+)
          +\lambda_+^{q-1}-\lambda_+^q.
\]
Both endpoints depend real-analytically and strictly decreasingly on \(b\in(r,1)\).

**Sharp vertex law.** As \(b\downarrow r\),
\[
1-\lambda_-(b)=\frac{2q}{q-1}(b-r)+O((b-r)^2),\qquad
1-\lambda_+(b)=\frac{2q}{q+1}(b-r)+O((b-r)^2),
\]
and consequently
\[
\lambda_+(b)-\lambda_-(b)
=\frac{4q}{q^2-1}(b-r)+O((b-r)^2).
\]
Remarkably, the first-order width coefficient depends only on the denominator \(q\), not the numerator \(p\).

## Assumptions and scope
The map is defined on \([0,1)\) with its ordinary fractional-part convention. Its rotation number is that of the monotone degree-one lift \(x\mapsto\lfloor x\rfloor+\lambda\{x\}+b\). Only reduced positive rationals strictly below one and slopes strictly between zero and one are covered. Endpoint statements refer to admissible slopes in this open domain; the limiting vertices \(\lambda=1\) and \(b=1\) are not included.

## Proof
**1. Previously known horizontal tongues.** For fixed \(0<t<1\), Laurent and Nogueira's rational rotation-number formula, also recorded as Proposition 7 of Gaivão and Nogueira, states that rotation number \(r=p/q\) occurs exactly when
\[
L(t)\le b\le U(t),\quad
L(t)=\frac{S_{p,q}(t)}{Q_q(t)},\quad
U(t)=\frac{S_{p,q}(t)+t^{q-1}-t^q}{Q_q(t)}.
\]
Indeed, the usual polynomial is \(1+\sum_{j=1}^{q-2}d_jt^j\), with \(d_j=\lfloor(j+1)r\rfloor-\lfloor jr\rfloor\). For \(1\le j\le q-2\), coprimality gives \(d_j=\lceil(j+1)r\rceil-\lceil jr\rceil\), and the two boundary coefficients are \(1\) and \(0\); hence it equals \(S_{p,q}\). This fixed-slope horizontal formula is not claimed as new. It immediately gives
\[
U(t)-L(t)=\frac{t^{q-1}(1-t)}{Q_q(t)}>0.
\]

**2. A cyclic-word ordering lemma.** Let \(w_j=\lceil(j+1)r\rceil-\lceil jr\rceil\), periodically extended with period \(q\). Its first \(k\) symbols contain \(\lceil kr\rceil\) ones. A shift by any integer \(s\) contains \(\lceil(s+k)r\rceil-\lceil sr\rceil\) ones in its first \(k\) symbols. For \(1\le k\le q-1\), the excess
\[
D_k=\lceil kr\rceil-\lceil(s+k)r\rceil+\lceil sr\rceil
\]
belongs to \(\{0,1\}\), and \(D_q=0\). Summation by parts shows
\[
0\le\sum_{h=0}^{q-1}t^h(w_h-w_{h+s})
 =(1-t)\sum_{k=1}^{q-1}t^{k-1}D_k
 \le 1-t^{q-1}<1-t^q.
\]
For a nontrivial cyclic shift, the first inequality is strict: otherwise all \(D_k\) vanish, the period-\(q\) word equals that shift, and its number \(p\) of ones would be divisible by a nontrivial divisor of \(q\), contradicting \(\gcd(p,q)=1\).

The lower mechanical word \(d_j=\lfloor(j+1)r\rfloor-\lfloor jr\rfloor\) has the dual property: each shifted prefix has at least as many ones as the unshifted prefix and at most one more. Therefore, for any nontrivial shift, its weighted difference lies strictly between \(-(1-t^q)\) and \(0\).

**3. Strict motion of both horizontal boundaries.** For any periodic binary digit word \((e_0,\ldots,e_{q-1})\), put
\[
W_j(t)=\sum_{h=0}^{q-1}t^h e_{j-1-h\ \mathrm{mod}\ q},\qquad
x_j(t,b)=\frac{bQ_q(t)-W_j(t)}{1-t^q}.
\]
These numbers satisfy the formal periodic recurrence \(x_{j+1}=t x_j+b-e_j\) and \(x_q=x_0\).

At \(b=L(t)\), choose \(e_j=d_j\). Reversing this lower word gives the upper word \(w\); thus \(W_0=S_{p,q}\) and \(x_0=0\). By Step 2, for \(1\le j<q\) the remaining coordinates satisfy \(0<x_j<1\). At \(b=U(t)\), instead take \(e'_0=1\), \(e'_{q-1}=0\), and \(e'_j=d_j\) for \(1\le j\le q-2\). Reversing \(e'\) gives precisely the lower mechanical word. Consequently
\[
W'_0=S_{p,q}-1+t^{q-1},\qquad
bQ_q-W'_0=1-t^q,
\]
so \(x'_0=1\), while \(0<x'_j<1\) for \(1\le j<q\) by the dual bound in Step 2. These are respectively the zero-hitting and one-sided one-hitting boundary cycles. In both constructions the complete period-\(q\) polynomial recurrence is valid even at a boundary point.

Differentiate the recurrence along either boundary curve \(b=B(t)\), holding \(x_0=0\) or \(x'_0=1\) fixed. Since \(x_q=x_0\), differentiation and iteration give
\[
B'(t)=-\frac{\sum_{j=0}^{q-1}t^{q-1-j}x_j(t,B(t))}{Q_q(t)}<0.
\]
For the lower boundary at least \(x_1>0\); for the upper boundary already \(x'_0=1>0\). Hence **both** \(L\) and \(U\) are strictly decreasing on the entire interval \((0,1)\), not merely near a vertex.

**4. Inversion and exact domain.** The polynomials give
\[
L(0)=U(0)=1,\qquad L(1)=U(1)=\frac pq.
\]
Strict monotonicity proves that both are bijections from \((0,1)\) to \((p/q,1)\). For fixed \(b\in(p/q,1)\), the inequalities \(L(t)\le b\le U(t)\) are equivalent to \(t\ge L^{-1}(b)\) and \(t\le U^{-1}(b)\), respectively. Since \(L<U\), their inverse order is \(L^{-1}(b)<U^{-1}(b)\). This proves the claimed exact interval, with unique polynomial root endpoints. Both inverse functions are analytic by the nonvanishing derivatives in Step 3.

**5. The denominator-only asymptotic.** The upper word contains exactly \(p\) ones. Summation by parts and the coprime floor-sum identity yield
\[
S_{p,q}(1)=p,\quad
S'_{p,q}(1)=\sum_{j=0}^{q-1}j w_j
 =(q-1)p-\sum_{j=1}^{q-1}\lceil jr\rceil
 =\frac{(p-1)(q-1)}2.
\]
Since \(Q_q(1)=q\) and \(Q_q'(1)=q(q-1)/2\), differentiation gives
\[
L'(1)=-\frac{q-1}{2q},\qquad
U'(1)=-\frac{q+1}{2q}.
\]
Analytic inversion at \(t=1\) gives the two vertex expansions, whose difference is the stated universal width law.

## Verification
The included `check_exact.py` uses only Python's standard library and exact `Fraction` arithmetic. Executing `python check_exact.py` checks 5,972 triples with all reduced fractions of denominator at most 70 and four rational slopes, including both complete boundary cycles, their digit words, polynomial identities, strict derivative signs and the known horizontal order; it separately checks six near-vertex slopes. It passed during construction of this result. The finite tests supplement but do not replace the arbitrary-denominator proof above.

## Relationship to prior work
Laurent and Nogueira (2017 preprint, 2018 journal) give the exact horizontal mode-locking interval for each fixed contraction ratio. Gaivão and Nogueira (2020 preprint, Proposition 7 and the paragraph immediately following it) reproduce those bounds and explicitly note that precise endpoints of the **fixed-translation, variable-slope** interval were not available. Their zero-dimensional exceptional-set result does not supply these endpoints. The present finding adds an all-denominator proof of strict boundary monotonicity, unique algebraic vertical-section endpoints and the denominator-only vertex-width coefficient.

Gaivão, Laurent and Nogueira's later study of two-interval piecewise-affine maps provides more general rotation-number parameterizations, principally treating a translation-like coordinate as the variable for fixed slope data; it does not state the unique vertical inverses and universal wedge law in the form proved here. Gaivão's 2022 preprint on exceptional-set dimension analyzes perturbations of fixed-slope piecewise-affine maps, not these vertical rational tongues.

## Limitations
The boundary polynomial formulas are known and are explicitly credited; the asserted new information is monotonic inversion in the contraction ratio and the sharp vertex geometry. The theorem does not determine the rotation number at arbitrary irrational parameters or give a uniform error term as the denominator tends to infinity. Direct comparison with all older engineering mode-locking literature remains a residual originality risk; no independent audit has been performed.

## References
1. M. Laurent and A. Nogueira, *Rotation number of contracted rotations*, arXiv:1704.05130 (first posted April 2017), later *Journal of Modern Dynamics* **12** (2018), 175–191, Theorem 3, https://arxiv.org/abs/1704.05130 .
2. J. P. Gaivão and A. Nogueira, *Dynamics of piecewise increasing contractions*, arXiv:2007.08014 (first posted 2020-07-15), later *Bulletin of the London Mathematical Society* **54** (2022), 482–500, Proposition 7 and accompanying open question, https://arxiv.org/abs/2007.08014 .
3. J. P. Gaivão, M. Laurent and A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, *Aequationes Mathematicae*, DOI:10.1007/s00010-024-01064-2, Sections 1 and 5, https://doi.org/10.1007/s00010-024-01064-2 .
4. J. P. Gaivão, *Hausdorff Dimension of the Exceptional Set of Interval Piecewise Affine Contractions*, arXiv:2211.14140 (2022), later *Qualitative Theory of Dynamical Systems* **24** (2025), article 86, https://arxiv.org/abs/2211.14140 .
