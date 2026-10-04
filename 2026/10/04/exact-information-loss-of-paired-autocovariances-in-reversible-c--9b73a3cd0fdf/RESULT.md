# Exact information loss of paired autocovariances in reversible chains

## Finding

Let \((X_t)_{t\ge0}\) be a stationary reversible Markov chain with invariant law
\(\pi\), and let \(g\in L^2(\pi)\) be centered and nonconstant. Normalize its
autocorrelation sequence by
\[
r_k=
\frac{\operatorname{Cov}_\pi(g(X_0),g(X_k))}
{\operatorname{Var}_\pi(g)},
\qquad
r_0=1.
\]
Define the paired autocovariances
\[
\Gamma_k=r_{2k}+r_{2k+1},
\qquad k\ge0.
\]

Reversibility gives a unique spectral probability measure \(\nu\) on
\([-1,1]\) such that
\[
r_k=\int_{-1}^1\lambda^k\,\nu(d\lambda).
\]
The complete paired sequence has the moment representation
\[
\boxed{
\Gamma_k=\int_0^1 x^k\,G(dx),
}
\tag{1}
\]
where the representing measure \(G\) is exactly
\[
\boxed{
G(B)=
\int_{\{\lambda:\lambda^2\in B\}}
(1+\lambda)\,\nu(d\lambda)
}
\tag{2}
\]
for Borel \(B\subseteq[0,1]\). By the Hausdorff moment theorem, the infinite
sequence \((\Gamma_k)_{k\ge0}\) determines \(G\) uniquely.

The loss of information from \(\nu\) to \(G\) can be classified completely.
For a measurable function
\[
\eta:[0,1)\to[0,1],
\]
put
\[
T(\eta)=
\frac{G(\{1\})}{2}
+
\int_{[0,1)}
\left[
\frac{\eta(x)}{1+\sqrt{x}}
+
\frac{1-\eta(x)}{1-\sqrt{x}}
\right]G(dx).
\tag{3}
\]
Whenever
\[
T(\eta)\le1,
\]
define a probability measure on \([-1,1]\) by assigning, for \(x<1\),
\[
\frac{\eta(x)}{1+\sqrt{x}}\,G(dx)
\]
to the point \(+\sqrt{x}\) and
\[
\frac{1-\eta(x)}{1-\sqrt{x}}\,G(dx)
\]
to the point \(-\sqrt{x}\), then assigning
\[
\frac{G(\{1\})}{2}
\]
to \(+1\), and the residual mass
\[
1-T(\eta)
\]
to \(-1\).

Every such measure produces the same paired sequence (1), and conversely every
spectral probability measure producing \(G\) is obtained in this way.

Consequently, a finite measure \(G\) on \([0,1]\) is compatible at the
spectral-moment level with a normalized reversible autocorrelation sequence if
and only if
\[
\boxed{
J(G):=
\int_0^1\frac{G(dx)}{1+\sqrt{x}}
\le1.
}
\tag{4}
\]

The compatible spectral measure is unique if and only if
\[
\boxed{
J(G)=1
\quad\text{or}\quad
G((0,1))=0.
}
\tag{5}
\]
Thus paired autocovariances lose information precisely when there is both
positive slack in (4) and spectral mass at a nontrivial squared eigenvalue.

This is not only an abstract spectral ambiguity. Consider
\[
G=
\frac12\delta_{1/4}
+
\frac12\delta_{1/9}.
\]
Two distinct spectral probability measures in the fiber are
\[
\nu_A=
\frac13\delta_{1/2}
+
\frac1{12}\delta_{1/3}
+
\frac7{12}\delta_{-1/3}
\tag{6}
\]
and
\[
\nu_B=
\frac3{16}\delta_{1/2}
+
\frac7{16}\delta_{-1/2}
+
\frac38\delta_{1/3}.
\tag{7}
\]
They satisfy
\[
r_1^{(A)}=r_1^{(B)}=0
\]
but
\[
r_2^{(A)}=\frac{17}{108},
\qquad
r_2^{(B)}=\frac{19}{96},
\]
and
\[
r_3^{(A)}=\frac5{216},
\qquad
r_3^{(B)}=-\frac5{288}.
\]
Nevertheless, for every \(k\ge0\),
\[
\boxed{
\Gamma_k^{(A)}
=
\Gamma_k^{(B)}
=
\frac12\left(\frac14\right)^k
+
\frac12\left(\frac19\right)^k.
}
\tag{8}
\]

Both measures are realized by finite-state irreducible aperiodic reversible
chains. Their complete paired sequences, and therefore their normalized
asymptotic variance,
\[
-1+2\sum_{k\ge0}\Gamma_k
=
\frac{35}{24},
\]
are identical. Their finite-horizon behavior is not: the normalized variance
of the three-step sample mean is
\[
\frac{179}{486}
\]
for (6) and
\[
\frac{163}{432}
\]
for (7).

## Assumptions and scope

The chain is stationary and reversible. No positivity assumption is imposed
on its Markov operator, so negative eigenvalues are allowed.

The main classification concerns the spectral measures associated with one
fixed centered observable. For arbitrary non-finitely-supported \(G\), the
fiber formula classifies all probability measures on \([-1,1]\) compatible
with the paired moments. The theorem does not claim that every such abstract
measure is realized by a finite-state chain.

For finitely supported measures, however, every fiber point is realizable by
a finite product of symmetric two-state reversible chains. The explicit
counterexample uses only eigenvalues strictly between \(-1\) and \(1\), so
its realizing chains are irreducible and aperiodic.

## Proof

By reversibility, the centered Markov operator is self-adjoint, so the
spectral theorem gives a probability measure \(\nu\) on \([-1,1]\) with
\[
r_k=\int\lambda^k\,\nu(d\lambda).
\]
Therefore
\[
\begin{aligned}
\Gamma_k
&=
r_{2k}+r_{2k+1}\\
&=
\int\lambda^{2k}(1+\lambda)\,\nu(d\lambda).
\end{aligned}
\]
Pushing the weighted measure \((1+\lambda)\nu(d\lambda)\) forward under
\[
\lambda\mapsto\lambda^2
\]
gives (1)--(2). Since \(G\) is supported on \([0,1]\), its complete moment
sequence determines it uniquely.

We now invert (2). On \(x\in[0,1)\), write \(s=\sqrt{x}\). Let
\(\alpha\) be the positive-branch pushforward of \(\nu\), and let \(\beta\)
be the negative-branch pushforward. Then
\[
G(dx)=(1+s)\alpha(dx)+(1-s)\beta(dx).
\tag{9}
\]
Both summands are dominated by \(G\). Hence there is a measurable
\(\eta\in[0,1]\) such that
\[
(1+s)\alpha(dx)=\eta(x)G(dx),
\]
and therefore
\[
(1-s)\beta(dx)=(1-\eta(x))G(dx).
\]
This gives the two branch masses in (3).

At \(x=1\), only the \(+1\) spectral atom contributes to \(G\), with multiplier
\(2\), so
\[
\nu(\{1\})=\frac{G(\{1\})}{2}.
\]
The \(-1\) atom is invisible to (2). Normalization therefore forces it to have
mass \(1-T(\eta)\). This proves that every compatible \(\nu\) has the stated
form. Direct substitution into (2) proves the converse.

The quantity \(T(\eta)\) is minimized by choosing
\[
\eta(x)=1
\]
for every \(x\in(0,1)\), because
\[
\frac1{1+\sqrt{x}}
<
\frac1{1-\sqrt{x}}.
\]
The minimum is precisely
\[
J(G)=
\int_0^1\frac{G(dx)}{1+\sqrt{x}}.
\]
Thus a probability measure in the fiber exists exactly when \(J(G)\le1\),
proving (4).

For uniqueness, observe that
\[
T(\eta)-J(G)
=
\int_{(0,1)}
(1-\eta(x))
\left[
\frac1{1-\sqrt{x}}
-
\frac1{1+\sqrt{x}}
\right]G(dx).
\tag{10}
\]
If \(J(G)=1\), feasibility forces the integral in (10) to vanish, so the
positive branch is forced at every nontrivial squared eigenvalue; variation at
\(x=0\) has no effect because the two branches coincide there. Hence the
spectral measure is unique.

If \(G((0,1))=0\), the only possible spectral locations are \(0,+1,-1\), and
their masses are fixed by \(G\) and normalization, so uniqueness again holds.

Conversely, suppose
\[
J(G)<1
\quad\text{and}\quad
G((0,1))>0.
\]
There is then a set of positive \(G\)-mass bounded away from \(1\). Starting
from \(\eta=1\), decrease \(\eta\) by a sufficiently small positive amount on
that set. The increase in \(T(\eta)\) is finite and can be kept below the
positive slack \(1-J(G)\). This gives a distinct feasible spectral measure,
so uniqueness fails. This proves (5).

For finite-state realizability, for each \(\lambda\in(-1,1)\) use the
symmetric two-state kernel
\[
P_\lambda=
\frac12
\begin{pmatrix}
1+\lambda&1-\lambda\\
1-\lambda&1+\lambda
\end{pmatrix}.
\]
It is irreducible, aperiodic, reversible with respect to the uniform law, and
its centered sign coordinate has eigenvalue \(\lambda\). A product of these
kernels has orthogonal coordinate eigenfunctions. If the observable is a
linear combination of those coordinates with squared coefficients equal to
the desired spectral weights, its normalized spectral measure is exactly the
prescribed finite measure.

Applying this construction to (6) and (7) gives two eight-state irreducible
aperiodic reversible chains. The displayed moments and (8) follow by direct
substitution. Finally,
\[
-1+2\sum_{k\ge0}\Gamma_k
=
-1+
2\left(
\frac{1/2}{1-1/4}
+
\frac{1/2}{1-1/9}
\right)
=
\frac{35}{24}.
\]
For a three-step stationary average,
\[
\frac{\operatorname{Var}(3^{-1}\sum_{t=0}^2g(X_t))}
{\operatorname{Var}_\pi(g)}
=
\frac{3+4r_1+2r_2}{9},
\]
which gives the two distinct values stated above.

## Verification

The accompanying exact-rational checker reconstructs \(G\) from thousands of
random finitely supported spectral measures and then reconstructs the original
measure through the fiber formula. It checks (4), normalization, and equality
of every tested paired moment.

It separately verifies the two explicit spectral measures (6)--(7), their
different individual autocorrelations, their identical paired sequence,
their identical normalized asymptotic variance, and their different
three-step sample-mean variances.

The finite-state realization is checked algebraically from
\[
P_\lambda(1,-1)^\mathsf{T}
=
\lambda(1,-1)^\mathsf{T}.
\]
The checker is supplementary; the fiber theorem is proved analytically above.

## Relationship to prior work

Geyer introduced the paired sequence
\[
\Gamma_k=\gamma_{2k}+\gamma_{2k+1}
\]
for reversible-chain variance estimation and proved positivity, monotonicity,
and convexity properties used by initial-sequence estimators.

Berg and Song later proved that the full reversible autocovariance sequence is
a moment sequence on \([-1,1]\), while the paired sequence is a Hausdorff
moment sequence on \([0,1]\). They explicitly note that the paired sequence,
although completely monotone, is not entirely satisfactory for estimating the
entire autocovariance sequence. Their full-text proposition establishes the
forward representations but does not give an inverse fiber, an identifiability
criterion, or a finite-state exact aliasing construction.

A published related result gives sharp two-lag variance envelopes after
assuming the Markov operator is positive, which restricts the relevant
spectrum to \([0,1]\). In that positive-spectrum regime, the map in (2) is
one-to-one and the information-loss phenomenon disappears. Its stated
negative-spectrum limitation therefore does not cover the present
classification.

The Hausdorff moment theorem supplies uniqueness of \(G\) from its complete
moment sequence; that classical result is used as an ingredient and is not
claimed as new. The finding here is the exact inverse fiber of the
reversible-chain pairing map, its uniqueness criterion, and the explicit
geometrically ergodic finite-state aliasing example.

Targeted searches using paired autocovariance, initial-sequence,
identifiability, negative spectrum, spectral aliasing, and Geyer-sequence
terminology did not locate an equivalent fiber theorem.

## Limitations

The complete inverse classification is at the level of representing spectral
measures. Finite support guarantees finite-state Markov realizability by the
product construction; no claim is made here that every continuous fiber
measure has a finite-state realization.

The paired sequence still identifies the normalized asymptotic variance when
the relevant series converges. The theorem concerns information lost about
the individual autocovariances and finite-horizon behavior, not a failure of
the classical initial-sequence variance identity.

The 1992 archive source was verified bibliographically and through its
abstract and later full-text discussions. An authorized historical PDF was
obtained, but its scientific pages did not yield machine-readable text in the
available extraction. It is therefore not used for a whole-document
noncoverage claim.

Older spectral or moment-problem literature may contain an equivalent inverse
transformation under terminology different from paired autocovariances.

## References

1. C. J. Geyer, “Practical Markov Chain Monte Carlo,” *Statistical Science*
   7 (1992), 473--483, DOI 10.1214/ss/1177011137, published 1992-11-01.
2. S. Berg and H. Song, “Efficient shape-constrained inference for the
   autocovariance sequence from a reversible Markov chain,” arXiv:2207.12705,
   first submitted 2022-07-26; later *Annals of Statistics* 51 (2023),
   2440--2470.
3. F. Hausdorff, “Summationsmethoden und Momentfolgen. I,”
   *Mathematische Zeitschrift* 9 (1921), 74--109.
