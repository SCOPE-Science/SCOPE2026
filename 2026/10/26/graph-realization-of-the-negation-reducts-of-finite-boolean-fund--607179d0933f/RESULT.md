# Graph realization of the negation reducts of finite Boolean fundamental preconditionals

## Finding

**Theorem.** Fix a finite nonempty set \(V\) of \(n\) labelled atoms and the Boolean lattice \(B=\mathcal P(V)\). For a Chen \(\mathsf F\)-preconditional \(\to\) on \(B\), write \(N(A)=A\to\varnothing\). The **set of possible induced unary operations \(N\)** is in canonical bijection with the simple undirected graphs on \(V\). More precisely, each such graph \(G=(V,E)\) supplies
\[
N_G(A)=\{v\in V:\text{for every }a\in A,\ \{v,a\}\in E\},\qquad N_G(\varnothing)=V,
\]
and an explicit realizing conditional
\[
\boxed{A\Rightarrow_G B=N_G(A\setminus B)\cup(A\cap B).}
\]
Conversely every \(\mathsf F\)-preconditional on \(B\) induces exactly one of these operations, and the graph is recovered from the singleton values by \(\{u,v\}\in E\iff v\in N(\{u\})\) for distinct atoms. Thus there are **exactly** \(2^{\binom n2}\) distinct labelled unary negation reducts of \(\mathsf F\)-preconditionals on \(B\). This is **not** a count of all binary preconditionals on \(B\).

The displayed conditional satisfies **both modus ponens** and **normality**, despite allowing nonclassical negations:
\[
A\cap(A\Rightarrow_G B)\subseteq B,\qquad
(A\Rightarrow_G B)\cap(A\Rightarrow_G C)=A\Rightarrow_G(B\cap C).
\]
For this explicit family, **negation import**
\[
N_G(A\Rightarrow_G B)\subseteq A\Rightarrow_G N_G(B)\qquad(\forall A,B\subseteq V)
\]
holds **if and only if \(G\) is complete**. In the complete-graph case the conditional reduces to classical Boolean implication \(V\setminus A\cup B\). This last equivalence concerns the constructed family, not every possible preconditional with the same negation.

## Assumptions and scope

The term preconditional uses precisely the five inequalities of Chen's Definition 3.1 on a bounded lattice:
\[
\begin{gathered}
1\to a\leq a,\quad a\wedge b\leq a\to b,\quad
 a\to b\leq a\to(a\wedge b),\\
 a\to(b\wedge c)\leq a\to b,\quad
 a\to((a\wedge b)\to c)\leq(a\wedge b)\to c.
\end{gathered}
\]
An \(\mathsf F\)-algebra additionally satisfies the three laws from Chen's Definition 3.3: conditional identity \(a\to a=1\), semicomplementation \(a\wedge(a\to0)=0\), and double-negation inflation \(a\leq (a\to0)\to0\). All graph vertices/atoms are labelled, graphs have no loops or multiple edges, and all sets and operations are finite. The theorem concerns the **unary reduct** \(N\), not uniqueness of its binary conditional extension.

## Proof

### I. Every induced negation is a simple-graph polarity

For a preconditional, Chen's Lemma 3.2 (alternatively Holliday's Proposition 3) establishes that its derived negation \(N\) is order reversing. The three additional \(\mathsf F\) laws give
\[
N(\varnothing)=V,\qquad X\cap N(X)=\varnothing,\qquad X\subseteq N(N(X)).
\]
The first equality follows from \(\varnothing\to\varnothing=V\). Antitonicity and double-negation inflation imply the **self-adjoint polarity equivalence**
\[
X\subseteq N(Y)\quad\Longleftrightarrow\quad Y\subseteq N(X).
\]
Indeed, if \(X\subseteq N(Y)\), antitonicity gives \(N(N(Y))\subseteq N(X)\), while \(Y\subseteq N(N(Y))\). The converse follows by swapping \(X,Y\).

Set \(u\sim v\) exactly when \(v\in N(\{u\})\). The polarity equivalence makes \(\sim\) symmetric; semicomplementation makes it irreflexive. Thus it is a simple undirected graph. For any \(A\subseteq V\), applying the polarity equivalence to singleton sets gives
\[
\begin{aligned}
v\in N(A)&\Longleftrightarrow \{v\}\subseteq N(A)
\Longleftrightarrow A\subseteq N(\{v\})\\
&\Longleftrightarrow (\forall a\in A)\ a\in N(\{v\})
\Longleftrightarrow(\forall a\in A)\ v\in N(\{a\}).
\end{aligned}
\]
So \(N=N_G\), including the empty-set case. Different labelled graphs give different singleton negations. This proves the **upper bound** on the number of possible unary reducts.

### II. Every graph has an \(\mathsf F\)-conditional lifting

For an arbitrary simple graph define \(N=N_G\). Its direct description shows the four identities
\[
N(\varnothing)=V,\quad N(X\cup Y)=N(X)\cap N(Y),\quad
X\cap N(X)=\varnothing,\quad X\subseteq N(N(X)).
\]
The third uses the absence of loops, the fourth symmetry. In particular \(N\) is antitone.

Define \(A\Rightarrow B=N(A\setminus B)\cup(A\cap B)\). We check all five preconditional axioms in the Boolean lattice.

**P1.** \(V\Rightarrow B=N(V\setminus B)\cup B=B\), since no vertex of \(V\setminus B\) is adjacent to itself and therefore \(N(V\setminus B)\subseteq B\).

**P2.** \(A\cap B\subseteq A\Rightarrow B\) by the displayed union.

**P3.** Both \(A\setminus B\) and \(A\cap B\) are unchanged when \(B\) is replaced by \(A\cap B\); hence \(A\Rightarrow B=A\Rightarrow(A\cap B)\).

**P4.** The relation \(B\cap C\subseteq B\) implies \(A\setminus B\subseteq A\setminus(B\cap C)\), and antitonicity gives \(N(A\setminus(B\cap C))\subseteq N(A\setminus B)\). The other union component \(A\cap B\cap C\) is contained in \(A\cap B\). Therefore \(A\Rightarrow(B\cap C)\subseteq A\Rightarrow B\).

**P5.** Put \(U=A\cap B\), \(X=U\setminus C\), and \(T=U\Rightarrow C=N(X)\cup(U\cap C)\). Since \(X\cap N(X)=\varnothing\) and \(X\cap C=\varnothing\), we have \(X\cap T=\varnothing\), so \(X\subseteq A\setminus T\). Antitonicity gives \(N(A\setminus T)\subseteq N(X)\subseteq T\). Also \(A\cap T\subseteq T\). Consequently \(A\Rightarrow T=N(A\setminus T)\cup(A\cap T)\subseteq T\), as required.

Furthermore \(A\Rightarrow A=N(\varnothing)\cup A=V\) proves conditional identity; \(A\Rightarrow\varnothing=N(A)\) proves the claimed induced negation; and \(A\cap N(A)=\varnothing\) and \(A\subseteq N(N(A))\) prove the remaining \(\mathsf F\) laws. The realization proves the lower bound \(2^{\binom n2}\) and the stated bijection.

### III. Two strengthening laws

For modus ponens, compute
\[
A\cap(A\Rightarrow B)
=[A\cap N(A\setminus B)]\cup(A\cap B).
\]
Any point of the first term lying outside \(B\) would lie in both \(A\setminus B\) and its negation, impossible by semicomplementation. Thus the whole expression is contained in \(B\).

For normality put \(X=A\setminus B\), \(Y=A\setminus C\). Then
\[
N(X)\cap N(Y)=N(X\cup Y)=N(A\setminus(B\cap C)).
\]
When distributing the intersection of the two unions in the definition of \(\Rightarrow\), the remaining terms are all contained in \(A\cap B\cap C\): for example, \(N(X)\cap A\cap C\subseteq B\), since \(N(X)\cap X=\varnothing\); similarly for \(N(Y)\cap A\cap B\). The intersection term \((A\cap B)\cap(A\cap C)=A\cap B\cap C\) is already present. This proves the claimed equality.

### IV. Negation import has the sharp complete-graph boundary

If \(G\) is complete, every set has \(N_G(X)=V\setminus X\), and \(A\Rightarrow_G B=(V\setminus A)\cup B\), the ordinary Boolean implication. Its negation-import inequality is immediate: \(N_G(A\Rightarrow_G B)=A\setminus B\subseteq(V\setminus A)\cup(V\setminus B)=A\Rightarrow_G N_G(B)\) requires care because \(A\setminus B\) need not lie in \(V\setminus A\), **but it lies in \(V\setminus B\)**, so the inclusion follows.

Conversely suppose \(G\) is not complete, and choose two different nonadjacent vertices \(i,j\). Let \(A=\{i\}\) and \(B=\{j\}\). Then \(A\Rightarrow_G B=N_G(A)\), and \(i\in N_G(N_G(A))=N_G(A\Rightarrow_G B)\) by double-negation inflation. On the other hand \(i\notin N_G(B)\) since \(i,j\) are nonadjacent, so \(A\Rightarrow_G N_G(B)=N_G(A)\), which does not contain \(i\) by irreflexivity. The negation-import inclusion fails.

## Verification

The included independent-of-library, standard-library-only script `graph_preconditional_check.py` exhaustively enumerates all simple labelled graphs on \(1\) to \(4\) vertices and all subset triples, evaluating P1–P5, conditional identity, semicomplementation, double-negation inflation, modus ponens, normality, the exact induced-negation identity and the negation-import classification. Run `python3 graph_preconditional_check.py` from the extracted package. The observed output was

```
atoms 1 graphs 1 axiom-triples 8
atoms 2 graphs 2 axiom-triples 128
atoms 3 graphs 8 axiom-triples 4096
atoms 4 graphs 64 axiom-triples 262144
GRAPH_PRECONDITIONAL_OK 266376
```

The finite test is corroboration only; the proof above establishes all statements uniformly for every finite \(n\ge1\).

## Relationship to prior work

Chen's 2026 preconditional algebraic semantics, Definitions 3.1 and 3.3, provides exactly the five axioms and the \(\mathsf F\) conditions tested here. His Remark 3.5 identifies the negation reduct as a fundamental lattice and cites earlier weak-pseudocomplementation theory; his general relational and conservativity results do not classify which unary negations occur **on each fixed finite Boolean carrier** or exhibit the conditional \(N_G(A\setminus B)\cup(A\cap B)\) with modus ponens, normality and the sharp negation-import boundary.

Holliday's 2024/2025 *Preconditionals*, Proposition 4, constructs \(\neg A\vee(A\wedge B)\) from an arbitrary precomplementation. That construction does not generally satisfy conditional identity for a graph negation: \(N_G(A)\cup A\) need not be the top element. The present conditional evaluates \(N_G(A\setminus B)\) instead, ensuring identity and the further laws. Holliday's 2023 article establishes relational representation for weak pseudocomplementations and general preconditionals; it does not state this finite Boolean lifting and exact graph-reduct spectrum.

Available previous classifications for \(\mathsf F\)-preconditionals on **finite chains** give a factorial census with a single common chain-negation reduct. A finite Boolean lattice with two atoms is a nonchain and already admits two different unary reducts, indexed by the empty and single-edge graph. Neither the previous chain results nor a general representation into a possibly larger lattice implies this exact same-carrier graph classification. This is a scoped, conditional lifting result, not an assertion that the polarity/graph encoding of a fundamental negation is itself new.

## Limitations

The formula counts distinct **unary negation operations**, not the number of \(\mathsf F\)-preconditionals, nor the number of their possible binary operations, nor their isomorphism classes without atom labels. Isomorphism classes of unary reducts correspond to unlabelled simple graphs, but no enumeration of unlabelled graphs is needed for the result. The sharp negation-import assertion is for the explicit constructed operation \(\Rightarrow_G\), not for every extension of \(N_G\). These structures generally **fail weak monotonicity** \(B\subseteq A\Rightarrow_G B\) on noncomplete graphs, so they do not contradict the theorem characterizing Heyting implications by modus ponens and weak monotonicity. Priority uncertainty remains possible for a general same-carrier extension theorem not identified in the checked literature; no independent validation has been performed.

## References

[1] Zhicheng Chen, “Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations,” arXiv:2607.20221, first public 22 July 2026, §§3–4. https://arxiv.org/abs/2607.20221

[2] Wesley H. Holliday, “Preconditionals,” arXiv:2402.02296, first public 3 February 2024, Propositions 3–6 and §3. https://arxiv.org/abs/2402.02296

[3] Wesley H. Holliday, “A Fundamental Non-Classical Logic,” *Logics* 1 (2023), 36–79, arXiv:2207.06993, §§3–4 and §6. https://arxiv.org/abs/2207.06993

[4] “Fixed-point normal form for finite-chain preconditionals,” published mathematical record, 4 October 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-fixed-point-normal-form-for-finite-chain-preconditionals--3d55c0067825
