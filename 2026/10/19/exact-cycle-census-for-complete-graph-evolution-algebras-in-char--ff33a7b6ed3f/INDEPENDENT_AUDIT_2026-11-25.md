# Independent mathematical audit

## correctness

PASS

The graph multiplication gives T=A∘F, with coordinate Frobenius F and A=I+J, Jx=(Σx_i)1. Since F commutes with the binary matrix A and J²=nJ, odd n gives projection onto the sum-zero hyperplane H; on H the map is F and every other point reaches H in exactly one step. Fixed points on H for F^k have dimension n−1 over the fixed field of size 2^g. For even n, A²=I; for even k all vectors over the fixed field are fixed by T^k. For odd k the trace argument in RESULT.md is sound: pairwise coordinate differences are fixed by F^k, and the common equation σ(y)+y=c with c in the fixed field is soluble iff tc=0, with 2^g lifts. Equivalently, a normal basis over F_2 makes F^k act as g shifts of length t on n-component blocks; on each cycle the fixed equation forces its initial block into ker(A^t−I), of dimension n when t is even and n−1 otherwise. This verifies the exceptional even-n branch without trace. F^f=I implies the stated period divisibility, and inversion of P_k=Σ_{d|k}dC_d gives the exact least-period orbit counts. The finite verifier was inspected, not run; its odd-branch assertion verify.py:34 is tautological and does not independently check the sum-zero image. The algebraic proof does.

## originality

PASS

The complete-graph algebra and its binary adjacency dynamics predates the record. The contribution is the explicit extension-field iterate census and classification, not Möbius inversion, the adjacency calculation, or general finite-field normal form. A substantially broader catalog result does imply the entire theorem, including the exceptional branch, but its shown catalog date is later; no evidence establishes that theorem as earlier prior art. It is recorded as exact coverage rather than treated as a different subject. The earlier graph/dynamics sources inspected do not state the extension-field theorem.

## value

PASS

The complete graph is a standard test family for evolution algebras. This calculation resolves every finite-extension periodic orbit and all transient depths uniformly, not just idempotents or a small prime-field example. The interaction between graph parity and relative Frobenius orbit length has a concrete effect on orbit counts, useful as a benchmark for broader graphical dynamics. The method is elementary and does not purport to be a new linear-algebra tool.

The dated certificate retains the supplied scientific assessment, sources and limitations.
