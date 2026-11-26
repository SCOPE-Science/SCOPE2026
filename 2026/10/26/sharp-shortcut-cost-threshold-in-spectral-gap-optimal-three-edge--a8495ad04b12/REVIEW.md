# Independent mathematical audit

## correctness

PASS

For the corrected /workspace/repairs/2/RESULT.md. The frozen Finding's assertion that adding an edge's conductance would strictly increase the gap at fixed other weights is false here: adding shortcut weight is a PSD update that annihilates the at least m−1 zero-terminal gap eigenvectors. The repair states the exact invariance in this comparison, not a fixed-budget comparison. Independently, concavity validates path-permutation and terminal-reflection averaging. The even constant-on-path sector gives 0 and (m+1)x, the two fluctuation sectors give x and x+2y each m−1 times, and the odd constant-on-path sector is the displayed normalized two-by-two block. For gap at least one, x≥1 and its Schur complement is the stated bound on y. Minimizing the reciprocal-plus-linear lower cost in z uses mx+2z−1=mx/√τ when feasible; below and at the threshold the resulting lower cost increases strictly with x. Above the threshold the constrained minimizer is z=0, and x²/(mx−1) is nondecreasing for x≥1. At x=1 the bound is tight with positive y, contact in the odd block and the same z=0 on both branches at equality. This gives the value, symmetric optimizer, and multiplicity m after scaling. The fixed shortcut is unchanged by averaging. The repair also justifies unrestricted multiplicity explicitly: the kernel of an average of PSD operators on the orthogonal complement of the constants is contained in every summand's kernel. The even zero-terminal fluctuation vectors there force each outer weight, and the odd gap vector has nonzero opposite values on the two interior vertices of every path, forcing each middle weight once the outer weights are fixed. Thus even the full optimal Laplacian is fixed. The frozen exact and numerical check sources and recorded output were inspected, not executed; global optimality and rigidity are analytic.

## originality

PASS

The corrected exact result for m≥2 survives the statement-level comparisons. The closest indexed result with the same topology minimizes a different objective. The closest indexed result with the same priced spectral-gap objective is the four-cycle, outside this range and with different optimizer behavior. The general budgeted-Laplacian formulation is established and not claimed as new; its displayed theory and examples do not supply the corrected closed form or rigidity on this topology.

## value

PASS

The repaired result resolves a concrete design tradeoff: how costly a direct redundant link can become before every optimum must delete it. It provides the full optimal value, exact boundary behavior, and spectral/optimizer rigidity for arbitrarily many alternate paths. The path modes explain why merely allowing more shortcut weight cannot improve the gap at the optimum with the other weights fixed. The result is not a numerical SDP instance or a renaming of a solved cycle problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
