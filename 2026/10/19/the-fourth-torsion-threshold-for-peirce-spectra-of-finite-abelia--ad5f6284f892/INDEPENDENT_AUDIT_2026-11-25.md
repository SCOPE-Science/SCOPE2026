# Independent mathematical audit

## correctness

PASS

Reindexing e_x e_y=e_(2y−x) gives the Fourier rule c_χ(vu)=c_(χ^−1)(v)c_(χ²)(u). For an idempotent u, P_χ=c_χ(u)c_(χ^−1)(u) satisfies P_χ=P_χP_(χ²); the eigenvalues of R_u² are P_(χ²). If there is no four-torsion, all squared characters lie in the odd part, where squaring is a permutation, and the recursion around each cycle gives P∈{0,1}. A basis idempotent yields 1 and −1 if inversion has a two-element orbit; the uniform idempotent kills a difference of distinct basis vectors in the same 2G coset. If 2G=0 then R_u is the identity for every nonzero idempotent (which has augmentation 1). Independently, in the order-four subgroup itself, the sums of each parity class are fixed by every right translation. Thus u=((1+t)(e_0+e_2)+(1−t)(e_1+e_3))/4 is an idempotent for every complex t; e_0−e_2 has eigenvalue t. Multiplication restricts to the subgroup algebra, so this proves the all-complex branch in G. The frozen global Fourier family is also valid: the only nonzero possible coordinates are at the trivial character and a self-inverse square of an order-four character, and on the order-four inverse pair both off-diagonal entries are t. The trivial group and t=0 are covered. Bounded group-basis witness checks for seven groups passed (python3 /workspace/replay_checks.py 1); the proof, not the finite checks, covers arbitrary t and G.

## originality

PASS

The nontrivial odd-order spectrum and the trivial-core branch are prior, and the entire elementary-two-factor extension of the odd case is a mechanical implication of prior work, not a separate novelty. Positive credit is limited to demonstrating that four-torsion suffices for the full complex spectrum in a core and hence closing the exact boundary. The strongest later indexed overlap is an exact three-branch statement with an additional diagonalizability theorem; that later record does not establish prior coverage.

## value

PASS

The spectrum is a natural invariant already studied in quandle algebras. Showing a jump from a fixed discrete set to all of C at a specific group-theoretic threshold fills the even-core boundary and separates two behaviors among non-Latin cores. The arbitrary complex value can already be witnessed in one small subcore, so the classification is useful across all finite abelian groups without solving their idempotent varieties. No distinct value is claimed for rederiving the previously implied discrete branches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
