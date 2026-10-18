# Complete five-root binomid classification with one exceptional quintic

## Finding

Let \(a_1\le a_2\le a_3\le a_4\le a_5\) be nonnegative integers and put
\[
f(n)=\prod_{i=1}^{5}(n+a_i),\qquad n=1,2,\ldots .
\]
Call \(f\) *binomid* when every generalized coefficient
\[
B_f(n,k)=\frac{\prod_{t=n-k+1}^{n}f(t)}{\prod_{t=1}^{k}f(t)}
\qquad(0\le k\le n)
\]
is an integer (empty products equal one). Then the following are equivalent:

1. \(f\) is binomid;
2. the three quantities \(f(2)/f(1)\), \(f(3)/f(1)\), and \(f(3)f(4)/(f(1)f(2))\) are integers;
3. the ordered shift tuple is one of
\[
\begin{gathered}
(0,0,0,0,0),\ (0,0,0,0,1),\ (0,0,0,1,1),\ (0,0,0,1,2),\\
(0,0,0,1,3),\ (0,0,1,1,2),\ (0,0,1,2,3),\ (0,1,2,3,4).
\end{gathered}
\]

Seven families are products of Pascal-column polynomials, up to nonzero constant multiples. The eighth, with shift tuple \((0,0,0,1,3)\), has
\(f(n)=n^3(n+1)(n+3)\) and is binomid despite the gap in its root-shift multiplicities.

## Assumptions and scope

The shifts are **five integers** ordered as written, all nonnegative. Hence \(f(n)>0\) for every positive integer \(n\). The classification includes repeated shifts and makes no claim about arbitrary rational-root or complex-root quintics, polynomials with positive roots, or binomidness at higher iterated levels. Nonzero constant rescalings leave the generalized coefficients unchanged.

## Proof

**Necessity and exhaustive finite recognition.** The three tests in the statement are particular generalized coefficients, namely \(B_f(2,1)\), \(B_f(3,1)\), and \(B_f(4,2)\). Let \(q(a)=(a+2)/(a+1)\), a strictly decreasing function on the nonnegative integers. The first test is precisely that \(R_5=\prod_{i=1}^5q(a_i)\) is integral.

An exact finite branch-and-bound calculation suffices to classify every possible first-test tuple, with no arbitrary root cutoff. For a sorted prefix of length \(j<5\), let \(R_j=\prod_{i=1}^{j}q(a_i)\) and \(r=5-j\). If the next shift is \(a\ge a_j\) (or \(a\ge0\) when the prefix is empty), any completion satisfies
\[
R_j< R_5\le R_jq(a)^r.
\]
Therefore an integral completion requires
\[
R_jq(a)^r\ge \lfloor R_j\rfloor+1.
\]
The left side decreases strictly to \(R_j\) as \(a\) increases, so only finitely many \(a\) are possible. Recursing over every integer \(a\) satisfying the displayed inequality is exhaustive, and exact rational arithmetic decides the terminal divisibility. The attached `verify.py` implements this recursion with `fractions.Fraction`; it traverses 927,939 finite prefix nodes and finds exactly 1,323 nondecreasing five-tuples with integral \(f(2)/f(1)\). Filtering these by the other two stated divisibilities leaves exactly the eight displayed tuples. These are finite exhaustive calculations certified by the explicit termination and coverage invariant, not an arbitrary range scan.

**Seven standard cases.** In seven of the eight tuples the multiplicities \(e_s=|\{i:a_i=s\}|\) are weakly decreasing in \(s\ge0\), with eventually zero terms. Consequently \(f(n)\) is a nonzero constant multiple of a product of Pascal-column polynomials \(C_h(n)=\binom{n+h-1}{h}\): take \(e_{h-1}-e_h\) copies of \(C_h\). The binomid property of every \(C_h\) follows, for example, from its determinantal formula of consecutive binomial coefficients; pointwise products and constant rescalings preserve binomidness. These facts are explicitly proved or cited in Shapiro, Sections 1–2 (arXiv:2302.02243v1). The remaining tuple has \(e_2=0<e_3=1\), so it cannot be such a product: multiplicities of a Pascal-column product must be weakly decreasing.

**Exceptional case.** Let \(f(n)=n^3(n+1)(n+3)\). For any integer \(m\ge2\) and \(0\le x,y<m\), define
\[
E_m(x,y)=\sum_{s\in\{0,0,0,1,3\}}
\left(\left\lfloor\frac{x+y+s}{m}\right\rfloor-
\left\lfloor\frac{x+s}{m}\right\rfloor-
\left\lfloor\frac{y+s}{m}\right\rfloor+
\left\lfloor\frac{s}{m}\right\rfloor\right).
\]
We claim \(E_m\ge0\) for all \(m\ne4\); for \(m=4\) it is nonnegative except \(E_4(1,1)=-1\). Moreover \(E_2(1,1)=1\).

To verify the claim, write \(c=\lfloor(x+y)/m\rfloor\). The three zero shifts give \(3c\). For \(m\ge6\), when \(c=1\), either nonzero shift contributes at least \(-1\), so \(E_m\ge1\). When \(c=0\), a negative contribution from shift \(s\in\{1,3\}\) would require both \(x,y\ge m-s\), contradicting \(x+y<m\) since \(m\ge2s\). For \(m=5\), the sole possible negative contribution when \(c=0\) occurs at \((x,y)=(2,2)\) for shift \(3\), and shift \(1\) contributes \(+1\) there. For \(m=4\), the only unbalanced negative case is \((x,y)=(1,1)\); the cases \((1,2)\) and \((2,1)\) have a compensating positive shift-\(1\) term. For \(m=3\), shift \(3\) is a zero shift and the other shift cannot be negative when \(c=0\); for \(m=2\), direct examination of the four pairs gives nonnegativity and \(E_2(1,1)=1\). This establishes every claimed inequality for every modulus, not merely the finitely tested ones.

Fix a prime \(p\), and integers \(n\ge k\ge0\). Set \(x=k\), \(y=n-k\) and reduce both modulo \(p^j\) for each \(j\ge1\). Legendre's factorial valuation identity yields exactly
\[
\nu_p(B_f(n,k))=
\sum_{j\ge1} E_{p^j}(k\bmod p^j,(n-k)\bmod p^j).
\]
This sum is finite for fixed \(n,k\). All terms are nonnegative except possibly the \(p^j=4\) term. Such a negative term forces both residues to be \(1\) modulo \(4\), and therefore the \(p^j=2\) term is \(+1\), compensating exactly. Hence \(\nu_p(B_f(n,k))\ge0\) for every prime, and \(B_f(n,k)\in\mathbb Z\) for all \(n,k\). This proves sufficiency and the theorem.

## Verification

Run `python3 verify.py` in the directory containing this file. The Python standard-library verifier performs exact rational prefix enumeration (1,323 terminal candidates, 927,939 prefix nodes), checks the three recognition tests, all pairs of residues for moduli \(2\) through \(64\), and direct generalized coefficients in rows \(1\) through \(80\) for all eight tuples. It emits the recorded `verification_output.txt`. The infinite binomid conclusion rests on the modulus lemma and Legendre's identity; finite checks alone are not a substitute.

## Relationship to prior work

Shapiro's *Divisibility Properties for Integer Sequences* (arXiv:2302.02243v1, first public 2023-02-04), especially Sections 1–2 and 4.3, proves the Pascal-column result, pointwise closure, and a classification through degree two; it explicitly describes higher-degree polynomial classification as difficult. The present result concerns the natural quintic subfamily with five nonpositive integer roots, not arbitrary quintics. Caalim and Tanaka (arXiv:2505.20018v1) give a general prime-valuation/binomid-index framework rather than this eight-tuple or three-test classification. No equivalent quintic theorem was found in the inspected published-finding corpus records or targeted searches; that observation is not a proof of global originality.

## Limitations

The proof uses one exhaustive, reproducible finite enumeration for the necessity classification, with explicit mathematical bounds and exact arithmetic. The exceptional sufficiency proof is unrestricted. The theorem does not extend to arbitrary quintic coefficients, negative root shifts, the classification of all binomid polynomials of degree five, or second-level binomidness. Unindexed equivalent literature is a residual originality risk.

## References

1. Daniel B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1, 2023-02-04, https://arxiv.org/pdf/2302.02243.
2. Jonathan Caalim and Yu-ichi Tanaka, *On the monoid of lexicographically minimal extensions*, arXiv:2505.20018v1, 2025-05-26, https://arxiv.org/pdf/2505.20018.
