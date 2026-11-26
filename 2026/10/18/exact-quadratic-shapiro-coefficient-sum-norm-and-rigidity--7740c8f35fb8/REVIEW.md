# Independent mathematical audit

## correctness

PASS

On the complex degree-at-most-two space let ζ=e^{iπ/3}. Using ζ²=ζ−1 and λ=(2−ζ)/3, the real-conjugate pair of weights on ζ,ζ̄ has moments (1,1,0), with each absolute weight 1/√3. This certifies the upper bound on the full complex ball. Independently, expanding the modulus square of the numerator gives 21+8 cos t−4 cos(2t)=27−8(cos t−1/2)², with exactly the two stated contacts. Equality after fixing the scalar phase makes both evaluations match p_*. Their difference is c(z²−z+1); subtracting the boundary stationarity equations at the contacts gives the coefficients −(1+ζ) and 1+ζ̄ acting by real part on c, with determinant −3√3/2 in real coordinates. This forces c=0, including when lower-degree polynomials are allowed. The frozen SymPy verifier was inspected, not executed; these exact reductions independently check its decisive identities and uniqueness argument.

## originality

PASS

Technau discusses exactly M_{1,3} but supplies only a strictly larger upper bound. The evidence supports the exact constant and phase rigidity as distinct from the inspected earlier statements. A later indexed stronger bidisk theorem materially overlaps both claims and is not counted as earlier coverage based on its later date.

## value

PASS

The invariant is a singled-out odd-cutoff case of a named partial-sums problem with a published nonsharp bound at precisely this parameter. The sharp value, explicit extremizer and complete complex rigidity are independently usable; the contribution is not a numerical improvement alone and does not purport to solve other cutoffs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
