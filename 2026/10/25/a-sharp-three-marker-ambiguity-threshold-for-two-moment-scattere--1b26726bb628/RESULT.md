# A sharp three-marker ambiguity threshold for two-moment scattered-subword reconstruction

## Finding
For a binary word \(w\in\{a,b\}^{*}\), let \(\binom wu\) be the number of *scattered* occurrences of the subword \(u\), and observe only
\[
\mathcal O(w)=\bigl(|w|_a,|w|_b,\binom{w}{ab},\binom{w}{aab}\bigr).
\]
Every word of length at most six is uniquely determined by this observation. At length seven, exactly two observation fibers have size two, namely \(\{\mathtt{abbaaab},\mathtt{baaabba}\}\) and \(\{\mathtt{abbbaab},\mathtt{baabbba}\}\); every other fiber is a singleton. If a word has at most two occurrences of \(b\), its observation determines it uniquely, at *every* length.

More strongly, **unbounded ambiguity already occurs with exactly three occurrences of \(b\)**. For every integer \(r\ge1\), put
\[
R=7^r,\quad L=\lceil\sqrt R\rceil,\quad k=2L+1,\quad S=3L+1,\quad H=\frac{S^2+2R-3S}{6}.
\]
The integer-valued observation \(\mathcal O(w)=(k,3,S,H)\), for words of length \(2L+4\), has **exactly \(\lfloor r/2\rfloor+1\) distinct preimages**. In particular, the greatest fiber size grows without bound along these explicit lengths despite the fixed three-\(b\) restriction. No formula for the global maximum fiber size at arbitrary length is asserted.

## Assumptions and scope
The alphabet is the two-element ordered alphabet \(\{a,b\}\); words are linear, not circular. All scattered-subword multiplicities count strictly increasing selections of positions; adjacent positions are allowed. Both letter counts are included in the observation, although only one is independent when word length is supplied. Equality of observations is exact integer equality. All assertions concern finite words; the infinite construction is indexed by integer \(r\ge1\).

## Proof
**Step 1: exact moment encoding.** Let \(k=|w|_a\), \(m=|w|_b\). Enumerate the \(b\)'s from left to right and let \(0\le t_1\le\cdots\le t_m\le k\) be the number of preceding \(a\)'s. This sequence and the word determine one another uniquely: insert \(b\)'s after respectively \(t_i\) occurrences of \(a\). Directly counting subsequences gives
\[
S:=\binom{w}{ab}=\sum_{i=1}^m t_i,\qquad H:=\binom{w}{aab}=\sum_{i=1}^m\binom{t_i}{2},\qquad Q:=\sum_{i=1}^m t_i^2=2H+S.
\]
For \(m\le2\), the first two power sums determine the sorted sequence: for two terms the product is \((S^2-Q)/2\), so the unordered roots of \(z^2-Sz+(S^2-Q)/2\) are fixed. Thus the word is unique. Also, for \(k\le2\), each \(t_i\) lies in \(\{0,1,2\}\), and the three multiplicities are uniquely solved from \(m,S,Q\) (invertible Vandermonde system). Consequently, ambiguity requires \(k,m\ge3\).

**Step 2: the first collisions.** At length at most six the only potentially ambiguous case is \(k=m=3\). Enumerating the \(\binom63=20\) possible nondecreasing triples \((t_1,t_2,t_3)\) with \(0\le t_i\le3\) produces 20 distinct ordered pairs \((S,Q)\). The appended exact-integer checker reproduces this finite exhaustive step, independently via direct scattered-subword counting and via moments. At length seven the two possible nontrivial compositions are \((k,m)=(4,3),(3,4)\). The \(\binom73=35\) sorted triples with bound four yield one repeated moment pair, \((0,3,3)\) and \((1,1,4)\), which give the first stated doubleton. For \((k,m)=(3,4)\), let \(c_j\) be the number of \(b\)'s having \(j\) preceding \(a\)'s. The constraints fix \(\sum c_j\), \(\sum jc_j\), and \(\sum j^2c_j\), so two solutions differ by an integer multiple of \((1,-3,3,-1)\). Nonnegativity and total multiplicity four allow exactly one nontrivial pair, \((c_0,c_1,c_2,c_3)=(1,0,3,0)\) and \((0,3,0,1)\). These give the second doubleton. The remaining compositions have \(k\le2\) or \(m\le2\) and are unique.

**Step 3: exact norm reduction for three markers.** When \(m=3\), write \(x=t_2-t_1\ge0\), \(y=t_3-t_2\ge0\). Subtracting the first power sum from the second gives the exact identity
\[
3Q-S^2=2(x^2+xy+y^2).
\]
Thus the fixed observation \((k,3,S,H)\) corresponds bijectively to nonnegative lattice pairs solving
\[
x^2+xy+y^2=R:=\frac{3(2H+S)-S^2}{2},\quad 2x+y\equiv S\pmod3,
\]
subject to \(0\le (S-2x-y)/3\) and \((S+x+2y)/3\le k\). In fact, \(t_1=(S-2x-y)/3\), \(t_2=t_1+x\), \(t_3=t_2+y\), which proves both directions of this correspondence.

**Step 4: exact Eisenstein-norm count.** Let \(R=7^r\). The positive-definite form \(x^2+xy+y^2\) is the norm of \(x-y\omega\) in the Euclidean ring \(\mathbb Z[\omega]\), with \(\omega^2+\omega+1=0\). The prime 7 splits into the nonassociate conjugate norm-seven factors \(3+\omega\) and \(3+\omega^2\). Unique factorization, the six units, and \(r+1\) assignments of the two primes give exactly \(6(r+1)\) integral pairs of norm \(7^r\). The six unit rotations act by rotations of the norm lattice through \(60\) degrees, so the closed sector \(x,y\ge0\) contains \(r+1\) solutions when \(r\) is odd (no boundary solutions), and \(r+2\) when \(r\) is even (six boundary solutions are counted twice across sectors). Since \(7^r\equiv1\pmod3\), each sector solution has \(x-y\not\equiv0\pmod3\). The reflection \((x,y)\mapsto(y,x)\) has no fixed point on this norm shell and exchanges the two possible nonzero residues of \(2x+y\pmod3\); exactly half satisfy \(2x+y\equiv1\pmod3\). The resulting number is precisely
\[
\frac12\begin{cases}r+1&\text{if \(r\) is odd},\\r+2&\text{if \(r\) is even}\end{cases}=\lfloor r/2\rfloor+1.
\]

**Step 5: all selected lattice points are admissible.** Take \(L=\lceil\sqrt R\rceil\), \(k=2L+1\), and \(S=3L+1\). The congruence condition becomes \(2x+y\equiv1\pmod3\). For any nonnegative norm-\(R\) pair, \(2x+y\le2\sqrt R\le2L\) and \(x+2y\le2L\). Hence \(t_1=(3L+1-2x-y)/3\ge0\) and \(t_3=(3L+1+x+2y)/3\le2L+1=k\). The quantity \(H=(S^2+2R-3S)/6\) is integral because \(S=3L+1\) and \(R=7^r\equiv1\pmod3\), and nonnegative because it equals the resulting sum of binomial coefficients. Every selected norm point therefore determines a valid word with the announced observation, and every word in that fiber arises from one of these points. The exact fiber cardinality follows.

## Verification
Run `python3 verification/right_bounded_block_check.py` using Python 3 standard library only. The checker directly enumerates all binary words at lengths zero through ten, confirms two distinct length-seven doubletons and the absence of shorter collisions, independently matches the direct scattered-subword counts to the moment formula, and enumerates the norm-sector fibers at powers \(7^r\) for \(1\le r\le9\) together with actual word witnesses. The output ends in `RBB_TWO_MOMENT_PASS first_collisions=7 classes=2 growing_three_marker_fibers=1..9`. These finite checks complement, but do not replace, the all-\(r\) algebraic proof.

## Relationship to prior work
Fleischmann, Lejeune, Manea, Nowotka, and Rigo develop reconstruction from right-bounded-block scattered factors and the underlying integer equations, obtaining a sufficient family of at most \(\min(|w|_a,|w|_b)+1\) observations; that moment encoding and general reconstruction setting are antecedents, not original contributions here. Their Proposition 18 classifies a different two-query setting using letter counts and \(\binom{w}{ab}\). The present theorem concerns the **fixed** observations \(\binom{w}{ab}\) and \(\binom{w}{aab}\) and obtains an exact minimal collision threshold and arbitrarily large fixed-three-marker fibers. Richomme and Rosenfeld address adaptive subword/factor queries and do not imply the particular two-moment fiber law. The Eisenstein norm factorization is a classical arithmetic ingredient, not a novel number-theoretic statement.

## Limitations
Only this specific weak, nonadaptive two-moment observation is classified at the first collision and for the stated infinite norm-power family. A formula for arbitrary fibers or for the global maximum at every word length is not proved. Novelty remains conditional on discoverable and inspected literature; a differently phrased full-text result may still overlap. No independent mathematical audit has been carried out.

## References
1. P. Fleischmann, M. Lejeune, F. Manea, D. Nowotka, M. Rigo, *Reconstructing Words from Right-Bounded-Block Words*, arXiv:2001.11218 (initial public version January 30, 2020), especially Section 3, Lemma 17, Proposition 18, and Theorem 19. https://arxiv.org/pdf/2001.11218
2. G. Richomme and M. Rosenfeld, *Reconstructing Words Using Queries on Subwords or Factors*, STACS 2023, DOI:10.4230/LIPIcs.STACS.2023.52. https://drops.dagstuhl.de/storage/00lipics/lipics-vol254-stacs2023/LIPIcs.STACS.2023.52/LIPIcs.STACS.2023.52.pdf
3. Standard Euclidean factorization of Eisenstein integers \(\mathbb Z[\omega]\) and its six-unit norm representation count (used in the proof; no novelty asserted for this ingredient).
