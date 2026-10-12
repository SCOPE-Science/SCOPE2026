# Strict weak-order modal term spectra recover every noninitial level width

## Finding

Let \(h\ge1\) and let \(W=A_1\sqcup\cdots\sqcup A_h\) be a finite ordinal sum of nonempty antichains, with \(n_i=|A_i|\ge1\). Give \(W\) the irreflexive transitive accessibility relation \(xRy\) exactly when the level of \(x\) is strictly earlier than that of \(y\), and put \(\mathcal A=(\mathcal P(W),\neg,\land,0,1,\Diamond)\), where \(\Diamond X=\{x: (\exists y)\,xRy\land y\in X\}\). For \(m\ge1\), write \(S_m(q)=\sum_{k=1}^{m}\binom{q}{k}\). The exact count of \(r\)-ary term operations of \(\mathcal A\), for every \(r\ge0\) with \(q=2^r\), is \[|\operatorname{Clo}_r(\mathcal A)|=2^{E_{\mathbf n}(q)},\qquad E_{\mathbf n}(q)=q\sum_{i=1}^{h}\prod_{j=i+1}^{h}S_{n_j}(q).\] Two such complex modal algebras have identical term-operation cardinalities at every finite arity if and only if they have the same height and the same ordered widths at all noninitial levels \((n_2,\ldots,n_h)\). The first-level width \(n_1\) is completely invisible to this invariant. All assertions include \(h=1\) and \(r=0\).

Equivalently, the complete arity spectrum of the Boolean modal algebra on a finite *strict* weak order determines the entire ordered level-width vector except for its initial width. The distinction between strict accessibility and reflexive accessibility is essential.

## Assumptions and scope

A finite strict weak order here is an ordinal sum \\(A_1\\oplus\\cdots\\oplus A_h\\) of nonempty finite antichains, \\(h\\ge1\\), in which a world can access every world of each *later* level, no world of its own level, and no world of an earlier level. Thus the accessibility relation is irreflexive and transitive. Each \\(n_i=|A_i|\\) is a positive integer. The algebra has all Boolean operations and ordinary existential \\(\\Diamond\\); counting modalities, nominals, a universal modality, and named level predicates are **not** included.

An \\(r\\)-ary term operation is a function \\(\\mathcal A^r\\to\\mathcal A\\) induced by an algebraic term over the stated signature. The nullary case \\(r=0\\) is included, as are level vectors with \\(h=1\\) or singleton antichains. Set \\(q=2^r\\). The binomial expressions \\(S_m(q)\\) are polynomials over \\(\\mathbb Q\\), evaluated at these positive integer values; \\(\\binom{q}{k}=0\\) for positive integers \\(q<k\\). Empty products are \\(1\\).

## Proof

**1. Modal height detects the level.** For \\(1\\le i\\le h\\), consider the formula
\\[\\delta_i:=\\Diamond^{h-i}\\top\\land\\neg\\Diamond^{h-i+1}\\top.\\]
A world on level \\(A_i\\) admits a strict accessibility path of length \\(k\\) exactly when \\(0\\le k\\le h-i\\). Therefore \\(\\delta_i\\) holds precisely at worlds of \\(A_i\\), uniformly in every valuation. In particular, level membership is not an additional predicate.

**2. Complete pointed-type invariants.** Given \\(r\\) propositional inputs, assign to each world its Boolean truth-pattern color in an alphabet \\(C\\) of size \\(q\\). Let \\(P_j\\subseteq C\\) be the nonempty set of colors occurring in \\(A_j\\). For a world \\(x\\in A_i\\), define its signature
\\[\\sigma(x)=(i,c(x),P_{i+1},\\ldots,P_h).\\]
Every modal formula has its truth at \\(x\\) determined by this signature. This is proved by induction on formulas. The Boolean and atomic cases are immediate. At the diamond step, a world \\(x\\in A_i\\) satisfies \\(\\Diamond\\varphi\\) precisely when, for some \\(j>i\\) and some \\(d\\in P_j\\), \\(\\varphi\\) holds at a point of level \\(j\\) and color \\(d\\). By induction the latter truth is determined by \\((j,d,P_{j+1},\\ldots,P_h)\\), which is encoded in \\(\\sigma(x)\\). Multiplicities within \\(P_j\\), and the colors at the other points of \\(A_i\\), never enter.

Conversely, **each signature is definable** by a finite formula. For a color \\(c\\), let \\(\\chi_c\\) be the conjunction of the input literals specifying that color; for \\(r=0\\), it is \\(\\top\\). For every later level \\(j>i\\) and each \\(d\\in C\\), use \\(\\Diamond(\\delta_j\\land\\chi_d)\\) when \\(d\\in P_j\\), and its negation when \\(d\\notin P_j\\). Conjoin these tests with \\(\\delta_i\\land\\chi_{c(x)}\\). This formula holds exactly at pointed valuations of the prescribed signature, including across distinct valuations. Each choice of a local color and a nonempty later-level palette of size at most the respective level width is realizable: place one occurrence of every prescribed palette color on each later level, fill its unused points arbitrarily, and color the distinguished world as prescribed.

**3. Operation count.** The number of realizable palettes at a level of width \\(m\\) is \\(S_m(q)=\\sum_{k=1}^m\\binom qk\\). Hence the number of distinct signatures of level \\(i\\) is \\(q\\prod_{j=i+1}^h S_{n_j}(q)\\). Different levels have different modal-height signatures, so the total is
\\[E_{\\mathbf n}(q)=q\\sum_{i=1}^{h}\\prod_{j=i+1}^{h}S_{n_j}(q).\\]
A term operation must assign a single Boolean output to each signature. Conversely, because each signature has a characteristic formula, every Boolean assignment to this finite signature set is the truth assignment of one disjunction of characteristic formulas. All the signatures occur in some pointed valuations, so distinct assignments yield distinct operations. This proves the exact count \\(2^{E_{\\mathbf n}(2^r)}\\).

**4. Inverse reconstruction and sharp invisibility.** The exponent \\(E_{\\mathbf n}(q)\\) is a rational polynomial in \\(q\\). Agreement of the operation counts for every \\(r\\ge0\\) implies agreement of those polynomials, since the set \\(\\{2^r:r\\ge0\\}\\) is infinite. At \\(q=1\\), every \\(S_m(1)=1\\), so \\(E_{\\mathbf n}(1)=h\\), recovering the height.

Write \\(F_h(q)=E_{\\mathbf n}(q)/q\\). The formula factors recursively as
\\[F_1(q)=1,\\qquad F_h(q)=1+S_{n_h}(q)F_{h-1}(q),\\]
where \\(F_{h-1}\\) belongs to the shortened vector ending at level \\(h-1\\). Each \\(S_m(0)=0\\), and its linear coefficient is
\\[[q]S_m(q)=S_m'(0)=H_m^{\\pm}:=\\sum_{k=1}^{m}\\frac{(-1)^{k-1}}{k}.\\]
The numbers \\(H_m^{\\pm}\\) are pairwise distinct for positive integers \\(m\\): even-indexed partial sums of the alternating harmonic series increase strictly to \\(\\log2\\), while odd-indexed partial sums decrease strictly to \\(\\log2\\). Thus \\([q]F_h=H_{n_h}^{\\pm}\\) uniquely recovers \\(n_h\\). Then exact polynomial division gives
\\[F_{h-1}(q)=\\frac{F_h(q)-1}{S_{n_h}(q)}.\\]
Repeating recovers \\(n_{h-1},\\ldots,n_2\\) in order. Finally, the expression for \\(E_{\\mathbf n}\\) has no occurrence of \\(n_1\\), so changing that first width never changes the spectrum. This proves both directions, including the one-level case.

For illustration, at unary arity the level vectors \\((1,2,1)\\) and \\((5,2,1)\\) both have exactly \\(2^{18}\\) term operations, whereas \\((1,1,2)\\) has \\(2^{20}\\). The invariant remembers the *ordered* later widths, not merely their multiset.

## Verification

A standalone Python verifier at `artifacts/verify.py` uses only the standard library. Run `python3 artifacts/verify.py` from the extracted package root. Its last execution returned:

```text
VERIFY_OK vectors 56 type_tests 168 pointed_valuation_samples 738094 inverse_polynomials 56 direct_clone_tests 22 direct_term_operations_total 16860 root_invariance_families 5
```

The checks enumerate pointed valuations and independently construct nested successor-type signatures; compare them bijectively with the proposed level-and-palette signatures; test the formula at \\(q=1,2,4\\); reconstruct later widths from exact rational polynomials; and directly close the finite sets of nullary and unary algebraic operations in small frames. The direct term-closure computations are separate from the pointed-type enumeration. The code also verifies that changing the initial width leaves the polynomial fixed. These are finite corroborations, **not** a proof for arbitrary widths, heights, or arities; the general result follows from the four mathematical steps above.

## Relationship to prior work

Goldblatt's analysis of transitive frames of bounded circumference (arXiv:1905.11617, first public version 28 May 2019), especially its discussion of irreflexive transitive frames and Section 9 on modal complex algebras, supplies the motivating semantic class but does not state an exact arity-by-arity term-operation census or an inverse ordered-width theorem. Camerlo, Pistone, and Rapallo (arXiv:1712.04191, first public version 12 December 2017) study polynomial constraints on the range of a single modal operator of a finite frame; that range is a different invariant from the full Boolean modal term clone. Reflexive linear-preorder and self-reflexive weak-order computations use different accessibility relations; their palette-reduction or generator criteria do not imply this strict-frame polynomial without a separate comparison and proof.

The claim here concerns precisely finite *irreflexive* ordinal sums of antichains and the exact spectrum/inverse problem. It does not assert novelty for the elementary underlying bisimulation principle or for the alternating-harmonic sequence itself.

## Limitations

The classification is restricted to finite nonempty level vectors and ordinary, single-modality Boolean modal terms. It does not classify isomorphisms of the full algebras, modal theories of arbitrary transitive frames, frames with reflexive points or accessibility within levels, or other signature expansions. Equal spectra do **not** force frame isomorphism, because the initial level size is invisible. No independent audit of correctness or priority has been performed; broader historical literature could contain the same finite-clone inverse theorem under different terminology.

## References

1. R. Goldblatt, *Modal Logics that Bound the Circumference of Transitive Frames*, arXiv:1905.11617 (first posted 28 May 2019), esp. Sections 2–3 and 9. https://arxiv.org/abs/1905.11617
2. R. Camerlo, G. Pistone, F. Rapallo, *Modal Operators and Toric Ideals*, arXiv:1712.04191 (first posted 12 December 2017), esp. Sections 1–2 and 5. https://arxiv.org/abs/1712.04191
3. P. Blackburn, M. de Rijke, Y. Venema, *Modal Logic*, Cambridge University Press, 2001, chapters on Kripke semantics and modal algebras (general background).
