# Parity rigidity and exact first-defect laws for central-binomial quadratic characters

## Finding
Let \(p\) be an odd prime, let \(\chi_p\) denote its Legendre character extended by \(\chi_p(0)=0\), and put \(B(n)=\binom{2n}{n}\). Say that \(p\) is *parity-rigid* if
\[
\chi_p(B(n))=(-1)^n\qquad\text{for every }n\ge0\text{ with }p\nmid B(n).
\]
The following three assertions form one classification and its quantitative consequences.

**Rigidity and sharp first defect.** The parity-rigid odd primes are exactly \(3\) and \(5\). For each odd prime \(p>5\), the integer
\[
j_p=\min\{n\ge1:p\nmid B(n),\ \chi_p(B(n))\ne(-1)^n\}
\]
exists and satisfies \(1\le j_p\le5\). Writing \(\epsilon_a=\chi_p(a)\), its exact value for \(p\ge11\) is
\[
j_p=\begin{cases}
1,&\epsilon_2=+1,\\
2,&\epsilon_2=-1,\ \epsilon_3=+1,\\
3,&\epsilon_2=\epsilon_3=-1,\ \epsilon_5=+1,\\
4,&\epsilon_2=\epsilon_3=\epsilon_5=-1,\ \epsilon_7=-1,\\
5,&\epsilon_2=\epsilon_3=\epsilon_5=-1,\ \epsilon_7=+1.
\end{cases}
\]
For \(p=7\) one has \(j_p=1\). The bound \(5\) is attained by infinitely many primes.

**Density of first defects.** Among primes, the natural densities of the five cases \(j_p=1,2,3,4,5\), respectively, are exactly
\[
\frac12,\quad\frac14,\quad\frac18,\quad\frac1{16},\quad\frac1{16}.
\]
The finite exceptional set \(\{2,3,5,7\}\) does not affect these densities.

**Quantitative exceptional family.** For every \(L\ge1\), count residues of
\[
A(n)=\binom{4n+2}{2n+1}\pmod 5,
\qquad 0\le n\le\frac{5^L-3}{2}.
\]
Let \(N_r(L)\) count those \(n\) giving residue \(r\). Then \(N_1(L)=N_4(L)=0\) and
\[
N_0(L)=\frac{5^L-3^L}{2},\qquad
N_2(L)=\frac{3^L-1+2\operatorname{Im}(2+i)^L}{4},\qquad
N_3(L)=\frac{3^L-1-2\operatorname{Im}(2+i)^L}{4}.
\]
In particular the exact imbalance is \(N_2(L)-N_3(L)=\operatorname{Im}(2+i)^L\); among nonzero residues the two possibilities become asymptotically equiprobable, with error of order \((\sqrt5/3)^L\).

## Assumptions and scope
All primes in the rigidity theorem are odd. The Legendre character is applied only to nonzero binomial residues in the definition of rigidity and first defect, so zeros have no assigned sign. The first-defect formulas involving \(\epsilon_3,\epsilon_5,\epsilon_7\) are asserted for \(p\ge11\), where all five tested binomial coefficients are nonzero modulo \(p\). The last statement counts exactly the finite interval displayed, not arbitrary consecutive blocks or a distribution over primes.

## Proof
**1. Exceptional rigidity.** Lucas's theorem states that if \(n\) has base-\(p\) digits \(d_i\), then \(p\nmid B(n)\) if and only if each digit satisfies \(2d_i<p\), in which case
\[
B(n)\equiv\prod_i\binom{2d_i}{d_i}\pmod p.
\]
For \(p=3\), the allowed digits are \(0,1\), giving Legendre signs \(+1,-1\); for \(p=5\), the allowed digits are \(0,1,2\), giving signs \(+1,-1,+1\). In both cases the local sign is \((-1)^{d_i}\). Since \(p\) is odd, \(n\equiv\sum_i d_i\pmod2\); multiplying signs proves rigidity for every allowed \(n\).

**2. First defect.** The first five positive central-binomial coefficients factor as
\[
B(1)=2,\quad B(2)=2\cdot3,\quad B(3)=2^2\cdot5,\quad
B(4)=2\cdot5\cdot7,\quad B(5)=2^2\cdot3^2\cdot7.
\]
For \(p\ge11\) they are all units modulo \(p\). Comparing their characters successively with \(-1,+1,-1,+1,-1\) proves the five branches: after the first three signs agree, necessarily \(\epsilon_2=\epsilon_3=\epsilon_5=-1\); the fourth agrees precisely when \(\epsilon_7=+1\), at which point the fifth has sign \(+1\) instead of \(-1\). Thus no prime \(p\ge11\) is rigid and \(j_p\le5\). For \(p=7\), \(\chi_7(2)=+1\) already contradicts the required sign at index one. This proves the complete rigidity classification.

**3. Prime densities and sharpness.** For \(p>7\), quadratic reciprocity gives
\[
\left(\frac2p\right)=(-1)^{(p^2-1)/8},\quad
\left(\frac3p\right)=(-1)^{(p-1)/2}\left(\frac p3\right),\quad
\left(\frac5p\right)=\left(\frac p5\right),\quad
\left(\frac7p\right)=(-1)^{(p-1)/2}\left(\frac p7\right).
\]
Thus the four signs depend only on \(p\bmod840\). Among the \(\varphi(840)=192\) units modulo \(840\), each prescribed four-sign pattern occurs in exactly \(12\) residue classes: given the sign of \(2\), there are two eligible classes modulo \(8\); given that choice, the required sign for \(3\) fixes one class modulo \(3\); the sign for \(5\) allows two classes modulo \(5\); and the sign for \(7\) allows three classes modulo \(7\). The Chinese remainder theorem multiplies these counts to \(2\cdot1\cdot2\cdot3=12\). Dirichlet's theorem implies natural density \(1/16\) for each pattern. Summing the appropriate \(8,4,2,1,1\) patterns gives the five densities. In particular the last class has positive density, so the cutoff \(5\) is sharp at infinitely many primes.

**4. Exceptional residue frequencies.** Put \(m=2n+1\); the stated interval is equivalent to the odd integers \(1\le m<5^L\). Lucas's theorem makes \(\binom{2m}{m}\) nonzero modulo \(5\) precisely when all \(L\) base-\(5\) digits of \(m\) belong to \(\{0,1,2\}\). Each digit equal to \(1\) contributes a factor \(2\), while digits \(0,2\) contribute \(1\). If \(t\) digits equal \(1\), the residue is \(2^t\pmod5\); because \(m\) is odd, \(t\) is odd. Consequently the only nonzero residues are \(2\) for \(t\equiv1\pmod4\) and \(3\) for \(t\equiv3\pmod4\). The polynomial \((2+z)^L\) counts digit strings by \(t\). Its odd coefficients total \((3^L-1)/2\), and the difference of the \(t\equiv1\pmod4\) and \(t\equiv3\pmod4\) coefficients is \(\operatorname{Im}(2+i)^L\). Solving for the two counts gives \(N_2,N_3\); subtracting from the total \((5^L-1)/2\) odd values gives \(N_0\). Finally \(|\operatorname{Im}(2+i)^L|\le 5^{L/2}\) gives the stated relative decay.

## Verification
A standalone Python checker `verify.py` independently (a) computes first discrepancies using direct integer binomial coefficients for every odd prime below \(5000\), (b) checks the character law by direct binomial coefficients for \(1400\) exceptional-prime indices, (c) checks the \(16\) quadratic-character patterns among coprime classes modulo \(840\), and (d) independently enumerates every shifted index for \(1\le L\le6\), including all \(7812\) cases in the largest block, against the exact closed forms. All checks passed. This finite verification is corroboration, not the proof of the infinite assertions; the proof uses Lucas's theorem, quadratic reciprocity, CRT and Dirichlet's theorem.

## Relationship to prior work
Guo and Krattenthaler, arXiv:1301.7651, Conjecture 7.1 (first public release 2013-01-31), proposed full residue coverage for broad shifted binomial families; it is not a theorem establishing the character law. Vsemirnov, *On a conjecture of Guo and Krattenthaler* (2014), established the restricted residue sets \(\{0,2,3\}\) and \(\{0,1,4\}\) modulo \(5\) for specific shifted central-binomial families. That residue restriction is prior work, not claimed as new here. The new claims are the sharp prime-uniform first-defect cutoff, the exact density classification, and the finite-block frequency/imbalance law. Yaqubi–Mirzavaziri (2017), Section 4, and He–Yuan (2024), Introduction and Section 3, discuss or cite Vsemirnov's counterexamples and other global residue-set questions; the material inspected does not contain these frequency or first-defect formulas. Vsemirnov's complete text was not accessible for comparison, leaving priority uncertainty about any finer assertions there.

## Limitations
No result is claimed for the Legendre character at zero or for prime \(2\). The prime-density result uses Dirichlet's theorem and does not give uniform effective error bounds. The block count is tied to the specified lengths \(5^L\). The exact p-adic valuations of the binomial coefficients and their distribution over unrestricted \(n\) are not determined. The Vsemirnov paper was inspected only through its publisher preview and theorem as quoted in other papers; this is a residual originality risk, not a correctness limitation.

## References
- V. J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651 (first version 2013-01-31), Section 7, Conjecture 7.1.
- M. Vsemirnov, *On a conjecture of Guo and Krattenthaler*, International Journal of Number Theory **10** (2014), 1541–1543, DOI:10.1142/S1793042114500420.
- D. Yaqubi and M. Mirzavaziri, *Some divisibility properties of binomial coefficients*, arXiv:1701.06217 (2017), Section 4.
- Y. He and P. Yuan, *Results on some conjectures about binomial coefficients*, Bulletin of the Mathematical Society of Sciences Mathematical of Romania **67** (2024), 429–448, Sections 1 and 3; https://ssmr.ro/bulletin/pdf/67-4/articol_4.pdf.
- É. Lucas, classical digitwise congruence for binomial coefficients (1878); quadratic reciprocity; Dirichlet's theorem on primes in arithmetic progressions (standard tools).
