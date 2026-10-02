# Extension-maximal Harborth witnesses in \(C_9^2\)

Let \(G=C_9\times C_9\). A 9-sum is a 9-element subset whose sum is zero. Write \(g(G)\) for the ordinary Harborth constant. To avoid collision with the established notation \(g^k(G)\) for the \(k\)-Harborth constant, define \(h_2(G)\) here to be the least integer \(m\) such that every \(m\)-element subset of \(G\) contains two disjoint 9-sums.

Define
\[
S_{16}=\{(0,1),(0,2),(1,0),(1,1),(2,7),(3,4),(3,5),(4,2),(4,3),(5,0),(5,8),(6,7),(6,8),(7,5),(8,3),(8,4)\},
\]
and
\[
S_{20}=S_{16}\cup\{(0,3),(5,1),(6,5),(7,2)\}.
\]

## Result

1. \(S_{16}\) contains no 9-sum, and every one-point extension of \(S_{16}\) contains a 9-sum. Thus it is extension-maximal 9-sum-free and gives \(g(C_9^2)\ge17\). Novelty is not claimed for the bare numerical lower bound 17.

2. \(S_{20}\) contains exactly 1832 9-sums, every two of which intersect, and every one-point extension of \(S_{20}\) contains two disjoint 9-sums. Hence \(h_2(C_9^2)\ge21\), with an explicit extension-maximal witness.

3. For every finite abelian group \(H\),
\[
h_2(H)\le g(H)+\exp(H).
\]
Indeed, from a set of that size extract one \(\exp(H)\)-term zero-sum; the remaining \(g(H)\) points contain a second disjoint one.

## Verification

A fresh exhaustive enumeration independently reproduces all four finite claims: zero 9-sums in \(S_{16}\); no bad one-point extension of \(S_{16}\); exactly 1832 9-sums in \(S_{20}\) with no disjoint pair; and no bad one-point extension of \(S_{20}\).

The deterministic certificate is `artifacts/certify.py`; its retained output is `artifacts/verification.log`.

## Scope

Only the displayed one-sided bounds and extension-maximality statements are claimed. Exact values, global cardinality optimality of the witnesses, higher-prime analogues, and classification are not established.

## Literature note

The notation \(g^k(G)\) is already used in Lemos–Moriya–Moura–Silva for the \(k\)-Harborth constant, meaning existence of one zero-sum subset of size \(k\). The disjoint-pair invariant \(h_2\) above is a different predicate.
