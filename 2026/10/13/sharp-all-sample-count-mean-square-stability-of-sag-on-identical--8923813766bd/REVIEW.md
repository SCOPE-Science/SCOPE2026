# Independent mathematical audit

## correctness

PASS

Orthogonal diagonalization reduces arbitrary SPD dimension to scalar mode s=eta lambda. For each n>=2 a positive definite quadratic memory-and-iterate energy V satisfies exactly E[Vnext|state]-V=(s-2)x^2 for 0<s<=2. Its summed drift implies E[x_k^2] summable and memory convergence for s<2; at s=2 conservation of positive energy prevents convergence from nonzero states. For s>2 the exact 4x4 second-moment matrix has det(I-T)=-2s(s-2)/n^3<0 and therefore an eigenvalue >1; deterministic initial moment vectors span the four-dimensional moment coordinates, proving that convergence for every initialization is impossible. Independent enumeration of per-index conditional energy changes verifies 15 rational cases. No a.s. divergence or geometric rate is asserted.

## originality

PASS

The SAG algorithm and known general conservative sufficient stepsizes were already established by Schmidt–Le Roux–Bach. Their general-convex and strongly convex results do not imply an all-n exact necessary-and-sufficient eta lambda_max(H)<2 threshold for identical SPD quadratic components with arbitrary initialized memory. Similar Resultary results concern STORM, SVRG and other schemes rather than the same SAG recurrence.

## value

PASS

SAG is a canonical finite-sum memory method; knowing its exact all-initialization mean-square stability boundary even in the identical-components benchmark sharply separates a memory algorithm from conservative general worst-case step bounds. The positive Lyapunov energy is a reusable structural certificate for that natural benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
