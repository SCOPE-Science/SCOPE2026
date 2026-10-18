# Irrational record densities in every reduced squarefree progression

## Finding
Let \(R\) be the record-value set of the greedy coprime permutation with initial values \(f(1)=1\), \(f(2)=3\), and subsequent values the least as-yet-unused positive integer coprime to the previous value. For **every** squarefree integer \(m\ge2\) and every integer \(a\) with \(\gcd(a,m)=1\), the natural density
\[
\delta_{m,a}=\lim_{X\to\infty}\frac{\#\{r\in R: r\le X,\ r\equiv a\pmod m\}}{X}
\]
exists and is **irrational** (and consequently strictly positive). In particular, the unrestricted density of the record set is irrational, by taking \(m=2\), \(a=1\). The assertion includes infinitely many progressions and does not assume unproved hypotheses on the primes.

## Assumptions and scope
Here the positive integers include \(1\), and a record is a value \(f(t)\) at a step \(t>3\) where \(f(t)-f(t-1)>1\); the initial value \(3\) may be included without affecting densities. Equivalently, up to this finite convention, the records are generated increasingly from \(r_1=3\) by
\[
r_{j+1}=r_j+\ell(r_j-1)-1,
\]
where \(\ell(u)\) is the least prime not dividing the positive integer \(u\). Every prime at least \(3\) is a record and every record is odd. These facts and the primorial translation theorem are established in the source literature.

Let \(p_n\) denote the \(n\)-th prime, \(P_n=\prod_{j=1}^{n}p_j\), and choose any \(n_0\ge3\) such that \(m\mid P_{n_0}\), possible because \(m\) is squarefree. For \(n\ge n_0\) define
\[
w_n(a)=\#\{r\in R:p_{n+1}\le r\le P_n+1,\ r\equiv a\pmod m\},
\qquad s_n(a)=\#\{r\in R:p_n\le r<p_{n+1},\ r\equiv a\pmod m\}.
\]
The result is about ordinary natural densities among **all** integers, not merely limits along primorial subsequences.

## Proof
**1. Residue-preserving primorial recursion.** The established primorial-copy theorem states that, through the interval ending at \(P_{n+1}+1\), successive blocks are copies of the preceding record block translated by integer multiples of \(P_n\), with the initial short prime interval deleted. Because \(m\mid P_n\), those translations preserve the residue \(a\pmod m\). Thus the exact source recurrence holds class by class:
\[
w_{n+1}(a)=p_{n+1}w_n(a)-s_{n+1}(a)\qquad(n\ge n_0).
\]
It follows that \(\rho_n(a):=w_n(a)/P_n\) is decreasing, nonnegative, and hence converges to
\[
\rho(a)=\frac{w_{n_0}(a)}{P_{n_0}}-\sum_{k=n_0+1}^{\infty}\frac{s_k(a)}{P_k}.
\]
All terms of this series are exact integers divided by primorials. It converges absolutely: all records are odd, so \(0\le s_k(a)\le (p_{k+1}-p_k)/2<p_k/2\), the strict inequality following from Bertrand's postulate.

**2. Full natural density.** We spell out why the preceding limit is not just a subsequence density. Given large \(X\), choose \(n\) with \(P_n\le X<P_{n+1}\). The same primorial-copy theorem partitions the records in this range into translated length-\(P_n\) blocks, each with the pattern of \(w_n(a)\) residues; the first boundary interval contains fewer than \(p_{n+1}\) integers. Each such pattern, by the exact recursion, consists of \(p_n\) consecutive copies of the length-\(P_{n-1}\) pattern with at most \(s_n(a)\) initial deletions. These statements remain valid for prefixes: counting the last incomplete length-\(P_{n-1}\) subblock incurs an error at most \(P_{n-1}\), and the initial deleted/boundary intervals of all full length-\(P_n\) blocks together incur at most a constant times \(p_{n+1}^2\) errors. Hence, uniformly for \(P_n\le X<P_{n+1}\),
\[
\left|\#\{r\in R:r\le X,\ r\equiv a\pmod m\}-X\rho_{n-1}(a)\right|
=O(P_{n-1}+p_{n+1}^{2}).
\]
The implied constant is absolute for fixed \(m\). Since \(X\ge P_n=p_nP_{n-1}\), \(p_n\to\infty\), and \(p_{n+1}^{2}/P_n\to0\), division by \(X\) proves that the natural density exists and equals \(\rho(a)\). This is the residue-class refinement of the block-counting argument that proves existence of the unrestricted density in the source.

**3. The rational-denominator obstruction.** Define the strictly positive tail, for each \(n\ge n_0\),
\[
T_n=P_n(\rho_n(a)-\delta_{m,a})
=\sum_{k=n+1}^{\infty}\frac{s_k(a)}{p_{n+1}p_{n+2}\cdots p_k}.
\]
Dirichlet's theorem gives infinitely many primes congruent to \(a\pmod m\), each of which is a record. Therefore infinitely many of the \(s_k(a)\) are positive, so \(T_n>0\) for every \(n\). For \(k\ge n+1\), the oddness bound and Bertrand's inequality give
\[
0<T_n\le\frac{p_{n+2}-p_{n+1}}{2p_{n+1}}+
\frac{1}{2(p_{n+1}-1)}.
\]
The first term tends to zero because the prime number theorem implies \(p_{n+2}/p_{n+1}\to1\); the second visibly tends to zero. Thus \(T_n\to0\) from above.

Suppose \(\delta_{m,a}=u/v\) for integers \(u\) and \(v>0\). Then
\[
vT_n=vw_n(a)-uP_n
\]
is a positive integer for **every** \(n\ge n_0\). Yet \(vT_n\to0\), an impossibility. Hence \(\delta_{m,a}\) is irrational. Since it is a limit of nonnegative frequencies, it must then be positive. This proves all assertions.

## Verification
A standalone exact-integer program, `verify.py`, generates the records from the least-missing-prime recurrence through \(P_6+1=30031\). It checks the residue-preserving block recurrence for all reduced classes of moduli \(2,3,5,6,7,10,11,15\) whenever these moduli divide the applicable primorial and the required blocks have been generated (90 exact identities). It evaluates rational truncations for both reduced classes modulo \(3\). These are checks of finite instances only; the infinite assertions follow from the primorial-copy theorem, Dirichlet's theorem, the prime number theorem, and the tail contradiction in the proof.

## Relationship to prior work
Basistha and Ionascu establish the record recursion, primorial copying, and the existence of the **unrestricted** density (Theorems 2.9 and 2.12 of the 2023 preprint, corresponding to Theorems 2.19 and 2.24 in the published version). Their results do not determine whether that density is rational and do not give irrationality of all reduced-class densities. The present argument preserves residue classes through each primorial translation and uses positive prime occurrences to show that the rational approximants have nonzero tails tending to zero after clearing a primorial denominator. Earlier calculations of individual residue classes, by themselves, do not imply these irrationality conclusions.

## Limitations
No effective irrationality measure or transcendence statement is proved. Squarefree moduli and reduced residue classes are required; the theorem does not classify densities of non-coprime classes or arbitrary nonsquarefree moduli. The finite computations do not establish the infinite statement and do not supply independent mathematical certification. The literature comparison cannot exclude an unindexed equivalent proof.

## References
1. A. K. Basistha and E. J. Ionascu, *A special sequence and primorial numbers*, arXiv:2302.02838, first public version 2023-02-06, especially §§1–2, Theorems 2.9 and 2.12. https://arxiv.org/pdf/2302.02838
2. A. K. Basistha and E. J. Ionascu, *Permutations of \(\mathbb N\) and primorial numbers*, *Revue Roumaine de Mathématiques Pures et Appliquées* (2025), DOI 10.59277/RRMPA.2025.235.255, especially Theorems 2.19 and 2.24. https://imar.ro/journals/Revue_Mathematique/pdfs/2025/3-4/4.pdf
3. OEIS A261271, record sequence and least-missing-prime recurrence. https://oeis.org/A261271
