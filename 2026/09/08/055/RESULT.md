# Apolarity invariants for a P5 Perazzo-type quartic with three-variable base

## Context

Consider the quartic
\[
F^* = x_0u^3+x_1v^3+x_2(u+v)^3+w^4
\]
over \(\mathbb{Q}\), viewed through Macaulay apolarity in six variables. This is a concrete Perazzo-type example with three base variables. The goal is an exact named-object computation; no classification theorem for the whole family is asserted.

## Result

Let \(A=R/\operatorname{Ann}(F^*)\).

1. The Hilbert vector is
\[
H(A)=(1,6,7,6,1).
\]

2. The classical first Hessian of \(F^*\) vanishes identically. The three rows corresponding to \(x_0,x_1,x_2\) have support only in the \(u,v\) columns, so they lie in a two-dimensional coordinate subspace.

3. Weak Lefschetz holds. For
\[
L^*=x_0+x_1+x_2+u+v+w,
\]
the map \(A_1\to A_2\) has rank \(6\), with an exhibited \(6\times6\) minor equal to \(2\), and the map \(A_2\to A_3\) has rank \(6\), with an exhibited \(6\times6\) minor equal to \(4\). The outer maps have rank \(1\).

4. The graded Betti rows \(\beta_{i,t}\) are:
- \(t=0\): \(1,0,0,0,0,0,0\)
- \(t=1\): \(0,0,0,0,0,0,0\)
- \(t=2\): \(0,14,0,0,0,0,0\)
- \(t=3\): \(0,2,36,0,0,0,0\)
- \(t=4\): \(0,4,8,39,0,0,0\)
- \(t=5\): \(0,0,20,12,20,0,0\)
- \(t=6\): \(0,0,0,39,8,4,0\)
- \(t=7\): \(0,0,0,0,36,2,0\)
- \(t=8\): \(0,0,0,0,0,14,0\)
- \(t=9\): \(0,0,0,0,0,0,0\)
- \(t=10\): \(0,0,0,0,0,0,1\).

Therefore \(\operatorname{Ann}(F^*)\) has **14 quadratic, 2 cubic, and 4 quartic minimal generators**. The projective dimension is \(6\) and the regularity is \(4\).

## Evidence

Exact rational apolar computation gives catalecticant ranks \(1,6,7,6,1\). A direct symbolic determinant calculation gives the zero Hessian. Quotient-basis multiplication matrices for \(L^*\) give the two full middle ranks and the minors \(2\) and \(4\). Koszul-complex rank-nullity gives the displayed Betti rows; the rows satisfy the Euler/Hilbert identities and Gorenstein symmetry. A fresh independent recomputation reproduced all of these values.

## Limitations

- This is one named object, not a classification of the three-variable-base Perazzo family.
- The Betti table is an exact Koszul--Tor computation rather than a structural minimal-resolution argument.
- The annihilator generator counts follow from the first Betti column; an explicit minimal generating set is not displayed.
- WLP is certified by one explicit Lefschetz element; the full Lefschetz locus is not described.

## Reproducibility

The committed verifier `artifacts/verify_Fstar.py` reconstructs the catalecticants, Hessian, multiplication maps and Koszul homology in exact arithmetic.

## References

- L. Fiorindo, E. Mezzetti, R. M. Miró-Roig, *Perazzo 3-folds and the weak Lefschetz property*, arXiv:2206.02723.
- R. M. Miró-Roig, J. Pérez-Díez, *Perazzo hypersurfaces and the weak Lefschetz property*, arXiv:2402.09188.
- E. Mezzetti, R. M. Miró-Roig, *Perazzo n-folds and the weak Lefschetz property*, arXiv:2405.14756.
