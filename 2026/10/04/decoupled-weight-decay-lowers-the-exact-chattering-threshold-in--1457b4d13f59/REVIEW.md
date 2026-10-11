# Independent mathematical audit

## correctness

PASS

On a symmetric nonzero orbit x_t=±a with β1=0, squared gradients are constant. Starting from v0=0, the bias-corrected second moment is exactly h^2a^2 for every β2<1, so the source AdamW update reduces to x^+=(1−δ)x−α h x/(ha+ε). Requiring x^+=−x gives a=α/(2−δ)−ε/h and existence exactly c=αh/ε>2−δ. The minimizer linearization has multiplier 1−δ−c, crossing −1 at the same threshold. When β2=0 the exact odd scalar map has magnitude multiplier M(z)=1−δ−αh/(hz+ε), strictly increasing from 1−δ−c to 1−δ; for c≤2−δ it lies strictly in (−1,1) for every z>0, giving global magnitude contraction to zero. Above threshold the unique symmetric two-cycle has derivative d=1−δ−(2−δ)^2/c with −1<d<1, hence is locally attracting. I independently checked the cycle and derivative numerically for several δ; the proof is analytic.

## originality

PASS

The AdamW primary paper was inspected at Algorithm 2 and establishes the decoupled update but does not analyze quadratic periodic dynamics. Bock–Weiß's primary paper establishes period-two limit cycles for Adam on quadratics with bias correction, and its accessible full text contains no weight-decay discussion. Resultary searches for an AdamW quadratic two-cycle threshold produced no matching theorem. The audited claim therefore combines two prior lines in a way not implied by either: adding a decoupled shrinkage term changes the exact threshold to 2−δ, creates a strip where decay turns convergence into a stable nonzero cycle, and yields a global below-threshold classification in the β2=0 slice.

## value

PASS

The result isolates a counterintuitive stability effect of a widely used optimizer modification: decoupled decay can lower the flip threshold and create a stable nonzero cycle in a parameter strip where the same memoryless adaptive method converges without decay. The exact threshold, amplitude, stability multiplier and global convergent side make this a motivated boundary theorem, not a routine numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
