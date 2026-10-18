# Independent mathematical audit

## correctness

PASS

For invertible qubit T=UA, Bloch normalization has c=2g/(1+g²), d=(1−g²)/(1+g²). Maximization of the pure-state postselection displacement gives G(A)=g=(a−b)/(a+b). When g≤1/√3, averaging the exact Bloch inner product along the latitude z=−g yields at least one input with disturbance≥g uniformly over SO(3) polar-unitary rotations; when g≥1/√3 the equator average gives G(T)≥g/sqrt(1+g²)≥1/2. Consequently G(T)<1/2 implies G(A)≤G(T). Nonzero singular operators have disturbance supremum one and are excluded. Completeness and equality of outcome probabilities follow from sum |M_y|²=I. Independently rechecked the rotation-angle algebra, boundary g=1/√3 and the trace-distance factor 1/2.

## originality

PASS

Butucea–Johannes–Stein explicitly formulate polar-factor gentleness as a conjectural step, supported by numerical qubit experiments; their positive-operator lemma alone does not compare UA to A. Antieigenvalue/operator-angle prior work may compute G(A), but that extremum by itself does not prove the arbitrary left-polar-unitary inequality. Resultary search returned this exact claim but no distinct covering record. Risk of an alternative classical two-dimensional operator-angle theorem remains.

## value

PASS

Resolves an explicitly posed qubit measurement conjecture in the strict alpha<1/2 regime, and permits the sharper gentle-to-quantum-differential-privacy parameter 2log((1+alpha)/(1−alpha)) without assuming positive Kraus operators. Its phase split is mathematically motivated by the threshold under which the comparison is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
