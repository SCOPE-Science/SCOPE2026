# Hawthorne’s sparse-multiplication NIP examples are necessarily unstable

## Finding

Christopher Hawthorne proved that, for every integer \(d\ge2\),
\[
T_d=\operatorname{Th}(\mathbb Z,+,d^{\mathbb N},\times\!\upharpoonright d^{\mathbb N})
\]
is NIP, and that for every prime \(p\ge7\),
\[
S_p=\operatorname{Th}(\mathbb F_p[t],+,t^{\mathbb N},\times\!\upharpoonright t^{\mathbb N})
\]
is NIP.

These examples are never stable. In fact, their instability is already visible on the distinguished sparse set.

Write \(P=d^{\mathbb N}\) in the integer case and \(P=t^{\mathbb N}\) in the polynomial case, and let \(R(x,y,z)\) denote the graph of multiplication restricted to \(P\). Under the exponent bijection
\[
d^n\longleftrightarrow n
\qquad\text{or}\qquad
t^n\longleftrightarrow n,
\]
the induced relational structure \((P,R)\) is canonically isomorphic to \((\mathbb N,\operatorname{Add})\), where \(\operatorname{Add}(i,j,k)\) means \(i+j=k\).

More sharply, exponent order is definable without parameters:
\[
x\prec y
\quad\Longleftrightarrow\quad
P(x)\wedge P(y)\wedge x\ne y\wedge
\exists z\bigl(P(z)\wedge R(x,z,y)\bigr).
\]
Indeed, for powers \(a^i,a^j\) (with \(a=d\) or \(a=t\)), there exists a power \(a^k\) satisfying \(a^ia^k=a^j\) exactly when \(i\le j\); the inequality \(x\ne y\) makes this \(i<j\).

Therefore, taking \(a_i=d^i\) (or \(t^i\)) gives
\[
a_i\prec a_j\quad\Longleftrightarrow\quad i<j.
\]
The formula defining \(\prec\) has the order property, so both theories are unstable. Combining this with Hawthorne's NIP theorems gives the strict classification
\[
\boxed{T_d\text{ is NIP but unstable for every }d\ge2}
\]
and
\[
\boxed{S_p\text{ is NIP but unstable for every prime }p\ge7}.
\]

## Why this is useful

Hawthorne's examples are presented as tame NIP expansions obtained by adding multiplication only on an exponentially sparse set. The observation above places them exactly on the unstable side of the stability/NIP boundary: the restricted multiplication does not merely remain tame enough for NIP, it already reconstructs the ordered additive monoid of exponents on the sparse set.

This also gives a simple conceptual explanation for the instability. No interaction with the ambient addition is needed: the restricted multiplication graph alone defines exponent order.

## Relationship to prior work

Hawthorne's *Automata and tame expansions of \((\mathbb Z,+)\)* proves the NIP statement for the integer family, and *Contributions to the theory of \(F\)-automatic sets* proves the polynomial-ring statement for primes \(p\ge7\). His thesis gives a unified presentation of the two restricted-multiplication constructions (with the polynomial theorem stated there in the earlier \(p\ge9\) form).

The present deduction is not a new NIP theorem. Its contribution is the complementary sharp lower-bound classification: these NIP examples are provably not stable, witnessed by an explicit parameter-free order formula on the sparse power sort.

Targeted searches for the paper titles together with “unstable,” “order property,” “strictly NIP,” “Presburger,” and the restricted-multiplication notation did not locate this explicit conclusion. The deduction is short and may be folklore; that is the main originality risk.

## Source anchors

- Christopher D. C. Hawthorne, *Automata and tame expansions of \((\mathbb Z,+)\)*, arXiv:2007.00070; first submitted 30 June 2020; primary MSC 03C45.
- Christopher Hawthorne, *Contributions to the theory of \(F\)-automatic sets*, arXiv:2011.12405; first submitted 24 November 2020; published in *The Journal of Symbolic Logic*; primary MSC 03C45.
- Hawthorne's 2021 thesis *A guide to F-automatic sets* gives a full-text unified treatment of the restricted-multiplication constructions.

## Limitations

The instability argument is elementary once the restricted multiplication graph is present, so uncatalogued folklore is a real possibility. The \(p\ge7\) bound is inherited entirely from Hawthorne's NIP theorem; this observation does not improve it. It also does not determine finer NIP invariants such as dp-rank.
