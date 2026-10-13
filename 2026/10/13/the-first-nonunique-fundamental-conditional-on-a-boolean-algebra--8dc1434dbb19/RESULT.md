# The first nonunique fundamental conditional on a Boolean algebra

## Finding

Write \(B_n=\mathcal P([n])\), with the inclusion order, bottom \(0=\varnothing\), and top \(1=[n]\). A **preconditional** is a binary operation \(\Rightarrow\) satisfying (P1)--(P5) below; an **F-preconditional** additionally satisfies conditional identity, semicomplementation, and double-negation inflation. Its **derived negation** is \(\nu(a)=a\Rightarrow0\).

**Theorem (sharp negation-fibre threshold).** Among finite Boolean algebras, \(B_3\), with eight elements, is the smallest whose F-preconditionals need not be determined by their derived negation. On \(B_3\), fix the weak pseudocomplementation
\[
\nu_*(a)=\begin{cases}1,&a=0,\\0,&a\ne0.\end{cases}
\]
Exactly \(3^6=729\) distinct labeled F-preconditionals induce \(\nu_*\). They form exactly \(138\) isomorphism classes under automorphisms of the Boolean carrier. Every one of these \(729\) operations also satisfies the stronger flattening equation
\[
a\Rightarrow((a\wedge b)\Rightarrow c)=(a\wedge b)\Rightarrow c.
\]
On \(B_2\) (four elements), exactly two F-preconditionals exist and they have different derived negations. On \(B_1\) (two elements), exactly one exists.

## Assumptions and scope

All sets and operations are finite. The lattice meet is intersection, join is union, and \(a\le b\) means \(a\subseteq b\). In the following axioms, \(a,b,c\) range over the entire lattice:
\[
\begin{aligned}
\mathrm{(P1)}&\quad 1\Rightarrow a\le a,\\
\mathrm{(P2)}&\quad a\wedge b\le a\Rightarrow b,\\
\mathrm{(P3)}&\quad a\Rightarrow b\le a\Rightarrow(a\wedge b),\\
\mathrm{(P4)}&\quad a\Rightarrow(b\wedge c)\le a\Rightarrow b,\\
\mathrm{(P5)}&\quad a\Rightarrow((a\wedge b)\Rightarrow c)\le(a\wedge b)\Rightarrow c.
\end{aligned}
\]
The three extra F-axioms are \(a\Rightarrow a=1\), \(a\wedge\nu(a)=0\), and \(a\le\nu(\nu(a))\). These coincide with the algebraic usage in Chen (2026), Definition 3.3. "Labeled" means the atoms of \([3]\) are fixed. Isomorphisms may permute atoms but must preserve the conditional operation.

## Proof

**Reduction valid in every preconditional.** By (P1) and (P2), \(1\Rightarrow b=b\). By (P3) and (P4),
\[
a\Rightarrow b=a\Rightarrow(a\wedge b).
\]
Thus, for each antecedent \(a\), its conditional row is determined by its values on subsets of \(a\), monotone by (P4), with \(u\subseteq a\Rightarrow u\) by (P2). Conditional identity gives \(a\Rightarrow a=1\). Also \(0\Rightarrow b=1\) for every \(b\).

**All operations over \(\nu_*\) on \(B_3\).** Fix \(X=[3]\) and require \(a\Rightarrow0=0\) for nonempty \(a\). The empty-antecedent row is constantly \(X\); the full-antecedent row is \(X\Rightarrow b=b\); and each singleton antecedent \(a\) has \(a\Rightarrow b=X\) when \(a\subseteq b\) and \(a\Rightarrow b=0\) otherwise. These rows are forced by the reduction.

For a two-element antecedent \(a=\{i,j\}\), the values at \(0\) and \(a\) are forced to be \(0\) and \(X\). Write \(k\) for the unique element of \(X\setminus a\). By (P2), \(u=a\Rightarrow\{i\}\) contains \(i\). Set \(b=a\) in (P5) to get \(a\Rightarrow(a\Rightarrow\{i\})\subseteq a\Rightarrow\{i\}\). If \(u\) contains \(j\), then it contains all of \(a\), whence by consequent monotonicity and identity \(a\Rightarrow u=X\); therefore \(u=X\). If \(u\) does not contain \(j\), it is either \(\{i\}\) or \(\{i,k\}\). Consequently each flag \((a,i)\), where \(|a|=2\) and \(i\in a\), has exactly the three possible values
\[
a\Rightarrow\{i\}\in\bigl\{\{i\},\;\{i,k\},\;X\bigr\}.
\]
There are six such flags. The choices are independent: define the remaining values in every row by the previous forced values and \(a\Rightarrow b=a\Rightarrow(a\cap b)\). Axioms (P1)--(P3) are then immediate, and (P4) holds because each two-element row has only the comparabilities \(0\subseteq\{i\}\subseteq a\) and \(0\subseteq\{j\}\subseteq a\).

It remains to verify (P5), not merely assume independence. Put \(d=a\cap b\). If \(a=X\), its row is the identity, giving equality in (P5). If \(a=0\), both sides are \(X\). For singleton \(a\), each value in its row is \(0\) or \(X\), and the equality is immediate for \(d=0\) or \(a\). For two-element \(a\): if \(d=0\), then \(d\Rightarrow c=X\); if \(d\) is a singleton, then \(d\Rightarrow c\in\{0,X\}\), both fixed by the \(a\)-row; and if \(d=a\), each possible value \(a\Rightarrow c\) is fixed by the \(a\)-row, using antecedent absorption when it contains the outside atom \(k\). In every case \(a\Rightarrow(d\Rightarrow c)=d\Rightarrow c\). Thus **all** \(3^6\) choices satisfy even flattening equality. Their negation is \(\nu_*\), whose semicomplementation and double-negation inflation hold directly, and conditional identity was built in. Every possible F-preconditional over \(\nu_*\) has been accounted for, so the labeled count is \(729\).

**Isomorphism classes.** Automorphisms of \(B_3\) are exactly permutations of the three atoms, forming \(S_3\). They permute the six flags \((a,i)\) while leaving the choice labels \(0,1,2\) unchanged (the middle value always adds the unique atom outside \(a\)). The identity has six flag-orbits, each transposition has three, and each three-cycle has two. Burnside's lemma gives
\[
\frac{3^6+3\cdot3^3+2\cdot3^2}{6}=138.
\]

**Sharpness at smaller carriers.** The one-atom Boolean algebra has only the top row and empty row, so its F-preconditional is unique. For \(B_2\), write its atoms as \(i,j\). As above, the empty row is constantly \(1\), the top row is the identity, and each atomic row is uniquely fixed by \(\nu(i)\) and its value \(i\Rightarrow i=1\). Semicomplementation forces \(\nu(i)\subseteq\{j\}\) and \(\nu(j)\subseteq\{i\}\). Double-negation inflation rules out exactly one of these two atomic negations being nonempty. Hence the only possibilities are both empty, giving the drastic conditional, or \(\nu(i)=\{j\},\nu(j)=\{i\}\), giving classical material implication. Both are F-preconditionals; the former is the universal bounded-lattice construction already described in Holliday (2023), and the latter is the Boolean Heyting implication. Their derived negations differ. The one-element Boolean algebra has a unique binary operation, completing the minimality claim.

## Verification

The standalone file `verify.py` uses only Python's standard library; run `python3 verify.py`. It enumerates all \(3^6=729\) flag assignments and checks (P1)--(P5) and all three F-axioms over every finite argument triple on \(B_3\). It independently checks the \(S_3\) fixed-point counts \(729,27,27,27,9,9\), verifies the quotient \(138\), and exhausts the reduced two-atom search space to obtain the two F-preconditionals with distinct negations. It prints `VERIFY_OK`. The symbolic reductions above, not an unbounded computational search, establish completeness of the classification.

## Relationship to prior work

Chen (2026) defines K-, T-, and F-algebras, proves semantic completeness and a finite model property, and supplies the exact axioms used here, but does not enumerate Boolean conditional fibres. Holliday (2023), Section 3, explicitly considers \(\nu_*\) on the four-element Boolean lattice, and Section 6 constructs the drastic preconditional on any bounded lattice; thus neither the existence of \(\nu_*\) nor the existence of one such conditional is claimed as new. Holliday (2025), Proposition 4, proves uniqueness of the Sasaki hook when the derived negation is an **involutive** semicomplementation. The negation \(\nu_*\) is noninvolutive on \(B_3\), so that theorem does not imply the 729-element fibre or the sharp threshold. The present theorem instead classifies a fixed-negation fibre on the first nonchain Boolean carrier at which that fibre is nontrivial.

## Limitations

The classification and numerical counts concern only the fixed negation \(\nu_*\) on an eight-element Boolean algebra; no formula is asserted for all negations on \(B_3\) or for larger carriers. No new completeness, decidability, or asymptotic complexity theorem is claimed. Exhaustive code testing is a reproducibility check of the finite normal form and is not an independent audit. Unfound terminology or an unindexed finite-algebra classification could still duplicate the counting claim.

## References

- Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221v1, publicly posted 2026-07-22. https://arxiv.org/abs/2607.20221
- Wesley H. Holliday, *A Fundamental Non-Classical Logic*, *Logics* 1 (2023), 36--79, Section 3 and Section 6; DOI:10.3390/logics1010004. https://www.mdpi.com/2813-0405/1/1/4
- Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, revised 2025, especially Section 2 and Proposition 4. https://arxiv.org/abs/2402.02296
