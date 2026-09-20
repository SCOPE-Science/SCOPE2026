# Review: all-characteristic character rank formula for graphical groups

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Rossmann's Proposition 2.3 is stated over arbitrary commutative rings and identifies
\[
G'=\mathbf F_qE,\qquad G/G'\cong\mathbf F_qV,
\]
with \(G'\) central and the group commutator equal to the graphical Lie bracket. Thus no
odd-characteristic identification is needed for the central-extension step.

For a fixed central character \(\lambda\), the corresponding summand of \(\mathbf CG\) is a twisted
group algebra of the abelian quotient \(A=G/G'\). The proof in `RESULT.md` derives its complete
Wedderburn structure from the radical of the cocycle commutator bicharacter: there are
\(|\operatorname{rad}\beta_\lambda|\) simple modules, all of dimension
\(\sqrt{|A|/|\operatorname{rad}\beta_\lambda|}\).

Using the nondegenerate field-trace pairing, the radical for the central character indexed by
\(y\in\mathbf F_q^E\) is exactly \(\ker B_\Gamma(y)\). Alternating matrices have even rank in every
characteristic. Hence rank \(2i\) gives exactly \(q^{n-2i}\) irreducibles of degree \(q^i\).
The sum-of-squares identity is exact block by block and totals \(|G|\).

The complete-bipartite corollary follows because
\[
B_{K_{a,b}}(y)=\begin{pmatrix}0&M\\-M^T&0\end{pmatrix}
\]
has rank \(2\operatorname{rank}M\) over every field. The complete-graph corollary uses the standard
count of alternating matrices of prescribed rank, valid in characteristic \(2\) as well.

## Originality

**PASS, to the best of our knowledge.** Rossmann's 2022 paper explicitly records the
character-rank reduction only for odd \(q\), via O'Brien--Voll, and asks how
\(\operatorname{ch}(\Gamma,i;q)\) depends on \(q\). It lists complete graphs only under an
odd-\(q\) qualification. O'Brien--Voll's general formula is for finite \(p\)-groups of nilpotency
class less than \(p\), so its stated hypotheses do not cover class-two graphical groups in
characteristic \(2\).

Targeted searches for the graphical-group terminology, the character-enumeration question, even
characteristic, and the complete-bipartite family did not locate a later source giving the theorem
above. Adjacent later work, including Qiao's 2024 paper on totally-isotropic polynomials and abelian
subgroups of graphical groups, addresses a different enumeration problem.

The representation theory of twisted group algebras and central extensions is classical; no
originality is claimed for that method. Busby--Smith (1970) and later treatments establish the
general framework. Because the proof here is a short application of classical projective
representation theory, an equivalent statement under different class-two-group terminology remains
the principal originality risk. No such statement was found in the sources checked.

## Value

**PASS.** The theorem removes a genuine characteristic restriction from the character-degree
description for the entire graphical-group family. It also gives a new explicit polynomial family
for Rossmann's character-enumeration question:
\[
\operatorname{ch}(K_{a,b},r;q)=q^{a+b-2r}N_{a,b,r}(q)
\]
for every prime power \(q\). The complete-graph formula simultaneously extends to even
characteristic.

## Scientific limitations

The theorem reduces the general question to rank counts but does not prove polynomiality in \(q\)
for arbitrary graphs. The complete-bipartite and complete-graph families are explicit because their
rank strata are standard matrix spaces. Originality is qualified by the possibility of an older
equivalent class-two/projective-representation formulation not indexed using graphical-group
terminology.

## Sources checked

- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*,
  Bull. Lond. Math. Soc. 54 (2022), DOI 10.1112/blms.12665.
- E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*,
  Trans. Amer. Math. Soc. 367 (2015), DOI 10.1090/tran/6276.
- R. C. Busby and H. A. Smith, *Representations of Twisted Group Algebras*,
  Trans. Amer. Math. Soc. 149 (1970), DOI 10.1090/S0002-9947-1970-0264418-8.
- Y. Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*,
  arXiv:2408.09963 (2024).
