# Congruence-lattice normal form and rarity laws for layered temporal Heyting algebras

## Finding

Fix an integer \(n\geq1\). Consider **loop-decorated layered temporal transits** on a labelled \(n\)-element set: the underlying order is an ordinal sum \(P=L_1\oplus\cdots\oplus L_h\) of nonempty antichains; the transit relation consists of all strict order pairs and the reflexive loops at the selected points \(F_i\subseteq L_i\). Let \(A(P,F)\) be its finite temporal Heyting algebra of upsets, with the adjoint temporal operations induced by this relation and its inverse, as in Alvarez [1].

**Congruence-lattice normal form.** The congruence lattice of \(A(P,F)\) is order-isomorphic to the reverse-inclusion poset of the following explicitly described subsets: the empty set, and each
\[
S_{j,T}=T\cup\bigcup_{i>j}L_i,\qquad 1\leq j\leq h,\quad\varnothing\ne T\subseteq L_j,
\]
for which both
\[
(j=1\ \text{or}\ T\subseteq F_j),\qquad
(j=h\ \text{or}\ T=L_j\ \text{or}\ F_{j+1}=L_{j+1})
\]
hold. Distinct pairs \((j,T)\) give distinct sets. These are precisely the *archival upsets* of the transit, so the congruence correspondence itself is the one proved in [1]. No additional congruences occur.

**Simple and subdirectly-irreducible criteria.** For \(h\geq2\), the algebra is simple exactly when
\[
F_h=\varnothing\quad\text{and}\quad F_i\ne L_i\ \text{for every }2\leq i<h.
\]
It is subdirectly irreducible exactly when \(|L_1|=1\) or \(F_2\ne L_2\). For \(h=1\), either property holds exactly when \(|L_1|=1\). Loops on the bottom level do not affect simplicity for \(h\geq2\).

**Exact labelled and unlabelled censuses.** Put
\[
U(z)=e^{2z}-1,\quad V(z)=e^{2z}-e^z,\quad W(z)=e^z-1.
\]
The exponential generating functions of all, simple, and subdirectly-irreducible labelled transits, respectively, are
\[
\boxed{T(z)=\frac{U(z)}{1-U(z)},\quad
S(z)=2z+\frac{U(z)W(z)}{1-V(z)},\quad
I(z)=2z+\frac{2zU(z)+(U(z)-2z)V(z)}{1-U(z)}.}
\]
An isomorphism type is a list of pairs \((|L_i|,|F_i|)\). Accordingly, replace \(U,V,W\), respectively, by
\[
u(z)=\frac{z(2-z)}{(1-z)^2},\qquad
v(z)=\frac{z}{(1-z)^2},\qquad
w(z)=\frac{z}{1-z}
\]
in these formulas to obtain the ordinary generating functions \(\bar T,\bar S,\bar I\) for unlabelled types (the isolated \(2z\) terms remain unchanged).

For \(1\leq n\leq8\), the labelled sequences \((T_n),(S_n),(I_n)\) are, in order,
\[
\begin{aligned}
(T_n)&=(2,12,104,1200,17312,299712,6053504,139733760),\\
(S_n)&=(2,4,30,256,2670,33304,484470,8054176),\\
(I_n)&=(2,8,84,1032,15080,261556,5283964,121972976).
\end{aligned}
\]
The unlabelled sequences are
\[
\begin{aligned}
(\bar T_n)&=(2,7,24,82,280,956,3264,11144),\\
(\bar S_n)&=(2,2,7,20,54,143,376,986),\\
(\bar I_n)&=(2,4,17,64,227,786,2697,9224).
\end{aligned}
\]

**Sharp frequency contrast.** Let \(\rho=(\log2)/2\), \(\phi=(1+\sqrt5)/2\), and \(\sigma=\log\phi\). Under the uniform distribution on all labelled loop-decorated layered transits, as \(n\to\infty\),
\[
\boxed{\frac{S_n}{T_n}\sim\frac4{\phi+2}\left(\frac\rho\sigma\right)^{n+1},\qquad
\frac{I_n}{T_n}\longrightarrow 2-\sqrt2+(\sqrt2-1)\log2.}
\]
The decay ratio \(\rho/\sigma\) is approximately \(0.7202100452\); the subdirectly-irreducible limiting share is approximately \(0.8728974005\). Thus simplicity is exponentially rare, while subdirect irreducibility retains a positive limiting frequency.

## Assumptions and scope

All carriers are finite and nonempty. All levels are nonempty antichains, ordered strictly from bottom to top. The forward relation \(R\) contains exactly every strict comparable ordered pair, plus a chosen set of loops; the backward relation is \(R^{-1}\). These data define finite temporal Esakia spaces with the discrete topology, hence temporal Heyting algebras via [1, Definitions 3–6 and Theorem 1]. The counts are of **this restricted family**, not of arbitrary finite temporal Heyting algebras. In the labelled counts the world labels are fixed; distinct orders or distinct loop sets count separately. In the unlabelled counts, isomorphisms preserve the order and temporal relation, so the level-size/reflexive-count sequence is a complete invariant.

## Proof

**1. Archival-upset classification.** Every nonempty order upset has a unique least occupied layer \(L_j\), meets it in a nonempty \(T\subseteq L_j\), and contains every higher layer. Hence it has the displayed form. Proposition 2 of [1] says that an upset is archival if and only if for every comparable pair \(x<z\), with \(x\) outside and \(z\) inside the upset, some **reflexive point of the upset** lies between \(x\) and \(z\), endpoints allowed.

When \(j>1\), take \(x\in L_{j-1}\) and \(z\in T\). The only point of the interval lying in the upset is \(z\), so each \(z\in T\) must be reflexive: \(T\subseteq F_j\). This restriction disappears at \(j=1\). If \(j<h\) and \(T\ne L_j\), take \(x\in L_j\setminus T\) and \(z\in L_{j+1}\). The only reflexive candidate in the interval that lies in the upset is \(z\), so the entire next level must be reflexive: \(F_{j+1}=L_{j+1}\). Otherwise this second condition is vacuous. Conversely, for any comparable crossing pair, either its lower endpoint lies below \(L_j\), in which case the first restriction supplies a reflexive witness in the first included level (or the upper endpoint itself); or its lower endpoint lies in \(L_j\setminus T\), in which case the second restriction supplies a reflexive point in the next included level. If the first included level equals the bottom level, lower-endpoint crossings can only begin in its omitted subset; if it is the last level, none can begin there and end above. This proves both necessity and sufficiency.

Theorem 2 of [1] identifies the congruence lattice with the reverse-inclusion poset of closed archival upsets. Every subset is closed in a finite discrete space, establishing the complete normal form, including the congruence order, without assuming a new general congruence correspondence.

**2. Simple and subdirectly-irreducible cases.** The whole carrier and the empty set are always archival. Simplicity means these are the only archival upsets. For \(h\ge2\), any nonempty proper archival upset can first occur in a level \(j\ge2\) with a nonempty reflexive subset, or at \(j=1\) with a proper \(T\), the latter requiring the whole second level to be reflexive. If the top level has a reflexive point, its singleton upper upset is archival; if some intermediate level is fully reflexive, its full upper suffix is archival; conversely if the top level has no reflexive point and all intermediate levels contain a loopless point, the normal form excludes all proper nonempty archival upsets. (When the second level is fully reflexive, it is an intermediate level if \(h>2\), and its nonempty proper lower-level upsets are also caught.) This gives the stated criterion; for \(h=1\) every subset is archival, so simplicity holds just for a singleton.

A nontrivial finite algebra is subdirectly irreducible precisely when its congruence lattice has a unique smallest nonidentity element, equivalently the archival-upset family has a **unique maximal proper subset**. If \(|L_1|>1\) and \(F_2=L_2\), the \(|L_1|\) different upsets obtained by deleting one first-level point from the carrier are distinct maximal proper archival subsets, so it is not subdirectly irreducible. Otherwise, no two such maximal proper first-level upsets exist: when \(|L_1|=1\), none can be proper with nonempty first-level trace; when \(F_2\ne L_2\), the normal form excludes all proper archival upsets meeting the first level. The remaining nonempty proper archival upsets are nested across their earliest occupied levels, and at each level the admissible traces are either all nonempty subsets of a single reflective set \(F_j\) or just the full level. Thus the family has one maximal proper element whenever it is nonempty; when it is empty the algebra is simple and hence subdirectly irreducible. The one-level case is immediate.

**3. Generating functions.** In labelled exponential generating functions, an unrestricted nonempty level with an arbitrary choice of reflective points contributes \(U=e^{2z}-1\); a nonempty level with at least one loopless point contributes \(V=e^{2z}-e^z\); and a nonempty entirely loopless level contributes \(W=e^z-1\). An arbitrary nonempty ordered list of levels contributes \(U/(1-U)\). A simple frame is either one single world with either loop status (term \(2z\)), or a bottom unrestricted level, any number of intermediate levels of type \(V\), and a top level of type \(W\). This gives \(S\). An irreducible frame with at least two levels either has a singleton bottom level (term \(2zU/(1-U)\)) or a nonsingleton bottom level followed by a level with at least one loopless point and arbitrary higher levels (term \((U-2z)V/(1-U)\)); include the singleton frame \(2z\). This gives \(I\). Replacing exponential level weights with the ordinary weights \(u=\sum_{a\ge1}(a+1)z^a\), \(v=\sum_{a\ge1}az^a\), and \(w=\sum_{a\ge1}z^a\) gives the unlabelled formulas.

**4. Asymptotics.** The unique dominant pole of \(T=U/(1-U)\) is at \(\rho\) with local principal part \(1/[4(\rho-z)]\). The unique dominant pole of \(S-2z=UW/(1-V)\) is at \(\sigma\), since \(e^{2\sigma}-e^\sigma=1\), with principal part \(1/[(\phi+2)(\sigma-z)]\). The other complex poles have strictly larger modulus in each case. Comparing coefficients gives the displayed simple-to-total ratio. In \(I\), the pole at \(\rho\) has the same denominator as \(T\), and the ratio of pole numerators is \(2\rho+(1-2\rho)(2-\sqrt2)=2-\sqrt2+(\sqrt2-1)\log2\). Coefficient asymptotics give the second limit.

## Verification

Run the included `checker.py` with Python 3 and the standard library: `python3 checker.py`. It uses three complementary finite procedures. First, it independently enumerates **every** labelled layered transit with at most five worlds (17,312 at exactly five), computes every upset, directly tests the finite archival witness condition, and compares that family to the stated normal form. It then independently computes the temporal reachability relation and the congruence-theoretic simple/subdirectly-irreducible predicates, checking agreement. Finally, for sizes one through eight it compares ordered-composition formulas against exact rational generating-series coefficients and counts orbits through level-size/reflexive-count signatures. The last output line is `ALL_CHECKS_OK` when all assertions pass. This exhaustiveness applies only to the finite checked sizes; the all-size claims rest on the proof above.

## Relationship to prior work

Alvarez [1] develops the temporal-Heyting duality, establishes the congruence/archival-upset correspondence (Theorem 2), provides the finite interval-witness criterion (Proposition 2), and gives general simple/subdirectly-irreducible characterizations. Those broad theorems are premises explicitly used here, **not claimed as new**. The present contribution is an explicit complete congruence poset for loop-marked ordinal sums of antichains and its exact labelled/unlabelled censuses and asymptotic contrast. The unrestricted total labelled count \(2^n\) times the ordered-Bell number is known and serves as a check, not an originality claim [2]. An earlier incidence-temporal-transit congruence classification treats graph-incidence posets of height two via a graph contraction and downset lattice; its sparse incidence structures and lack of an all-size layered census do not imply these formulas. The counts of ordinary maps between finite weak orders address a different mapping problem and do not imply these modal congruence criteria or rarity laws. No examined source supplies these precise enumerative formulas; this is not a proof of historical uniqueness.

## Limitations

The frame family is a strict subclass of all finite temporal transits. The generating functions do not enumerate arbitrary finite temporal Heyting algebras. The proof relies on the previously published general duality theorem and finite archival condition. The enumeration checker verifies finite instances only. Older equivalent results under another framing of loop-marked ordered partitions may exist; a full historical uniqueness claim would require a broader specialist literature audit. No independent audit or formal proof-assistant certification has been performed.

## References

[1] D. Q. Alvarez, *A dual characterisation of simple and subdirectly-irreducible temporal Heyting algebras with applications to the temporal Heyting calculus*, arXiv:2505.08014, first posted 12 May 2025, revised 16 June 2026, DOI:10.1007/s00012-026-00939-6. See Definitions 3–6, Theorem 2, and Proposition 2. https://arxiv.org/abs/2505.08014

[2] OEIS A216794, labelled ordered partitions with binary marks; the unrestricted total count is an existing sequence. https://oeis.org/A216794
