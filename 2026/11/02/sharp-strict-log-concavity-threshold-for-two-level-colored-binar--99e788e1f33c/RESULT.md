# Sharp strict log-concavity threshold for two-level colored binary partitions

## Finding

For each positive integer \(m\), let \(a_m(n)\), \(n\ge0\), count \(m\)-colored partitions using only parts of sizes \(1\) and \(2\); thus
\[
\sum_{n\ge0}a_m(n)q^n=\frac{1}{(1-q)^m(1-q^2)^m}.
\]
The entire positive-index sequence is **strictly log-concave if and only if \(m\ge4\)**:
\[
\bigl(\forall n\ge1:\ a_m(n)^2>a_m(n-1)a_m(n+1)\bigr)
\quad\Longleftrightarrow\quad m\ge4.
\]
This is the exact sharp color threshold for the first two denominations of colored binary partitions; no asymptotic lower bound on \(n\) is needed.

## Assumptions and scope

All quantities are integers; \(m\ge1\), \(n\ge0\). Distinguishable colors for equal-sized parts are counted as in the generating function; \(a_m(0)=1\), and \(a_m(n)=0\) for negative \(n\). The result is about **two allowed part sizes only**, not the unrestricted product over all powers of two.

## Proof

Set \(\Delta_m(n)=a_m(n)^2-a_m(n-1)a_m(n+1)\). First, coefficient extraction gives \(a_m(0)=1\), \(a_m(1)=m\), and \(a_m(2)=m(m+3)/2\), hence
\[
\Delta_m(1)=\frac{m(m-3)}2.
\]
For \(m\in\{1,2,3\}\) this is nonpositive, establishing the necessary threshold.

It remains to show that the four sequences with \(m\in\{4,5,6,7\}\) are strictly log-concave. Write \(n=2t+\varepsilon\), where \(t\ge0\) and \(\varepsilon\in\{0,1\}\). Since
\[
(1-q)^{-m}(1-q^2)^{-m}=(1+q)^m(1-q^2)^{-2m},
\]
we obtain the exact quasipolynomial formula
\[
a_m(2t+\varepsilon)=\sum_{\substack{0\le j\le m\\j\equiv\varepsilon\;({\rm mod}\;2)}}\binom mj\binom{t-(j-\varepsilon)/2+2m-1}{2m-1},
\]
where the ordinary combinatorial binomial coefficient is zero if its nonnegative integer upper argument is smaller than the lower argument. For either parity this is a polynomial in \(t\) of degree at most \(2m-1\); its polynomial extension also satisfies \(a_m(-1)=0\) when the odd branch is evaluated at \(t=-1\).

The following identities give **all eight** strict inequalities simultaneously. Put \(R_r(t)=\prod_{j=1}^{r}(t+j)^2\). For the row indexed by \(m\), let \(r,K,W_0,W_1,P_0,P_1\) have the values shown. Then
\[
\Delta_m(2t+\varepsilon)=\frac{R_r(t)}{K}\,W_\varepsilon(t)P_\varepsilon(t)
\qquad(t\ge0,\ \varepsilon\in\{0,1\}).
\]

| \(m\) | \(r\) | \(K\) | \(W_0(t)\) | \(W_1(t)\) |
|:--:|:--:|--:|:--|:--|
| 4 | 5 | 907200 | \(1\) | \((t+6)/(t+1)\) |
| 5 | 7 | 457228800 | \(1/(t+7)\) | \(1/(t+1)\) |
| 6 | 8 | 36212520960000 | \(1\) | \((t+9)/(t+1)\) |
| 7 | 10 | 93211028951040000 | \(1/(t+10)\) | \(1/(t+1)\) |

| \(m\) | \(P_0(t)\) | \(P_1(t)\) |
|:--:|:--|:--|
| 4 | \(4t^2+24t+63\) | \(4t^2+28t+21\) |
| 5 | \(2t^3+22t^2+75t+126\) | \(2t^3+26t^2+107t+90\) |
| 6 | \(64t^4+1152t^3+7184t^2+18000t+22275\) | \(64t^4+1280t^3+9136t^2+27360t+22275\) |
| 7 | \(32t^5+832t^4+8104t^3+36308t^2+73128t+70785\) | \(32t^5+928t^4+10216t^3+53012t^2+129096t+99099\) |

Each factor on the right is strictly positive for \(t\ge0\). For reproducibility, `verify.py` reconstructs the binomial-sum polynomials with exact rational arithmetic and checks each factorization at \(4m-1\) distinct nonnegative integers. Since each side is a rational polynomial in \(t\) of degree at most \(4m-2\), those finite checks prove each **polynomial identity for all \(t\)** by the root bound; they are not statistical extrapolations. The script also checks the boundary value and independently computes coefficients from the colored-parts sum.

For completeness, the strict property extends from \(m=4,5,6,7\) to all larger colors by convolution. A nonnegative sequence on \(\mathbb N_0\), with no internal zeros, is log-concave precisely when all \(2\times2\) minors of its lower-triangular Toeplitz matrix are nonnegative: this follows directly from the nonincreasing adjacent ratios. For nonnegative log-concave sequences \(u,v\), Cauchy--Binet applied to the product of Toeplitz matrices proves that their convolution is log-concave. If \(u\) is strictly log-concave and \(v(0)>0\), the minor with rows \(n,n+1\) and columns \(0,1\) has, in the Cauchy--Binet sum, the strictly positive summand
\[
\bigl(u(n)^2-u(n-1)u(n+1)\bigr)v(0)^2;
\]
all other summands are nonnegative. Thus the convolution is *strictly* log-concave for every \(n\ge1\). Since the generating functions satisfy \(A_m(q)=A_4(q)A_{m-4}(q)\) and every \(A_m\) is coefficientwise positive, strong induction beginning with the four cases \(4\) through \(7\) proves the assertion for all \(m\ge4\).

## Verification

Run `python3 verify.py` using Python's standard library; no external dependency is required. The program verifies 168 exact rational polynomial evaluations, sufficient by the explicit degree bound to certify the eight factor identities; it also checks 516 independent coefficient comparisons and finite direct inequalities (these supplemental finite tests are not an infinite proof). Its output must read `PASS` and terminate without an assertion error. The algebraic convolution argument and the sharp necessary condition above are independent of computational extrapolation.

## Relationship to prior work

Gawron, Miska and Ulas, first available 2017-03-06, formulate strict log-concavity for the **full** \(m\)-colored binary partition generating function as Conjecture 5.10. The present theorem determines the complete uniform threshold for its **first two denominations** and does not imply their infinite-product conjecture: adjoining extra factors need not preserve log-concavity. Gajdzica's 2022 Theorem 5.6 gives eventual log-concavity for broad finite multisets under explicit assumptions; it does not give the exact all-index threshold for this specific multiset. Bringmann, Kane, Pahari and Rolen study *ordinary* colored partitions with all positive part sizes, which is another distinct sequence.

## Limitations

The theorem does not establish strict log-concavity after permitting \(4,8,16,\ldots\), nor a uniform theorem for arbitrary finite sets of permitted denominations. The proof supplies the exact two-level boundary only. Independent scientific validation and absolute bibliographic priority have not been established.

## References

1. M. Gawron, P. Miska, M. Ulas, *Arithmetic properties of coefficients of power series expansion of a binary infinite product*, arXiv:1703.01955v1 (2017-03-06), especially Conjecture 5.10. https://arxiv.org/abs/1703.01955
2. K. Gajdzica, *Log-concavity of the restricted partition function and the new Bessenrodt--Ono type inequality*, arXiv:2206.04752v1 (2022-06-09), especially Theorem 5.6. https://arxiv.org/html/2206.04752v1
3. K. Bringmann, B. Kane, A. Pahari, L. Rolen, *Strict log-concavity of k-coloured partitions*, Proceedings of the Royal Society of Edinburgh, published online 2026-05-18, DOI 10.1017/prm.2026.10154.
