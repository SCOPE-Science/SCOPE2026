# Modulo-four quotient collapse for the scattered pattern \(010\)

## Finding
Let \(m\ge 2\) be an integer, and let \(t\in\{0,\ldots,m-1\}\). Let \(N_{010}(w)\) count triples of indices \(i<j<k\) whose letters in a finite binary word \(w\) are \(0,1,0\), respectively. Define
\[
L_{m,t}=\{w\in\{0,1\}^{*}:N_{010}(w)\equiv t\pmod m\}.
\]
The number \(\kappa(L_{m,t})\) of states in the **minimal complete deterministic automaton** is
\[
\boxed{\kappa(L_{m,t})=
\begin{cases}
m^{3},&m\text{ odd},\\
m^{3}/8,&4\mid m\text{ and }t\text{ odd},\\
m^{3}/2,&m\text{ even and not }(4\mid m\text{ and }t\text{ odd}).
\end{cases}}
\]
Thus, for every multiple of four, changing the desired occurrence residue from even to odd reduces the minimum automaton by a factor of four. For moduli congruent to two modulo four, no such reduction occurs.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); occurrences are scattered subsequences, counted **with multiplicity of index triples**, not distinct patterns or contiguous factors. Words may be empty, and residues are modulo the positive integer \(m\ge2\). The state count includes the start state and all complete letter transitions. The result holds for every residue, including zero. All algebra below is performed in \(\mathbb Z/m\mathbb Z\) unless parity is explicitly indicated.

## Proof
**1. The counting automaton.** After reading a prefix \(u\), put
\(x=N_0(u)\), \(y=N_{01}(u)\), and \(z=N_{010}(u)\) modulo \(m\). Here \(N_0\) counts zero symbols and \(N_{01}\) counts ordered scattered pairs. Its two letter maps are
\[
A(x,y,z)=(x+1,y,z+y),\qquad B(x,y,z)=(x,y+x,z).
\]
Starting at \((0,0,0)\) and accepting exactly \(z=t\) recognizes the language. Both transformations are permutations of \((\mathbb Z/m\mathbb Z)^3\), and both have order dividing \(m\).

**2. Reachability and its sole parity obstruction.** For an ordinary word, let \(x\) be its total number of zeroes, and for each letter \(1\) let \(i\) denote the number of preceding zeroes. That letter contributes \(i\) to \(y\) and \(i(x-i)\) to \(z\). Modulo two, \(i^2\equiv i\), so
\[
z\equiv(x-1)y\pmod2.\tag{1}
\]
This is a necessary condition when \(m\) is even.

To show it is sufficient, use the left-to-right word action of \(A,B\), with inverse actions realized by nonnegative powers because both maps have finite order. The word \(C=ABA^{-1}B^{-1}\) induces
\[
C(x,y,z)=(x,y+1,z-x-1),
\]
and the word \(D=ACA^{-1}C^{-1}\) induces
\[
D(x,y,z)=(x,y,z-2).
\]
From \((0,0,0)\), apply \(A^x\), then \(C^y\), obtaining \((x,y,-y(x+1))\). Applying powers of \(D\) produces every value of \(z\) with that parity if \(m\) is even, and every \(z\) if \(m\) is odd. Because \(-y(x+1)\equiv y(x-1)\pmod2\), (1) precisely describes the reachable set in the even case. Hence the number of reachable triples is \(m^3\) for odd \(m\), and \(m^3/2\) for even \(m\).

**3. Every possible suffix test.** For any suffix \(v\), write \(a=N_0(v)\), \(b=N_{10}(v)\), and \(d=N_{010}(v)\). Partitioning an occurrence of \(010\) according to its crossing of the boundary between a prefix \(u\) and \(v\) yields the exact identity
\[
N_{010}(uv)\equiv z+a y+b x+d\pmod m.\tag{2}
\]
Reversing \(v\) preserves the values \(N_0\), \(N_{010}\) and swaps \(N_{10}\) with \(N_{01}\), so Step 2 also classifies attainable suffix triples \((a,b,d)\). In particular, for odd \(m\) all triples occur, whereas for even \(m\) precisely those satisfying \(d\equiv(a-1)b\pmod2\) occur.

**4. Distinguishing quotients for odd modulus.** If two reachable states differ, select \(a,b\) for which \(\Delta z+a\Delta y+b\Delta x\not\equiv0\pmod m\): choose \(a=b=0\) if \(\Delta z\ne0\), otherwise use \(a=1,b=0\) or \(a=0,b=1\) to detect \(\Delta y\) or \(\Delta x\). Every \(d\) is available, so choose \(d\) to make (2) equal \(t\) for the first state and not the second. Hence all \(m^3\) states are inequivalent.

**5. Even modulus: exact quotient criterion.** Write \(q=(x,y,z)\) and \(q'=(x',y',z')\) for two reachable states and \(\Delta x=x'-x\), \(\Delta y=y'-y\), \(\Delta z=z'-z\). By (1), a suffix with given \((a,b)\) can be accepting from \(q\) precisely when
\[
(x+a-1)(y+b)\equiv t\pmod2.\tag{3}
\]
If \(t\) is odd, (3) allows just one parity pair: \(a\equiv x\), \(b\equiv1-y\). If \(t\) is even, it allows the other three parity pairs. These feasible-pair sets uniquely identify the parities of \(x,y\), so states with different such parities cannot be equivalent.

Suppose therefore that \(q,q'\) have the same \(x,y\) parities. For each feasible \((a,b)\), exactly one choice of \(d\pmod m\) makes the suffix accepting from \(q\), and that choice is attainable by Step 3. Thus the states have the same right language if and only if
\[
\Delta z+a\Delta y+b\Delta x\equiv0\pmod m
\quad\text{for every feasible }(a,b).\tag{4}
\]
Varying \(a\) or \(b\) by two in a feasible parity pair gives \(2\Delta y=2\Delta x=0\pmod m\). Thus each of \(\Delta x,\Delta y\) is either \(0\) or \(h=m/2\).

If \(m\equiv2\pmod4\), then \(h\) is odd, while \(\Delta x,\Delta y\) are even; both vanish and (4) forces \(\Delta z=0\). If \(4\mid m\) and \(t\) is even, the three feasible parity pairs contain pairs differing in either single parity coordinate; comparing (4) on those pairs directly forces \(\Delta x=\Delta y=0\), then \(\Delta z=0\). In these cases all reachable states are inequivalent.

Finally let \(4\mid m\) and \(t\) be odd. Equation (3) permits only \((a,b)\equiv(x,1-y)\pmod2\). The equivalent states are exactly those satisfying
\[
\Delta x,\Delta y\in\{0,h\},\qquad
\Delta z+x\Delta y+(1-y)\Delta x\equiv0\pmod m.\tag{5}
\]
For each of the four choices of \(\Delta x,\Delta y\), (5) gives one \(\Delta z\); because \(h\) is even, all four triples satisfy (1) and are reachable. Thus every right-language equivalence class has size exactly four. Dividing \(m^3/2\) reachable states by four yields \(m^3/8\), completing all cases. \(\square\)

## Verification
Run `python3 verify.py` using Python 3.9+ with no external dependencies. The checker constructs all reachable counting states for each \(2\le m\le14\), independently minimizes the resulting complete DFA for every target residue, and checks the displayed formula. It also compares the counter against exhaustive index-triple subsequence counting on all 4,095 binary words of lengths zero through eleven, over eight test moduli. The finite tests supplement the parameter-uniform proof; they do not establish its infinitely many cases by themselves.

## Relationship to prior work
Mansour, Rastegar and Roitershtein (2019) study counts of subsequence pattern occurrences via automata and obtain asymptotic pattern-frequency results; their exact-length occurrence-count language problems do not give the present **modular Myhill–Nerode index**. Hahn, Cheon and Han (2023) analyze Parikh matrices and equalities of **ordered** scattered-subword counts over three letters, but their equivalence classifications do not produce the periodic modulus-four quotient collapse for the repeated-letter pattern \(010\). Related exact modular state counts for words of the form \(0^r1\) concern a different subsequence pattern and do not imply (5): separated equal endpoint letters create a specific parity obstruction. Generic permutation-automaton minimization provides a framework, but the concrete reachability and fourfold right-congruence calculation are required to deduce the formula.

## Limitations
Only the **minimal DFA state count** is established. No claim is made about the syntactic monoid's cardinality, complexity of other patterns, finite alphabets beyond binary, or contiguous occurrences. Possible unindexed work on modular length-three subsequence counters is an originality risk. The self-contained argument has not undergone independent external audit.

## References
1. T. Mansour, R. Rastegar, A. Roitershtein, *Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations*, arXiv:1905.05646 (first posted 2019-05-14), https://arxiv.org/pdf/1905.05646.
2. J. Hahn, H. Cheon, Y.-S. Han, *M-equivalence of Parikh Matrix over a Ternary Alphabet*, CIAA 2023, doi:10.1007/978-3-031-40247-0_10; author PDF https://toc.yonsei.ac.kr/~emmous/papers/corrected_ciaa23.pdf.
