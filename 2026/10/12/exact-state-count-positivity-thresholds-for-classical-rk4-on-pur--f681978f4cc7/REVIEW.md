# Independent mathematical audit

## correctness

PASS

From Q=P-I and R4(z)=sum_{k=0}^4 z^k/k!, expand R4(xQ)=sum_{j=0}^4 a_j(x)P^j with a_j=x^j E_{4-j}(-x)/j!. For N=2, absorbing powers collapse: 1-a0>=0 iff x<=unique root rho2 of x^3-4x^2+12x-24. For N=3 the sign of a1 gives rho3; a2+a3+a4=x^2(3x^2-8x+12)/24>0. For N=4 first-row last entry is a3+a4=x^3(4-3x)/24, yielding 4/3. For N>=5 distinct first-row third-step entry a3=x^3(1-x)/6 becomes negative immediately after x=1, and 0<=x<=1 makes every coefficient nonnegative. All row sums remain one. Independent exact symbolic checks reproduced all five coefficient identities and rational witnesses N4,x=3/2:-9/128 and N5,x=6/5:-36/625; these checks corroborate the symbolic proof.

## originality

PASS

Horvath (2005) establishes broad positive-IVP step-size bounds, not the exact N=2,3,4,>=5 homogeneous absorbing-path classification in the accessible abstract. Lóczi--Ketcheson arXiv:1303.6651 develops absolute-monotonicity radius, yielding the universal RK4 radius 1 but not the finite-dimensional larger end-step windows. Related Resultary Padé, SSP-SDIRK and Crank--Nicolson findings have different stability maps and cannot imply this table. Relevant inaccessible older full text remains an explicit priority risk.

## value

PASS

The smallest pure-birth state count that witnesses the universal RK4 absolute-monotonicity barrier is a motivated and natural sharp finite cutoff; the exact smaller-state exceptions quantify how final-time stochasticity can persist when general sufficient RK positivity bounds fail. It is not a numerical toy parameter sweep or an arbitrary slice: the absorbing-path generator is canonical and the full N>=2 family is classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
