# Supported scientific review

## Correctness — PASS

The Chinese remainder theorem independently determines one residue for each of the two offsets \(c,d\) modulo each of the first \(k-1\) primes. Coprimality of \(a,b\) proves that every nonnegative representation of the constructed integer has index \(1\le t\le k-1\); the corresponding prime divides both multipliers. This is an exhaustive infinite proof, not a numerical inference. The primorial growth \(\log M_k\sim k\log k\) is a standard consequence of the prime number theorem, establishing uniformity. For \(k=5\), the explicit fourfold inequality is checked algebraically. Exact standalone code independently enumerates all representations of 150 small instances and verifies 464 CRT witnesses. Risks: the analytic asymptotic uses the classical prime number theorem; no numerical or conditional assumptions replace it.

## Originality — PASS (with residual risk)

Theorem 1.6 of Ding–Wang–Zhang [1] gives only the constant-scale all-pairs lower bound \(G(a,b)\ge ab\), and their Theorem 1.7 gives a stronger bound only along selected sequences with one generator fixed. The new all-pairs logarithmic lower bound does not follow from either. Jaffe [2] gives upper estimates and conjectures the fourfold lower bound; the concrete \(413\)-threshold proves a large-parameter slice but not the full conjecture. Mathematical-result searches for the exact coprime-coordinate invariant, primorial obstruction, and equivalent CRT construction found no dominating published statement. Related Frobenius results for a different semigroup of Pythagorean quadruples and densities of polynomial gcd values do not imply this two-generator claim. An unindexed elementary Jacobsthal-type argument could predate this construction; search noncoverage is not proof of uniqueness.

## Mathematical value — PASS

The published problem asks about the size of a new natural Diophantine Frobenius invariant. The construction makes a striking **uniform all-pairs** jump from a constant normalized lower bound to unbounded normalized growth, quantifies it at the \(\log H/\log\log H\) scale, and gives a finite threshold for a separately posed fourfold lower-bound conjecture. The exact reason—covering every feasible nonnegative representation by a distinct forced common prime—is structurally meaningful. This neither solves the exact Frobenius invariant nor establishes an optimal growth order.

## Closest literature and limitations

[1] Y. Ding, W. Wang and H. Zhang, *The Diophantine Frobenius Problem revisited*, arXiv:2509.08599v1 (2025), especially Theorems 1.6 and 1.7 and their proofs.

[2] G. N. Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, arXiv:2610.17267v1 (2026), especially §7.

No independent audit or optimality proof is asserted. The relevance of possible unindexed older CRT constructions remains a scientific literature risk.

Self-review: passed. Independent audit: not yet performed.
