# A Lucas-number formula for shortest circular covers of binary words with runs at most two

## Finding
For every integer \(n\geq3\), let \(\mathcal R_n\) be the set of all *ordinary finite* binary words of length \(n\) containing neither `000` nor `111` as a consecutive factor. A circular cover is a cyclic binary word in which every member of \(\mathcal R_n\) occurs as a cyclic window of length \(n\); other windows and repeated occurrences are permitted. If \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\), the least possible length is exactly

\[
\boxed{L_n=2(F_{n+1}+F_{n-1}-1).}
\]

In particular, \(L_n=6,12,20,34,56,92,150,244,396,642\) at orders \(n=3,4,5,6,7,8,9,10,11,12\), respectively. Each optimum can be realized with **no forbidden length-three factor, even across the circular boundary**. Every required length-\(n\) word then occurs once or twice; exactly \(2F_{n-1}-2\) distinct required words occur twice, and all others occur once.

## Assumptions and scope
The binary alphabet is \(\{0,1\}\). A finite word avoids `000` and `111` if neither is an internal consecutive factor; no condition is placed on the repetition of the finite word itself. Thus transient words whose own cyclic wrap would create a forbidden triple still belong to \(\mathcal R_n\). A circular binary word of length \(L\) has exactly \(L\) indexed cyclic windows of length \(n\), read with positions modulo \(L\). The minimization is over all such circular words; it does **not** require their additional windows to avoid the forbidden factors.

The primary construction nevertheless satisfies that stronger avoidance condition. All words and indices in the proof are literal binary strings, not equivalence classes under rotation, reversal, or complementation.

## Proof
**1. Counting the required factors.** Each word in \(\mathcal R_j\) is specified by its first bit (two choices) and a composition of \(j\) into maximal constant-run lengths from \(\{1,2\}\). Consequently, for \(j\geq1\),
\[
|\mathcal R_j|=2F_{j+1}.
\]

**2. A connected de Bruijn graph.** Fix \(n\geq3\) and put \(m=n-1\). Let \(G_n\) have as vertices all words in \(\mathcal R_m\). Every \(w\in\mathcal R_n\) is an arc from its length-\(m\) prefix \(p(w)\) to its length-\(m\) suffix \(s(w)\). This digraph is strongly connected: for any two vertices \(u,v\), take an alternating bridge \(B\) of length two or three whose first bit differs from the last bit of \(u\), and whose last bit differs from the first bit of \(v\). Such a bridge always exists by choosing its parity. The concatenation \(uBv\) contains no forbidden triple. Its consecutive length-\(m\) windows therefore give a path from \(u\) to \(v\) in \(G_n\).

**3. An explicit Eulerian augmentation.** Define \(\mathcal X_n\subseteq\mathcal R_n\) to contain the words whose first two bits are different, whose last two bits are different, and which are not completely alternating. Add a **second copy** of each arc corresponding to a member of \(\mathcal X_n\), producing a directed multigraph \(H_n\).

For any vertex \(v\) of length \(m\), write \(r_{\mathrm{first}}(v)=1\) if its first two bits agree and \(0\) otherwise, and define \(r_{\mathrm{last}}(v)\) analogously. In \(G_n\),
\[
\deg^+(v)=2-r_{\mathrm{last}}(v),\qquad
\deg^-(v)=2-r_{\mathrm{first}}(v).
\]
Indeed, an extension is forbidden precisely when it would create a constant triple at the relevant end. If \(v\) is not completely alternating, its additional outgoing degree in \(H_n\) is \(1-r_{\mathrm{first}}(v)\) and its additional incoming degree is \(1-r_{\mathrm{last}}(v)\): the unique possible new bit must differ from the terminal bit, or respectively the unique preceding bit from the initial bit. If \(v\) is completely alternating, both additional degrees are zero and its original in- and out-degrees are already equal. Thus every vertex in \(H_n\) has equal in- and out-degree. Since \(G_n\) is strongly connected, \(H_n\) has an Eulerian circuit. Its edge labels form a circular cover of length
\[
|\mathcal R_n|+|\mathcal X_n|.
\]
All its windows avoid the forbidden triples because every edge belongs to \(\mathcal R_n\).

Deleting the first and last letters gives a bijection between the admissible length-\(n\) words with unequal first pair and unequal last pair and \(\mathcal R_{n-2}\): reconstruct the deleted letters as the complements of the now-exposed endpoint letters. Exactly two such words are fully alternating. Therefore
\[
|\mathcal X_n|=|\mathcal R_{n-2}|-2=2F_{n-1}-2.
\]
This proves the upper bound in the theorem.

**4. A lower bound even allowing forbidden extra windows.** Define the following potential on **every** binary word \(v\) of length \(m\), including vertices not in \(G_n\): let \(a(v)\in\{0,\ldots,m-1\}\) be the number of consecutive unequal neighboring pairs from the beginning of \(v\) before its first equal pair (or \(m-1\) when \(v\) is completely alternating), and put \(\phi(v)=-a(v)\).

For *every* binary length-\(n\) word \(w\), the de Bruijn shift \(p(w)\to s(w)\) satisfies
\[
\phi(s(w))-\phi(p(w))\leq1. \tag{1}
\]
To verify this, if the prefix begins with equal bits then its alternating-prefix count is zero and the inequality is immediate. If its first equal pair occurs later, shifting discards one initial unequal pair and decreases \(a\) by exactly one. If the prefix is fully alternating, shifting either leaves \(a\) unchanged or decreases it by one. Furthermore, for each \(w\in\mathcal X_n\), the first equal pair occurs strictly after the first pair and strictly before the last pair, hence
\[
\phi(s(w))-\phi(p(w))=1. \tag{2}
\]

The degrees in \(H_n\) are balanced, so the total potential increment summed over its multiset of arcs is zero. By (2), the sum of the potential increments over one copy of every required arc is therefore \(-|\mathcal X_n|\). Now take **any** circular word containing every member of \(\mathcal R_n\), even if it contains forbidden additional windows. Its windows form a closed walk in the unrestricted binary de Bruijn graph. Distinguish one occurrence of each required arc; call all remaining occurrences supplementary. Their potential increments must sum to \(+|\mathcal X_n|\), because increments telescope to zero around the closed walk. By (1), each supplementary arc contributes at most one. Hence at least \(|\mathcal X_n|\) supplementary windows are necessary. The total length is at least
\[
|\mathcal R_n|+|\mathcal X_n|
=2F_{n+1}+2F_{n-1}-2.
\]
The Eulerian construction reaches this bound. This completes the proof for every integer \(n\geq3\).

## Verification
`verify.py` (Python standard library) reconstructs \(\mathcal R_n\), \(\mathcal X_n\), all degree balances, connectivity, an explicit Eulerian cover, exact cyclic-window multiplicities, the potential inequalities on **all** binary arcs, and the Fibonacci formula for every order \(3\leq n\leq16\). Its observed terminal marker is `VERIFY_OK`. `crosscheck.py` independently calculates the finite directed postman augmentation minimum for \(3\leq n\leq13\), using pairwise de Bruijn overlap distances and a self-contained Hungarian assignment algorithm; it returned `CROSSCHECK_OK`. The table `witnesses.csv` gives deterministically reconstructed optimal circular sequences for \(3\leq n\leq12\). Run `python3 verify.py` and `python3 crosscheck.py` with no third-party dependencies.

The finite computations corroborate the proof but are not an exhaustive verification of infinitely many orders. The complete all-order argument is the explicit balancing construction and the universal potential inequality in the preceding section.

## Relationship to prior work
Moreno's *De Bruijn sequences and De Bruijn graphs for a general language* (2005; thesis chapter 3) and Moreno–Matamala's *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (arXiv:0711.1695, 2007, pp. 1–9) analyze exact-once restricted de Bruijn cycles and lexicographically minimal Eulerian traversals. Their exact-once/periodic-language formulation does not provide the present shortest repeated-window cover of **all ordinary finite admissible factors**: for instance, at order four the ten admissible factors do not form a balanced de Bruijn graph, and the optimum instead has length twelve. The 2007 paper's use of *minimum* refers to lexicographic order, not minimum length with repetitions.

Chee, Etzion, Nguyen, Ta, Tran and Vu, *Maximum Length RLL Sequences in de Bruijn Graph* (arXiv:2403.01454, first posted 2024), considers long sequences with distinct run-length-constrained windows and emphasizes maximum distinct-window length, rather than minimum length covering **every** allowed finite factor, with repetitions permitted. Classical Eulerian traversal and directed route-inspection methods underlie the framework; the contribution here is the explicit all-order optimal augmentation and a matching potential bound for this symmetric two-forbidden-factor language. No claim of independent historical-priority certification is made.

## Limitations
The exact theorem is specific to the binary constraint forbidding both constant triples, to one circular covering word, and to ordinary finite length-\(n\) factors. It does not classify all optimal covers, give analogous formulas for longer maximum-run constraints or different alphabets, or optimize *linear* covering strings. No physical-channel or synchronization-error correction guarantee is inferred. The originality assessment is limited to the sources and comparisons recorded in `AUDIT.json`; a previously unindexed equivalent identity would supersede the priority claim.

## References
1. E. Moreno, *De Bruijn sequences and De Bruijn graphs for a general language*, Information Processing Letters 96 (2005), 214–219; text included as chapter 3 of *De Bruijn graphs and sequences in languages with restrictions*, University of Chile thesis, 2005. https://www.dim.uchile.cl/~emoreno/publicaciones/FINALES/tesis04_De_Bruijn_sequences_and_graphs_in_restricted_languages.pdf
2. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695, 12 November 2007. https://arxiv.org/abs/0711.1695
3. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454, 3 March 2024. https://arxiv.org/abs/2403.01454
