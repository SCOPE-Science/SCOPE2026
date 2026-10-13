# Finite-use arity separation in bounded Ramsey theory
## Finding

For integers \(n,\ell\ge 1\), let
\[
\mathsf{BRT}^{n}_{2,\ell}
\]
be bounded Ramsey's theorem for two-colorings of \(n\)-tuples: an instance is a coloring
\[
f:[\mathbb N]^n\to\{0,1\}
\]
with no \(f\)-homogeneous set of color \(1\) of size \(\ell\), and a solution is an infinite \(f\)-homogeneous set of color \(0\).

Let
\[
\mathsf{BRT}^{2}_{2}
\]
denote the pairs problem in which the finite bound is supplied with the instance.

Then:

\[
\boxed{
\text{No fixed finite number of applications of }\mathsf{BRT}^{2}_{2}
\text{ can solve }\mathsf{BRT}^{3}_{2,4}
\text{ in the Hirschfeldt--Jockusch reduction game.}
}
\]

Equivalently, the fixed four-obstruction triple principle cannot be obtained by any bounded finite iteration of the pairs-level bounded Ramsey problem.

This is a separation **inside the bounded Ramsey hierarchy**. Patey and Shafer prove the stronger benchmark separation against finitely many uses of the full pair Ramsey theorem \(\mathsf{RT}^{2}_{2}\); the present statement isolates the consequence for the lower-arity bounded principle itself.

## Assumptions and scope

The reduction notion is the finite-use version of \(\omega\)-reducibility defined through the Hirschfeldt--Jockusch game.

Only a fixed finite number of oracle applications is ruled out. No claim is made here about unrestricted \(\omega\)-reducibility between the two bounded Ramsey principles.

The source's hard principle is the fixed-bound statement
\[
\mathsf{BRT}^{3}_{2,4},
\]
not merely the unparameterized union over all bounds.

The pairs problem is used only through the following elementary fact: a valid bounded-Ramsey pair instance is also an instance of ordinary Ramsey's theorem for pairs, and every infinite ordinary homogeneous solution must automatically have color \(0\).

## Proof

Patey and Shafer prove the following in Theorem 1.7:

for every finite \(k\),
\[
\mathsf{BRT}^{3}_{2,4}\not\leq^k_\omega\mathsf{RT}^{2}_{2}.
\]

In words, no fixed finite number of applications of Ramsey's theorem for pairs suffices to solve every instance of the fixed-bound triple problem.

It remains to compare the pairs-level bounded problem with ordinary Ramsey's theorem for pairs.

Take any valid instance
\[
(\ell,f)
\]
of
\[
\mathsf{BRT}^{2}_{2},
\]
so
\[
f:[\mathbb N]^2\to\{0,1\}
\]
has no color-\(1\) homogeneous set of size \(\ell\).

Submit the same coloring \(f\) as an instance of
\[
\mathsf{RT}^{2}_{2}.
\]

Let \(H\) be any infinite \(f\)-homogeneous set returned by Ramsey's theorem.

If \(H\) were homogeneous for color \(1\), then any \(\ell\) elements of \(H\) would form a color-\(1\) homogeneous set of size \(\ell\), contradicting the promise on the bounded-Ramsey instance.

Therefore \(H\) must be homogeneous for color \(0\). Hence \(H\) is already a solution to the original bounded-Ramsey instance.

Thus one application of
\[
\mathsf{BRT}^{2}_{2}
\]
can be simulated uniformly by one application of
\[
\mathsf{RT}^{2}_{2}.
\]

Now suppose, toward a contradiction, that some fixed finite number of applications of
\[
\mathsf{BRT}^{2}_{2}
\]
were sufficient to solve
\[
\mathsf{BRT}^{3}_{2,4}.
\]

Replace each call to the bounded pairs problem by the one-call simulation above. This would yield a reduction using only finitely many applications of
\[
\mathsf{RT}^{2}_{2}.
\]

That contradicts Patey--Shafer's Theorem 1.7, which excludes every fixed finite number of such applications.

Therefore no bounded finite iteration of the pairs-level bounded Ramsey problem solves
\[
\mathsf{BRT}^{3}_{2,4}.
\]

## Verification

The source's definition of bounded Ramsey's theorem was checked directly in the primary preprint. It defines
\[
\mathsf{BRT}^{n}_{2,\ell}
\]
using the absence of a color-\(1\) homogeneous set of size \(\ell\), and defines the unbounded-bound version by universal quantification over \(\ell\).

Theorem 1.7 was checked in the primary full text and states that for every finite \(k\),
\[
\mathsf{BRT}^{3}_{2,4}\not\leq^k_\omega\mathsf{RT}^{2}_{2}.
\]

The proof of that theorem is based on preservation of multiple hyperimmunities and triangle-free graphs with suitably small independence number.

The only additional step needed here is the one-call simulation of a bounded pair instance by ordinary pair Ramsey. That step is immediate from the instance promise and does not depend on any unproved combinatorial assertion.

No finite experiment is used.

## Relationship to prior work

Patey and Shafer emphasize that
\[
\mathsf{BRT}^{3}_{2}
\]
is the first level of the bounded Ramsey hierarchy that is not computably true, while the pairs-level principle
\[
\mathsf{BRT}^{2}_{2}
\]
is computably true.

Their main separation theorem is formulated against the stronger benchmark
\[
\mathsf{RT}^{2}_{2},
\]
showing that finitely many uses of full pair Ramsey do not suffice for
\[
\mathsf{BRT}^{3}_{2,4}.
\]

The present consequence re-expresses that lower bound internally to the bounded hierarchy: even repeated access to the lower-arity bounded problem cannot bridge the arity jump in any fixed finite number of calls.

Targeted searches for bounded Ramsey triples versus bounded Ramsey pairs, finite iteration, finite parallelization, and the exact fixed-bound principle did not locate this internal-hierarchy formulation.

## Limitations

The result is a finite-use separation only.

It does not decide unrestricted
\[
\omega\text{-reducibility}
\]
between the corresponding principles.

It does not provide a new lower-bound construction; it transfers the source's lower bound through a uniform identity-on-instances simulation.

The result also does not claim that the pairs and triples principles differ under every stronger reducibility notion.

## References

[1] Ludovic Patey and Paul Shafer, “Bounded Ramsey's theorem for triples in computability theory,” arXiv:2604.02092, first posted 2 April 2026.

[2] Quentin Le Houérou and Ludovic Patey, “The reverse mathematics of bounded Ramsey's theorem for pairs,” arXiv:2509.03688, first posted 3 September 2025.
