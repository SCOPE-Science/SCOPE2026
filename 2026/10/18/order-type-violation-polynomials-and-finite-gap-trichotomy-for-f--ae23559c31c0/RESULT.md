# Order-type violation polynomials and finite-gap trichotomy for finite Gödel chains

## Finding

**Theorem.** Let \(k\ge 1\) and let \(E\) be any equation \(t(x_1,\ldots,x_k)=s(x_1,\ldots,x_k)\) in the bounded Heyting signature \(\{\wedge,\vee,\to,\bot,\top\}\). Write \(C_n\) for the \(n\)-element Gödel (Heyting) chain, where \(n\ge2\), and \(\operatorname{ds}_{C_n}(E)\) for the probability that a uniform independent \(k\)-tuple satisfies \(E\). There are explicitly computable nonnegative integers \(c_0(E),\ldots,c_k(E)\) such that, **for every \(n\ge2\)**,
\[
1-\operatorname{ds}_{C_n}(E)
=\frac{1}{n^k}\sum_{d=0}^{k}c_d(E)\binom{n-2}{d}.
\]
Here the binomial coefficient is zero for \(d>n-2\). In particular,
\[
\lim_{n\to\infty}\operatorname{ds}_{C_n}(E)=1-\frac{c_k(E)}{k!}.
\]
Exactly one of the following applies to the class \(\mathcal P\) of all finite nonempty direct products of nontrivial finite Gödel chains:

1. Every \(c_d(E)\) is zero. Then \(E\) is valid in every member of \(\mathcal P\).
2. \(c_k(E)=0\), but some \(c_d(E)>0\). Then \(E\) has **no finite satisfiability gap** even on single chains: it fails on all sufficiently large chains, but its satisfaction degree tends to one.
3. \(c_k(E)>0\). Then, for every \(A\in\mathcal P\), either \(\operatorname{ds}_A(E)=1\) or
\[
\operatorname{ds}_A(E)\le 1-\frac{1}{(k+2)^k}.
\]

These cases and the entire exact probability sequence are determined by inspecting at most \((k+2)^k\) assignments in the single chain \(C_{k+2}\). The gap constant is explicit, not asserted optimal.

## Assumptions and scope

A finite Gödel chain is \(C_n=\{0,1,\ldots,n-1\}\), ordered as written, with
\[
a\wedge b=\min(a,b),\quad a\vee b=\max(a,b),\qquad
a\to b=\begin{cases}n-1,&a\le b,\\b,&a>b.\end{cases}
\]
The constants \(\bot\) and \(\top\) are \(0\) and \(n-1\), respectively. The probability \(\operatorname{ds}_{A}(E)\) uses independent uniform sampling *with replacement* from \(A^k\). The class \(\mathcal P\) consists of finite Cartesian products of these chains with the coordinatewise Heyting operations; **it is not the class of all finite Gödel algebras**, because not every finite Gödel algebra is a direct product of chains. No claim is made for arbitrary finite Heyting or Gödel algebras.

A *boundary-marked weak order type* on the labelled variables \(x_1,\ldots,x_k\) consists of an optional block assigned bottom, an optional block assigned top, and \(d\) nonempty ordered interior blocks, with each variable in exactly one block. Thus \(0\le d\le k\). Define \(c_d(E)\) as the number of such types for which \(t\) and \(s\) evaluate differently. This is well-defined by the proof.

## Proof

**Step 1: order preservation of term evaluation.** Let \(h:C_m\hookrightarrow C_n\) be a strictly increasing map that preserves both \(0\) and the greatest element. It preserves minimum and maximum. It also preserves Heyting implication: if \(a\le b\), both implications equal their respective greatest elements; if \(a>b\), both equal \(b\) (after applying \(h\)). Induction on the two terms therefore gives
\[
h(t^{C_m}(\mathbf a))=t^{C_n}(h(\mathbf a)),\qquad
h(s^{C_m}(\mathbf a))=s^{C_n}(h(\mathbf a)).
\]
Consequently, the truth or failure of \(E\) depends only on which variables equal each other, which equal bottom or top, and the strict order of the remaining interior blocks—not on the particular chain elements chosen.

**Step 2: count the realizations of a weak order type.** A type with \(d\) ordered interior blocks is realized on \(C_n\) by choosing exactly \(d\) distinct elements of \(\{1,\ldots,n-2\}\), in their increasing order. There are \(\binom{n-2}{d}\) choices. Every \(k\)-tuple has one and only one such type. Grouping all failing types by \(d\) gives
\[
\#\{\mathbf a\in C_n^k:t(\mathbf a)\ne s(\mathbf a)\}
=\sum_{d=0}^{k}c_d(E)\binom{n-2}{d},
\]
proving the claimed exact polynomial in \(n-2\). Every type is represented in \(C_{k+2}\), because it uses at most \(k\) interior values; this also proves the finite algorithmic bound.

**Step 3: limit and dichotomy.** The leading coefficient of the displayed polynomial is \(c_k(E)/k!\). Since \(c_k(E)\) counts only strict total orderings of all \(k\) variables strictly between bottom and top, \(0\le c_k(E)\le k!\). Dividing by \(n^k\) yields the limit. If all \(c_d(E)=0\), no assignment violates \(E\). If \(c_k(E)=0\) and some lower coefficient is positive, the numerator is \(O(n^{k-1})\) but is positive for every \(n\ge d+2\), where \(d\) is any index with positive coefficient; hence the violation probability tends to zero through positive values. This rules out a finite gap.

**Step 4: positive uniform gap.** Suppose \(c_k(E)\ge1\). For \(n\ge k+2\), the violation probability is at least
\[
\frac{\binom{n-2}{k}}{n^k}
=\frac1{k!}\prod_{j=2}^{k+1}\left(1-\frac jn\right).
\]
Each factor is nonnegative and increases with \(n\), so this expression is minimized at \(n=k+2\), where it equals \((k+2)^{-k}\). For \(2\le n<k+2\), any violated equation has at least one failing tuple, hence violation probability at least \(n^{-k}>(k+2)^{-k}\). This proves the uniform gap on every single chain.

For \(A=C_{n_1}\times\cdots\times C_{n_r}\), coordinatewise equality gives
\[
\operatorname{ds}_{A}(E)=\prod_{i=1}^{r}\operatorname{ds}_{C_{n_i}}(E).
\]
If any factor is not fully satisfying, the product does not exceed \(1-(k+2)^{-k}\); otherwise it is one. Conversely a sequence of nonvalid single chains with satisfaction degrees approaching one already witnesses the absence of a gap for \(\mathcal P\). This establishes the trichotomy.

## Verification

The standalone finite checker `verify.py` constructs boundary-marked weak order types from representative assignments in \(C_{k+2}\), computes the predicted binomial polynomial, and separately enumerates *every* assignment in \(C_n^k\) for \(2\le n\le9\). It covers 201 explicit and reproducibly generated equations of arities one through three, evaluating 153,624 assignments and checking 4,259 canonical pattern visits. It also separately checks equation satisfaction on 16 Cartesian products of small chains.

Running `python verify.py` produced:
```
VERIFY_OK equations=201 tuple_assignments=153624 canonical_patterns=4259 product_pairs=16
double-negation-top [1, 0]
double-negation-elimination [0, 1]
material-implication [0, 1, 1]
reflexivity [0, 0]
excluded-middle [0, 1]
comparison [2, 4, 2]
```
For example, when \(E\) is \(\neg\neg x=\top\), the numerator is the constant one, so \(\operatorname{ds}_{C_n}(E)=1-1/n\) and there is no gap. When \(E\) is \(\neg\neg x=x\), the numerator is \(n-2\), so the equation has a gap over \(\mathcal P\) but is valid in \(C_2\). For \(x\to y=\neg x\vee y\), the numerator is
\[
(n-2)+\binom{n-2}{2}=\frac{(n-1)(n-2)}{2},
\]
and the satisfaction degree tends to \(1/2\).

Finite tests support the checker and examples; the proof for all terms and chain sizes is the order-embedding argument, not the enumerations.

## Relationship to prior work

Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (first preprint October 21, 2021, arXiv:2110.11515), develop finite satisfiability gaps in Heyting algebras, classify one-variable equations in the unrestricted class, establish degree multiplicativity for direct products (Proposition 1.14), and explicitly raise classification in restricted settings such as Gödel algebras (discussion, Section 6.6). Those contributions are not claimed as new.

Fermüller, Lang and Pavlova, *From Truth Degree Comparison Games to Sequents-of-Relations Calculi for Gödel Logic* (2022, DOI:10.1007/s11787-022-00300-0), describe the min/max/implication semantics and prove/explain the fundamental dependence of Gödel-term truth comparisons on relative order of truth values. That pre-existing semantic property is the starting lemma here, not the novelty claim.

The contribution assessed here is an exact **nonnegative binomial-basis violation polynomial for every multi-variable equation**, the resulting computable all-equation finite-gap trichotomy on chain products, the rational permutation-limit law, and an equation-independent positive gap bound in the full-gap case. The inspected works study classification or proof systems, not this combined enumeration-and-gap result.

## Limitations

The class \(\mathcal P\) excludes finite Gödel algebras that are merely subdirect products of chains, as well as general finite Heyting algebras. The bound \((k+2)^{-k}\) is not optimized. The coefficient computation may be exponential in \(k\); no claim of efficient complexity for arbitrary input arity is made. The proof is mathematical and self-reviewed; independent mathematical audit and publication-priority verification have not been performed. Earlier results under order-pattern counting, fuzzy-logic statistics, or equational-probability terminology could provide equivalent coverage; the full Noetherian Gödel logics paper was not materially examined.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first publicly posted 2021-10-21), especially Proposition 1.14 and Sections 2, 3, 6.6.
2. C. Fermüller, T. Lang and A. Pavlova, *From Truth Degree Comparison Games to Sequents-of-Relations Calculi for Gödel Logic*, Logica Universalis **16** (2022), 221–235, DOI:10.1007/s11787-022-00300-0.
3. J. P. Aguilera, J. Bydžovský and D. Fernández-Duque, *Noetherian Gödel logics*, Journal of Logic and Computation **32** (2022), 1487–1503, DOI:10.1093/logcom/exac064 (abstract-level contextual comparison only).
