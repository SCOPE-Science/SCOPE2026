# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The deficit
\[
D_{n,r}(x)
=
n\exp\!\left(r\sum_i x_i\log x_i\right)
-
\sum_i\exp\!\left(r x_i\sum_j\log x_j\right)
\]
was re-expanded directly at \(x=t\mathbf1\). The constant and linear terms
cancel. The second-order coefficient simplifies to
\[
t^{rnt}
\left(\frac r t-\frac{nr^2}{2}(\log t)^2\right)
\left(n\sum_i y_i^2-(\sum_i y_i)^2\right),
\]
and the final factor equals \(\sum_{i<j}(y_i-y_j)^2\).

The scalar function \(t(\log t)^2\) on \((0,1]\) has its unique interior
maximum \(4/e^2\) at \(t=e^{-2}\). Hence the transverse Hessian is negative
somewhere on the diagonal exactly when \(r>e^2/(2n)\). At \(r=1\) this
occurs for every \(n\ge4\), giving genuine nearby counterexamples with all
coordinates still in \((0,1]\).

The critical calculation was also checked independently from the exact
one-coordinate factorization
\[
D_{n,r_0}
=
P^{r_0t}[n a^{r_0\varepsilon}-P^{r_0\varepsilon}-(n-1)],
\]
where \(t=e^{-2}\), \(a=t+\varepsilon\), \(P=at^{n-1}\), and
\(r_0=e^2/(2n)\). With \(u=e^2\varepsilon\), the bracket has cubic term
\[
-\frac{(n-1)(n-2)}{12n^2}u^3,
\]
which gives the stated negative cubic coefficient for \(n\ge3\).

The verification artifact uses high-precision arithmetic only as
corroboration. It reproduces the \(n=4,r=1\) strict counterexample, compares
\(D/\varepsilon^2\) with the analytic quadratic coefficient, checks the
\(r=e\) failures, and compares \(D/\varepsilon^3\) with the critical cubic
coefficient.

## Originality

PASS, to the best of our knowledge.

The 2014 Coronel--Huancas primary source was checked at Theorem 1.4, its
three-variable proof discussion, and Conjecture 3.3. The theorem is stated
for arbitrary \(n\), while the displayed proof details in Section 2.5 are
developed in three variables.

The closest correction located is Matejíčka (2016),
*On the Cîrtoaje's conjecture*. Its introduction explicitly says that
Theorems 1.2 and 1.3, Lemma 3.1, and Conjectures 3.1 and 3.2 of the 2014
paper are not valid. Theorem 1.4 and Conjecture 3.3 are not included in that
list. The subsequent 2016 paper *Some remarks on Cîrtoaje's conjecture* and
the 2017 *Next generalization of Cîrtoaje's inequality* treat another
Cîrtoaje-type inequality and generalized solution sets.

Searches used the exact paper title, Theorem 1.4, Conjecture 3.3, the
product inequality itself, counterexample/invalidity language, local and
second-variation terminology, and the threshold \(e^2/(2n)\). A 2025 paper
on the two-variable Cîrtoaje inequality and a 2026 collection of
power-exponential inequalities were also checked as recent status
indicators. No located source states the all-\(n\) failure of Theorem 1.4 or
the diagonal-instability boundary derived here.

The main residual originality risk is an unindexed correction, informal
note, or equivalent calculation written in substantially different
notation. Absence from the searches is not a proof that no such source
exists.

## Value

PASS.

This result does more than refute a later conjectural parameter extension:
it gives an analytic family of counterexamples to a theorem published in
2014, for every dimension \(n\ge4\). The same Hessian calculation identifies
the exact onset \(e^2/(2n)\) of diagonal quadratic instability in the
parameterized problem, and the cubic calculation settles the critical
value for every \(n\ge3\). The mechanism is elementary, explicit, and
reusable for nearby power-exponential inequalities.

## Limitations

- The locally stable side \(r\le e^2/(2n)\) is not proved globally valid.
- The critical case \(n=2,\ r=e^2/4\) is unresolved by the displayed
  expansion.
- The \(r=1\) cases \(n=2,3\) are not classified globally here.
- Originality is to the best of our knowledge; unindexed equivalent coverage
  remains possible.
- Independent audit has not been performed.
