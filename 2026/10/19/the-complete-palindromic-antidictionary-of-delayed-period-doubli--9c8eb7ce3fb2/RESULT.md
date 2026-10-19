# The complete palindromic antidictionary of delayed period-doubling substitutions

## Finding
For each integer \(q\ge3\), define the binary \(q\)-uniform substitution
\[\mu_q(0)=0^{q-1}1,\qquad \mu_q(1)=0^q,\qquad d^{(q)}=\lim_{m\to\infty}\mu_q^m(0).\]
A **minimal absent factor** is a finite binary word which does not occur contiguously in \(d^{(q)}\), although every proper contiguous factor does.

Let \(Z_q=0^{q-1}\), \(T_q(u)=\mu_q(u)Z_q\), and let \(b_t=1\) for even \(t\) and \(b_t=0\) for odd \(t\). Then the complete minimal absent factor set is the disjoint union
\[
\{11\}\;\cup\;\{b_tT_q^t(0^j)b_t:\ t\ge0,\ 1\le j\le2q-3,\ j\ne q-1\}\;\cup\;\{0T_q^t(0^{2q-2})0,\;1T_q^t(0^{2q-2})1:\ t\ge0\}.
\]
Every listed absent word is a palindrome, and all minimal absent factors are listed. At each scale \(t\), there are exactly \(2q-2\) different words, with lengths \(q^t(j+1)+1\) for the appropriate seed \(j\). The ordinary generating series of their counts by length is
\[
F_q(z)=z^2+\sum_{t\ge0}\left(\sum_{\substack{1\le j\le 2q-3\\j\ne q-1}}z^{q^t(j+1)+1}+2z^{q^t(2q-1)+1}\right).
\]
This determines the complete forbidden basis of the factor language: a finite binary word occurs in \(d^{(q)}\) if and only if it contains none of the listed minimal absent words.

## Assumptions and scope
The alphabet is \(\{0,1\}\), lengths refer to contiguous factors, and \(q\) ranges over **all integers at least three**. The morphism is primitive, because \(\mu_q^2\) maps both symbols to words containing both symbols; its fixed point is uniformly recurrent. The familiar case \(q=2\) is an already studied period-doubling word and is not asserted as an original specialization. The parameter \(q\) is a substitution block length, not an alphabet size.

For any finite factor \(u\), define its simultaneous extension set
\[E(u)=\{(a,b)\in\{0,1\}^2:aub\text{ occurs in }d^{(q)}\}.\]
A factor is **bispecial** if it has both left extensions and both right extensions. We include the empty word \(\varepsilon\) as a possible core.

## Proof
**1. Exact zero-run geometry.** Every occurrence of \(1\) is at an index congruent to \(q-1\pmod q\), and
\[d^{(q)}_{qi+r}=0\ (0\le r\le q-2),\qquad d^{(q)}_{qi+q-1}=1-d^{(q)}_i.\]
There is no factor \(11\), since each substitution block begins with \(q-1\) zeros. Both \(00\) and \(010\) occur in the fixed point. Thus consecutive zeros of the *preimage* are separated by distances one or two; consequently consecutive ones in the image are separated by zero runs of lengths exactly \(q-1\) and \(2q-1\), and both lengths occur. No longer zero run occurs.

For the empty core, \(E(\varepsilon)=\{(0,0),(0,1),(1,0)\}\). For each nonempty all-zero bispecial core \(0^j\), the exact extension sets follow from the two run lengths. A run of \(L\) zeros supplies extensions \((0,0)\) if \(L\ge j+2\), supplies each of \((0,1),(1,0)\) if \(L\ge j+1\), and supplies \((1,1)\) precisely if \(L=j\). Therefore \(0^j\) is bispecial exactly when \(1\le j\le2q-2\). On these cores,
\[
E(0^j)=\begin{cases}
\{(0,0),(0,1),(1,0),(1,1)\},&j=q-1,\\
\{(0,1),(1,0)\},&j=2q-2,\\
\{(0,0),(0,1),(1,0)\},&\text{all remaining }1\le j\le2q-3.
\end{cases}
\]
These observations also prove that the empty core contributes exactly the absent word \(11\).

**2. Unique desubstitution of longer bispecial factors.** Let \(v\) be bispecial and contain a \(1\). As every \(1\) in the fixed point has the same residue \(q-1\), *all occurrences of \(v\) start at the same residue modulo \(q\)*. A left extension \(1v\) exists and forces this starting residue to be zero. A right extension \(v1\) exists and forces \(|v|\equiv q-1\pmod q\). Hence, for a uniquely determined nonempty finite factor \(u\),
\[v=\mu_q(u)0^{q-1}=T_q(u).\]
The letter just before \(v\) and the letter just after \(v\), for an occurrence corresponding to \(aub\), are respectively \(1-a\) and \(1-b\). Uniform recurrence ensures that every two-sided extension of \(u\) occurs away from the left endpoint. Thus **exactly**
\[E(T_q(u))=\{(1-a,1-b):(a,b)\in E(u)\}.\]
In particular, \(T_q(u)\) is bispecial if and only if \(u\) is bispecial, and its missing extension pairs are the bitwise complements of the missing pairs of \(u\). Conversely every bispecial \(u\) contains \(0\), so \(T_q(u)\) contains a \(1\) and the equality applies. Repeatedly desubstituting any nonzero bispecial factor must eventually reach an all-zero bispecial core, since each step decreases its length. Consequently the complete list of nonempty bispecial cores is
\[T_q^t(0^j),\quad t\ge0,\quad1\le j\le2q-2.\]

**3. From extension deficits to minimal absence.** A binary word of length at least two is minimal absent precisely when it has the form \(aub\), where \(u\) is a bispecial factor and \((a,b)\notin E(u)\). Indeed the prefix \(au\) and suffix \(ub\) must occur, which supplies both left and right extensions, while \(aub\) is absent; conversely this condition makes both maximal proper factors occur, hence every proper factor occurs. For the empty core this yields \(11\). The zero-run extension table yields no absent word at \(j=q-1\), one absent word \(10^j1\) at every other \(j\le2q-3\), and two at \(j=2q-2\). Applying the exact complement rule at each \(T_q\)-step yields the stated two families with parity-dependent endpoints. This proves exhaustiveness and absence.

**4. Distinctness, palindromes, and lengths.** The morphism-with-boundary map can be written
\[T_q(u_1\cdots u_m)=Z_q(1-u_1)Z_q(1-u_2)\cdots Z_q(1-u_m)Z_q.\]
It preserves reversal: \(T_q(\operatorname{rev}u)=\operatorname{rev}(T_q(u))\). Each seed is palindromic, and both endpoint symbols match, so every minimal absent word is palindromic. The exact length recurrence is \(|T_q(u)|=q|u|+q-1\), giving \(|T_q^t(0^j)|=q^t(j+1)-1\). Hence its absent superwords have length \(q^t(j+1)+1\). The permitted values of \(j+1\) lie in \([2,2q-1]\) but exclude its sole multiple of \(q\), namely \(q\); therefore no two scale-seed pairs have the same length. Within the exceptional seed \(j=2q-2\), the two endpoint choices differ. The count is \((2q-4)+2=2q-2\) words at each scale. The generating series follows.

**5. Forbidden basis of the language.** Every nonfactor has a length-minimal nonfactor among its contiguous subwords. Such a subword is minimal absent, so the catalog characterizes the full factorial language by pattern avoidance.

## Verification
The accompanying standalone program `verify.py` creates two independent finite prefixes: one by iterating the substitution, the other directly using the base-\(q\) digit recursion. It verifies agreement on the first \(25{,}000\) symbols for each \(q=2,\ldots,9\). For each such parameter, it enumerates every length-\(n\) factor of the generated prefix for \(1\le n\le75\), derives the observed minimal absent factors from their maximal proper factors, and compares the result with the theorem's predicted list. It terminates with `VERIFY_OK q=2..9 independent_generators_N25000 full_absent_factor_enumeration_lengths_1..75`. These finite checks do not establish completeness in the infinite word; that assertion follows from Steps 1–4.

Run `python3 verify.py` using Python 3 and its standard library. No external dependencies, files, or numerical solvers are required.

## Relationship to prior work
Klouda's 2012 theorem supplies a general method to generate bispecial factors of circular non-pushy D0L systems. That is algorithmic prior coverage of a broad class of morphisms, but the inspected paper does not state the concrete \(q\)-uniform substitution, the seed deficit table, the palindromic forbidden basis, or the explicit count of \(2q-2\) words per scale; those statements require the present extension computation.

Cassaigne, Fici, Sciortino, and Zamboni (2014) define minimal forbidden factor complexity and study cyclic complexity, including the classical period-doubling word, but do not compute this family of antidictionaries. Košík and Starosta (2019), Proposition 13, give the bispecial desubstitution structure for the **classical \(q=2\)** period-doubling morphism. That is a substantively related special case and is excluded from the novelty assertion. Their paper does not analyze the multi-seed extension table for every \(q\ge3\). Related generalized period-doubling sequences defined on \(q\)-symbol alphabets are different objects from the binary morphisms considered here.

## Limitations
The result concerns this one explicitly defined binary substitution family and its entire infinite fixed-point language. It does not claim a formula for arbitrary primitive substitutions or alphabet-generalized period-doubling systems. The full original-literature record may contain an equivalent calculation under a different description; the originality assessment is limited to the specified searches and inspected full-text material. The independent scientific audit has not been performed. All-length correctness rests on the proof rather than on bounded enumeration.

## References
1. K. Klouda, *Bispecial factors in circular non-pushy D0L languages*, arXiv:1201.1186 (first submitted 2012-01-05), especially the method of bispecial-generating maps.
2. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (first submitted 2014-02-24), Definitions and Section 5.
3. V. Košík, Š. Starosta, *On Substitutions Closed Under Derivation: Examples*, arXiv:1907.05751 (first submitted 2019-07-12), Section 5 and Proposition 13.
