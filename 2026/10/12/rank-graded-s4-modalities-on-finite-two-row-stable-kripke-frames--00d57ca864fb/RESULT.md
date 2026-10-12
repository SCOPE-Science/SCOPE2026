# Rank-graded S4 modalities on finite two-row stable Kripke frames

## Finding

For every integer \(n\ge2\), take the finite distributive stable frame
\(W_n=C_2\times C_n\), where \(C_k\) is the \(k\)-element chain. Work with
Kavvos's stable bimodules \(R\subseteq W_n^2\), hence with their uniquely induced
adjoint modal pair \(\blacklozenge_R\dashv\Box_R\) on the complete lattice
\(\operatorname{Filt}(W_n)\) of nonempty filters. Restrict to those satisfying the
additional S4-style equations
\[
\Box_R(F)\subseteq F,\qquad \Box_R^2(F)=\Box_R(F)
\quad\text{for all }F\in\operatorname{Filt}(W_n).
\]
(The defining stable-bimodule conditions already ensure that \(\Box_R\)
preserves finite meets and the top filter.)

Let \(R_n(u)\) be the fixed-filter rank polynomial: each admissible *distinct*
stable bimodule is counted once, with weight
\(u^{|\{F:\Box_R(F)=F\}|}\). Then
\[
\boxed{R_n(u)=\sum_{m=2}^{n}\binom{n-2}{m-2}u^m
\left(\sum_{c=0}^{m}(m-c+1)u^c-2\right).}
\tag{1}
\]
Equivalently, the entire family is encoded by the rational bivariate series
\[
\boxed{\sum_{n\ge2}R_n(u)z^{n-2}
=\frac{u^2(1+u-z(1+u+u^2))^2}
{(1-z(1+u))^2(1-z(1+u^2))}.}
\tag{2}
\]
Every fixed-filter rank from \(2\) through \(2n\) occurs. The two extremal
ranks are each unique; exactly \(2(n-1)\) structures have three fixed filters,
and exactly two have \(2n-1\) fixed filters. The number without rank weighting is
\[
R_n(1)=2^{n-5}(n^2+11n+6),\qquad n\ge2.
\tag{3}
\]
The *numeric sequence in (3) is already present in OEIS A341867*, as
\(T(2,n-2)\). No novelty is claimed for that ungraded sequence. The stated
contribution is the precise modal interpretation, fixed-filter-rank refinement,
canonical forms, and bivariate generating function.

For illustration,
\[
R_2(u)=u^2+2u^3+u^4,\quad
R_3(u)=u^2+4u^3+4u^4+2u^5+u^6,
\]
\[
R_4(u)=u^2+6u^3+10u^4+8u^5+5u^6+2u^7+u^8.
\]

## Assumptions and scope

The frame \(W_n\) is the *entire* labeled lattice \(C_2\times C_n\), not an
arbitrary product or an isomorphism class varying with the relation. The
relations must satisfy all four stable-bimodule conditions of Definition 4.1
in the source paper, as well as bimodule monotonicity. The modal map
\(\Box_R\) acts on all nonempty filters, with those filters ordered by inclusion.
In the finite case, every filter is principal; the lattice of filters is
canonically order-isomorphic to \(W_n^{\mathrm{op}}\), hence to
\(L_n=C_2\times C_n\) after reversing both coordinates. All enumerations here
count concrete relations on this fixed frame, not isomorphism classes of frames
or of modal algebras. The adjoint modal pair is uniquely determined by
\(\Box_R\) and conversely by the stable correspondence established in
Section 4 of Kavvos's paper.

## Proof

**1. Fixed elements of a meet-preserving S4 operator.** Let \(L\) be any
finite bounded lattice, and let \(f:L\to L\) satisfy
\[
f(1)=1,\quad f(x\wedge y)=f(x)\wedge f(y),\quad
f(x)\le x,\quad f(f(x))=f(x).
\]
Because meet preservation implies monotonicity, the fixed set
\(S=\{x:f(x)=x\}\) is closed under meets. It contains \(0\) by deflation and
\(1\) by hypothesis. If \(x,y\in S\), monotonicity yields
\(x\vee y=f(x)\vee f(y)\le f(x\vee y)\le x\vee y\), so it is also
join-closed. Thus \(S\) is a bounded sublattice.

Conversely, for every bounded sublattice \(S\subseteq L\), define
\[
f_S(x)=\bigvee\{s\in S:s\le x\}.
\tag{4}
\]
This join lies in \(S\), because the set is nonempty (it contains \(0\)) and
\(S\) is finite and join-closed. It is the largest element of \(S\) below
\(x\); in particular it is deflationary, idempotent, fixes exactly \(S\), and
fixes \(1\). The inclusion map \(S\hookrightarrow L\) is a finite-join
homomorphism and has \(f_S\) as right adjoint: for \(s\in S\),
\(s\le x\iff s\le f_S(x)\). Right adjoints preserve meets in \(S\), and the
inclusion of the sublattice preserves those meets in \(L\). Hence
\(f_S(x\wedge y)=f_S(x)\wedge f_S(y)\). Finally, every earlier operator
coincides with \(f_S\): its value at \(x\) is a fixed point below \(x\), while
monotonicity makes it at least every fixed point below \(x\). This proves a
bijection between the allowed operators and bounded sublattices, with
\(|\operatorname{Fix}(f_S)|=|S|\).

**2. Two-row normal form.** Identify \(L_n\) with
\(\{0,1\}\times\{0,\dots,n-1\}\) using coordinatewise meet and join.
A bounded sublattice \(S\) contains \((0,0)\) and \((1,n-1)\). In each column
\(j\), label the selection of its two elements by
\(\varnothing\) (neither), \(A\) (only \((0,j)\)), \(C\) (both), or
\(B\) (only \((1,j)\)). Omit the empty labels. We claim that the remaining
word is weakly increasing in the order \(A<C<B\), with its first letter
\(A\) or \(C\), and its last \(C\) or \(B\). Necessity of these endpoint
conditions is immediate.

For the ordering, take two occupied columns \(i<j\). If the earlier column
contains its upper-row element and the later column contains its lower-row
element, the meet and join of those two points force the lower-row element
also at \(i\) and the upper-row element also at \(j\). This excludes
\(B\) followed by \(A\) or \(C\), and \(C\) followed by \(A\). Conversely,
if the selected occupied labels are of the form \(A^aC^cB^b\), all
cross-row pairs at different columns already have their coordinatewise meet
and join selected (or require no new points), while same-row pairs are
trivially closed. This establishes the normal form, including the possibility
of arbitrarily many empty columns.

**3. Grading and enumeration.** Let \(m\) be the number of occupied columns,
which necessarily includes the first and last, so \(2\le m\le n\). Their
positions can be chosen in \(\binom{n-2}{m-2}\) ways. For a fixed number
\(c\) of double-occupied \(C\) columns, all nonempty words have
\(a+c+b=m\) and \(a,b\ge0\), giving \(m-c+1\) words. For \(c=0\), exactly
two words (all \(A\), or all \(B\)) violate the endpoint condition; for
\(c>0\), none does. Such a word fixes precisely \(a+2c+b=m+c\) filter
elements. Multiplication by its weight and summing proves (1).

For (2), use
\[
\sum_{n\ge m}\binom{n-2}{m-2}z^{n-2}
=\frac{z^{m-2}}{(1-z)^{m-1}},
\]
and the elementary identity
\[
\sum_{m\ge0}x^m\sum_{c=0}^{m}(m-c+1)u^c
=\frac{1}{(1-x)^2(1-ux)}.
\]
Subtracting the two forbidden \(c=0\) words in every \(m\ge2\), then
substituting \(x=uz/(1-z)\) and simplifying gives (2).
At \(u=1\), the right side of (2) reduces to
\((2-3z)^2/(1-2z)^3\), whose coefficient of \(z^{n-2}\) is (3).
The leading and smallest coefficients and full-support property follow
directly from (1): \(m=n\) and \(c=0,1,\dots,n\) cover ranks
\(n,\dots,2n\); for ranks \(k\le n\), take \(m=k,c=0\) when \(k\ge2\).
The rank-two, rank-three, rank-\((2n-1)\), and rank-\(2n\) coefficients are
\(1\), \(2(n-1)\), \(2\), and \(1\), respectively.

**4. Return to stable relations.** By Sections 4 and 4.2 of Kavvos,
finite stable bimodules on a fixed stable frame correspond bijectively to
finite-meet- and top-preserving modal right adjoints on the lattice of
nonempty filters. For \(W_n\), this filter lattice is \(L_n\) up to canonical
order reversal. The extra equations \(\Box\le\mathrm{id}\) and
\(\Box^2=\Box\) are exactly those of step 1. All counts and normal forms
therefore apply to distinct stable relations, not merely to abstract
endomaps.

## Verification

Run \(python3\ \texttt{verify.py}\) (Python standard library only). The verifier
independently enumerates all \(21{,}844\) bounded-subset candidates on
\(L_n\) through \(n=8\), obtains \(2{,}143\) actual bounded sublattices,
and checks their exact fixed-set rank distributions and normal forms.
It checks \(351\) directly constructed interior-operator tables through
\(n=6\), screens all \(46{,}912\) unrestricted function tables through
\(n=3\), and screens all \(65{,}536\) relations on the four-world frame
\(W_2\) against the stable-bimodule axioms (exactly \(16\) stable, of which
\(4\) meet the extra S4 conditions). It also checks the rational series
coefficientwise through \(n=10\). These are finite consistency checks;
the general statements depend on the proof above.

## Relationship to prior work

Kavvos, *Two-dimensional Kripke Semantics II: Stability and Completeness*,
arXiv:2406.03578 (first submitted June 5, 2024), gives the stable-bimodule
semantics, modal adjunction, and categorical correspondence used in step 4.
Its Sections 3 and 4 were inspected, and no two-row fixed-filter-rank
classification or rational census (1)--(2) was found. The correspondence
itself is prior work, not claimed as new.

OEIS A341867 (Jianing Song and subsequent contributors) contains the
ungraded row \(T(2,n-2)\) with exactly the values of (3); McConville and
Mühle's *Bubble Lattices I: Structure* (arXiv:2202.02874) and *Bubble
Lattices II: Combinatorics* (arXiv:2208.13683) are cited there for another
interpretation of the whole array. The ungraded sequence, its rational
univariate series, and the abstract operator--fixed-sublattice
correspondence are not asserted original. The novel target is the natural
fixed-filter-rank refinement for stable S4 frames, with explicit forms and
bivariate series. That refinement cannot be recovered merely from the
ungraded OEIS row without additional structure.

## Limitations

No claim is made for higher-width products, non-S4 stable modalities,
infinite stable frames, or quotients by frame automorphisms. The published
source does not propose this enumeration as an open problem; its relation
to stable semantics motivates the choice of operators. A prior unindexed
rank-refined sublattice enumeration might imply (1)--(2), and the
originality assessment does not rule that out. This is a concise finite
enumeration theorem, not a new modal completeness or representation theorem.
Independent mathematical audit has not been performed.

## References

1. G. A. Kavvos, *Two-dimensional Kripke Semantics II: Stability and Completeness*, arXiv:2406.03578 (v1, 2024-06-05), Sections 3--4, https://arxiv.org/html/2406.03578v3 .
2. J. Song and collaborators, *OEIS A341867*, https://oeis.org/A341867 , especially row \(T(2,n)\) and references.
3. T. McConville and H. Mühle, *Bubble Lattices I: Structure*, arXiv:2202.02874, https://arxiv.org/abs/2202.02874 .
4. T. McConville and H. Mühle, *Bubble Lattices II: Combinatorics*, arXiv:2208.13683, https://arxiv.org/abs/2208.13683 .
