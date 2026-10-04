# Sharp length threshold for modular freedom under three-wise-independent fair bits

## Finding

Let \(q\ge4\) be an integer. Among all lengths \(n\), the least one for which
three-wise-independent fair bits can realize **every** probability law for their
Hamming weight modulo \(q\) is
\[
\boxed{n=q^2+2}.
\]

More precisely, let \(X_1,\ldots,X_n\) be Bernoulli variables with
\[
\Pr(X_i=1)=\frac12
\]
and assume every three distinct coordinates are mutually independent. Write
\[
K=\sum_{i=1}^nX_i.
\]
At
\[
n=q^2+2,
\]
for every residue \(r\in\{0,\ldots,q-1\}\) there is such a vector satisfying
\[
K\equiv r\pmod q
\quad\text{almost surely}.
\]
Consequently, by mixing these residue-vertex laws, every probability vector
\[
(\pi_0,\ldots,\pi_{q-1})
\]
is attainable as
\[
\pi_r=\Pr(K\equiv r\pmod q).
\]

The threshold is sharp. No length
\[
n\le q^2+1
\]
has this full-simplex property.

At the sharp length, each residue vertex can be realized by an exchangeable
law whose Hamming-weight distribution has at most five support points.

## Assumptions and scope

The coordinates are fair Bernoulli variables and are required to be
three-wise independent. No assumption of mutual independence is made.

The quantity minimized is the number \(n\) of Bernoulli coordinates, not the
cardinality of a finite sample space supporting their joint law. The result is
therefore different from minimum-row questions for orthogonal arrays.

The statement is for \(q\ge4\). Small moduli have separate low-dimensional
behavior and are not included in the theorem.

## Proof

Three-wise independence and fairness force the first three factorial moments
of \(K\):
\[
\mathbb E K=\frac n2,
\qquad
\mathbb E[K(K-1)]=\frac{n(n-1)}4,
\qquad
\mathbb E[K(K-1)(K-2)]=\frac{n(n-1)(n-2)}8.
\]
Equivalently,
\[
\mathbb E K=\frac n2,
\qquad
\operatorname{Var}(K)=\frac n4,
\qquad
\mathbb E\left(K-\frac n2\right)^3=0.
\tag{1}
\]

Conversely, suppose a random variable \(K\) on
\(\{0,\ldots,n\}\) satisfies these three factorial-moment identities.
Conditional on \(K=k\), choose uniformly among all \(k\)-subsets of
\(\{1,\ldots,n\}\) and put ones on that subset. Then, for
\(j=1,2,3\),
\[
\Pr(X_{i_1}=\cdots=X_{i_j}=1)
=
\frac{\mathbb E[(K)_j]}{(n)_j}
=
2^{-j}.
\]
Inclusion-exclusion gives all \(2^j\) patterns with probability \(2^{-j}\),
so the resulting Bernoulli vector is three-wise independent and fair.

Fix a residue \(r\), impose
\[
K\equiv r\pmod q,
\]
and write
\[
K=r+qJ.
\]
Then \(J\) is integer-valued on
\[
\{0,\ldots,N\},
\qquad
N=\left\lfloor\frac{n-r}{q}\right\rfloor,
\]
and (1) becomes
\[
\mathbb E J=m,
\qquad
\operatorname{Var}(J)=v,
\qquad
\mathbb E(J-m)^3=0,
\tag{2}
\]
where
\[
m=\frac{n-2r}{2q},
\qquad
v=\frac{n}{4q^2}.
\]

Write
\[
a=\lfloor m\rfloor,
\qquad
\delta=m-a.
\]
A useful lattice lemma gives the smallest variance compatible with the mean
and zero third centered moment.

If \(0<\delta<1/2\), then for every integer \(J\in[0,N]\),
\[
J(J-a)(J-a-1)\ge0.
\]
Taking expectations and using (2) yields
\[
\operatorname{Var}(J)\ge
v_{\min}
=
\frac{\delta(1-\delta)m}
     {m-(1-2\delta)}.
\tag{3}
\]
Equality is attained on \(\{0,a,a+1\}\).  Indeed, with
\[
D=a+3\delta-1,
\]
the masses
\[
p_0=
\frac{\delta(1-\delta)(1-2\delta)}
     {a(a+1)D},
\]
\[
p_a=
\frac{(a+\delta)(1-\delta)(a+2\delta-1)}
     {aD},
\]
and
\[
p_{a+1}=
\frac{\delta(a+\delta)(a+2\delta)}
     {(a+1)D}
\]
are nonnegative, sum to one, have mean \(m\), attain (3), and have zero third
centered moment.

If \(\delta>1/2\), apply the same argument to \(N-J\). Thus, with
\[
x=N-m,
\]
\[
v_{\min}
=
\frac{\delta(1-\delta)x}
     {x-(2\delta-1)}.
\tag{4}
\]
For \(\delta=0\), one has \(v_{\min}=0\); for
\(\delta=1/2\), one has \(v_{\min}=1/4\).

Now set
\[
n=q^2+2,
\qquad
v=\frac14+\frac{1}{2q^2}.
\tag{5}
\]
For every residue, elementary bounds give \(a\ge1\) and \(a+2\le N\).

The low-variance law just constructed satisfies
\[
v_{\min}\le v.
\tag{6}
\]
Here is a compact verification of (6). Put
\[
\varepsilon=\left|\delta-\frac12\right|
\]
and let \(x=m\) in the left-skew case and \(x=N-m\) in the
right-skew case. Whenever \(\varepsilon>0\), formulas (3)-(4) give
\[
v_{\min}-\frac14
=
\frac{\varepsilon(1/2-\varepsilon x)}
     {x-2\varepsilon}.
\tag{7}
\]
For odd \(q\), the possible fractional parts at (5) are the odd
\((2q)^{-1}\)-grid, so nonzero \(\varepsilon\) is an integer multiple of
\(1/q\). If the right side of (7) is positive, its largest relevant case is
\(\varepsilon=1/q\), where \(x=q/2-1/q\) and
\[
v_{\min}-\frac14
=
\frac{2}{q^2(q^2-6)}
\le
\frac{1}{2q^2}
\qquad(q\ge5).
\]
For even \(q\ge6\), the same argument leaves only
\(\varepsilon=1/q\), now with
\[
x=\frac q2-\frac12-\frac1q,
\]
and
\[
v_{\min}-\frac14
=
\frac{1}{q^2(q-3)}
\le
\frac{1}{2q^2}.
\]
For \(q=4\), direct substitution gives the only nontrivial low variance
\[
v_{\min}=\frac{27}{112}<\frac9{32}=v,
\]
while the other cases have \(v_{\min}=0\) or \(1/4\).
This proves (6).

We also need a same-mean, zero-skew law with variance above \(v\). Let
\(A\) be the two-point law on \(\{a-1,a+1\}\) with mean \(m\), and let
\(B\) be the two-point law on \(\{a,a+2\}\) with mean \(m\).
Explicitly,
\[
A(a-1)=\frac{1-\delta}{2},
\qquad
A(a+1)=\frac{1+\delta}{2},
\]
and
\[
B(a)=\frac{2-\delta}{2},
\qquad
B(a+2)=\frac{\delta}{2}.
\]
Their third centered moments have opposite signs. The mixture
\[
H=\frac{2-\delta}{3}A+\frac{1+\delta}{3}B
\]
has zero third centered moment and variance
\[
v_H=
\frac{(2-\delta)(1+\delta)}3
\ge\frac23.
\tag{8}
\]
For \(q\ge4\), (5) gives \(v\le9/32<2/3\). By (6)-(8), a convex mixture
of the low law and \(H\) has exactly variance \(v\), while retaining mean
\(m\) and zero third centered moment. Its support contains at most five
integers. Mapping back by \(K=r+qJ\) proves that every residue vertex is
attainable at \(n=q^2+2\).

Because every residue-vertex construction has the same factorial moments,
arbitrary convex mixtures preserve three-wise independence and produce every
law on \(K\bmod q\).

It remains to prove minimality.

First suppose
\[
n\le q^2-2.
\]
As \(r\) ranges over the residues, the fractional part of
\[
m=\frac{n-2r}{2q}
\]
comes within \(1/(2q)\) of \(1/2\). Every integer-valued random variable with
mean \(m\) has
\[
\operatorname{Var}(J)\ge\delta(1-\delta)
\ge
\frac14-\frac{1}{4q^2}
=
\frac{q^2-1}{4q^2}
>
\frac{n}{4q^2}.
\]
Thus at least one residue is already impossible from the second moment.

Three lengths remain:
\[
q^2-1,\qquad q^2,\qquad q^2+1.
\]
At these lengths the second moment alone can cease to obstruct all residues,
but the zero-third-moment condition still does.

For odd \(q\ge5\), use respectively
\[
r=0,\qquad r=1,\qquad r=0.
\]
For even \(q\ge4\), use respectively
\[
r=\frac q2-1,\qquad r=\frac q2-1,\qquad r=\frac q2.
\]
At the first two lengths, formulas (3)-(4) give
\(v_{\min}>1/4\), whereas the required variance is at most \(1/4\).

At \(n=q^2+1\), the required excess over \(1/4\) is
\[
\frac{1}{4q^2}.
\]
For odd \(q\),
\[
v_{\min}-\frac14
=
\frac{q^2+1}{4q^2(q^2-3)}
>
\frac{1}{4q^2},
\]
and for even \(q\),
\[
v_{\min}-\frac14
=
\frac{q^2+q+1}{4q^2(q^2-q-3)}
>
\frac{1}{4q^2}.
\]
So a residue vertex is impossible at each of these three lengths as well.
Hence no \(n\le q^2+1\) has full modular freedom, completing the proof.

## Verification

A standalone exact-rational checker accompanies the result. It constructs the
low-variance and high-variance laws using rational arithmetic, mixes them to
the target variance, maps them back to Hamming weights, and checks the first
three factorial moments exactly.

It also replays the second-moment obstruction below the pairwise threshold and
the explicit third-moment obstructions at the three boundary lengths.

The computation is supplementary; the universal theorem follows from the
lattice inequalities and constructions in the proof.

## Relationship to prior work

Benjamini, Gurel-Gurevich, and Peled developed a systematic framework for
Boolean functions under limited independence and explicitly connected
\(k\)-wise independence to classical moment problems. Their work studies
functions including majority, AND, tribes, and percolation, but the inspected
text does not state a Hamming-weight congruence simplex or the sharp minimum
length \(q^2+2\).

Di Cecco gives sharp upper and lower tail probabilities for a discrete random
variable on \(\{0,\ldots,n\}\) when its first three moments are fixed, and
records the equivalence with exchangeable Bernoulli count models. That result
optimizes threshold events \(K\ge k\); it does not determine whether all mass
can be confined to one arithmetic progression, nor the minimum Bernoulli
length at which every residue class is feasible.

Orthogonal-array theory gives an equivalent language for finite-support
three-wise-independent binary models. Work on minimum-row binary orthogonal
arrays of strength three addresses the sample-space cardinality of an array,
rather than the minimum number of Bernoulli coordinates needed to make the
Hamming-weight residue law arbitrary.

Targeted searches using limited-independence, orthogonal-array,
Hamming-weight, congruence, residue-support, and modular-sum terminology did
not locate the threshold or an equivalent statement.

## Limitations

The theorem concerns three-wise independence with exactly fair Bernoulli
marginals. Biased marginals change all three target moments.

The theorem minimizes coordinate length, not support size of the joint law.
It does not give the smallest finite sample space for the residue-vertex
constructions.

The small moduli \(q=2\) and \(q=3\) are excluded from the stated theorem.

The originality search was targeted rather than exhaustive. In particular,
older coding-theoretic or design-theoretic literature could encode an
equivalent Hamming-weight congruence statement under terminology not captured
by the searches.

## References

1. I. Benjamini, O. Gurel-Gurevich, and R. Peled, “On K-wise Independent
   Distributions and Boolean Functions,” arXiv:1201.3261, first submitted
   2012-01-16.
2. D. Di Cecco, “Upper and lower bounds for the reliability measure of a
   discrete distribution conditionally on the first three moments,”
   arXiv:1201.6387, first submitted 2012-01-30.
3. C. Carlet, R. Kiss, and G. P. Nagy, “Simplicity conditions for binary
   orthogonal arrays,” arXiv:2204.00835, version inspected 2022-09-09.
