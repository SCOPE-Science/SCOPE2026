# Exactly 35 unary modality classes in crisp Gödel \(\mathsf{GS4^c}\)

## Finding

In the crisp Gödel–Dummett intuitionistic modal logic \(\mathsf{GS4^c}\), **exactly 35** equivalence classes of finite strings over the three unary operations intuitionistic negation \(N=\neg\), necessity \(B=\Box\), and possibility \(D=\Diamond\) occur, including the empty string. Equivalence means equality of the induced unary formula operators on every formula in every \(\mathsf{GS4^c}\) birelational model. This makes exact the previously published upper bound of 105.

All 35 representatives, in indexed order (the empty word is `ε`), are:

`ε`, `N`, `B`, `D`, `NN`, `BN`, `DN`, `NB`, `DB`, `BD`, `BNN`, `DNN`, `DBN`, `BDN`, `NNB`, `BNB`, `BDB`, `NBD`, `DBD`, `DBNN`, `BDNN`, `BDBN`, `DBDN`, `DNNB`, `DBNB`, `NBDB`, `NNBD`, `BNBD`, `BDBNN`, `DBDNN`, `BDNNB`, `NNBDB`, `DNNBD`, `DBNBD`, `BDNNBD`

## Assumptions and scope

World sets may be arbitrary and can include fallible worlds. The intuitionistic accessibility \(\preceq\) and modal accessibility \(R\) are preorders; \(\preceq\) is locally linear, and backward, forward, and downward confluence hold as in Pacheco's Definition 4 and Definition 5. Every variable valuation is a \(\preceq\)-upset containing the fallible worlds; the fallible-world set is a \(\preceq\)-upset and an \(R\)-upset. Box, diamond, and intuitionistic negation use the birelational semantics in the cited source. Strings are read from left to right as outermost-to-innermost operators; juxtaposition is composition, e.g., \(BN\varphi=\Box\neg\varphi\). The claim concerns all formulas, not merely variable valuations or finite frames.

## Proof

**1. Universally sound equations.** With \(N,B,D\) standing for the indicated unary operators, the following eight equations hold uniformly for all formulas and all \(\mathsf{GS4^c}\) models:

\[
BB=B,\quad DD=D,\quad NNN=N,\quad BDBD=BD,\quad DBDB=DB,
\]
\[
BN=ND,\qquad DNN=NBN,\qquad DNB=NB.
\]

The first five are Pacheco's Lemma 5 (the intuitionistic triple-negation law and the S4 closure/interior reductions); the sixth is his Lemma 10(1). For the seventh, the truth set of \(N\varphi\) is a \(\preceq\)-updownset by Pacheco's Lemma 15, and Lemma 17 gives \(DNN\varphi=NBN\varphi\).

For the eighth, fix \(\varphi\), and write \(x\) for its truth set. On truth sets use inclusion as the order. Because \(Bx\subseteq NNBx\), monotonicity and idempotence of \(B\), followed by \(BN=ND\), imply
\[
 Bx=BBx\subseteq BNNBx=NDNBx.
\]
Applying antitone \(N\) gives \(NNDNBx\subseteq NBx\). By Lemma 15 the set \(NBx\) is a \(\preceq\)-updownset; by Lemma 16 so is \(DNBx\); by Lemma 17 double negation fixes any such set. Hence \(DNBx\subseteq NBx\). The converse \(NBx\subseteq DNBx\) follows from reflexivity of \(R\). Therefore \(DNB=NB\). All eight equations remain sound in arbitrary models, including fallible-world models.

**2. Finite reduction to 35 representatives.** Put the 35 strings above in an indexed array. The finite congruence computation in `artifacts/verify.py` lists every string of length at most nine (29,524 strings including the empty word), connects strings related by replacing an occurrence of any one of the eight sound equations in either direction while staying in that finite universe, and computes connected components. For each of the 105 words formed by prepending one of \(N,B,D\) to a representative, the program proves that it lies in the same contextual-equation component as one of the indexed representatives. The exact 105 transitions, by generator, appear in `artifacts/closure_table.csv`. This is a finite derivation certificate: every union step is a context instance of a universally sound equality; the printed table covers all generators acting on all representatives. Induction on word length shows **every** word is semantically equivalent to one of the 35 representatives. The finite enumeration is a rigorously bounded *syntactic congruence calculation*, not an extrapolation from sampled Kripke models.

**3. Separating all 35 representatives.** Five birelational models, each with at most four worlds and with no fallible worlds, suffice to distinguish them all. World indices start at zero, and a relation row or truth set is encoded as a bitmask (bit \(i\) denotes world \(i\)). The tuple `(n,P,R,a)` specifies number of worlds, rows of \(\preceq\), rows of \(R\), and the truth set of one variable \(p\):

| Model | `n` | `P` row masks | `R` row masks | `a` mask |
| --- | ---: | --- | --- | ---: |
| 1 | 4 | `(3,2,4,8)` | `(1,3,15,8)` | 10 |
| 2 | 4 | `(3,2,4,8)` | `(1,2,12,12)` | 6 |
| 3 | 4 | `(1,2,4,8)` | `(13,6,4,8)` | 4 |
| 4 | 3 | `(3,2,4)` | `(1,2,7)` | 2 |
| 5 | 2 | `(1,2)` | `(3,2)` | 1 |

The checker verifies, for each tuple, reflexivity/transitivity of both relations, local linearity, backward/forward/downward confluence, and persistence of \(p\). By confluence, modal operations on upward-closed sets simplify to \(B(X)=\{w:R[w]\subseteq X\}\) and \(D(X)=\{w:R[w]\cap X\ne\varnothing\}\); intuitionistic negation is \(N(X)=\{w:\preceq[w]\cap X=\varnothing\}\). The checker evaluates all 35 representative words in every displayed model. Their five-coordinate output vectors are pairwise distinct, proving **at least** 35 inequivalent classes. Together with Step 2 this gives exactly 35.

## Verification

Execute `python3 artifacts/verify.py` in the directory containing the embedded file; it uses only Python's standard library. The program independently constructs all 29,524 words for the bounded congruence closure, checks all 105 generator reductions and the distinctness of the 35 representatives in five fully specified finite models. Successful output ends with `GS4C_35_VERIFY_OK`. The closure table is also embedded as `artifacts/closure_table.csv`. This verifies a *finite proof certificate* whose soundness is established in Step 1; no finite-model test alone is used to infer the all-model upper bound.

## Relationship to prior work

Pacheco's 2026 Theorem 18 proves finiteness and gives the numerical upper bound 105, but not the exact number; Lemmas 5, 10 and 15–17 are used and explicitly credited above. This result refines the 105 bound to a sharp 35, adding the equation \(DNB=NB\), a complete reduction certificate, and small separating models. Classical Kuratowski's 14-operator theorem and Ciraulo's 2025 constructive-topology treatment concern related but differently interpreted operators; neither identified source supplies this sharp \(\mathsf{GS4^c}\) calculation.

## Limitations

The theorem concerns the unary word monoid in \(\mathsf{GS4^c}\) only, not arbitrary multimodal formulas, the strictly weaker \(\mathsf{GS4}\), nor a classification of the equational theory with several variables. Its novelty is evaluated relative to the source and literature inspected; an older equivalent algebraic presentation could remain undiscovered. The five finite models establish separation, but no claim of minimality for the number of models or their sizes is made. Independent external validation is not yet performed.

## References

1. Leonardo Pacheco, *Modalities in non-classical variations of S4*, arXiv:2609.00736, first public 2026-09-01, https://arxiv.org/abs/2609.00736 (particularly Definitions 3–5, Lemmas 5, 10, 15–17 and Theorem 18).
2. Francesco Ciraulo, *Kuratowski's problem in constructive Topology*, *Journal of Logic and Analysis* 17:FDS1 (2025), https://doi.org/10.4115/jla.2025.17.FDS1.
