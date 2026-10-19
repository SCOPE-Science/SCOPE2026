# Sharp half-period factor balance and cyclic run-gap rigidity

## Finding
Let \(u\) be a primitive nonconstant word over any finite alphabet, of length \(p\ge 2\), and let \(w=u^\omega\). For finite words \(v,F\), write \(|F|_v\) for the number of (possibly overlapping) occurrences of \(v\) wholly contained in \(F\). Define the optimal uniform factor-balance constant
\[
B(w)=\max_{v\in\operatorname{Fac}(w),\ v\ne\varepsilon}\ \sup_{\substack{F,G\in\operatorname{Fac}(w)\\ |F|=|G|}}\bigl||F|_v-|G|_v\bigr|.
\]
For each letter \(c\), list the lengths of the **cyclic maximal runs** of \(c\) in the period \(u\) in decreasing order, calling the first two \(R_1(c)\ge R_2(c)\), with \(R_2(c)=0\) if the letter has only one run. Put \(k=\lfloor p/2\rfloor\). Then:
\[
\boxed{1\le B(w)\le k,\qquad B(w)=k\ \Longleftrightarrow\ \exists c:\ R_1(c)-R_2(c)\ge k.}
\]
In particular, for all positive integers \(a,b\), the two-run binary word \(w=(0^a1^b)^\omega\) has the **exact** constant \(B(w)=\lfloor(a+b)/2\rfloor\). Thus the universal half-period bound is sharp at every period \(p\ge2\), with a complete structural characterization of equality across all finite alphabets.

## Assumptions and scope
The period \(p\) is **least**: no shorter positive period generates \(w\). Runs are computed cyclically, so a run wrapping across the end of \(u\) and its beginning is one run. For a letter absent from \(u\), its run list is empty and it plays no role. A word is primitive here if it is not a proper positive integer power. All comparison factors \(F,G\) are contiguous and of the same finite length; the tested pattern \(v\) may have any finite positive length. This is the exact optimal constant in the standard definition of uniform factor-balancedness, not the looser frequency-discrepancy normalization.

## Proof
**1. Reduction to circular incidence.** Fix a nonempty factor \(v\) of \(w\). Define \(S_v\subseteq\mathbb Z/p\mathbb Z\) as the residues at which occurrences of \(v\) begin, and put \(t=|S_v|\). For any factor \(F\) of length \(L\ge|v|\), starting at residue \(i\), the number of its occurrences of \(v\) equals the number of elements of the periodic indicator \(\mathbf1_{S_v}\) in an interval of \(M=L-|v|+1\) consecutive starting residues. Write \(M=qp+r\), with \(0\le r<p\). Every such interval contains exactly \(qt\) occurrences from its complete circuits; hence the difference between two equal-length factors depends only on the counts in circular arcs of length \(r\). If \(L<|v|\), both counts are zero.

**2. Sharp circular bound.** For any \(S\subseteq\mathbb Z/p\mathbb Z\) of size \(t\), a circular arc of length \(r\) contains between \(\max(0,r-(p-t))\) and \(\min(r,t)\) selected residues. Therefore its counting oscillation is at most \(\min(t,p-t)\le\lfloor p/2\rfloor\). Since this is uniform in \(v,L\), the upper bound follows. Since \(u\) is nonconstant, some letter occurs at some but not all positions. Comparing length-one factors shows \(B(w)\ge1\).

We also record the equality lemma. Put \(k=\lfloor p/2\rfloor\). The oscillation of length-\(r\) arcs equals that of the complementary length-\(p-r\) arcs, so it is bounded also by \(\min(r,p-r)\). If it equals \(k\), then necessarily both \(t\) and \(r\) belong to \(\{k,p-k\}\). If \(p=2k\), necessarily \(t=r=k\): one arc must contain all \(k\) selected residues and another none, so \(S\) is one circular block of \(k\) consecutive residues. If \(p=2k+1\), four cases remain: \((t,r)=(k,k),(k,k+1),(k+1,k),(k+1,k+1)\). In order, attaining the full gap forces, respectively, an arc of length \(k\) containing all \(S\), an arc of length \(k+1\) disjoint from \(S\), an arc of length \(k\) disjoint from \(S\), or an arc of length \(k+1\) containing all \(S\). In every case \(S\) or its complement is exactly the stated arc, so \(S\) itself is a single circular block of size \(k\) or \(k+1\). Conversely any such block attains oscillation \(k\) (choose a circular arc of length \(k\) inside it and one inside its complement, taking complements of arcs when the block has size \(k+1\)). Thus, for arbitrary \(p\ge2\):
\[
\max_{0\le r<p}\left(\max_i|S\cap[i,i+r)|-\min_i|S\cap[i,i+r)|\right)=k
\iff\ S\text{ is a circular interval of length }k\text{ or }p-k.
\]
Here the displayed intervals are interpreted modulo \(p\).

**3. Equality forces a dominant constant-letter run.** Suppose \(p\ge4\), so \(k\ge2\), and \(B(w)=k\). The equality lemma gives a factor \(v\) whose occurrence-start residues form a circular interval containing at least two consecutive positions. Hence \(v\) occurs starting at two adjacent positions in \(w\), and the overlap equations \(v_j=v_{j+1}\), for every consecutive pair inside \(v\), force \(v=c^\ell\) for some letter \(c\) and \(\ell\ge1\). A maximal cyclic run of \(c\) of length \(R\) contributes exactly \(\max(0,R-\ell+1)\) occurrence starts of \(c^\ell\). Since the full start set is one block of size \(t\in\{k,p-k\}\), precisely one run contributes, and all others contribute zero. Thus its length is \(R_1(c)=t+\ell-1\) and \(R_2(c)<\ell\). It follows that \(R_1(c)-R_2(c)\ge t\ge k\).

Conversely suppose \(R_1(c)-R_2(c)\ge k\). Choose the pattern \(v=c^\ell\) with \(\ell=R_1(c)-k+1\ge1\). The longest cyclic run then contributes exactly \(k\) consecutive occurrence starts, and every other cyclic run is shorter than \(\ell\), so contributes none. The equality lemma gives \(B(w)=k\). The argument is valid for \(p\ge4\), and also proves sufficiency for \(p=2,3\). For those two smaller periods, every primitive nonconstant word has a letter occurring exactly once in its cyclic period, so its longest and second-longest runs have lengths \(1\) and \(0\), and the same criterion and equality follow. This proves the equivalence for every \(p\ge2\).

**4. Extremal family.** In \(u=0^a1^b\) each symbol occurs in a single cyclic run; one has length at least \(\lceil(a+b)/2\rceil\), with second-longest run length zero. The run gap therefore exceeds \(k=\lfloor(a+b)/2\rfloor\). The theorem gives \(B((0^a1^b)^\omega)=k\). The word \(u\) is primitive because it has exactly one cyclic transition from \(0\) to \(1\) and one from \(1\) to \(0\).

## Verification
A standalone Python checker enumerates occurrence residues of every distinct factor of lengths \(1\) through \(p\), enumerates circular arcs, and computes the exact optimum. For every primitive binary period of length \(2\) through \(9\) (974 periods) and every primitive ternary period of length \(2\) through \(7\) (3222 periods), it checks the universal bound and the run-gap criterion. Separately, its direct equal-length substring-counting algorithm checks all ternary periods and every binary two-run period in the ranges, without using cyclic indicator formulas. These tests corroborate the theorem; the preceding proof covers all periods, alphabets, factor lengths and positions. Run `python3 periodic_balance_checker.py`; expected output is in `periodic_balance_checker_output.txt`.

## Relationship to prior work
The quantitative notion of uniformly factor-balanced words is central to Espinoza, Popoli and Stipulanti, *Factor-balancedness, linear recurrence, and factor complexity*, arXiv:2602.03746v1 (first posted 2026-02-03), especially Sections 1, 3.1, 3.3, 4 and 5. Their general results give conditions for bounded factor-count differences, including linearly recurrent and substitutive settings. The theorem here instead gives an **optimal numerical constant**, a **sharp period-only universal bound**, and an **if-and-only-if classification of equality** for all primitive periodic words. Adamczewski's *Balances for fixed points of primitive substitutions*, Theoretical Computer Science 307 (2003), develops a broader background for balancedness but does not supply this stated cyclic run-gap criterion in the material examined. A search of relevant mathematical research records and nearby literature did not reveal this exact assertion; absence from a search is not a uniqueness proof.

## Limitations
The bound describes purely periodic words; ultimately periodic words with nonempty nonperiodic preperiod need not satisfy the same bound. The theorem does not give a closed form for \(B(w)\) when the run-gap equality criterion fails, although a finite cyclic-incidence computation determines it. The proof relies on a standard circular counting inequality, so an equivalent older combinatorial formulation could exist. No independently performed scientific audit or external validation is asserted.

## References
1. B. Espinoza, P. Popoli, M. Stipulanti, *Factor-balancedness, linear recurrence, and factor complexity*, arXiv:2602.03746v1, 2026-02-03. https://arxiv.org/html/2602.03746v1
2. B. Adamczewski, *Balances for fixed points of primitive substitutions*, Theoretical Computer Science 307 (2003), 47–75, DOI:10.1016/S0304-3975(03)00092-6.
