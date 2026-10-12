# Minimum abelian power-semigroup hosts for finite monogenic semigroups

## Finding
For positive integers \(\mu,\lambda\), let \(S_{\mu,\lambda}\) be the finite monogenic semigroup with index \(\mu\) and period \(\lambda\): its first \(\mu+\lambda-1\) positive powers are distinct and the first repeating power satisfies \(x^{\mu+\lambda}=x^\mu\). For a finite abelian group \(G\), write \(\mathcal P_*(G)\) for the semigroup of **nonempty** subsets under Minkowski addition, and define
\[
M(\mu,\lambda)=\min\{|G|:G\text{ finite abelian and }S_{\mu,\lambda}\hookrightarrow\mathcal P_*(G)\}.
\]
Then
\[
\boxed{M(\mu,\lambda)=\begin{cases}\lambda,&\mu=1,\\(\mu+1)\lambda,&\mu\ge2.\end{cases}}
\]

There is also an exact classification of **all** representations in hosts of the minimum order. For \(\mu=1\), the host is \(G\cong C_\lambda\) and the generating subset is a singleton containing a generator. For \(\mu\ge2\), every optimal generating subset has the form \(A=\{a,a+b\}\), where \(H=\langle b\rangle\) has order \(\mu+1\), the quotient \(G/H\) is cyclic of order \(\lambda\), and \(a+H\) generates this quotient; every such pair gives an optimal representation. In particular, a **cyclic** optimal host always exists: take \(G=C_{(\mu+1)\lambda}\), \(a=1\), and \(b=\lambda\) for \(\mu\ge2\), or take \(G=C_\lambda\) and \(A=\{1\}\) for \(\mu=1\). Here residue notation refers to the corresponding cyclic group.

## Assumptions and scope
All groups are finite, abelian, written additively, and may be the trivial group. All subsets used as semigroup elements are nonempty. Powers of \(A\) are repeated sumsets, with the first power indexed by \(1\). The semigroup embedding is determined by the image of the generator, so existence is equivalent to finding a subset with exactly the stipulated index and period. The statement optimizes **host-group order**, not the number of subset generators, and does not assert a minimum among nonabelian groups.

## Proof
Choose an arbitrary nonempty subset \(A\subseteq G\), a point \(a\in A\), and put \(B=A-a\) and \(H=\langle B\rangle\le G\). Then \(0\in B\), and for every positive integer \(k\),
\[
A^k=ka+kB,\qquad B\subseteq 2B\subseteq3B\subseteq\cdots\subseteq H.
\]
Here \(kB\) denotes the sum of \(k\) copies of \(B\). Since \(B\) generates \(H\) as a subgroup of a **finite** group, it also generates \(H\) using nonnegative sums. Consequently this ascending chain eventually reaches \(H\). Let \(\nu\ge1\) be its first such index.

Every inclusion before reaching \(H\) is strict. Indeed, if \(kB=(k+1)B\), then \(kB+B=kB\), so repeated addition of elements of \(B\) preserves \(kB\). The nonnegative sums of \(B\) fill \(H\), so \(kB+H=kB\); since \(kB\) is a nonempty subset of \(H\), this forces \(kB=H\). Thus \(|B|<|2B|<\cdots<|\nu B|=|H|\), with the vacuous-chain convention if \(\nu=1\).

Before \(\nu\), different powers \(A^k\) have strictly increasing cardinalities, while for every \(k\ge\nu\) they equal the cosets \(ka+H\). Therefore the index of \(A\) is exactly \(\nu\), and its eventual period is exactly the order of \(a+H\) in \(G/H\). In particular, for a realization of \(S_{\mu,\lambda}\),
\[
\mu=\nu,\qquad \lambda=\operatorname{ord}_{G/H}(a+H),\qquad
\lambda\mid[G:H].
\]
If \(\mu=1\), then \(|G|=|H|[G:H]\ge\lambda\). Equality requires \(|H|=1\), hence \(A\) is a singleton; the quotient-period condition forces \(G\) cyclic with its singleton element a generator. This also attains equality.

If \(\mu\ge2\), then \(B\ne\{0\}\) and \(|B|\ge2\). There are \(\mu-1\) strict inclusions from \(B\) to \(\mu B=H\). Thus
\[
|H|\ge |B|+(\mu-1)\ge\mu+1,
\qquad |G|=|H|[G:H]\ge(\mu+1)\lambda.
\]
Equality forces \(|H|=\mu+1\), \([G:H]=\lambda\), and \(|B|=2\). Therefore \(B=\{0,b\}\); as \(H=\langle B\rangle\), the element \(b\) generates \(H\), and the element \(a+H\) generates \(G/H\). This proves necessity of the stated normal form. Conversely, for any such data, \(kB=\{0,b,\ldots,kb\}\) for \(1\le k\le\mu\), so the first full sumset is \(\mu B=H\) and the quotient period is \(\lambda\). Thus the normal form always realizes the required semigroup with host order exactly \((\mu+1)\lambda\).

Finally, in the cyclic group of order \((\mu+1)\lambda\), the element \(b=\lambda\) has order \(\mu+1\), and the image of \(a=1\) in the quotient by \(\langle b\rangle\) has order \(\lambda\). This proves existence of a cyclic minimizing host. The \(\mu=1\) witness follows from a singleton generator in \(C_\lambda\). These arguments cover \(\lambda=1\) and the trivial-group boundary without exceptions.

## Verification
An accompanying standalone Python script, `verify.py`, independently enumerates all nonempty subsets of each finite abelian group in invariant-factor form with order at most \(12\). It computes the exact index and period by repeating subset addition until a collision, tests the universal lower bound, checks every equality case against the normal form, and confirms optimal realization of every parameter pair whose bound is at most \(12\). It also checks \(130\) explicit construction cases beyond this census. The run reports `GROUP_PROFILES=17`, `NONEMPTY_SUBSETS=13309`, `OPTIMAL_SUBSETS=325`, `OBSERVED_INDEX_PERIOD_PAIRS=29`, `EXPLICIT_WITNESSES=130`, followed by `VERIFY_OK`. These are **finite checks**, not the proof of the universal result; the preceding argument proves the general claim.

## Relationship to prior work
Bershadsky, Kublanovsky, and Mashevitzky describe the power-semigroup embeddability programme, including finite and periodic commutative semigroups (Section 5, Problems 5.3–5.5). Lau establishes reductions for the qualitative representation question for finite commutative semigroups. The exact minimum finite abelian host order for every index–period pair, and the characterization of all equality cases, are not stated in the inspected passages. Tringali's 2026 survey focuses primarily on arithmetic and automorphisms of power monoids rather than host-order minimization for monogenic semigroups. General sumset-growth facts motivate the strict-chain argument but do not themselves state the optimal host-order classification. Earlier work on subsemigroups of complexes and an inaccessible publisher full text could potentially contain equivalent formulations; no claim of exhaustive bibliographic coverage is made.

## Limitations
The result is limited to a single-generator target semigroup and finite **abelian** host groups. It does not settle the general finite commutative-semigroup embeddability problem or classify host-minimizers outside the abelian category. The computational verification is exhaustive only in the specified finite range. Two plausible historical/publisher sources were not accessible in full, leaving a stated literature risk.

## References
1. S. Bershadsky, S. Kublanovsky, G. Mashevitzky, *The Lyapin's notebook: a collection of unsolved problems in Semigroup Theory*, arXiv:2604.04763 (first posted 2026-04-06), especially Section 5, Problems 5.3–5.5. https://arxiv.org/abs/2604.04763
2. A. Lau, *Finite Abelian semigroups represented into the power set of finite groups*, Czechoslovak Mathematical Journal 29 (1979), 159–162. https://dml.cz/dmlcz/101590
3. S. G. Bershadsky and S. I. Kublanovsky, *On power semigroups of groups*, Semigroup Forum 111 (2025), 543–560. https://doi.org/10.1007/s00233-025-10594-3
4. S. Tringali, *Power monoids and their arithmetic: a survey*, arXiv:2602.15754 (2026). https://arxiv.org/abs/2602.15754
5. F. D. Pedersen and W. S. Sizer, *Subsemigroups of the finite complexes of a group*, Semigroup Forum 20 (1980), 285–292.
