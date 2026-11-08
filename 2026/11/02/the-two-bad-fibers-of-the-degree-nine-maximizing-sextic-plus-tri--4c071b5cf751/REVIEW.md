# Independent mathematical audit

## correctness

PASS

PASS: The primitive polynomial F=XYZ[(X²+Y²+Z²)³-27X²Y²Z²] defines a flat relative Cartier divisor. For char≠2,3 the source derivatives and Hessian determinant 3888=2⁴3⁵ give four off-axis nodes; six axis cusps become E7 after adding their coordinate lines, plus three vertex nodes. Bézout rules out reducibility of the sextic and its delta total 6+4=10 yields geometric genus 0. In char 2 the exact polynomial identity F=XYZ G² with G=(X+Y+Z)³+XYZ gives a nodal irreducible rational cubic, normalized by [s³:t³:(s+t)³], three order-three axis contacts, and a saturated Jacobian scheme V(G²) disjoint from three vertices. In char 3 F=XYZ Q³, Q=X²+Y²+Z² smooth; axes meet it transversely at six points, giving nine reduced-support nodes, and Jacobian scheme V(Q³) plus vertices. Signed labels have collision weights (4,2,2,2,1,1,1) mod 2 and stay distinct mod 3. Independently expanded F and all three partial derivatives modulo 2 and 3 with SymPy; they match the exact nonreduced ideals. Boundary limitation: only the fixed integral equation, not intrinsic stable reduction or positive-characteristic freeness.

## originality

PASS

PASS (qualified): Dimca–Ilardi–Pokora–Sticlaru Example 6.4 already gives this precise equation, six E7 and seven nodes, Tjurina 49, and free exponents over C. These are not novel. The new prime-by-prime scheme-theoretic factorization, nodal-cubic normalization, conic multiplicity and thirteen labeled section collisions are not implied by the generic complex basket alone; no earlier covering calculation was found.

## value

PASS

PASS: This is a complete arithmetic-degeneration and Jacobian-scheme classification of a distinguished maximizing divisor, identifying the exact two bad residue characteristics and differing nonreduced special fibers. The scheme structures and labeled collisions offer reusable exact data beyond the characteristic-zero singularity count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
