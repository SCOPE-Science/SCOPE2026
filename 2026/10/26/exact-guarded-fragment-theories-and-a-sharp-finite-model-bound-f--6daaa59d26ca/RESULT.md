# Exact guarded-fragment theories and a sharp finite-model bound for unary-coloured equivalence relations

## Finding

Fix an integer \(k\geq0\). Work in the constant-free first-order signature consisting of equality, one binary predicate \(E\), and exactly \(k\) freely interpreted unary predicates. All structures are nonempty and \(E\) is interpreted as an equivalence relation. Formulas belong to the ordinary guarded fragment (GF), with atomic guards and no additional relation symbols or counting quantifiers.

Let \(c=2^k\) be the number of unary colours (complete truth assignments to the \(k\) predicates). For each \(E\)-class \(C\), set
\[
 v(C)=\bigl(\min\{2,|C\cap U_t|\}\bigr)_{t=1}^{c}\in\{0,1,2\}^{c}\setminus\{\mathbf0\},
\]
where \(U_t\) denotes the set of elements of colour \(t\). The value \(2\) means **at least two**, not exactly two. Define the *class-profile spectrum* \(S(M)=\{v(C):C\in M/E\}\), forgetting how many classes realize a given profile.

**Theorem.** For any two nonempty (possibly infinite) such structures \(M,N\), the following are equivalent:

1. \(M\) and \(N\) satisfy exactly the same GF sentences;
2. \(S(M)=S(N)\).

Every GF sentence is effectively equivalent, over this restricted class, to a GF sentence of quantifier rank at most \(3\). Moreover, every satisfiable GF sentence has a finite model of cardinality at most
\[
 \boxed{B_k=c3^{c}=2^k3^{2^k}},
\]
and this is the **smallest possible uniform bound** (independent of formula length) for the fixed \(k\)-predicate signature. There are exactly
\[
 \boxed{2^{3^c-1}-1}
\]
distinct GF sentence-equivalence classes of nonempty structures in this signature. For one unary predicate, these numbers are respectively \(B_1=18\) and \(255\); without unary predicates, they are \(B_0=3\) and \(3\).

## Assumptions and scope

The guarded-fragment syntax is the closure of atomic formulas under Boolean connectives and quantification of the form \(\exists\bar y\,(\gamma(\bar x,\bar y)\wedge\psi(\bar x,\bar y))\) or \(\forall\bar y\,(\gamma(\bar x,\bar y)\to\psi(\bar x,\bar y))\), where the guard \(\gamma\) is a **single atom** containing all free variables of the quantified matrix; single-variable unguarded quantification is also permitted (equivalently guarded by equality). The only binary atoms are \(E(x,y)\) and equality. Neither nested-equivalence symbols beyond \(E\) nor freely interpreted binary guards are allowed. Domain nonemptiness is part of the class definition. No restriction is imposed on the size or number of equivalence classes, and colours need not all occur.

A *GF sentence-equivalence class* means an equivalence class of models under agreement on every GF sentence, **not** under full first-order elementary equivalence. The sharpness of \(B_k\) quantifies over all satisfiable GF sentences in this fixed signature, with no restriction on sentence length.

## Proof

**1. Construct the canonical structure.** Let \(S\) be any nonempty subset of \(\{0,1,2\}^{c}\setminus\{\mathbf0\}\). Form a finite structure \(K(S)\) with exactly one equivalence class \(C_v\) for each \(v\in S\). Give \(C_v\) exactly \(v_t\) elements of colour \(t\). Then \(S(K(S))=S\), and
\[
 |K(S)|=\sum_{v\in S}\sum_{t=1}^{c}v_t\leq\sum_{v\in\{0,1,2\}^{c}}\sum_t v_t
 =c(0+1+2)3^{c-1}=c3^c.
\]

**2. Prove GF invariance using guarded partial maps.** If \(S(M)=S(N)\), consider all colour-preserving partial bijections between (i) singleton guarded sets and (ii) pairs of distinct, \(E\)-related elements, subject to the requirement that the source and target elements lie in classes of the *same profile*. Include the empty partial map. These maps are partial isomorphisms: in this signature their atomic data consist only of equality, colours, and whether the two vertices are \(E\)-related (which they are within a guarded pair).

They constitute a guarded back-and-forth system. Given such a map and a new guarded tuple in \(M\), if the tuple meets the previous domain, it lies in the same \(E\)-class. Retain images of shared vertices and choose the remaining images of the required colours in the corresponding class of \(N\). At most two distinct vertices occur in the new guarded tuple. Availability of each colour once or twice is recorded **exactly** by the truncated profile. If the new tuple is disjoint from the old domain, take any class of the required profile in \(N\), which exists because the spectra agree. The converse move is symmetric. The back-and-forth condition refers to the currently shared variables, not to elements released at an earlier move. Thus the standard guarded-bisimulation invariance theorem gives \(M\models\varphi\iff N\models\varphi\) for every GF sentence \(\varphi\). This applies also to infinite \(M,N\).

**3. Show profiles are GF-definable.** For each colour \(t\), let \(\chi_t(y)\) be its quantifier-free conjunction of positive and negative unary literals. Using only \(E\)-guards, the following formulas with free variable \(x\) test the three possible entries of a class profile:
\[
 Z_t(x):=\forall y\,(E(x,y)\to\neg\chi_t(y)),
\]
\[
 O_t(x):=\exists y\,\bigl(E(x,y)\wedge\chi_t(y)\wedge
       \forall z\,(E(y,z)\to(\chi_t(z)\to z=y))\bigr),
\]
\[
 T_t(x):=\exists y\,\bigl(E(x,y)\wedge\chi_t(y)\wedge
       \exists z\,(E(y,z)\wedge\chi_t(z)\wedge z\ne y)\bigr).
\]
Their quantifier ranks are at most \(2\); note in the inner \(z\)-quantifier the outer variable \(x\) is **not free in the matrix**, so the binary guard \(E(y,z)\) is legitimate. Let \(\Theta_v(x)\) be the conjunction of \(Z_t,O_t,T_t\) according as \(v_t=0,1,2\). Then
\[
 M\models\exists x\,\Theta_v(x)\quad\Longleftrightarrow\quad v\in S(M).
\]
The existence sentence has rank at most \(3\). It separates any two different spectra, proving the converse of step 2.

**4. Collapse, exact number, and sharpness.** For any spectrum \(S\) let \(\Xi_S\) assert the existence of every profile in \(S\) and the nonexistence of every other nonzero profile. Explicitly, it is the conjunction of the corresponding positive/negative \(\exists x\,\Theta_v(x)\) statements, all of quantifier rank at most \(3\). Every nonempty \(S\) is realized by \(K(S)\), so there are exactly \(2^{3^c-1}-1\) different GF theories. For an arbitrary GF sentence \(\varphi\), disjoin the finitely many \(\Xi_S\) for which \(K(S)\models\varphi\). Step 2 proves equivalence and the rank-three collapse; the construction is effective for each fixed \(k\).

Finally, take \(S_*\) to be the set of **all** nonzero profiles and take the rank-three GF sentence \(\Xi_{S_*}\) (equivalently, the conjunction of all profile-existence sentences). Each profile must occur in a different \(E\)-class, requiring at least \(\sum_t v_t\) elements for that class. Hence every model has size at least \(\sum_{v\in S_*}\sum_t v_t=c3^c\). The canonical \(K(S_*)\) attains equality. Therefore no smaller uniform model-size bound can hold.

## Verification

The standalone script `verify_guarded_equiv.py` uses only the Python standard library. Run `python verify_guarded_equiv.py` to reproduce the finite checks. It enumerates all partitions and unary two-colourings of domains of sizes \(1\) through \(5\) (\(1954\) structures), constructs canonical representatives, compares the profile formulas to independently evaluated \(E\)-guarded witnesses, and verifies the guarded back-and-forth relation explicitly on \(418\) selected structures. Separately, for \(c=1,2,4\), it builds the all-profile witness, checks sizes \(3,18,324\), and checks that deleting any one element destroys at least one required profile. Its concluding signals are `SHARP_PROFILE_BOUND_OK` and `CANONICAL_GUARDED_EQUIVALENCE_OK`. Finite checks are supporting evidence only; the result for arbitrary structures is proved in the preceding paragraphs.

## Relationship to prior work

Guarded bisimulation and its preservation of GF are classical; they are **used**, not claimed as new. Bárány, Gottlob, and Otto, *Querying the Guarded Fragment* (2014), develop general small-model constructions and guarded-bisimulation canonisation. Fiuk, *Random Models and Guarded Logic* (2026), obtains sharp general asymptotic small-model bounds by different methods. Fiuk, *The Guarded Fragment with Nested Equivalences* (first public version 14 May 2026), studies a much broader vocabulary and proves that allowing equality plus unrestricted auxiliary relation symbols can yield undecidability even with one designated equivalence relation. The present sharply restricted signature allows an explicit complete profile invariant, a formula-independent optimal finite-model bound, and an exact census of GF theories. The 2026 papers do not state these specialized numerical claims in the inspected text. The exact enumeration is not a consequence of the general bounds alone without the class-profile analysis.

## Limitations

The theorem fails to cover signatures with any additional binary (or higher-arity) predicates, additional distinguished equivalence relations, constants, counting quantifiers, or the full two-variable first-order fragment; it also does not assert full first-order equivalence of structures. Formula sizes for the saturation witness and rank-three translation can grow enormously with \(k\). This is a complete mathematical proof but not an independent audit of historical priority; the broad guarded-bisimulation literature creates a residual risk that an earlier special-case formulation already gives the same exact invariant or bound.

## References

1. Oskar Fiuk, *The Guarded Fragment with Nested Equivalences*, arXiv:2605.15072, first submitted 2026-05-14, https://arxiv.org/abs/2605.15072 (Sections 1 and 6, plus signature discussion and proof of the equality obstruction).
2. Oskar Fiuk, *Random Models and Guarded Logic*, arXiv:2601.05247, first submitted 2026-01-08, https://arxiv.org/html/2601.05247 (full paper, introduction, Theorems 1.1--1.2, and model construction discussion).
3. Vince Bárány, Georg Gottlob, Martin Otto, *Querying the Guarded Fragment*, Logical Methods in Computer Science 10(2:3), 2014, https://arxiv.org/pdf/1309.5822 (Section 2 on guarded bisimulation and Section 6 on general canonisation).
4. Andréka, van Benthem, and Németi (1998), foundational introduction of guarded fragments, as discussed and cited in References 1--3.
