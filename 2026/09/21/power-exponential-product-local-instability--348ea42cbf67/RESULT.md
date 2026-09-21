# A diagonal-instability mechanism for a power-exponential product inequality

## Statement

For \(n\ge 2\), \(r>0\), and \(x=(x_1,\dots,x_n)\in(0,1]^n\), define
\[
D_{n,r}(x)
=
n\prod_{i=1}^n x_i^{r x_i}
-
\sum_{i=1}^n
\left(\prod_{j=1}^n x_j\right)^{r x_i}.
\]

Coronel and Huancas (2014) stated, as their Theorem 1.4, that
\[
D_{n,1}(x)\ge 0
\qquad (n\in\mathbb N,\ x_i\in(0,1]),
\]
and later proposed the parameterized inequality \(D_{n,r}(x)\ge0\) for
\(r\in[0,e]\) as Conjecture 3.3.

The following second-variation formula gives a systematic obstruction.

**Theorem.** Fix \(t\in(0,1]\) and \(y=(y_1,\dots,y_n)\in\mathbb R^n\). As
\(\varepsilon\to0\),
\[
D_{n,r}(t\mathbf 1+\varepsilon y)
=
t^{rnt}
\left(
\frac r t-\frac{nr^2}{2}(\log t)^2
\right)
\left(
n\sum_{i=1}^n y_i^2-\left(\sum_{i=1}^n y_i\right)^2
\right)
\varepsilon^2
+O(\varepsilon^3).
\]
The variance factor is
\[
n\sum_i y_i^2-\left(\sum_i y_i\right)^2
=
\sum_{1\le i<j\le n}(y_i-y_j)^2.
\]

Consequently:

1. The diagonal family has a negative transverse second variation somewhere
   in \((0,1]^n\) exactly when
   \[
   r>\frac{e^2}{2n}.
   \]
   At the maximizing diagonal point \(t=e^{-2}\),
   \[
   D_{n,r}(e^{-2}\mathbf1+\varepsilon y)
   =
   e^{-2rn/e^2}\,r(e^2-2nr)
   \sum_{i<j}(y_i-y_j)^2\,\varepsilon^2
   +O(\varepsilon^3).
   \]

2. In particular, the published Theorem 1.4 is false for every
   \[
   \boxed{n\ge4}.
   \]
   Indeed \(1>e^2/(2n)\) for \(n\ge4\), so every nonconstant direction gives
   nearby counterexamples at \(t=e^{-2}\).

3. The parameterized Conjecture 3.3 is false for every \(n\ge2\). More
   precisely, for each \(n\ge2\) and every
   \[
   \frac{e^2}{2n}<r\le e,
   \]
   it has counterexamples arbitrarily close to the diagonal
   \(e^{-2}\mathbf1\).

4. The critical value is already unstable for \(n\ge3\). If
   \[
   r_0=\frac{e^2}{2n},\qquad
   x_1=e^{-2}+\varepsilon,\qquad
   x_2=\cdots=x_n=e^{-2},
   \]
   then
   \[
   D_{n,r_0}(x)
   =
   -\frac{(n-1)(n-2)e^5}{12n^2}\,\varepsilon^3
   +O(\varepsilon^4).
   \]
   Hence Conjecture 3.3 also fails at \(r=e^2/(2n)\) for every \(n\ge3\).

The critical case \(n=2,\ r=e^2/4\) is not decided by this expansion.

## Proof of the second-variation formula

Put
\[
S_1=\sum_{i=1}^n y_i,\qquad S_2=\sum_{i=1}^n y_i^2,
\]
and write \(x_i=t+\varepsilon y_i\). Define
\[
A=r\sum_{i=1}^n x_i\log x_i,\qquad
L=\sum_{i=1}^n\log x_i,\qquad
B_i=r x_iL.
\]
Then
\[
D_{n,r}=n e^A-\sum_{i=1}^n e^{B_i}.
\]

Taylor expansion at the diagonal gives
\[
A
=
rnt\log t
+r(\log t+1)S_1\varepsilon
+\frac r{2t}S_2\varepsilon^2
+O(\varepsilon^3),
\]
and
\[
B_i
=
rnt\log t
+r(S_1+n(\log t)y_i)\varepsilon
+\frac r t\left(y_iS_1-\frac12S_2\right)\varepsilon^2
+O(\varepsilon^3).
\]
After expanding the exponentials, the constant and linear terms cancel. The
quadratic contribution from the non-exponential second-order terms is
\[
\frac r t(nS_2-S_1^2),
\]
while the squared linear terms contribute
\[
-\frac{nr^2}{2}(\log t)^2(nS_2-S_1^2).
\]
Factoring out \(e^{rnt\log t}=t^{rnt}\) proves the formula.

For fixed \(r,n\), a negative transverse quadratic term exists exactly when
\[
rnt(\log t)^2>2.
\]
On \(0<t\le1\),
\[
\max t(\log t)^2=\frac4{e^2},
\]
attained at \(t=e^{-2}\). Thus such a \(t\) exists exactly when
\(r>e^2/(2n)\).

For \(r=1\) and \(n\ge4\), this condition holds because \(e^2<8\le2n\).
Taking, for example, \(y=(1,0,\dots,0)\) and sufficiently small positive
\(\varepsilon\) keeps all coordinates in \((0,1]\) and makes \(D_{n,1}<0\).

## Critical cubic term

Let \(t=e^{-2}\), \(r_0=e^2/(2n)\), \(a=t+\varepsilon\), and
\(P=a t^{n-1}\). For the one-coordinate perturbation above,
\[
D_{n,r_0}
=
P^{r_0t}
\left[
n a^{r_0\varepsilon}
-P^{r_0\varepsilon}
-(n-1)
\right].
\]
Set \(u=e^2\varepsilon\). Since \(a=t(1+u)\) and
\(r_0\varepsilon=u/(2n)\),
\[
n a^{r_0\varepsilon}
-P^{r_0\varepsilon}
-(n-1)
=
-\frac{(n-1)(n-2)}{12n^2}u^3+O(u^4).
\]
Moreover \(P^{r_0t}=e^{-1}+O(u)\). As \(u^3=e^6\varepsilon^3\), this yields
\[
D_{n,r_0}
=
-\frac{(n-1)(n-2)e^5}{12n^2}\varepsilon^3
+O(\varepsilon^4).
\]

## A concrete counterexample

For \(n=4\), \(r=1\), let
\[
t=e^{-2},\qquad
(x_1,x_2,x_3,x_4)=(t+10^{-3},t,t,t).
\]
High-precision evaluation gives
\[
D_{4,1}(x)
\approx -6.2196915253892544522\times10^{-7}<0.
\]
Thus the failure of Theorem 1.4 does not depend on taking \(r\ne1\).

The accompanying verification script checks this example, the quadratic
coefficient for several dimensions, the failure at \(r=e\), and the critical
cubic coefficient.

## Literature context and originality

Coronel and Huancas, *The proof of three power-exponential inequalities*
(2014), state Theorem 1.4 for arbitrary \(n\) and \(x_i\in(0,1]\), and
their Section 3 states Conjecture 3.3 with the parameter \(r\in[0,e]\).

Matejíčka (2016), in *On the Cîrtoaje's conjecture*, explicitly records that
Theorems 1.2 and 1.3, Lemma 3.1, and Conjectures 3.1 and 3.2 of the 2014
paper are not valid, and gives a counterexample to a different
power-exponential inequality. That correction does not list Theorem 1.4 or
Conjecture 3.3. Matejíčka's subsequent 2016 and 2017 papers concern the
Cîrtoaje inequality and its generalized solution sets rather than the product
inequality above. Later papers located through 2026 cite the 2014 article but
do not appear to state this diagonal second-variation obstruction.

To the best of our knowledge, the failure of the published Theorem 1.4 for
all \(n\ge4\), the quantified counterexample range for Conjecture 3.3, and
the threshold \(e^2/(2n)\) for diagonal second-variation instability have not
previously been recorded. This is not an exhaustive originality guarantee;
an unindexed correction, note, or equivalent result in different notation
remains possible.

## Limitations

- The condition \(r\le e^2/(2n)\) is only a local second-variation stability
  condition along the diagonal family; it does **not** prove the global
  inequality in that range.
- The critical case \(n=2,\ r=e^2/4\) is not classified here.
- The result does not determine whether the original \(r=1\) inequality is
  globally valid for \(n=2\) or \(n=3\); it only shows that the stated
  all-\(n\) theorem fails for every \(n\ge4\).
- Originality is assessed to the best of our knowledge from the sources and
  searches described above.

## Reproducibility

Run
```text
python artifacts/verify_power_exponential_instability.py
```
with Python 3 and `mpmath`. The script uses 80 decimal digits and verifies
representative asymptotic ratios and strict numerical counterexamples.

## References

1. A. Coronel and F. Huancas, *The proof of three power-exponential
   inequalities*, Journal of Inequalities and Applications 2014, Article 509.
   DOI: 10.1186/1029-242X-2014-509. arXiv:1409.1968.
2. L. Matejíčka, *On the Cîrtoaje's conjecture*, Journal of Inequalities and
   Applications 2016, Article 152. DOI: 10.1186/s13660-016-1092-2.
3. L. Matejíčka, *Some remarks on Cîrtoaje's conjecture*, Journal of
   Inequalities and Applications 2016. DOI: 10.1186/s13660-016-1211-0.
4. L. Matejíčka, *Next generalization of Cîrtoaje's inequality*, Journal of
   Inequalities and Applications 2017, Article 159.
   DOI: 10.1186/s13660-017-1436-6.
5. E. Hara, D. Haranaka, Y. Nishizawa, and T. Yokota, *New three proofs of
   Cîrtoaje inequality*, Journal of Mathematical Inequalities 19 (2025),
   909--919. DOI: 10.7153/jmi-2025-19-58.
6. A. Kyriakis, *A Collection of Inequalities Involving Power Exponential and
   Logarithmic Functions*, Earthline Journal of Mathematical Sciences 16
   (2026), 199--220. DOI: 10.34198/ejms.16226.16.199220.
