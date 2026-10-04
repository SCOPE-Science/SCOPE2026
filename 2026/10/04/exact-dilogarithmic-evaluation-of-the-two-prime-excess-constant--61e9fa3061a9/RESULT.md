# Exact dilogarithmic evaluation of the two-prime excess constant
## Finding
For the piecewise profile \(G\) used in the two-prime excess term of Hughes's density theorem, define \(I=\int_0^2 G(w)\,\mathrm{d}w\). Then
\[I=\frac{\pi^2}{3}+6\operatorname{Li}_2\!\left(-\frac34\right)-2\operatorname{Li}_2\!\left(-\frac12\right)+(\log 2)^2+3(\log 3)^2-6\log 2\log 3+14\log 7-20\log 2-12\log 3.\]
The numerical value is \(I=0.058879779905129229210273471667\ldots\), matching the value reported by quadrature in the source.

## Assumptions and scope
The function \(G\) is exactly the three-piece function in equation (18) of arXiv:2609.25446v1: on \(0\le w\le1\),
\[G(w)=1-rac{2}{w+2}\left(1+\lograc{w+2}{2}ight);\]
on \(1\le w\lerac32\),
\[G(w)=rac{4-3w-2\log(3/(2w))+4\log((w+2)/3)}{w+2};\]
and on \(rac32\le w\le2\),
\[G(w)=rac{w-2+4\log((w+2)/(2w))}{w+2}.\]
Here \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\) for the arguments used below. No statement is made about the unresolved asymptotic form of the densities \(d_t\).

## Proof
Put
\[\Phi(w)=\log w\,\log\left(1+rac w2ight)+\operatorname{Li}_2\!\left(-rac w2ight).\]
From the defining dilogarithm series (or its standard derivative),
\[\Phi'(w)=rac{\log w}{w+2}.\]
The first piece integrates directly:
\[I_1=\int_0^1G(w)\,\mathrm{d}w=1-2\lograc32-\left(\lograc32ight)^2.\]
For the second piece, rewrite its rational part as \(-3+10/(w+2)\). An antiderivative on \([1,3/2]\) is
\[A_2(w)=-3w+\left(10-2\lograc32ight)\log(w+2)+2\Phi(w)+2\left(\lograc{w+2}3ight)^2.\]
For the third piece, an antiderivative on \([3/2,2]\) is
\[A_3(w)=w-4\log(w+2)+2(\log(w+2))^2-4\log2\,\log(w+2)-4\Phi(w).\]
Therefore \(I=I_1+A_2(3/2)-A_2(1)+A_3(2)-A_3(3/2)\). The only dilogarithm values that occur are \(\operatorname{Li}_2(-1/2)\), \(\operatorname{Li}_2(-3/4)\), and \(\operatorname{Li}_2(-1)=-\pi^2/12\). Substitution of the endpoints and collection of logarithms gives exactly the displayed formula.

## Verification
The accompanying `verify.py` evaluates the two negative-rational dilogarithms from their convergent power series and independently integrates the published three pieces by split Simpson quadrature. Its recorded output is `VERIFY_OK closed=0.05887977990512816 direct=0.058879779905129243 abs_diff=1.08e-15`. The computation is corroborative; the proof is the exact antiderivative calculation above.

## Relationship to prior work
Hughes defines the same \(I\), reports \(I=0.0588797799\ldots\), and uses it in the lower bound \(\liminf_{t	o\infty}(\log t)(d_t-
u_t)\ge KI\). Section 5 gives the three explicit pieces of \(G\), states that the first piece integrates in closed form, and obtains the full \(I\) by high-precision quadrature plus a separate rational lower-bound certification. The source does not give an exact closed form for the full integral. Searches for the exact decimal, the same profile, and a dilogarithmic evaluation did not identify a prior same-statement formula. NIST DLMF §25.12 supplies the standard dilogarithm definition used in the proof.

## Limitations
This result evaluates a constant already defined by the source. It does not improve Hughes's asymptotic lower bound, prove existence of a limiting constant for \(d_t\log t\), or resolve Erdős Problem #859. Novelty searches reduce but cannot eliminate the risk of an unindexed equivalent symbolic evaluation.

## References
1. Scott D. Hughes, *The density of sums of distinct divisors*, arXiv:2609.25446v1, 21 September 2026.
2. NIST Digital Library of Mathematical Functions, §25.12, *Polylogarithms*.
