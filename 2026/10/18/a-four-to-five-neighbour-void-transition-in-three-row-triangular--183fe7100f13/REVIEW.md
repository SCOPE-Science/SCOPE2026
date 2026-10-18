# Scientific review

## Correctness

**PASS.** The six incident bonds are written explicitly, so the local three-column inequality counts precisely the occupied neighbours. Each cyclic occupancy word gives one closed transfer walk and conversely. Exhaustion of only \(512\) local triples establishes the complete cycle-bearing component decomposition for **all** lengths; the characteristic polynomials are exact integer-matrix identities, reproduced by `triangular_tube_verify.py`. Strong connectivity plus a self-loop proves primitivity. Rational Collatz bounds and exact real-root counts locate the ninth-degree Perron factor. Perron perturbation gives concentration; the threshold-five geometric classification gives its density independently. The independent bitmask graph census for lengths four through six checks both thresholds against the trace formula.

## Originality

**PASS under identified source-access uncertainty.** The nearest available theory is the bulk bootstrap-percolation work of Kogut--Leath (1981) and Choi--Yu (2019), neither of whose inspected accessible portions gives this finite-width fixed-state polynomial. In Choi--Yu's full arXiv text, sections on the triangular lattice concern percolation thresholds, critical exponents and Newman--Ziff simulation, not enumerating all absorbing microstates. Chang--Shrock (2000) contains complete width-three toroidal geometry but counts Potts proper colourings instead. The earlier square-strip pruning result lacks the diagonal bonds, and its census is not a dominating theorem for this triangular graph. Search failure alone is not used as a novelty proof. The 1981 original full text was inaccessible and could contain an unrecognized finite-size table; specialized unindexed strip enumerations also remain possible.

## Mathematical value

**PASS.** For the naturally narrowest six-regular periodic triangular-lattice tube, two consecutive high survival thresholds exhibit a qualitative change: entirely empty transverse sections have positive equilibrium frequency at threshold four but disappear from every nonempty threshold-five frozen state. This separates a real structural mechanism from the mere fact that thresholds have different counts. The explicit ninth-degree and cubic entropy laws, occupation densities, and exact finite-volume checks provide benchmark invariants for finite-size bootstrap and kinetically constrained lattice studies. No bulk dynamical or percolation assertion is claimed.

## Closest literature and limitations

Kogut--Leath (1981), DOI 10.1088/0022-3719/14/22/013: only bibliographic metadata and abstract inspected; full-text coverage risk retained. Chang--Shrock (2000), arXiv:cond-mat/0004129: geometry and chromatic-polynomial problem inspected in full-text sections. Choi--Yu (2019), arXiv:1903.01595: finite-size simulation method, triangular-lattice results and table inspected in full text. The earlier square-lattice width-three pruning count is distinct; the mask word \((1,5,7,3)\) is a triangular-only stable witness. Uniform frozen-state statistics need not equal states reached by pruning randomized initial occupations. Numerical decimals are approximations to exact spectral quantities.

Self-review: passed. Independent audit: not yet performed.
