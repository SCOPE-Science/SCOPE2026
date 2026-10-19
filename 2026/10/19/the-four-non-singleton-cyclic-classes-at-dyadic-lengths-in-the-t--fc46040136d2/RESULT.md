# The four non-singleton cyclic classes at dyadic lengths in the Thue–Morse word

## Finding
Let \(t=011010011001\cdots\) be the fixed point starting in \(0\) of the substitution \(\mu(0)=01\), \(\mu(1)=10\). For every integer \(k\ge2\), put \(N=2^k\) and partition the distinct length-\(N\) contiguous factors of \(t\) into classes under cyclic rotation. A *class size* means the number of distinct occurring factors belonging to that rotation class, **not** the number of occurrences or possible rotations.

Exactly one class has size \(N\), exactly three classes have size \(2\), and exactly \(2N-8\) classes have size \(1\); no other class sizes occur. The size-\(N\) class consists of all rotations of \(T_k=\mu^k(0)\). The three size-\(2\) classes are represented, respectively, by \(\mu^{k-2}(0010)\), \(\mu^{k-2}(0101)\), and \(\mu^{k-2}(1011)\). In particular the previously known count of cyclic classes \(c_t(N)=2N-4\) is refined to a complete orbit-occupancy profile.

## Assumptions and scope
Indices of infinite words start at zero. If \(u=u_0\cdots u_{n-1}\), write \(\operatorname{rot}_j(u)=u_j\cdots u_{n-1}u_0\cdots u_{j-1}\), for \(0\le j<n\). Write \(\mathcal F_n\) for the set of all distinct length-\(n\) factors of \(t\). A cyclic class is \(\mathcal F_n\cap\{\operatorname{rot}_j(u):0\le j<n\}\) for a given \(u\in\mathcal F_n\). No statement is made for nondyadic lengths.

Define the circularly one-step extendible factors
\[
E(n)=\{u\in\mathcal F_n:uu_0\in\mathcal F_{n+1}\}
\]
and let \(D(n)\) be the number of distinct length-\(n\) factors whose first and last letters differ.

## Proof
**1. Recognizability and splitting.** Each length-\(2m\) factor beginning at an even position is uniquely \(\mu(u)\), with \(u\in\mathcal F_m\). Each one beginning at an odd position is uniquely
\[
\overline{v_0}\,\mu(v_1\cdots v_{m-1})\,v_m,\qquad v=v_0\cdots v_m\in\mathcal F_{m+1},
\]
where \(\overline 0=1\), \(\overline1=0\). Conversely every displayed word occurs, since its underlying factor occurs. The even- and odd-start sets are disjoint for lengths at least four: the first two disjoint letter-pairs of an even-start factor are both unequal, whereas if both first pairs of an odd-start factor were unequal, its three underlying letters would coincide. The Thue–Morse word has no triple \(000\) or \(111\), because equality of two adjacent output symbols can occur only across a \(\mu\)-block boundary, and these boundaries are separated by two positions.

**2. The cyclicly extendible core.** Directly from the six length-three factors \(001,010,011,100,101,110\) and their substituted windows, the length-four and length-five factor sets are
\[
\begin{split}
\mathcal F_4={}&\{0010,0011,0100,0101,0110,1001,1010,1011,1100,1101\},\\
\mathcal F_5={}&\{00101,00110,01001,01011,01100,01101,10010,10011,10100,10110,11001,11010\}.
\end{split}
\]
Hence \(E(4)=\{0011,0110,1001,1100\}\), precisely the four rotations of \(T_2=0110\).

For every \(m\ge2\), the even-start elements of \(E(2m)\) are precisely \(\mu(E(m))\): appending their initial letter forces the next underlying letter to equal the previous underlying first letter. The odd-start elements of \(E(2m)\) are precisely \(\operatorname{rot}_1(\mu(E(m)))\): for an odd-start length-\(2m+1\) factor, equality of the first and last displayed letters is equivalent to equality of the first and last underlying letters. Thus
\[
E(2m)=\mu(E(m))\ \cup\ \{\operatorname{rot}_1(\mu(u)):u\in E(m)\}.
\]
Since \(\mu\) carries every rotation of a length-\(m\) word to an even rotation of its image, induction yields, for every \(k\ge2\),
\[
E(2^k)=\{\operatorname{rot}_j(T_k):0\le j<2^k\}.
\]
The rotations are distinct. Indeed \(T_2=0110\) is primitive. If \(u\) is a nonconstant primitive cyclic word, \(\mu(u)\) has a unique circular pairing into adjacent unequal-letter pairs: its block pairing has zero equal-letter pairs, while the other pairing has at least two because a nonconstant circular binary word has at least two transitions. Any cyclic period of \(\mu(u)\) therefore preserves that pairing and is even. Halving such a period would produce a proper cyclic period of \(u\), impossible. Thus \(\mu(u)\) is primitive, and induction gives primitivity of every \(T_k\), \(k\ge2\).

**3. The new odd classes are singletons.** Let \(m\ge4\). For an odd-start factor \(f=\overline{v_0}\mu(v_1\cdots v_{m-1})v_m\) with \(v_m\ne v_0\), consider the two pairings of the \(2m\) circular positions into adjacent pairs. The pairing using positions \((1,2),(3,4),\ldots,(2m-1,0)\) has exactly one equal-letter pair, namely the wrap pair \((2m-1,0)\). The opposite pairing has as many equal-letter pairs as there are adjacent changes among \(v_0,\ldots,v_m\). This number is at least two: any binary word of length at least five with at most one change would contain \(000\) or \(111\). Hence the uniquely one-defective circular pairing and the position of its defect identify the displayed word uniquely within its rotation class. In particular each such factor occupies a singleton class.

By contrast an even-start factor \(\mu(u)\), for \(u\in\mathcal F_m\), has one circular adjacent pairing containing zero equal-letter pairs and the opposite pairing contains the cyclic number of changes of \(u\), which is at least two because \(u\) is nonconstant and that number is even. The two types therefore cannot be conjugate. Moreover \(\mu(u)\) and \(\mu(u')\) are conjugate if and only if \(u\) and \(u'\) are conjugate: the uniquely zero-defective pairing forces every admissible shift of their images to be even.

If instead \(v_m=v_0\), the odd-start factor equals \(\operatorname{rot}_1(\mu(v_0\cdots v_{m-1}))\) and the underlying prefix \(v_0\cdots v_{m-1}\) lies in \(E(m)\). The disjointness of even and odd factor sets therefore implies the following exact recursion on cyclic class *sizes*: for each class \(U\) of length-\(m\) factors, the corresponding non-singleton-or-inherited class at length \(2m\) has size
\[
|U|+|U\cap E(m)|;
\]
in addition there are exactly \(D(m+1)\) new singleton classes, one for each odd-start factor with differing underlying endpoints. These exhaust all length-\(2m\) factors.

**4. Number of new singletons.** A length-\(2m+1\) factor at an even start is \(\mu(v_0\cdots v_{m-1})v_m\), and at an odd start is \(\overline{v_0}\mu(v_1\cdots v_m)\), each for a length-\(m+1\) factor \(v\). Both preserve whether the underlying first and last letters differ. They are injective and, when \(m\ge2\), disjoint by step 1. Thus \(D(2m+1)=2D(m+1)\) for \(m\ge2\). Direct enumeration yields \(D(3)=4\), and consequently
\[
D(2^k+1)=2^{k+1}\quad(k\ge1).
\]

**5. Induction on scale.** At length four, inspection of \(\mathcal F_4\) shows one class of size four (the rotations of \(0110\)) and three classes of size two, represented by \(0010\), \(0101\), \(1011\); no singleton class occurs. Suppose the claim holds at length \(m=2^k\), \(k\ge2\). By step 2, \(E(m)\) is the entire unique size-\(m\) class and no other class meets \(E(m)\). Step 3 then doubles precisely that class's size, leaves all other inherited class sizes unchanged, and creates \(D(m+1)=2m\) singleton classes. The three doubletons are mapped to their \(\mu\)-images. Since the singleton count is zero at \(m=4\), its value at length \(N=2^k\) is \(2N-8\). This proves every assertion for all \(k\ge2\). \(\square\)

## Verification
`verification.py` constructs the **complete** set of factors of each tested length using the four two-letter factors and substitution-aligned blocks. It independently compares those complete sets with long direct prefixes at smaller scales; it checks the class-size histogram, the three specific doubleton representatives, the full rotation class, the one-step extendible factors, and the count of opposite-ended factors. Run `python3 verification.py` in the same directory; the expected terminal message is `VERIFY_OK`. Computational ranges are finite and are not used as substitutes for the induction.

## Relationship to prior work
Cassaigne, Fici, Sciortino, and Zamboni introduced cyclic complexity and proved general facts about the Thue–Morse word, including its growth and parity recognizability. Krawchuk and Rampersad (2018, Proposition 1) **already proved** the aggregate identity \(c_t(2^k)=2^{k+1}-4\) using automata, and Shallit (2023, Proposition 1) reiterates it. The aggregate identity is **not** presented here as new. The contribution is the individual class-size spectrum and explicit exceptional-class representatives. Knowing the total number of factors and the number of cyclic classes alone does not determine this occupancy spectrum.

## Limitations
The classification concerns distinct occurring factors rather than factor frequencies or the size of the full abstract rotation orbit. It is restricted to dyadic lengths, and no independent mathematical audit has been performed. Although three close primary papers were inspected, equivalent statements in unindexed or inaccessible texts cannot be ruled out.

## References
- J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (first posted 2014-02-24), especially Section 5.3, https://arxiv.org/abs/1402.5843.
- C. Krawchuk, N. Rampersad, *Cyclic Complexity of Some Infinite Words and Generalizations*, Integers 18A (2018), #A12, especially Proposition 1, https://math.colgate.edu/~integers/sjs12/sjs12.pdf.
- J. Shallit, *Proof of a Conjecture of Krawchuk and Rampersad on the Cyclic Complexity of the Thue–Morse Sequence*, Integers 23 (2023), #A44, especially Proposition 1, https://math.colgate.edu/~integers/x44/x44.pdf.
