# Scientific assessment: exact cone-direction spectrum

## Correctness — PASS

The theorem uses the same supporting-base convention as Feldman's Lemma 8. For each cone apex all other extreme points lie on the associated base supporting hyperplane. Distinct directions therefore give distinct apexes, which are affinely independent because the base affine functionals isolate the apexes. If fewer than \(n+1\) apices occur, an extra extreme point lies on every base hyperplane, making their normals independent and giving a residual base of dimension \(n-k\). Residual dimensions zero and one would force a simplex, eliminating the counts \(n\) and \(n-1\). Explicit cross-polytopal pyramids realize all other counts. No analytic step depends on finite enumeration; SymPy exact-rank checks cover 35 illustrative finite cases.

## Originality — PASS, with remaining historical risk

Feldman's arXiv:2608.04516v1, Lemma 8, establishes only finiteness of the set of cone directions and explicitly presents the \(n+1\) bound and simplex-only equality as a conjecture. The primary text of Pineda-Villavicencio, Ugon, and Yost on multifold pyramids addresses their face counts and specialized free joins, not the supporting-direction spectrum of arbitrary compact convex bodies. Semantic searches for affine apices, cone directions, exact count, and pyramidal decompositions did not reveal a covering statement. A classical equivalent in older or unindexed pyramid literature remains possible; absence from search results is not a proof of global novelty.

## Mathematical value — PASS

The result resolves a specific conjecture printed in recent convex-geometric literature and determines the entire sharp numerical spectrum, including a two-value forbidden gap immediately below the simplex maximum. The intrinsic residual base theorem supplies a structural explanation and works for non-polyhedral convex bodies, beyond examples or a mere restatement of the conjectured inequality.

## Source comparisons and limits

Primary source: D. V. Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516v1 (August 5, 2026), Lemma 8 and §5, https://arxiv.org/html/2608.04516v1 . Its finiteness lemma does not imply the sharp count or nonsimplex gap. A further primary comparison is G. Pineda-Villavicencio, J. Ugon and D. Yost, *Lower bound theorems for general polytopes*, https://arxiv.org/pdf/1509.08218, §1; its relevant free-join discussion does not state the theorem. The classification concerns exact, not approximate, cone directions and does not improve centroid-overlap constants. Universal correctness is supported by the analytic proof, not the finite-rank checks.

Same-model review: passed. Independent audit: not yet performed.
