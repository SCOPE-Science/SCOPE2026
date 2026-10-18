# Independent mathematical audit

## correctness

PASS

The two explicit five-by-eight code matrices match the original paper’s weak-flip column vectors. For any received output support Y, maximum likelihood is attained by the minimum-weight codeword containing Y (all 0<p<1). Complete independent 256-output enumeration gives 5P_rec=5-4p^3-2p^5+2p^7 and 5P_dis=5-p^2-2p^3-2p^5-p^6+2p^8. Their difference is p^2(1-p)^2(1+p)(2p^3+p-1). The cubic is strictly increasing with one zero rho about 0.5897545; for rho<p<1 the alternative strictly outperforms the conjectured recursive base. At p=9/10, exact gain in average success is 1044981/250000000, independently obtained with rational likelihood enumeration.

## originality

PASS

Chen, Lin, and Moser expressly conjecture optimality for five Z-channel messages (2011 equations 25-29; 2013 equations 88-92). Their length-eight base is precisely the challenged column sequence; their proven M<=4 cases do not cover it. The competing code rearranges original weak-flip columns and establishes an exact, stronger-performance witness not in the inspected primary treatments. No located published or database statement supplies this high-noise falsifier.

## value

PASS

A constructive, exactly verified counterexample refutes the starting base case of a specific published recursive coding-optimality conjecture under precisely the original channel, blocklength, alphabet, uniform prior, and ML decoding. The interval of failure and exact fidelity/error gain are independently useful, despite not determining the globally best code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
