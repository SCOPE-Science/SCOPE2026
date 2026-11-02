# The first even-length group-complexity gaps and their recovery in the Thue–Morse word

## Finding
Let \(\mathbf t=011010011001\cdots\) be the fixed point beginning in \(0\) of the morphism \(\mu(0)=01\), \(\mu(1)=10\). Write \(F_n\) for its set of distinct length-\(n\) factors. For a subgroup \(G\le S_n\), let \(p_G(n)\) be the number of intersections of \(F_n\) with the \(G\)-orbits on all binary words of length \(n\); equivalently, \(p_G(n)=|F_n/{\sim_G}|\).

The exact attainable spectra at the first two nontrivial even lengths are
\[
\{p_G(4):G\le S_4\}=\{3,4,5,6,7,8,10\},
\]
\[
\{p_G(6):G\le S_6\}=\{3,4,5,6,7,8,9,10,11,12,13,14,16\}.
\]
In particular, the penultimate values \(9\) and \(15\) are respectively absent. In contrast, the length-eight penultimate value is attained: \(|F_8|=22\), and the involution
\[
\sigma=(1\ 2)(3\ 8)(4\ 5)(6\ 7)
\]
satisfies \(p_{\langle\sigma\rangle}(8)=21\). Its unique nonsingleton intersection of a permutation orbit with \(F_8\) is \(\{01001011,10110100\}\).

These statements concern attainable group-complexity values, not the number of possible subgroups or the general all-length spectrum.

## Assumptions and scope
The alphabet is exactly the labeled binary alphabet \(\{0,1\}\), and the symmetric group acts by arbitrary coordinate permutations. Every subgroup of \(S_4\) or \(S_6\) is permitted; only the particular displayed cyclic subgroup is required at length eight. Here a permutation in one-line notation \([b_1,\ldots,b_n]\) sends position \(i\) to \(b_i\). Using the inverse coordinate action instead produces identical subgroup orbit partitions because groups are closed under inversion.

## Proof
**Finite-factor lemma.** Fix \(n\ge2\), and put \(m=\lceil\log_2n\rceil\). Then
\[
F_n=\bigcup_{a,b\in\{0,1\}} \operatorname{Factors}_n\bigl(\mu^m(ab)\bigr).
\]
To prove it, partition the infinite Thue–Morse word into consecutive length-\(2^m\) blocks \(\mu^m(t_i)\). A factor of length \(n\le2^m\) meets at most two such blocks, hence belongs to the right side for a neighboring letter pair \(t_it_{i+1}\). All four binary bigrams occur in the word (already in \(\mu^3(0)=01101001\)), so each factor on the right also occurs in the infinite word. Thus the finite computation is exhaustive, rather than a prefix-sampling heuristic.

The lemma produces \(|F_4|=10\), \(|F_6|=16\), and \(|F_8|=22\). At lengths four and six, the observed numbers of ones in factors each take precisely three values; the full symmetric group therefore gives the lower bound \(p_G(n)\ge3\), with equality attained by \(G=S_n\).

**Penultimate exclusion.** For a finite factor set \(F\) of size \(r\), suppose a subgroup \(G\) identifies exactly one pair of members of \(F\), so that it has \(r-1\) classes. Some element \(g\in G\) maps these two distinct factors to each other. The cyclic subgroup \(\langle g\rangle\le G\) already identifies that pair and cannot have fewer than \(r-1\) classes. Hence its class count is exactly \(r-1\). Consequently, to rule out the penultimate value for **every** subgroup it suffices to enumerate single permutations. The standalone verifier enumerates all \(4!=24\) and \(6!=720\) permutations, constructs their cyclic subgroups exactly, and computes their orbit intersections with the full factor sets provided by the lemma. None has class count \(9\) at length four or \(15\) at length six. This is a finite exhaustive proof of the two exclusions.

**Attainability.** The table `W4` and `W6` in `verify_tm_even_group_spectra.py` gives explicit sets of generating permutations for each displayed attainable value, including the trivial group for the ordinary complexity. The verifier generates each subgroup under composition, then counts equivalence classes by the canonical minimum of every factor's full group orbit. It confirms each target value. Since the trivial and full-group values are included and the penultimate ones were excluded for all subgroups, the two spectra are exact. As an independently organized cross-check, `verify_tm_six_subgroups.cpp` enumerates all \(1{,}455\) subgroups of \(S_6\) by adjoining arbitrary group elements and confirms the same attainable values.

**Length eight.** The finite-factor lemma gives the 22 factors. Applying the displayed order-two permutation to all 22 shows that only \(01001011\) and \(10110100\) are interchanged within the factor set; every other factor has a singleton intersection with its two-element orbit. Hence \(p_{\langle\sigma\rangle}(8)=21\). The complete check is executed in the same standalone verifier.

## Verification
Run `python3 verify_tm_even_group_spectra.py` using Python 3 standard libraries. The output in `verification_output.txt` lists the 24 and 720 checked permutations, validates all 20 witness generator sets, and checks the length-eight involution and unique pair. For an independent exhaustive subgroup census, compile `verify_tm_six_subgroups.cpp` with `g++ -O3 -std=c++17`, run it and compare with `subgroup_census_output.txt`. That census finds exactly 1,455 subgroups and, for length six, 18 attaining value 3, 82 attaining 4, 84 attaining 5, 220 attaining 6, 148 attaining 7, 366 attaining 8, 85 attaining 9, 277 attaining 10, 8 attaining 11, 111 attaining 12, 6 attaining 13, 49 attaining 14, and 1 attaining 16. These counts total 1,455. The main proof does not depend on taking the published subgroup-count total on trust.

## Relationship to prior work
Launer, Puzynina and Voloshinova (2026) study which values of group complexity are attainable and prove, by an antipodal-pair argument, that certain odd-length values for complement-closed binary words are impossible. Their argument does not yield the two even-length spectra above: at even length, a balanced factor may belong to the same positional orbit as its complement. This is precisely the distinction illustrated by the length-eight witness. Charlier, Puzynina and Zamboni (2015) developed the underlying group-complexity framework and generalized Morse–Hedlund bounds; their bound does not give these attainable-value sets. A 2017 presentation gives one specific length-four Thue–Morse group-complexity value \(7\), not the full spectrum.

## Limitations
There is no general theorem for arbitrary even lengths, and no claim that the length-eight subgroup is the only one attaining 21. The finite exhaustive argument for excluding penultimate values is limited to lengths four and six. The subgroup-census multiplicities are corroborative data, not needed for the displayed theorem. Potential implicit prior coverage in older group-action examples cannot be excluded without independent literature review.

## References
1. M. Launer, S. Puzynina and E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620v1 (first public 2026-07-08), particularly Section 4, Proposition 1. https://arxiv.org/html/2607.07620
2. É. Charlier, S. Puzynina and L. Q. Zamboni, *On a group theoretic generalization of the Morse–Hedlund theorem*, arXiv:1505.03848v2 (2015), particularly Section 2. https://arxiv.org/pdf/1505.03848
3. É. Charlier, *Permutation groups and the Morse–Hedlund theorem*, 2017 presentation, length-four Thue–Morse group-action example. https://www.discmath.ulg.ac.be/charlier/Charlier-expose-Londres2017.pdf
