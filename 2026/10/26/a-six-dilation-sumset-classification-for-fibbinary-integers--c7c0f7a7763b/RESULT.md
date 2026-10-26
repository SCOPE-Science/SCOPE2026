# A six-dilation sumset classification for fibbinary integers

## Finding

Let \(\mathcal F\) be the set of all nonnegative integers whose ordinary base-two representations contain no adjacent ones, including zero. For an integer \(d\ge1\), put \(S_d=\mathcal F+d\mathcal F=\{a+db:a,b\in\mathcal F\}\). Then the following is an exact classification for the first six positive multipliers:

\[
\begin{aligned}
\mathbb N_0\setminus S_1&=\varnothing,\\
\mathbb N_0\setminus S_2&=\varnothing,\\
\mathbb N_0\setminus S_3&=\varnothing,\\
\mathbb N_0\setminus S_4&=\{4j+3:j\ge0\},\\
\mathbb N_0\setminus S_5&=\{3\},\\
\mathbb N_0\setminus S_6&=\left\{\frac{4^k-7}{3}:k\ge2\right\}.
\end{aligned}
\]

The last exceptional set is \(\{3,19,83,339,1363,\ldots\}\), is infinite, has natural density zero, and satisfies the **exact** counting law, for every real \(X\ge0\),

\[
\#\{0\le n\le X:n\notin S_6\}
=\max\left(0,\left\lfloor\log_4(3X+7)\right\rfloor-1\right).
\]

Thus this first range of multipliers exhibits complete coverage, periodic positive-density exclusion, a single obstruction, and a sparse nonperiodic infinite family.

## Assumptions and scope

All addends and indices are nonnegative integers; zero is included in \(\mathcal F\). Representations use **ordered** pairs \((a,b)\) with unrestricted equality allowed and exact integer addition. The classification is asserted for precisely \(1\le d\le6\), not for general multipliers or the number of distinct representations. The standard representation of a positive integer has no leading zeros.

## Proof

**Step 1: exact digitwise representation automata.** Fix a multiplier \(d\) among the six. Write the digits of a proposed equality \(a+db=n\) from least to most significant, as \(a_i,b_i,n_i\in\{0,1\}\). Keep a state \((p,q,c)\), where \(p,q\) are the preceding digits of the two addends and \(c\) is the nonnegative carry. Initially \((p,q,c)=(0,0,0)\). On reading a prescribed next digit \(t\) of \(n\), choose \(u,v\in\{0,1\}\) with \(pu=qv=0\), put

\[
 z=u+dv+c,
 \qquad z\equiv t\pmod2,
 \qquad (p,q,c)\longmapsto(u,v,\lfloor z/2\rfloor).
\]

The restrictions on \(u,v\) are **equivalent** to both summands avoiding adjacent ones. Inductively \(0\le c\le d\) (since \(z\le1+2d\)), so the nondeterministic state set has at most \(4(d+1)\) elements. The digitwise identity is precisely the usual base-two carrying rule. For a canonical \(n>0\) with \(L\) digits, both addends are at most \(n\) and hence have at most \(L\) digits; therefore a path realizes \(a+db=n\) if and only if its final carry is zero. The case \(n=0\) is represented by \((a,b)=(0,0)\).

After reading a word, let \(Q\) be the *set* of reachable triples; the representation automaton is accepting precisely when a triple in \(Q\) has carry zero. On digit \(t\), its exact deterministic transition is the union of the above transitions over every triple in \(Q\). This determinization is finite, with no probabilistic or heuristic step.

**Step 2: independent proposed exception recognizers.** Read canonical binary words least-significant bit first, hence nonzero words always finish with a one. For \(d=1,2,3\), the exceptional language is empty. For \(d=4\), a word is exceptional exactly when its two low bits are `11`. For \(d=5\), the only exceptional word is `11` itself. For \(d=6\), the proposed exceptional language consists exactly of the word `11` and the words `11001` followed by zero or more copies of `01`, all written least-significant bit first. The latter words, reversed into ordinary notation, give precisely \((4^k-7)/3\) for \(k\ge3\); the word `11` gives the \(k=2\) term. These languages have the explicit deterministic recognizers encoded in `verify.py`.

**Step 3: complete finite equivalence certificate.** Form the product of the determinized representation automaton of Step 1 and the exception recognizer of Step 2. Start at the pair of initial states, and perform breadth-first enumeration of **every** reachable product state along **both** possible digit labels. For each reachable state and its outgoing digit-one edge, the two accepting indicators are opposite. This is the exact condition needed for every positive canonical binary expansion, because its final digit in least-significant-bit-first order is one. The special one-digit expansion of zero is tested separately. The exhaustive product-state sizes, in order \(d=1,\ldots,6\), are

\[
(4,6,18,9,41,29).
\]

The complete product transition tables, showing source-state subsets, target states, both outgoing edges, and accepting indicators, are in `state_table.txt`. The complete independent state-generation and comparison algorithm is `verify.py` (Python standard library). Because the full finite reachable graph has been enumerated with both outgoing edges for **each** vertex, this proves equivalence of the two languages at **all** lengths, not just to a cutoff. Steps 1 and 2 translate the accepted language back to the six claimed arithmetic identities.

**Step 4: exception enumeration.** For the sixth multiplier, \((4^k-7)/3\le X\) is equivalent to \(4^k\le3X+7\). Counting integers \(k\ge2\) satisfying this inequality gives the displayed exact formula. Consequently the complement of \(S_6\) has logarithmic counting growth, and natural density zero. The complement of \(S_4\) has density \(1/4\); the other four complements are finite or empty.

## Verification

Run `python3 verify.py`. This regenerates the reachable finite-state product graphs, compares every canonical ending-digit-one transition, and confirms the zero case. It also independently enumerates all sums \(a+db\le10000\) and compares membership with the six formulas. To regenerate the printed complete transition certificate, run `python3 verify.py --write-certificate state_table.txt` and compare the bytes to the supplied `state_table.txt`. The script uses only exact integer arithmetic and the Python standard library. The finite numerical enumeration is ancillary; the infinite assertions follow from complete finite-state reachability and the digitwise carrying lemma.

## Relationship to prior work

The fibbinary integers are OEIS A003714 and have the standard Zeckendorf-word interpretation. Macfarlane's 2024 papers study the fibbinary/Wythoff array and the complement of the original fibbinary set, not the mixed dilated sumsets \(\mathcal F+d\mathcal F\). Dekking's 2021 preprint develops methods for sumsets associated to substitution fixed points, with examples involving Beatty/Fibonacci-word, Thue--Morse, and von Neumann sets; its stated theorems do not cover this fibbinary six-dilation classification. These papers supply object and question motivation and useful nearby methods but do not state the geometric obstruction law proved here.

## Limitations

The result addresses only the first six positive dilations, including a structurally distinctive sixth case. It makes no assertion for \(d\ge7\), for representation multiplicities, or for other restricted digit languages. The proof is self-contained but uses an exhaustive finite-state certificate; its source and complete transition data accompany the text. The published-literature comparison does not establish publication priority against every unindexed source or every possible implicit consequence of earlier general automata techniques. No independent mathematical audit has been performed.

## References

1. A. J. Macfarlane, *On the fibbinary numbers and the Wythoff array*, arXiv:2405.18128 (first submitted 2024-05-28), https://arxiv.org/abs/2405.18128.
2. A. J. Macfarlane, *On the structure of the complement of the set of fibbinary numbers*, arXiv:2406.12455 (first submitted 2024-06-18), https://arxiv.org/abs/2406.12455.
3. F. Michel Dekking, *Sumsets and fixed points of substitutions*, arXiv:2105.04959 (first submitted 2021-05-11), https://arxiv.org/abs/2105.04959.
4. OEIS A003714, *Fibbinary numbers*, https://oeis.org/A003714.
