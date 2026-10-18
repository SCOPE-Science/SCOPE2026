# Independent mathematical audit

## correctness

PASS

All 5 root-to-tip paths have length 55 and submitted K has exactly the shared-path Brownian off-diagonals 25,35,50. Symbolic direct inversion of every 4×4 selected covariance K_S+ηI produces only L,R,M; L=2(2η²+205η+4600)/((η+55)(η²+145η+3700)), R=2/(η+105)+2/(η+80), M=2/(η+105)+2/(η+90). R−M=20/((η+80)(η+90))>0, and L−R has numerator −10(2η³+205η²−1225η−198500) over a positive denominator. The cubic has exactly one positive root (one sign change plus IVT), 29.8018144905886…, separating disjoint optimal omission classes C/D vs A/E. For <=4 tips, k=1,2,n are noise-invariant; the only n=4,k=3 cases root split 2+2 or1+3 have common minimizing cherry. The latter follows from strictly positive three-tip GLS coefficients and replacing a tip with the independent root-child tip, lowering all incident covariances. Independent SymPy reconstruction checked identities and all five four-tip exclusions. No finite grid is used to establish uniqueness.

## originality

PASS

Previously published Brownian GLS, error covariance, effective sample size and tree-subset selection furnish the model and objective. The exact sharp combinatorial onset of a noise-induced change in argmax—universal non-switch below five tips and an explicit rational five-tip switch—is not asserted by the relevant full sources inspected or surfaced by Resultary. General matrix optimal-design methods could conceal an equivalent smaller-dimensional example; this remains a substantive residual risk.

## value

PASS

Separates sampling precision improvements from stability of the actual optimal taxon set under measurement noise. A sharp five-tip minimum plus explicit threshold and competing optimal classes is a motivated boundary in correlated experimental design rather than a generic numerical trial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
