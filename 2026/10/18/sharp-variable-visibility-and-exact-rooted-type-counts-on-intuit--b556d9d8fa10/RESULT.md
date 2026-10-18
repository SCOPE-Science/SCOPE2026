# Sharp variable visibility and exact rooted type counts on intuitionistic forks

## Finding

For each integer \(k\geq1\), let \(F_k\) be the intuitionistic Kripke frame consisting of a least world \(r\) and exactly \(k\) incomparable maximal worlds above it. Fix \(n\geq1\) propositional letters. A persistent valuation has a root color \(a\subseteq[n]\) and a nonempty set \(S\subseteq\{t\subseteq[n]:a\subseteq t\}\) of distinct maximal-world colors, with \(1\leq |S|\leq k\).

**Rooted-type classification and exact census.** Two such pointed valuations, possibly on different forks, satisfy exactly the same intuitionistic formulas in these \(n\) letters at their respective roots if and only if their pairs \((a,S)\) coincide. Consequently, the number of distinct rooted formula theories realized on \(F_k\) equals
\[
T(n,k)=\sum_{j=0}^{n}\binom{n}{j}\sum_{s=1}^{\min(k,2^{n-j})}\binom{2^{n-j}}{s}.
\]
This stabilizes at \(k=2^n\), when
\[
T(n,k)=\sum_{j=0}^{n}\binom{n}{j}\bigl(2^{2^{n-j}}-1\bigr)\qquad(k\geq2^n).
\]
For instance, \(T(2,k)\) for \(k=1,2,3,4\) is \(9,17,21,22\), and \(T(3,k)\) for \(k=1,\ldots,8\) is \(27,76,144,217,273,301,309,310\).

**Sharp variable visibility.** Write \(\operatorname{Log}_n(F_k)\) for all formulas in at most \(n\) letters valid at every world under every persistent valuation on \(F_k\). Then
\[
\operatorname{Log}_n(F_1)\supsetneq\operatorname{Log}_n(F_2)
\supsetneq\cdots\supsetneq\operatorname{Log}_n(F_{2^n})
=\operatorname{Log}_n(F_{2^n+1})=\cdots.
\]
In particular, for any integers \(1\leq k<\ell\), the **smallest positive number of propositional letters** capable of distinguishing the frame logics of \(F_k\) and \(F_\ell\) is exactly
\[
\left\lceil\log_2(k+1)\right\rceil.
\]
The distinction has explicit formulas, not merely a nonconstructive counting argument.

## Assumptions and scope

Formulas belong to ordinary intuitionistic propositional logic with \(\land,\lor,\to,\bot\), and \(\neg\varphi\) abbreviates \(\varphi\to\bot\). At a world \(w\), \(w\Vdash\varphi\to\psi\) means that each \(u\geq w\) forcing \(\varphi\) also forces \(\psi\). Every atomic truth set is upward closed. There are exactly \(n\geq1\) available letters and \(k\geq1\) leaves; no distinctness restriction is imposed on the colors of different leaves. The count is of **rooted formula theories**, not of valuations, frames, all possible world theories jointly, or elements of a free Heyting algebra.

We identify a color \(t\subseteq[n]\) with the Boolean assignment of the letters that it contains. Let \(C_n=\mathcal P([n])\). Define the intuitionistic minterm
\[
\beta_t=\Bigl(\bigwedge_{i\in t}p_i\Bigr)\land
\Bigl(\bigwedge_{i\notin t}\neg p_i\Bigr),
\]
with empty conjunction interpreted as \(\top=\bot\to\bot\). At a maximal world, \(\beta_t\) holds exactly when that world's color is \(t\).

## Proof

**1. Invariance of rooted truth.** We prove by structural induction on \(\varphi\) that its truth at the root depends only on \((a,S)\). The atomic and lattice-constant cases are immediate; conjunction and disjunction follow from induction. A maximal world is classical for all propositional formulas, so whether it satisfies \(\varphi\) depends only on its Boolean color. At the root,
\[
r\Vdash\varphi\to\psi
\quad\Longleftrightarrow\quad
\bigl(r\not\Vdash\varphi\ \text{or}\ r\Vdash\psi\bigr)
\ \text{and}\ 
\bigl(\forall t\in S:\ t\models_{\mathrm{cl}}\varphi\Rightarrow t\models_{\mathrm{cl}}\psi\bigr).
\]
The first factor is decided by the induction hypothesis, and the second only by \(S\). Thus equal pairs give identical rooted truth for every formula.

**2. Separation of different pairs.** If \(a\neq a'\), some atom \(p_i\) distinguishes the roots. If \(S\neq S'\), choose \(t\) in their symmetric difference. At any maximal world, \(\beta_t\) is true exactly at color \(t\). At the root, \(\neg\beta_t\) holds exactly when no world above the root forces \(\beta_t\). If any world above the root forces \(\beta_t\), then a leaf does: for the root itself this follows from persistence, and for a leaf it is immediate. Hence
\[
r\Vdash\neg\beta_t\quad\Longleftrightarrow\quad t\notin S.
\]
It separates the two roots. These arguments prove both directions of the claimed type classification, without appealing to a bounded formula search.

**3. Counting the types.** When \(|a|=j\), there are exactly \(2^{n-j}\) possible colors for a leaf. For any \(1\leq s\leq\min(k,2^{n-j})\), choosing \(s\) of them yields one possible distinct-color set \(S\). Every such set is realized by assigning its colors to \(s\) leaves and repeating one color on the remaining leaves. There are \(\binom nj\) choices of \(a\) of size \(j\); distinct pairs have distinct theories by step 2. Summing gives \(T(n,k)\), and summing all nonempty subsets gives the stable formula at \(k\geq2^n\).

**4. Validity monotonicity and eventual equality.** Given a valuation on \(F_k\) and any \(\ell\geq k\), duplicate leaf colors to obtain a valuation on \(F_\ell\) with the same root pair \((a,S)\). The roots then agree on all formulas by step 1; at leaves, the duplicated worlds also agree with the originals. Therefore \(\operatorname{Log}_n(F_\ell)\subseteq\operatorname{Log}_n(F_k)\). Conversely, whenever \(k,\ell\geq2^n\), any possible root pair on either fork can be realized on the other because \(|S|\leq2^n\leq\min(k,\ell)\). Thus any counterexample at a root transfers, and a leaf counterexample is classical and also transfers to a leaf of the other fork. Hence their \(n\)-variable logics coincide.

**5. Explicit strictness witness.** For each \(1\leq k<2^n\), define
\[
\Theta_{n,k}=\bigvee_{\substack{A\subseteq C_n\\|A|=k}}
\neg\Bigl(\bigvee_{t\in C_n\setminus A}\beta_t\Bigr).
\]
The disjunctions are finite and nonempty in the displayed range. For any valuation on \(F_k\), take a \(k\)-element set \(A\) containing every leaf color. No leaf forces a \(\beta_t\) with \(t\notin A\), and by persistence neither can the root; so the corresponding disjunct is true at the root. At a leaf, any \(k\)-set containing that leaf's color supplies a true disjunct. Hence \(\Theta_{n,k}\) is valid on \(F_k\). On \(F_{k+1}\), give \(k+1\) leaves pairwise distinct colors, with the all-false root color. Every \(k\)-set \(A\) omits the color of some leaf, which forces its associated minterm. Therefore each negated disjunction is false at the root, and \(\Theta_{n,k}\) is not valid on \(F_{k+1}\). By duplicating the counterexample leaf colors, it is also invalid on every \(F_\ell\) with \(\ell>k\).

Finally fix \(k<\ell\). If \(2^n\leq k\), the two \(n\)-variable logics are equal by step 4. If \(2^n>k\), step 5 separates them with \(\Theta_{n,k}\). The least integer \(n\geq1\) in the latter case is \(\lceil\log_2(k+1)\rceil\), proving the sharp visibility bound.

## Verification

The accompanying standalone Python program `verify_fork_types.py` uses actual Kripke implication on the \(k+1\)-world fork, enumerates all upward-closed atomic valuations for the indicated finite parameter ranges, independently computes root colors and distinct leaf-color sets, and evaluates the distinguishing formulas and finite disjunction witnesses. Running `python verify_fork_types.py` produced the following completed checks:

- 43,291 valuation/type checks for all \(1\leq n\leq3\) and \(1\leq k\leq5\), matching the exact count in each case;
- 1,013 direct separating-formula evaluations for all \(1\leq n\leq3\) and \(1\leq k\leq3\), matching the type classification;
- 999 full-formula validity checks and an explicit falsifying valuation on the next larger fork for every tested \(n,k\) with \(n\leq3\) and \(k\leq\min(3,2^n-1)\).

All checks passed. The proofs above, rather than these finite tests, establish the quantified claims for arbitrary positive \(n,k,\ell\).

## Relationship to prior work

Almeida (2026) studies uniform local tabularity of intermediate logics using colored finite Kripke models, finite-model reductions, implication-depth bisimulations, and two-fork examples (notably Definitions 2.3–2.5, Propositions 2.6 and 2.13, and Theorem 3.2). The general semantic machinery is background for this finding. The present result asks a different, **exact** question on all finite forks: it gives the entire rooted \(n\)-type census, the precise point of stabilization in branching, and an explicit minimal-variable separating formula for each lower branching threshold. The inspected sections of Almeida's paper and dissertation do not state this combined count-and-cutoff theorem.

Hyttinen–Martins–Moraschini–Quadrellaro (2024) use finite colors and an exponential bound on distinguishable types in a layered **infinite** Esakia-space construction (Sections 3–4). Their bound does not enumerate rooted theories on the \(F_k\) family or determine the strict finite-variable fork-validity hierarchy. The value \(2^n\) here follows from the finite antichain of independent maximal worlds, and the sharpness is witnessed by the formulas \(\Theta_{n,k}\); it should not be conflated with general bounds on height, width, arbitrary posets, or all finite-variable free algebras.

## Limitations

The proof concerns two-level rooted forks and ordinary intuitionistic propositional logic only. A rooted semantic-type count is not the number of formulas modulo frame validity, nor the cardinality of the \(n\)-generated free algebra of that intermediate logic. No analogous cutoff for posets with intermediate levels or modal extensions is asserted. Although the cited general bisimulation and coloring theory explains why finite color profiles matter, an equivalent unindexed fork-specialization may exist; no independence from earlier work is claimed. No external independent audit has been performed.

## References

1. Rodrigo Nicolau Almeida, *Uniform Local Tabularity in Intuitionistic Logic*, arXiv:2601.11208 (version 1 submitted 2026-01-16; version 2 2026-06-30), https://arxiv.org/abs/2601.11208 .
2. Rodrigo Nicolau Almeida, *Representations and Model Theory of Free Heyting Algebras*, doctoral thesis, ILLC Dissertation Series DS-2026-14, relevant Sections 2.3, 3.2, and 6, https://eprints.illc.uva.nl/id/document/13880 .
3. Tapani Hyttinen, Miguel Martins, Tommaso Moraschini, and Davide E. Quadrellaro, *Strictly n-Finite Varieties of Heyting Algebras*, *Journal of Symbolic Logic* (online 2024), doi:10.1017/jsl.2024.48, https://doi.org/10.1017/jsl.2024.48 .
