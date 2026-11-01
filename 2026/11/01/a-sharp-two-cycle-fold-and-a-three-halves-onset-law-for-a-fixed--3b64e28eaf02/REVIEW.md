# Mathematical review: a sharp two-cycle fold and a three-halves onset law

## Correctness — PASS

The result is a theorem about the complete real-plane **primitive period-two** orbit count of
\(F_{\alpha,\beta}(x,y)=(\alpha\cos x+\beta(y^2-1)x,y+x)\) for \(\alpha>0\) and \(0<\beta\le2\).
The coordinate update forces the first coordinates of a prime two-cycle to be \(x,-x\), and the
midpoint substitution gives the necessary and sufficient pair of equations
\(z^2+x^2/4=1-1/\beta\), \(\alpha\cos x=\beta z x^2\). Hence for \(1<\beta\le2\) all real solutions
are positive roots of the specific function \(Q_\beta(x)=\beta x^2\sqrt{1-1/\beta-x^2/4}/\cos x\).
The strict-concavity step is nontrivial: an explicit degree-eight polynomial has nine strictly
positive rational Bernstein coefficients on the critical domain, proving \((\log Q_\beta)''<0\).
This yields an exact root count of zero, one, or two, plus a nondegenerate fold. Rescaling at
\(\beta\downarrow1\) proves the leading \(3/2\) exponent. The standalone `verify.py` independently
checks the algebraic reductions, polynomial identity, Bernstein coefficients, asymptotic maximizer,
and six period-two points by forward iteration. Finite checks do not prove infinite statements.

## Originality — PASS within inspected evidence

Almatroud and Pham (doi:10.3390/math11061319), first published March 9, 2023, define exactly the
same FPFM1 map in their equation (5) and numerically examine its bifurcation diagrams and
Lyapunov exponents in Sections 2–4. The full material inspected does not furnish a complete
primitive period-two census, the fold threshold, or its three-halves onset law. Its proof of no
fixed points is explicitly credited, not claimed as new. Ramadoss et al. (doi:10.3390/sym14102110)
use a serial nonlinear-map construction \(x'=a\sin(b\cos(y)x)+c\), which is mathematically
different; Zhang et al. (doi:10.1088/1674-1056/ac7294) study a map with cosine memristance in the
\(y\)-dependent coefficient, also a different map. Previously published short-cycle analyses of
rational Rulkov, Duffing, Bogdanov, and Gumowski–Mira maps do not imply the stated cosine–quadratic
census. Direct and synonym searches have not located equivalent coverage. An unindexed analysis
of the identical FPFM1 short-period equations remains a priority risk; negative searches are not
proof of uniqueness.

## Value — PASS

The model was introduced for its unusual absence of fixed points and studied numerically. The
existence, number and annihilation of its shortest periodic orbits are a natural missing
dynamical invariant, not an arbitrary finite parameter slice. The classification covers the
entire original numerical \(\beta\)-range and gives a sharp, all-parameter fold curve as well as
a nonanalytic \((\beta-1)^{3/2}\) onset law. In particular it rigorously accounts for exactly two
prime two-cycles at the paper's representative parameters \((\alpha,\beta)=(1/10,17/10)\).
The result is not a theorem of global stability, chaoticity, or physical performance.

## Closest work and limitations

The closest primary source is Almatroud–Pham (2023), doi:10.3390/math11061319; numerically studied
periodic phenomena in related memristive maps do not give this full-real-plane classification.
The proof deliberately restricts \(0<\beta\le2\), where cosine is positive on the entire
possible two-cycle ellipse. Higher parameter values and the two-cycle return eigenvalues are
not classified. Neither independent validation nor exhaustive publication-priority clearance
has occurred.

Self-review: passed. Independent audit: not yet performed.
