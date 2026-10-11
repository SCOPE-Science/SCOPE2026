# Sharp quadratic convexity and the exact initial Day modulus of a hybrid \(\ell_1\)–Hilbert norm

## Finding
For every integer \(n\ge 2\) and real \(t>0\), equip the real vector space \(\mathbb R^n\) with
\[
N_t(z)=\bigl(\|z\|_1^2+t\|z\|_2^2\bigr)^{1/2}.
\]
Put \(p=\lfloor n/2\rfloor\), \(q=\lceil n/2\rceil\), and
\[
s=\sqrt{\left(1+\frac{t}{p}\right)\left(1+\frac{t}{q}\right)},\qquad
c=\frac{s-1}{s+1},\qquad
\varepsilon_*=\frac{2}{\sqrt{1+c}}.
\]
The **largest** constant \(C\) such that
\[
\frac{N_t(x)^2+N_t(y)^2}{2}
-N_t\!\left(\frac{x+y}{2}\right)^2
\ge C\,N_t\!\left(\frac{x-y}{2}\right)^2
\quad\text{for all }x,y\in\mathbb R^n
\tag{1}
\]
is exactly \(C=c\).

Moreover, for the classical Day modulus of convexity of \((\mathbb R^n,N_t)\),
\[
\delta(\varepsilon)=\inf\left\{
1-N_t\!\left(\frac{x+y}{2}\right):
N_t(x),N_t(y)\le1,\ N_t(x-y)\ge\varepsilon\right\},
\]
there is an **exact maximal initial interval of equality**:
\[
\delta(\varepsilon)=1-\sqrt{1-\frac{c\varepsilon^2}{4}}
\quad (0\le\varepsilon\le\varepsilon_*),
\tag{2}
\]
whereas
\[
\delta(\varepsilon)>1-\sqrt{1-\frac{c\varepsilon^2}{4}}
\quad (\varepsilon_*<\varepsilon\le2).
\tag{3}
\]
For even \(n\), the coefficient simplifies to \(c=t/(n+t)\). For odd \(n\), the same coefficient involves the balancing product \(pq=(n^2-1)/4\), yielding an explicit parity-dependent formula. At \(n=3,t=1\), \(c=2-\sqrt3\).

## Assumptions and scope
All spaces and vectors are real. The two norms \(\|\cdot\|_1\) and \(\|\cdot\|_2\) are the standard finite-dimensional sequence norms; \(t>0\) is arbitrary. The function \(N_t\) is a norm because it is the Euclidean combination of two norms. The modulus is stated using closed-unit-ball points, an equivalent conventional definition for this norm. In (1), \(C\) is one fixed constant required to hold for all pairs, with no restriction on signs or coordinates. The upper endpoint \(\varepsilon=2\) is included in the strict inequality (3).

## Proof
**1. A universal quadratic-defect reduction.** Write \(m=(x+y)/2\) and \(d=(x-y)/2\). For each coordinate choose \(\sigma_i\in\{-1,1\}\) with \(\sigma_i m_i=|m_i|\) (either choice at a zero coordinate). In particular \(\sum_i\sigma_i m_i=\|m\|_1\). For either sign,
\[
\|m\pm d\|_1^2\ge\left(\sum_i\sigma_i(m_i\pm d_i)\right)^2.
\]
Averaging these two inequalities and adding the Euclidean quadratic identity yields
\[
\frac{N_t(m+d)^2+N_t(m-d)^2}{2}-N_t(m)^2
\ge\left(\sum_i\sigma_i d_i\right)^2+t\|d\|_2^2.
\tag{4}
\]
The denominator desired in (1) is \(N_t(d)^2=\|d\|_1^2+t\|d\|_2^2\).

**2. Sharp minimization of the ratio.** Replace \(d_i\) by \(\sigma_i d_i\); both its \(\ell_1\) and Euclidean norms stay unchanged. If all nonzero coordinates have the same sign, the quotient of the right side of (4) by \(N_t(d)^2\) is \(1\). Otherwise, let \(a\ge1\) and \(b\ge1\) be the numbers of positive and negative coordinates (so \(a+b\le n\)), and let \(A,B>0\) be their respective sums of magnitudes. By Cauchy–Schwarz,
\[
\|d\|_2^2\ge\frac{A^2}{a}+\frac{B^2}{b},
\tag{5}
\]
with equality precisely when the positive coordinates are equal and the negative magnitudes are equal. As the quotient increases with \(\|d\|_2^2\) for fixed \(A,B\),
\[
\frac{(A-B)^2+t\|d\|_2^2}{(A+B)^2+t\|d\|_2^2}
\ge
1-\frac{4}{(1+t/a)r+2+(1+t/b)/r},\qquad r=\frac AB.
\tag{6}
\]
The denominator on the right is minimized over \(r>0\) at
\[
r=\sqrt{\frac{1+t/b}{1+t/a}},
\]
and its minimum is \(2+2\sqrt{(1+t/a)(1+t/b)}\). Consequently the quotient is bounded below by
\[
\frac{\sqrt{(1+t/a)(1+t/b)}-1}{\sqrt{(1+t/a)(1+t/b)}+1}.
\tag{7}
\]
This expression strictly decreases if either \(a\) or \(b\) increases, since \(t>0\). Under \(a+b\le n\), it is therefore minimized by using every coordinate and balancing the two group sizes: \(\{a,b\}=\{p,q\}\). The minimum equals \(c\). Formula (4) establishes (1) with \(C=c\).

**3. Attainment and normalization.** Choose
\[
r=\sqrt{\frac{1+t/q}{1+t/p}},\qquad
 d=\bigl(\underbrace{r/p,\ldots,r/p}_{p\text{ entries}},
 \underbrace{-1/q,\ldots,-1/q}_{q\text{ entries}}\bigr),
\]
and set \(v=(|d_1|,\ldots,|d_n|)\). Direct substitution into (5)–(7) gives
\[
(r-1)^2+t\|d\|_2^2=cN_t(d)^2,
\qquad (r^2-1)+t\left(\frac{r^2}{p}-\frac1q\right)=0.
\tag{8}
\]
For every \(k\ge1\), both \(kv+d\) and \(kv-d\) lie in the closed nonnegative orthant. Squaring the norm there and using (8) gives the exact identities
\[
N_t(kv+d)^2=N_t(kv-d)^2=(k^2+c)N_t(d)^2,
\qquad N_t(kv)=kN_t(d).
\tag{9}
\]
In particular, (1) is an equality for \(x=kv+d\), \(y=kv-d\); thus no constant larger than \(c\) works.

Normalize the pair from (9) by \(D=N_t(d)\sqrt{k^2+c}\), that is, set \(x_k=(kv+d)/D\), \(y_k=(kv-d)/D\). Both are unit vectors and
\[
N_t(x_k-y_k)=\frac{2}{\sqrt{k^2+c}},
\qquad N_t\!\left(\frac{x_k+y_k}{2}\right)=\frac{k}{\sqrt{k^2+c}}.
\tag{10}
\]
For an arbitrary pair in the unit ball, (1) implies
\[
N_t\!\left(\frac{x+y}{2}\right)^2
\le1-\frac{c}{4}N_t(x-y)^2.
\]
This proves the lower bound in (2) and (3). Conversely, for any \(0<\varepsilon\le 2/\sqrt{1+c}\), choosing \(k=\sqrt{4/\varepsilon^2-c}\ge1\) in (10) attains it. At \(\varepsilon=0\), choose identical unit vectors. Hence (2) holds.

**4. Why equality stops sharply.** Suppose \(\varepsilon>\varepsilon_*\) and equality held in the quadratic lower bound for \(\delta(\varepsilon)\). Since the unit ball in \(\mathbb R^n\) is compact, the defining infimum is attained. Equality forces \(N_t(x)=N_t(y)=1\), \(N_t(d)=\varepsilon/2\), and equality at every step of (4)–(7). The ratio in (7) must equal \(c<1\), so the signed vector \((\sigma_i d_i)_i\) has both positive and negative coordinates. For (4) to be equality, each vector \((\sigma_i(m_i\pm d_i))_i\) has all coordinates of one sign. The positive coordinate of \(d\) makes \(\sigma_i(m_i+d_i)>0\) somewhere; the negative coordinate makes \(\sigma_j(m_j-d_j)>0\) elsewhere. Hence *both* signed vectors are coordinatewise nonnegative. It follows that \(|m_i|\ge|d_i|\) for every \(i\), and thus \(N_t(m)\ge N_t(d)=\varepsilon/2\). But the purported equality requires
\[
N_t(m)^2=1-\frac{c\varepsilon^2}{4}<\frac{\varepsilon^2}{4}
\]
when \(\varepsilon>2/\sqrt{1+c}\), a contradiction. Compactness then gives the strict inequality (3). This completes the proof.

## Verification
The accompanying standalone `verify.py` is executable with Python 3 and only the standard library. Running `python3 verify.py` produced `Exact rational identities: 12`, `Deterministic numeric witness + random tests: 67536`, and `PASS (finite checks only)`. The exact-rational cases include a nontrivial odd-dimensional parameter, \(n=3,t=7\), whose minimizing coefficient is \(5/7\). The numeric checks cover \(2\le n\le13\), several positive parameters, explicit sharp witness pairs and seeded random pairs. These finite tests supplement the analytic proof and are not substitutes for the universal statements.

## Relationship to prior work
García-Lirola and Raja study moduli of convexity obtainable by renorming superreflexive spaces and their relation to generalized cotype; their results do not determine the exact midpoint coefficient of this specified finite-dimensional norm. Banaś, Ochab, and Zając survey strict and uniform convexity and smoothness moduli, without a formula for this hybrid family. De Bernardi and Veselý prove equality among several general definitions of convexity modulus for convex sets; such equivalence does not evaluate the present norm's modulus or its equality threshold. The present statements use classical definitions but require a family-specific signed-coordinate minimization and equality classification.

## Limitations
The complete classical modulus \(\delta(\varepsilon)\) is **not** determined for \(\varepsilon>\varepsilon_*\); only a strict comparison with the sharp quadratic envelope is proved there. The result is for real scalars, finite \(n\ge2\), and \(t>0\). No complex-space claim or assertion of uniqueness among all possible extremizing pairs is made. No uniqueness assertion is made for the extremizers; exact values beyond the equality threshold are not claimed.

## References
1. L. C. García-Lirola and M. Raja, *Uniformly convex renormings and generalized cotypes*, arXiv:1911.05657 (first public version 13 November 2019), https://arxiv.org/abs/1911.05657.
2. J. Banaś, J. Ochab and T. Zając, *On the smoothness of normed spaces*, Annals of Functional Analysis **15**, article 9 (2024), publicly posted 16 December 2023, https://doi.org/10.1007/s43034-023-00310-z.
3. C. A. De Bernardi and L. Veselý, *Moduli of uniform convexity for convex sets*, Archiv der Mathematik **123**, 413–422 (2024), first published 20 July 2024, https://doi.org/10.1007/s00013-024-02031-8.
