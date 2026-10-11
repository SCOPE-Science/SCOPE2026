# A dimension–parameter boundary layer for sharp pluriharmonic Bohr radii

## Finding

For each integer
\[
n\ge1
\]
and parameter
\[
0<\alpha<1,
\]
let
\[
r_{n,\alpha}
\]
be the sharp Bohr radius characterized by Theorem 4.1 of arXiv:2607.27272v1. Thus
\[
x_{n,\alpha}=n r_{n,\alpha}\in(0,1)
\]
is the unique solution of
\[
x+2n(1-\alpha)\sum_{m=2}^{\infty}\frac{x^m}{m}
=
1+2n(1-\alpha)\sum_{m=2}^{\infty}\frac{(-1)^{m-1}}{m n^m}.
\]

Let the class parameter vary with the dimension and define
\[
\tau_n=n(1-\alpha_n),
\qquad
x_n=n r_{n,\alpha_n}.
\]

If
\[
\tau_n\to\tau\in[0,\infty),
\]
then
\[
x_n\to\xi(\tau),
\qquad
r_{n,\alpha_n}\sim\frac{\xi(\tau)}{n},
\]
where
\[
\xi(0)=1
\]
and, for
\[
\tau>0,
\]
the number
\[
\xi(\tau)\in(0,1)
\]
is the unique solution of
\[
\xi+2\tau\bigl(-\log(1-\xi)-\xi\bigr)=1.
\]

If
\[
\tau_n\to\infty,
\]
then
\[
\sqrt{\tau_n}\,x_n\to1
\]
and hence
\[
r_{n,\alpha_n}
\sim
\frac{1}{n\sqrt{n(1-\alpha_n)}}.
\]

For fixed
\[
0<\alpha<1,
\]
put
\[
a=1-\alpha.
\]
Then
\[
r_{n,\alpha}
=
\frac{1}{\sqrt a}\,n^{-3/2}
-
\frac{5}{6a}\,n^{-2}
+
O_\alpha(n^{-5/2}).
\]

The sharp radius therefore has a dimension–parameter boundary layer at
\[
1-\alpha\asymp n^{-1}.
\]
For fixed
\[
\alpha,
\]
the scale is
\[
n^{-3/2},
\]
whereas in the endpoint window the scale is
\[
n^{-1}
\]
with a nonconstant profile.

## Assumptions and scope

The class is the normalized pluriharmonic family
\[
\mathscr{P}_{\mathcal H_n^0}(\alpha)
\]
introduced in arXiv:2607.27272v1. We restrict to
\[
0<\alpha<1,
\]
which lies in the parameter range used by the source theorem.

The radius
\[
r_{n,\alpha}
\]
is exactly the source's sharp radius for its Bohr inequality on the polydisc of polyradius
\[
1/n.
\]
No new notion of Bohr radius is introduced.

This result does not concern the classical Bohr radius of all bounded holomorphic functions on the unit polydisc, nor the powered first or second Bohr radii of bounded vector-valued pluriharmonic functions.

## Proof

Set
\[
S(x)
=
-\log(1-x)-x
=
\sum_{m=2}^{\infty}\frac{x^m}{m}
\]
and
\[
T_n
=
\log(1+1/n)-1/n
=
\sum_{m=2}^{\infty}\frac{(-1)^{m-1}}{m n^m}.
\]
The exact source equation becomes
\[
x_n+2\tau_nS(x_n)
=
1+2\tau_nT_n.
\]

The alternating logarithmic expansion gives
\[
T_n
=
-\frac{1}{2n^2}
+
O(n^{-3}).
\]
Because
\[
0<1-\alpha_n<1,
\]
we have
\[
\tau_n<n,
\]
so
\[
2\tau_nT_n=O(n^{-1}).
\]

Suppose first that
\[
\tau_n\to\tau<\infty.
\]
For
\[
\tau>0,
\]
the function
\[
F_\tau(x)
=
x+2\tau S(x)
\]
is continuous and strictly increasing on
\[
[0,1),
\]
starts at zero, and diverges as
\[
x\uparrow1.
\]
Hence
\[
F_\tau(x)=1
\]
has a unique root
\[
\xi(\tau)\in(0,1).
\]
Any subsequential limit of
\[
x_n
\]
must satisfy this limiting equation, so uniqueness gives
\[
x_n\to\xi(\tau).
\]

When
\[
\tau=0,
\]
the limiting equation reduces to
\[
x=1.
\]
If a subsequence stayed a fixed distance below one, the term containing
\[
\tau_n
\]
would vanish and the left side would converge to that smaller limit, contradicting convergence of the right side to one. Thus
\[
x_n\to1.
\]

Now suppose
\[
\tau_n\to\infty.
\]
If
\[
x_n
\]
did not tend to zero, then
\[
2\tau_nS(x_n)
\]
would diverge along a subsequence, whereas the right side tends to one. Therefore
\[
x_n\to0.
\]
Since
\[
S(x)=\frac{x^2}{2}+O(x^3),
\]
we obtain
\[
x_n+\tau_nx_n^2\bigl(1+O(x_n)\bigr)=1+o(1).
\]
The first term vanishes, so
\[
\tau_nx_n^2\to1.
\]

For the fixed-parameter expansion, let
\[
a=1-\alpha>0,
\qquad
\varepsilon=n^{-1/2}.
\]
Seek
\[
x_{n,\alpha}
=
A\varepsilon+B\varepsilon^2+O(\varepsilon^3).
\]
Using
\[
S(x)=\frac{x^2}{2}+\frac{x^3}{3}+O(x^4)
\]
and
\[
2naT_n=-a\varepsilon^2+O(\varepsilon^4),
\]
the constant term gives
\[
aA^2=1,
\]
so
\[
A=a^{-1/2}.
\]
The coefficient of
\[
\varepsilon
\]
gives
\[
A+2aAB+\frac{2a}{3}A^3=0,
\]
hence
\[
B=-\frac{5}{6a}.
\]

The exact derivative of the left root function is
\[
1+\frac{2na\,x}{1-x}.
\]
At the two-term approximation it has order
\[
\varepsilon^{-1}.
\]
The residual there is
\[
O(\varepsilon^2),
\]
so the mean-value theorem and strict monotonicity give a root error
\[
O(\varepsilon^3).
\]
Dividing by
\[
n=\varepsilon^{-2}
\]
proves the displayed radius expansion.

## Verification

The primary full text was inspected at the class definition, Theorem 4.1, its monotone auxiliary function, its sharpness witness, and the dimensional plot. The source proves that the root is sharp and unique. It displays the radius only for
\[
n=1,2,3,4
\]
and does not state a high-dimensional asymptotic or a joint scaling in
\[
n(1-\alpha).
\]

The proof above is analytic and uses the exact source equation. Finite computation is not used to infer an infinite-dimensional limit.

The bundled standard-library checker solves the exact source equation by bisection. For fixed
\[
\alpha,
\]
it checks convergence of the leading normalization and the two-term residual. It also checks the finite-\(\tau\) profile at three positive values of
\[
\tau.
\]
The stored numerical output is only a sanity check.

## Relationship to prior work

Majumder, Banerjee, Panja, and Pramanik introduce
\[
\mathscr{P}_{\mathcal H_n^0}(\alpha)
\]
and characterize its sharp Bohr radius by the root equation used here. Their theorem gives existence, uniqueness, and sharpness but no dimension limit.

The classical high-dimensional Bohr radius for bounded holomorphic functions on the unit polydisc is a different invariant. Bayart, Pellegrino, and Seoane-Sepúlveda prove the scale
\[
\sqrt{\frac{\log n}{n}}
\]
for that problem. Its hypotheses and majorant inequality differ from the normalized pluriharmonic distance-to-boundary problem here.

Das studies powered Bohr radii for bounded vector-valued holomorphic or pluriharmonic functions, and Halder studies first and second powered Bohr radii for bounded operator-valued pluriharmonic functions on complete Reinhardt domains. Those definitions are not implication-equivalent to the sharp radius in the present source.

Targeted searches for the exact source, high-dimensional asymptotics of its root, the fixed-parameter
\[
n^{-3/2}
\]
scale, and the crossover variable
\[
n(1-\alpha)
\]
did not locate an equivalent published statement.

## Limitations

The theorem is specific to the sharp radius defined in arXiv:2607.27272v1.

The remainder
\[
O_\alpha(n^{-5/2})
\]
is not uniform as
\[
\alpha\uparrow1.
\]
The finite-\(\tau\) profile is the appropriate replacement in that boundary layer.

The source is a recent preprint. A later revision or an unindexed follow-up could independently add related asymptotics.

## References

1. S. Majumder, A. Banerjee, S. Panja, and D. Pramanik, *Coefficient estimates and Bohr phenomenon for pluriharmonic mappings in the polydisc*, arXiv:2607.27272v1, 29 July 2026.
2. F. Bayart, D. Pellegrino, and J. B. Seoane-Sepúlveda, *The Bohr radius of the \(n\)-dimensional polydisk is equivalent to \(\sqrt{(\log n)/n}\)*, Advances in Mathematics 264 (2014), 726–746; arXiv:1310.2834.
3. N. Das, *The \(p\)-Bohr radius for vector-valued holomorphic and pluriharmonic functions*, Forum Mathematicum 36 (2024), 765–782; arXiv:2303.14257.
4. H. Halder, *On the second Bohr radius for vector valued pluriharmonic functions*, arXiv:2601.12608v2, 2026.
