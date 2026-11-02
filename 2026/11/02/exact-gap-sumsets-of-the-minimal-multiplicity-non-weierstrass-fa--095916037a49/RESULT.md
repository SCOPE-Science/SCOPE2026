# Exact gap-sumsets of the minimal-multiplicity non-Weierstrass family

## Finding

For every integer \(g\ge13\) with \(3\nmid g\), let
\[
S_g=\langle6,9,g,g+3\rangle\subseteq\mathbb Z_{\ge0},\qquad
G_g=\mathbb Z_{>0}\setminus S_g,\qquad F=2g-3.
\]
For every integer \(h\ge1\), the complete \(h\)-fold gap-sumset is
\[
\begin{aligned}
hG_g=[h,hF]\cap\mathbb Z\;\setminus\;&\Bigl(
\{hF-g+3j:1\le j\le\lfloor g/3\rfloor\}\\
&\quad\cup\{hF-(2g-6)+3j:1\le j\le\lfloor(2g-6)/3\rfloor\}\Bigr).
\end{aligned}
\]
The two omitted progressions are disjoint and contain exactly \(g-3\) integers in total, independently of \(h\). Thus
\[
|hG_g|=(2h-1)g-4h+4.
\]
In particular, for every \(h\ge2\),
\[
(2h-1)(g-1)-|hG_g|=2h-3>0.
\]
Consequently **none of Buchweitz's higher gap-sum tests** detects the non-Weierstrass property of this infinite family, whose non-Weierstrass property was established by Eisenbud and Schreyer (2026). The non-Weierstrass theorem itself is prior work, not a new assertion proved here.

## Assumptions and scope

A *numerical semigroup* is an additively closed cofinite subset of \(\mathbb Z_{\ge0}\) containing zero. Its *gaps* are the positive integers outside it and its *genus* is the number of gaps. For a finite integer set \(G\) and integer \(h\ge1\), \(hG=\{x_1+\cdots+x_h:x_i\in G\}\) is its \(h\)-fold Minkowski sum, with repetitions allowed. The interval \([u,v]\cap\mathbb Z\) includes both endpoints.

The sole parameters are an integer \(g\ge13\) not divisible by three and an integer \(h\ge1\). The statement is combinatorial and independent of base field. The connection to Weierstrass realizability concerns the already-published complex-curve obstruction for these numerical semigroups. No assertion about any semigroup with \(3\mid g\) is made.

## Proof

**Step 1: the three residue progressions of gaps.** Let \(\alpha\in\{1,2\}\) be the least positive residue of \(g\) modulo three and let \(\beta\in\{1,2\}\) be the least positive residue of \(2g\) modulo three, so \(\{\alpha,\beta\}=\{1,2\}\). Set
\[
A=\{\alpha,\alpha+3,\ldots,g-3\},\qquad
B=\{\beta,\beta+3,\ldots,2g-3\}.
\]
All positive multiples of three except three belong to \(S_g\), because \(6,9\) generate every multiple of three at least six. The smallest semigroup element in residue class \(g\pmod3\) is \(g\), and the smallest in residue class \(2g\pmod3\) is \(2g\). Adding multiples of three gives all subsequent entries in either class. Hence
\[
G_g=\{3\}\sqcup A\sqcup B.
\]
The largest gap is \(F=2g-3\). Directly counting the two residue progressions and the singleton gives \(|G_g|=g\). Also \(\{1,2,3\}\subset G_g\).

**Step 2: every residue class in every higher sumset is an uninterrupted progression.** For \(h=1\), the preceding display gives this property, but the residue-zero progression has one element. For \(h=2\), the three residue pieces are
\[
(A+B)\cup\{6\},\qquad (A+A)\cup(3+B),\qquad (B+B)\cup(3+A).
\]
Each sum of two step-three progressions is again a complete step-three progression. The first union is a progression because \(A+B\) begins at three and contains six; the other two are progressions because their respective initial terms differ by at most three and their intervals overlap or touch. (The shortest original progression, \(A\), has at least four terms since \(g\ge13\).) Thus every residue piece of \(2G_g\) is a complete step-three progression with at least two terms.

Assume the same for \(hG_g\) with \(h\ge2\). In any fixed residue class modulo three, the corresponding part of \((h+1)G_g\) is the union of the appropriate parts of \(hG_g+3\), \(hG_g+A\), and \(hG_g+B\). Each is a complete step-three progression containing at least two terms, and each begins between \(h+1\) and \(h+5\): by induction the first members of the three residue pieces of \(hG_g\) are the integers \(h,h+1,h+2\), since \(hG_g\subseteq[h,\infty)\) and \(\{1,2,3\}\subseteq G_g\). Thus first terms in a fixed residue differ by at most three, and these progressions overlap or touch, leaving no internal holes. Each residue piece of \((h+1)G_g\) again contains at least two terms. Moreover its first term is the unique integer of its residue among \(h+1,h+2,h+3\). This completes the induction.

**Step 3: exact upper endpoints.** Every summand belongs to \(A\), \(B\), or \(\{3\}\). Starting from the unconstrained maximum \(hF\), each selection from \(A\) costs at least \(F-(g-3)=g\), and each singleton-three selection costs \(F-3=2g-6\), while a selection from \(B\) costs at least zero. Modulo three, these losses are respectively \(g\), \(2g\), and zero. The least loss in the zero class is zero (take only \(F\)); the least loss in class \(g\pmod3\) is \(g\) (take one \(g-3\) and \(h-1\) copies of \(F\)); and the least loss in class \(2g\pmod3\) is \(2g-6\) (take one three and \(h-1\) copies of \(F\)). Indeed, a three selection already costs \(2g-6>g\), two \(A\) selections cost at least \(2g>2g-6\), and all other relevant nonnegative combinations cost more. The three maxima are consequently
\[
hF,\qquad hF-g,\qquad hF-(2g-6),
\]
in three different residues modulo three.

**Step 4: all omitted integers and their count.** Step 2 shows that each residue piece begins at the appropriate member of \(\{h,h+1,h+2\}\) and continues by threes to its Step 3 maximum. Therefore the only omitted integers from \([h,hF]\cap\mathbb Z\) are the numbers above the two lower maxima having the same residues. They are precisely the two progressions stated in the theorem. Their lengths are \(\lfloor g/3\rfloor\) and \(\lfloor(2g-6)/3\rfloor\), whose sum is \(g-3\) because \(3\nmid g\). Subtraction from the interval's \(h(2g-4)+1\) elements proves
\[
|hG_g|=h(2g-4)+1-(g-3)=(2h-1)g-4h+4.
\]

Buchweitz's necessary condition for a genus-\(g\) numerical semigroup to be Weierstrass is \(|hG|\le(2h-1)(g-1)\) for every integer \(h\ge2\). The difference for the present family equals \(2h-3>0\), completing the claimed failure of **all** of these tests to detect non-Weierstrass realizability. This numerical conclusion is logically distinct from the published syzygy obstruction proving that these semigroups are in fact non-Weierstrass.

## Verification

The self-contained Python 3 program `verify_gap_sums.py` constructs semigroup membership by dynamic addition from its four generators; independently enumerates every gap-sumset by Minkowski addition; and compares each set, not only its size, with the two explicit omitted progressions. It verifies \(864\) parameter pairs: all \(g\) from \(13\) through \(120\) not divisible by three, and all \(h\) from \(1\) through \(12\). It also checks the exact Buchweitz deficit in every applicable case. When executed, it prints `VERIFY_OK`.

The finite program is **not** a proof for arbitrary parameters; Steps 1–4 supply that proof. The script does not reproduce or independently validate the published theorem that this family is non-Weierstrass.

For \(g=13\), the first sumset sizes are \(|G_{13}|=13\), \(|2G_{13}|=35\), and \(|3G_{13}|=57\); the corresponding Buchweitz thresholds at orders two and three are \(36\) and \(60\).

## Relationship to prior work

Eisenbud and Schreyer, *A family of Non-Weierstrass Semigroups*, arXiv:2603.00780v1 (first submitted 28 February 2026), introduce the family \(\langle6,9,g,g+3\rangle\) and prove its non-Weierstrass status for \(g\ge13\), \(3\nmid g\) (Example 3.2). Their argument uses graded syzygies; their inspected original manuscript does not state the exact all-order gap-sumsets above. Their later revision has a different title and has not been exhaustively compared.

Eliahou, García-García, Marín-Aragón and Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup* (2022/2023), introduce \(\beta_G(h)=|hG|-(2h-1)(|G|-1)\), study general eventual sumset growth and construct semigroups whose Buchweitz sets are nonempty. Their general eventual-linearity theorem applies abstractly here but neither specifies this family nor determines the exact formula starting at order one. Here \(\beta_{G_g}(h)=3-2h\) for all \(h\ge1\), so the entire Buchweitz set is empty despite non-Weierstrass status.

García-García, Marín-Aragón, Torres and Vigneron-Tenorio, *On reducible non-Weierstrass semigroups* (2020/2021), construct other non-Weierstrass families, including those detectable by the second-order Buchweitz criterion; those generator families and their statements do not imply this exact calculation. Standard Macaulay2 `buchweitz` and `buchweitzSemigroups` documentation likewise concerns detectable, rather than undetected, instances.

## Limitations

The explicit formula is specific to the four-generated family and assumes \(3\nmid g\), \(g\ge13\). It does not classify all non-Weierstrass semigroups invisible to Buchweitz's condition, nor does it prove the independent, previously established non-Weierstrass theorem. No human or independent mathematical audit has been performed. There remains a possibility that older additive-combinatorial statements imply a special case or that later revisions of the motivating paper contain a related observation; the claim to mathematical priority is therefore qualified.

## References

1. D. Eisenbud and F.-O. Schreyer, *A family of Non-Weierstrass Semigroups*, arXiv:2603.00780v1, 28 February 2026, https://arxiv.org/abs/2603.00780.
2. S. Eliahou, J. I. García-García, D. Marín-Aragón and A. Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup*, Bulletin of the Brazilian Mathematical Society 54, article 4 (2023), https://doi.org/10.1007/s00574-022-00322-8; preprint arXiv:2011.09187.
3. J. I. García-García, D. Marín-Aragón, F. Torres and A. Vigneron-Tenorio, *On reducible non-Weierstrass semigroups*, Open Mathematics 19 (2021), 1134–1144; preprint arXiv:2005.12896.
4. NumericalSemigroups package, Macaulay2, `buchweitz` and `buchweitzSemigroups` documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/NumericalSemigroups/html/_buchweitz.html.
