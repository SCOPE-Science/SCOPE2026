# Ordinal-block normal form for the infinite-accumulation modality on Alexandrov chains

## Finding

Fix any ordinal \(\theta\), and put \(X_\theta=\{\beta:\beta<\theta\}\) with the Alexandrov topology of all ordinal initial segments (all downward-closed subsets). Let
\[
\mathsf D(A)=\{\beta<\theta: |A\cap(\beta+1)|\ge\aleph_0\}
\]
be the infinite-accumulation operator. This is precisely the interpretation of the purely nonstandard halo diamond of Montacute (2026), applied to a truth set \(A\) on this space.

**Complete one-step normal form.** If \(A\subseteq X_\theta\) is finite, then \(\mathsf D(A)=\varnothing\). Otherwise, list its first \(\omega\) members in strictly increasing order as \((a_n)_{n<\omega}\), and put \(\delta(A)=\sup_{n<\omega}(a_n+1)\). Then
\[
\boxed{\mathsf D(A)=[\delta(A),\theta).}
\]
Here \([\eta,\theta)=\{\beta<\theta:\beta\ge\eta\}\), understood as empty if \(\eta\ge\theta\).

**Every transfinite iterate.** Set \(\mathsf D^0(A)=A\), \(\mathsf D^{\alpha+1}(A)=\mathsf D(\mathsf D^\alpha(A))\) and \(\mathsf D^\lambda(A)=\bigcap_{\alpha<\lambda}\mathsf D^\alpha(A)\) at nonzero limits. For infinite \(A\), the precise formulas are
\[
\boxed{\mathsf D^n(A)=[\delta(A)+\omega\cdot(n-1),\theta)\quad(1\le n<\omega),}
\]
\[
\boxed{\mathsf D^\alpha(A)=[\delta(A)+\omega\cdot\alpha,\theta)\quad(\alpha\ge\omega).}
\]
For finite \(A\), all positive iterates are empty.

**Exact rank spectrum.** Taking \(A=X_\theta\) gives, for all ordinals \(\alpha\),
\[
\boxed{\mathsf D^\alpha(X_\theta)=[\omega\cdot\alpha,\theta).}
\]
Consequently its extinction rank, defined as the least \(\rho\) with \(\mathsf D^\rho(X_\theta)=\varnothing\), is
\[
\boxed{\rho(\theta)=\min\{\gamma:\omega\cdot\gamma\ge\theta\}.}
\]
The space is always \(\omega\)-scattered (its greatest \(\omega\)-perfect subset is empty). Every nonzero countable ordinal \(\gamma\) is the rank of a countable \(T_0\) Alexandrov chain, for example \(X_{\omega\cdot\gamma}\). The least ordinal \(\theta\) realizing \(\gamma\) is \(\omega\cdot\eta+1\) when \(\gamma=\eta+1\) is a successor, and \(\omega\cdot\gamma\) when \(\gamma\) is a nonzero limit.

The point \(\beta<\theta\) disappears at precisely the first stage \(\gamma\) satisfying \(\omega\cdot\gamma>\beta\). Thus the \(\omega\)-accumulation modality has an exact transfinite, pointwise ordinal-block normal form on these spaces.

## Assumptions and scope

An ordinal is identified with its set of predecessors. Open sets in \(X_\theta\) are exactly the downward-closed subsets of \(\theta\), not the usual Hausdorff order topology. This topology is Alexandrov and \(T_0\), and is non-\(T_1\) whenever \(\theta\ge2\). The smallest open neighbourhood of \(\beta\) is \([0,\beta]\). All ordinal sums/products are ordinary (noncommutative) ordinal operations; \(\omega\cdot\gamma\) means multiplication on the **left** by \(\omega\).

No choice of atomic valuation is assumed for the first normal form: it holds for **every** \(A\subseteq X_\theta\). Countability is needed only for the realization claim about countable spaces; the normal forms hold for arbitrary \(\theta\). This is a statement about the infinite-accumulation operator and its transfinite iterations, not a claim about the validity theory of every formula of a larger bimodal language.

## Proof

**1. Neighbourhood reduction.** Every open neighbourhood of \(\beta\) contains its least open neighbourhood \([0,\beta]\). Hence \(\beta\in\mathsf D(A)\) if and only if \(A\cap[0,\beta]\) is infinite. This proves the displayed defining formula directly. Montacute's Theorem 6.4 identifies this operator with the nonstandard-halo diamond.

**2. First infinite block.** If \(A\) is infinite, its inherited ordinal well-order has a unique first strictly increasing sequence \(a_0<a_1<\cdots\) of length \(\omega\). Set \(\delta=\sup_n(a_n+1)\). For \(\beta<\delta\), some \(a_n>\beta\), so at most the first \(n\) members of \(A\) can lie at or below \(\beta\); the intersection is finite. For \(\beta\ge\delta\), all the \(a_n\) lie below \(\beta\), so the intersection is infinite. This is the claimed one-step tail. If \(\delta=\theta\), the tail is empty, as required. Finite \(A\) has no infinite intersection with any neighbourhood.

**3. Tail step.** For any \(\eta\le\theta\), the first \(\omega\) members of a nonempty tail \([\eta,\theta)\) exist exactly when \(\eta+\omega\le\theta\), and are \(\eta+n\), for \(n<\omega\). Their supremum is \(\eta+\omega\). If the tail is shorter than \(\omega\), or absent, its derivative is empty; the same closed formula therefore applies in all cases:
\[
\mathsf D([\eta,\theta))=[\eta+\omega,\theta).
\]
For \(\eta>\theta\), both sides are empty as well.

**4. Transfinite induction.** Apply the tail step after the first derivative. At each finite successor, the threshold gains \(\omega\); associativity gives \(\delta+\omega\cdot(n-1)\). At the first limit,
\[
\bigcap_{1\le n<\omega}[\delta+\omega\cdot(n-1),\theta)
=[\delta+\omega\cdot\omega,\theta),
\]
because right ordinal multiplication and right ordinal addition are continuous at increasing limits. At every later successor, add \(\omega\); at every later limit, take the supremum of prior thresholds. This yields \([\delta+\omega\cdot\alpha,\theta)\) for every \(\alpha\ge\omega\), including thresholds already beyond \(\theta\). The equality between intersection of tails and the tail from their supremum also holds when the supremum exceeds \(\theta\), because all sets involved are empty beyond the endpoint.

**5. Full-space and rank formulas.** If \(\theta\le\omega\), the full space has no infinite initial segment within \(\theta\), so \(\mathsf D(X_\theta)=\varnothing\); the stated formula holds. For \(\theta>\omega\), the first \(\omega\) members are the finite ordinals, and \(\delta(X_\theta)=\omega\). For finite \(n\ge1\), the threshold is \(\omega+\omega(n-1)=\omega n\); at infinite \(\alpha\), it is \(\omega+\omega\alpha=\omega(1+\alpha)=\omega\alpha\). At stage \(0\), \([0,\theta)=X_\theta\). The thresholds are strictly increasing, so there is no nonempty fixed stage; the first stage with threshold at least \(\theta\) is exactly \(\rho(\theta)\). The greatest \(\omega\)-perfect subset must be contained in every iterate, hence is empty.

**6. Sharp countable spectrum.** For each nonzero countable \(\gamma\), the ordinal \(\omega\gamma\) is countable and \(\omega\beta<\omega\gamma\) whenever \(\beta<\gamma\), giving \(\rho(\omega\gamma)=\gamma\). If \(\gamma=\eta+1\), the least ordinal above \(\omega\eta\) is \(\omega\eta+1\), and it has extinction rank \(\gamma\); any smaller \(\theta\) has rank at most \(\eta\). If \(\gamma\) is a limit, \(\omega\gamma=\sup_{\beta<\gamma}\omega\beta\); every smaller \(\theta\) lies below some \(\omega\beta\), hence has rank less than \(\gamma\). Thus \(\omega\gamma\) is least at a nonzero limit. Point-removal stages follow immediately from the full-space formula.

## Verification

The accompanying `checker.py` tests an independent **finite-threshold analogue**: replace “infinite” by “at least \(m\)” for \(m\ge2\) on all finite ordinal initial-segment spaces of sizes at most ten. Direct neighbourhood evaluation agrees with the predicted first-hit threshold and every finite iterate for all tested subsets. It also checks the resulting finite extinction-rank formula for larger finite chains. This does **not** certify transfinite ordinal arithmetic or constitute a finite proof of the infinite claim; all transfinite statements follow from the explicit induction above.

Useful hand-checks: on \(X_{\omega^2}\), exactly \(\omega\) derivative stages are required; on \(X_{\omega^2+1}\), one additional stage is required. On \(X_{\omega+1}\), the first derived set is the singleton \(\{\omega\}\) and the second is empty. The distinction between the Alexandrov initial-segment topology and the familiar ordinal order topology is essential.

## Relationship to prior work

Montacute (2026), Theorem 6.4, identifies the nonstandard halo operator with \(\omega\)-accumulation; Theorem 6.14 supplies the general transfinite decomposition and the existence of a largest perfect kernel. The paper does not compute the derivatives, their exact point ranks, or their closure ordinals for these Alexandrov ordinal chains. The present proof uses those definitions but is independent of nonstandard-analysis machinery.

Classical Cantor–Bendixson ordinal ranks on **Hausdorff order-topological ordinals** are older (see Kechris 1995 and the Mazurkiewicz–Sierpiński classification). They imply neither the initial-segment Alexandrov formula \([\omega\alpha,\theta)\) nor its first-\(\omega\)-block normal form for arbitrary valuations. In particular, the new calculation should not be confused with classical Cantor–Bendixson ranks in the order topology. Other purely finite Alexandrov spaces have identically empty infinite-accumulation images, as noted already by Montacute.

## Limitations

This is an exact calculation on a **canonical family of linearly ordered Alexandrov spaces**, not on arbitrary non-\(T_1\) topologies. The rank spectrum statement by itself is not claimed as novel among arbitrary scattered spaces; the specific ordinal-multiplication normal form and canonical non-\(T_1\) chain realizations are the subject. The possibility of an older equivalent derivation under 'condensation derivative', 'infinite derived set' or Alexandrov-order terminology remains a literature-priority risk. There is no independent audit.

## References

1. Yoàv Montacute, *Halo Semantics for Modal Logic*, arXiv:2606.31885v1 (publicly posted 2026-06-30), EPTCS 447 (2026), 623–635, DOI:10.4204/EPTCS.447.35; accessible full text: https://www.researchgate.net/publication/408300250_Halo_Semantics_for_Modal_Logic .
2. Alexander S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, for classical Cantor–Bendixson terminology and ranks.
3. Mazurkiewicz–Sierpiński classification of countable compact order-topological spaces, recalled in the literature on Cantor–Bendixson ranks; comparison only, not used in the proof.
