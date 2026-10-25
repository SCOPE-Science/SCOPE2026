# A unique sharp Ehrhart coefficient threshold for one-step lecture-hall simplices

## Finding

For every integer \(n\ge5\) and every integer \(a\ge1\), let
\[
P_{n,a}=\left\{x\in\mathbb R^n:0\le \frac{x_1}{a}\le\cdots\le\frac{x_{n-1}}{a}\le\frac{x_n}{a+1}\le1\right\},
\]
and let \(L_{n,a}(t)=\#(tP_{n,a}\cap\mathbb Z^n)\), its Ehrhart polynomial. Write \(E_j=e_j(1,2,\ldots,n-1)\), where \(e_j\) is the elementary symmetric polynomial of degree \(j\). Define
\[
Q_n(z)=\frac{E_4}{n-4}+\left(\frac{E_4}{n}+\frac{E_3}{2}\right)z+\frac{n-3}{12}E_2z^2-\frac{(n-1)(n-2)(n-3)}{720}z^4.
\]
Then the exact coefficient formula is
\[
[t^{n-4}]L_{n,a}(t)=\frac{a^{n-5}}{(n-1)!}Q_n(a).
\]
The quartic \(Q_n\) has **exactly one positive real root** \(\rho_n\), and this root is simple. Thus the displayed Ehrhart coefficient is strictly positive for integers \(1\le a<\rho_n\), zero if \(a=\rho_n\) is an integer, and strictly negative for integers \(a>\rho_n\). In particular its first strictly negative integer parameter is exactly
\[
\beta(n)=\lfloor\rho_n\rfloor+1.
\]
Moreover the sharp threshold has the dimension-asymptotic law
\[
\boxed{\displaystyle\lim_{n\to\infty}\frac{\beta(n)}{n^{4/3}}=\left(\frac{15}{8}\right)^{1/3}}.
\]
The exact first-negative parameters for dimensions \(5,6,7,8,9\) are \(16,19,23,27,31\), respectively. This theorem concerns **one specific Ehrhart coefficient**; it does not assert that all earlier parameters are Ehrhart-positive or resolve monotonicity of Ehrhart non-positivity for the entire polynomial.

## Assumptions and scope

All quantities are defined over the ordinary integer lattice, with \(n\ge5\) an integer and \(a\ge1\) an integer. The real variable \(z\) in \(Q_n(z)\) is introduced only for locating a sign-change threshold; no nonintegral lecture-hall parameter is needed. For \(1\le j\le4\), \(e_j(1,\ldots,n-1)\) is the coefficient-symmetric sum over distinct \(j\)-subsets of \(\{1,\ldots,n-1\}\). The coefficient \([t^{n-4}]\) is in the ordinary monomial basis, not the \(h^*\)-basis. At a positive integer root the coefficient vanishes and the first strictly negative parameter is the next integer.

## Proof

**1. Exact lattice count.** Fix an integer dilation \(t\ge0\), and condition on the last coordinate \(x_n=y\). The remaining coordinates form a weakly increasing \((n-1)\)-tuple of integers between \(0\) and \(\lfloor ay/(a+1)\rfloor\). The stars-and-bars count is therefore
\[
L_{n,a}(t)=\sum_{y=0}^{(a+1)t}\binom{\lfloor ay/(a+1)\rfloor+n-1}{n-1}.
\]
Equivalently, condition on \(x_{n-1}=u\), with \(0\le u\le at\). There are \(\binom{u+n-2}{n-2}\) choices for the earlier coordinates and \((a+1)t-u-\lceil u/a\rceil+1\) choices for the last. Since \(\lceil u/a\rceil\) equals the number of integers \(q\in\{0,\ldots,t-1\}\) with \(aq<u\), summing the hockey-stick identities and cancelling gives the polynomial identity
\[
L_{n,a}(t)=\binom{at+n}{n}+\sum_{q=0}^{t-1}\binom{aq+n-1}{n-1}.\tag{1}
\]
Both sides agree for every nonnegative integer \(t\); the right side is a polynomial in \(t\) by Faulhaber's formula, so (1) is an identity of polynomials. This also follows from the one-step extension decomposition in the cited 2025 source.

**2. Extract the critical coefficient.** Put \(r=n-4\ge1\). The coefficient of \(t^r\) in the first term of (1) is
\[
\frac{a^{n-4}}{n!}\,e_4(1,2,\ldots,n).
\]
Expanding the second term in powers of \(q\) gives
\[
\binom{aq+n-1}{n-1}=\frac1{(n-1)!}\sum_{k=0}^{n-1}a^kE_{n-1-k}q^k.
\]
For Bernoulli numbers with \(B_0=1\), \(B_1=-1/2\), \(B_2=1/6\), \(B_3=0\), \(B_4=-1/30\), the standard power-sum identity reads
\[
[t^r]\sum_{q=0}^{t-1}q^k=\frac1{k+1}\binom{k+1}{r}B_{k+1-r},
\]
where the right side is zero when \(k+1<r\). Only \(k=n-5,n-4,n-3,n-2,n-1\) contribute. Their respective nonzero coefficients are \(1/(n-4)\), \(-1/2\), \((n-3)/12\), and \(-(n-1)(n-2)(n-3)/720\); the potential cubic-in-\(a\) term is zero because \(B_3=0\). Finally,
\[
e_4(1,\ldots,n)=E_4+nE_3,
\]
so the \(a^{n-4}\) term simplifies to \(E_4/n+E_3/2\) after factoring \(a^{n-5}/(n-1)!\). This proves the asserted exact quartic identity, including all factorial normalizations.

**3. One sharp crossing.** Since \(n\ge5\), each of \(E_2,E_3,E_4\) is strictly positive. Thus the coefficient sequence of \(Q_n\) in descending powers of \(z\), after omitting the missing cubic term, has signs \((- ,+,+,+)\). Descartes' rule of signs gives **at most** one positive root counted with multiplicity. Also \(Q_n(0)>0\) and \(Q_n(z)\to-\infty\) as \(z\to+\infty\), so the intermediate value theorem provides a positive root. The root is therefore unique and simple, with positive and negative signs on its respective sides. To see that \(\rho_n>1\), note
\[
E_4\ge(n-1)(n-2)(n-3)(n-4),
\]
so the positive constant term of \(Q_n\) alone exceeds the absolute value of its negative quartic term at \(z=1\). Hence the claimed threshold is meaningful within the integer domain \(a\ge1\).

**4. Growth with dimension.** For each fixed \(j\in\{2,3,4\}\), the elementary-symmetric asymptotic is
\[
e_j(1,\ldots,n-1)=\frac{n^{2j}}{2^j j!}+O(n^{2j-1}).
\]
Consequently, for every fixed \(c>0\), substituting \(z=cn^{4/3}\) in \(Q_n\) and dividing by \(n^{25/3}\) yields
\[
\frac{Q_n(cn^{4/3})}{n^{25/3}}\longrightarrow\frac{c}{384}-\frac{c^4}{720}.
\]
The right side is positive for \(0<c<(15/8)^{1/3}\) and negative for \(c>(15/8)^{1/3}\). Uniqueness of the positive root squeezes \(\rho_n/n^{4/3}\) to \((15/8)^{1/3}\). Replacing \(\rho_n\) with \(\lfloor\rho_n\rfloor+1\) changes this ratio by at most \(n^{-4/3}\), proving the stated limit.

## Verification

The standalone script `verify.py` uses only the Python standard library. It constructs the elementary symmetric coefficients over exact integers and checks the quartic signs. Independently, it counts integer points by slicing at the final coordinate, checks (1) by binomial sums, obtains the entire Ehrhart polynomial from Newton forward differences, and compares the monomial coefficient with the quartic identity using rational arithmetic. It tests six integer parameters in each dimension \(5\) through \(9\), their first-negative parameter boundaries, and the sign structure through dimension \(250\). Running `python3 verify.py` prints:

`VERIFY_OK exact_counts=240 dim5to9_a6 beta5to9=16,19,23,27,31 sign_pattern_n5to250`

The finite verification is not a proof of the all-dimensional theorem or the asymptotic limit; those follow from the exact identities in the preceding section.

## Relationship to prior work

Caicedo, Juhnke, and Poullot introduced the one-step family \((a,\ldots,a,a+1)\) as a source of Ehrhart non-positivity and proved that \([t^{n-4}]L_{n,a}(t)<0\) for all sufficiently large \(a\) at each fixed \(n\ge5\) (Theorem 3.5, arXiv:2508.18890). They tabulated the first-negative integer values in dimensions \(5\) through \(8\) and conjectured monotonicity of **overall** Ehrhart non-positivity. The new content here is the exact four-term quartic formula for the targeted coefficient, its unique global positive sign change for every dimension, and the dimension-asymptotic \(n^{4/3}\) threshold with leading constant. The cited paper's asymptotic fixes dimension and sends \(a\) to infinity; it does not imply the new joint-dimensional threshold law. Brändén and Solus (arXiv:1911.12459) establish triangulation and algebraic properties of lecture-hall polytopes; their results do not evaluate the sign-crossing threshold of this Ehrhart coefficient.

## Limitations

The theorem does **not** show that the full Ehrhart polynomial is coefficientwise positive for every \(a\le\lfloor\rho_n\rfloor\): other coefficients may change sign earlier. Thus it does not resolve Conjecture 3.4 of the 2025 source. The explicit quartic-root characterization is exact but does not give a simple elementary formula for every integer \(\beta(n)\). Historical originality is assessed against the inspected primary texts and database records, not by a proof of global priority; independently checking additional recent or differently indexed literature remains appropriate. No independent external scientific audit has been performed.

## References

1. J. B. Caicedo, M. Juhnke, and G. Poullot, *Ehrhart non-positivity and unimodular triangulations for classes of s-lecture hall simplices*, arXiv:2508.18890 (first submitted 2025-08-26). https://arxiv.org/abs/2508.18890
2. P. Brändén and L. Solus, *Some Algebraic Properties of Lecture Hall Polytopes*, arXiv:1911.12459 (2019). https://arxiv.org/abs/1911.12459
3. M. Beck and S. Robins, *Computing the Continuous Discretely*, 2nd ed., Springer (2015), for standard Ehrhart generating functions and coefficient extraction.
