# Divisor–tail skyline census of deterministic modal term operations

## Finding

Let \(W\) be a nonempty finite set, \(f:W\to W\) a total function, and let \(\mathcal A_f=(\mathcal P(W),\cap,\cup,{}^{\complement},\varnothing,W,\Diamond)\), where \(\Diamond U=f^{-1}(U)\). For every integer \(r\ge0\), put \(q=2^r\). For a vertex \(w\), write \(h(w)\) for its distance along \(f\) to its first cycle vertex and \(\ell(w)\) for the length of that cycle. Define the **divisor–tail skyline**
\[
D_f=\{d\ge1:\ d\mid\ell(w)\text{ for some }w\in W\},\qquad H_f(d)=\max_{w:\ d\mid\ell(w)}h(w).
\]
For \(d\ge1\), let \(P_q(d)=\sum_{e\mid d}\mu(e)q^{d/e}\), with \(\mu\) the arithmetic Möbius function. The exact number of distinct \(r\)-ary term operations of \(\mathcal A_f\) is
\[
\boxed{\bigl|\operatorname{Clo}_r(\mathcal A_f)\bigr|=2^{E_f(2^r)},\qquad E_f(q)=\sum_{d\in D_f}q^{H_f(d)}P_q(d).}
\]
This includes nullary operations: \(\bigl|\operatorname{Clo}_0(\mathcal A_f)\bigr|=2\). The polynomial \(E_f(q)\) has degree \(L_f=\max_{w\in W}(h(w)+\ell(w))\); its leading coefficient is the number of **distinct** cycle lengths \(\ell\) satisfying \(H_f(\ell)+\ell=L_f\). In particular, the entire arity-by-arity term-operation census depends on the functional graph only through its divisor–tail skyline, and it ignores multiplicity of indistinguishable branches and cycle components.

## Assumptions and scope

An \(r\)-ary term operation is a map \(\mathcal P(W)^r\to\mathcal P(W)\) induced by a term in \(r\) formal input variables, Boolean operations, the constants \(\varnothing,W\), and arbitrary finite nesting of the unary modality \(\Diamond\). Distinct means distinct as operations on **all input valuations**, not distinct strings of symbols or distinct generated subsets for one fixed valuation. The accessibility relation is the functional one \(wRv\iff v=f(w)\): each world has **exactly one** successor. No surjectivity, connectedness, or injectivity assumption is made. \(W\ne\varnothing\), and \(r\ge0\).

## Proof

**1. Normal form and the universal trace set.** Since \(\Diamond=f^{-1}\) preserves \(\cap\), \(\cup\), complement, and Boolean constants, induction on a term pushes each application of \(\Diamond\) through all Boolean connectives. Hence every term is equivalent on \(\mathcal A_f\) to a Boolean combination of finitely many atoms \(\Diamond^t x_i\), where \(1\le i\le r\) and \(t\ge0\). Interpret any valuation of the \(r\) variables as a coloring \(c:W\to\{0,1\}^r\). The evaluation of \(\Diamond^t x_i\) at \(w\) is precisely the \(i\)-th bit of \(c(f^t(w))\). Therefore the output of every term at \(w\) depends solely on the rooted forward color trace
\[
\tau(c,w)=(c(w),c(f(w)),c(f^2(w)),\ldots).
\]
Let \(T_f(q)\) denote the **set of distinct infinite rooted traces** obtained over every coloring \(c:W\to[q]\) and every vertex \(w\). It is finite, because the number of colored pointed finite graphs is finite. Every term induces a Boolean truth function on \(T_f(q)\). Conversely, any two distinct infinite traces in this finite set differ at some time coordinate and some propositional bit. One finite horizon \(M\) therefore distinguishes every pair, and for every trace \(\tau\) the conjunction of literals on all coordinates \((i,t)\), \(t\le M\), matching \(\tau\) holds exactly on that trace. Disjoining these conjunctions defines **any prescribed** subset of \(T_f(q)\). Thus all \(2^{|T_f(q)|}\) Boolean trace predicates, and no others, are term-definable. Distinct prescribed trace predicates induce distinct term operations because each trace is realizable by definition. Consequently
\[
\bigl|\operatorname{Clo}_r(\mathcal A_f)\bigr|=2^{|T_f(q)|}.
\]

**2. Realizability of ultimately periodic traces.** For an infinite word \(\tau\) on \([q]\), its *minimal eventual period* is the least \(d\ge1\) such that \(\tau_{t+d}=\tau_t\) at all sufficiently large \(t\). Its *exact preperiod* is the least \(b\ge0\) for which those equalities hold at all \(t\ge b\). A trace based at \(w\) is realizable precisely when its minimal period \(d\) divides \(\ell(w)\) and its exact preperiod \(b\) is at most \(h(w)\). Necessity is immediate because the orbit of \(w\) enters a cycle of length \(\ell(w)\) after \(h(w)\) steps. Sufficiency follows by reading the prescribed first \(h(w)+\ell(w)\) letters around the path and cycle, assigning the corresponding vertex colors, and assigning arbitrary colors elsewhere. The period condition ensures consistency on the cycle. Hence the possible pairs \((b,d)\) are exactly \(d\in D_f\), \(0\le b\le H_f(d)\).

**3. Exact enumeration.** The number of primitive cyclic words of length \(d\) on an alphabet of size \(q\), with a distinguished starting position, is \(P_q(d)=\sum_{e\mid d}\mu(e)q^{d/e}\), by Möbius inversion from the \(q^d\) words of period dividing \(d\). For exact preperiod \(b=0\), there are \(P_q(d)\) rooted infinite periodic words of least period \(d\). For \(b\ge1\), choose the periodic tail in \(P_q(d)\) ways, choose its preceding letter *different* from the corresponding periodic predecessor in \(q-1\) ways, and choose the previous \(b-1\) letters freely in \(q^{b-1}\) ways. This gives exactly \((q-1)q^{b-1}P_q(d)\) words, because the indicated inequality characterizes minimality of \(b\). Summing over \(b\le H_f(d)\) yields
\[
P_q(d)\left(1+\sum_{b=1}^{H_f(d)}(q-1)q^{b-1}\right)=P_q(d)q^{H_f(d)}.
\]
Words with different exact pairs \((b,d)\) are disjoint, so \( |T_f(q)|=\sum_{d\in D_f}P_q(d)q^{H_f(d)}=E_f(q)\), proving the boxed formula.

**4. Degree and leading coefficient.** The polynomial \(P_q(d)\) is monic of degree \(d\), and all lower powers in it have degree less than \(d\), including \(d=1\). For every \(d\in D_f\), a witness \(w\) for the maximum \(H_f(d)\) satisfies \(H_f(d)+d\le h(w)+\ell(w)\le L_f\). Conversely, choosing \(w\) attaining \(L_f\) and \(d=\ell(w)\) gives \(H_f(d)+d\ge L_f\). Hence \(\deg E_f=L_f\). Each skyline term reaching that degree contributes coefficient one. If \(d\) is a proper divisor of \(\ell(w)\) for an optimizing witness, then \(H_f(d)+d<h(w)+\ell(w)\le L_f\); thus equality can occur only for \(d\) that is an actual cycle length. These are precisely the distinct lengths \(\ell\) with \(H_f(\ell)+\ell=L_f\). Their contributions cannot cancel because they have positive leading coefficients.

**5. Boundary cases and illustrations.** When \(r=0\), \(q=1\), only \(P_1(1)=1\) is nonzero, so \(E_f(1)=1\), yielding the two constant operations. A single fixed point has \(E_f(q)=q\); an incoming chain of height \(h\) ending at a fixed point has \(E_f(q)=q^{h+1}\). A directed \(n\)-cycle has \(E_f(q)=\sum_{d\mid n}P_q(d)=q^n\). Disjoint cycles of lengths two and three have \(E_f(q)=q^2+q^3-q\); at \(r=1\) their Boolean-algebra term clone has \(2^{10}=1024\) unary term operations. Cycle multiplicities have no effect, but adjoining a cycle of a new primitive period can change the count.

## Verification

The enclosed standalone `verify.py` implements the skyline polynomial, an independent direct enumeration of all rooted color traces for all functions on up to four vertices at alphabet sizes one, two and three, modal partition refinement on those entire colored-model ensembles, and explicit enumeration of the Boolean algebra generated by modal shifts of input predicates on the smallest cases. A fixed-seed collection of larger random endofunctions checks combinatorial invariants, not completeness. The program uses only Python's standard library. Run `python3 verify.py`; the expected first line is `VERIFY_OK exhaustive_maps_x_alphabets=864 independent_refinement_checks=864 direct_term_closures=15 randomized_invariants=1000`. The finite tests are checks only, not the proof for arbitrary \(W\).

## Relationship to prior work

Wißmann, Milius and Schröder (first preprint 2021; expanded journal version 2022) construct modal formulas distinguishing inequivalent finite-coalgebra states; this supports the classical behavioral-signature perspective, but is not a census of all \(r\)-ary term operations on one deterministic Boolean modal algebra. Ten Cate and Koudijs (2023 preprint, version 2024) establish general characterizability criteria and local-tabularity connections for classes of modal frames; their object is not the exact number of term operations for a fixed finite endofunction. Castillo-Ramirez, Mata-Gutiérrez and Zaldivar-Corichi (2019 preprint, revised 2021) count structure-preserving cellular automata with prescribed memory sets over **group** shifts, whereas the present operators are arbitrary Boolean combinations of a possibly noninjective **single-map** preimage and the quantity is a term-operation clone cardinality. Primitive-word Möbius inversion and Boolean normal forms are classical tools and are not claimed as discoveries. Earlier results on the generation of the **underlying algebra by particular valuations** concern a different invariant: a set of chosen generators and whether it separates the worlds, not a census of all operations of a fixed arity across all valuations.

## Limitations

The theorem requires a total deterministic transition map and full Boolean operations. It is not a count for nondeterministic relational modalities or for fragments lacking complement. The formula determines arity-wise operation counts, not a classification of clone isomorphisms between different underlying sets. The literature comparison does not rule out implicit coverage in older universal-algebra, unary-dynamical-system, or symbolic-dynamics terminology; independent scrutiny remains necessary.

## References

1. T. Wißmann, S. Milius, L. Schröder, *Explaining Behavioural Inequivalence Generically in Quasilinear Time*, arXiv:2105.00669 (first public 2021-05-03), DOI:10.4230/LIPIcs.CONCUR.2021.32; expanded version *Quasilinear-time Computation of Generic Modal Witnesses for Behavioural Inequivalence*, Logical Methods in Computer Science 18(4), 6 (2022), arXiv:2203.11175, DOI:10.46298/LMCS-18(4:6)2022.
2. B. ten Cate, R. Koudijs, *Characterising Modal Formulas with Examples*, arXiv:2304.06646 (first public 2023-04-13).
3. A. Castillo-Ramirez, O. Mata-Gutiérrez, A. Zaldivar-Corichi, *Cellular automata over algebraic structures*, arXiv:1908.09675 (first public 2019-08-26).
4. Classical Möbius inversion / primitive-word enumeration (standard enumerative combinatorics; no attribution of a new identity).
