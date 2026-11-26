# Independent mathematical audit

## correctness

PASS

On the upper triangle the triplet (x,y,2−x−y) is cyclically permuted and all three states remain in the triangle. Below it the linear branch A(x,y)=(y,x+y) has nondecreasing coordinate sum along its iterates. Thus T≥n iff the sum at the (n−1)st linear iterate is less than one, i.e. F_n x+F_{n+1}y<1. The two intercepts are within the square, and the difference of successive triangle areas is 1/(2F_nF_{n+2}); the upper triangle itself has area 1/2. Shrinking support allows uniform replacement of h by h(0,0), yielding both constants by Binet's formula and divergence at the critical moment exponent because the summands do not tend to zero. In coordinates u=F_n x,v=F_{n+1}y the normalized entry band converges in area to φ⁻¹≤u+v≤1; its limiting density is uniform since h(0,0)>0. The landing map tends uniformly to ((u+v)/φ,u+v), and the section u+v=t has length t in the measure coordinates (t,u). This gives the stated normalized weak limit as n→∞ (not a finite-n singular law). VERIFICATION.md and verify.py describe/check finite polygon areas at n=1,…,19 only; the final pre-entry check in the loop is waived on the last step, so strict entry timing is established by the proof, not that loop. The supplied code was inspected, not run.

## originality

PASS

Credit the critical half-memory dynamics and Fibonacci recurrence to Góra et al.; the uniform formulas are direct area consequences and the moment threshold follows from the mass asymptotic. The distinct contribution supported by the comparison is the quantitative entrance analysis, especially the normalized limiting landing distribution for all stated source densities. No priority claim is made for the recurrence or for a new derivation of eventual periodicity.

## value

PASS

The conditional law answers where unusually late entrants reach the periodic region, not just whether or how fast they arrive. It identifies both the singular ray and the nonuniform probability measure along it, and shows why the law is insensitive to the source density near the repelling origin. These are useful quantitative additions to the previously known periodic dynamics at this critical parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
