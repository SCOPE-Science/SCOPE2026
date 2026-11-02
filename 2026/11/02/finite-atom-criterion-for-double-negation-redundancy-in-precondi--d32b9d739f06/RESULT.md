# Finite atom criterion for double-negation redundancy in preconditional lattices

## Finding

Consider the three algebraic systems of Chen's fundamental propositional logic with a preconditional, using Holliday's five axioms. For each **finite bounded lattice** \(L\), let \(\mathcal T(L)\) be all preconditional operations on its fixed carrier satisfying conditional identity and semicomplementation, and let \(\mathcal F(L)\subseteq\mathcal T(L)\) also satisfy double-negation inflation. Then

\[
\boxed{\mathcal T(L)=\mathcal F(L)\quad\Longleftrightarrow\quad
L\text{ has at most one atom}.}
\]

For a nontrivial finite lattice, this is equivalent to \(0\) being meet-prime (there are no two nonzero elements whose meet is \(0\)). The criterion holds **without distributivity, modularity, or a chain assumption**. A canonical \(\mathcal F\)-preconditional exists on every bounded lattice; the two-atom witness below alters only one antecedent row of this canonical operation.

The least finite carrier on which the two algebraic classes differ has four elements: the Boolean diamond \(B_2=\{0,p,q,1\}\). On this carrier there are exactly four \(\mathcal T\)-operations and exactly two \(\mathcal F\)-operations. Under lattice automorphisms, the four \(\mathcal T\)-operations form three isomorphism classes and the two \(\mathcal F\)-operations form two classes.

## Assumptions and scope

A bounded lattice \((L,\wedge,\vee,0,1)\) may be the one-element lattice. An **atom** is an element \(u>0\) having no element strictly between \(0\) and \(u\). A *preconditional* \(\to\) obeys, for all \(a,b,c\in L\), the source's axioms

\[
\begin{aligned}
\text{(P1)}&\quad 1\to a\le a,\\
\text{(P2)}&\quad a\wedge b\le a\to b,\\
\text{(P3)}&\quad a\to b\le a\to(a\wedge b),\\
\text{(P4)}&\quad a\to(b\wedge c)\le a\to b,\\
\text{(P5)}&\quad a\to((a\wedge b)\to c)\le(a\wedge b)\to c.
\end{aligned}
\]

Write \(\neg a=a\to0\). Membership in \(\mathcal T(L)\) adds \(a\to a=1\) and \(a\wedge\neg a=0\). Membership in \(\mathcal F(L)\) additionally requires \(a\le\neg\neg a\). These are properties of **operations on the fixed underlying lattice**, not an assertion that the corresponding global deductive systems are identical.

## Proof

### One or zero atoms: automatic double negation

Every nonzero element of a nontrivial *finite* lattice lies above an atom. If there is a unique atom \(u\), every nonzero element contains \(u\). Consequently any two nonzero elements have nonzero meet. In a \(\mathcal T\)-expansion, the semicomplement law \(a\wedge\neg a=0\) therefore forces \(\neg a=0\) whenever \(a>0\). Conditional identity at \(0\) gives \(\neg0=0\to0=1\). Hence for every \(a>0\), \(\neg\neg a=\neg0=1\ge a\); at \(a=0\) the double-negation inequality is automatic. Thus every \(\mathcal T\)-operation is an \(\mathcal F\)-operation. On a singleton lattice the conclusion is immediate.

### Two atoms: a universal separating preconditional

For context, every bounded lattice admits the canonical operation \(a\to_0 b=1\) if \(a\le b\), and \(a\to_0b=a\wedge b\) otherwise. It obeys (P1)-(P4); for (P5), if \(d=a\wedge b\nleq c\), its inner output is \(d\wedge c<d\le a\) and the outer output is exactly \(d\wedge c\). The derived negation is \(\neg0=1\) and \(\neg a=0\) for every positive \(a\), so this is always a \(\mathcal F\)-operation.

Conversely, suppose the finite lattice has distinct atoms \(p,q\). In particular \(p\wedge q=0\), \(p\nleq q\), and \(p<1\). Define a binary operation for every \(a,b\in L\) by

\[
a\Rightarrow b=\begin{cases}
1,&a\le b,\\
q,&a=p\text{ and }a\nleq b,\\
a\wedge b,&a\ne p\text{ and }a\nleq b.
\end{cases}
\]

We verify all five axioms, including the potentially restrictive importation axiom (P5).

For (P1), the row with antecedent \(1\) is the identity: since \(p\ne1\), \(1\Rightarrow b=b\) whether or not \(b=1\). For (P2), if \(a\le b\) the output is top, and if \(a\nleq b\) the output is either \(a\wedge b\) or, when \(a=p\), the value \(q\), in which case the atomicity of \(p\) gives \(p\wedge b=0\). Thus \(a\wedge b\le a\Rightarrow b\).

The operation depends on \(b\) only through \(a\wedge b\). Indeed, \(a\le b\) iff \(a\le a\wedge b\), and when \(a=p\) but \(p\nleq b\), atomicity gives \(p\wedge b=0\). Therefore \(a\Rightarrow b=a\Rightarrow(a\wedge b)\), proving (P3) with equality. Each row is monotone in its consequent: the row for \(p\) jumps from \(q\) to \(1\) when the consequent begins to contain \(p\); any other row has the value \(a\wedge b\) below the threshold \(a\le b\), and the value \(1\) at or above that threshold. Monotonicity proves (P4).

For (P5), put \(d=a\wedge b\), so \(d\le a\). We must show \(a\Rightarrow(d\Rightarrow c)\le d\Rightarrow c\). If \(d\le c\), then \(d\Rightarrow c=1\) and the inequality is immediate. Otherwise \(d>0\). If \(d=p\), then \(d\Rightarrow c=q\). As \(p\le a\) and \(p\nleq q\), we have \(a\nleq q\); if \(a=p\) the outer conditional equals \(q\), and if \(a\ne p\) it is \(a\wedge q\le q\). Finally, if \(d\ne p\) and \(d\nleq c\), then \(d\Rightarrow c=d\wedge c<d\le a\). In this case \(a\ne p\), because \(0<d\le p\) would force \(d=p\). Therefore \(a\Rightarrow(d\wedge c)=a\wedge d\wedge c=d\wedge c\). All cases satisfy (P5).

Conditional identity holds by the first case of the definition. The negation is explicitly

\[
\neg0=1,\qquad\neg p=q,\qquad
\neg a=0\quad(a>0,\ a\ne p).
\]

Since \(p\wedge q=0\), this is a semicomplementation. Thus \(\Rightarrow\in\mathcal T(L)\). But \(\neg\neg p=\neg q=0\) and \(p\nleq0\), so \(\Rightarrow\notin\mathcal F(L)\). This establishes the converse and the criterion for every finite bounded lattice.

### The sharp four-element census

Every finite bounded lattice with fewer than four elements is a chain and has at most one atom. A four-element lattice with two atoms is necessarily \(B_2\). Put \(B_2=\{0,p,q,1\}\), with \(p\wedge q=0\). In any \(\mathcal T(B_2)\)-operation, (P1)-(P2) force \(1\to b=b\); conditional identity and (P3)-(P4) give \(0\to b=1\) and \(a\to b=a\to(a\wedge b)\). Thus the only undetermined entries are \(u=p\to0=p\to q\) and \(v=q\to0=q\to p\). Semicomplementation forces

\[
u\in\{0,q\},\qquad v\in\{0,p\}.
\]

Conversely every one of these four choices satisfies (P1)-(P5) and conditional identity; for (P5), the inner antecedent \(d=a\wedge b\) is \(0,p,q,1\). The cases \(d=0\) or \(d\le c\) give inner output \(1\); if \(d=p\nleq c\), the inner output is \(u\in\{0,q\}\), fixed by either possible outer row \(a=p\) or \(a=1\); the case \(d=q\nleq c\) is symmetric. Hence \(|\mathcal T(B_2)|=4\). Directly applying \(a\le\neg\neg a\) shows that precisely the parameter pairs \((u,v)=(0,0)\) and \((u,v)=(q,p)\) are \(\mathcal F\)-operations. Hence \(|\mathcal F(B_2)|=2\). Swapping \(p\) and \(q\) exchanges the two mixed pairs and fixes both unmixed pairs, giving the isomorphism counts.

## Verification

Run \(\texttt{python3 checker.py}\) from the directory containing the standalone checker. It evaluates (P1)-(P5), conditional identity, semicomplementation, and double-negation inflation directly from operation tables. It verifies the four \(\mathcal T\)- and two \(\mathcal F\)-expansions on \(B_2\), brute-force scans all operations on chains of two and three elements, verifies the separating construction on all \(242\) labelled posets on one through four points via their finite ideal lattices (including \(154\) with two or more atoms), and verifies a nondistributive five-element diamond. The final printed line is \(\texttt{ALL_CHECKS_OK}\). Finite tests are supporting checks; the proof above establishes the universal quantifier over all finite bounded lattices.

## Relationship to prior work

Chen defines \(\mathcal T\)- and \(\mathcal F\)-algebras and proves soundness and completeness results; Holliday gives the five preconditional axioms and their representation theory. The published *Fixed-point normal form for finite-chain preconditionals* proves equality of these expansions **on finite chains**. Since every chain has one atom, this is a special case of the criterion above, not a theorem covering arbitrary finite lattices. The new part is the sharp **if-and-only-if criterion on all finite bounded lattice reducts**, with a uniform witness for every lattice having two atoms, and the complete first separating-carrier census. Nothing is claimed about the earlier chain classification or about the general representation and completeness theorems.

## Limitations

The atom criterion is proved for **finite** bounded lattices. Its converse is not asserted for arbitrary infinite atomless lattices. The classification does not enumerate conditional operations on arbitrary nonchain lattices, does not classify relational presentations, and does not strengthen the global decidability bounds of the underlying logical systems. Priority searches are non-exhaustive, especially for equivalent formulations in older lattice-with-negation literature. 

## References

[1] Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221, first posted 22 July 2026. https://arxiv.org/abs/2607.20221

[2] Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, first posted 3 February 2024. https://arxiv.org/abs/2402.02296

[3] *Fixed-point normal form for finite-chain preconditionals*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-fixed-point-normal-form-for-finite-chain-preconditionals--3d55c0067825

[4] Wesley H. Holliday and Guillaume Massas, *Fundamental Logic Through the Lens of Modality*, arXiv:2606.29954, first posted 29 June 2026. https://arxiv.org/abs/2606.29954
