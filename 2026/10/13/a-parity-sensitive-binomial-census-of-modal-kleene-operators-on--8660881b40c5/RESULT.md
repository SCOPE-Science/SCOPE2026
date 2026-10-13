# A parity-sensitive binomial census of modal Kleene operators on finite chains

## Finding
For each positive integer \(m\), let \(E_m\) denote the number of unary operations \(\Box\) on the \(m\)-element Kleene chain satisfying binary meet preservation and the positivity and consistency inequalities defined below. Let \(N_m\) count those operations additionally satisfying \(\Box 1=1\). Then \(E_1=N_1=1\), and, for every integer \(r\ge1\),

\[
\begin{aligned}
E_{2r}&=\binom{2r-1}{r}^{2}+\binom{2r}{r+1}, &
N_{2r}&=\binom{2r-1}{r}\binom{2r-2}{r-1}+\binom{2r-1}{r},\\
E_{2r+1}&=\binom{2r}{r}^{2}+\binom{2r}{r+1}, &
N_{2r+1}&=\binom{2r}{r}\binom{2r-1}{r-1}+\binom{2r-1}{r}.
\end{aligned}
\]

More strongly, every admissible operation has a unique low/high normal form at the negation midpoint, described in the proof. For chain sizes \(m=1,\ldots,10\), the values of \(E_m\) are \(1,2,5,13,40,115,415,1281,4956,16086\), and those of \(N_m\) are \(1,2,3,9,21,70,210,735,2485,8946\). Because a finite chain has no nonidentity order automorphism, these numbers are also isomorphism-class counts of such expansions of the fixed Kleene chain.

## Assumptions and scope
Fix \(m\ge1\). Write \(K_m=\{0,1,\ldots,m-1\}\) in its natural order, with lattice operations minimum and maximum, bottom \(0\), top \(1_{K_m}=m-1\), and strong involutive negation \(\sim i=m-1-i\). It is a Kleene algebra because \(x\wedge\sim x\le y\vee\sim y\) for all elements. We impose **only** the following three axioms on a unary operation \(f=\Box:K_m\to K_m\), quantified over all \(x,y,z\in K_m\):

\[
\begin{array}{ll}
(\mathrm M)& f(x\wedge y)=f(x)\wedge f(y),\\
(\mathrm {Pos})&\sim f(z\vee\sim z)\le f(z\vee\sim z),\\
(\mathrm {Con})&f\bigl(x\vee(z\wedge\sim z)\bigr)\le f(x)\vee\sim f\bigl(x\vee(z\wedge\sim z)\bigr).
\end{array}
\]

Here **normality** means the optional additional equation \(f(1_{K_m})=1_{K_m}\); it is *not* included in (M), which preserves binary rather than empty meets. We do not assume extensivity, idempotence, commutation with negation, implication, or preservation of bottom. These hypotheses must not be replaced by the stronger conditions defining a nucleus.

## Proof
Put \(r=\lfloor m/2\rfloor\) and \(s=\lfloor(m-1)/2\rfloor\). On a chain, (M) is equivalent to monotonicity: \(x\le y\) implies \(f(x)=\min(f(x),f(y))\), and conversely any monotone function preserves binary minima. The elements \(z\vee\sim z\) run through all of \(\{r,\ldots,m-1\}\); the elements \(z\wedge\sim z\) run through all of \(\{0,\ldots,s\}\). Thus (Pos) is equivalent to \(f(r)\ge r\), since \(f\) is monotone and \(\sim a\le a\) exactly when \(a\ge r\).

For (Con), set \(t=z\wedge\sim z\). The condition is automatic when \(x\ge t\) and reduces to
\[
f(t)\le \max\bigl(f(x),m-1-f(t)\bigr)
\]
when \(x<t\). Monotonicity gives \(f(x)\le f(t)\), so the displayed inequality is equivalent to the implication
\[
0\le x<t\le s,\qquad f(x)<f(t)\quad\Longrightarrow\quad f(t)\le s.\tag{*}
\]
Indeed \(f(t)\le m-1-f(t)\) is equivalent to \(f(t)\le s\). If \(f(0),\ldots,f(s)\) are not all \(\le s\), let \(t\le s\) be the least index where \(f(t)>s\). If \(t>0\), (\(*\)) applied at \(x=t-1\) fails. Hence \(f(0)>s\), and (\(*\)) forces \(f(0)=\cdots=f(s)=c>s\). Conversely, either of these patterns satisfies (\(*\)). Therefore (Con) is exactly the disjoint dichotomy:

**Low branch:** all \(f(0),\ldots,f(s)\) lie in \(\{0,\ldots,s\}\); **high branch:** these values are the same \(c\in\{s+1,\ldots,m-1\}\). This is a normal form, not only a counting device.

When \(m=2r\), the low branch has an arbitrary nondecreasing length-\(r\) lower block with values in \(\{0,\ldots,r-1\}\), followed by an arbitrary nondecreasing length-\(r\) upper block with values in \(\{r,\ldots,2r-1\}\) by (Pos). Each block has \(\binom{2r-1}{r}\) choices, yielding the squared term in \(E_{2r}\). In the high branch the first \(r\) values equal \(c\ge r\) and the final \(r\) values form a nondecreasing sequence from \(\{c,\ldots,2r-1\}\). For a fixed \(c\), stars-and-bars gives \(\binom{3r-c-1}{r}\) such tails. Summing over \(c=r,\ldots,2r-1\) yields \(\binom{2r}{r+1}\) by the hockey-stick identity. Requiring the final element to map to top replaces the last lower-branch tail count by \(\binom{2r-2}{r-1}\) and the high-branch sum by \(\binom{2r-1}{r}\), producing \(N_{2r}\).

When \(m=2r+1\), the low branch has \(f(r)\le r\) by definition but \(f(r)\ge r\) by (Pos), hence \(f(r)=r\). The \(r\) preceding values may be any nondecreasing values in \(\{0,\ldots,r\}\), and the \(r\) succeeding values may be any nondecreasing values in \(\{r,\ldots,2r\}\). Each block has \(\binom{2r}{r}\) choices. In the high branch the first \(r+1\) values equal \(c\ge r+1\); the final \(r\) are arbitrary nondecreasing values in \(\{c,\ldots,2r\}\). The same hockey-stick summation gives \(\binom{2r}{r+1}\). Freezing the last value to top changes the low upper-block count to \(\binom{2r-1}{r-1}\) and the high sum to \(\binom{2r-1}{r}\), yielding \(N_{2r+1}\). The one-element case has exactly one unary operation and that operation is normal. This completes all cases and both directions of the classification.

## Verification
The accompanying standalone `verify_kleene_chain.py` enumerates **every** nondecreasing unary map on each chain size \(1\le m\le10\), tests the literal quantified (Pos) and (Con) conditions using the chain operations, independently calculates the four formula cases, and compares the counts for both unrestricted and normal maps. Execute `python3 verify_kleene_chain.py`; the successful terminal marker is `VERIFY_OK`. This checks the first ten cases, not the unbounded result; the latter follows from the dichotomy and binomial proof above. The largest exhaustive case checks \(\binom{19}{10}=92378\) monotone functions.

## Relationship to prior work
Celani, Menchón, and Miguelez (2026) introduced modal Kleene algebras and their twist/triple and topological representations. The accessible primary abstract concerns categorical representation and duality; accessible detailed secondary expositions give the exact three displayed axioms. Those accessible portions do not report this parity-dependent counting formula, the midpoint normal form, or the normal/non-normal split. This comparison is **not** a claim about the inaccessible complete preprint. Celani and Rivieccio (2023) study modal enrichments of Heyting-derived structures, especially nuclei, and do not on their described premises directly imply the counts for non-normal Kleene-chain operations. Ordinary counts of monotone maps do not impose (Pos) and (Con).

## Limitations
The finite-chain enumeration does not classify modal expansions of arbitrary finite Kleene algebras, or operators satisfying extra modal equations. Isomorphism-class equality uses rigidity of the fixed chain and does not extend automatically to other Kleene algebras. The original 2026 preprint PDF was not available through the attempted open reading routes; its full text might contain a relevant special case or stronger theorem, so publication-level originality requires human full-text comparison. No independent audit has been performed.

## References
1. S. Celani, P. Menchón, V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937 (first publicly posted 2026-08-11), https://arxiv.org/abs/2608.10937 .
2. *A Modal Expansion of Kleene Algebras via Twist Structures*, Moonlight literature review, https://www.themoonlight.io/en/review/a-modal-expansion-of-kleene-algebras-via-twist-structures (secondary description of the formal axioms; not the primary full text).
3. S. A. Celani and U. Rivieccio, *Intuitionistic Modal Algebras*, Studia Logica, DOI:10.1007/s11225-023-10065-2 (published online 2023-09-15), https://doi.org/10.1007/s11225-023-10065-2 .
