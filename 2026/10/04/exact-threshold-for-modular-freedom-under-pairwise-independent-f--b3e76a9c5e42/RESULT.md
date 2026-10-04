# Exact threshold for modular freedom under pairwise-independent fair bits

## Finding

Let \(q\ge2\) and \(n\ge2\), and let \(X_1,\ldots,X_n\) be Bernoulli variables
with
\[
\Pr(X_i=1)=\frac12
\]
for every \(i\). Write
\[
K=\sum_{i=1}^nX_i.
\]

For a residue \(r\in\{0,\ldots,q-1\}\), define
\[
N=\left\lfloor\frac{n-r}{q}\right\rfloor,\qquad
m=\frac{n-2r}{2q},\qquad
v=\frac{n}{4q^2},
\]
and
\[
\delta=m-\lfloor m\rfloor.
\]

There exists a pairwise-independent fair Bernoulli vector for which
\[
K\equiv r\pmod q
\quad\text{almost surely}
\]
if and only if
\[
0\le m\le N
\]
and
\[
\boxed{
\delta(1-\delta)\le v\le m(N-m).
}
\]

This single-residue criterion has a sharp global consequence. Let
\[
\Pi_{n,q}
=
\left\{
\bigl(\Pr(K\equiv0\!\!\!\pmod q),\ldots,
\Pr(K\equiv q-1\!\!\!\pmod q)\bigr)
\right\},
\]
where the set ranges over all pairwise-independent fair Bernoulli vectors of
length \(n\). Then
\[
\Pi_{n,q}
\]
equals the entire probability simplex on \(q\) points for every
\[
n\ge q^2-1.
\]
Moreover \(q^2-1\) is the exact eventual threshold: when
\[
n=q^2-2,
\]
at least one simplex vertex is impossible. Thus the least integer
\(n_0(q)\) such that full modular freedom holds for every \(n\ge n_0(q)\) is
\[
\boxed{n_0(q)=q^2-1.}
\]

For odd \(q\), a forbidden residue at \(n=q^2-2\) is \(r=q-1\). For even
\(q\), one is
\[
r=\frac q2-1.
\]

## Assumptions and scope

The Bernoulli variables are required to be pairwise independent, not mutually
independent. Their common marginal is exactly \(1/2\). The modulus \(q\) is an
arbitrary integer at least \(2\).

The theorem determines when a single residue class can contain the Hamming
weight almost surely, and from that gives an exact threshold for realizing an
arbitrary probability law on the residue of the Hamming weight.

The theorem does not classify the smallest support size of the joint
distribution, nor does it address \(k\)-wise independence for \(k\ge3\), biased
marginals, or nonbinary coordinates.

## Proof

Pairwise independence and fairness force
\[
\mathbb E K=\frac n2
\]
and
\[
\operatorname{Var}(K)=\frac n4.
\]
Equivalently,
\[
\mathbb E[K(K-1)]=\frac{n(n-1)}4.
\]

Assume first that
\[
K\equiv r\pmod q
\]
almost surely. Then
\[
J=\frac{K-r}{q}
\]
is integer-valued and supported on
\[
\{0,1,\ldots,N\},
\qquad
N=\left\lfloor\frac{n-r}{q}\right\rfloor.
\]
Its mean and variance are
\[
\mathbb E J
=
\frac{\mathbb E K-r}{q}
=
\frac{n-2r}{2q}
=
m
\]
and
\[
\operatorname{Var}(J)
=
\frac{\operatorname{Var}(K)}{q^2}
=
\frac{n}{4q^2}
=
v.
\]

Let
\[
a=\lfloor m\rfloor,
\qquad
\delta=m-a.
\]
For every integer \(j\),
\[
(j-a)(j-a-1)\ge0.
\]
Taking expectations gives
\[
v-\delta(1-\delta)\ge0,
\]
hence
\[
v\ge\delta(1-\delta).
\]
Also, for \(0\le J\le N\),
\[
J(N-J)\ge0.
\]
Therefore
\[
Nm-\mathbb E J^2\ge0,
\]
which is exactly
\[
v\le m(N-m).
\]
The support condition itself also forces
\[
0\le m\le N.
\]
This proves necessity.

For sufficiency, suppose the displayed inequalities hold. There are two
canonical distributions on \(\{0,\ldots,N\}\) with mean \(m\).

The first is the nearest-lattice distribution:
\[
L=
\begin{cases}
a,&\text{with probability }1-\delta,\\
a+1,&\text{with probability }\delta.
\end{cases}
\]
It has variance
\[
v_{\min}=\delta(1-\delta).
\]

The second is the endpoint distribution:
\[
H=
\begin{cases}
0,&\text{with probability }1-m/N,\\
N,&\text{with probability }m/N,
\end{cases}
\]
when \(N>0\). It has variance
\[
v_{\max}=m(N-m).
\]
Degenerate endpoint cases are interpreted in the evident limiting way.

Because both laws have mean \(m\), any convex mixture of them also has mean
\(m\), while its variance is the corresponding convex mixture of
\(v_{\min}\) and \(v_{\max}\). Hence every variance in the interval
\[
[v_{\min},v_{\max}]
\]
is attained by an integer-valued \(J\) supported on
\(\{0,\ldots,N\}\). In particular there is such a \(J\) with variance \(v\).

Now put
\[
K=r+qJ.
\]
Then
\[
0\le K\le n,
\qquad
K\equiv r\pmod q,
\]
and \(K\) has the required first two moments.

Construct a Bernoulli vector conditionally on \(K=k\) by choosing uniformly
among all \(k\)-subsets of \(\{1,\ldots,n\}\) and placing ones on that subset.
This exchangeable construction satisfies
\[
\Pr(X_i=1)
=
\frac{\mathbb E K}{n}
=
\frac12
\]
and, for \(i\ne j\),
\[
\Pr(X_i=X_j=1)
=
\frac{\mathbb E[K(K-1)]}{n(n-1)}
=
\frac14.
\]
Thus every pair is independent. This proves the single-residue criterion.

If each residue \(r\) has one such joint law \(Q_r\), then every mixture
\[
\sum_{r=0}^{q-1}\pi_rQ_r
\]
has the same one- and two-coordinate marginals, hence remains pairwise
independent and fair. Its residue law is exactly
\[
(\pi_0,\ldots,\pi_{q-1}).
\]
Therefore all residue distributions are attainable if and only if every
simplex vertex is attainable.

It remains to determine the eventual threshold.

Assume
\[
n\ge q^2-1.
\]
For any \(r\), put
\[
s\equiv n-r\pmod q,
\qquad
0\le s\le q-1.
\]
Then
\[
N-m=\frac{n-2s}{2q}.
\]
Since
\[
n\ge q^2-1\ge2q-2,
\]
one has \(m\ge0\), and also \(m\le N\) because
\[
\frac n2\ge q-1\ge s.
\]

For the lower variance bound, if \(n\ge q^2\), then
\[
v=\frac{n}{4q^2}\ge\frac14
\]
and
\[
\delta(1-\delta)\le\frac14.
\]
At the single boundary value \(n=q^2-1\), the fractional part of \(m\) cannot
equal \(1/2\): that would require
\[
q^2-1-2r\equiv q\pmod{2q},
\]
but the left-hand difference
\[
q^2-q-1
\]
is odd whereas \(2r\) is even. Since \(m\) lies on the
\((2q)^{-1}\)-lattice, its fractional part is then at least
\[
\frac1{2q}
\]
away from \(1/2\). Therefore
\[
\delta(1-\delta)
\le
\frac14-\frac1{4q^2}
=
\frac{q^2-1}{4q^2}
=
v.
\]

For the upper variance bound,
\[
m(N-m)
=
\frac{(n-2r)(n-2s)}{4q^2}.
\]
For \(q\ge3\),
\[
(n-2r)(n-2s)
\ge
(n-2q+2)^2.
\]
The function
\[
(n-2q+2)^2-n
\]
is increasing for
\[
n\ge q^2-1,
\]
and at \(n=q^2-1\) it equals
\[
(q-1)^4-(q^2-1)>0.
\]
Hence
\[
m(N-m)\ge\frac{n}{4q^2}=v.
\]
For \(q=2\), the same inequality is checked directly for the two residues and
all \(n\ge3\). Thus every residue is attainable whenever
\[
n\ge q^2-1.
\]

Finally let
\[
n=q^2-2.
\]
If \(q\) is odd, choose
\[
r=q-1.
\]
If \(q\) is even, choose
\[
r=\frac q2-1.
\]
In both cases
\[
m\equiv\frac12\pmod1,
\]
so the minimum possible variance of an integer-valued \(J\) with mean \(m\)
is
\[
\frac14.
\]
But the required variance is
\[
v
=
\frac{q^2-2}{4q^2}
<
\frac14.
\]
That residue is therefore impossible. This proves that
\[
q^2-1
\]
is the exact eventual threshold.

## Verification

A standalone exact-rational checker accompanies this result. It evaluates the
criterion, constructs the two mean-matched extremal laws for \(J\), mixes them
to the required variance, converts back to \(K\), and verifies exactly that
\[
\mathbb E K=\frac n2,
\qquad
\mathbb E[K(K-1)]=\frac{n(n-1)}4.
\]
It also checks the sharp threshold and the explicit forbidden residue at
\(n=q^2-2\) over a broad finite range of moduli.

The checker is supplementary. The theorem for all \(q\) and \(n\) follows
from the inequalities in the proof, not from finite enumeration.

## Relationship to prior work

Benjamini, Gurel-Gurevich, and Peled study how Boolean functions can behave
under limited independence. Their 2012 paper explicitly formulates extremal
questions over \(k\)-wise independent inputs, uses classical moment-problem
methods, and notes that integer support creates additional sharpness issues.
Their examples include XOR at the binary level, but the inspected paper does
not state the modular-simplex criterion above or the threshold \(q^2-1\).

Ramachandra and Natarajan study tight probability bounds for sums of
pairwise-independent Bernoulli variables through linear optimization and fixed
first and second moments. Their inspected full preprint treats tail and union
events, not the distribution of the Hamming weight modulo an arbitrary
integer, and it does not state the present residue-feasibility interval or the
complete modular-freedom threshold.

The closest published repository results found in the targeted semantic search
concern pairwise-independent occupancy statistics and rare-sum weak limits.
Those results use related moment reductions, but neither one determines exact
finite-\(n\) congruence-class support for fair Bernoulli sums.

## Limitations

The exact threshold concerns pairwise independence and fair Bernoulli
marginals. For biased marginals, the target mean and variance change and the
same two-moment reduction gives a different feasibility region; no universal
closed threshold is asserted here.

For \(k\)-wise independence with \(k\ge3\), additional factorial moments are
fixed, so the two-moment interpolation used here is insufficient.

The originality assessment is based on targeted searches of limited-
independence, orthogonal-array, modular-Hamming-weight, and moment-problem
literature plus inspection of the closest full texts. A congruence-support
formulation equivalent to this theorem could exist under coding-theoretic
terminology not captured by those searches.

## References

1. I. Benjamini, O. Gurel-Gurevich, and R. Peled, “On K-wise Independent
   Distributions and Boolean Functions,” arXiv:1201.3261, first submitted
   2012-01-16.
2. A. Ramachandra and K. Natarajan, “Tight Probability Bounds with Pairwise
   Independence,” arXiv:2006.00516, first submitted 2020-05-31; later
   published in *SIAM Journal on Discrete Mathematics* 37 (2023), 516–555.
3. N. I. Akhiezer, *The Classical Moment Problem and Some Related Questions in
   Analysis*, Hafner, 1965.
