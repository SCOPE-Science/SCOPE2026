# Exact radix and reading-order state costs of modular base-four digit counting

## Finding

For every integer \(r\ge 2\), define \(d_3(n)\) as the number of digits equal to \(3\) in the ordinary base-four representation of \(n\ge 0\), and define the binary sequence
\[
 b_r(n)=\begin{cases}1,&d_3(n)\equiv0\pmod r,\\0,&\text{otherwise}.\end{cases}
\]
The exact number of states in a minimal complete deterministic finite automaton with output (DFAO) generating \(b_r\) is
\[
\boxed{\operatorname{sc}_{4,\mathrm{MSD}}(b_r)=r,\qquad
\operatorname{sc}_{2,\mathrm{MSD}}(b_r)=2r^2,\qquad
\operatorname{sc}_{2,\mathrm{LSD}}(b_r)=3r.}
\]
In all three conventions, every representation of the same nonnegative integer, including zero padding in the permitted input-reading convention, must produce the same output. More explicitly, a most-significant-digit-first (MSD) input allows arbitrary **leading** zeros, while a least-significant-digit-first (LSD) input allows arbitrary **trailing** zeros. The empty input may be used to represent zero. In particular, the recent nonregular-Abelian-complexity example \(b_3\) has minimal state counts \(3\), \(18\), and \(9\) in these respective conventions.

## Assumptions and scope

A DFAO is a complete deterministic automaton with a fixed output in \(\{0,1\}\) at every state; its size is the number of reachable, pairwise output-distinguishable states. In the MSD convention, a word of digits is read left to right in the usual order. In the LSD convention, the least significant digit is read first. For a binary input \(w\), the base-four representation of its numerical value is obtained by grouping the binary digits in consecutive pairs from the right, with an additional leading \(0\) when needed. A base-four digit \(3\) is precisely the binary pair \(11\). The modulus \(r\) is fixed but otherwise arbitrary in \(\{2,3,\ldots\}\); no primality assumption is needed. The state counts concern the indicator output \(b_r\), not the full residue output \(d_3\pmod r\).

## Proof

**The base-four MSD automaton.** Use state space \(\mathbb Z/r\mathbb Z\), initial state \(0\), output \(1\) only at residue \(0\), and transition \(x\mapsto x+1\) on digit \(3\), with the other three digits fixing the state. It computes \(b_r\), ignores leading zeros, and reaches all \(r\) states using repetitions of \(3\). Two distinct residues are distinguished by appending sufficiently many copies of \(3\), proving \(\operatorname{sc}_{4,\mathrm{MSD}}=r\).

**The binary MSD automaton.** Its states are triples \((u,v,e)\in(\mathbb Z/r\mathbb Z)^2\times\{0,1\}\), initially \((0,0,0)\), with output \(1\) exactly when \(u=0\). The transitions are
\[
 T_0(u,v,e)=(v,u,0),\qquad T_1(u,v,e)=(v+e,u,1).
\]
To establish their interpretation, index the letters of a binary prefix \(w\) starting at \(1\). Let \(E(w)\) count occurrences of \(11\) ending at positive **even** positions, and \(O(w)\) count occurrences ending at **odd** positions; indices below \(2\) contribute nothing. If \(|w|\) is even, take \((u,v)=(E(w),O(w))\pmod r\); if it is odd, take \((u,v)=(O(w),E(w))\pmod r\). Set \(e\) equal to the last digit of \(w\), or \(0\) for the empty prefix. Appending a digit \(z\) changes which of the two parity counts is the right-aligned count; its only new adjacent \(11\) is formed exactly when \(ez=1\). Therefore the updated triple is \((v+ez,u,z)\). The right-aligned count is \(u\); consequently this automaton computes \(b_r\). An initial \(0\) leaves its start state unchanged, as required for arbitrary leading zero padding.

All \(2r^2\) states are reachable. On any state with third coordinate \(0\), direct substitution in the transition formulas gives
\[
 T_{1100}(u,v,0)=(u+1,v,0),\qquad
 T_{0110}(u,v,0)=(u,v+1,0).
\]
Repeatedly applying these two words reaches every \((u,v,0)\) from the initial state; appending \(1\) takes \((v,u,0)\) to \((u,v,1)\), reaching every remaining state.

They are pairwise distinguishable. For any starting state, appending \(00\) produces \((u,v,0)\). Thus the suffix \(00(1100)^t\) produces an output determined by \(u+t\pmod r\), and \(00(0110)^t0\) produces an output determined by \(v+t\pmod r\). Varying the nonnegative integer \(t\) separates any pair whose first or second coordinates differ. If two states have the same \((u,v)\) but different \(e\), the suffix \(1\) takes them to states whose first coordinates differ by \(1\pmod r\), after which the preceding distinguishing suffix applies. Therefore all \(2r^2\) states are Myhill--Nerode-distinct. This proves \(\operatorname{sc}_{2,\mathrm{MSD}}=2r^2\).

**The binary LSD automaton.** Use \(3r\) states \(N_x,P_{x,0},P_{x,1}\), with \(x\in\mathbb Z/r\mathbb Z\). The residue \(x\) counts completed right-aligned \(11\) digit pairs, and \(N\) means no bit is pending, whereas \(P_{x,b}\) means one low bit \(b\) is waiting for its high bit. Start at \(N_0\). All three state types output \(1\) exactly when \(x=0\). Their transitions on a digit \(z\in\{0,1\}\) are
\[
 N_x\xrightarrow{z}P_{x,z},\qquad
 P_{x,b}\xrightarrow{z}N_{x+bz}.
\]
This computes \(b_r\), since each completed pair increases the residue exactly when it is \(11\). If the input stops with a pending low bit, the missing high bit is zero and changes nothing. Appending a trailing zero to an LSD representation therefore does not change the output. All \(N_x\) are reachable from \(N_0\) using \((11)^x\), where representatives \(0\le x<r\) are taken; reading one more digit reaches \(P_{x,0}\) or \(P_{x,1}\).

We prove all these states distinct. Any two \(N_x,N_y\) with \(x\ne y\) are distinguished by \((11)^t\) for a suitable \(t\ge1\). For two pending states with differing residues, \(0(11)^t\) distinguishes them; with the same residue but differing pending bits, \(1(11)^t\) distinguishes them. Finally compare \(N_x\) and \(P_{y,b}\). On suffix \((11)^t\), for \(t\ge1\), their completed-pair residues become respectively \(x+t\) and \(y+b+t-1\). On suffix \(1(11)^t\), their residues become \(x+t\) and \(y+b+t\). If the states were equivalent, equality of outputs for all positive \(t\), which traverse every residue class modulo \(r\), would force both \(x=y+b-1\) and \(x=y+b\pmod r\). These are incompatible for \(r\ge2\). Hence the \(3r\) reached states are all distinguishable, proving \(\operatorname{sc}_{2,\mathrm{LSD}}=3r\). The three asserted exact formulas follow.

## Verification

A standalone, dependency-free verifier is supplied at `verification/checker.py`. Run `python3 verification/checker.py`. It generates each automaton independently from its defined transition table, reaches all states by breadth-first search, refines output-equivalence partitions to stability, and compares the resulting minimal sizes against all three closed formulas for every \(r\in\{2,\ldots,9\}\). It additionally compares the automata's outputs against direct base-four digit counting for the first \(512\) nonnegative integers with four zero-padding choices and all three input conventions. The exact recorded output is in `verification/checker_output.txt`. These finite checks are corroboration; the mathematical lower bounds above apply to every \(r\ge2\) without a computational cutoff.

## Relationship to prior work

Allouche, Rampersad, Rigo, Shallit, and Stipulanti (arXiv:2610.03837, first posted October 2, 2026) introduced the sequence \(b_3\) in the context of a \(2\)-automatic word whose Abelian complexity is not \(2\)-regular. Their Lemma 6 proves binary automaticity by conversion from a four-uniform morphism, but their main theorem and calculations concern Abelian complexity, not minimal automaton state counts. The new assertion concerns precise automaton sizes, including the arbitrary-modulus family, rather than the known automaticity or nonregularity theorem. Zantema and Bosma's work on complexity of automatic sequences develops the distinction between digit-reading conventions and automaton-minimality measures. Moradi, Rampersad, and Shallit develop state complexity for automatic sequences and related operations; their results do not give these three explicit digit-count formulas. The Myhill--Nerode distinguishability principle itself is classical and not claimed as novel.

## Limitations

Only the count of the base-four digit \(3\) modulo \(r\), with zero-versus-nonzero output, is treated. No assertion is made for other base-four target digits, full residue-valued outputs, unrelated automatic words, or general base conversions. For \(r=3\), the result determines the automata sizes of a recently studied example; it does not improve the published nonregular-Abelian-complexity proof. A search cannot rule out an earlier or differently formulated automaton minimization of this particular modular digit-count family. No independent scientific audit has been performed.

## References

1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837v1, submitted 2026-10-02, https://arxiv.org/abs/2610.03837.
2. H. Zantema and W. Bosma, *Complexity of Automatic Sequences*, 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC7206635/.
3. D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017, version inspected April 2026, https://arxiv.org/abs/2512.10017.
4. J. E. Hopcroft, R. Motwani, J. D. Ullman, *Introduction to Automata Theory, Languages, and Computation*, standard Myhill--Nerode minimality principle.
