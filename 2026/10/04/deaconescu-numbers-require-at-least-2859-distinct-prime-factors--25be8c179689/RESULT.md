# Deaconescu numbers require at least 2859 distinct prime factors

## Finding
Let \(S_2\) be Schemmel's second totient function,
\[
S_2(p^\alpha)=
\begin{cases}
0,&p=2,\\
p^{\alpha-1}(p-2),&p>2,
\end{cases}
\]
extended multiplicatively. A composite integer \(n\) is called a Deaconescu number when
\[
S_2(n)\mid \varphi(n)-1.
\]

Every Deaconescu number satisfies
\[
\omega(n)\ge 2859,
\]
where \(\omega(n)\) is the number of distinct prime factors.

This strengthens the 2022 lower bound \(\omega(n)\ge7\) and the 2025 lower bound \(\omega(n)\ge17\). In the special multiplier-\(3\) case, the 2025 literature proves \(\omega(n)\ge48\); the same exact extremal calculation used below raises that threshold to \(2859\).

## Assumptions and scope
For a composite Deaconescu number, write
\[
M S_2(n)=\varphi(n)-1.
\]
Hasanalizade proves that such \(n\) is odd and squarefree. The squarefree conclusion also follows immediately: if \(p^2\mid n\), then \(p\) divides both \(\varphi(n)\) and \(S_2(n)\), contradicting the displayed equation modulo \(p\).

Because \(n\) is odd and squarefree,
\[
S_2(n)=\prod_{p\mid n}(p-2)
\]
is odd, while \(\varphi(n)-1\) is odd. Hence \(M\) is odd. Hasanalizade's \(M=1\) lemma excludes composite solutions, so
\[
M\ge3.
\]

No existence of a Deaconescu number is asserted. The result is a necessary lower bound conditional only on the defining divisibility.

## Proof
Write
\[
n=\prod_{i=1}^r p_i,\qquad r=\omega(n).
\]
The defining equation is
\[
M\prod_{i=1}^r(p_i-2)=\prod_{i=1}^r(p_i-1)-1.
\]
Also
\[
M=\frac{\varphi(n)-1}{S_2(n)}
<
\frac{\varphi(n)}{S_2(n)}
=
\prod_{i=1}^r\frac{p_i-1}{p_i-2}.
\]
For fixed \(r\) and a fixed admissible congruence class of the primes, the product on the right is maximized by choosing the smallest allowed primes, because
\[
\frac{p-1}{p-2}=1+\frac1{p-2}
\]
strictly decreases with \(p\).

We first classify the possible prime residues modulo \(3\).

If \(3\mid n\), no other prime factor can be congruent to \(2\pmod3\). Indeed, such a factor would make the left side of the defining equation divisible by \(3\). If some remaining prime were \(1\pmod3\), the right side would be \(-1\pmod3\); if all remaining primes were \(2\pmod3\), the right side would be \(1\pmod3\). Both are contradictions. Thus every prime factor other than \(3\) is \(1\pmod3\). Reducing the equation modulo \(3\) then gives
\[
M\equiv(-1)^r\pmod3.
\]
Hence \(M\ge5\) when \(r\) is odd and \(M\ge7\) when \(r\) is even.

Now suppose \(3\nmid n\). Prime factors from the two nonzero residue classes cannot both occur: if one prime is \(2\pmod3\), the left side is \(0\pmod3\), while if another is \(1\pmod3\), the right side is \(-1\pmod3\). Therefore all prime factors are in a single nonzero residue class.

If every prime factor is \(1\pmod3\), then
\[
M\equiv(-1)^{r+1}\pmod3,
\]
so \(M\ge5\) for even \(r\) and \(M\ge7\) for odd \(r\).

If every prime factor is \(2\pmod3\), reduction modulo \(3\) gives no further restriction, but still \(M\ge3\).

It remains to bound the three extremal products. Let
\[
q_1<q_2<\cdots
\]
be the primes congruent to \(1\pmod3\), beginning with \(7\), and let
\[
s_1<s_2<\cdots
\]
be the primes congruent to \(2\pmod3\), beginning with \(5\).

Exact integer cross-multiplication gives
\[
2\prod_{j=1}^{2857}\frac{q_j-1}{q_j-2}<5,
\]
\[
\prod_{j=1}^{2858}\frac{q_j-1}{q_j-2}<5,
\]
and
\[
\prod_{j=1}^{2858}\frac{s_j-1}{s_j-2}<3.
\]
The relevant terminal primes are
\[
q_{2857}=56569,\qquad q_{2858}=56599,\qquad s_{2858}=56081.
\]

The first inequality dominates every \(3\mid n\) pattern with \(r\le2858\): its extremal ratio is below \(5\), while the permitted multiplier is at least \(5\). The second dominates every all-\(1\pmod3\) pattern with \(r\le2858\), again because \(M\ge5\). The third dominates every all-\(2\pmod3\) pattern with \(r\le2858\), because \(M\ge3\).

In every case this contradicts
\[
M<\frac{\varphi(n)}{S_2(n)}.
\]
Therefore
\[
\omega(n)\ge2859.
\]

For calibration, the exact product for the all-\(2\pmod3\) pattern crosses \(3\) at the very next prime:
\[
\prod_{j=1}^{2859}\frac{s_j-1}{s_j-2}>3,
\qquad
s_{2859}=56087.
\]
Thus \(2859\) is the exact cutoff supplied by this modulo-\(3\) extremal-product argument.

## Verification
The accompanying `verify.py` uses an Eratosthenes sieve through \(100000\) and exact Python integers. It independently constructs the prime lists in the two nonzero residue classes modulo \(3\) and checks the four cross-multiplied inequalities
\[
2\prod_{j=1}^{2857}(q_j-1)
<
5\prod_{j=1}^{2857}(q_j-2),
\]
\[
\prod_{j=1}^{2858}(q_j-1)
<
5\prod_{j=1}^{2858}(q_j-2),
\]
\[
\prod_{j=1}^{2858}(s_j-1)
<
3\prod_{j=1}^{2858}(s_j-2),
\]
and
\[
\prod_{j=1}^{2859}(s_j-1)
>
3\prod_{j=1}^{2859}(s_j-2).
\]
It also checks the terminal primes \(56569,56599,56081,56087\).

No floating-point comparison is used for the proof certificate. The displayed decimal approximations in `thresholds.json` are descriptive only.

## Relationship to prior work
Hasanalizade's 2022 paper proves that every Deaconescu number is odd, squarefree, and has at least seven distinct prime factors. Its proof already uses the basic ratio
\[
M<\prod_{p\mid n}\frac{p-1}{p-2},
\]
but only for a small-prime exclusion through six factors.

Mandal's 2025 paper is the closest later work. It raises the general lower bound to \(17\), proves that a multiplier-\(3\) solution has all prime divisors congruent to \(2\pmod3\), and obtains \(\omega(n)\ge48\) in that case. The present argument strengthens that residue analysis by using the exact decreasing product over admissible primes and treats all multiplier classes, not only \(M=3\).

Exact-title, exact-number, multiplier-\(3\), residue-class, and Schemmel-totient searches located no prior statement of the \(2859\) bound or the \(56087\) extremal threshold.

## Limitations
The argument does not prove Deaconescu's conjecture; it only forces any counterexample to have at least \(2859\) distinct prime factors.

The cutoff \(2859\) is sharp for this particular coarse strategy because the all-\(2\pmod3\) extremal ratio first exceeds \(3\) at its \(2859\)-th prime. Additional congruence or structural information could yield a substantially larger lower bound.

Search non-detection is not a proof of novelty. An unindexed computation could have obtained the same extremal cutoff.

## References
1. Elchin Hasanalizade, “On a conjecture of Deaconescu,” arXiv:2206.10355v1, first posted 14 June 2022; *Integers* 22 (2022), A99.
2. Sagar Mandal, “A Note on Deaconescu's Conjecture,” arXiv:2507.02930v1; *Annals of West University of Timisoara - Mathematics and Computer Science* 61 (2025), 55–60, DOI 10.2478/awutm-2025-0005.
3. M. Deaconescu, “Adding units mod \(n\),” *Elemente der Mathematik* 55 (2000), 123–127.
