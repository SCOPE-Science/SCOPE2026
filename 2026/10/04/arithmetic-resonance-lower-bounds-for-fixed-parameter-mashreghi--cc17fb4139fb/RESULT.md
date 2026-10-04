# Arithmetic resonance lower bounds for fixed-parameter Mashreghi–Ransford constants

## Finding

Fix
\[
\beta>1,
\qquad
\alpha=\sqrt{\beta^2-1}.
\]
Let \(\kappa(\beta)\) denote the least constant for which the Mashreghi–Ransford inequality holds at this particular value of \(\beta\):
\[
\limsup_{n\to\infty}\frac{|a_n|}{\alpha^n}
\le
\kappa(\beta)
\left(
\limsup_{n\to\infty}\frac{|b_n|}{\beta^n}
\right)^{1/2}
\left(
\limsup_{n\to\infty}\frac{|c_n|}{\beta^n}
\right)^{1/2},
\]
where
\[
b_n=\sum_{k=0}^n\binom{n}{k}a_k,
\qquad
c_n=\sum_{k=0}^n\binom{n}{k}(-1)^{n-k}a_k.
\]

Put
\[
\phi=\arccos(1/\beta)\in(0,\pi/2).
\]
Then
\[
\Gamma(\beta)
\le
\kappa(\beta)
\le
\frac{2}{\sqrt3},
\]
where
\[
\Gamma(\beta)=
\begin{cases}
\sec\!\bigl(\pi/(2q)\bigr),
&
\phi/\pi=p/q
\ \text{in lowest terms and \(q\) is odd},\\[4pt]
1,
&
\phi/\pi
\ \text{is irrational or has even reduced denominator}.
\end{cases}
\]

The lower bound comes from the real sequence
\[
a_n
=
\frac{(i\alpha)^n-(-i\alpha)^n}{2i}.
\]
For this canonical two-pole family the normalized ratio is exactly
\[
\frac{1}
{\limsup_{n\to\infty}|\sin(n\phi)|}.
\]

Consequently this sharpness mechanism has a genuine arithmetic resonance profile. It gives a strict fixed-parameter lower bound above \(1\) exactly when \(\phi/\pi\) is rational with odd reduced denominator. The largest resonance is
\[
q=3,
\]
which forces
\[
\phi=\pi/3,
\qquad
\beta=2,
\qquad
\Gamma(2)=\frac{2}{\sqrt3}.
\]
Thus the classical \(\beta=2\) sharpness example is the shortest odd resonance of a full parameter family.

## Assumptions and scope

The binomial transforms are
\[
b_n=\sum_{k=0}^n\binom{n}{k}a_k,
\qquad
c_n=\sum_{k=0}^n\binom{n}{k}(-1)^{n-k}a_k.
\]
Only sequences satisfying
\[
b_n,c_n=O(\beta^n)
\]
are admissible.

Bouthat's 2026 theorem gives the universal upper bound
\[
\kappa(\beta)\le\frac{2}{\sqrt3}
\]
for every \(\beta>1\), and proves that this universal constant is optimal by the special parameter \(\beta=2\).

The present result refines only the lower-bound side at fixed \(\beta\). Except at \(\beta=2\), it does not determine \(\kappa(\beta)\).

## Proof

Define
\[
a_n
=
\frac{(i\alpha)^n-(-i\alpha)^n}{2i}.
\]
This sequence is real. Since
\[
\frac{a_n}{\alpha^n}
=
\frac{i^n-(-i)^n}{2i},
\]
it vanishes for even \(n\) and has modulus \(1\) for odd \(n\). Hence
\[
A
:=
\limsup_{n\to\infty}\frac{|a_n|}{\alpha^n}
=
1.
\]

The binomial theorem gives
\[
b_n
=
\frac{(1+i\alpha)^n-(1-i\alpha)^n}{2i}.
\]
Because
\[
|1+i\alpha|
=
\sqrt{1+\alpha^2}
=
\beta
\]
and
\[
1+i\alpha
=
\beta e^{i\phi},
\qquad
\cos\phi=\frac1\beta,
\]
we obtain
\[
b_n
=
\beta^n\sin(n\phi).
\]
Therefore
\[
B
:=
\limsup_{n\to\infty}\frac{|b_n|}{\beta^n}
=
L(\phi),
\]
where
\[
L(\phi)
=
\limsup_{n\to\infty}|\sin(n\phi)|.
\]

Likewise,
\[
c_n
=
\frac{(-1+i\alpha)^n-(-1-i\alpha)^n}{2i}.
\]
Now
\[
-1+i\alpha
=
\beta e^{i(\pi-\phi)},
\]
so
\[
c_n
=
\beta^n\sin(n(\pi-\phi))
=
(-1)^{n+1}\beta^n\sin(n\phi).
\]
Thus
\[
C
:=
\limsup_{n\to\infty}\frac{|c_n|}{\beta^n}
=
L(\phi).
\]

For this admissible sequence the ratio appearing in the best-constant problem is therefore
\[
\frac{A}{\sqrt{BC}}
=
\frac1{L(\phi)}.
\]
It follows that
\[
\kappa(\beta)\ge\frac1{L(\phi)}.
\]

It remains to evaluate \(L(\phi)\).

If
\[
\phi/\pi
\]
is irrational, then the multiples of \(\phi\) are dense modulo \(\pi\), so
\[
L(\phi)=1.
\]

Suppose instead that
\[
\phi/\pi=p/q
\]
in lowest terms. Multiplication by \(p\) permutes the residue classes modulo \(q\), and hence
\[
L(\phi)
=
\max_{0\le k<q}
\left|
\sin\left(\frac{k\pi}{q}\right)
\right|.
\]
If \(q\) is even, the residue
\[
k=q/2
\]
occurs and therefore
\[
L(\phi)=1.
\]
If \(q\) is odd, the two closest residues to \(q/2\) are
\[
(q-1)/2
\quad\text{and}\quad
(q+1)/2,
\]
so
\[
L(\phi)
=
\cos\left(\frac{\pi}{2q}\right).
\]
This proves the stated formula for \(\Gamma(\beta)\).

Finally, among odd denominators allowed by
\[
0<\phi<\pi/2,
\]
the smallest possible denominator is \(q=3\). Since
\[
\sec\left(\frac{\pi}{2q}\right)
\]
strictly decreases with \(q\ge3\), the largest value furnished by this family is
\[
\sec(\pi/6)=\frac2{\sqrt3}.
\]
The case \(q=3\) necessarily has
\[
\phi=\pi/3,
\]
so
\[
\beta=\sec(\pi/3)=2.
\]
Bouthat's universal upper bound then shows
\[
\kappa(2)=\frac2{\sqrt3}.
\]

## Verification

The transform identities above are exact consequences of the binomial theorem. In particular, no asymptotic approximation is used to obtain
\[
b_n=\beta^n\sin(n\phi)
\]
or
\[
c_n=(-1)^{n+1}\beta^n\sin(n\phi).
\]

The orbit maximum for rational \(\phi/\pi\) is a finite residue-class calculation. For irrational \(\phi/\pi\), density modulo \(\pi\) gives the limiting supremum \(1\).

The fresh primary theorem was inspected at the statement and proof level. It uses the same normalization
\[
\alpha=\sqrt{\beta^2-1},
\]
states the universal constant \(2/\sqrt3\), and identifies the classical sharpness witness only at \(\beta=2\). Its normalized angle is defined by
\[
\cos\phi=1/\beta,
\]
which is exactly the angle used here.

No numerical experiment or finite truncation is used as evidence.

## Relationship to prior work

Mashreghi and Ransford proved the original growth inequality with universal constant \(2\) and exhibited the \(\beta=2\) two-pole sequence that forces the universal constant to be at least \(2/\sqrt3\).

Bouthat proves in 2026 that
\[
2/\sqrt3
\]
is the optimal universal constant for all \(\beta>1\). The paper explicitly formulates optimality at the universal level and repeats the \(\beta=2\) witness. It does not introduce the best constant \(\kappa(\beta)\) at a fixed parameter, nor does it analyze the same witness as \(\beta\) varies.

The present calculation keeps the sharpness construction at the natural moving scale
\[
\alpha=\sqrt{\beta^2-1}
\]
and evaluates its normalized ratio for every fixed parameter. The result exposes the arithmetic distinction between irrational angles, even-denominator rational angles, and odd-denominator rational resonances.

Targeted searches for fixed-\(\beta\) constants, rational-angle resonance, and parameterized binomial-transform sharpness did not locate an equivalent statement.

## Limitations

The lower function
\[
\Gamma(\beta)
\]
is not claimed to equal the true fixed-parameter constant
\[
\kappa(\beta)
\]
except at \(\beta=2\).

For irrational angles and rational angles of even reduced denominator, this particular family yields only the baseline lower bound \(1\). Other sequence families may give larger fixed-parameter obstructions.

The result therefore identifies the exact resonance profile of the canonical two-pole sharpness mechanism, not a complete solution of the fixed-\(\beta\) optimization problem.

## References

1. L. Bouthat, *The sharp constant in the Mashreghi–Ransford inequality*, arXiv:2609.08852v1, 2026.
2. J. Mashreghi and T. Ransford, *Binomial sums and functions of exponential type*, Bulletin of the London Mathematical Society 37 (2005), 15--24, DOI:10.1112/S0024609304003625.
