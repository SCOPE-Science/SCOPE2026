# Certified audit tuple for the Fermat-plus-tail dual septic in the socle-7 compressed cell

## Context

Whether every codimension-3 Artinian Gorenstein algebra over a field of
characteristic zero has the Weak Lefschetz Property (WLP) is open. Boij et
al. reduce the problem to compressed algebras of odd socle degree and settle
the first open case with Hilbert function (1,3,6,6,3,1). The 2024
small-Sperner theorem proves WLP when the Sperner number is at most d+1 and
states it is still open when socle degree and Sperner number are both above
6. The next compressed cell, socle degree 7 with Hilbert function
(1,3,6,10,10,6,3,1) (socle d=7, Sperner 10 > d+1=8), lies in that open
region. Macaulay inverse-system duality, higher-Hessian criteria
(Maeno–Watanabe, Gondim), Jordan-type stratification, and the
Buchsbaum–Eisenbud structure theorem for codimension-3 Gorenstein ideals are
the surrounding programs.

## Definitions

Let k = QQ, S = k[x,y,z] acting by ordinary differentiation on R = k[X,Y,Z].
For homogeneous F of degree 7, A = S/Ann(F) is the apolar Artinian Gorenstein
algebra of socle degree 7. F is compressed when its Hilbert function is the
maximal (1,3,6,10,10,6,3,1) (total length 40). Hess^2(F) is the second higher
Hessian: determinant of the 6x6 matrix (d_a d_b F) over second-order
differential operators. L = x+2y+3z is the logged linear form; x_L denotes
multiplication by L. Jordan type is the partition of 40 given by the Jordan
blocks of x_L. mu_d counts minimal generators of Ann(F) in degree d.
Buchsbaum–Eisenbud: a codimension-3 Gorenstein ideal with 5 generators is a
5x5 pfaffian (all generators quartic here); one with 7 generators a 7x7
pfaffian.

## Result

For F0 = X^7+Y^7+Z^7+X^3 Y^2 Z^2 over QQ, A0 = S/Ann(F0):

- Hilbert function (1,3,6,10,10,6,3,1), length 40.
- Second higher Hessian (6x6, cubic entries):
  det = 4423680 X^4 (21 X^10 Y^2 Z^2 + 2205 X^7 Y^7 + 2205 X^7 Z^7
  + X^6 Y^4 Z^4 + 231525 X^4 Y^5 Z^5 + 126 X^3 Y^9 Z^2
  + 126 X^3 Y^2 Z^9 + 15435 Y^7 Z^7), not identically zero.
- At L = x+2y+3z, x_L:[A0]_3 -> [A0]_4 has rank 10 with determinant -36;
  full rank profile across degrees 0->1 through 6->7 is maximal:
  (1,3,6,10,6,3,1). Hence A0 has WLP at L.
- Jordan type of x_L is [8,6,6,4,4,4,2,2,2,2] (10 blocks, sum 40;
  kernel dimensions of powers 0..9: 0,10,20,26,32,35,38,39,40,40).
- Minimal generator degrees of Ann(F0): mu_4 = 5, mu_5 = 2, else 0
  (annihilator dimensions 0,0,0,0,5,15,25,35; R1*I_4 has rank 13 inside the
  15-dimensional I_5; R1*I_5 spans I_6). So 5 quartic + 2 quintic minimal
  generators: quartic count matches a 5x5 pfaffian count, total count matches
  a 7x7 pfaffian count, but the degree distribution is mixed (neither pure
  5x5 nor pure 7x7).
- Bridge identity: det(x_L:A3->A4) = -hess^3(point)/2796089100573081600,
  checked at 8 integer points.

## Proof / evidence

Exact QQ computer algebra, replayable via `python3 output/artifacts/verify_F0.py`
(stdlib + sympy, prints VERIFY_OK): catalecticant ranks for the Hilbert
function; symbolic 6x6 Hessian determinant plus factorization; quotient-basis
multiplication matrices via catalecticant projection giving exact ranks,
middle-block determinant, and kernel dimensions yielding the Jordan
partition; annihilator nullspaces with product-containment check giving mu
values. Staged scripts step1/step2/step3/step4/step12 log each component;
step11 logs the bridge identity. Independently re-executed during audit with
byte-matching numbers.

## Limitations

Universal WLP over the (1,3,6,10,10,6,3,1) cell is NOT proved; a ~140-septic
plausibility sweep (all Hessian-nonsingular at probes) is uncertified
context only. F0 itself HAS WLP, so it is a positive boundary data point,
not a failure witness. Jordan type is for the logged L (full maximal rank
profile) rather than a proved generic Jordan type. Buchsbaum–Eisenbud
comparison is a minimal-generator-degree count/degree comparison, not a full
printed minimal free resolution with differentials. No Macaulay2/Singular on
host; replay uses exact sympy linear algebra. Ordinary derivatives introduce
nonzero factorial scalars versus divided-power conventions; nonvanishing and
ranks are unaffected over QQ.

## Reproducibility

Run `python3 output/artifacts/verify_F0.py` (requires sympy); expect
HilbertFunction [1,3,6,10,10,6,3,1], factored Hess2 as above, mid-block det
-36 rank 10, Jordan [8,6,6,4,4,4,2,2,2,2], mu {4:5, 5:2}, and VERIFY_OK.
Runtime minutes.

## References

- Boij–Migliore–Miro-Roig–Nagel–Zanello, arXiv:1302.5742 (codim-3 WLP
  reduction; socle-5 cell).
- Boij–Migliore–Miro-Roig–Nagel, arXiv:2406.17943 (Sperner <= d+1; stated
  open region socle and Sperner both >6).
- Maeno–Watanabe, arXiv:0903.3581 (higher-Hessian criterion).
- Gondim, arXiv:1506.06387 (higher Hessians; failures in codim >= 4).
- Altafi, arXiv:2007.10684 (SLP Hilbert functions / SI-sequences).
- Altafi et al., arXiv:2502.18149 (codim-3 SLP for binomial dual generators).
