# High-precision numerical calibration of a 6-torsion elliptic-dilogarithm ratio on the CM curve y^2 = x^3 + 1

## Context

Let E/Q be y^2=x^3+1, Cremona label 36a1 (LMFDB member 36.a4 in isogeny class 36.a). Let U=(2,3), V=(-1,0), and
xi = 3[(U)-(O)] - [(V)-(O)].
The original target proposed the exact identity

L(E,2)/pi = (1/12) D_q(xi),

for a stated Tate-uniformization convention. This record now distinguishes the exact finite group-law facts from the numerical regulator/L-value experiment.

## Exact finite arithmetic

The following statements are rigorous over Q:

- U and V lie on E.
- 2U=(0,1).
- 3U=V=(-1,0).
- 6U=O, so U has exact order 6.
- 2V=O, so V has exact order 2.
- xi has degree zero, and the point relation 3U-V=O holds.

These assertions follow from the ordinary rational group law on y^2=x^3+1.

## Numerical experiment

Using the convention

q = -exp(-pi*sqrt(3)),
z_U = i exp(-5*pi*sqrt(3)/6),
z_V = -i exp(-pi*sqrt(3)/2),

and the Bloch-Wigner lattice sum D_q(z)=sum_{n in Z} D(q^n z), high-precision computation gives

D_q(U) ≈ -0.673234725134315088298051383701,
D_q(V) ≈ 0,
D_q(xi) ≈ -2.01970417540294526489415415110.

The repository's PARI computation reports

L(E,2) ≈ 0.9400130073882257815,
L(E,2)/pi ≈ 0.29921543339302892813.

Combining these numerical values gives

(1/12) D_q(xi) ≈ -0.16830868128357877207,

which is far from the listed positive L(E,2)/pi value, and

(L(E,2)/pi) / D_q(xi) ≈ -0.14814814814814814815,

suggesting the rational factor -4/27.

Accordingly, the numerical data strongly suggest the conjectural calibration

L(E,2)/pi = -(4/27) D_q(xi)

under the stated conventions.

## What is and is not proved

This package does **not** provide a rigorous disproof of the 1/12 identity and does **not** prove the -4/27 identity. The Bloch-Wigner lattice sum is evaluated numerically without a certified truncation/roundoff enclosure, and the L-value is imported from a PARI computation without a rigorous interval certificate in this package. The large numerical gap is persuasive computational evidence, but an exact equality or inequality requires validated error bounds or a symbolic regulator formula.

The exact theorem content of this record is therefore limited to the rational torsion/divisor arithmetic above. The regulator comparison and -4/27 factor are a reproducible high-precision numerical observation and conjecture.

## Independent audit reproduction

The independent audit recomputed the regulator side from the closed-form q, z_U, and z_V at 70-digit precision. For D_q(U), truncations M=30,60,90 agree at the displayed digits; D_q(V) is numerically zero at this precision. The audit did not rerun the PARI L-function computation and does not promote the numerical experiment to an exact theorem.

## Reproducibility

- `artifacts/compute_ratio.py` reproduces the PARI/mpmath experiment when cypari/PARI is available.
- `artifacts/closedform_check.py` supplies the auxiliary closed-form/Euler checks retained from the original package.

## Literature context

General Bloch and elliptic-dilogarithm regulator theory explains why such comparisons are natural. The present record makes no claim of a new general regulator theorem; its research contribution is the concrete numerical calibration target for this specific 6-torsion divisor on y^2=x^3+1.

## Limitations

No certified interval arithmetic for D_q or L(E,2) is included. The -4/27 relation is conjectural. Convention choices for the elliptic dilogarithm and uniformization must be fixed exactly before any future symbolic proof is compared with this numerical factor.
