# Independent mathematical audit

## correctness

PASS

For the equal Bernoulli base the order-two transform is uniform. Multiplicative closure and compact support follow from Mergny, Theorem 1.4(ii) and Proposition 3.4. The frozen proof's citation to Lemma 3.1(i) alone omits the compactness step; Proposition 3.4 in the same paper supplies it. Product moments are (n+1)^(-k), so summing the second-order resolvent gives Li_(k-1)(1/z)/z; its negative half logarithmic derivative gives the stated ordinary resolvent. The exact nonzero imaginary part of the cut denominator gives locally uniform analytic boundary values and permits Stieltjes inversion without interior singular mass. On the negative axis the successive-polylog quotient is O(1/log(1/|z|)), yielding the half atom; at 1 the quotient is at most logarithmic, yielding no atom. For p=k-1 and y=log(1/x), the real leading terms -y^s/s! and exact imaginary terms -pi*y^(s-1)/(s-1)! give imaginary quotient asymptotic -pi*p/y^2, including p=2. At y approaching zero the numerator jump dominates the denominator jump by one power (up to a logarithm at p=2), giving the stated zeta coefficient. Expanding the logarithmic derivative also gives both proposed raw moments. RESULT.md lines 37–62 give the replay path. The inspected finite checker is supplemental and was not used as the all-power proof.

## originality

PASS

Pass for the explicit higher-power measure classification, not the closure theorem, the general inversion method, or the second-power benchmark. No inspected source covers the complete k>=3 atom and endpoint hierarchy.

## value

PASS

The symmetric two-point law at order two is the natural seed whose Dirichlet mean is uniform, not an arbitrary numerical slice. Determining exactly how half the mass remains atomic at every finite power, while the positive half has a fixed logarithmic singularity type at zero and a power-dependent vanishing order at one, gives distributional information not available from closure or the first moments. The full edge and mass analysis, rather than the formal series substitution, supplies the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
