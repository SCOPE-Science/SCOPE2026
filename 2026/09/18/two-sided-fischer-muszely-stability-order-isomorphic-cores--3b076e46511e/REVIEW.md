# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Passed.**

The argument uses Hatori--Oi's Theorem 5.2 twice. For a bijection \(T:A_+\to B_+\) with finite forward and inverse FM defects, that theorem gives bounded positive linear maps \(L:A\to B\) and \(M:B\to A\) at finite uniform distance from \(T\) and \(T^{-1}\), respectively.

The crucial mutual-inverse step was checked directly. For \(a\in A_+\),
\[
n\|ML(a)-a\|
=
\|ML(na)-na\|
\le 3\|M\|\Delta(T)+3\Delta(T^{-1}).
\]
Division by \(n\) gives \(ML(a)=a\), and the positive cone generates \(A\). The symmetric argument gives \(LM=I_B\). Thus \(M=L^{-1}\), with both maps positive and bounded. No complementability, compactness, or duality assumption is used.

The converse bounded-perturbation estimate is a direct three-error inequality. If
\(D(T,R)\le\eta\) for a linear order isomorphism \(R\), then
\(\Delta(T)\le3\eta\), while
\[
D(T^{-1},R^{-1})\le\|R^{-1}\|\eta
\]
and hence \(\Delta(T^{-1})\le3\|R^{-1}\|\eta\).

The weighted \(c_0\) family was checked coordinatewise. The scalar inverse has slopes
\(1/(1+w)\) and \(1/w\). Its additive defect is nonnegative and at most
\(\varepsilon/w\) in every branch, with equality at
\(u=v=(1+w)\varepsilon\). This proves
\[
\Delta(T_w^{-1})=\sup_n\varepsilon/w_n.
\]
The forward defect is exactly \(\varepsilon\), and the dyadic/asymptotic core is multiplication by \(w\). Multiplication by a bounded strictly positive sequence has dense range on \(c_0\), and is a bounded order isomorphism exactly when \(\inf_n w_n>0\).

## Originality

**Passed, to the best of our knowledge.**

The primary 2026 Hatori--Oi paper was checked at theorem level. Theorem 5.2 gives the unique positive linear core at distance at most \(3\varepsilon\) and only dense positive image in general. Example 5.3 gives the continuous bijective \(c_0\) map with weights \(w_n=1/n\) whose core is not onto. Corollary 6.2 already proves that an additional coarse lower distance estimate forces the core to be a linear order isomorphism. Therefore the present result does not claim that inverse finite FM defect is the weakest possible supplementary assumption.

What was not found in that paper or in searches using inverse, two-sided, approximate-FM, order-isomorphism, bounded-perturbation, and \(c_0\) terminology is the exact equivalence
\[
\Delta(T^{-1})<\infty
\iff
\text{the forward asymptotic core is an order isomorphism},
\]
the identification of the two asymptotic cores as literal inverses, or the exact weighted-family formula
\(\Delta(T_w^{-1})=\varepsilon/\inf w_n\).

Tabor's 2003 theorem was checked as prior stability work: its domain is a group and its range a whole Banach space, so it does not give the positive-cone order-isomorphism criterion. Dong--Leung--Li's positive-cone stability theorem concerns approximate isometries rather than the FM defect.

A material residual prior-art risk is O. Hatori and S. Oi, *Order isomorphisms on positive cones of non-unital \(C^*\)-algebras* (unpublished manuscript, 2026), which is cited in the primary paper without a public identifier. Its full text was not inspected. It is plausibly relevant to the order-isomorphism theory, although the available 2026 JB-algebra paper already records the stability theorem, the loss-of-surjectivity example, and the coarse lower-distance restoration result against which the present statement was compared.

## Value

**Passed.**

Hatori--Oi's new stability theorem leaves a concrete structural gap: a bijective approximate FM map can have a dense but nonsurjective linear asymptotic core. The result identifies exactly what repairs this failure in the natural two-sided setting: finite FM defect for the inverse. It also shows that the forward and inverse linearizations cannot drift independently; scaling forces them to be genuine inverse order isomorphisms.

The weighted \(c_0\) family supplies an exact boundary rather than only an existence argument. The forward defect stays fixed at \(\varepsilon\), whereas the inverse defect is \(\varepsilon/\inf w_n\) and becomes infinite precisely when the core loses bounded invertibility. The original \(w_n=1/n\) counterexample is therefore the singular endpoint of an explicit condition-number family.

## Limitations

The constants inherited from Hatori--Oi are not claimed optimal. The inverse-FM condition is not minimal, since Hatori--Oi's Corollary 6.2 uses a different coarse lower-distance condition that also forces an order isomorphism. The exact inverse-defect formula is specific to the diagonal \(c_0\) family. No novelty is claimed for the existing weighted Jordan representation once an order isomorphism is known.
