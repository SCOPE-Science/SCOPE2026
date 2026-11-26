# Independent mathematical audit

## correctness

PASS

Write q=(e_x-e_y)/sqrt(2) and v=(gamma(e_x+e_y)+sum_z w_z e_z)/sqrt(2). For every real diagonal F, [D,F]q=(f(x)-f(y))v, so ||[D,F]|| is at least sqrt(C) times the gap. For the gap-one potential supported on {x,y} with values +1/2 and -1/2 the entire commutator is vq^T-qv^T. It vanishes off span(q,v), and its two nonzero singular values when C>0 are both ||v||=sqrt(C). Scaling attains the bound. For C=0 both rows have no off-diagonal entries, and the same potential can be scaled arbitrarily. D's diagonal commutes with every F and does not enter. Substitution gamma=0 or 1 and sum w_z^2=k gives both unweighted cases and their ratio. Independent symbolic spot check: python3 -B /workspace/reproduce_frozen.py 2 verifies the two witness identities with arbitrary symbolic weights, diagonals on the pair, outside edge and potentials on a four-point space; the argument above proves all sizes.

## originality

PASS

Exact complete-graph/deleted-link formulas and two same-day false-twin specializations are established coverage. The supported distinction is the sharp common-profile formula for arbitrary real weights (either zero or nonzero pair coupling), independent of the whole outside submatrix. The located sources and related records do not cover that statement. Antisymmetrization is a standard symmetry argument, not itself a new method here.

## value

PASS

The substantive result is exact ambient-independence for a natural class of vertex pairs, not the elementary averaging trick or the known complete-graph value. For a graph joined to two twin apices it determines their distance without solving the surrounding distance problem and gives an exact edge-deletion response independent of every internal edge of the base. It also covers signed weighted attachments, and provides a sharp norm certificate and optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
