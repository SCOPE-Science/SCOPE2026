# The first eight-divisor threshold in the factorial knapsack problem

## Finding

For each positive integer \(n\), let \(h(n!)\) denote the smallest nonnegative integer \(k\) such that **every** integer \(t\) with \(1\le t\le n!\) can be represented as a sum of at most \(k\) **distinct positive divisors** of \(n!\). The exact values for \(1\le n\le12\) are

\[
\bigl(h(1!),h(2!),\ldots,h(12!)\bigr)
=(1,1,2,3,4,5,5,6,7,7,7,8).
\]

In particular, \(12!\) is **the first factorial for which eight distinct divisors are necessary**. Exactly **175** of the \(479001600\) integers in \([1,12!]\) are not expressible using seven or fewer distinct divisors of \(12!\). All 175 exceptional targets are odd; the least is \(475785157\) and the greatest is \(479001547\). Their complete ascending list is `EXTREMAL_TARGETS.json`. Every target does have an eight-or-fewer-distinct-divisor representation.

The count of targets requiring the maximum number of terms for \(n=1,\ldots,12\) is respectively

\[
(1,2,2,5,9,14,343,306,1,7150,272934,175).
\]

## Assumptions and scope

All sums use pairwise distinct **positive** divisors of the respective factorial; the empty sum represents only zero, which is not one of the \(n!\) positive targets. For each target the selected divisors can be different. No restriction on the sizes of the chosen divisors beyond dividing the factorial is imposed. The theorem is a finite, exact determination for \(1\le n\le12\), with no extrapolation beyond that range.

## Proof

Let \(N=n!\), and enumerate its complete divisor set \(D\), obtained by prime factorization of \(N\). For \(j\ge0\), let \(B_j\) be an integer whose binary digit in position \(t\) is 1 exactly when \(t\) is a sum of exactly \(j\) distinct elements of the currently processed subset of \(D\). Initially \(B_0=1\), \(B_j=0\) for \(j>0\). Write \(L=2^{N+1}-1\). For every divisor \(d\in D\), update **in descending \(j\)** by

\[
B_j\longleftarrow B_j\mathbin{\mathrm{OR}}\bigl((B_{j-1}\ll d)\mathbin{\mathrm{AND}}L\bigr).
\]

Here \(\ll\), OR and AND are the usual exact, nonnegative-integer bit operations. Descending order makes the current divisor available at most once. Inductively each bit exactly encodes either a representation excluding \(d\) or one including \(d\); no representation of a sum not exceeding \(N\) can be lost by discarding bits above \(N\), since all divisors are positive. Thus after all divisors, the bitwise union \(U_k=B_0\mathbin{\mathrm{OR}}\cdots\mathbin{\mathrm{OR}}B_k\) exactly encodes sums with at most \(k\) distinct divisors. Since bit 0 is set, the number of uncovered positive targets is exactly \((N+1)-\operatorname{popcount}(U_k)\).

The complete exact integer execution of this finite recurrence, with all divisors verified to divide \(N\), gives the stated \(h\) values. At \(n=12\), \(D\) contains \(792\) divisors; \(U_7\) has exactly \(175\) missing positive bits, identified by the attached complete `EXTREMAL_TARGETS.json`, whereas \(U_8\) has all \(479001601\) bits 0 through \(N\) set. The verifier repeats the same exhaustive computation for every \(n\le12\), checks the whole missing-target list, its order, its parity and the two endpoints, and checks that \(U_{h-1}\) is incomplete and \(U_h\) complete. These exhaust the domain and prove the asserted exact finite classification.

## Verification

Run `python3 verify.py` in a directory containing `EXTREMAL_TARGETS.json`. It requires only standard-library Python, exact integers and sufficient memory for bitsets up to \(12!\) (approximately 1.3 GB peak in one run). Its final expected line is `VERIFY_OK first_eight_threshold=12 exact_full_range=PASS targets=175 finite_only=YES`.

As a separate implementation cross-check, `crosscheck.cpp`, built with a C++17 compiler, uses arrays of machine-word bitsets and a different divisor enumeration to confirm the results for \(8\le n\le11\). This is an algorithmic cross-check, not an independent scientific audit.

## Relationship to prior work

The function \(h(N)\) and the factorial knapsack problem are classical; the question appears in Erdős's collected problems. Hughes (2026) studies \(h(n!)\) and proves an asymptotic upper bound. Tenenbaum and Yokota (1990), and Yokota (1995), study divisor representations and greedy bounds. The present finite result concerns the first exact eight-term threshold and the complete set of targets requiring eight terms; it does **not** claim the definition, practical-number property, generic subset-sum recurrence, or asymptotic bounds as new. No equivalent exact value and complete 175-target list was found in the literature that could be inspected. Unindexed tables or inaccessible early knapsack sources could contain it.

## Limitations

The result covers only \(n\le12\). It does not provide any uniform growth estimate, a direct arithmetic characterization of the 175 targets independent of the finite certificate, or an asymptotic theorem. The exhaustive computation is an exact finite proof conditional on correct implementation and reproducible execution, not a symbolic closed-form proof. The listed target set is only claimed complete within \([1,12!]\). Bibliographic priority remains subject to unavailable older full texts and indexing gaps; no external independent audit has occurred.

## References

1. Scott D. Hughes, *Sums of distinct divisors of factorials* (first posted 2026-09-09), arXiv:2609.10902v1, https://arxiv.org/abs/2609.10902.
2. G. Tenenbaum and H. Yokota, *Length and denominators of Egyptian fractions, III*, Journal of Number Theory 35 (1990), 150–156, DOI: 10.1016/0022-314X(90)90109-5; cited in Hughes (2026).
3. H. Yokota, *On a Knapsack Problem involving Divisors of n!*, Research Bulletin of Hiroshima Institute of Technology 29 (1995), 25–28; bibliographic record https://jglobal.jst.go.jp/detail?JGLOBAL_ID=200902179472007507.
4. Erdős Problems, Problem 18, https://www.erdosproblems.com/18.
