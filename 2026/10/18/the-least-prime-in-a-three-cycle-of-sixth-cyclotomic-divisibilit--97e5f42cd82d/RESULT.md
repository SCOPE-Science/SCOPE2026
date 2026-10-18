# The least prime in a three-cycle of sixth-cyclotomic divisibility

## Finding
Put \(F(t)=t^2-t+1=\Phi_6(t)\). On the set of positive primes, draw a directed arrow \(u\to v\) when \(u\ne v\) and \(v\mid F(u)\). Then **the smallest prime that can occur as the least vertex of a directed cycle of length exactly three is \(349\)**. Moreover, the only directed three-cycle whose least vertex does not exceed \(349\), up to cyclic rotation, is
\[
349\longrightarrow121453\longrightarrow9710803\longrightarrow349.
\]

This cycle supplies a squarefree integer with exactly three prime factors,
\[
N=349\cdot121453\cdot9710803=411612748708891,
\]
for which the reciprocal-gcd sum is an integer:
\[
\mathcal H(N):=\sum_{j=1}^{N}\frac1{\gcd(N,j)}
=410433300314317.
\]
The minimum assertion concerns the **least vertex in a directed three-cycle**, not the least integer with three prime factors satisfying reciprocal-gcd integrality.

## Assumptions and scope
All vertices are ordinary positive rational primes. A directed three-cycle consists of three *distinct* primes \(p,q,r\) with \(q\mid F(p)\), \(r\mid F(q)\), and \(p\mid F(r)\). Its least vertex is \(\min\{p,q,r\}\). The statement is unconditional and applies to every such cycle, without restricting its other two primes.

For the minimum proof, it suffices to consider a cycle rotated so that \(p=\min\{p,q,r\}\le349\); then \(q>p\) and \(r>p\). No bound on either \(q\) or \(r\) is added: the divisibility conditions themselves bound the candidates, since \(q\mid F(p)\) and \(r\mid F(q)\).

## Proof
First, a complete finite search can decide whether a three-cycle has least prime at most \(349\). For each prime \(2\le p\le349\), enumerate every prime divisor \(q>p\) of \(F(p)\). For each such \(q\), enumerate every prime divisor \(r>p\) of \(F(q)\), discarding \(r=q\). Check the final condition \(p\mid F(r)\). Every cycle with minimum at most \(349\) appears **exactly once** in this enumeration, since the least prime determines the cyclic rotation uniquely. Conversely, every closing path produced by the enumeration is a three-cycle.

All factor lists are obtained by division by \(2\) and then every odd integer up to the current square root, removing repeated factors before continuing. This detects all prime divisors: a remaining factor greater than one after trial division is prime. Trial division similarly tests every candidate vertex for primality. Thus there is no probabilistic primality assumption and no truncation of the possible \(q\) or \(r\). The executable `verify.py` carries out this exhaustive procedure with only exact integer arithmetic, while `paths.csv` records every resulting two-edge path. There are exactly \(70\) candidate paths with \(p\le349\), of which \(69\) have \(p<349\), and exactly one closes into a three-cycle. The closing path is \((349,121453,9710803)\); none of the first \(69\) closes. The checker separately reconstructs and compares every row of the CSV.

For the exhibited closing path, all three integers are prime by complete trial division and
\[
F(349)=121453,
\qquad F(121453)=7^2\cdot31\cdot9710803,
\]
\[
F(9710803)=349\cdot270199671043.
\]
Therefore all three required arrows exist. In fact, \(349\) admits only \(121453\) as an outgoing prime neighbor, and among the prime factors of \(F(121453)\) only \(9710803\) exceeds \(349\); this independently proves uniqueness at the endpoint. Combining the endpoint cycle with the exhaustive exclusion below it establishes the claimed minimum.

For the arithmetic consequence, elementary divisor grouping gives, for every positive integer \(n\),
\[
\mathcal H(n)
=\sum_{d\mid n}\frac{\varphi(n/d)}d
=\frac1n\sum_{e\mid n}e\varphi(e).
\]
The numerator is multiplicative, and at a prime \(u\) its value is \(1+u(u-1)=F(u)\). Hence for any product \(n=pqr\) of three *distinct* primes,
\[
\mathcal H(n)=\frac{F(p)F(q)F(r)}{pqr}.
\]
Our directed cycle makes the numerator divisible by each of the pairwise coprime primes \(p,q,r\), hence by their product. The exact multiplication gives the displayed value of \(\mathcal H(N)\), completing the proof.

## Verification
From a directory containing both `verify.py` and `paths.csv`, run `python3 verify.py`. Successful execution prints `VERIFICATION_OK` and the counts \(70\), \(1\), and the exact value of \(\mathcal H(N)\). The checker reconstructs the full bounded candidate set rather than merely checking the displayed example, checks primality by exhaustive trial division, verifies the three divisibilities, and checks the integer product and reciprocal-gcd quotient.

An independent calculation using prime factorization and exact modular arithmetic confirmed the same \(70\) candidates and the unique closing path. The proof of *completeness* is the two-stage enumeration argument above together with exhaustive trial division; observing \(70\) test outcomes without that argument would not establish the minimum.

## Relationship to prior work
De Koninck and Letendre [1] study the integer values of this reciprocal-gcd sum and describe prime-factor cycles for the polynomial \(F(t)=t^2-t+1\) as a way to construct further solutions. They prove an upper bound on the counting function and present a small four-prime example, while explicitly asking about the lengths of the prime-factor cycles attainable from a starting prime. Their identities justify the relevance of such cycles; they do not specify the least prime in a three-cycle or the three-prime witness proved here.

OEIS A317480 [2] tabulates initial reciprocal-gcd-integral integers. The publicly displayed terms stop well below the exhibited three-prime integer and do not determine the least vertex of a three-cycle. The published \(\sigma_{2,2}\) prime-pair result [3] instead concerns reciprocal divisibility for \(t^2+t+1=\Phi_3(t)\) and the exact common divisor of two associated values. Its pairwise classification does not imply an existence or minimal-prime statement for three-cycles of \(\Phi_6\).

Targeted searches for the exact prime triple, reciprocal-gcd-integral three-prime witnesses, sixth-cyclotomic directed three-cycles, and stronger classifications did not locate a prior statement implying this minimum. Search non-detection alone is not a proof of novelty.

## Limitations
This result neither classifies cycles whose minimum vertex exceeds \(349\) nor asserts that \(N\) is the least three-prime solution of the integrality problem. It does not establish that infinitely many such cycles or solutions exist. The exact finite certificate proves only the stated minimal vertex cutoff; any broader assertion would require further work. Unindexed earlier computations of these particular primes remain a literature risk.

## References
1. Jean-Marie De Koninck and Patrick Letendre, “The Integer Values of \(\sum_{i=1}^{n}1/\gcd(n,i)\),” arXiv:2610.10572v1, first public version 4 October 2026, §§1, 5, 7. https://arxiv.org/html/2610.10572v1
2. OEIS A317480, “Numbers \(m\) such that \(\sum_{k=1}^{m}1/\gcd(k,m)\) is an integer.” https://oeis.org/A317480
3. “Exact common cyclotomic divisor for \(\sigma_{2,2}\) prime pairs,” published mathematical result concerning reciprocal \(\Phi_3\) prime pairs. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-common-cyclotomic-divisor-for-sigma-2-2-prime-pairs--f65bdfb7afa8/RESULT.md
