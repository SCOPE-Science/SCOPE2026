# Exact value-frequency law for consecutive arithmetic-progression LCM quotients

## Finding
For integers \(k\ge0\), \(a\ge1\), \(b\ge0\), and \(n\ge1\), define the positive integer
\[
G_{k,a,b}(n)=\frac{\prod_{i=0}^{k}(b+a(n+i))}{\operatorname{lcm}_{0\le i\le k}(b+a(n+i))}.
\]
This theorem gives the **complete value distribution**, rather than only the previously known period, for every \(k,a,b\). Let \(d=\gcd(a,b)\), \(A=a/d\), \(B=b/d\), and \(N=k+1\). For each prime \(p\le k\) with \(p\nmid A\), set
\[
e_p=\max\{j:p^j\le k\},\qquad C_p=\sum_{j=1}^{e_p}\left(\left\lfloor\frac{N}{p^j}\right\rfloor-1\right).
\]
Write \(N=\sum_{j\ge0}d_{p,j}p^j\), with \(0\le d_{p,j}<p\). Define
\[
M_{p,h}(z)=\begin{pmatrix}p-h&hz\\p-h-1&(h+1)z\end{pmatrix},\quad
F_{p,k}(z)=\frac{z^{C_p}}{p^{e_p}}\begin{pmatrix}1&0\end{pmatrix}
\left(\prod_{j=0}^{e_p-1}M_{p,d_{p,j}}(z)\right)
\begin{pmatrix}1\\1\end{pmatrix}.
\]
The matrix product is ordered by increasing \(j\); empty products equal the identity. Then the multivariate polynomial
\[
\boxed{\quad\mathcal F_{k,A}(\{z_p\})=\prod_{\substack{p\le k\\p\text{ prime},\ p\nmid A}}F_{p,k}(z_p)\quad}
\]
is exactly the joint probability generating function for the prime valuations of \(G_{k,a,b}(n)/d^k\), with \(n\) uniformly distributed over one complete period. In particular, the coefficient of \(\prod_p z_p^{u_p}\) is the precise fraction of \(n\) for which
\[
G_{k,a,b}(n)=d^k\prod_{\substack{p\le k\\p\nmid A}}p^{u_p}.
\]
All other positive values have frequency zero. The smallest period is
\[
P=\prod_{\substack{p\le k,\ p\nmid A\\p^{e_p}\nmid N}}p^{e_p}.
\]
For every real \(s\), the exact mean of the \(s\)-th power over this period, also its natural-density mean, is
\[
\frac1P\sum_{n=1}^{P}G_{k,a,b}(n)^s=d^{ks}\prod_{p\le k,\ p\nmid A}F_{p,k}(p^s).
\]
Finally the normalized value law is **independent of \(B\)**. It equals the law of \(G_{k,1,0}\) after deleting from each value all prime-power factors belonging to primes dividing \(A\). In particular, when \(\gcd(A,\operatorname{lcm}(1,\ldots,k))=1\), the normalized law is precisely that of \(G_{k,1,0}\).

## Assumptions and scope
All variables are integers with the indicated ranges, with \(\gcd(0,a)=a\). The empty least common multiple in the last statement for \(k=0\) is interpreted as \(1\). The sample space is a uniform residue class modulo the **minimal positive period** of the positive-integer sequence; periodicity makes this equal to natural frequencies. Variables \(z_p\) are commuting formal indeterminates. Coefficients of \(\mathcal F_{k,A}\) are rational nonnegative and sum to one. The theorem is an exact counting statement, not a claim of statistical independence across nonuniform or bounded-incomplete samples.

## Proof
1. Scaling every progression term by \(d\) scales their product by \(d^{k+1}\) and their least common multiple by \(d\), so \(G_{k,a,b}=d^kG_{k,A,B}\). If \(p\mid A\), then \(p\nmid B\) by coprimality; none of the normalized progression terms is divisible by \(p\).

2. Fix \(p\nmid A\). Let \(m_j\) be the number of terms divisible by \(p^j\). By subtracting the largest valuation from their valuation sum,
\[
\nu_p(G_{k,A,B}(n))=\sum_{j\ge1}\max(0,m_j-1).
\]
For \(j>e_p\), there is at most one multiple of \(p^j\) among the \(k+1\) progression terms, since the difference of two such terms is \(A(i-i')\) with \(0<|i-i'|\le k<p^j\). For \(1\le j\le e_p\), there is at least one; here \(m_j-1\ge0\). Put \(x\equiv n+BA^{-1}-1\pmod{p^{e_p}}\), where the inverse of \(A\) is taken modulo \(p^{e_p}\). Multiplication by \(A^{-1}\) converts the progression divisibility test into an ordinary consecutive-integer test, so
\[
m_j=\left\lfloor\frac{N}{p^j}\right\rfloor+c_j(x),
\quad c_j(x)=\left\lfloor\frac{(x\bmod p^j)+(N\bmod p^j)}{p^j}\right\rfloor\in\{0,1\}.
\]
The integers \(c_j\) are exactly the successive carry bits in base-\(p\) addition of \(N\) to \(x\). Therefore \(\nu_p(G_{k,A,B}(n))=C_p+\sum_{j=1}^{e_p}c_j(x)\).

3. Consider uniformly distributed base-\(p\) digits of \(x\bmod p^{e_p}\). If the incoming carry is zero and the corresponding digit of \(N\) equals \(h\), exactly \(p-h\) input digits give outgoing carry zero, and \(h\) give outgoing carry one. If the incoming carry is one, these numbers are \(p-h-1\) and \(h+1\). Weight outgoing carry one by \(z\); this is precisely the matrix \(M_{p,h}(z)\). Starting at carry zero and summing both possible final carries proves the displayed formula for \(F_{p,k}\). Its normalization at \(z=1\) is one because every matrix has row sum \(p\).

4. The local valuation depends only on \(n\bmod p^{e_p}\). If \(p^{e_p}\mid N\), the relevant digits of \(N\) vanish; all carry bits vanish and the local valuation is constant. Otherwise \(c_{e_p}(x)\) is the indicator of a single nonempty proper cyclic interval of residues modulo \(p^{e_p}\). This indicator has full minimal period \(p^{e_p}\): a proper nonempty cyclic interval is not invariant under a nontrivial rotation. Since \(\sum_{j<e_p}c_j\) is periodic modulo \(p^{e_p-1}\), the complete local valuation cannot have period \(p^{e_p-1}\). Thus its least period is \(p^{e_p}\). The valuation at each distinct prime has a period that is a power of that prime; the least common period of the integer-valued quotient is their product \(P\), recovering the established period formula.

5. For each active prime, the map \(n\mapsto n+BA^{-1}-1\) is a permutation modulo \(p^{e_p}\). The Chinese remainder theorem makes these residue classes jointly independent when \(n\) is uniform modulo \(P\). Thus their probability generating functions multiply; constant local factors are included as well. Every value of \(G_{k,A,B}\) has no prime factor greater than \(k\), by step 2. This proves the coefficient statement, moment identity, and the independence of \(B\). Comparing the same local laws with those for \(A=1,B=0\) proves the prime-deletion universality. All arguments include \(k=0\), for which \(G=1\).

## Verification
The accompanying `verify_frequency.py` constructs each local carry matrix by exact integer counts, computes the complete value histogram without enumerating the full period in its main method, and independently compares it with direct products and least common multiples on every residue of the minimal period for \(k=0,\ldots,15\), \(a=1,\ldots,8\), and \(b=0,\ldots,7\), namely \(1024\) parameter triples. The tests include non-coprime \(a,b\), constant local factors, and cancellation at \(p^{e_p}\mid k+1\). For \(k=6,a=1,b=0\), the minimal period is \(60\) and the exact value-frequency pairs are \((12,6),(24,6),(36,3),(48,12),(60,4),(72,3),(120,4),(144,6),(180,2),(240,8),(360,2),(720,4)\); their frequencies sum to \(60\). The proof, not enumeration, establishes the all-parameter claim.

## Relationship to prior work
Hong and Qian introduced the arithmetic-progression quotient, derived its prime-local valuation count in Eq. (3.2), and determined its least period in Theorem 1.2 (arXiv:0903.0530). Ji and Ji established analogous periodicity for much more general polynomial progressions and also recovered the linear least-period formula (arXiv:0903.1162). Farhi and Kane earlier determined the ordinary consecutive-integer least period (arXiv:0808.1507). These are the direct starting points, not claimed as new. The present theorem concerns the full joint **frequency distribution of values**, an explicit carry-transfer evaluation and the progression-independence law; no equivalent statement was located in the inspected relevant sections of the two accessible primary papers. Existing local valuation identities provide an important starting point and reduce the conceptual distance of the extension.

## Limitations
No claim is made that individual prime valuations are independent when sampling a non-complete period, nor that this compact polynomial is already listed in published literature. The period computation is previously known and is included for self-containment only. The all-value distribution is a mathematically direct but non-identical strengthening of a known valuation-count formula. An unindexed equivalent generating function or pre-existing carry-based treatment may exist. Independent mathematical audit and exhaustive publication-priority verification remain unperformed.

## References
- S. Hong and G. Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530 (first submitted 2009-03-03), especially Theorem 1.2 and Eq. (3.2), https://arxiv.org/abs/0903.0530.
- Q.-Z. Ji and C.-G. Ji, *On the periodicity of some Farhi arithmetical functions*, arXiv:0903.1162 (submitted 2009-03-06), https://arxiv.org/abs/0903.1162.
- B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507 (submitted 2008-08-11), https://arxiv.org/abs/0808.1507.
