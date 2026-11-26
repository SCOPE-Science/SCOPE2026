# Independent mathematical audit

## correctness

PASS

For odd q, set D=A−B, so A=(C+D)/2 and B=(C−D)/2. Their conditions are equivalent to D*=D, CD+DC=0 and D²=−C². Different eigenspaces of the split selfadjoint C are orthogonal and each is nondegenerate. The anticommutation equation forces D to map V_λ into V_{−λ}; for λ nonzero the equation on D² makes the map invertible, so an unpaired eigenspace or unequal dimensions are impossible. On a paired block write D's upper-right entry as λT; selfadjointness gives the lower-left as λT*, and the square condition is T*T=−I and TT*=−I. This is exactly an anti-isometry of the two forms. The two determinant square classes must agree after negation of one form; this is exactly the stated character test. The valid maps form one torsor under the orthogonal group of the plus-labelled eigenspace. The kernels of C±D are graphs over one m_λ-dimensional eigenspace, so each summand has rank m_λ there. On V_0, B_0=−A_0; a square-zero selfadjoint A_0 has isotropic image U and kernel U^⊥, and the canonical identification V_0/U^⊥≅U* gives a bijection with nonsingular symmetric maps U*→U. The isotropic-line count from the finite-field quadratic zero count and quotienting by a hyperbolic plane multiply to count complete isotropic flags, then division by the flags in an r-plane gives I_r. The stabilizers of the two congruence classes relative to GL_r give S_r, with the stated orders and Witt signs. All factors are positive on the stated support, with the empty, zero-dimensional and rank-zero conventions consistent. The choices are ordered, so swapping A and B does not call for division by two. The independent replay directly tested all 59049 selfadjoint 4×4 matrices in each of four F3 cases and found 1+32z+144z², 2z+8z², 8z² and 0, checking both ranks. Replay: /workspace/branches/55fdf519-8983-4966-bb9c-1f6e34fdcdf4/record5_reproduce.py with record5_small_run.json and record5_other_runs.json. The uploaded check.py was inspected, not run. The replay is not a test of all odd q or of the recorded extension-field sample; the proof covers arbitrary odd q in the split setting.

## originality

PASS

Pass is for the exact ordered fiber polynomial for a fixed split semisimple selfadjoint target, including its nonzero blocks and all ranks, conditional on the retrieved evidence. The existence criterion is already given by the primary classification, and the entire zero-target polynomial is covered by a later distinct indexed formula. Neither is credited as new. The actual broader existence and constructive passages were compared with the fixed-target enumeration; they do not supply the latter. No indexed or primary full count with the nonzero anti-isometry torsors and the zero-block rank contribution was established. This is not a priority assertion.

## value

PASS

Existence does not determine the multiplicities of decompositions, even for invertible targets. The result supplies a fixed-target finite-field enumeration, separates the dependence on eigenspace form types from the nilpotent freedom on the zero eigenspace, and gives the attained ranks and their exact weights. The nonzero-block torsor count and its rank contribution address a natural gap beyond the earlier existence theorem and the known zero-target count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
