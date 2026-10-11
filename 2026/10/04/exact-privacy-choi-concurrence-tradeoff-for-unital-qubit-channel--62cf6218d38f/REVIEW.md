# Independent mathematical audit

## correctness

PASS

The output Bloch radius is at most the largest singular value, giving uniform lower/upper eigenvalue bounds; antipodal singular-vector inputs and the aligned rank-one measurement attain their likelihood-ratio quotient, proving the exact privacy parameter. Local unitaries diagonalize a unital qubit channel to Pauli form, where the normalized Choi state is Bell diagonal and Wootters' formula plus the CP tetrahedron gives concurrence equal to one half of the positive part of the singular-value sum minus one. Privacy bounds every singular value by tanh(epsilon/2), and depolarizing noise saturates all three simultaneously. Fresh checks over 10,000 random Pauli channels matched the singular-value concurrence formula to machine precision and representative depolarizing points saturated the frontier.

## originality

PASS

The recent all-channel privacy theorem proves only the sharp entanglement-breaking threshold, while the privacy–utility paper optimizes state fidelity and trace-distance objectives. Standard unital-qubit geometry and Wootters concurrence supply static ingredients but contain no privacy constraint. The audited positive-branch concurrence optimum therefore requires a new exact privacy parameter for an arbitrary unital Bloch map and a constrained singular-value optimization; no equivalent Resultary record was found.

## value

PASS

The theorem turns a newly established binary privacy threshold into an exact quantitative entanglement-resource curve and identifies the sharp mechanism throughout the unital-qubit class. That is a natural and interpretable resource tradeoff, not a routine restatement of the zero-entanglement threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
