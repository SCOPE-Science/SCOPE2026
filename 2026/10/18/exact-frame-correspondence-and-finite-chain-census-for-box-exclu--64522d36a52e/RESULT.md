# Exact frame correspondence and finite-chain census for box excluded middle

## Finding
Let \(F=(W,\leq,R)\) be a nonempty birelational intuitionistic modal frame: \(\leq\) is a partial order, and
\[
 x\leq y\ \land\ yRz\quad\Longrightarrow\quad xRz.
\]
Propositional valuations are upward-closed in \(\leq\), intuitionistic connectives have their standard Kripke clauses, and \(x\Vdash\Box\varphi\) means \(R(x)\subseteq\llbracket\varphi\rrbracket\). Define \(\uparrow S=\{z\in W:\exists s\in S\ (s\leq z)\}\).

**Exact correspondence.** The following are equivalent, for any cardinality of \(W\):

1. Every valuation on \(F\) validates the full box excluded-middle schema \(\Box\varphi\vee\neg\Box\varphi\) at every world.
2. Every valuation validates its single atomic instance \(\Box p\vee\neg\Box p\) at every world.
3. For all \(x\leq y\), \(R(x)\subseteq\uparrow R(y)\); equivalently,
\[
 \forall x,y,z\ \bigl(x\leq y\wedge xRz\ \Longrightarrow\ \exists t\ (yRt\wedge t\leq z)\bigr).
\]
4. For all \(x\leq y\), \(\uparrow R(x)=\uparrow R(y)\).

**Exact chain census.** Fix the labelled chain \(W_n=\{0<1<\cdots<n-1\}\), \(n\geq1\), and count all binary relations \(R\subseteq W_n^2\) satisfying the basic birelational condition and validating box excluded middle. The count is
\[
 C_n=1+\sum_{j=0}^{n-1}(n+1)^j=1+\frac{(n+1)^n-1}{n}.
\]
For comparison, imposing the stronger condition \(x\leq y\wedge xRz\Rightarrow yRz\) gives exactly \(2^n\) relations. The difference first occurs at \(n=2\); the five valid relations on that chain include one not satisfying the stronger condition. In particular, \(C_1,C_2,C_3,C_4=2,5,22,157\), and \(C_n\sim (n+1)^n/n\).

## Assumptions and scope
This is **frame validity**, quantified over all upward-persistent propositional valuations and all modal formulas; it is not validity at one fixed valuation. No image-finiteness, seriality, reflexivity of \(R\), or finiteness of \(W\) is assumed for the correspondence. Empty successor sets are allowed. The frame condition on \(R\) is the standard \(\Box\)-persistence condition, not the stronger box-excluded-middle condition. The census fixes the chain labels and does not quotient by isomorphism (a finite chain has only its identity order automorphism).

## Proof
**Persistence.** By induction, every formula's truth set \(U\) is upward-closed. For the box case, if \(x\leq y\) and \(R(y)\subseteq R(x)\), then \(R(x)\subseteq U\) implies \(R(y)\subseteq U\). The intuitionistic propositional cases are standard.

**Correspondence, necessity.** Condition 1 implies condition 2. Suppose condition 3 fails: there exist \(x\leq y\) and \(z\in R(x)\setminus\uparrow R(y)\). Set the upward-persistent atomic valuation \(\llbracket p\rrbracket=\uparrow R(y)\). Then \(y\Vdash\Box p\), while \(x\not\Vdash\Box p\). Since \(x\leq y\) and \(y\Vdash\Box p\), also \(x\not\Vdash\neg\Box p\). Hence the atomic instance fails at \(x\). Thus condition 2 entails condition 3.

**Correspondence, sufficiency.** Assume condition 3 and take any formula \(\varphi\) with upward-closed truth set \(U\). For \(x\leq y\), if \(y\Vdash\Box\varphi\), then \(R(y)\subseteq U\), and therefore \(R(x)\subseteq\uparrow R(y)\subseteq U\); hence \(x\Vdash\Box\varphi\). Basic frame persistence gives the reverse implication. Thus box formulas have constant truth along comparable worlds. If \(x\not\Vdash\Box\varphi\), no \(y\geq x\) forces \(\Box\varphi\), so \(x\Vdash\neg\Box\varphi\). Therefore condition 1 follows. Finally, basic persistence implies \(R(y)\subseteq R(x)\) for \(x\leq y\), so \(\uparrow R(y)\subseteq\uparrow R(x)\); condition 3 supplies the reverse inclusion, proving equivalence with condition 4.

**Chain normal form.** On \(W_n\), basic persistence means nested rows \(R(0)\supseteq R(1)\supseteq\cdots\supseteq R(n-1)\). Condition 4 says the rows have identical upward closures. On a finite chain an upward closure is either empty or the final segment beginning at its least element. Hence either every row is empty, or there is a unique common row minimum \(m\in\{0,\ldots,n-1\}\). In the latter case, every row contains \(m\) and contains no world below \(m\). For each \(j>m\), membership of \(j\) down the nested row sequence is an arbitrary initial segment, with exactly \(n+1\) choices (length \(0\) through \(n\)). All these choices are independent. There are \((n+1)^{n-1-m}\) relations for the fixed minimum \(m\). Summing over \(m\) and adding the all-empty relation yields the displayed formula.

**Strong-condition comparison and sharp witness.** Under the basic persistence condition, adding \(x\leq y\wedge xRz\Rightarrow yRz\) forces every row on a chain to equal every other row. Hence there are exactly \(2^n\) such relations. For the two-point chain \(0<1\), take \(R(0)=\{0,1\}\) and \(R(1)=\{0\}\). It satisfies the basic condition and has common minimum \(0\), hence validates every instance of box excluded middle; it violates the strong condition because \(0R1\) but not \(1R1\). For \(n=1\), every reflexive comparison is equality, so the strong condition is automatic. Therefore two worlds is the sharp witness size.

## Verification
Run `python3 check_bem.py` from the directory containing this report. The program directly compares condition 3 with the original semantic axiom over every labelled poset and every persistence-compatible relation for \(1\leq n\leq3\), enumerating all upward-closed atomic valuations. It also checks the chain counts by direct enumeration for \(1\leq n\leq4\) and the displayed two-point witness. These are finite consistency checks; the proof above establishes the statements for all parameters.

## Relationship to prior work
Van der Giessen, Joosten, Mayaux and Navarro Arroyo (2025), Definition 3.1.2 and Lemma 3.1.6, use the basic birelational condition and prove the stronger \(\mathsf{BEM}\) frame condition sufficient for \(\Box\varphi\vee\neg\Box\varphi\). Example 3.1.7 explicitly demonstrates that their sufficient condition is not necessary, using four worlds. Their completeness result for \(\mathsf{iK}+\mathsf{bem}\) over the stronger class does not characterize *all frames* validating the schema. The present result characterizes that larger class exactly, gives its chain census, and supplies a minimal two-world witness. The correspondence uses the family of upward-closed sets and is not an unconditional statement about unrestricted classical valuations.

Literature comparisons included logically nearby finite-chain KI, FIK, and birelational-census results, and a result about commuting box/diamond condensations. Those impose distinct interaction conditions or address different operations; none of their reported statements implies the all-valuation characterization or the count above. The possibility of an equivalent description under other modal/Heyting-algebra terminology remains. Mayaux's September 2024 thesis on the predecessor mixed-model framework is also relevant; the accessible repository summary covers completeness but does not settle whether its uninspected full text contains the same refined correspondence. The first verified public release of the specific 2025 article and its displayed nonnecessity example is 2025-10-20.

## Limitations
The exact enumeration is for a **fixed linearly ordered carrier**, not arbitrary finite posets. It is not a new completeness or decidability theorem for \(\mathsf{iK}+\mathsf{bem}\). The similarity searches do not establish absolute novelty; independent literature review has not been conducted. Finite enumeration verifies only the stated small cases, not the infinite correspondence proof.

## References
1. Iris van der Giessen, Joost J. Joosten, Paul Mayaux, Vicent Navarro Arroyo, *On the Contingency of Logic in Possible World Semantics*, first public arXiv version 2025-10-20, arXiv:2510.17302; *Logica Universalis*, DOI:10.1007/s11787-025-00400-7. Sections 3.1 and 3.3.
2. Paul Mayaux, *Possible worlds and the contingency of logic*, Master's thesis, Universitat de Barcelona, repository record dated 2024-09, https://hdl.handle.net/2445/215519. Earlier treatment of mixed models and completeness; full thesis PDF was not accessible for detailed comparison.
3. Alex K. Simpson, *The Proof Theory and Semantics of Intuitionistic Modal Logic*, University of Edinburgh dissertation, 1994; standard persistent birelational semantics.
