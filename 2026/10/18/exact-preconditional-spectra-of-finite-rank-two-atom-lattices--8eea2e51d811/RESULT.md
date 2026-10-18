# Exact preconditional spectra of finite rank-two atom lattices

## Finding

For each integer \(k\ge2\), let \(M_k\) be the bounded lattice with bottom \(0\), top \(1\), and \(k\) pairwise incomparable atoms \(a_1,\ldots,a_k\), with every atom strictly between the bounds. A **preconditional** is a binary operation \(\Rightarrow\) satisfying the five axioms in the next section. The number of labeled preconditionals on \(M_k\) is exactly
\[
N_k=2^k+2k3^{k-1}+(k+3)^k.
\]
Exactly
\[
I_k=1+k2^k+(k+2)^k
\]
of these are induced by precomplementations \(\nu\) through \(a\Rightarrow b=\nu(a)\vee(a\wedge b)\). Consequently
\[
\lim_{k\to\infty}\frac{I_k}{N_k}=e^{-1}.
\]
There is a complete, constructive normal form for every operation counted. In particular, \(N_2=41\), \(I_2=25\), while the first nondistributive case has \(N_3=278\), \(I_3=150\). All counts are for the fixed labeled lattice; they are not isomorphism-class counts. The \(k=2\) values are a previously recorded special case, not a novelty claim.

## Assumptions and scope

The lattice operation \(\wedge\) is the meet. For every \(x,y,z\in M_k\), require:

1. \(1\Rightarrow x\le x\).
2. \(x\wedge y\le x\Rightarrow y\).
3. \(x\Rightarrow y\le x\Rightarrow(x\wedge y)\).
4. \(x\Rightarrow(y\wedge z)\le x\Rightarrow y\).
5. \(x\Rightarrow((x\wedge y)\Rightarrow z)\le(x\wedge y)\Rightarrow z\).

These are Holliday's preconditional axioms, also used as the algebraic semantics of Chen's \(\mathsf K\) system. The theorem concerns \(\mathsf K\)-algebras; no assertion is made about the stricter \(\mathsf T\) or \(\mathsf F\) classes. A precomplementation here means an antitone unary map \(\nu\) with \(\nu(1)=0\).

## Proof

Axioms 3 and 4 give the identity \(x\Rightarrow y=x\Rightarrow(x\wedge y)\); axiom 4 also gives monotonicity in the second argument. Axioms 1 and 2 force \(1\Rightarrow y=y\), while the zero row is constant \(0\Rightarrow y=t\) for a uniquely chosen \(t\in M_k\).

For each atom \(a_i\), set \(u_i=a_i\Rightarrow0\) and \(v_i=a_i\Rightarrow a_i\). The entire atom row is determined by these two values: it equals \(v_i\) when the consequent is \(a_i\) or \(1\), and \(u_i\) otherwise. Monotonicity and axiom 2 say \(u_i\le v_i\) and \(a_i\le v_i\). Thus \(v_i\in\{a_i,1\}\). Apply axiom 5 with the inner antecedent equal to \(a_i\): its only potentially nontrivial instance is
\[
a_i\Rightarrow(a_i\wedge u_i)\le u_i.
\]
It follows that the **entire list** of permissible atom-row pairs, before considering \(t\), is
\[
(u_i,v_i)\in\{(0,a_i),(a_i,a_i),(0,1),(1,1)\}\cup\{(a_j,1):j\ne i\}.
\]
This list has \(k+3\) elements.

In axiom 5 with outer antecedent \(a_i\), the inner antecedent \(a_i\wedge y\) can only be \(0\) or \(a_i\). The latter is already handled by the displayed pair restriction. The former contributes exactly
\[
a_i\Rightarrow(a_i\wedge t)\le t.
\]
When the outer antecedent is \(0\) or \(1\), axiom 5 is automatic. Hence these conditions, separately for each atom, are both necessary and sufficient for all five axioms. This also proves that every allowed tuple gives one operation and that distinct tuples give distinct operations.

Now classify the bottom-row value. If \(t=0\), every \(u_i=0\), leaving two choices per atom and \(2^k\) operations. If \(t=a_s\), the distinguished \(a_s\)-row has \(v_s=a_s\) and two choices for \(u_s\); each other atom row has three choices: \((0,a_i)\), \((0,1)\), or \((a_s,1)\). Thus there are \(2\cdot3^{k-1}\) operations for each of the \(k\) choices of \(s\). If \(t=1\), all \(k+3\) choices are available independently at every atom. Summation gives \(N_k\).

Holliday's precomplementation construction assigns \(x\Rightarrow y=\nu(x)\vee(x\wedge y)\). It is injective because \(\nu(x)=x\Rightarrow0\). For an antitone \(\nu\) with \(\nu(1)=0\), choose \(\nu(0)=t\) and choose each \(\nu(a_i)\le t\) independently; no other order comparison imposes a condition. For \(t=0\), there is one choice; for any atomic \(t\), there are \(2^k\); and for \(t=1\), there are \((k+2)^k\). This establishes \(I_k\).

Finally, \(N_k/(k+3)^k\to1\) and \(I_k/(k+2)^k\to1\), since the other summands are exponentially smaller than these powers. Hence their ratio tends to \(((k+2)/(k+3))^k\to e^{-1}\).

## Verification

The standalone Python 3 program `verify_rank_two_preconditionals.py` constructs every operation satisfying the first four axioms via exhaustive atom-row candidates, then independently evaluates all five original quantified axioms on every candidate. It additionally tests the precomplementation-induced representation for each accepted table. Running it gives exact labeled totals \((N_2,I_2)=(41,25)\), \((N_3,I_3)=(278,150)\), and \((N_4,I_4)=(2633,1361)\), including a complete count stratified by \(t\). These finite tests are independent consistency checks; the preceding proof establishes the formulas for every integer \(k\ge2\).

## Relationship to prior work

Holliday established the five axioms and the general construction of a preconditional from a precomplementation, together with a general relational representation (arXiv:2402.02296). Chen identified all bounded lattices with these operations as the algebraic models of \(\mathsf K\), within a broader study of \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\) (arXiv:2607.20221, publicly released July 22, 2026). Their results provide the axiomatic and semantic framework; they do not provide the explicit rank-two normal form, its all-\(k\) census, or the asymptotic proportion obtained here. Previously recorded computations on the four-element Boolean lattice already give the \(k=2\) special case; the new assertions concern the all-\(k\) normal form and enumeration, including the nondistributive family \(k\ge3\).

## Limitations

The theorem counts labeled operations on the specified lattice, not their automorphism orbits. It does not classify the stronger \(\mathsf T\) and \(\mathsf F\) subclasses or arbitrary bounded lattices. The proof is self-contained once the five axioms and the known precomplementation construction are supplied; computational verification ends at \(k=4\). Absence of an equivalent publication in the searches performed is not a proof of absolute novelty, and independent audit has not been performed.

## References

- Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221v1 (first public July 22, 2026), especially Sections 3.1–3.2, https://arxiv.org/abs/2607.20221.
- Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, especially Definition 1 and Proposition 4, https://arxiv.org/abs/2402.02296.
- Wesley H. Holliday, *A Fundamental Non-Classical Logic*, *Logics* 1 (2023), Section 6, https://www.mdpi.com/2813-0405/1/1/4.
