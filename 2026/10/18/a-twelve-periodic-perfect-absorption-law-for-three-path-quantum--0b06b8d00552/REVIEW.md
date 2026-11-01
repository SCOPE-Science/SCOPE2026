# Independent mathematical audit

## correctness

PASS

Reconstructed the finite-dimensional contraction-to-dark-subspace argument: the sink-free adjacency eigenvectors are reducing and every complementary eigenvalue of -ihA-(kappa/2)P_a has strictly negative real part (Jordan blocks also decay). For a source-visible eigenvector z!=0, short arms require lambda!=±1 and give u1=z/(lambda^2-1),u2=lambda*z/(lambda^2-1). The long Chebyshev recurrence, both endpoint constraints and identity U^2+V^2-lambda*U*V=1 imply -(lambda^2-1)(lambda^2-3)=0, hence lambda=±sqrt(3). The U recurrence at ±sqrt(3) selects exactly m≡7(mod12). At those m two sink-dark normalized vectors have squared norm 2m+1, b amplitude 1, are orthogonal and exhaust source-visible modes, producing S=2/(2m+1). Independent exact symbolic checks verified the identity and both endpoint signs for m=3..61, dense spectral projector computations for m=3..72 agreed to 2.1e-16, six constructed vectors passed and finite-time dynamics were checked. These computations corroborate rather than establish the all-m theorem.

## originality

PASS

Statement-level literature comparison found the dark-projector/absorbing-site reduction to be established in quantum-walk transport, while the all-m evaluation for adjacency theta paths of lengths (3,3,m), exceptional residue m=7 mod 12, and exact terminal-source dark weight 2/(2m+1) were not identified in the inspected primary results. The assessment is best of knowledge: absence of a search hit is not a proof of novelty.

## value

PASS

The three-route theta network is a natural minimal two-terminal, multichannel interference geometry; its quantitative question whether a designated opposite-terminal excitation is eventually fully absorbed is physically and spectrally motivated. The theorem closes that question for every third-arm length with a sharp period-twelve phase boundary and an exact trapped fraction invariant under any positive local sink rate and nonzero uniform hopping. This is a nontrivial complete classification and exact benchmark, not a table of arbitrary small cases. The value is specific to ideal coherent infinite-time adjacency transport and does not imply robustness to phase/disorder or a general transport theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
