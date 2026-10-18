# Independent mathematical audit

## correctness

PASS

PASS: B=I-A/L is simultaneously entrywise nonnegative and PSD for SPD Stieltjes A with L spectral maximum. From x_(m+1)=p_m(B)b/L, the exact polynomial recurrence gives p0=1, p1=1+(1+β)z, p2=1+z+(1+β)^2 z^2, p3=1+z+(1-β²)z²+(1+β)^3 z³, p4=1+z+z²+(1+β)²(1-2β)z³+(1+β)^4z⁴. All coefficients through p3 nonnegative; p4 likewise for β<=1/2 iff κ<=9. For κ>9, the PSD nonnegative four-path block C with (C³)_14=1,(C⁴)_14=6 embedded as Bε=diag(εC,1-1/κ) has exact spectral endpoints and a negative order-ε³ x5_1 for sufficiently small ε (despite positive ε⁴ term). Independently iterated the stated rational κ16 five-by-five matrix and found x5_1=-77/31250000000, with earlier first-coordinate values nonnegative. All-real κ sharpness rests on ε inequalities, not that sample.

## originality

PASS

PASS best-of-knowledge: Nesterov constant-parameter accelerated recurrence and rate are standard in Ghadimi–Feyzmahdavian–Johansson, but no finite-iterate entrywise Stieltjes cone statement there. A published heavy-ball result happens to have threshold nine yet uses different update and fails already at step two, so it does not imply this fifth-iterate Nesterov threshold. Published-finding search did not find an equivalent Nesterov positive-cone iff theorem.

## value

PASS

PASS: Identifies the first sharp nonnegative-cone violation iteration for exact spectrally tuned look-ahead Nesterov on an important inverse-positive SPD matrix class. The fifth-iterate threshold and explicit weak-coupling Stieltjes counterfamily matter for feasibility/positivity interpretation of accelerated solvers; not an objective-rate restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
