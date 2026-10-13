# Exactly 35 unary modal words on nonfallible Gödel–S4 frames

## Finding

For the specified class of **nonfallible** birelational Gödel–S4 frames, the number of equivalence classes of unary words in \(\neg\), \(\Box\), and \(\Diamond\), including the identity, is exactly \(35\). This is a classification of operators on arbitrary upward-closed propositions, not just on a selected valuation or a fixed finite frame.

Put `B=box`, `D=diamond`, and `N=intuitionistic negation`, reading strings from outermost to innermost, with `ε` denoting the empty word. The following \(35\) words form a complete set of inequivalent representatives:

`ε, B, D, N, BD, BN, DB, DN, NB, NN, BDB, BDN, BNB, DBD, DBN, NBD, NBN, NDN, NNB, BDBN, BNBD, DBDN, DBNB, NBDB, NBDN, NBNB, NDBN, NNBD, DBNBD, NBDBN, NBNBD, NDBDN, NDBNB, NNBDB, NDBNBD`

## Assumptions and scope

A frame is \((W,\preceq,R)\) with nonempty \(W\); both \(\preceq\) and \(R\) are reflexive and transitive. For every \(w\), the upper cone \(\{v:w\preceq v\}\) is linearly ordered by \(\preceq\). We assume the following interactions for arbitrary worlds:

- Forward: \(wRu\) and \(w\preceq v\) imply some \(u'\succeq u\) with \(vRu'\).
- Backward: \(wRu\) and \(u\preceq t\) imply some \(v\succeq w\) with \(vRt\).
- Downward: \(w\preceq v\) and \(vRt\) imply some \(u\) with \(wRu\) and \(u\preceq t\).

An admissible propositional truth set \(X\subseteq W\) is upward closed. **Nonfallible** means the bottom formula is false at every world; hence intuitionistic negation is \(N(X)=\{w:\forall v\succeq w, v\notin X\}\). Define the other operations by the birelational modal clauses:

\[B(X)=\{w:\forall v\succeq w\;\forall u\,(vRu\Rightarrow u\in X)\},\]
\[D(X)=\{w:\forall v\succeq w\;\exists u\,(vRu\land u\in X)\}.\]

Confluence makes these equal to the simpler direct-successor clauses \(B(X)(w)\iff\forall u(wRu\Rightarrow u\in X)\) and \(D(X)(w)\iff\exists u(wRu\land u\in X)\). The empty word acts as the identity. This result is **not** an exact count for models admitting fallible (bottom-forcing) worlds, which are excluded.

## Proof

**Step 1: semantic operator identities.** Reflexivity and transitivity make \(B\) an interior operator and \(D\) a closure operator on the lattice of upward-closed subsets, so \(BB=B\), \(DD=D\), \(BDBD=BD\), and \(DBDB=DB\). The last two hold for any interior–closure pair: if \(I\leq\operatorname{id}\leq C\), then \(ICIC=IC\) and \(CICI=CI\). Standard intuitionistic negation satisfies \(NNN=N\).

The two additional identities are \(BN=ND\) and \(DNB=NB\). For the first, \(BNX(w)\) means no successor \(u\) of \(w\) has an upper extension in \(X\). If \(NDX(w)\) failed, there would be \(v\succeq w\) and \(vRt\) with \(t\in X\); downward confluence would give \(wRu\) with \(u\preceq t\), a contradiction. Conversely, failure of \(BNX(w)\) gives \(wRu\preceq t\in X\), and backward confluence gives \(v\succeq w\) with \(vRt\), contradicting \(NDX(w)\). For \(DNB=NB\), reflexivity yields \(NBX\subseteq DNBX\). Conversely, if \(wRu\) and \(NBX(u)\), then \(BX(v)\) for some \(v\succeq w\) would, by forward confluence, yield \(u'\succeq u\) and \(vRu'\). Transitivity of \(R\) would give \(BX(u')\), contradicting \(NBX(u)\). Thus \(DNBX\subseteq NBX\).

**Step 2: universal upper bound.** Pacheco's finite-modalities reduction for \(\mathsf{GS4^c}\) supplies \(105\) representatives: the seven negation-free words `ε,B,D,BD,DB,BDB,DBD`, together with all `aNb` where `a` is one of the fourteen classical S4 modalities `q` or `Nq` for these seven `q`, and `b` is one of the seven. The model class here is a subfamily of the source's frame class, so this bound applies. Generate the finite set of all words of length at most \(10\) and connect two words whenever one results from replacing a subword by one side of any of the seven proved identities. Every edge is sound in **any** context. An exhaustive, replayable union–find computation in `verify.py` groups the \(105\) published candidate words into exactly \(35\) components and finds the stated \(35\) representatives, one in each component. This supplies an explicit finite chain of valid equalities from every candidate to a representative, proving at most \(35\) classes.

**Step 3: universal lower bound.** Both witness frames have world set \(\{0,1,2,3\}\), intuitionistic order rows `(3,2,4,8)` interpreted as bit masks (world \(0\preceq1\)), and accessibility rows `(1,2,15,8)` and `(1,3,12,12)`, respectively. In row \(i\), bit \(j\) indicates accessibility to \(j\). Direct checks establish the preorder, local linearity and all three confluences. Each frame has exactly \(12\) upward-closed valuations. For each of the \(35\) representatives, the vector of its four-world truth sets under all \(24\) valuations across both frames is calculated by the original, unsimplified semantic clauses. These \(35\) signatures are pairwise distinct. Thus no two representatives can be equivalent over the model class; at least \(35\) classes exist.

Combining the two inequalities proves exactly \(35\).

## Verification

Run `python3 verify.py` using Python 3 and the standard library. Successful replay prints `UPPER_NORMAL_FORMS=35`, `FINITE_WITNESSES=35`, and `VERIFY_OK`. The program builds all length-at-most-ten words, all sound context rewrites, and both finite countermodels, and checks the resulting cardinalities. As a separate stress test, all \(457\) ordered triples of small-world frames satisfying the stated conditions among three-world reflexive-transitive relations were exhaustively checked for the seven operator identities on every upset. The infinite-model theorem depends on the semantic proof above and the published reduction, not on extrapolation from finite examples.

## Relationship to prior work

L. Pacheco's 2026 paper *Modalities in non-classical variations of S4* establishes finiteness of the full \(\mathsf{GS4^c}\) signature and provides an upper reduction to \(105\) candidate modalities, but does not give this exact \(35\)-element classification on the nonfallible subfamily. Classical S4 has fourteen unary modalities by the classical Kuratowski/Parry-style analysis; this does not determine the intuitionistic-negation semigroup. A previously circulated finite-witness result showed at least \(35\) distinct modalities for the **larger** full frame class; that lower bound alone neither gives the needed \(35\) upper bound nor proves separation within the nonfallible class. The present finding provides both missing components for this restricted but natural semantics.

## Limitations

The result classifies unary compositions only; it does not count formulas with binary connectives or multiple variables. It explicitly excludes bottom-forcing worlds and does not settle the exact number for the full fallible model class. The upper reduction relies on the cited source's finite-modalities theorem. The finite certificate is fully replayable but is not an external independent audit. Additional literature under alternative terminology could contain equivalent identities or the same exact count.

## References

1. Leonardo Pacheco, *Modalities in non-classical variations of S4*, arXiv:2609.00736v1 (first public 2026-09-01); especially birelational semantics and finite-normal-form theorem.
2. C. E. Parry, classical unary S4 modality-counting results, as cited in Pacheco's references.
3. Juan P. Aguilera, David Fernández-Duque, Leonardo Pacheco, *Polytopological Semantics for Intuitionistic Modal Logics*, arXiv:2604.23234v1 (2026), background on constructive and Gödel–S4 semantics.
