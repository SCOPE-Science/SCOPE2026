# Exact cutoff in the Wei–Guo complete-monotonicity conjecture

## Statement

Wei and Guo (2014) defined, for \(i\in\mathbb N_0\) and \(t>0\),
\[
\mathcal F_i(t)
=\frac{\operatorname{Li}_{-(i+1)}(e^{-t})}
        {\operatorname{Li}_{-i}(e^{-t})},
\]
and showed that \(\mathcal F_i\) is decreasing. Their second ratio satisfies
\(\mathcal G_i=\mathcal F_i\) for \(i\ge1\), while
\[
\mathcal G_0(t)=\frac1{e^t-1}.
\]
Conjecture 12 of their paper asks whether every \(\mathcal F_i\) and
\(\mathcal G_i\) is completely monotone on \((0,\infty)\).

The conjecture has the following exact index classification.

**Theorem.** For \(i\in\mathbb N_0\),
\[
\mathcal F_i \text{ is completely monotone}
\quad\Longleftrightarrow\quad i\le2.
\]
Likewise,
\[
\mathcal G_i \text{ is completely monotone}
\quad\Longleftrightarrow\quad i\le2.
\]
Consequently, Wei–Guo Conjecture 12 is true for \(i=0,1,2\) and false for
every \(i\ge3\).

For the first failing index \(i=3\), a pole obstruction already occurs at
\[
z=\log(2+\sqrt3)-i\pi,
\]
which lies in the open right half-plane.

## Eulerian-polynomial form

Put \(q=e^{-t}\). Let \(A_n(q)\) be the Eulerian polynomials in the
normalization
\[
\sum_{m\ge1}m^nq^m
=\operatorname{Li}_{-n}(q)
=\frac{qA_n(q)}{(1-q)^{n+1}},
\qquad |q|<1.
\]
Thus
\[
A_0=A_1=1,\qquad
A_2=1+q,\qquad
A_3=1+4q+q^2,
\]
and
\[
A_{n+1}(q)
=q(1-q)A_n'(q)+(1+nq)A_n(q).
\]
It follows that
\[
\mathcal F_i(t)
=\frac{A_{i+1}(q)}{(1-q)A_i(q)}.
\]

We use two elementary consequences of the recurrence.

**Lemma 1.** For \(n\ge2\), \(A_n\) is monic of degree \(n-1\), has
constant term \(1\), and has \(n-1\) distinct negative real zeros.

*Proof.* Monicity, degree, and constant term follow immediately by induction
from the recurrence. The zero statement can also be proved inductively from
the same recurrence. If
\[
r_1<\cdots<r_{n-1}<0
\]
are the simple zeros of \(A_n\), then
\[
A_{n+1}(r_j)=r_j(1-r_j)A_n'(r_j).
\]
These values alternate in sign. Since \(A_{n+1}(0)=1\), there is a zero in
\((r_{n-1},0)\), and the alternating signs give one zero in each
\((r_j,r_{j+1})\). Comparing the sign at \(r_1\) with the monic leading
term as \(q\to-\infty\) gives one more zero in \(( -\infty,r_1)\). These
\(n\) disjoint intervals contain all \(n\) zeros, so they are distinct and
negative. The base case \(A_2(q)=1+q\) is immediate. \(\square\)

**Lemma 2.** For every \(n\ge3\), \(A_n\) has a zero in \((-1,0)\).

*Proof.* Let \(r_1,\dots,r_{n-1}<0\) be its zeros. Since \(A_n\) is monic
with constant term \(1\),
\[
\prod_{j=1}^{n-1}|r_j|=1.
\]
If every \(|r_j|\ge1\), equality of the product would force
\(|r_j|=1\) for all \(j\). All roots would then equal \(-1\), contradicting
their distinctness because \(n-1\ge2\). \(\square\)

## Failure for every \(i\ge3\)

Fix \(i\ge3\), and choose a zero \(r\in(-1,0)\) of \(A_i\). The recurrence
gives
\[
A_{i+1}(r)
=r(1-r)A_i'(r)\ne0,
\]
because \(r\) is a simple zero. Hence the quotient
\[
R_i(z)=
\frac{A_{i+1}(e^{-z})}
     {(1-e^{-z})A_i(e^{-z})}
\]
has a genuine pole at
\[
z_0=-\log(-r)-i\pi,
\qquad \Re z_0=-\log(-r)>0.
\]
On the positive real axis, \(R_i(t)=\mathcal F_i(t)\).

A completely monotone function on \((0,\infty)\) is, by the
Hausdorff–Bernstein–Widder theorem, a Laplace transform
\[
f(t)=\int_{[0,\infty)}e^{-ts}\,d\mu(s)
\]
of a nonnegative measure. Such a transform extends holomorphically to the
entire half-plane \(\Re z>0\): on every smaller half-plane
\(\Re z\ge\sigma>0\), derivatives are dominated by a constant multiple of
\(e^{-\sigma s/2}\), whose \(\mu\)-integral is finite.

If \(\mathcal F_i\) were completely monotone, this Laplace-transform
extension and \(R_i\) would agree for positive real \(z\), hence by analytic
continuation on the punctured right half-plane. The genuine pole at \(z_0\)
would then have to be removable, a contradiction. Therefore
\(\mathcal F_i\) is not completely monotone for any \(i\ge3\).

For \(i=3\),
\[
A_3(q)=q^2+4q+1
\]
has the zero \(r=-2+\sqrt3\in(-1,0)\). Thus
\[
z_0=-\log(2-\sqrt3)-i\pi
=\log(2+\sqrt3)-i\pi
\]
is an explicit right-half-plane pole.

Since Wei and Guo show \(\mathcal G_i=\mathcal F_i\) for every \(i\ge1\),
the same obstruction proves failure of \(\mathcal G_i\) for all \(i\ge3\).

## The three positive cases

Writing again \(q=e^{-t}\),

\[
\mathcal F_0(t)=\frac1{1-q}
=\sum_{m\ge0}e^{-mt},
\]
and
\[
\mathcal G_0(t)=\frac{q}{1-q}
=\sum_{m\ge1}e^{-mt},
\]
so both are completely monotone.

For \(i=1\),
\[
\mathcal F_1(t)=\mathcal G_1(t)
=\frac{1+q}{1-q}
=1+2\sum_{m\ge1}e^{-mt},
\]
again a Laplace transform of a positive discrete measure.

For \(i=2\),
\[
\mathcal F_2(t)=\mathcal G_2(t)
=\frac{1+4q+q^2}{1-q^2}
=1+4\sum_{m\ge0}e^{-(2m+1)t}
 +2\sum_{m\ge1}e^{-2mt}.
\]
This is also a Laplace transform of a positive discrete measure. Hence the
classification is complete.

## Context and originality

Wei and Guo explicitly posed the all-\(i\) complete-monotonicity assertion
as Conjecture 12 after proving only monotonic decrease of the ratios and the
lowest examples. The source paper was inspected in full.

The literature check covered the exact paper title and DOI, the conjecture
number, the ratios
\(\operatorname{Li}_{-(i+1)}(e^{-t})/\operatorname{Li}_{-i}(e^{-t})\),
equivalent Eulerian-polynomial quotients, and combinations of these terms
with complete monotonicity, Laplace transforms, poles, and Eulerian zeros.
Later literature on complete monotonicity and on Eulerian real-rootedness
was also checked. No source located through the publication date gave this
cutoff \(i\le2\), a counterexample for \(i=3\), or the all-\(i\ge3\)
right-half-plane pole obstruction.

Accordingly, the originality claim is **to the best of our knowledge**.
A differently phrased, unpublished, or poorly indexed prior resolution may
exist.

## Limitations

This result classifies complete monotonicity for the two ratio families in
Conjecture 12, but does not address stronger properties such as logarithmic
complete monotonicity where they might make sense. The obstruction is
qualitative: for \(i\ge3\) it proves that some complete-monotonicity
inequality must fail, but it does not identify the first derivative order or
the first positive real \(t\) at which a sign violation occurs. No independent
audit has yet been performed.

## References

1. C.-F. Wei and B.-N. Guo, *Complete Monotonicity of Functions Connected
   with the Exponential Function and Derivatives*, Abstract and Applied
   Analysis **2014** (2014), Article ID 851213.
   https://doi.org/10.1155/2014/851213

2. C. A. Athanasiadis, *On the real-rootedness of the Eulerian
   transformation*, Journal of the London Mathematical Society **111**
   (2025), e70083.
   https://doi.org/10.1112/jlms.70083

3. P. Hitczenko and S. Janson, *Weighted Random Staircase Tableaux*,
   Combinatorics, Probability and Computing **23** (2014), 1114–1147.
   https://doi.org/10.1017/S0963548314000327
