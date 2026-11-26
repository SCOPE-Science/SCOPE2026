# Independent mathematical audit

## correctness

PASS

The frozen proof's bijection at line 91 is false: G(99/100)=1/199, so the asserted domain loses all equilibria for 0<gamma<=1/199. The repaired RESULT.md uses G(0)=1, G(1)=0 and G'<0 on the full physical interval; the thresholds and Finding are unchanged. Independent exact replay (python /workspace/checks/5.py) derives the characteristic cubic from the simplex ODE, verifies the determinant identity, and obtains quartic evaluations 357701/3125000, -135039/1280000, -45/2 and 52 at the four bracket ends. Two sign changes in the coefficient list and these disjoint sign brackets certify exactly two simple positive roots, in the corrected domain. All three cubic coefficients are positive; the Routh first column gives zero or two right-half-plane roots, and at equality the factorization (lambda+A)(lambda^2+B) and real crossing derivative -(AB-C)'/[2(A^2+B)] give the two directed transverse crossings. These arguments apply for every recovery rate stated, on the conserved simplex only.

## originality

PASS

The exact classification for the published Fig. 8(a) model slice is supported as distinct by the sources inspected. In particular, the exact originating model and parameter set are known, and repeated loss and regain of stability is not itself new. Correcting the endemic domain does not change the claim being compared.

## value

PASS

The parameter slice is fixed by a published numerical example whose wider analysis was explicitly left open. The exact stability and unstable-dimension intervals distinguish a bounded loss of endemic stability from an instability persisting to the endpoint, and locate the reported run relative to both transitions. This gives useful checks for later nonlinear bifurcation work, without asserting Hopf nondegeneracy, cycles or global behavior. The repaired domain preserves this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
