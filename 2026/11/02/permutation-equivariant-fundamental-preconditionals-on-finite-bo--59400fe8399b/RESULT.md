# Permutation-equivariant fundamental preconditionals on finite Boolean algebras

## Finding

**Theorem.** Fix an integer \(m\ge2\) and an \(m\)-element set \(U\). On the bounded Boolean lattice \(\mathcal P(U)\), consider binary operations \(\Rightarrow\) satisfying the five preconditional laws (P1)–(P5) below, conditional identity, semicomplementation, and double-negation inflation. Suppose also that \(\Rightarrow\) commutes with every permutation of \(U\). Exactly one such operation has Boolean-complement negation, namely material implication
\[
 A\Rightarrow B=(U\setminus A)\cup B.
\]
Every other operation has the induced negation \(N(\varnothing)=U\) and \(N(A)=\varnothing\) for nonempty \(A\), and is characterized uniquely as follows.

For each \(1\le k\le m-1\), choose nonnegative integers \(z_k,b_k,c_k\) with \(z_k+b_k+c_k=k-1\). Put \(z_1=b_1=c_1=0\). These choices are admissible exactly when
\[
 z_1\le z_2\le\cdots\le z_{m-1},\qquad
 b_d>0\ \Longrightarrow\ c_k\le c_d\quad(1\le d<k\le m-1).
\]
For \(\varnothing\ne A\subsetneq U\) and \(D=A\cap B\), the operation is determined by
\[
 A\Rightarrow B=\begin{cases}
 \varnothing,&D=\varnothing,\\
 U,&D=A,\\
 D,&1\le |D|\le z_{|A|},\\
 D\cup(U\setminus A),&z_{|A|}<|D|\le z_{|A|}+b_{|A|},\\
 U,&z_{|A|}+b_{|A|}<|D|<|A|.
 \end{cases}
\]
The exceptional rows are \(\varnothing\Rightarrow B=U\) and \(U\Rightarrow B=B\). Conversely, every admissible array gives such an operation; distinct arrays give distinct operations.

The exact number \(N_m\) of these labelled-carrier, permutation-equivariant expansions (including material implication) is the number of admissible arrays plus one. For \(m=2,3,4,5,6,7,8\), respectively,
\[
 (N_2,N_3,N_4,N_5,N_6,N_7,N_8)=(2,4,13,55,261,1310,6802).
\]
There is a finite-state exact recurrence: begin at rank \(1\) with state \((z,h)=(0,\infty)\) of weight \(1\). At rank \(k\ge2\), from each state \((z,h)\) select integers \(z'\in[z,k-1]\), \(c'\in[0,k-1-z']\) with \(c'\le h\), and set \(b'=k-1-z'-c'\). Transfer the state to \((z',\min(h,c'))\) if \(b'>0\), and to \((z',h)\) otherwise, summing weights. After rank \(m-1\), add one to the total weight. The initial \(\infty\) is an unconstrained upper bound and can be represented by \(m\).

## Assumptions and scope

All quantifiers range over subsets of the same finite \(U\), with inclusion as the lattice order. The preconditional axioms are
\[
\begin{aligned}
\mathrm{(P1)}\;&U\Rightarrow B\subseteq B;\\
\mathrm{(P2)}\;&A\cap B\subseteq A\Rightarrow B;\\
\mathrm{(P3)}\;&A\Rightarrow B\subseteq A\Rightarrow(A\cap B);\\
\mathrm{(P4)}\;&A\Rightarrow(B\cap C)\subseteq A\Rightarrow B;\\
\mathrm{(P5)}\;&A\Rightarrow((A\cap B)\Rightarrow C)\subseteq (A\cap B)\Rightarrow C.
\end{aligned}
\]
The additional fundamental conditions are \(A\Rightarrow A=U\), \(A\cap N(A)=\varnothing\), and \(A\subseteq N(N(A))\), where \(N(A)=A\Rightarrow\varnothing\). Permutation equivariance means \(\sigma(A\Rightarrow B)=\sigma(A)\Rightarrow\sigma(B)\) for every permutation \(\sigma:U\to U\). No monotonicity in the antecedent, Heyting adjunction, or modus ponens is assumed.

## Proof

**Step 1: reduction of the rows and negation.** (P3) and (P4) give \(A\Rightarrow B=A\Rightarrow(A\cap B)\). (P1) and (P2) give \(U\Rightarrow B=B\). Conditional identity, (P3), and (P4) give \(\varnothing\Rightarrow B=U\). The standard preconditional antitonicity lemma says \(A\subseteq B\Rightarrow N(B)\subseteq N(A)\); indeed, (P4) gives \(N(B)=B\Rightarrow\varnothing\subseteq B\Rightarrow N(A)\) when \(A\subseteq B\), and (P5), with \(B\cap A=A\), bounds the right-hand side by \(N(A)\).

For a proper nonempty \(A\), semicomplementation gives \(N(A)\subseteq U\setminus A\). The stabilizer of \(A\) acts transitively on \(U\setminus A\), so permutation equivariance forces \(N(A)\in\{\varnothing,U\setminus A\}\), with the choice depending only on \(|A|\). If \(N(A)=U\setminus A\) for some \(A\), antitonicity gives Boolean negation on all singleton subsets of \(A\), and inflation gives Boolean negation on their co-singleton complements. Every proper nonempty set lies within a co-singleton; antitonicity then forces the complement option for that set. Thus either \(N\) is Boolean complementation at every set or \(N(A)=\varnothing\) for every nonempty \(A\).

In the complement case, (P4) implies \(N(A)\subseteq A\Rightarrow B\), and (P2) implies \(A\cap B\subseteq A\Rightarrow B\). Conversely, take \(D=A\setminus B\) in (P5), with its consequent \(\varnothing\). Since \(N(D)=U\setminus D=(U\setminus A)\cup B\), (P5) gives \(A\Rightarrow N(D)\subseteq N(D)\). Row reduction gives \(A\Rightarrow N(D)=A\Rightarrow B\), so material implication is forced. Its standard Boolean-algebra adjunction proves all the laws.

**Step 2: local row alphabet.** Now suppose negation is degenerate. Fix \(\varnothing\ne A\subsetneq U\) and \(D\subsetneq A\) with \(D\ne\varnothing\). By (P2), \(D\subseteq A\Rightarrow D\). The stabilizer fixing \(A\) and \(D\) setwise has three orbits \(D\), \(A\setminus D\), and \(U\setminus A\); therefore the only possible outputs are \(D\), \(A\), \(D\cup(U\setminus A)\), and \(U\). (P5) with its inner antecedent equal to \(A\) gives \(A\Rightarrow(A\Rightarrow D)\subseteq A\Rightarrow D\). The option \(A\Rightarrow D=A\) violates this because \(A\Rightarrow A=U\not\subseteq A\). We retain only three types: \(0=D\), \(1=D\cup(U\setminus A)\), and \(2=U\).

For \(D=\varnothing\) the output is \(N(A)=\varnothing\), and for \(D=A\) it is \(U\). By (P4), these types are nondecreasing as \(|D|\) increases: if \(D\subseteq E\subseteq A\), then \(A\Rightarrow D\subseteq A\Rightarrow E\). Hence every row is a word \(0^{z_k}1^{b_k}2^{c_k}\) of length \(k-1\), determined by its triple.

**Step 3: the exact compatibility constraints.** Let \(\varnothing\ne D\subsetneq A\subsetneq U\), where \(|D|=d<k=|A|\), and examine (P5) as \(C\) varies. Put \(E=D\cap C\), \(|E|=j\). If \(D\Rightarrow E=\varnothing\) or \(U\), (P5) is automatic. If the \(D\)-row has type \(0\) at \(j\), then \(D\Rightarrow E=E\), so (P5) requires \(A\Rightarrow E\subseteq E\): exactly type \(0\) in the \(k\)-row at \(j\). As \(j\) ranges over the zero prefix, this is equivalent to \(z_k\ge z_d\).

If instead the \(D\)-row has type \(1\) at \(j\), its output is \(E\cup(U\setminus D)\). Its intersection with \(A\) has size \(k-d+j\), and (P5) says the corresponding \(k\)-row output is contained in \(E\cup(U\setminus D)\). Types \(0\) and \(1\) satisfy this inclusion; type \(2\) fails because \(D\setminus E\ne\varnothing\). Requiring type \(\le1\) for every \(j\) in the \(d\)-row's ones interval is equivalent (by checking its maximal \(j=d-1-c_d\)) to \(c_k\le c_d\) whenever \(b_d>0\). These implications for all \(d<k\) give precisely the two stated array restrictions. If \(D=\varnothing\), then \(D\Rightarrow C=U\), and (P5) is tautological. If \(D=A\), (P5) is row idempotence, automatic for each of the three row types. If \(A=U\), (P5) follows from \(U\Rightarrow X=X\). Thus the restrictions are both necessary and sufficient for (P5).

**Step 4: the other conditions and counting.** Each listed operation obeys (P1)–(P4) by its top-row identity, intersection-dependence, inclusion of \(D\), and monotone rows. The weak negation satisfies semicomplementation and double-negation inflation because \(N(N(A))=U\) for nonempty \(A\). Conditional identity is built in. Distinct triple arrays differ on an orbit of pairs, and cannot define the same binary operation. The recurrence scans all choices of zero prefixes and two suffixes while remembering precisely the active upper bound on future two suffixes; induction on the ranks proves that its weight counts all admissible arrays, giving the exact count and displayed values.

## Verification

The accompanying standard-library `checker.py` independently enumerates all permutation-orbit choices before applying the theorem, evaluates (P1)–(P5) and the three fundamental conditions on every triple of subsets, and compares the survivors with the proposed forms for \(m=2,3,4\). It reports exact agreement and survivor totals \(2,4,13\). Separately it constructs admissible arrays for \(m=2,\ldots,8\), yielding \(2,4,13,55,261,1310,6802\), and confirms these counts through an independent state-recurrence implementation. The finite checker is corroboration, not a substitute for the all-\(m\) proof above.

## Relationship to prior work

Holliday introduced the five preconditional axioms and established properties of their induced negation. Chen introduced the \(\mathsf F\) extension with conditional identity, semicomplementation and double-negation inflation. These are the exact input axioms, not new definitions. Related classifications on finite chains and finite three-atom Boolean algebras answer different counting problems; their statements do not determine the all-size permutation-equivariant classification of the binary operation. The present finding concerns precisely the automorphism-invariant expansions, and does not assert an original description of Boolean material implication or the general preconditional framework.

## Limitations

The theorem is specific to finite atomic Boolean lattices and invariance under *all* atom permutations. It does not count unrestricted preconditionals, lattices other than powersets, or equational subclasses requiring further axioms such as modus ponens. The displayed counts are rigorously determined by the structural theorem; finite enumeration alone would not verify their continuation. A possible equivalent classification under alternative symmetry/clone terminology remains a priority risk. No independent audit has been performed.

## References

1. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296 (first posted February 3, 2024), Definition 1, Proposition 1, and Sections 2.2–2.4. https://arxiv.org/abs/2402.02296
2. Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221 (first posted July 22, 2026), algebraic \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\) semantics. https://arxiv.org/abs/2607.20221
