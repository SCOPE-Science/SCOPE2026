# Independent mathematical audit

## correctness

PASS

Path endpoint tie retention makes each rim update under hub=0 the AND of a symmetric two-neighbor relation with endpoint loops, and under hub=1 the corresponding OR. The length-two relation is connected, eliminating nonunanimous fixed/static-hub cycles for fans. The auxiliary edges {0,1}, {i-1,i+1}, {n-2,n-1} make exactly one cycle on n sites. Solving x=DEx is equivalent to no isolated ones, while hub bit switching imposes 2a>n>2b. Cyclic run compositions count c_n(a,a-r)=n/r*C(a-r-1,r-1)*C(n-a-1,r-1) for one runs of size >=2; wheel distance-two relation is one cycle if n odd, two parity cycles if even, and its two static-hub alternating orbits give the +2. Symmetric adjacency plus half identity gives a strict two-step energy potential whenever the current state is not already 2-periodic, excluding periods >=3. Independently enumerated fan/wheel states for 3<=n<=10; odd counts matched and the sign at n=4 matched, but n=12 comparison relies on exact formula rather than this direct finite scan.

## originality

PASS

Classical symmetric threshold maps already have period<=2 and cyclic-majority fixed-word count formulas; those subclaims are credited. The coupled fan/wheel primitive cycle count, odd rim-deletion invariance and even examples of opposite count changes are different from static cellular-automaton fixed points and from global convergence results. Older automaton literature may cover equivalent hub-coupled counts under another term, so priority is qualified.

## value

PASS

The exact recurrent orbit census explains a sharp parity-dependent change under the deletion of ONE graph edge, including cases of both increases and decreases. This bridges threshold dynamics with a run-word enumeration and is a motivated graph perturbation invariant beyond fixed-point counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
