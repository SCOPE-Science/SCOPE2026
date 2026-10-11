# Independent mathematical audit

## correctness

PASS

For any integer \(j\ge0\), the quadratic \(Q_j(x)=(x+j)(x+j+1)/[(k+j)(k+j+1)]\) is nonnegative on every integer below \(k\) and at least one on every integer at least \(k\). Taking expectations gives \(\Pr(X\ge k)\le[v+j(j+1)]/[(k+j)(k+j+1)]\). With \(j=\lfloor v/k\rfloor\), the three displayed masses on \(k,-j,-j-1\) are nonnegative and solve the mass, mean and second-moment equations, so the bound is attained. Equality in the pointwise majorant restricts support to those three lattice points, giving uniqueness after deleting zero masses. Writing \(v=kj+r\) yields the exact positive Cantelli gap by direct algebra. The inspected exact-rational verifier checks the moment identities, majorant and gap formula over broad rational test data, while the theorem follows from the infinite-lattice sign argument.

## originality

PASS

Targeted searches for sharp integer-valued, lattice-valued, discrete one-sided Chebyshev/Cantelli inequalities, the consecutive-root quadratic, and the exact rational formula did not locate an equivalent statement. The inspected modern generalized-moment literature explains polynomial-majorant duality but treats different support classes; Ghosh's accessible abstract treats arbitrary and nonnegative laws, not integer support; Troffaes--Basu use exchangeable sample statistics. Thus the exact lattice correction, universal three-point extremizer and uniqueness remain best-of-knowledge original.

## value

PASS

The theorem gives the exact sharp correction to one of the standard one-sided moment inequalities when the support is quantized, including all variances, an explicit unique extremizer and the exact gain over the continuous bound. This is a natural complete lattice moment problem with reusable sharp constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
