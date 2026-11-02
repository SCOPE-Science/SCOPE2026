# Complete Tribonacci three-pseudoperiod census through substitution length \(1705\)

## Finding

Let \(\tau\) be the infinite fixed point beginning in \(0\) of the substitution \(\mu(0)=01\), \(\mu(1)=02\), \(\mu(2)=0\). Call a strictly increasing triple of positive integers \((a,b,c)\) a *three-pseudoperiod* if, for every integer \(i\geq0\), at least one of \(\tau_i=\tau_{i+a}\), \(\tau_i=\tau_{i+b}\), and \(\tau_i=\tau_{i+c}\) holds.

**Theorem (exact finite cutoff).** Among all triples with \(1\leq a<b<c\leq1705=|\mu^{12}(0)|\), exactly **145217** are three-pseudoperiods of the *infinite* word \(\tau\). The accompanying `triples.csv` gives the complete set in increasing lexicographic order, not just a count. In particular, for the natural substitution-length cutoff \(C\), the number \(N(C)\) of three-pseudoperiods with largest shift at most \(C\) is:

| \(C\) | 7 | 13 | 24 | 44 | 81 | 149 | 274 | 504 | 927 | 1705 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(N(C)\) | 1 | 4 | 15 | 55 | 207 | 801 | 2648 | 9604 | 37596 | 145217 |

The sole three-pseudoperiod at cutoff \(7\) is \((4,6,7)\).

## Assumptions and scope

All positions start at zero; shifts are strictly positive and distinct; the alphabet is the labeled set \(\{0,1,2\}\). The claim concerns the infinite fixed point and **only** triples with maximum shift at most \(1705\). It does not classify triples with larger shifts. This cutoff is the twelfth iterate's length, not an inferred natural asymptotic threshold.

## Proof

**Lemma 1 (exact adjacent-letter language).** The length-two factors of \(\tau\) are precisely \(00,01,02,10,20\). Indeed, the only internal adjacent pairs of the substituted letters are \(01\) and \(02\); every image begins with \(0\), while an image ends in \(0\), \(1\), or \(2\), so every boundary pair is one of \(00,10,20\). Each of these five occurs in \(\mu^4(0)\), proving equality.

**Lemma 2 (finite factor universe for an infinite word).** Put \(L=1706\) and \(B_x=\mu^{14}(x)\) for each \(x\in\{0,1,2\}\). Their lengths are \(5768,4841,3136\), respectively. In particular each is at least \(L\). Let \(F\) denote the union of all length-\(L\) factors of \(B_xB_y\), over the five adjacent pairs \(xy\) in Lemma 1. Then \(F\) is exactly the set of length-\(L\) factors of \(\tau\). For inclusion from right to left, factorize \(\tau=\mu^{14}(\tau)\) into the successive blocks \(B_{\tau_0}B_{\tau_1}\cdots\): a window of length \(L\), starting anywhere within a block of length at least \(L\), cannot extend beyond the next block. For the reverse inclusion, every adjacent pair \(xy\) actually occurs in \(\tau\); its image \(B_xB_y\) consequently occurs in \(\tau\). Both inclusions are exact, without any reliance on a finite-prefix stabilization heuristic. Exhaustive de-duplication yields \(|F|=3413\).

**Lemma 3 (finite cover criterion).** Fix \(1\leq a<b<c\leq1705\). The three-pseudoperiod condition is equivalent to the following finite statement:

\[
\forall w\in F:\quad w_0\in\{w_a,w_b,w_c\}.
\]

This follows immediately from Lemma 2, since all four positions lie inside a length-\(1706\) window. Every position in the infinite word begins such a window, and every window in \(F\) appears at some position.

**Exhaustive exact evaluation.** For each \(w\in F\), form its set of *matching shifts*
\[
M(w)=\{j\in\{1,\ldots,1705\}:w_j=w_0\}.
\]

For each first pair \(a<b\), initialize candidate third shifts \(Q=\{b+1,\ldots,1705\}\). For every distinct \(M(w)\) with \(a,b\notin M(w)\), replace \(Q\) by \(Q\cap M(w)\). Emit precisely the triples \((a,b,c)\) with \(c\in Q\). By Lemma 3, this procedure emits every permissible pseudoperiod once and no impermissible triple. `census.py` implements this exhaustive finite computation using arbitrary-precision integer bitsets; its exact output is `triples.csv`, which has **145217 data rows**. The row count and all displayed cutoff counts follow by exact integer counting of this complete list. Thus the mathematical reduction plus the full exact enumeration establish the infinite-word claim.

## Verification

Run `python3 census.py reproduced.csv` to regenerate the full table, followed by `python3 verify.py triples.csv`. The verifier checks the canonical table's SHA-256 (`03a725ce29a938e5315b6d4f164a788f1b8f90ddde93db8f32fe0f99a2c65c74`) and exact row ordering, independently enumerates factors from the finite prefix \(\mu^{18}(0)\), confirms that its \(3413\) factors coincide *exactly* with Lemma 2's supertile factors, recomputes the whole census using separately assembled masks, compares all **145217 triples**, verifies the cutoff table, and exercises direct position checks. All checks return `VERIFY_OK` on the supplied artifacts. The two factor constructions offer an independent computational cross-check; the logical reason this finite computation controls the **infinite** word is Lemma 2.

## Relationship to prior work

Meleshko, Ochem, Shallit, and Shan prove that the Tribonacci word has the pseudoperiod \((4,6,7)\), establish that it has no two-pseudoperiod, and explicitly pose Open Problem 30: characterize *all* its three-pseudoperiods. Their result does not provide the count, table, or exact finite cutoff reached here. This result gives a complete certified initial segment of that open classification rather than purporting to solve the all-shifts problem. Similar bounded word-factor queries can be solved using substitutions, but the particular enumeration and its precise shift cutoff are not obtained simply from the paper's one example.

## Limitations

No description of three-pseudoperiods with maximum shift greater than \(1705\) is established. No rational generating function, automaton characterization, or asymptotic formula is claimed. Originality beyond the inspected sources cannot exclude an uncatalogued equivalent finite census. The standalone computation is exact for the stated bounded domain, not an infinite enumeration of every triple.

## References

- J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, first public July 20, 2022, §4.5 and Open Problem 30; https://arxiv.org/html/2207.10171v3 ; https://arxiv.org/abs/2207.10171 .
- The On-Line Encyclopedia of Integer Sequences, A080843 (Tribonacci word) and A000073 (Tribonacci lengths), https://oeis.org/A080843 and https://oeis.org/A000073 .
