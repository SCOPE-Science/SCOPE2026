# Independent mathematical audit

## correctness

PASS

For r,s>=2, with a=(r-1)/r, u=(s-1)/s, t=2u, L=8-t, B=aL+t, the asserted squared distortion Q=B^2/(4aL) follows from a universal variance obstruction and matching centered-simplex embedding. For every noncontracting embedding, within-branch leaf means give W>=t, across-branch means Y/a+W>=8, while root-child and child-leaf expansion plus Cauchy-Schwarz give sqrt(Y)<=D+sqrt(D^2-W). The right-hand obstruction is strictly decreasing in W, hence D^2>=Q. Independently evaluated all seven squared-image pair types and compared 1<=image squared/d_tree squared<=Q at (r,s)=(2,2),(2,3),(3,2),(3,3),(4,5), obtaining Q=81/56 at (2,2) and the predicted range; checked proof equality forces each simplex, mutually orthogonal leaf residuals, and unique Gram matrix rank rs-1. Derivatives in a,u are strictly positive. Read actual verify.py; its finite-grid checks cannot replace the all-r,s variance argument.

## originality

PASS

General Euclidean tree embeddings of Linial-Magen-Saks give asymptotic distortion upper bounds as |T| grows; Linial-Saks fork bounds address different large-depth asymptotics; none of the accessible statements supplies sharp rational two-parameter formula with unique Gram optimizer for complete depth-two trees. Literature full text of closest 1998 paper unavailable, explicitly retained as priority risk. No direct logical implication from broad O(loglog n) bounds to exact Q or rigidity.

## value

PASS

Depth-two complete branching trees are a canonical first nontrivial family for metric Hilbert distortion; the exact optimum, unique affine dimension rs-1, and strict branching monotonicity are independently useful calibrated finite-metric invariants, not a routine upper bound. General all-tree embedding theorems do not give their precise values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
