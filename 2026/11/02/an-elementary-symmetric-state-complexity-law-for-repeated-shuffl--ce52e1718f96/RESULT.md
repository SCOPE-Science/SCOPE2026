# An elementary-symmetric state-complexity law for repeated shuffles of ordered-block words

## Finding
Let \(d\ge1\) and \(k\ge0\) be integers, let \(\Sigma=\{a_1,\ldots,a_d\}\) consist of distinct letters, and fix positive integers \(p_1,\ldots,p_d\). Put \(u=a_1^{p_1}a_2^{p_2}\cdots a_d^{p_d}\). Write \(L_{k,\mathbf p}=\underbrace{\{u\}\shuffle\cdots\shuffle\{u\}}_{k\text{ copies}}\), with \(L_{0,\mathbf p}=\{\varepsilon\}\), for the language of all interleavings that respect the order within each copy. Let \(\kappa(L)\) denote the number of states in its complete minimal deterministic finite automaton (DFA). Define \(e_r(\mathbf p)=\sum_{1\le j_1<\cdots<j_r\le d}p_{j_1}\cdots p_{j_r}\), with \(e_0=1\). Then

\[
\boxed{\kappa(L_{k,\mathbf p})=1+\sum_{r=0}^{d}e_r(\mathbf p)\binom{k}{r}.}
\]

The exact state complexity is invariant under every permutation of the block lengths \(p_1,\ldots,p_d\), although the corresponding languages generally differ. It is a degree-\(d\) polynomial in the number of shuffled copies, with leading coefficient \(p_1\cdots p_d/d!\). For \(p_1=\cdots=p_d=1\), it simplifies to \(1+\binom{k+d}{d}\). For two letters it specializes to \(2+k(p_1+p_2)+\binom{k}{2}p_1p_2\).

A companion exact membership theorem states that a word \(w\in\Sigma^*\) belongs to \(L_{k,\mathbf p}\) if and only if its final letter counts are \(|w|_{a_j}=kp_j\) for every \(j\), and every prefix \(v\) satisfies

\[
|v|_{a_{j+1}}\le p_{j+1}\left\lfloor\frac{|v|_{a_j}}{p_j}\right\rfloor\qquad(1\le j<d).
\]

## Assumptions and scope
The letters are pairwise distinct, the block lengths are strictly positive, and the alphabet is exactly \(\Sigma\). The shuffle operation preserves within-copy order and does not require the copies to be kept contiguous. A DFA is complete: every state has one transition on each letter, including a rejecting sink. Binomial coefficients with lower index exceeding their upper index are zero. The theorem includes \(k=0\), when the language is the singleton \(\{\varepsilon\}\) and its minimal complete DFA has two states. No claim is made for block words in which a letter reappears after a different letter, or for shuffles of nonidentical words.

## Proof
**1. Prefix characterization.** Each copy of \(u\) can emit a letter \(a_{j+1}\) only after completing its own \(p_j\) letters \(a_j\). If a prefix contains \(A_j\) letters \(a_j\), at most \(\lfloor A_j/p_j\rfloor\) copies can have completed that block. Hence the number \(A_{j+1}\) cannot exceed \(p_{j+1}\lfloor A_j/p_j\rfloor\). Total letter counts give the remaining necessary conditions.

Conversely, suppose a word has the required total counts and all the prefix inequalities. For each symbol \(a_j\), assign occurrences numbered \(1,\ldots,kp_j\) consecutively in batches of \(p_j\) to copies numbered \(1,\ldots,k\). When the \(t\)-th occurrence of \(a_{j+1}\) is read, it is assigned to copy \(c=\lceil t/p_{j+1}\rceil\). The inequality at that prefix implies \(c\le\lfloor A_j/p_j\rfloor\), so copy \(c\) has already completed its entire preceding block. Each copy consequently reads exactly \(u\), establishing sufficiency.

**2. Minimal quotient automaton.** Let \(\mathcal P\) be the set of integer count vectors \(\mathbf i=(i_1,\ldots,i_d)\) with \(0\le i_j\le kp_j\) and \(i_{j+1}\le p_{j+1}\lfloor i_j/p_j\rfloor\) for \(1\le j<d\). The prefix characterization gives a complete DFA whose non-sink states are the vectors in \(\mathcal P\); a letter increments its component when the new vector is admissible, otherwise it moves to the sink. The sole accepting vector is \((kp_1,\ldots,kp_d)\).

Every vector in \(\mathcal P\) is reachable: the sorted prefix \(a_1^{i_1}\cdots a_d^{i_d}\) obeys the prefix inequalities. Every such state has an accepting continuation: append the missing occurrences in increasing letter order, namely \(a_1^{kp_1-i_1}\cdots a_d^{kp_d-i_d}\). If two vectors are distinct, their accepting completions have different mandatory Parikh vectors \((kp_1-i_1,\ldots,kp_d-i_d)\); an accepting continuation of one cannot be an accepting continuation of the other. The sink has no accepting continuation. By Myhill–Nerode, all \(|\mathcal P|+1\) states are pairwise distinguishable, and therefore the constructed DFA is minimal.

**3. Exact lattice-point count.** For a feasible vector write \(i_j=p_jt_j+r_j\), where \(0\le t_j\le k\); when \(t_j=k\), necessarily \(r_j=0\), while otherwise \(0\le r_j<p_j\). Feasibility is equivalent to \(t_1\ge t_2\ge\cdots\ge t_d\), together with the condition \(r_j=0\) whenever \(j\ge2\) and \(t_j=t_{j-1}\). Indeed, a strict decrease \(t_j<t_{j-1}\) allows all \(p_j\) residues, whereas equality forces zero residue.

Fix the set \(J\subseteq\{2,\ldots,d\}\) of positions at which the level drops strictly, and put \(h=|J|+1\). There are \(\binom{k}{h}\) choices for the \(h\) distinct levels if \(t_1<k\); their combined residue multiplicity is \(p_1\prod_{j\in J}p_j\). There are \(\binom{k}{h-1}\) choices when \(t_1=k\); their residue multiplicity is \(\prod_{j\in J}p_j\). Therefore

\[
|\mathcal P|=\sum_{J\subseteq\{2,\ldots,d\}}\Bigg(\prod_{j\in J}p_j\Bigg)\left[\binom{k}{|J|}+p_1\binom{k}{|J|+1}\right].
\]

Split this sum into subsets of \(\{1,\ldots,d\}\) not containing and containing \(1\). The result is \(\sum_{r=0}^{d}e_r(\mathbf p)\binom{k}{r}\). Adding the sink proves the asserted formula. The symmetry in block lengths follows from the symmetric elementary polynomials. The degree and specializations follow directly from the formula, using Vandermonde's identity for the unit-block case. This completes the proof.

## Verification
The accompanying `checker.py` constructs actual finite shuffle languages directly by interleaving copies, independently derives their distinct right quotients by complete prefix/suffix enumeration, and compares the answer with the theorem. For ten explicit choices of block lengths and copy counts, it also enumerates all words with the required final letter composition and checks the claimed prefix inequalities. A separate test compares the formula with a direct lattice-vector enumeration in 600 parameter cases. Run `python3 checker.py`; it uses Python's standard library only. These finite checks are corroborative and are not used as proofs of the universal quantifiers.

## Relationship to prior work
Biegler, Daley and McQuillan (2009), *On the Shuffle Automaton Size for Words*, study shuffle automata for two words. Their Theorem 10 provides an exact count for two special periodic words with non-repeating underlying period, and Theorem 12 gives a quadratic upper bound for shuffles of two words built from a period whose skeleton has one section per letter. They do not state the present simultaneous exact formula for arbitrary positive block lengths and arbitrary numbers of identical copies. In particular, a quadratic upper bound does not determine the elementary-symmetric coefficients or permutation-invariance of the exact minimum.

Brzozowski et al. (2015, arXiv:1512.01187) derive general worst-case bounds for shuffling two regular languages. Their bounds do not specialize to an equality giving the fixed singleton-family formula here. Hoffmann (2021) studies regularity of *unbounded* iterated shuffle for commutative languages, which is a different operation and class from a specified finite number of copies of one ordered noncommutative word. The proof here is independent of any worst-case state-complexity upper-bound assumption.

## Limitations
The result covers strictly monotone block words with pairwise distinct stage letters and identical copies; it does not address repeated-letter skeletons, heterogeneous processes or unbounded shuffle closure. An exact earlier version of this polynomial under other terminology (for example, lattice-word or parallel trace recognition) cannot be excluded by bibliographic searching. The mathematical proof and finite checks do not independently certify historical priority or external validation.

## References
1. F. Biegler, M. Daley and I. McQuillan, *On the Shuffle Automaton Size for Words*, EPTCS 3 (2009), 79–89, arXiv:0907.5111, first submitted 2009-07-29. https://arxiv.org/abs/0907.5111
2. J. Brzozowski, G. Jirásková, B. Liu, A. Rajasekaran and M. Szykuła, *On the State Complexity of the Shuffle of Regular Languages*, arXiv:1512.01187, first submitted 2015-12-03. https://arxiv.org/abs/1512.01187
3. S. Hoffmann, *Regularity Conditions for Iterated Shuffle on Commutative Regular Languages*, arXiv:2103.09587 (2021). https://arxiv.org/abs/2103.09587
