# Independent mathematical audit

## correctness

PASS

For symmetric two-habitat phase generator A_i=[[r_i1-m,m],[m,r_i2-m]] with a single m>0 and positive durations, reconstructed E_i=exp(tau_i a_i)(cosh(tau_i d_i)I+q_i B_i), B_i=[[b_i,m],[m,-b_i]], q_i>0. Since E_i are symmetric positive definite, cyclic trace and reversal show all products of at most three phases have identical trace, and their common determinant fixes the full 2x2 spectrum and Floquet rate. For four phases independently expanded the only order-sensitive trace term and symbolically verified tr(B1 B2 B3 B4)-tr(B1 B3 B2 B4)=4m²(b1-b4)(b2-b3). Thus the sign law follows from positive common scalar and strict monotonicity of the Perron root in trace at fixed positive determinant. Dihedral action on four permutations yields three trace classes, all distinct for four distinct contrasts. For tau_i=m=1, b=(1,-1,2,-2), and r_{i1/2}=+/-b_i-2/5, the displayed exact exponential-trace brackets certify Lambda_1234<0<Lambda_1324. Independently checked the polynomial identity symbolically, and numerical 65-digit evaluation corroborated the strict witness; original standalone verify.py uses rational series/tail certificate inspected but was not trusted as proof without the independent analytic reconstruction.

## originality

PASS

The precise minimum four-phase order-sensitivity threshold, exact signed contrast-product law, three dihedral orbit values and same-multiset extinction/growth witness are assessed; general dispersal-induced growth and ordered noncommutative Floquet products are prior mathematics. Available primary ecological texts do not present this exact finite-permutation classification in inspected sections; related matrix-product literature remains a residual risk.

## value

PASS

Determines a sharp structural threshold for chronology effects in a canonical two-patch ecological ODE, with an exact signed law that predicts which ordering increases growth and a certified extinction-to-growth reversal without changing seasons or migration. This clarifies when temporal ordering itself can change the linear persistence boundary. Fixed symmetric migration and linearity are essential scope restrictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
