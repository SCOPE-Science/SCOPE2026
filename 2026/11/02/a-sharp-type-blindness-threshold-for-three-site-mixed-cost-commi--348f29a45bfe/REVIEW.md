# Independent mathematical audit

## correctness

PASS

For three distinct metric locations with distances p<=r<=q<=p+r and three co-located agents, compare A=(0,1), B=(1,2), C=(0,2). All-average baseline twice costs are (2p+q+r,p+q+2r,p+r+2q); switch-to-max increments give exact affine differences: 2(C_A-C_B)=(p-r)+(2p-q)t0+(p-r)t1+(q-2r)t2 and 2(C_A-C_C)=(p-q)+(p-q)t0+(2p-r)t1-r t2. Maximizing over eight type vectors yields p-r+max(0,2p-q) and p-q+max(0,2p-r); both <=0 iff 3p<=q+r. Conversely if 3p>q+r, all-average forces shortest pair but t=(1,0,0) favors B by (3p-q-r)/2, including ties. Independent enumeration of all 8 profiles for every 8327 ordered integer metric triangle p<=r<=q<=44 reproduced equivalence, and verified 3,4,4 plus four-point line counterexamples. Analytical affine inequalities prove all real metrics.

## originality

PASS

Gruszecki–Anshelevich (2026) investigates type-independent mixed max/sum committee rules but its general guarantee is approximation and line treatment permits co-location. Han–Anshelevich (2025) studies compatibility of homogeneous max and sum aggregates, not arbitrary per-agent mixed types. Deligkas et al. study homogeneous facility objectives under strategic reporting. None of the inspected relevant results gives exact distinct-site universal optimum iff 3p<=q+r across all eight heterogeneous profiles. Best-of-knowledge qualification persists.

## value

PASS

For the smallest nontrivial constrained committee design with privately varying individual cost types, this gives the exact zero-loss type-blind region and a sharp obstruction where even agreement between homogeneous optima fails. The three-point line corollary and four-point counterexample locate a meaningful finite boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
