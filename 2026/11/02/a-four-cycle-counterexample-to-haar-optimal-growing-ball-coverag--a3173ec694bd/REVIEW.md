# Independent mathematical audit

## correctness

PASS

For S=Z/4Z with shortest-cycle distance, unit-rate Poisson arrivals and unit-speed expanding closed balls, the tail of the first all-site cover time follows by inclusion-exclusion of all 15 nonempty target subsets. For a subset A, the Poisson void intensity has successive slopes a=mu(A), b=mu(B(A,1)),1 on the intervals [0,1],[1,2],[2,infinity); integrating gives I(a,b)=(1-e^-a)/a + e^-a(1-e^-b)/b + e^-a-b (continuous at a=0,b=0). Independent from-scratch subset enumeration recovers E_h=25/3-(32/3)e^-1/4+6e^-1/2-(4/3)e^-3/4-(4/3)e^-1 =2.544980946964... for uniform Haar h and E_nu=2+2e^-1/2-2e^-1=2.477302437082... for antipodal nu=(1/2,0,1/2,0). Independently, thinning gives first arrival at two supported sites as independent Exp(1/2), with C_nu=M+max(1,min(G,2)), M~Exp(1), G~Exp(1/2). Alternating exact rational Taylor bounds yield 0.0676785098698< E_h-E_nu <0.0676785099821. Thus Haar is strictly not optimal; there is no global optimizer claim. Full result and exact verifier blobs inspected in frozen Git tree.

## originality

PASS

Best-of-knowledge PASS for explicit negative answer on the smallest nontrivial cycle to the unrestricted compact-group Haar minimization question for Poisson growing balls. Aldous 2022 explicitly formulates the growth-model question, and the previously known fixed-radius nonuniform examples are not growing-ball counterexamples. Related structured coupon collector examples use fixed-radius/discrete coupons rather than expanding metric balls. Priority risk for an independently published finite-group witness remains.

## value

PASS

An elementary, exact, robust strict counterexample answers an explicit research question about Haar optimality in the general growing-ball model. It distinguishes the geometric group-invariance property from optimal center law. Even a four-point counterexample is valuable because it settles the unrestricted conjectural principle, without claiming connected-group behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
