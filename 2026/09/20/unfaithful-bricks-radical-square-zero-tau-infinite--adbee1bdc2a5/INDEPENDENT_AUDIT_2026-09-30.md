# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/unfaithful-bricks-radical-square-zero-tau-infinite--adbee1bdc2a5`  
Assigned and audited source tree: `21efed39e68ca6fd46500a26a5ed1984dc890178`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `85a84ea6851abdc80fa5e085026766fcc051be46`  
Disposition: **passed**

## Correctness

**independently_supported**. The brick classification follows correctly from the known sink-source affine-Dynkin reduction. For a sincere module the annihilator has no semisimple idempotent part; without parallel arrows, primitive idempotents isolate each one-dimensional arrow block, so the annihilator is exactly the span of zero arrow maps. In an affine tree, a zero arrow is a bridge and splits a sincere representation, so every sincere brick is faithful, while every nonsincere brick is unfaithful and only finitely many occur on proper finite-Dynkin supports. In an alternating affine n-cycle, a nonsincere indecomposable has a proper connected A-type support, hence is the unique thin interval module on that support; n choices at each length 1,...,n-1 give n(n-1). A sincere unfaithful brick has exactly one zero arrow, factors through A_n, and is the unique sincere thin indecomposable there, giving n more and n^2 total. For Kronecker, a sincere unfaithful brick has a nonzero proper annihilator line in the two-arrow space and factors through A_2, hence has dimension (1,1); conversely every nonzero scalar arrow pair is a brick with a one-dimensional annihilator, giving P^1(k). The ideal-lattice argument then isolates Kronecker as the nondistributive case over the algebraically closed field.

## Originality

**qualified_supported_source_question_resolution**. Mousavand-Paquette explicitly note that all regular Kronecker bricks are unfaithful and ask whether a minimal tau-tilting-infinite algebra is nondistributive exactly when it has infinitely many unfaithful bricks. Their paper also supplies the radical-square-zero affine sink-source reduction, so these are prior inputs. Searches did not locate the complete radical-square-zero answer, the exact n^2 alternating-cycle count, or the tree-type sincere-faithful classification. The result is therefore supported as a direct resolution of the published question on this complete subclass, while the proof's elementary affine-quiver nature leaves significant folklore/differently-phrased prior-art risk.

## Scientific value

**meaningful_complete_subclass_resolution**. The theorem answers a published structural question on the full minimal radical-square-zero subclass and gives a sharp mechanism-level trichotomy: parallel arrows create a projective family, cycles create finitely many single-zero-arrow sincere bricks, and affine trees force sincere faithfulness.

## Independent checks

- Reconstructed the annihilator decomposition for sincere modules with and without parallel arrows.
- Counted all proper connected supports of an n-cycle and used A-type positive roots to recover n(n-1) nonsincere bricks.
- Checked that two zero arrows disconnect a sincere cycle representation while exactly one zero arrow yields the unique sincere A_n indecomposable.
- Re-derived the Kronecker P^1 classification and the finite-versus-infinite ideal-lattice dichotomy.

## Literature and evidence checked

- https://doi.org/10.1017/nmj.2022.28
- https://doi.org/10.1090/proc/13162
- https://doi.org/10.2307/1969899
- https://www.math.uni-bielefeld.de/~wcrawley/17noncommalg2/Noncommutative%20Algebra%202%20v4.pdf
- https://arxiv.org/abs/2602.14171
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/unfaithful-bricks-radical-square-zero-tau-infinite--adbee1bdc2a5

## Limitations

- The theorem applies only to minimal tau-tilting-infinite algebras with radical square zero.
- The general Mousavand-Paquette nondistributivity question remains open outside this subclass.
- Classical affine-quiver representation theory and Jans's ideal-lattice criterion are essential prior inputs.
- Because the remaining argument is elementary after the source reduction, folklore or unindexed equivalent observations remain a material originality risk.
