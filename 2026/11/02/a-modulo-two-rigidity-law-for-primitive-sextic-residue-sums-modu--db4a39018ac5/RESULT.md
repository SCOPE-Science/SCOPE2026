# A modulo-two rigidity law for primitive sextic residue sums modulo seven times a prime

## Finding
For every prime \(q\equiv1\pmod4\), \(q\ne7\), define
\[
H_q=\{y\in(\mathbb Z/7q\mathbb Z)^\times:y\bmod7=(\frac{y\bmod q}{q})\bmod7\}.
\]
The right-hand symbol is the Legendre symbol, regarded as \(1\) or \(-1\) modulo \(7\). This is a cyclic subgroup of index six, the kernel of an odd primitive sextic character. Write
\[
\Delta_q=\sum_{h\in H_q}\langle h\rangle_{7q}-\frac{7q(q-1)}2,
\]
where \(\langle h\rangle_{7q}\) is the least positive representative. Then \(\Delta_q/(7q)\) is always an integer and
\[
\boxed{\frac{\Delta_q}{7q}\equiv
\begin{cases}1\pmod2,&q\equiv9,13,25\pmod{28},\\
0\pmod2,&q\equiv1,5,17\pmod{28}.
\end{cases}}
\]
In particular, for every prime \(q\equiv9,13,25\pmod{28}\), the subgroup is not sum-balanced, and its deviation satisfies \(|\Delta_q|\ge7q\). This is a necessary-congruence obstruction, not a complete characterization of the other three classes.

A more precise formula gives the exact deviation. Put \(r=q\bmod7\) and \(E_q(S)=\sum_{1\le x<q,\,x\bmod7\in S}(\frac{x}{q})\). Then
\[
\frac{2\Delta_q}{7q}=\begin{cases}
-E_q(\{0,1\}),&r=1,\\
-E_q(\{1\}),&r=2,\\
-E_q(\{1,2,5\}),&r=3,\\
+E_q(\{2,5,6\}),&r=4,\\
+E_q(\{6\}),&r=5,\\
+E_q(\{0,6\}),&r=6.
\end{cases}
\]
The condition \(E_q(S)=0\) is therefore necessary and sufficient for this particular subgroup to be sum-balanced. The novelty claimed here is the complete residue-class parity obstruction and its explicit seven-class mechanism, not the general character criterion or the example at modulus \(35\) already in the source paper.

## Assumptions and scope
The prime \(q\) is odd and \(q\equiv1\pmod4\). The subgroup \(H_q\) is defined by both Chinese-remainder projections and not by an arbitrarily selected generator. Let \(\varepsilon_q(x)=(\frac{x}{q})\). Because \(\varepsilon_q(-1)=1\), the graph \(x\mapsto(\varepsilon_q(x),x)\) is isomorphic to the cyclic group \(\mathbb F_q^\times\) and has order \(q-1\). Its index in the unit group modulo \(7q\) is six. If \(\chi_7\) is an order-six character modulo \(7\), then \(\chi_7(-1)=-1\) and \(H_q=\ker(\chi_7\varepsilon_q)\); both local characters are nonprincipal, hence the character has conductor \(7q\), exact order six and odd parity. The subgroup omits \(-1\).

## Proof
For each integer \(1\le x<q\), let \(y_+(x)\) and \(y_-(x)\) denote the unique representatives in \([1,7q)\) congruent respectively to \(+1\) and \(-1\) modulo \(7\) and to \(x\) modulo \(q\). There are unique \(j_\pm(x)\in\{0,1,\ldots,6\}\) satisfying
\[
y_\pm(x)=x+qj_\pm(x),\qquad
j_\pm(x)=[(\pm1-x)q^{-1}]_7,
\]
where \([\cdot]_7\) means least nonnegative residue modulo \(7\), and the inverse is taken modulo \(7\).

Because \(x\mapsto q-x\) exchanges the sets \(\{y_+(x)\}\) and \(\{7q-y_-(x)\}\), their combined sum is \(7q(q-1)\). Selecting \(y_+(x)\) when \(\varepsilon_q(x)=1\) and \(y_-(x)\) otherwise therefore gives
\[
2\Delta_q=q\sum_{x=1}^{q-1}\varepsilon_q(x)(j_+(x)-j_-(x)).
\]
For fixed \(r=q\bmod7\), the difference in parentheses depends only on \(c=x\bmod7\). Direct evaluation of the seven residues shows that it is \(+2\) away from \(S=\{0,1\}\) and \(-5\) on \(S\) for \(r=1\); similarly its two values differ by seven in each of the remaining five cases. Explicitly, the exceptional class sets and signs are \((r,S,\text{sign})=(1,\{0,1\},-),(2,\{1\},-),(3,\{1,2,5\},-),(4,\{2,5,6\},+),(5,\{6\},+),(6,\{0,6\},+)\). Since \(\sum_{x=1}^{q-1}\varepsilon_q(x)=0\), all common constant terms disappear. This proves the displayed six-branch formula.

Each displayed class set \(S\) is stable under \(c\mapsto r-c\pmod7\). Thus the associated integers \(1\le x<q\) are stable under the fixed-point-free involution \(x\mapsto q-x\). On every pair the Legendre symbols are equal, since \(\varepsilon_q(-1)=1\). Consequently
\[
E_q(S)\equiv\#\{1\le x<q:x\bmod7\in S\}\pmod4,
\]
because each pair contributes either \(+2\) or \(-2\), congruent modulo four. The number of selected integers is always even, establishing \(7q\mid\Delta_q\). Writing \(q=7k+r\), those six cardinalities, in order \(r=1,2,3,4,5,6\), are \(2k,k+1,3k+2,3k+1,k,2k\). Now \(q\equiv1\pmod4\) forces respectively \(k\equiv0,1,2,3,0,1\pmod4\). Their cardinalities modulo four are respectively \(0,2,0,2,0,2\). Dividing the exact character-sum formula by two gives the asserted parity law. In the three odd cases the quotient is a nonzero odd integer, and therefore \(|\Delta_q|\ge7q\).

## Verification
The accompanying `checker.py` independently constructs the CRT subgroup and sums its least positive representatives, then calculates the Legendre sum over the class sets and checks both the exact formula and the parity law. Running `python checker.py 3000` tested all 211 eligible primes at most 3000 and returned `VERIFY_OK`. All arithmetic is integral. These finite checks corroborate rather than replace the proof for all eligible primes.

## Relationship to prior work
Ma, Merca and Zhang [1, Theorem 6.5] give a general index-six criterion through primitive sextic and quadratic first moments, and [1, Example 6.8] explicitly gives the centered subgroup modulo 35. Their discussion explicitly leaves infinitude of primitive sextic examples unresolved. The present parity law specializes to the cyclic primitive family with the modulus-seven local character and proves a concrete congruence obstruction for infinitely many primes. In contrast to the character-moment identity, the proof uses the integer CRT lifts and the fixed-point-free quadratic symmetry to obtain a modulo-four sum invariant. Earlier work of Pomerance and Ulmer [2] concerns the stronger property of balance of all cosets by half-interval counts. Girstmair [3] surveys related quadratic-residue and digit/class-number phenomena. No claim of determining the general primitive sextic balance problem is made.

## Limitations
The necessary restriction \(q\equiv1,5,17\pmod{28}\) is not sufficient. In particular, the theorem does not establish that infinitely many eligible primes have \(\Delta_q=0\), does not analyze every index-six subgroup modulo \(7q\), and does not exclude the remaining congruence class \(17\pmod{28}\). Earlier implicit congruence deductions from character-sum work remain a priority risk. Exact exhaustive checks of primes below 3000 are finite supporting evidence, not a proof of infinitude.

## References
[1] Haobo Ma, Mircea Merca and Wenlin Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes*, arXiv:2610.29608v1, first posted 2026-10-21, especially Theorem 6.5, Example 6.8 and concluding remarks. https://arxiv.org/abs/2610.29608

[2] Carl Pomerance and Douglas Ulmer, *On Balanced Subgroups of the Multiplicative Group*, arXiv:1204.6705 (2012), published 2013. https://arxiv.org/abs/1204.6705

[3] Kurt Girstmair, *Power Residues, Digit Expansions, and Relative Class Numbers*, Surveys in Mathematics and its Applications 21 (2026), 157–176. https://www.utgjiu.ro/math/sma/v21/a21_06.html
