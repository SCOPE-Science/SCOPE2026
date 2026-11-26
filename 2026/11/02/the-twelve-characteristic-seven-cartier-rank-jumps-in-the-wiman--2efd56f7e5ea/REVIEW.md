# Independent mathematical audit

## correctness

PASS

In square coordinates, writing a=u-w,b=v-w expresses the cubic as w*8(a²-ab+b²)+2a³+(1-t)a²b+(1+t)ab²+2b³. The quadratic has distinct roots. At a=1 and r=b satisfying r²-r+1=0 the cubic term becomes 2r-1-t, and (2r-1)²=4 in F7. Away from t²=4 the polynomial is primitive and linear in w, hence integral; the node accounts for the full arithmetic genus of the cubic. The coordinate-axis cubic (all three equivalent by cyclic rotation) has coefficients 2,1-t,1+t,2 up to order; its discriminant reduces to (t²-4)(t²+1). Away from its roots the axis intersections are simple, and no intersection is a vertex since the pure-cube coefficient is 2. Valuations at intersections with u=0 and v=0 give independent square classes of u/w and v/w. Hence the pullback sextic is integral, is unramified over the node with four ordinary nodes, and is nonsingular everywhere else by the simple axis intersections and étaleness off the axes. The normalization has genus six. The six independent vanishing adjoint cubics are therefore a basis. In the affine plane adjoint formula Cartier keeps monomials of F^6 times the numerator whose two affine exponents are 6 modulo 7 and applies inverse Frobenius to their coefficients; homogenizing gives exactly the stated H indexing. Evenness of F forces H to preserve the exponent parities, and cyclic rotation identifies the three two-dimensional adjoint blocks. Independently recomputed the x-parity block by multinomial expansion in the square coordinates, using the pure-cube coefficients 2, mixed coefficients 1±t, and uvw coefficient -12. The replay is to sum 6! times the products of chosen coefficient powers divided by their factorials at each target square-coordinate exponent (7(alpha+1)-(beta+1))/2, then subtract the columns for x³ and xy² or xz² and read the negatives of the xy² and xz² entries. The resulting block is [[A+B,C],[-C,A-B]] with A=t^6+4t^4+2t²+5, B=4t^5+6t and C=5t^5+4t. Its determinant is t^12+3t^10+6t^8+4t^6+2t^4+4, equal to D in F7[t]. Euclidean reduction gives gcd(D,D')=gcd(D,C)=gcd(D,(t²-4)(t²+1))=1. Thus each block has rank one at every one of twelve distinct roots and rank two elsewhere in U. Inverse Frobenius preserves matrix rank. The a-number is consequently 3 or 0 as claimed; full Cartier rank yields ordinarity, but rank three does not give the exceptional p-rank.

## originality

PASS

The pencil and its Wiman member are classical; the exact characteristic-seven ordinary answer at t=0 is also established. The distinct claim is the entire rank locus in the stated plane parameter, including a=3 at all twelve roots. The inspected geometric and singleton computations do not give this statement or imply it.

## value

PASS

The calculation stratifies a classical genus-six pencil by a naturally varying arithmetic invariant, going beyond the known ordinary Wiman point. It gives the exact exceptional divisor and establishes that every jump removes three dimensions of Cartier rank rather than just detecting nonordinarity. This is usable information about the arithmetic family even without the further p-rank or Newton polygon classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
