# Complete classification of modular periodicity for relatively-prime subset counts

## Finding

Let \(\Phi(n)\) be the number of nonempty subsets \(A\subseteq\{1,\ldots,n\}\) for which \(\gcd(\gcd(A),n)=1\). For every integer \(m\ge1\), the sequence \(\Phi(n)\bmod m\) is eventually periodic **if and only if** \(m\mid6\). In the periodic cases it is identically zero for \(n\ge3\).

More strongly, for each \(m\nmid6\), each proposed period \(T\ge1\), and each threshold \(B\ge1\), there are \(u,v>B\) such that
\[
 u\equiv v\pmod T,\qquad \Phi(u)\not\equiv\Phi(v)\pmod m.
\]
For every odd \(m\ge5\), one can choose \(u=p\) prime and \(v=pq\) a product of distinct primes. When \(4\mid m\), a prime and its square provide witnesses modulo four.

## Assumptions and scope

All integer moduli are positive. The greatest common divisor of a singleton is its member; the empty subset is excluded. Eventual periodicity means the existence of integers \(T\ge1\) and \(N\ge1\) for which \(\Phi(n+T)\equiv\Phi(n)\pmod m\) holds for every \(n\ge N\). The result concerns the generalized subset-counting function \(\Phi\), not Euler's classical totient.

## Proof

**1. Inclusion–exclusion and exact small-support values.** For all \(n\ge1\), Möbius inversion on divisors of \(n\) gives
\[
 \Phi(n)=\sum_{d\mid n}\mu(d)\bigl(2^{n/d}-1\bigr).
\]
For \(n>1\) the constant terms sum to zero, so \(\Phi(n)=\sum_{d\mid n}\mu(d)2^{n/d}\). In particular, for distinct primes \(p,q\),
\[
 \Phi(p)=2^p-2,\qquad
 \Phi(pq)=2^{pq}-2^p-2^q+2,\qquad
 \Phi(p^2)=2^{p^2}-2^p.
\]
Each formula can also be read directly from the exclusion of subsets supported entirely on multiples of the prime factors.

**2. Every divisor of six is eventually periodic.** The displayed sum consists of even terms whenever \(n>1\), giving \(2\mid\Phi(n)\). To establish divisibility by three for \(n\ge3\), note that \(2^k\equiv(-1)^k\pmod3\). If \(n\) is odd, all exponents \(n/d\) are odd, so the Möbius sum reduces to \(-\sum_{d\mid n}\mu(d)=0\). Write an even \(n=2^a w\), with \(w\) odd. If \(a\ge2\), every exponent \(n/d\) for squarefree \(d\mid n\) is even, and the sum reduces to \(\sum_{d\mid n}\mu(d)=0\). If \(a=1\), the inequality \(n\ge3\) forces \(w>1\); pairing squarefree divisors \(e\mid w\) with \(2e\) gives
\[
 \Phi(2w)\equiv \sum_{e\mid w}\mu(e)\bigl(1-(-1)\bigr)
 =2\sum_{e\mid w}\mu(e)=0\pmod3.
\]
Consequently, \(\Phi(n)\equiv0\pmod6\) for all \(n\ge3\), proving eventual constancy for every \(m\mid6\).

**3. Nonperiodicity for any odd modulus greater than three.** Fix odd \(m\ge5\), an arbitrary proposed period \(T\ge1\), and threshold \(B\ge1\). Let \(d\) denote the multiplicative order of \(2\) modulo \(m\). We have \(d\ge3\): orders one and two would respectively force \(m\mid1\) or \(m\mid3\). Since \(d\ge3\), its reduced residue classes contain some \(r\not\equiv1\pmod d\). Dirichlet's theorem yields arbitrarily large primes \(p\equiv r\pmod d\). In particular,
\[
 \Phi(p)=2^p-2\not\equiv0\pmod m,
\]
by the definition of multiplicative order. Put \(L=\operatorname{lcm}(T,d)\). Dirichlet's theorem again supplies a prime \(q\equiv1\pmod L\), distinct from \(p\), with \(pq>B\). Then \(pq\equiv p\pmod T\), while \(2^q\equiv2\pmod m\) and \(2^{pq}\equiv2^p\pmod m\). Therefore
\[
 \Phi(pq)=2^{pq}-2^p-2^q+2\equiv0\pmod m,
\]
which differs from \(\Phi(p)\). Both witness indices exceed \(B\), contradicting any eventual period \(T\).

**4. Moduli divisible by four.** Given \(T,B\), Dirichlet's theorem gives an odd prime \(p>B\) with \(p\equiv1\pmod T\). Hence \(p^2\equiv p\pmod T\), but for every odd prime \(p\),
\[
 \Phi(p)=2^p-2\equiv2\pmod4,\qquad
 \Phi(p^2)=2^{p^2}-2^p\equiv0\pmod4.
\]
Thus the residue sequence is not eventually periodic modulo four or any multiple of four.

**5. Exhaustion of moduli.** If \(m\nmid6\), then either \(4\mid m\), or \(m\) has an odd divisor \(s\ge5\): for \(m\) odd take \(s=m\); otherwise write \(m=2s\) with odd \(s\ge5\). A period modulo \(m\) would yield one modulo \(4\) or \(s\), contradicting step 3 or 4. This completes the proof.

## Verification

The accompanying standard-library `check_phi.py` checks the inclusion-exclusion formulas against direct subsets for the first fourteen indices, verifies residue zero modulo six for the next 118 indices, and constructs 700 explicit prime/semiprime modular witnesses across all odd moduli between five and fifty-nine and periods through twenty-five. It separately checks 25 prime/prime-square witnesses modulo four. These finite checks corroborate the algebra but do not replace Dirichlet's theorem or the argument for arbitrary periods and moduli.

Run `python3 check_phi.py` in the directory containing these files. Its successful output starts with `VERIFY_OK`.

## Relationship to prior work

Pongsriiam's 2013 paper defines the subset counts and asks in Question 3.5 whether the functions \(D(n)\) and \(\Phi(n)\) are periodic modulo a prime. The present result gives an exact classification for \(\Phi(n)\) modulo *every* positive integer, including the exceptional moduli six, four, and nine. It does not answer the corresponding question for \(D(n)\).

Ayad and Kihel previously proved nonperiodicity modulo most primes for the distinct function \(f(n)\), which counts subsets of gcd one. The identity \(\Phi(n+1)=2(f(n+1)-f(n))\) creates a possible indirect route for odd moduli if one assumes a sufficiently strong eventual-nonperiodicity theorem for \(f\); a published statement of ordinary nonperiodicity alone is not identical to eventual nonperiodicity. The present proof is direct and handles arbitrary moduli. Their 2008 paper supplies general subset-counting identities. Pongsriiam's later work settles the separate sign comparison between \(D\) and \(\Phi\), but the examined full text does not state this modular classification. OEIS A038199 records values and an equivalent Möbius formula, not a full modular-periodicity classification.

## Limitations

No statement is proved about the periodicity of \(D(n)\), nor about minimal periods or density of nonzero residues for moduli failing the criterion. Existence of primes in prescribed coprime residue classes uses Dirichlet's theorem, not the finite verifier. Priority remains subject to full-text comparison with the 2009 Ayad–Kihel nonperiodicity paper, whose complete text was not accessible in the examined sources; its stronger possible formulations are a specific residual originality risk.

## References

1. P. Pongsriiam, “Relatively Prime Sets, Divisor Sums, and Partial Sums,” arXiv:1306.4891v1, first public 2013-06-20, Questions 3.1–3.5. https://arxiv.org/pdf/1306.4891
2. M. Ayad and O. Kihel, “On the Number of Subsets Relatively Prime to an Integer,” *Journal of Integer Sequences* 11 (2008), Article 08.5.5. https://cs.uwaterloo.ca/journals/JIS/VOL11/Ayad/ayad3.pdf
3. M. Ayad and O. Kihel, “The Number of Relatively Prime Subsets of {1, 2, ..., n},” *Integers* 9 (2009), A14, 163–166. https://doi.org/10.1515/INTEG.2009.015
4. P. Pongsriiam, “Local Behaviors of the Number of Relatively Prime Sets,” *International Journal of Number Theory* 12 (2016), 1575–1593. https://doi.org/10.1142/S1793042116500962
5. OEIS Foundation, A038199, relatively-prime-subset counts. https://oeis.org/A038199
