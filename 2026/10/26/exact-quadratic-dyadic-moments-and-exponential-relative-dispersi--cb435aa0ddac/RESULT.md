# Exact quadratic dyadic moments and exponential relative dispersion of a divisor-counting sequence

## Finding
Let \(s:\mathbb N_{\ge1}\to\mathbb N_0\) be the sequence A383066 defined by \(s(1)=0\), \(s(2)=s(3)=1\), and, for every integer \(k\ge1\),
\[
\begin{aligned}
s(4k)&=2s(2k)-s(k),\\
s(4k+1)&=2s(2k)+s(2k+1),\\
s(4k+2)&=2s(2k+1)+s(2k),\\
s(4k+3)&=2s(2k+1)-s(k).
\end{aligned}
\]
For every integer \(n\ge0\), put
\[
R_n=\sum_{2^n\le k<2^{n+1}}s(k),\qquad
P_n=\sum_{2^n\le k<2^{n+1}}s(k)^2.
\]
Then the **exact quadratic row-moment generating function** is
\[
\boxed{\sum_{n\ge0}P_nz^n=
\frac{2z(1+z+2z^2)}{(1+z)(1-2z)(1-11z+2z^2)}.}
\]
In particular,
\[
P_0=0,\quad P_1=2,\quad P_2=26,\quad P_3=294,
\]
and \(P_n=12P_{n-1}-11P_{n-2}-20P_{n-3}+4P_{n-4}\) for all \(n\ge4\). More explicitly, writing
\[
\lambda_{\pm}=\frac{11\pm\sqrt{113}}2,\qquad K=\frac3{14}\left(1+\frac1{\sqrt{113}}\right),
\]
one has, for every \(n\ge0\),
\[
\boxed{
P_n=\frac3{14}\left[
\left(1+\frac1{\sqrt{113}}\right)\lambda_+^n+
\left(1-\frac1{\sqrt{113}}\right)\lambda_-^n
\right]-\frac{2^n}3-\frac{2(-1)^n}{21}.}
\]
For \(n\ge1\), let \(X_n\) be \(s(k)\) when \(k\) is uniform in the dyadic interval \([2^n,2^{n+1})\), and let \(\mu_n=\mathbb E[X_n]\). With
\[
\alpha_+=\frac{5+\sqrt{17}}2,\qquad
q=\frac{2\lambda_+}{\alpha_+^2}
=\frac{4(11+\sqrt{113})}{(5+\sqrt{17})^2}>1,
\]
the exact second moment gives the **exponentially growing squared coefficient of variation**
\[
\boxed{\frac{\operatorname{Var}(X_n)}{\mu_n^2}\sim\frac{17K}4\,q^n.}
\]
Numerically \(q\approx1.03952283129313\), so the coefficient of variation itself grows at exponential base approximately \(1.01956992467\). This is a statement about dyadic relative second moments, not a limiting distribution.

## Assumptions and scope
All quantities above are exact for the specifically defined 2-regular integer sequence. The generating-function identity is an identity of formal power series over \(\mathbb Q\). The asymptotic claim takes \(n\to\infty\) through nonnegative integers; \(X_n\) samples the dyadic row uniformly, not an interval of arbitrary endpoints and not a uniformly sampled divisor of a quadratic value.

The known divisor-tree interpretation starts with \((d,m)=(1,0)\) and gives every node two children
\[
L(d,m)=(d,m+d),\qquad
R(d,m)=\left(\frac{(m+d)^2+1}{d},m+\frac{m^2+1}{d}\right),
\]
where \(d\) is a positive divisor of \(m^2+1\). The values \(m\) on level \(n\), in left-to-right order, are precisely \(s(k)\) for \(2^n\le k<2^{n+1}\). The published construction justifies this identification; the moment computation below is independent once the child maps are fixed.

## Proof
**1. A closed four-state quadratic transfer.** Set \(e=(m^2+1)/d\). Thus \(d,e\) are positive integers and \(de=m^2+1\). The two child triples \((d',e',m')\) are exactly
\[
(d,d+e+2m,m+d),\qquad(d+e+2m,e,m+e).
\]
These follow by substituting the child formulas and using \(de=m^2+1\); both preserve the displayed invariant.

At level \(n\), define
\[
A_n=\sum(d^2+e^2),\qquad B_n=\sum m(d+e),\qquad P_n=\sum m^2,
\]
with sums over all \(2^n\) nodes. At the root, \((A_0,B_0,P_0)=(2,0,0)\). Let \(T_n=2^n\). For any parent, the sums of the respective observables over its two children are
\[
\begin{aligned}
(d_L^2+e_L^2)+(d_R^2+e_R^2)
&=3(d^2+e^2)+8m(d+e)+12m^2+4,\\
m_L(d_L+e_L)+m_R(d_R+e_R)
&=2(d^2+e^2)+5m(d+e)+6m^2+2,\\
m_L^2+m_R^2&=(d^2+e^2)+2m(d+e)+2m^2.
\end{aligned}
\]
The constants \(4\) and \(2\) arise exactly from \(de=m^2+1\). Summing produces, for every \(n\ge0\),
\[
\begin{pmatrix}A_{n+1}\\B_{n+1}\\P_{n+1}\\T_{n+1}\end{pmatrix}
=
\begin{pmatrix}
3&8&12&4\\2&5&6&2\\1&2&2&0\\0&0&0&2
\end{pmatrix}
\begin{pmatrix}A_n\\B_n\\P_n\\T_n\end{pmatrix},
\qquad
\begin{pmatrix}A_0\\B_0\\P_0\\T_0\end{pmatrix}
=\begin{pmatrix}2\\0\\0\\1\end{pmatrix}.
\]
This is an exact transfer identity for all levels, with no truncation or empirical premise.

**2. Extract the second moment.** Write the transfer matrix as \(M\) and the initial column as \(v\). Formal series algebra gives
\[
\sum_{n\ge0}P_nz^n=e_3^{\mathsf T}(I-zM)^{-1}v.
\]
Expansion of the indicated four-by-four determinant and third adjugate row gives numerator \(2z(1+z+2z^2)\), while
\[
\det(I-zM)=(1+z)(1-2z)(1-11z+2z^2).
\]
This proves the rational identity. The denominator expands to \(1-12z+11z^2+20z^3-4z^4\), yielding the recurrence and four initial values. Partial fractions, or substitution into that recurrence and verification of four initial values, yields the closed form displayed above, with all powers and coefficients exact.

**3. Relative dispersion.** The published row-sum formula is
\[
R_n=\frac2{\sqrt{17}}(\alpha_+^n-\alpha_-^n),\qquad
\alpha_-=\frac{5-\sqrt{17}}2.
\]
Consequently \(\mu_n=R_n/2^n>0\) for \(n\ge1\) and
\[
\frac{\operatorname{Var}(X_n)}{\mu_n^2}
=\frac{2^nP_n}{R_n^2}-1.
\]
Since \(|\lambda_-|<\lambda_+\), \(2<\lambda_+\), \(1<\lambda_+\), and \(0<\alpha_-<\alpha_+\), the exact expressions imply
\(P_n\sim K\lambda_+^n\) and \(R_n\sim 2\alpha_+^n/\sqrt{17}\). Therefore
\[
\frac{2^nP_n}{R_n^2}\sim\frac{17K}{4}
\left(\frac{2\lambda_+}{\alpha_+^2}\right)^n.
\]
Finally,
\[
2\lambda_+-\alpha_+^2
=\frac12+\sqrt{113}-\frac52\sqrt{17}>0,
\]
as follows, for example, from \(\sqrt{113}>10\) and \(\sqrt{17}<21/5\). Hence \(q>1\), and subtracting \(1\) does not affect the asymptotic equivalent. This completes the proof.

## Verification
The standalone file `verify.py` reproduces the 2-regular recurrences independently of the divisor tree, constructs both children using exact integer arithmetic, and compares the full observable transfer with direct tree sums through depth \(12\). It also compares every tree value with the correspondingly indexed sequence value, checks the fourth-order quadratic-moment recurrence through that depth, and matches the first nine moment sums to the explicit claimed list. Run `python3 verify.py` from the directory containing this file. The reported successful run was `VERIFY_OK depths=12 exact_tree_nodes=8191 moment_recurrences=9 base_terms=PASS`.

These finite computations test implementation and algebraic bookkeeping but are not the proof of the formal identity or the asymptotic claim; those follow from the exact transfer and spectral comparison.

## Relationship to prior work
Shakov, *A 2-Regular Sequence That Counts The Divisors of \(n^2+1\)* (2025), introduces A383066 in this setting and gives the first row moment (Proposition 7) along with the divisor-counting construction. An earlier Shakov preprint (2024), *Polynomials in \(\mathbb Z[x]\) whose divisors are enumerated by \(\mathrm{SL}_2(\mathbb N_0)\)*, constructs the same sequence and establishes first row sums and ratios in Section 5. These results are premises, **not new contributions** here. The OEIS A383066 entry records the four 2-regular recurrences and references both papers.

The present claim is narrower than a general moment theorem: it supplies the particular exact quadratic transfer, a rational generating function with poles \(\lambda_\pm\), and a strict relative-dispersion exponent above one. The inspected prior formulas for first moments, divisor counts, and the largest term on a row do not, on their own, specify this second moment or its spectral growth constant.

## Limitations
No claim is made about a distributional limit for normalized sequence values, higher moments, arbitrary non-dyadic sample windows, or the rate of occurrence of particular divisor values. In particular, divergence of relative variance alone does not prove nonconvergence in probability after normalizing by the mean. A pre-existing general transfer or second-moment formula for this tree may yield an equivalent consequence, so bibliographic priority is not independently established.

## References
1. A. Shakov, *A 2-Regular Sequence That Counts The Divisors of \(n^2+1\)*, *Journal of Integer Sequences* **28** (2025), Article 25.6.2; arXiv:2510.22805v1 (26 October 2025), https://arxiv.org/abs/2510.22805.
2. A. Shakov, *Polynomials in \(\mathbb Z[x]\) whose divisors are enumerated by \(\mathrm{SL}_2(\mathbb N_0)\)*, arXiv:2405.03552v1 (6 May 2024), https://arxiv.org/abs/2405.03552.
3. OEIS Foundation, Sequence A383066, *A 2-regular sequence associated with the number of divisors of \(n^2+1\)*, https://oeis.org/A383066.
