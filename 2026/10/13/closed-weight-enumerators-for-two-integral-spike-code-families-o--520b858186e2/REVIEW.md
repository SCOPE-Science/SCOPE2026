# Independent mathematical audit

## correctness

PASS

Systematic identity columns give a bijection from q^k input messages to codewords. With s=Σ_i u_i mod q, the s=0 sector contributes A via the additive-character count of j nonzero residues with sum zero, [(q−1)^j+(q−1)(−1)^j]/q. For each s≠0, the pair (u_i,s−u_i) weighs 1 if u_i∈{0,s} and 2 otherwise; the root-of-unity filter gives a factor (2+(q−2)z)^k and (1−z)^k Σ_{a≠0} ζ^(−as)(1+ζ^{as})^k. Summing nonzero s uses exactly gcd(q,j−1)−1 nonzero solutions to (j−1)s=0, valid even for zero divisors, giving B. This is an exact partition for all integer q≥2, not a field-only argument. Independently directly enumerated generator codewords for 15 small (k,q) pairs and verified coefficients of the formula. A(1)=q^{k−1}, B(1)=(q−1)q^{k−1}, so all q^k words counted. Finite tests only corroborate the uniform character proof.

## originality

PASS

Imamura–Nakashima–Saito arXiv:2601.21121 supplies these same integral code families, general Smith-normal-form subset enumeration, extrema and low-k tables. The present claim compresses all intermediate weight coefficients over arbitrary q to one binomial–gcd statistic and two explicit polynomials; the inspected primary formulas do not display this all-k,q special closed expression. Generic Tutte/coboundary descriptions may compute the distribution but do not constitute explicit this formula in inspected material. A possibly hidden older closed Tutte specialization remains a residual risk.

## value

PASS

Gives an explicit complete weight spectrum, including intermediate coefficients and composite-modulus torsion dependence, for two named integral spike code families previously treated via general subset algorithms, extrema and finite tables. A mathematically natural structural compression with usable closed formula across all k,q, not a tiny fixed instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
