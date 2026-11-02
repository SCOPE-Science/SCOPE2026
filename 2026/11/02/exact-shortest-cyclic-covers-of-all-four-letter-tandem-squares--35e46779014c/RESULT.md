# Exact shortest cyclic covers of all four-letter tandem squares

## Finding

**Theorem.** For an integer \(q\ge 2\), let \(\Sigma=\{0,1,\ldots,q-1\}\) and let \(\mathcal T_q=\{abab:a,b\in\Sigma\}\) denote the full family of \(q^2\) four-letter tandem squares, including the constant words \(aaaa\). The shortest length of a **single cyclic word** containing all members of \(\mathcal T_q\) as cyclic consecutive factors is
\[
\boxed{L(q)=2q(q+1).}
\]
An explicit order of the targets attains equality for every \(q\). In particular, \(L(2)=12\), \(L(3)=24\), and \(L(4)=40\).

## Assumptions and scope

A cyclic word of length \(N\) is an indexed sequence \((w_0,\ldots,w_{N-1})\) over \(\Sigma\); its length-four factor at \(i\) is \((w_i,w_{i+1},w_{i+2},w_{i+3})\) with indices reduced modulo \(N\). The alphabet labels are fixed. The target family consists of **all** tandem squares with two-letter root, with repeated-root-symbol cases included. The covering word may contain additional, non-target length-four factors and repeated occurrences of a target. The result concerns one cyclic source, not a collection of separately cyclic sources or a target-exact universal cycle.

For distinct target words \(U,V\) define their shift cost \(c(U,V)=4-\operatorname{ov}(U,V)\), where \(\operatorname{ov}\) is their longest suffix-prefix overlap of length at most three. We use this value only for distinct targets.

## Proof

**1. Passage from a cover to a target tour.** In any cyclic cover choose one occurrence of each of the \(q^2\) distinct target factors, and list the chosen starts in cyclic order, giving a cyclic permutation \((U_1,\ldots,U_{q^2})\) of the targets. Let \(d_i\) be the forward distance between starts of consecutive chosen occurrences, with cyclic wraparound. Their sum is the length \(N\). If \(d_i<4\), the two length-four windows overlap in exactly \(4-d_i\) aligned symbols, so this overlap is a suffix-prefix overlap. If \(d_i\ge4\), then trivially \(d_i\ge c(U_i,U_{i+1})\). Thus in every case
\[
N=\sum_i d_i\ \ge\ \sum_i c(U_i,U_{i+1}). \tag{1}
\]
The chosen starts must differ because they are occurrences of different target factors, so all distances are positive.

**2. Every distinct-target shift costs one, three or four.** Write a target as \(abab\). A length-two overlap with another target \(cdcd\) would equate \(ab\) with \(cd\), forcing the targets to be identical. A length-three overlap requires \(bab=cdc\), hence \(cdcd=baba\); for distinct targets this occurs precisely when \(a\ne b\). Every other consecutive pair has shift cost three if the last letter of the first target equals the first letter of the next, and shift cost four otherwise. Let \(x\) count the shift-one transitions in the cyclic target tour, let \(z\) count shift-four transitions, and let \(m=\binom q2\). The remaining \(q^2-x-z\) transitions cost three. Therefore
\[
\sum_i c(U_i,U_{i+1})=3q^2-2x+z. \tag{2}
\]
A shift-one transition can occur only between the paired distinct targets \(abab\) and \(baba\), associated with the unordered pair \(\{a,b\}\). Both opposite transitions cannot occur for the same pair, since they would form an isolated directed two-cycle in the cyclic ordering of more than two targets. Hence \(x\le m\). Set \(s=m-x\).

**3. The letter-connectivity obstruction.** For each of the \(x\) used shift-one transitions, contract its adjacent two targets into one block. The contracted block has the same first and last symbol: either \(abab,baba\), beginning and ending in \(a\), or the reverse, beginning and ending in \(b\). Each constant target \(aaaa\) is also a one-target block with the same first and last symbol \(a\). Each of the remaining \(2s\) nonconstant target words is a one-target block: \(abab\) starts in \(a\) and ends in \(b\), and its opposite \(baba\) starts in \(b\) and ends in \(a\).

The contracted blocks still form one cyclic ordering. Every interblock transition of shift three joins **equal** boundary letters; a shift-four transition joins **different** boundary letters. Viewed as a closed walk of letter states, the cyclic block ordering therefore moves between distinct letter states only on (i) the unmatched one-target blocks arising from the \(s\) unused unordered pairs, or (ii) the \(z\) shift-four transitions. The \(s\) unmatched pairs contribute at most \(s\) distinct undirected edges on the letter set; each shift-four transition contributes at most one more. All \(q\) letter states are visited, because the constant blocks \(aaaa\), one per symbol, occur in the tour.

If \(s\ge1\), the induced underlying letter graph is connected and needs at least \(q-1\) distinct edges. Hence \(s+z\ge q-1\), and therefore \(2s+z\ge q\). If \(s=0\), all blocks start and end in the same symbol, so only shift-four transitions change the letter state. A closed walk visiting all \(q\ge2\) states must make at least \(q\) state changes, yielding \(z\ge q\). In either case
\[
2s+z\ge q. \tag{3}
\]
Combining (1)–(3) and \(2m=q(q-1)\) gives
\[
N\ge 3q^2-2(m-s)+z
=2q^2+q+2s+z
\ge 2q(q+1).
\]

**4. An attaining single-cycle construction.** Form a list of all targets by concatenating groups indexed by \(a=0,1,\ldots,q-1\). Group \(a\) starts with \(aaaa\) and then, for each \(b>a\) in increasing order, lists \(abab\) immediately followed by \(baba\). Each ordered target occurs exactly once. Consecutive targets **within** a group have shift cost three, except the designated ordered pairs \(abab\to baba\), which have shift cost one. The transition between consecutive groups has cost four, as does the transition from the last group back to the first group. There are precisely \(m\) shift-one transitions, \(q\) shift-four transitions and \(q^2-m-q\) shift-three transitions. Their cost sum is
\[
m+4q+3(q^2-m-q)=2q(q+1).
\]
Spell the target list by writing the first target in full, then appending the nonoverlapping suffix of each next target. Because the final-to-first transition has cost four, this string, interpreted cyclically, has the asserted length and contains every listed target. Thus equality is achieved, proving the theorem. \(\square\)

## Verification

The standalone `verify.py` is part of the package and uses only the Python standard library. It constructs and inspects all target cycles for \(2\le q\le50\), checks the exact length and occurrences of all \(q^2\) target words, and checks the expected transition cost counts. An independent Held–Karp subset dynamic program exhaustively searches all target-order Hamiltonian tours for \(q=2,3,4\), finding respective optima \(12,24,40\). A separate exhaustive check rules out all binary cyclic covering words shorter than length \(12\). All tests passed. The general lower bound above is a mathematical proof and does not rest on finite enumeration.

Reproduce with `python3 verify.py` in a directory containing that file. Runtime scales exponentially for the independent dynamic program, which is intentionally restricted to the stated small alphabet sizes.

## Relationship to prior work

Chen, Kitaev and Sun [1] investigate universal cycles or universal words for restricted sets of words, with exact-once coverage and existence questions. Gardner and Godbole [2] establish universal-cycle results for other structured word families. Sawada, Sears, Trautrim and Williams [3] give general constructions of de Bruijn sequences and universal cycles by concatenation. Cazaux, Juhel and Rivals [4] study general shortest-linear-superstring bounds and distinguish the broader shortest-cyclic-cover problem. None of the inspected results gives the exact optimum for covering **all** four-letter tandem squares in **one** cyclic word. The prescribed motif family, single-cycle requirement and exact length formula are essential to the statement; merely recognizing a general shortest-superstring formulation would not yield the bound without the letter-connectivity argument.

## Limitations

The proof covers precisely root-length-two squares \(abab\), all labeled alphabets of size \(q\ge2\), and cyclic covers permitting extra factors. It does not determine analogous minima for longer squares, for cover words required to contain no additional factors, or for a linear rather than cyclic source. Prior literature searches cannot exclude an equivalent result under different motif or superstring terminology. Finite computation only corroborates selected cases. No independent scientific audit has been performed.

## References

[1] Chen, Kitaev and Sun, *On the probability of existence of a universal cycle or a universal word for a set of words* (first public 2019-08-03), https://arxiv.org/abs/1908.01116.

[2] Gardner and Godbole, *Universal Cycles of Restricted Words* (first public 2017-11-19), https://arxiv.org/abs/1711.07029.

[3] Sawada, Sears, Trautrim and Williams, *Concatenation trees: A framework for efficient universal cycle and de Bruijn sequence constructions* (first public 2023-08-23), https://arxiv.org/abs/2308.12405.

[4] Cazaux, Juhel and Rivals, *Practical lower and upper bounds for the Shortest Linear Superstring*, SEA 2018, https://doi.org/10.4230/LIPIcs.SEA.2018.18.
