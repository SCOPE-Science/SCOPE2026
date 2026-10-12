# Sharp composite Vandiver-to-divisor-sum constant

## Finding
For Vandiver's arithmetic function
\[
V(n)=\prod_{d\mid n}(d+1),
\]
every composite integer \(n\) satisfies
\[
V(n)\ge \frac{30}{7}\sigma(n).
\]
Equality holds if and only if \(n=4\). Thus \(30/7\) is the exact minimum of \(V(n)/\sigma(n)\) over composite positive integers.

## Assumptions and scope
Here \(\sigma(n)=\sum_{d\mid n}d\), \(\tau(n)\) is the number of positive divisors, and
\[
T(n)=\prod_{d\mid n}d=n^{\tau(n)/2}.
\]
The statement is for every composite positive integer and has no computational cutoff.

## Proof
For composite \(n\), the divisors larger than \(1\) are \(d_1,\ldots,d_s\) with \(s=\tau(n)-1\ge2\). Expanding gives
\[
\frac{V(n)}2=\prod_{i=1}^s(d_i+1)
\ge 1+\sum_{i=1}^s d_i+\prod_{i=1}^s d_i
=\sigma(n)+T(n).
\]
Equality holds exactly when \(s=2\), equivalently when \(n\) is a prime square.

It remains to prove the sharp auxiliary inequality
\[
T(n)\ge \frac87\sigma(n).
\]
If \(\tau(n)=3\), then \(n=p^2\) for a prime \(p\), so
\[
7T(n)-8\sigma(n)=7p^3-8p^2-8p-8=(p-2)(7p^2+6p+4)\ge0,
\]
with equality exactly at \(p=2\), hence \(n=4\).

If \(\tau(n)=4\), then \(T(n)=n^2\) and \(\sigma(n)\le4n\). Since such a composite \(n\) is at least \(6\),
\[
\frac{T(n)}{\sigma(n)}\ge\frac n4\ge\frac32>\frac87.
\]

If \(\tau(n)\ge5\), then \(n\ge12\), because the composite integers below \(12\) have divisor counts at most \(4\). Again \(\sigma(n)\le n\tau(n)\), hence
\[
\frac{T(n)}{\sigma(n)}
\ge\frac{n^{\tau(n)/2-1}}{\tau(n)}
\ge\frac{12^{3/2}}5>\frac87.
\]
The last comparison is valid because \(12^{t/2-1}/t\) increases for integers \(t\ge5\): the ratio of consecutive terms is \(\sqrt{12}\,t/(t+1)>1\).

Therefore
\[
V(n)\ge2\bigl(\sigma(n)+T(n)\bigr)
\ge2\left(1+\frac87\right)\sigma(n)
=\frac{30}{7}\sigma(n).
\]
Equality requires equality in both steps, hence \(n=4\). Directly, \(V(4)=30\) and \(\sigma(4)=7\), so the constant is attained and is best possible.

## Verification
A standalone exact-integer verifier checks every composite \(n\le100000\). It confirms \(7T(n)\ge8\sigma(n)\), \(V(n)\ge2(\sigma(n)+T(n))\), and \(7V(n)\ge30\sigma(n)\), with the ratio minimum \(30/7\) attained uniquely at \(4\). This finite computation is regression evidence only; the proof above is symbolic and unbounded.

## Relationship to prior work
Sándor's 2021 paper defines \(V(n)=\prod_{d\mid n}(d+1)\). Its Theorem 7 proves \(V(n)\ge2(\sigma(n)+T(n))\) for composite \(n\), with equality exactly for prime squares, and Remark 7 deduces only the weaker strict inequality \(V(n)>4\sigma(n)\). The article lists primary MSC \(11A25\). The 2022 continuation treats further inequalities and asymptotics for the same function but does not state the sharp composite constant above.

Targeted scholarly and database searches covered the exact constant \(30/7\), the equivalent auxiliary bound \(7T(n)\ge8\sigma(n)\), best-constant language, and the equality case \(n=4\); no checked result implied the claim.

The 2021 journal PDF records receipt and acceptance but no Online First day. Day-level public evidence available here is an institutional newsletter explicitly labeled “17–23 September 2021” that lists the exact paper and DOI. The date field uses \(2021\text{-}09\text{-}17\), the first date of that public dated interval; no earlier day-level public posting was verified.

## Limitations
The result concerns the global lower constant for \(V(n)/\sigma(n)\) on composite integers. It does not classify other ratio level sets or optimal constants under additional restrictions. The day-level evidence for the 2021 source is interval-dated rather than an Online First timestamp. The finite verifier does not establish the infinite theorem.

## References
1. J. Sándor, “On Vandiver’s arithmetical function – I,” *Notes on Number Theory and Discrete Mathematics* 27 (2021), no. 3, 29–38. DOI: 10.7546/nntdm.2021.27.3.29-38.
2. J. Sándor, “On Vandiver’s arithmetical function – II,” *Notes on Number Theory and Discrete Mathematics* 28 (2022), no. 4, 710–718. DOI: 10.7546/nntdm.2022.28.4.710-718.
3. Babeș-Bolyai University research newsletter, “Newsletter 17–23 septembrie 2021,” listing the Part I paper and DOI.
