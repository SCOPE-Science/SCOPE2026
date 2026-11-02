# Scientific review

## Correctness — PASS

The guarantee follows from the exact squared-error projection identity. A leaf-symmetry reduction is valid globally by orthogonal equivalence of Gram-preserving permutations and concavity of the smallest eigenvalue. The radial two-by-two characteristic polynomial has a completed-square certificate for its unique maximizer, and the leaf-mode crossing is exactly linear in the hub/leaf sampling ratio. The equality case of the Rayleigh bound, combined with a nonvanishing radial response at every row, proves uniqueness for independently chosen probabilities, not only symmetric ones. The standalone symbolic and numerical verifier checked the identities, both regimes, a rational phase-boundary example, full Gram matrices, and independent probability perturbations. Tests do not replace the complete analytical proof. Limits: fixed iid one-step squared error only.

## Originality — PASS with bounded historical uncertainty

The general optimal probability SDP appears in Dai, Soltanalian and Pelckmans (2014, Theorem 2), and general saturated E-optimality is characterized implicitly by Pukelsheim and Torsney (1991). Neither inspected source yields the exact all-parameter one-hub/leaf probability formula, its sharp dimension-dependent branch threshold, or unrestricted uniqueness. Gower and Richtárik (2015) gives general iterative convergence theory rather than this specific solution. The closest published inverse-positive Gram theorem assumes a sign condition violated here, since every hub-to-leaf entry of \(G^{-1}\) is strictly negative. Earlier special low-dimensional and two-nonsingleton-community calculations have different domains and do not imply the present formula. Search absence is not a proof of priority; older E-design specializations may still overlap.

## Mathematical value — PASS

Optimal iid row selection is a fundamental quantity for the sharp worst-direction projection error bound, commonly requiring numerical semidefinite optimization. This exact family includes both positively and negatively equicorrelated leaf rows, gives an explicit sample allocation for arbitrarily many rows, and identifies a genuine change of active spectral obstruction and a sharp dimension threshold, for all \(m\ge3\). The boundary case \(b=a^2\) has a different nonzero large-dimensional hub selection limit, and the exact cutoff \(m=27\) for rational coherences \(a=3/10,b=1/10\) illustrates nontrivial finite-size behavior. The result is an exact class solution, not a generic solver speedup.

## Limitations and overlap risks

The broad optimal-design and diagonal-scaling literatures may contain equivalent specializations outside the materially inspected papers. The claim does not address multistep optimum, adaptive selection, non-unit rows, or zero hub correlation. No independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
