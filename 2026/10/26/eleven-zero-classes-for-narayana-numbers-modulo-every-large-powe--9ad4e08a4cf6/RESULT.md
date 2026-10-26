# Eleven zero classes for Narayana numbers modulo every large power of two

## Finding
Let \(N_0=0\), \(N_1=N_2=1\), and \(N_{n+3}=N_{n+2}+N_n\) for every integer \(n\ge0\). For every integer \(k\ge6\), the exact period of this sequence modulo \(2^k\) is
\[
P_k=7\cdot2^{k-1}.
\]
Exactly eleven positions in each complete period vanish modulo \(2^k\): eight have index congruent to zero modulo seven, one has index congruent to four modulo seven, and two have index congruent to six modulo seven. The natural density of vanishing indices is therefore
\[
\frac{11}{P_k}=\frac{22}{7\cdot2^k}.
\]
A stronger local statement explains the eight exceptional indices. There is a unique odd \(2\)-adic integer \(\alpha\in\mathbb Z_2\), with \(\alpha\equiv5\pmod8\), such that
\[
\nu_2(N_{28t})=5+\nu_2(t)+\nu_2(t-\alpha)
\]
for every positive integer \(t\). Consequently, among \(0\le n<P_k\), the eight vanishing indices divisible by seven are exactly \(n=28t\), where
\[
0\le t<2^{k-3},\qquad t\equiv0\ \text{or}\ \alpha\pmod{2^{k-5}}.
\]
Here \(N_0=0\) is included using the convention \(\nu_2(0)=+\infty\). These are statements about the exact zero pattern and a local valuation formula, not an assertion about valuations in every other residue class.

## Assumptions and scope
All index variables other than \(t\) and \(k\) are nonnegative integers. We use the conventional valuation \(\nu_2\) extended to \(\mathbb Q_2\) and \(\nu_2(0)=+\infty\). A \(2\)-adic integer \(\alpha\) is an element of the complete valuation ring \(\mathbb Z_2\); congruences involving \(\alpha\) mean equality after reduction in \(\mathbb Z_2/2^j\mathbb Z_2\). No unproved analytic convergence or uniqueness assertion is assumed.

## Proof
**1. Matrix order and the exact period.** Put
\[
M=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},\quad
v=\begin{pmatrix}1\\1\\0\end{pmatrix},\quad e=(0,0,1).
\]
Then \(M^nv=(N_{n+2},N_{n+1},N_n)^T\) and \(N_n=eM^nv\). Direct multiplication yields
\[
M^7=\begin{pmatrix}9&4&6\\6&3&4\\4&2&3\end{pmatrix},\qquad
M^{28}=\begin{pmatrix}27201&12664&18560\\18560&8641&12664\\12664&5896&8641\end{pmatrix}=I+8E.
\]
The reduction of \(M\) modulo two has order seven: its characteristic polynomial \(x^3+x^2+1\) is irreducible over \(\mathbb F_2\), so a root has multiplicative order seven; direct computation also shows \(M^7=I\pmod2\). Moreover \(M^{14}\not\equiv I\pmod8\) and
\[
E\equiv\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}\pmod2.
\]
For \(k\ge3\), repeated squaring of \(M^{28}=I+8E\) gives
\[
M^{7\cdot2^{k-1}}=I+2^k E_k,\qquad E_k\equiv E\pmod2.
\]
This inductive congruence follows because \((I+2^kE_k)^2=I+2^{k+1}(E_k+2^{k-1}E_k^2)\). Nonzero \(E_k\pmod2\), the base \(M^{14}\not\equiv I\pmod8\), and order seven modulo two together prove that the order of \(M\pmod{2^k}\) equals \(7\cdot2^{k-1}\). The integer vectors \(v,Mv,M^2v\) form a \(\mathbb Z\)-basis (determinant one), so a shift fixes the initial three-term state if and only if it fixes the entire matrix. Thus the order of \(M\) is exactly the period of the scalar sequence, not merely a period upper bound.

**2. A complete lifting law outside multiples of seven.** Reducing the recurrence modulo two gives zeros precisely at indices \(0,4,6\pmod7\). The third row of \(E\pmod2\) is \((1,1,0)\). Hence, for every \(k\ge3\),
\[
N_{n+P_k}\equiv N_n+2^k(N_{n+2}+N_{n+1})\pmod{2^{k+1}}.
\]
For \(n\equiv4\) or \(6\pmod7\), the factor \(N_{n+2}+N_{n+1}\) is odd. Each zero modulo \(2^k\) in either of these classes therefore has exactly one of its two lifts \(n\) and \(n+P_k\) vanishing modulo \(2^{k+1}\), and no new zero can arise from a nonzero residue at the previous level. At \(k=6\), direct recurrence evaluation over the full period \(P_6=224\) gives precisely
\[
\{0,28,56,84,112,140,168,196,216,221,223\}.
\]
The three exceptional indices not divisible by seven are \(216,221,223\); their classes modulo seven are respectively \(6,4,6\). The unique-lift rule proves that exactly these class counts persist for every \(k\ge6\).

**3. The analytic valuation law on multiples of twenty-eight.** The integral matrix \(E=(M^{28}-I)/8\) satisfies
\[
eEv=N_{28}/8=2320\equiv0\pmod{16},\qquad eE^2v\equiv1\pmod2.
\]
The series \(L=\log(I+8E)\in8M_3(\mathbb Z_2)\) converges, and the exponential \(\exp(tL)\) converges for each \(t\in\mathbb Z_2\). Define
\[
\Phi(t)=e\exp(tL)v=\sum_{j\ge1} A_jt^j,
\quad A_j=\frac{eL^jv}{j!}.
\]
Since \(ev=0\), the constant term vanishes, and for every nonnegative integer \(t\), the exponential-logarithm identity gives \(\Phi(t)=eM^{28t}v=N_{28t}\). Because \(L\equiv8E-32E^2\pmod{64}\), the two displayed integrality/parity conditions imply
\[
A_1/32\equiv1\pmod2,\qquad A_2/32\equiv1\pmod2.
\]
For every \(j\ge3\), the factorial bound yields \(\nu_2(A_j)\ge3j-\nu_2(j!)\ge8\). Thus division of the analytic series by \(32t\) produces a restricted convergent power series
\[
g(t)=\frac{\Phi(t)}{32t}=a+bt+2h(t),\qquad a,b\in\mathbb Z_2^\times,\quad h\in\mathbb Z_2\langle t\rangle,
\]
interpreted at \(t=0\) by its power series. Here \(\mathbb Z_2\langle t\rangle\) denotes series whose coefficients approach zero 2-adically. Hence \(g(t)\equiv1+t\pmod2\), and the formal derivative \(g'(t)\equiv1\pmod2\) at every \(2\)-adic argument. By Hensel lifting (or iteration of the isometric congruence), there is a unique odd \(\alpha\in\mathbb Z_2\) with \(g(\alpha)=0\). More precisely, for every \(x,y\in\mathbb Z_2\),
\[
\frac{g(x)-g(y)}{x-y}\equiv b\equiv1\pmod2\quad(x\ne y),
\]
because the difference quotient of \(2h\) is even. Consequently \(\nu_2(g(t))=\nu_2(t-\alpha)\) for every \(t\in\mathbb Z_2\); multiplying by \(32t\) proves the claimed valuation identity for every positive integer \(t\). Direct recurrence evaluation shows \(\nu_2(N_{140})=8\); since \(140=28\cdot5\), it follows that \(\nu_2(5-\alpha)=3\), hence \(\alpha\equiv5\pmod8\).

**4. Counting all roots.** The eight roots at \(k=6\) that are divisible by seven are all divisible by twenty-eight; and every lift differs by \(P_k\), itself a multiple of twenty-eight, so every root in that class at every higher level is divisible by twenty-eight. Write such an index as \(n=28t\), with \(0\le t<P_k/28=2^{k-3}\). Since \(\alpha\) is odd, for even \(t\) the valuation formula reduces to \(\nu_2(N_{28t})=5+\nu_2(t)\); for odd \(t\) it reduces to \(5+\nu_2(t-\alpha)\). Therefore \(2^k\mid N_{28t}\) exactly when \(t\equiv0\) or \(\alpha\pmod{2^{k-5}}\). These two incongruent residue classes each have four representatives in \([0,2^{k-3})\), giving eight. Adding the three uniquely lifted roots in classes four and six produces eleven in each period. This completes the proof.

## Verification
The accompanying self-contained Python program `verify.py` uses only integer arithmetic and the standard library. It reconstructs \(M^7\), \(M^{28}\), \(E\bmod2\), the two key parity conditions, the exact companion periods modulo \(2^k\) for \(3\le k\le13\), and every zero index in each complete period for \(6\le k\le13\). It also computes the unique odd local root residues \(\alpha\bmod2^j\) for \(1\le j\le8\); the first residues are \(5\bmod8\), \(13\bmod16\), and \(29\bmod32\). The program terminates with `VERIFY_OK` when all assertions pass. The infinite-range claims follow from the proved induction and \(2\)-adic analytic argument; finite tests are corroboration only.

## Relationship to prior work
Kuloğlu, *The Narayana Sequence in Finite Groups* (Fibonacci Quarterly 60, 2022), proves periodicity and gives a general prime-power period-lifting theorem (Theorem 2.5). Therefore the period calculation here is not presented as an independently novel general mechanism; it supplies the exact local period required to count roots. Guadalupe (arXiv:2112.06187, 2021) determines the \(3\)-adic valuation of the Narayana numbers. Ismail, Rihane and Anwar (2023) determine the \(3\)-adic valuations of \(N_n\pm1\). Their studied primes and targets differ from the \(2\)-adic zero classification here. Sobolewski (arXiv:1702.05819, 2017) gives valuations of even-order \(2k\)-nacci sequences, not the lacunary third-order Narayana recurrence, and its general sequence theorem concerns finiteness of a factorial equation, not the eleven residue classes. The exact eleven-root law and two-root local interpolation were not located in the inspected sources or targeted record searches; that search outcome does not establish publication priority.

## Limitations
The claim applies to powers \(2^k\) for \(k\ge6\). For smaller \(k\) there are different root counts. It does not give closed formulas for the three other \(2\)-adic root addresses, nor all individual valuations \(\nu_2(N_n)\). General prior recurrence period-lifting theory covers part of the period statement; only the concrete root enumeration and analytic local factorization are put forward as candidate advances. An unindexed earlier specialization or a stronger recurrence-valuation theorem could subsume them.

## References
1. M. Ismail, S. E. Rihane, and M. Anwar, “Narayana sequence and the Brocard–Ramanujan equation,” *Notes on Number Theory and Discrete Mathematics* 29 (2023), 462–473. DOI: 10.7546/nntdm.2023.29.3.462-473. Online first: 2023-07-06. https://nntdm.net/papers/nntdm-29/NNTDM-29-3-462-473.pdf
2. B. Kuloğlu, “The Narayana Sequence in Finite Groups,” *Fibonacci Quarterly* 60 (2022), 211–220. https://www.fq.math.ca/Papers1/60-5/kologlu.pdf
3. R. Guadalupe, “On the \(3\)-adic valuation of the Narayana numbers,” arXiv:2112.06187 (2021). https://arxiv.org/abs/2112.06187
4. B. Sobolewski, “The \(2\)-adic valuation of generalized Fibonacci sequences with an application to certain Diophantine equations,” arXiv:1702.05819 (2017). https://arxiv.org/abs/1702.05819
5. OEIS A000930 and A271901, Narayana numbers and their periods modulo primes. https://oeis.org/A271901
