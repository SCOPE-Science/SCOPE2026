# Exact Lucas-counted periodic-lift obstructions for cellular automaton rule 18

## Finding
Let \(\Phi:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be elementary cellular automaton rule 18: \((\Phi x)_i=1\) precisely when \((x_{i-1},x_i,x_{i+1})\) equals \(001\) or \(100\). Write \(Y=\Phi(\{0,1\}^{\mathbb Z})\). For every integer \(n\ge1\), an \(n\)-periodic point \(y\in Y\) admits an \(n\)-periodic preimage if and only if the number of \(1\)'s in one length-\(n\) period of \(y\) is even. Every such \(y\), without exception, has a preimage of period dividing \(2n\).

The \(n\)-periodic points of \(Y\) *without* an \(n\)-periodic preimage are exactly the cyclic binary words of length \(n\) with odd Hamming weight and no cyclic occurrence of \(11\). Their number is
\[
E_n=\frac{L_n-2\cos(n\pi/3)}2,\qquad n\ge1,
\]
where \(L_n=\varphi^n+(-\varphi^{-1})^n\) is the Lucas number and \(\varphi=(1+\sqrt5)/2\). Consequently
\[
\sum_{n\ge1}E_nz^n=\frac{z^2(2-z)}{(1-z-z^2)(1-z+z^2)},
\qquad E_n\sim \frac{\varphi^n}{2}.
\]
If \(y\) has *least* spatial period \(n\) and belongs to this exceptional set, then the least spatial period of any periodic antecedent of \(y\) is exactly \(2n\). This last assertion is restricted to primitive periods; for a nonprimitive \(n\)-block, a preimage of least period smaller than \(2n\) can exist.

## Assumptions and scope
Here \(n\)-periodic means fixed by the \(n\)-fold spatial shift; the least period may divide \(n\). The alphabet is binary, coordinates lie in \(\mathbb Z\), and \(Y\) is the **one-update spatial image**, not an eventual attractor or a limit set. A cyclic occurrence of \(11\) includes the pair across the last-to-first boundary. \(E_n\) counts *labeled length-\(n\) periodic points*, not shift-orbit classes or primitive-period orbits. A preimage of period dividing \(2n\) need not be unique. This work does not count distinct preimages or classify time-periodic trajectories under iteration of \(\Phi\).

## Proof
**1. The periodic parity obstruction.** In arithmetic modulo two, rule 18 obeys
\[
(\Phi x)_i=(1+x_i)(x_{i-1}+x_{i+1})\pmod2.
\]
For an \(n\)-periodic input \(x\), summing the right-hand side over \(i=0,\ldots,n-1\), the two unweighted neighbor sums are equal, and the two quadratic neighbor sums are equal by cyclic index shift. Therefore
\[
\sum_{i=0}^{n-1}(\Phi x)_i=0\pmod2.
\]
Thus odd output weight excludes any \(n\)-periodic input, for every \(n\ge1\).

**2. Any output containing \(11\) has a same-period antecedent.** Suppose \(y\in Y\) is \(n\)-periodic and \(y_i=y_{i+1}=1\) for some \(i\in\mathbb Z\). Choose an arbitrary bilateral input \(x\) with \(\Phi x=y\). Direct inspection of the two allowed input triples for output symbol \(1\) shows that the **unique** input four-block producing two consecutive ones is
\[
(x_{i-1},x_i,x_{i+1},x_{i+2})=(1,0,0,1).
\]
The identical four-block is forced at \(i+n\). Repeat the block \(x_{i+1},\ldots,x_{i+n}\) periodically to form an input \(\widetilde x\). At the two seams the replacement neighbor symbols equal the original neighbors because \(x_i=x_{i+1}=x_{i+n}=x_{i+n+1}=0\). Consequently every radius-one neighborhood in \(\widetilde x\) agrees with the corresponding neighborhood in \(x\) on the copied block, so \(\Phi\widetilde x=y\). This constructs an \(n\)-periodic antecedent. In particular an \(n\)-periodic image point containing \(11\) necessarily has even period weight.

**3. Every cyclic \(11\)-free output has an explicit double-period antecedent.** Let \(y\in\{0,1\}^{\mathbb Z}\) be any \(n\)-periodic point with \(y_i y_{i+1}=0\) for all \(i\). Choose \(p_0\in\{0,1\}\) and recursively define a bilateral phase by
\[
p_{i+1}=p_i\oplus y_i,
\]
where \(\oplus\) denotes addition modulo two. Set
\[
x_i=p_i(1-y_i).
\]
If \(y_i=1\), then \(y_{i-1}=y_{i+1}=0\), \(x_i=0\), and \((x_{i-1},x_{i+1})=(p_i,1-p_i)\); exactly one neighboring input bit is one, hence \((\Phi x)_i=1\). If \(y_i=0\), then \(p_{i+1}=p_i\); for \(p_i=1\) one has \(x_i=1\), forcing output zero, while for \(p_i=0\) both neighbor input bits are zero, also forcing output zero. Thus \(\Phi x=y\). Let \(k\) be the number of ones in one \(n\)-block: \(p_{i+n}=p_i\oplus(k\bmod2)\). If \(k\) is even, both \(p\) and \(x\) are \(n\)-periodic. If \(k\) is odd, both are \(2n\)-periodic (not necessarily of least period \(2n\)). Hence every cyclic \(11\)-free output is in \(Y\); in the odd case no \(n\)-periodic antecedent exists by step 1.

Steps 2–3 exhaust \(n\)-periodic points in \(Y\). They prove the if-and-only-if lifting condition, identify the entire exceptional family, and provide a \(2n\)-periodic antecedent in every case. If \(y\) has least period \(n\), every periodic antecedent has least period divisible by \(n\), since \(\Phi\) commutes with spatial shifts. In the exceptional case the possible least periods dividing \(2n\) are therefore only \(n\) and \(2n\); the first is impossible, so the explicit antecedent has least period \(2n\).

**4. Exact cyclic count.** Associate a variable \(t\) to every \(1\) and form
\[
M(t)=\begin{pmatrix}1&t\\1&0\end{pmatrix}.
\]
Each length-\(n\) cyclic path of this two-state nearest-neighbor graph corresponds bijectively to a cyclically \(11\)-free labeled binary word, with path weight \(t^k\) if the word has \(k\) ones. Hence \(F_n(t)=\operatorname{tr}(M(t)^n)\) and
\[
E_n=\frac{F_n(1)-F_n(-1)}2.
\]
The eigenvalues of \(M(1)\) are \(\varphi\) and \(-\varphi^{-1}\), giving \(F_n(1)=L_n\). Those of \(M(-1)\) are \(e^{\pm i\pi/3}\), giving \(F_n(-1)=2\cos(n\pi/3)\). This proves the closed formula, including \(n=1,2\) with cyclic boundary conditions. Taking traces and summing geometric matrix powers yields
\[
\sum_{n\ge1}F_n(1)z^n=\frac{z+2z^2}{1-z-z^2},\quad
\sum_{n\ge1}F_n(-1)z^n=\frac{z-2z^2}{1-z+z^2}.
\]
Their half-difference simplifies to the stated generating function. Since \(|2\cos(n\pi/3)|\le2\) and \(|-\varphi^{-1}|<1\), the asymptotic \(E_n\sim\varphi^n/2\) follows.

## Verification
Execute the included standalone `verify.py` using Python 3, from the package directory, with `python verify.py`. The checker independently generates the rule-18 de Bruijn transfer matrices, exactly multiplies their Boolean adjacency matrices, and compares trace conditions for period \(n\) and \(2n\) against direct finite-ring images for every \(n=1,\ldots,12\). It also checks the parity/adjacency obstruction classification and the Lucas formula across all these ring sizes. Observed output:

`VERIFY_OK: n=1..12; 8190 exact cyclic words; 32760 transfer/cycle/ring checks; 420 total exceptional words; 12 Lucas character formulas`

These finite checks are evidence for the explicit steps, not a substitute for the unrestricted arguments in the proof.

## Relationship to prior work
Wolfram's 1984 study already gives the finite-automaton formal-language treatment of elementary cellular automata, including rule 18; such image presentations and the one-step image entropy are prior art. Jiang and Xie (2002) studied rule-18 evolution complexity and its defects. Shreim and collaborators' 2006 preprint and subsequent 2007 paper develop finite-ring state-space and preimage questions. Salo (2022) formalized the same-period preimage obstruction as the weak periodic point condition and established its role in cellular-automaton regularity, including elementary automata. Sabrié and Törmä (2023 preprint) analyze rule-18 limit dynamics and the parity structure of multiple occurrences of the output marker `11`. These works supply overlapping background and partial ingredients; the focused evaluated statement here is the **all-period exceptional-language classification together with the Lucas/character count and exact period-doubling lift bound**. Finite-state decidability alone does not state this closed formula. We do not claim that the marker principle, the phase construction, or the Lucas numbers individually originate here.

## Limitations
A rule-specific periodic-lift census does not classify all preimage multiplicities, the global image shift, or temporal attractors. The same-period obstruction alone was already part of the general weak periodic point methodology; this result adds a concrete full exception language and its counted growth. Because general de Bruijn and weak-periodicity algorithms can compute finite-period properties, an earlier implicit derivation or unpublished tabulation cannot be ruled out by the inspected literature. No independent external audit or historical-priority certification has been performed.

## References
1. S. Wolfram, *Computation Theory of Cellular Automata*, Communications in Mathematical Physics 96 (1984), 15–57, DOI: `10.1007/BF01217347`.
2. Z.-S. Jiang and H.-M. Xie, *Evolution Complexity of the Elementary Cellular Automaton Rule 18*, Complex Systems 13 (2002), 271–295.
3. A. Shreim, P. Grassberger, W. Nadler, B. Samuelsson, J. E. S. Socolar, M. Paczuski, *Network Analysis of the State Space of Discrete Dynamical Systems*, arXiv:`cond-mat/0610447` (first public 2006-10-16); Phys. Rev. Lett. 98 (2007), 198701.
4. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:`2209.13373` (2022); Natural Computing 22 (2023), 527–538.
5. H. Sabrié and I. Törmä, *Limit dynamics of elementary cellular automaton 18*, arXiv:`2308.12744` (2023); Ergodic Theory and Dynamical Systems, online 2026.
