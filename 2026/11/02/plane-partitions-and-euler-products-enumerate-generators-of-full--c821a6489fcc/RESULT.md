# Plane partitions and Euler products enumerate generators of full transformation endomorphism monoids

## Finding

Write \(\mathcal T_n\) for the full transformation monoid on an \(n\)-element set and \(\mathcal E_n=\operatorname{End}(\mathcal T_n)\) for its semigroup endomorphism monoid; homomorphisms are not required to preserve the identity. For every integer \(n\ge5\), the minimum cardinality \(d_n\) of a generating set of \(\mathcal E_n\) is given by an explicit integer-partition/plane-partition Euler product:

\[
 d_n=3+[z^n]\left\{\operatorname{MSET}(B)(z)-\operatorname{MSET}(B_0)(z) +\prod_{j\ge1}(1-z^j)^{-j}-\prod_{j\ge1}(1-z^j)^{-1}\right\},
\]

where, with formal power series over the integers,

\[
 U(z)=\frac z{1-z},\quad P(z)=\prod_{j\ge1}(1-z^j)^{-1},\quad H(z)=\prod_{j\ge2}(1-z^j)^{-\lfloor j/2\rfloor},\quad B_0(z)=U(z)P(z),\quad B(z)=U(z)P(z)H(z),
\]

and the unlabelled multiset Euler transform is defined for a zero-constant-term series \(F\) by

\[
 \operatorname{MSET}(F)(z)=\exp\left(\sum_{k\ge1}\frac{F(z^k)}k\right).
\]

More precisely, in the notation of Gould–Grau–Johnson, the exact numbers of essential rank-two orbits and rank-three orbits are

\[
 r_2(n)=[z^n]\left(\prod_{j\ge1}(1-z^j)^{-j}-P(z)\right),\qquad
 r_3(n)=[z^n]\big(\operatorname{MSET}(B)-\operatorname{MSET}(B_0)\big),
\]

so \(r_2(n)\) is the number of plane partitions of \(n\) minus the number of ordinary partitions of \(n\). The first values \((d_5,\ldots,d_{12})\) are \((35,86,207,503,1206,2880,6808,15996)\).

## Assumptions and scope

All transformations are total maps of a finite set to itself. The coefficient operator \([z^n]\) acts on formal power series; every infinite product and exponential is coefficientwise well-defined because all nonconstant component generating series begin in positive degree. A rank here is the cardinality of the image of an **endomorphism** of \(\mathcal T_n\), not the image size of an underlying transformation. The statement for the generating rank \(d_n\) is restricted to \(n\ge5\): at \(n=4\), exceptional endomorphisms of rank seven require a separate analysis. The two generating functions also enumerate the indicated admissible-pair conjugacy orbits for positive \(n\), but this does not assert the same minimal-generator formula in exceptional dimensions.

The starting structural theorems are from Gould–Grau–Johnson (2023 preprint, subsequently published), especially their Sections 2 and 4: singular endomorphisms are indexed uniquely by permissible pairs \((t,e)\) satisfying \(t^3=t\), \(e^2=e\), \(te=et=e\); the symmetric group acts by simultaneous conjugation; rank three corresponds to \(t^2\ne t\), rank two to \(t^2=t\ne e\); and their Proposition 4.2 gives \(d_n=3+r_3(n)+r_2(n)\) for \(n\ge5\). The contribution proved below is the explicit enumeration of both orbit quantities.

## Proof

**1. Functional components.** From \(t^3=t\), every directed functional component of \(t\) is either a fixed-point root with a set of direct leaves, or a two-cycle with leaves attached directly to its two core vertices. There are no longer cycles or deeper trees. The relation \(te=e\) makes \(e\) constant on each such blue component, while \(et=e\) forces its image into the fixed points of \(t\). Since \(e^2=e\), each red fiber \(e^{-1}(r)\) contains exactly one distinguished red-fixed vertex \(r\), itself a blue-fixed vertex.

**2. A red fiber is a multiset of components.** Its distinguished blue star (root \(r\) and any number of leaves) contributes \(U(z)=z/(1-z)\). Every additional blue star contributes the same series \(U\) and is unordered, so the collection of additional stars has generating series \(P(z)=\prod_{j\ge1}(1-z^j)^{-1}\). For a blue two-cycle of total size \(j\ge2\), the attachment sizes to the two core vertices are a nonnegative unordered pair summing to \(j-2\). The number of its isomorphism types is exactly \(\lfloor j/2\rfloor\). Arbitrarily many such components therefore contribute \(H(z)=\prod_{j\ge2}(1-z^j)^{-\lfloor j/2\rfloor}\). Consequently one red fiber is counted by \(B=UPH\). In the absence of two-cycles it is counted by \(B_0=UP\). Different red fibers are themselves unordered, whence the standard multiset Euler transform gives \(\operatorname{MSET}(B)\) and \(\operatorname{MSET}(B_0)\) respectively. Subtracting counts precisely the conjugacy orbits with a two-cycle. By the rank-three criterion, their number is \(r_3(n)\). The red-distinguished root makes this decomposition canonical, so no unlabeled symmetries have been omitted or counted twice.

**3. Characterization of essential rank-two orbits.** Consider a rank-two admissible pair \((t,e)\), so \(t^2=t\ne e\), and only blue stars remain. A rank-two orbit is nonessential exactly when it is obtained as \((u^2,e)\) from a rank-three admissible pair \((u,e)\). Indeed, Gould–Grau–Johnson's multiplication formula shows that this is the only way products of strictly higher-rank endomorphisms can produce a rank-two image, and for \(n\ge5\) a suitable even-permutation-type rank-three left factor exists (take two disjoint transpositions and a fixed point), so every such \((u^2,e)\) is produced.

A two-cycle of \(u\) becomes two distinct fixed roots in \(u^2=t\); both belong to one red fiber and neither can be its red-fixed root, because \(eu=e\) forces that distinguished vertex to be fixed by \(u\). Therefore a nonessential rank-two pair has at least two **additional** blue stars in one red fiber. Conversely, choose two additional blue-star roots \(a,b\) in one red fiber, swap them under \(u\), and for every leaf \(x\) with \(t(x)=a\) or \(b\), set \(u(x)\) to the *opposite* core root. Set \(u=t\) on all other components. Then \(u^3=u\), \(u^2=t\), \(ue=eu=e\), and \(u\) contains a two-cycle. This proves the converse and the equivalence.

Thus an essential rank-two pair has at most **one** additional blue star in each red fiber. Such a fiber is counted by \(U(1+U)=z/(1-z)^2\), whose coefficient of \(z^j\) is \(j\): one choice with no additional star, or \(j-1\) ordered splits into sizes of the distinguished and nondistinguished stars. Taking an unordered multiset of fibers gives

\[
 \operatorname{MSET}\left(\frac z{(1-z)^2}\right)=\prod_{j\ge1}(1-z^j)^{-j}.
\]

The rank-one pairs are those with no additional blue star anywhere (equivalently \(t=e\)). Their red fibers have generating function \(U\), so their orbit series is \(\operatorname{MSET}(U)=P(z)\). Removing these yields the formula for \(r_2(n)\).

**4. Minimal generator count and an exact recurrence.** Substituting the two orbit formulas into Proposition 4.2 of the cited paper gives the formula for \(d_n\), for every \(n\ge5\). For effective computation, if \(b_m=[z^m]B(z)\) and \(A_n=[z^n]\operatorname{MSET}(B)\), then \(A_0=1\) and

\[
 nA_n=\sum_{k=1}^{n}A_{n-k}\sum_{d\mid k}d\,b_d.
\]

The identical recurrence applied to \(B_0\) gives \(A_n^{(0)}\), and \(r_3(n)=A_n-A_n^{(0)}\). This follows by taking the logarithmic derivative of the defining Euler transform, so it is an exact integer recurrence without enumeration of labeled transformations.

## Verification

The included scripts `artifacts/orbit_formulas.py` and `artifacts/verify_essential.py` are ordinary Python 3 programs using only the standard library. Execute them from the directory containing the `artifacts` folder:

```sh
python3 artifacts/orbit_formulas.py
python3 artifacts/verify_essential.py
```

The first script independently computes the Euler transforms and exhaustively constructs and simultaneously conjugates all admissible pairs on sets with at most five elements. The second enumerates all admissible pairs of sizes five and six, explicitly tests the square relation to rank-three parents, and counts simultaneous-conjugacy orbits of essential rank-two and rank-three pairs. The independent tests give respectively \((r_2(5),r_3(5))=(17,15)\) and \((r_2(6),r_3(6))=(37,46)\). These checks are finite corroboration, not a substitute for the all-\(n\) proof above.

## Relationship to prior work

Gould, Grau and Johnson prove the structural admissible-pair description, classify ranks, identify essential orbits and reduce the minimum generator size to \(3+r_3(n)+r_2(n)\) in their Proposition 4.2. At the end of their Section 4 they explicitly give an unlabelled two-coloured functional graph sketch for enumerating these quantities but do not derive the formulas. Grau's 2023 doctoral thesis also discusses the enumeration as a subsequent problem. The formulas above complete that reduction; the underlying pair classification and generator-rank reduction are **not** claimed as new.

Krattenthaler and Müller enumerate labeled solutions of certain transformation-semigroup equations, including systems of commuting idempotents. Their enumerated objects are not the orbits of compatible tripotent-idempotent pairs, and their conclusions do not directly supply the essential-orbit count or this minimal-generator formula. The fact that the rank-two result is a difference of classical plane- and ordinary-partition numbers does not itself establish prior coverage of this particular semigroup interpretation.

## Limitations

The result gives exact counts and a coefficient recurrence, not a closed elementary expression or asymptotic expansion for the rank-three coefficient sequence. It does not cover the exceptional generating-rank cases \(n\le4\), nor does it claim to classify all minimal generating sets up to equivalence. Comprehensive priority across all formulations of simultaneous-map orbit enumeration cannot be proved by a finite literature search; further equivalent enumeration under a different name remains possible. The theorem's correctness is reviewed but it has not undergone independent mathematical audit.

## References

1. V. Gould, A. Grau, M. Johnson, “The structure of \(\operatorname{End}(\mathcal T_n)\),” arXiv:2307.11596 (first submitted 21 July 2023), especially Theorem 2.1, Corollary 2.4, Proposition 4.2 and the unlabelled-coloured-graph discussion following Proposition 4.2. https://arxiv.org/abs/2307.11596
2. A. Grau, “Aspects of endomorphism monoids of certain algebras,” doctoral thesis, University of York, 2023, section on \(\operatorname{End}(\mathcal T_n)\) and further considerations. https://etheses.whiterose.ac.uk/id/eprint/33804/
3. C. Krattenthaler, T. Müller, “Equations in finite semigroups: explicit enumeration and asymptotics of solution numbers,” arXiv:math/0303028 (2003). https://arxiv.org/abs/math/0303028
