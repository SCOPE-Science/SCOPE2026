# Uniform catenary degree three for shifted Fibonacci numerical semigroups

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For every integer \(a\ge3\), consider
\[
S(a)=\langle F_a+F_j:j\ge0\rangle
    =\langle F_a,F_a+F_2,\ldots,F_a+F_{a-1}\rangle.
\]
The displayed finite generating set is the minimal generating set, as established in the source paper [1]. The standard catenary degree of this numerical semigroup is exactly
\[
\boxed{\mathsf c(S(a))=3\quad(a\ge3).}
\]
In particular, a factorization-distance invariant stays bounded by three even as the embedding dimension \(a-1\) grows without bound.

## Assumptions and scope
Write \(m=F_a\), \(g_0=m\), and \(g_i=m+F_i\) for \(2\le i<a\). A factorization of \(N\in S(a)\) is a vector of nonnegative multiplicities of these distinct minimal generators whose weighted sum is \(N\). For two factorizations \(u,v\), set \(z_j=\min(u_j,v_j)\) and
\[
d(u,v)=\max\!\left(\sum_j(u_j-z_j),\sum_j(v_j-z_j)\right).
\]
A \(c\)-chain is a sequence of factorizations of the same element with successive distance at most \(c\). The catenary degree \(\mathsf c(S(a))\) is the least integer \(c\) such that every pair of factorizations of every \(N\in S(a)\) can be joined by a \(c\)-chain.

## Proof
First assume \(a\ge4\). The following identities hold for the indicated ranges; each can be used in either direction as an equality of factorizations:

1. \(g_i+g_{i+1}=g_{i+2}+g_0\) for \(2\le i\le a-3\).
2. \(g_{a-2}+g_{a-1}=3g_0\).
3. \(2g_2=g_3+g_0\).
4. \(2g_3=g_4+g_2\) if \(a\ge5\).
5. \(2g_i=g_{i+1}+g_{i-2}\) for \(4\le i\le a-2\).
6. \(2g_{a-1}=2g_0+g_{\max(2,a-3)}\).

These identities follow respectively from \(F_i+F_{i+1}=F_{i+2}\), \(F_{a-2}+F_{a-1}=F_a\), \(2F_2=F_3\), \(2F_3=F_4+F_2\), \(2F_i=F_{i+1}+F_{i-2}\), and \(2F_{a-1}=F_a+F_{a-3}\), using \(F_1=F_2=1\) when \(a=4\). Each identity changes at most three atoms, so any use has distance at most three.

Orient every identity from left to right. On the multiset of nonzero Fibonacci offsets \(F_i\) attached to the generators \(g_i\), every rule either decreases the number \(K\) of nonzero offsets, or leaves \(K\) unchanged and strictly increases their squared sum \(Q=\sum F_i^2\) with multiplicity. To see the latter for the only relevant rules (the interior double splits), observe that replacing two equal positive summands by two unequal positive summands with the same total strictly increases the sum of squares. The quantity \(K\) is a nonnegative integer and \(0\le Q<Km^2\) for fixed \(K\), so the process terminates.

At termination no positive Fibonacci offset occurs twice and no two consecutive Fibonacci offsets occur. Thus the surviving positive offsets form a legal Zeckendorf expansion using only \(F_2,\ldots,F_{a-1}\). Their sum \(r\) lies in \([0,F_a-1]\), by the usual Zeckendorf theorem (equivalently by induction on the maximal permitted index). The total represented integer remains \(N\), so \(r\equiv N\pmod m\), and hence \(r\) is uniquely determined by \(N\). Uniqueness of the Zeckendorf expansion determines the positive generators and their multiplicities. The number of copies of \(g_0\) is then determined by the equation \(N=\sum g_i\). Therefore **every factorization of the same \(N\) reduces to one and the same factorization** using distance-at-most-three moves. Reversing one reduction path and concatenating with the other proves \(\mathsf c(S(a))\le3\).

For \(a=3\), the minimal generators are \(g_0=2\) and \(g_2=3\). The single relation \(2g_2=3g_0\) reduces every factorization to one with at most one copy of \(g_2\), proving the same upper bound.

For sharpness let \(a\ge3\), \(m=F_a\). The element \(3m\) has the factorizations \(3g_0\) and \(g_{a-2}+g_{a-1}\) when \(a\ge4\), or \(3g_0\) and \(2g_2\) when \(a=3\). They are the *only* factorizations. Indeed, three atoms summing to \(3m\) must all equal \(m\); two atoms cannot include \(m\) since every other generator is strictly less than \(2m\). For \(a\ge4\), two offsets summing to \(F_a\) must include \(F_{a-1}\), since \(2F_{a-2}<F_a\), and the other is then \(F_{a-2}\). For \(a=3\), the claim is immediate. The two disjoint-support factorizations have distance three, so \(\mathsf c(S(a))\ge3\). Combining both inequalities completes the proof.

## Verification
The standalone script `verify_fibonacci_catenary.py` constructs exact integer factorizations for \(3\le a\le11\) and all target values through \(\min(14F_a,250)\). It independently checks the terminating local-rewrite algorithm, exact preservation of the represented integer, distance at most three for each local move, uniqueness of the normal form for each target, and precisely two factorizations of \(3F_a\). Its reported replay checked 35,703 factorizations and 185,705 exact local transformations without assertion failure. These are finite corroborations; the argument above proves the general statement without a cutoff.

## Relationship to prior work
Robles-Pérez and Rosales [1] introduced and solved the Frobenius/genus problem for precisely this shifted-Fibonacci semigroup family, including its minimal generators and Zeckendorf Apéry set. López-Medel, Robles-Pérez and Rosales [2] later determined pseudo-Frobenius numbers and type of the same family (under an index shift), and its generalizations. Neither inspected treatment gives a catenary-degree theorem or a uniform distance-three factorization connection. The present statement concerns a different standard factorization invariant and is not derived by simply substituting the known Frobenius/genus or type formula.

## Limitations
The claim concerns the classical Fibonacci recurrence and its shifted infinite generating family, not general \(r\)-Fibonacci sequences. It gives the global catenary degree and an explicit bounded-distance normal form, not a classification of the catenary degrees of individual semigroup elements. Earlier sources may contain an implicit or unindexed equivalent result; no independent audit has been performed.

## References
[1] A. M. Robles-Pérez and J. C. Rosales, *The Extended Frobenius Problem for Fibonacci Sequences Incremented by a Fibonacci Number*, arXiv:2210.00816 (first posted 2022-10-03); *Mediterranean Journal of Mathematics* 20 (2023), article 222. https://arxiv.org/abs/2210.00816 ; https://doi.org/10.1007/s00009-023-02428-9 .

[2] J. M. López-Medel, A. M. Robles-Pérez and J. C. Rosales, *The extended Frobenius problem for r-Fibonacci sequences shifted by r-Fibonacci numbers*, *Arabian Journal of Mathematics* (2025). https://doi.org/10.1007/s40065-025-00513-3 .
