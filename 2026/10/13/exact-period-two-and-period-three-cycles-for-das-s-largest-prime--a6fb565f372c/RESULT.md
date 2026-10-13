# Exact period-two and period-three cycles for Das's largest-prime-divisor map
## Finding
For every integer \(k\ge1\), define \(\Phi_k\) on integers \(n\ge2\) by
\[
\Phi_k(n)=\begin{cases}
n+k,&n\text{ prime},\\
P(n),&n\text{ composite},
\end{cases}
\]
where \(P(n)\) denotes the largest prime divisor of a composite integer \(n\).

The exact period-two cycles are precisely
\[
p\longmapsto p+k\longmapsto p,
\]
where \(p\) is prime, \(p\mid k\), and
\[
P(k/p+1)\le p.
\]
Consequently, the number of period-two cycles is exactly
\[
\#\{p\text{ prime}:p\mid k,\ P(k/p+1)\le p\}.
\]

The map has an exact period-three cycle if and only if
\[
k+1=2^a
\]
for some integer \(a\ge1\) and \(k+2=2^a+1\) is prime. In that case the cycle is unique up to rotation and is
\[
2\longmapsto k+2\longmapsto2k+2\longmapsto2.
\]
Since primality of \(2^a+1\) forces \(a\) to be a power of two, the period-three parameters are equivalently
\[
k=2^{2^t}-1
\]
for those \(t\ge0\) for which the Fermat number \(2^{2^t}+1\) is prime.

## Assumptions and scope
The statement concerns the deterministic map above and exact periods two and three only. A cycle is considered up to cyclic rotation. No assumption is made on the size or parity of \(k\). The claim does not classify longer cycles or the total number of cycles for a fixed parameter.

## Proof
There are no fixed points: a prime increases by \(k\), while a composite maps to a prime strictly smaller than itself.

For a period-two cycle, two consecutive prime entries are impossible because a prime maps to a larger integer. Hence, after rotation, the cycle has a prime \(p\) followed by the composite \(p+k\). Returning to \(p\) means
\[
P(p+k)=p.
\]
In particular \(p\mid p+k\), so \(p\mid k\). Writing
\[
p+k=p(k/p+1),
\]
the equality \(P(p+k)=p\) is equivalent to \(P(k/p+1)\le p\). This proves necessity, and the same factorization proves sufficiency.

Now suppose an exact period-three cycle exists. Two composite entries cannot be consecutive because every composite maps to a prime, and three consecutive prime entries are impossible because prime steps add the positive quantity \(k\). Thus, after rotation, the cycle has exactly two consecutive primes \(p,q\) and one composite \(c\):
\[
p\longmapsto q=p+k\longmapsto c=p+2k\longmapsto p.
\]
The last arrow gives \(P(c)=p\), hence \(p\mid c=p+2k\) and therefore \(p\mid2k\). If \(p\) were odd, then \(p\mid k\), making \(q=p+k\) a multiple of \(p\) larger than \(p\), contrary to \(q\) being prime. Hence \(p=2\).

It follows that
\[
q=k+2,
\qquad
c=2k+2=2(k+1).
\]
The condition \(P(c)=2\) holds exactly when \(k+1\) is a power of two. Therefore \(k+1=2^a\) and the other prime in the cycle is \(q=2^a+1\). Conversely, if \(k+1=2^a\) and \(2^a+1\) is prime, then the displayed three arrows hold, so this is an exact period-three cycle.

Finally, if \(a=uv\) with \(v>1\) odd, then \(2^a+1=(2^u)^v+1\) is composite. Thus primality of \(2^a+1\) forces \(a\) to be a power of two, giving the Fermat-prime formulation.

## Verification
A standalone checker enumerates all parameters \(1\le k\le500\) and all starting values \(2\le n\le5000\), extracts exact cycles of lengths two and three, and compares them with the two symbolic criteria above. Its packaged output is

`VERIFY_OK k_max=500 n_max=5000 period2_period3_mismatches=0`

This finite computation is regression evidence only. The proof above is independent of the cutoff and establishes the theorem for every \(k\ge1\).

## Relationship to prior work
Das introduced this map, proved eventual periodicity for every orbit, proved that each fixed parameter has only finitely many loops, and gave examples including a period-three loop at \(k=15\). The source also asks about attainable periods and the growth of the number of loops. The checked paper does not state a complete classification of periods two or three.

Dubickas subsequently studied a broader class of bounded iterative sequences and, for the deterministic largest-prime-divisor specialization, expressed the prime subsequence through the recurrence \(p_{i+1}=P(p_i+k)\). Those results give boundedness and eventual periodicity in a wider framework, but the checked text does not give the exact two-cycle criterion or the Fermat-prime classification of three-cycles established here.

Targeted searches using the map definition, the period-two divisibility condition, the period-three power-of-two condition, and the Fermat-prime formulation found no checked source whose statement implies this classification. Two nearby published results concern a small-prime bound for cycles at even parameters and a finite record for the number of loops at one parameter; neither determines the exact short cycles.

## Limitations
Only exact periods two and three are classified. Nothing here settles existence for every longer period, counts all cycles for arbitrary \(k\), or improves the general bounds for long cycles. The originality assessment is relative to the checked literature and databases; an obscure or poorly indexed prior observation of these elementary short-cycle reductions remains possible.

## References
1. A. Das, “A Family of Iterated Maps on Natural Numbers,” arXiv:2312.06629v1, first public 11 December 2023; later published in *Experimental Mathematics*, DOI:10.1080/10586458.2023.2294184.
2. A. Dubickas, “A Class of Bounded Iterative Sequences of Integers,” *Axioms* 13 (2024), 107, DOI:10.3390/axioms13020107.
