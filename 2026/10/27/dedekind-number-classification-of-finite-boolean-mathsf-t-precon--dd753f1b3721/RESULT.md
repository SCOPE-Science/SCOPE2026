# Dedekind-number classification of finite Boolean \(\mathsf T\)-preconditional negation reducts

## Finding

Let \(V\) be a nonempty finite set of \(n\) labelled atoms, and let \(B=\mathcal P(V)\) be its Boolean lattice. A unary map \(N:B\to B\) occurs as \(N(A)=A\to\varnothing\) for some \(\mathsf T\)-preconditional on \(B\) **if and only if** it is antitone, \(N(\varnothing)=V\), and \(A\cap N(A)=\varnothing\) for every \(A\subseteq V\). Every such map has an explicit binary lift

\[
 A\Rightarrow_N B=N(A\setminus B)\cup(A\cap B).
\]

Let \(M(r)\) be the Dedekind number, i.e. the number of monotone Boolean functions of \(r\) Boolean variables, including both constants. The number of distinct unary negation reducts of \(\mathsf T\)-preconditionals on the labelled \(n\)-atom Boolean algebra is exactly

\[
 \boxed{(M(n-1)-1)^n}\qquad(n\ge1).
\]

The first values, for \(n=1,2,3,4\), are \(1,4,125,130321\). The corresponding stronger \(\mathsf F\)-negation reducts are the known symmetric loop-free graph polarities, numbering \(2^{\binom n2}\), or \(1,2,8,64\) for these atom counts. Thus \(\mathsf T\) and \(\mathsf F\) first separate on a four-element Boolean algebra. The theorem classifies **negations realizable by binary operations**, not all binary operations themselves.

## Assumptions and scope

For any bounded lattice, a preconditional \(\to\) satisfies, for all lattice elements \(a,b,c\), the five axioms of Holliday:

\[
\begin{aligned}
&\mathrm{(P1)}&&1\to a\le a;\\
&\mathrm{(P2)}&&a\wedge b\le a\to b;\\
&\mathrm{(P3)}&&a\to b\le a\to(a\wedge b);\\
&\mathrm{(P4)}&&a\to(b\wedge c)\le a\to b;\\
&\mathrm{(P5)}&&a\to((a\wedge b)\to c)\le(a\wedge b)\to c.
\end{aligned}
\]

In Chen's terminology a \(\mathsf T\)-preconditional also satisfies conditional identity \(a\to a=1\) and semicomplementation \(a\wedge(a\to0)=0\). An \(\mathsf F\)-preconditional further satisfies \(a\le(a\to0)\to0\). Here \(0=\varnothing\), \(1=V\), meet is intersection, and \(n\) counts **Boolean atoms**, not lattice elements. We count unary functions exactly, without quotienting by permutations of atoms.

## Proof

**Necessity.** For any preconditional the derived map \(N(a)=a\to0\) is antitone (Holliday, Proposition 1; also Chen, Lemma 3.2). Conditional identity at the bottom gives \(N(\varnothing)=\varnothing\to\varnothing=V\). Semicomplementation is precisely \(A\cap N(A)=\varnothing\). These three properties are therefore necessary.

**Sufficiency and all five preconditional axioms.** Suppose \(N\) satisfies the three stated properties and define \(\Rightarrow_N\) by the displayed formula. Write \(X\subseteq Y\) for Boolean order. Semicomplementation gives \(N(X)\subseteq V\setminus X\) and antitonicity gives \(X\subseteq Y\implies N(Y)\subseteq N(X)\).

For (P1), \(V\Rightarrow_N B=N(V\setminus B)\cup B=B\), because \(N(V\setminus B)\subseteq B\). For (P2), \(A\cap B\subseteq A\Rightarrow_N B\). For (P3), \(A\setminus(A\cap B)=A\setminus B\), so in fact \(A\Rightarrow_N B=A\Rightarrow_N(A\cap B)\). For (P4), replacing \(B\) by \(B\cap C\) enlarges \(A\setminus B\), hence antitonicity shrinks its negation, while the intersecting summand also shrinks.

For (P5) put \(D=A\cap B\) and \(H=D\Rightarrow_N C=N(D\setminus C)\cup(D\cap C)\). Semicomplementation ensures \((D\setminus C)\cap H=\varnothing\), hence \(D\setminus C\subseteq A\setminus H\). Thus

\[
 N(A\setminus H)\subseteq N(D\setminus C)\subseteq H.
\]

Also \(A\cap H\subseteq H\). Therefore \(A\Rightarrow_N H\subseteq H\), proving (P5) with no unstated symmetry or involution assumption. Conditional identity follows from
\(A\Rightarrow_N A=N(\varnothing)\cup A=V\). Finally, \(A\Rightarrow_N\varnothing=N(A)\), so semicomplementation of the derived negation is exactly the given hypothesis. This verifies the full \(\mathsf T\) algebra requirements, not just their unary consequences.

**Count.** For each atom \(v\in V\), put \(f_v(S)=1\) if and only if \(v\in N(S)\), for \(S\subseteq V\setminus\{v\}\). Semicomplementation forces \(v\notin N(S)\) whenever \(v\in S\). The remaining function \(f_v\) is antitone and has \(f_v(\varnothing)=1\). Complementing inputs converts it bijectively to a nonzero monotone Boolean function on \(n-1\) coordinates. Exactly \(M(n-1)-1\) such functions exist. The choices for distinct \(v\) have no coupling conditions, and the lifting theorem realizes every combination. Multiplication over the \(n\) labelled atoms gives \((M(n-1)-1)^n\).

**The stronger comparison.** The extra \(\mathsf F\) requirement \(A\subseteq N(N(A))\), together with antitonicity, is equivalent to the Galois condition \(X\subseteq N(Y)\iff Y\subseteq N(X)\) for singleton subsets and therefore for all subsets. For distinct atoms \(u,v\), let \(uv\) be an undirected edge when \(u\in N(\{v\})\); the condition makes this symmetric, and semicomplementation prohibits loops. If \(u\in N(A)\), antitonicity gives \(u\in N(\{v\})\) for every \(v\in A\). Conversely, if all those adjacencies hold, symmetry gives \(A\subseteq N(\{u\})\); antitonicity then gives \(N(N(\{u\}))\subseteq N(A)\), and inflation gives \(u\in N(N(\{u\}))\). Thus \(N(A)\) is precisely the common graph-neighbourhood of \(A\). There are \(2^{\binom n2}\) graphs. This recovers the previously established graph-polarity specialization but is not counted as a new result here.

**Sharp separation.** On \(V=\{u,v\}\), define
\(N(\varnothing)=V\), \(N(\{u\})=\varnothing\), \(N(\{v\})=\{u\}\), and \(N(V)=\varnothing\). It is normalized, antitone, and semicomplementary. Its displayed lift is a \(\mathsf T\)-preconditional, but \(N(N(\{v\}))=\varnothing\), so it is not \(\mathsf F\). A nontrivial bounded lattice on fewer than four elements is a chain. On a bounded chain, semicomplementation forces \(N(a)=0\) whenever \(a>0\), while conditional identity forces \(N(0)=1\). Consequently \(a\le N(N(a))\) holds for all \(a\), proving this four-element separation is the smallest possible among nontrivial bounded lattices.

## Verification

Run `python3 check.py` with Python 3 and no third-party dependencies. The checker independently enumerates all normalized antitone coordinate functions for up to four atoms, constructs every derived negation for up to three atoms, checks every instance of (P1)–(P5), identity and semicomplementation in their binary lifts, and compares the \(\mathsf F\) cases against every graph polarity. It also enumerates the four possible \(\mathsf T\) binary operation tables on the four-element Boolean lattice. Expected final signal: `BOOLEAN_PRECONDITIONAL_REDUCT_OK`.

The program is finite corroboration. The proof above establishes the formulas for every integer \(n\ge1\); no exhaustive enumeration beyond the stated sizes is claimed.

## Relationship to prior work

Holliday introduced preconditionals and showed that their derived negations are antitone; the earlier work also analyzes additional stronger axioms, including orthocomplementation and the Sasaki hook. Chen established the algebraic \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\) hierarchy and its general completeness theory. The normalized antitone semicomplementation conditions themselves are classical in the theory of weak negations; their standalone existence is not claimed as new. Earlier finite-chain classifications find coincident \(\mathsf T\)- and \(\mathsf F\)-classes, and prior finite Boolean work characterizes the stricter \(\mathsf F\)-negations by undirected graph polarities, including the same lifting formula specialized to symmetric negations.

What is established here beyond those results is **sufficiency for every normalized antitone semicomplementation on every finite Boolean carrier**, together with its precise Dedekind-number count and the sharp strictness boundary for the \(\mathsf T\)-versus-\(\mathsf F\) hierarchy. In particular, the older Boolean graph result cannot imply the new census by simply replacing graph parameters: general \(\mathsf T\)-negations need not satisfy Galois reciprocity, and their coordinate functions range over the entire downset lattice rather than simple undirected graphs.

## Limitations

The census counts negation reducts, not binary conditional operations or isomorphism classes. It requires finite Boolean lattices; no corresponding formula is asserted for arbitrary distributive or non-distributive bounded lattices. No claim of an independent review or a newly invented Dedekind-number identity is made. The universal lifting theorem and its application to Chen's hierarchy are the core mathematical statements. Although targeted primary-literature and equivalence searches did not identify a directly covering classification, an older reformulation in the literature on protocomplementations or conditional extensions remains a possible historical-priority risk.

## References

- Z. Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221 (first publicly submitted 2026-07-22), especially Definitions 3.1 and 3.3 and Lemma 3.2.
- W. H. Holliday, *Preconditionals*, arXiv:2402.02296 (first submitted 2024); published in *The Logica Yearbook 2023* (2025), especially Proposition 1, Lemma 1, and the Sasaki-hook characterization.
- W. H. Holliday, *A Fundamental Non-Classical Logic*, *Logics* 1 (2023), 36–79, for weak negation classes.
- Classical Dedekind numbers: counts of monotone Boolean functions / order ideals of finite Boolean lattices, used as known combinatorial quantities rather than claimed as new.
