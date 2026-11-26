# The intermediate-palette forced-colouring polynomial of clique windmills

## Finding

Let \(r\ge3\) and \(m\ge2\) be integers. The labelled graph \(W=K_1\vee(mK_{r-1})\) consists of a hub and \(m\) blades, each a clique on \(r-1\) vertices. Write \(N=1+m(r-1)\). Fix an integer palette size **\(r<q\le N\)** and use \(q\) named colours. A blank vertex may take the unique missing colour when its coloured neighbours display exactly \(q-1\) distinct colours. A partial assignment succeeds if these steps can finish a proper total colouring. Write \(F_{r,m;q}(z)\) for the sum of \(z^{|\operatorname{dom}f|}\) over successful initial assignments \(f\).

For this intermediate palette,
\[
F_{r,m;q}(z)=qU_{r,m}(q)z^{N-1}+q\bigl((q-1)_{r-1}\bigr)^m z^N,
\qquad
U_{r,m}(q)=\sum_{j=0}^{q-1}(-1)^j\binom{q-1}{j}\bigl((q-1-j)_{r-1}\bigr)^m.
\]
Here \((a)_s\) is the falling factorial, zero for integers \(0\le a<s\). The first coefficient is positive throughout \(r<q\le N\). Exactly \(N-1\) initial vertices are needed for minimum-size success; any such domain omits only the hub, and the number of successful assignments on it is \(qU_{r,m}(q)\).

In Farr's independent model, a specified colour has probability \(p\), and a blank has probability \(1-qp\), where \(0\le p\le1/q\). The corresponding evaluation is
\[
\operatorname{FC}_q(W;p)=qU_{r,m}(q)p^{N-1}(1-qp)+q\bigl((q-1)_{r-1}\bigr)^m p^N.
\]

## Assumptions and scope

The blades are distinguished by their vertex sets; colour names are not quotiented by permutations. Initial colours cannot be changed. A successful assignment is necessarily proper on the vertices it initially colours. Proper total assignments succeed with no steps. The assertion is about local forcing, not uniqueness of an extension under a different rule. The claimed range is \(r<q\le N\); the chromatic palette formula and the generic no-forcing ranges are not part of the claimed contribution.

## Proof

Every non-hub vertex has degree \(r-1<q-1\), so no leaf can be forced, even after the hub receives a colour. All leaves must therefore be seeded. If the hub too is seeded, the assignment succeeds exactly when it is proper: choose a hub colour, then inject the \(r-1\) labelled vertices of each blade into the remaining \(q-1\) colours. This gives \(q((q-1)_{r-1})^m\) assignments.

Otherwise the hub is the only blank. It can be filled precisely when its neighbours collectively display \(q-1\) colours. Choose the absent colour in \(q\) ways. With this choice fixed, distribute the other \(q-1\) colours injectively on each blade and require every one of them to occur at least once. If a prescribed subset of \(j\) colours is unused, there are \(((q-1-j)_{r-1})^m\) blade assignments. Inclusion–exclusion gives \(U_{r,m}(q)\). The hub's forced colour is absent from all the leaves, so the step produces a proper colouring. There is no overcount: the completed hub colour is recovered as the unique colour missing from the seed.

For positivity put \(t=q-1\) and \(s=r-1\). Since \(s\le t\le ms\), the \(t\) colours can be partitioned into \(m\) groups of size at most \(s\), allowing empty groups. Put each group in one blade, then pad every blade to \(s\) with other colours from the same \(t\)-colour set, without repeats within a blade. Every colour occurs. Conversely, when \(t>ms\) there are too few leaves to display all \(t\) colours. In the claimed range the nonzero \(z^{N-1}\) term proves the minimum and multiplicity. The probability formula weights the size-\(N-1\) assignments by \(p^{N-1}(1-qp)\) and the size-\(N\) assignments by \(p^N\), including the endpoints.

## Verification

The standalone standard-library program `verify_intermediate.py` compares inclusion–exclusion with a recurrence that tracks the size of the union of colours used after each blade. If \(u\) colours are already used and the next size-\(s\) blade introduces \(j\) new colours, there are \(\binom{q-1-u}{j}\binom{u}{s-j}s!\) choices of its ordered colours. The program checks both the intermediate range and the vanishing of the hub-blank term immediately above it, for \(3\le r\le8\) and \(2\le m\le6\). For \(q=N\) it independently checks \(qU_{r,m}(q)=N!\), since all colours except the hub's must occur once on the leaves. The bounded comparison is not the proof of the formula.

## Relationship to prior work and limitations

Farr and Morgan, [arXiv:2406.15746v1](https://arxiv.org/abs/2406.15746v1), give the independent-assignment probability framework. Farr, [arXiv:2609.17108v1](https://arxiv.org/abs/2609.17108v1), gives the local rule and general identities: Proposition 4(a) handles \(q<\chi(W)\) and Proposition 5 handles \(q>\Delta(W)+1=N\). The proper-total term is also the ordinary chromatic term. The contribution here is the extra nonzero coefficient for the intermediate range and the resulting exact minimum count, not those generic identities.

The chromatic palette \(q=r\) is known for the same windmills: [Forced colouring polynomials of clique windmills](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-forced-colouring-polynomials-of-clique-windmills--c1051e120f18/RESULT.md) gives the complete seed-size polynomial and minimum there. It is also a specialization of the heterogeneous clique-bouquet formula in [Exact forcing polynomials and parity-sensitive real zeros for clique bouquets](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-exact-forcing-polynomials-and-parity-sensitive-real-zeros-for-cl--d80fcc5f6b79/RESULT.md). Those results are cited as antecedents, not as findings of this note. For comparison, the different exponent in the intermediate palette reflects a different mechanism: no leaf can be forced at all. A distinct later record, [A palette-driven two-step forcing threshold for clique windmills](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-palette-driven-two-step-forcing-threshold-for-clique-windmills--b3d5092b434e/RESULT.md), contains the same larger-palette enumeration. This bounded literature comparison does not determine publication priority. No heterogeneous-bouquet or general block-graph result is claimed.
