# Complete preconditional spectrum on the four-element Boolean lattice

## Finding

Let \(B=\mathcal P(\{p,q\})\), ordered by inclusion, with bottom \(0=\varnothing\), top \(1=\{p,q\}\), and atoms \(r\in\{\{p\},\{q\}\}\). A *preconditional* is a binary operation \(\Rightarrow:B^2\to B\) satisfying Holliday's axioms \(\mathrm{P1}\)–\(\mathrm{P5}\), stated below. It is a \(\mathsf K\)-algebra in Chen's terminology. Define the parameters
\[
 t=0\Rightarrow0,\qquad u_r=r\Rightarrow0,\qquad v_r=r\Rightarrow r.
\]

**Classification theorem.** An operation is a preconditional if and only if its complete table has the form
\[
 a\Rightarrow b=\begin{cases}
 t & a=0,\\
 b & a=1,\\
 v_r & a=r\text{ is an atom and }r\subseteq b,\\
 u_r & a=r\text{ is an atom and }r\not\subseteq b,
 \end{cases}
\]
with, independently for each atom \(r\), the following precise requirements:
\[
 v_r\in\{r,1\},\quad u_r\subseteq v_r,\quad
 (r\subseteq u_r\Longrightarrow u_r=v_r),
\]
\[
 (r\subseteq t\Longrightarrow v_r\subseteq t),\qquad
 (r\not\subseteq t\Longrightarrow u_r\subseteq t).
\]
Thus there are exactly \(41\) distinct preconditionals on the labeled lattice \(B\), and \(24\) up to lattice isomorphism. Precisely \(25\) are induced from precomplementations by \(a\Rightarrow b=\nu(a)\cup(a\cap b)\), whereas the other \(16\) cannot have that representation. The induced and noninduced subclasses have respectively \(15\) and \(9\) isomorphism classes.

Using Chen's additional conditions, there are exactly \(4\) \(\mathsf T\)-operations (\(3\) up to isomorphism), of which exactly \(2\) are \(\mathsf F\)-operations (\(2\) up to isomorphism). The latter two-operator subcount is independently recorded in earlier work and is included here for the complete spectrum, not claimed as a new isolated fact. Moreover \(B\) is the smallest possible cardinality of a bounded lattice whose \(\mathsf T\)-operations need not be \(\mathsf F\)-operations.

## Assumptions and scope

For all \(a,b,c\in B\), the defining conditions are
\[
\begin{aligned}
 \mathrm{P1}:&\quad 1\Rightarrow a\subseteq a,\\
 \mathrm{P2}:&\quad a\cap b\subseteq a\Rightarrow b,\\
 \mathrm{P3}:&\quad a\Rightarrow b\subseteq a\Rightarrow(a\cap b),\\
 \mathrm{P4}:&\quad a\Rightarrow(b\cap c)\subseteq a\Rightarrow b,\\
 \mathrm{P5}:&\quad a\Rightarrow((a\cap b)\Rightarrow c)\subseteq(a\cap b)\Rightarrow c.
\end{aligned}
\]
Write \(\nu(a)=a\Rightarrow0\). A \(\mathsf T\)-operation also obeys \(a\Rightarrow a=1\) and \(a\cap\nu(a)=0\) for every \(a\). An \(\mathsf F\)-operation additionally obeys \(a\subseteq\nu(\nu(a))\). Isomorphisms are the lattice automorphisms of \(B\) acting by transport of the entire conditional table; the only nonidentity automorphism exchanges the two atoms. No assertion is made about arbitrary larger Boolean algebras.

## Proof

**1. Normal form before \(\mathrm{P5}\).** Combining \(\mathrm{P3}\) with \(\mathrm{P4}\) gives the exact equality \(a\Rightarrow b=a\Rightarrow(a\cap b)\). For \(a=1\), the first two axioms give \(1\Rightarrow b=b\). For \(a=0\), the equality makes the row constant \(t\). If \(a=r\) is an atom, only the two intersections \(0\) and \(r\) are possible. Thus its row is completely given by \((u_r,v_r)\); \(\mathrm{P2}\) forces \(r\subseteq v_r\), while \(\mathrm{P4}\) forces \(u_r\subseteq v_r\). Conversely these restrictions make \(\mathrm{P1}\)–\(\mathrm{P4}\) true for the displayed table.

**2. Exact reduction of \(\mathrm{P5}\).** Let \(d=a\cap b\). For \(a=0\), the fifth axiom reads \(t\subseteq t\). For \(a=1\), it is equality because the top row is the identity. For an atomic antecedent \(a=r\), either \(d=0\) or \(d=r\). The first case is precisely \(r\Rightarrow t\subseteq t\). The second case reduces to \(r\Rightarrow u_r\subseteq u_r\) and \(r\Rightarrow v_r\subseteq v_r\), since the latter are the only values in row \(r\). The last inequality is automatic because \(r\subseteq v_r\). If \(r\subseteq u_r\), the remaining self-inequality reads \(v_r\subseteq u_r\), equivalent with \(u_r\subseteq v_r\) to \(u_r=v_r\); otherwise it is tautological. Finally \(r\Rightarrow t\subseteq t\) says \(v_r\subseteq t\) when \(r\subseteq t\), and \(u_r\subseteq t\) otherwise. Therefore the conditions in the statement are both necessary and sufficient, with no omitted triples.

**3. Count.** If \(t=0\), each atom has \(u_r=0\) and independently \(v_r=r\) or \(1\), yielding \(4\) tables. If \(t\) is one atom, its own row has \(2\) choices, while the other atom's row has \(3\) choices, yielding \(6\) for each of the two such \(t\). If \(t=1\), then per atom there are \(2\) possible pairs with \(v_r=r\) and \(3\) with \(v_r=1\), yielding \(5^2=25\). Thus \(4+6+6+25=41\).

Of these, \(7\) are fixed under exchanging atoms: \(2\) with \(t=0\), none with single-atom \(t\), and \(5\) with \(t=1\). Burnside's lemma gives \((41+7)/2=24\) isomorphism classes. An antitone precomplementation \(\nu\) has \(\nu(1)=0\), arbitrary \(\nu(0)=t\), and independent \(\nu(r)\subseteq t\) for both atoms; every such map gives a preconditional by the known precomplementation construction. The number is \(\sum_{t\in B}4^{|t|}=1+4+4+16=25\); distinct maps yield distinct operations since \(\nu(a)=a\Rightarrow0\). Exactly \(5\) of these induced operations are fixed under swapping the atoms, so the induced orbit count is \((25+5)/2=15\). Subtraction gives \(16\) noninduced operations in \(9\) orbits.

**4. Stronger systems and the least separation.** Conditional identity forces \(t=v_{\{p\}}=v_{\{q\}}=1\). Semicomplementation leaves just \(u_{\{p\}}\in\{0,\{q\}\}\) and \(u_{\{q\}}\in\{0,\{p\}\}\), yielding four \(\mathsf T\)-operations. Double-negation inflation forces the two nonzero choices to occur together; thus \(\mathsf F\) has exactly the assignments \((u_{\{p\}},u_{\{q\}})=(0,0)\) and \((\{q\},\{p\})\). Every lattice with fewer than four elements is a chain. On any bounded chain, conditional identity gives \(\nu(0)=1\), and semicomplementation forces \(\nu(x)=0\) for each nonzero \(x\); consequently \(x\le\nu(\nu(x))\) for all \(x\). The \(\mathsf T\)-assignment \((u_{\{p\}},u_{\{q\}})=(0,\{p\})\) on \(B\) violates this: \(\nu(\nu(\{q\}))=\nu(\{p\})=0\). This proves sharp minimality.

## Verification

Run \(\texttt{python3 verify_boolean_preconditionals.py}\) from this directory. The standalone checker constructs all \(144\) parameter tuples allowed by \(\mathrm{P1}\)–\(\mathrm{P4}\), independently evaluates all five original quantified axioms on all \(64\) triples of Boolean elements, and tests the symbolic criteria against these direct evaluations for every tuple. It also recomputes the exact counts, atom-swap orbits, precomplementation-induced subclass, \(\mathsf T\) and \(\mathsf F\) subclasses, and explicit strictness witnesses. A finite exhaustive checker corroborates this particular finite theorem; the completeness of the normal form is established by the proof above.

## Relationship to prior work

Holliday introduced the five preconditional axioms and the precomplementation-induced construction; an explicit non-Heyting four-element example already appears in the source, so this result does not claim that example. Chen defined the \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\) algebraic classes and their general completeness theorems, but does not give the full four-element Boolean conditional census. Separate prior finite-chain classifications concern linear orders, not the first branching Boolean lattice. An earlier finite Boolean \(\mathsf F\)-conditional result already gives the two \(\mathsf F\)-operations on \(B\) while studying the eight-element case; the new classification concerns **all** \(\mathsf K\)-operations on \(B\), their symmetry types, the induced/noninduced divide, and the intermediate \(\mathsf T\) subcount.

## Limitations

The theorem applies to the four-element Boolean lattice only and does not assert an enumeration for larger Boolean algebras or all bounded lattices. Its uniqueness is not independently certified: equivalent finite-algebra enumerations could be unindexed. The identity of the two already-known \(\mathsf F\) operations is recorded as context, not new evidence of originality.

## References

1. Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221v1 (first public version 2026-07-22), Sections 3.1–3.3.
2. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, Definition 1, Proposition 2 and Figure 2.
