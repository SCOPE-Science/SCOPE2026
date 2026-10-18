# Unbounded central arc-sum multiplicity on positive-density cycles

## Finding
Place the labels \(1,2,\ldots,n\) clockwise on a cycle, in that order. A **proper arc** is a nonempty cyclically consecutive set of at most \(n-1\) vertices. Let \(M(n)\) be the number of proper arcs whose sum is half the sum of all labels, namely \(n(n+1)/4\), and put \(M(n)=0\) if the target is nonintegral.

**Theorem.** For every integer \(h\ge1\) there exists a residue class \(c_h\pmod{Q_h}\), with \(Q_h\) divisible by \(4\), such that every sufficiently large positive \(n\equiv c_h\pmod{Q_h}\) satisfies \(M(n)\ge2h\). In particular, the set of such \(n\) has positive lower natural density. Furthermore,
\[
\limsup_{n\to\infty}\frac{M(n)\log\log n}{\log n}\ge1.
\]
The central target is canonical under taking an arc's complement: both arcs then have the same sum. The theorem states that this middle value can have unbounded representation multiplicity, quantitatively and along full arithmetic progressions, even though the unrestricted coverage of cycle sums eventually fails.

## Assumptions and scope
All logarithms are natural. The result is unconditional. It concerns the fixed consecutive ordering, not arbitrary circular permutations. An arc is a vertex set; different starting positions and/or lengths describe distinct arcs. Neither empty nor full-cycle arcs are counted. The positive-density assertion is for **each fixed** \(h\); it does not assert that a single progression works for all thresholds simultaneously. The asymptotic limsup is along an unbounded sequence of cycle lengths.

## Proof
**1. Prime pairs.** Choose any \(h\) pairs of odd primes \((d_i,e_i)\), all \(2h\) primes different, satisfying
\[
\frac34<\frac{e_i}{d_i}<\frac45\qquad(1\le i\le h).
\]
Such choices exist for all \(h\): by the prime number theorem, for a sufficiently large \(X\) the disjoint intervals \((X,1.01X)\) and \((0.77X,0.78X)\) each contain at least \(h\) primes. Pair \(h\) primes from the first interval with \(h\) from the second. Their ratios lie strictly between \(0.77/1.01>3/4\) and \(0.78<4/5\). These ratios are distinct: equality of two reduced fractions of distinct prime numerator and denominator would force identical pairs.

**2. Congruences.** Set \(P=\prod_{i=1}^h d_ie_i\). By the Chinese remainder theorem there exists an integer \(k_0\) modulo \(P\) satisfying simultaneously
\[
 k_0\equiv0\pmod{d_i},\qquad4k_0+1\equiv0\pmod{e_i}
 \quad(1\le i\le h).
\]
Choose any sufficiently large positive \(k\equiv k_0\pmod P\), and write \(n=4k\). The total sum is \(T=n(n+1)/2=2k(4k+1)\); the central target is \(T/2=k(4k+1)\).

**3. Central nonwrapping arcs.** Define, for every \(i\),
\[
 u_i=\frac{2ke_i}{d_i},\qquad v_i=\frac{d_i(4k+1)}{e_i}.
\]
Both are positive integers by the congruences; \(u_i\) is even and \(v_i\) is odd. Moreover \(u_iv_i=T\). Hence
\[
 a_i=\frac{v_i-u_i+1}{2},\qquad
 b_i=\frac{v_i+u_i-1}{2}
\]
are integers, \(b_i-a_i+1=u_i\), and
\[
 \sum_{j=a_i}^{b_i}j
 =\frac{u_i(a_i+b_i)}2
 =\frac{u_iv_i}{2}=\frac{T}{2}.
\]
To check endpoints rather than merely an abstract consecutive-integer identity, put \(t_i=e_i/d_i\). From \(3/4<t_i<4/5\) we have
\[
 \frac{3k}{2}<u_i<\frac{8k}{5},\qquad
 5k+\frac54<v_i<\frac{16k}{3}+\frac43.
\]
Consequently \(a_i>17k/10+9/8>1\), and \(b_i<52k/15+1/6<4k-1\) for all \(k\ge3\). Thus \([a_i,b_i]\) is a proper standard arc strictly inside the labels \(1,\ldots,n\).

**4. Complement arcs and distinctness.** The complement of each interior interval on the cycle is a proper wrapping arc, also of sum \(T/2\). The \(h\) standard arcs have pairwise different lengths \(u_i=2kt_i\) because the ratios \(t_i\) are distinct. Furthermore, \(u_i<n/2\) while all complementary arcs have length \(n-u_i>n/2\). All \(2h\) arcs are therefore distinct. This proves \(M(4k)\ge2h\) for every sufficiently large \(k\equiv k_0\pmod P\). The corresponding cycle lengths form one residue class modulo \(4P\), with natural density exactly \(1/(4P)\), up to finitely many initial terms.

**5. Quantitative limsup.** For large \(h\), choose the primes in step 1 using \(X=h(\log h)^2\). By the prime number theorem, each of the two intervals then contains more than \(h\) primes. These choices satisfy \(d_i,e_i\le1.01X\), so \(P\le(1.01X)^{2h}\). Take the CRT representative \(0\le k_0<P\) and then \(k=k_0+P\), which ensures \(P\le k<2P\) and the endpoint conditions for all sufficiently large \(h\). With \(n_h=4k\),
\[
4P\le n_h<8P,\qquad
\log n_h\le2h\log(1.01h(\log h)^2)+O(1)
 =(2+o(1))h\log h.
\]
Since \(M(n_h)\ge2h\) and \(n_h\to\infty\), monotonicity of \(x\mapsto\log x/\log\log x\) for sufficiently large \(x\) implies
\[
 \frac{\log n_h}{\log\log n_h}\le(2+o(1))h
 \quad\Longrightarrow\quad
 \frac{M(n_h)\log\log n_h}{\log n_h}\ge1-o(1).
\]
This yields the asserted limsup. \(\square\)

## Verification
Run the standalone `verify.py` with Python 3; it uses only the standard library. For four concrete disjoint prime pairs it reconstructs CRT solutions, verifies each endpoint and exact arithmetic-progression sum, and checks that all listed arcs and their complements are distinct. It also brute-counts central arcs for small cycle lengths and compares the direct enumeration with an independent interval/complement count. This finite evidence is supplementary; the infinite claims follow from the CRT construction and the prime number theorem, not from finite experiments.

A small explicit witness uses \((d,e)=(17,13)\), \(k=68\), and \(n=272\). Then \(u=104\), \(v=357\), and the interval \([127,230]\), together with its wrapping complement, both sum to \(18564=T/2\).

## Relationship to prior work
Marotti and Needleman (2026), *Consecutive Cycle Sums*, prove that the consecutive-label cycle is not sum-complete for \(n\ge8\) and study how extra chords affect coverage. Their results concern existence of missing values and graph completion; they do not state a positive-density family with arbitrarily large multiplicity at the central value. The classical consecutive-integer representation theorem counts representations without enforcing the upper endpoint constraint \(b\le n\); by itself it does not imply the present bounded-interval and cyclic-arc statement. Yang and Zhang (2026) optimize the range of **fixed-length** window sums over arbitrary circular permutations, a different invariant. An earlier equivalent conclusion from general divisor-distribution methods cannot be ruled out.

## Limitations
No upper bound for \(M(n)\) is proved, and the lower growth statement is a limsup, not an estimate for all cycle lengths. The arithmetic progressions become sparse as \(h\) grows, so positive density for each fixed threshold does not mean a uniform density bound in \(h\). The result is not about all target sums or an optimal cycle permutation. Originality remains subject to external expert comparison.

## References
1. Jessica Marotti and Jonathan Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1 (first public 2026-10-06), https://arxiv.org/html/2610.08889v1 .
2. Yaoran Yang and Yutong Zhang, *Optimal Range of k-Consecutive Sums on a Circle for n = 2k + 1 and n = k² + 1*, Mathematics 14 (2026), article 1252, https://doi.org/10.3390/math14081252 .
3. Classical prime number theorem and Chinese remainder theorem; classical consecutive-integer sum/divisor correspondence (see the historical discussion and references in [1]).
