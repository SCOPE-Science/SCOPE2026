# The finite-population contact law in a stochastic COVID model is internally inconsistent

## Finding

The individual-based epidemic model has two incompatible exact contact laws.

Write
\[
M=n-y_H-y_C-y_D-1
\]
for the number of people available to a susceptible individual on a given day. Let
\[
N\le M
\]
be that individual's number of daily contacts, and let \(y_I\) and \(y_A\) denote the symptomatic and asymptomatic infectious people in the available pool.

The published contagion formula is
\[
\beta_{\mathrm{src}}
=
1-
\left(
1-\frac{q_Iy_I+q_Ay_A}{M}
\right)^N.
\]
It is obtained by treating the class counts among the \(N\) contacts as multinomial. That is the exact distribution when the \(N\) contact events are independent draws with replacement.

Later in the same model, the number of susceptible contacts made by an infectious individual is stated to be hypergeometric. A hypergeometric count is instead the exact law for choosing \(N\) distinct people without replacement.

These two sampling mechanisms are not the same at finite population size.

If the contacts are distinct, then the exact infection probability is
\[
\beta_{\mathrm{HG}}
=
1-
\frac{1}{\binom{M}{N}}
\sum_{\substack{i,a\ge0\\i+a\le N}}
\binom{y_I}{i}
\binom{y_A}{a}
\binom{M-y_I-y_A}{N-i-a}
(1-q_I)^i
(1-q_A)^a.
\]
Equivalently, its no-infection probability is
\[
\frac{
[z^N]
(1+(1-q_I)z)^{y_I}
(1+(1-q_A)z)^{y_A}
(1+z)^{M-y_I-y_A}
}{
\binom{M}{N}
}.
\]

For the simplest nontrivial state,
\[
y_I=1,\qquad y_A=0,
\]
this reduces to
\[
\beta_{\mathrm{HG}}=\frac{Nq_I}{M}.
\]
The published formula gives instead
\[
\beta_{\mathrm{src}}
=
1-\left(1-\frac{q_I}{M}\right)^N.
\]
For \(N>1\) and \(q_I>0\),
\[
\beta_{\mathrm{src}}<\beta_{\mathrm{HG}}.
\]

At the saturation boundary
\[
M=N=2,\qquad q_I=1,
\]
sampling two distinct people from a two-person contact pool necessarily includes the sole infectious person. Therefore
\[
\beta_{\mathrm{HG}}=1.
\]
The published formula gives
\[
\beta_{\mathrm{src}}=1-\left(1-\frac12\right)^2=\frac34.
\]

Conversely, if the multinomial law is intended to define the model, then susceptible contact events are independent draws. The number of susceptible contact events of an infectious individual must then be
\[
\operatorname{Bin}\!\left(
N,\frac{S(t)}{M}
\right),
\]
rather than hypergeometric.

Hence there is no single finite-population contact experiment for which both probability statements in the source are exact.

## Assumptions and scope

All population counts are nonnegative integers and
\[
0\le y_I+y_A\le M,\qquad
0\le N\le M,
\qquad
0\le q_I,q_A\le1.
\]

The correction concerns the exact finite-population sampling law. It does not claim that the paper's large-population simulations are numerically far from the intended model.

In particular, when
\[
\frac{N}{M}
\]
is small, sampling with and without replacement are close. The paper's first-order reproduction-number approximation therefore survives this correction.

The model's other class-transition rules, latency periods, quarantine durations, and clinical probabilities are not reassessed here.

## Proof

Under without-replacement sampling, the vector
\[
(J_I,J_A,N-J_I-J_A)
\]
of contact counts from the symptomatic infectious, asymptomatic infectious, and noninfectious groups has a multivariate hypergeometric distribution. Thus
\[
\Pr(J_I=i,J_A=a)
=
\frac{
\binom{y_I}{i}
\binom{y_A}{a}
\binom{M-y_I-y_A}{N-i-a}
}{
\binom{M}{N}
}.
\]

Conditional on these contact counts, independent transmission failures have probability
\[
(1-q_I)^i(1-q_A)^a.
\]
Averaging gives the displayed formula for \(1-\beta_{\mathrm{HG}}\).

For
\[
y_I=1,\qquad y_A=0,
\]
the unique infectious person is included in a uniformly chosen \(N\)-subset of the \(M\)-person pool with probability
\[
\frac{N}{M}.
\]
Conditional on inclusion, transmission occurs with probability \(q_I\). Therefore
\[
\beta_{\mathrm{HG}}=\frac{Nq_I}{M}.
\]

The source's multinomial expression is
\[
\beta_{\mathrm{src}}
=
1-\left(1-\frac{q_I}{M}\right)^N.
\]
Set
\[
x=\frac{q_I}{M}.
\]
For \(N>1\) and \(x>0\), the strict Bernoulli inequality gives
\[
(1-x)^N>1-Nx
\]
whenever \(x<1\). Hence
\[
1-(1-x)^N<Nx,
\]
which proves
\[
\beta_{\mathrm{src}}<\beta_{\mathrm{HG}}
\]
in the nondegenerate range. The saturation example is obtained by substituting
\[
M=N=2,\qquad q_I=1.
\]

For the converse, independent contact events with replacement assign each event to a susceptible individual with probability
\[
\frac{S(t)}{M}.
\]
The number of susceptible contact events in \(N\) trials is therefore binomial. A hypergeometric count would require drawing distinct members of the finite contact pool.

Finally, expanding the published one-infective formula gives
\[
1-\left(1-\frac{q_I}{M}\right)^N
=
\frac{Nq_I}{M}
-
\binom{N}{2}\frac{q_I^2}{M^2}
+
O(M^{-3}),
\]
for fixed \(N\). Thus the discrepancy begins at second order in the large-population regime, explaining why the source's leading reproduction-number approximation can remain correct even though the exact finite-population laws are incompatible.

## Verification

The bundled `verify.py` evaluates the multivariate-hypergeometric formula by exact rational arithmetic and by direct subset enumeration.

It verifies the saturation witness
\[
M=N=2,\qquad
y_I=1,\qquad
y_A=0,\qquad
q_I=1,
\]
for which the exact without-replacement probability is \(1\) and the published multinomial expression is \(3/4\).

It also checks a mixed two-infectious-class example and the one-infective closed form
\[
\beta_{\mathrm{HG}}=\frac{Nq_I}{M}.
\]

No simulation, asymptotic approximation, or finite search is used to establish the incompatibility.

## Relationship to prior work

Bardina, Ferrante, and Rovira, DOI 10.3934/math.2020490, define the COVID-19 model considered here. Their contagion calculation uses a multinomial distribution and presents the resulting power formula as the probability of contagion. In the reproduction-number discussion, the same paper states that the number of susceptible contacts among \(N\) contacts is hypergeometric.

Tuckwell and Williams, DOI 10.1016/j.mbs.2006.09.018, are the stated predecessor for the discrete contact model. Their full text explicitly says that the binomial contact-count law is used as an approximation when the population size is much larger than the daily number of contacts. Thus the distinction between finite-population sampling without replacement and the simpler binomial approximation is already present in the predecessor literature.

Ferrante, Ferraris, and Rovira, DOI 10.1007/s11749-015-0465-z, extend the same stochastic framework. Their model description says that a susceptible meets a given number of different individuals each day, but their later transition calculation again introduces the binomial law only under a large-population approximation. This makes clear that the general with-replacement approximation is prior knowledge.

The contribution here is source-specific: it identifies that the 2020 COVID-19 paper simultaneously uses the approximate multinomial law as an exact contagion probability and a hypergeometric law as an exact contact count, gives the exact two-infectious-class finite-population correction, and exhibits a saturation state where the two formulas differ by \(1/4\).

## Limitations

The result does not show that the numerical tables in the source change materially at the reported population size. With one infectious person and fixed \(N\), the discrepancy is of order
\[
M^{-2}.
\]
For the paper's early-outbreak regime with a very large accessible pool, it is therefore small.

The exact hypergeometric correction assumes that the intended finite-population contacts are distinct, which is the interpretation required by the paper's later hypergeometric statement and by its cited predecessor model. If instead repeated contacts are intentionally allowed, the multinomial contagion formula can be retained, but then the later hypergeometric contact-count assertion must be replaced by a binomial one.

The result does not address network persistence, repeated preferred contacts across days, or other contact structures beyond these two sampling mechanisms.

## References

1. X. Bardina, M. Ferrante, C. Rovira, “A stochastic epidemic model of COVID-19 disease,” AIMS Mathematics 5 (2020), 7661–7677. DOI: 10.3934/math.2020490. Published 26 September 2020.
2. H. C. Tuckwell, R. J. Williams, “Some properties of a simple stochastic epidemic model of SIR type,” Mathematical Biosciences 208 (2007), 76–97. DOI: 10.1016/j.mbs.2006.09.018.
3. M. Ferrante, E. Ferraris, C. Rovira, “On a stochastic epidemic SEIHR model and its diffusion approximation,” TEST 25 (2016), 482–502. DOI: 10.1007/s11749-015-0465-z.
