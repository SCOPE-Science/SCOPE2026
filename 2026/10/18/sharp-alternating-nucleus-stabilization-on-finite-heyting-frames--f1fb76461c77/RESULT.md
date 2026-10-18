# Sharp alternating-nucleus stabilization on finite Heyting frames

## Finding
For a nonempty finite poset \(P\) of height \(h\) (the maximum number of points in a chain), consider the Heyting algebra \(H(P)=\operatorname{Up}(P)\) of upward-closed subsets. Its nuclei are indexed by subsets \(S\subseteq P\) via
\[
j_S(U)=\{x\in P:\uparrow x\cap S\subseteq U\}.
\]
For arbitrary \(S,T\subseteq P\), put \(F=j_S\circ j_T\), composition from right to left, and \(C=S\cap T\). For every integer \(r\ge1\), the following are equivalent:

1. \(F^r=j_C\) as functions on all upsets.
2. For every nondecreasing sequence \(s_1\le t_1\le s_2\le t_2\le\cdots\le s_r\le t_r\), where each \(s_i\in S\) and each \(t_i\in T\), there exists \(c\in C\) satisfying \(s_1\le c\le t_r\).

Thus
\[
\left(j_S\circ j_T\right)^{\lfloor h/2\rfloor+1}=j_{S\cap T},
\]
and the exponent is optimal uniformly for **every** nonempty finite poset of height \(h\). In addition, the composition \(j_S\circ j_T\) is already a nucleus if and only if every comparable pair \(s\in S\), \(t\in T\), \(s\le t\), has a point of \(C\) in its order interval \([s,t]\).

## Assumptions and scope
All orders are finite, reflexive, antisymmetric and transitive. A nonempty poset has \(h\ge1\). \(U\) always denotes an upset; \(S\) and \(T\) are arbitrary subsets, not necessarily upsets. \(j_S\) is extensive, monotone, idempotent and preserves finite meets. The classical finite-poset indexing of nuclei by subsets is used (Lindenhovius; Ochs). The symbol \(F^r\) means \(r\)-fold **function** composition, not the pointwise lattice power. Paths are allowed to repeat comparable points; all displayed quantifiers are universal unless otherwise specified. The interval \([s,t]\) is \(\{c\in P:s\le c\le t\}\).

## Proof
**Composition expansion.** Directly from the definition, for any \(x\in P\),
\[
x\in (j_S\circ j_T)(U) \iff
\text{for every }s\in S,\ t\in T\text{ with }x\le s\le t,\ t\in U.
\]
Induction on \(r\) gives
\[
x\in F^r(U)\iff
\text{for every }x\le s_1\le t_1\le\cdots\le s_r\le t_r
\text{ of the stated colors, }t_r\in U.
\]
In particular, \(F^r(U)\subseteq j_C(U)\): for any \(c\in C\) above \(x\), use the constant alternating path consisting of \(c\).

**Exact bridge equivalence.** Suppose every alternating path admits a common-color point \(c\) between its endpoints. If \(x\in j_C(U)\), and a colored path begins above \(x\), then its bridge \(c\in C\) is in \(U\); the final point \(t_r\ge c\) lies in the upset \(U\). Thus \(x\in F^r(U)\), proving equality. Conversely, let a colored alternating path \(s_1\le t_1\le\cdots\le t_r\) have no common-color point between its endpoints. Set \(x=s_1\) and \(U=\uparrow(C\cap\uparrow s_1)\). Then \(x\in j_C(U)\) by construction, but \(t_r\notin U\), since any common-color generator below \(t_r\) would be the prohibited bridge. The given path witnesses \(x\notin F^r(U)\), contradicting equality. This proves both directions for every \(r\).

**Height bound.** Any sequence of \(2r\) comparable nondecreasing points with \(2r>h\) has two equal *adjacent* points, since otherwise all consecutive inequalities would be strict. Their successive colors are opposite, hence the equal point belongs to \(S\cap T\). It lies between \(s_1\) and \(t_r\). For \(r=\lfloor h/2\rfloor+1\), one has \(2r>h\), so the bridge equivalence proves the formula.

**Uniform sharpness.** For \(h\ge2\), let \(q=\lfloor h/2\rfloor\) and select a strict chain \(c_1<\cdots<c_h\). Define \(S=\{c_1,c_3,\ldots,c_{2q-1}\}\) and \(T=\{c_2,c_4,\ldots,c_{2q}\}\). These are disjoint. The sequence \(c_1\le c_2\le\cdots\le c_{2q}\) has the prescribed alternating colors but no bridge. Consequently \(F^q\ne j_\varnothing\). No smaller uniform exponent can suffice. If \(h=1\), all products stabilize after their first application, and the least permitted positive exponent is \(1\).

**One-step nucleus criterion.** The exact bridge equivalence at \(r=1\) says that \(F=j_C\) exactly when each comparable \(S\)-to-\(T\) pair admits an interval bridge. Such an \(F\) is a nucleus. Conversely, if \(F\) is itself idempotent then \(F^r=F\) for all \(r\ge1\); the universal height bound implies \(F=j_C\). Therefore this interval condition is necessary and sufficient for the product to be a nucleus.

## Verification
The included `verify.py` independently enumerates all labelled strict partial orders on \(1\) to \(4\) points, constructs their upsets and every indexed nucleus, computes both the compositional powers and the alternating-path bridge tests, and verifies the claimed equivalences. It checks \(242\) posets, \(57{,}332\) ordered pairs of nuclei, and \(120{,}468\) power/path identities, including the sharp height uniform bound. Run `python3 verify.py` in a standard Python 3 environment; no external package is required. These finite tests corroborate, but do not establish, the proof for unbounded \(h\).

## Relationship to prior work
Lindenhovius classifies nuclei over downset frames of Artinian posets using subsets; applying order duality yields the finite upset formula here. Ochs records a missing inverse correspondence formula. Escardó develops the general nuclear reflection of a prenucleus and the join of nuclei by composition and iteration. The eventual reflection is therefore **not** claimed to be novel. The result proved here is the finite-poset-specific exact alternating-path criterion, sharp uniform *height-dependent* number of iterations, and complete two-nucleus idempotence criterion. These are not the same as criteria for two nuclei to commute: a product can be a nucleus without its reverse composition agreeing. No general independent novelty certification is claimed.

## Limitations
The explicit exponent depends on the height of a **finite** poset and need not extend to infinite frames. The theorem is about alternating products of **two** nuclei, not arbitrary families or arbitrary prenuclei. The bridge test quantifies over paths; it does not assert a polynomial-time algorithm for every compressed poset representation. Prior general reflection results and possible equivalent descriptions in earlier closure-operator literature constrain any priority claim. No independent mathematical audit has been performed.

## References
1. Bert Lindenhovius, *Grothendieck topologies on a poset*, arXiv:1405.4408 (first public 2014-05-17), Appendix C, https://arxiv.org/abs/1405.4408.
2. Eduardo Ochs, *On a formula that is not in “Grothendieck Topologies in Posets”*, arXiv:2107.08501 (first public 2021-07-18), https://arxiv.org/abs/2107.08501.
3. Martín H. Escardó, *Joins in the Frame of Nuclei* (2003), especially Sections 1–3, https://martinescardo.github.io/papers/hmj.pdf.
