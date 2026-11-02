# Independent mathematical audit

## correctness

PASS

For P=z0+[0,1]u+[0,1]v with independent area-uniform X,Y, the coordinate differences xi,eta are independent triangular random variables with even moments E xi^(2j)=2/((2j+1)(2j+2)). With A=u·u>0, B=v·v>0, C=u·v and C²<AB, one has R²=A xi²+B eta²+2C xi eta. Independently expanded the polynomial with exact SymPy coefficients: M2=(A+B)/6, M4=(6A²+5AB+6B²+10C²)/90, M6=(A+B)(15A²-AB+15B²+56C²)/420, agreeing identically with RESULT.md. Setting S=A+B, p=AB/S², q=C²/S² yields precisely 0<p≤1/4 and 0≤q<p. The independent normalized-moment linear algebra gives x=12/5-14p/5+4q, y=54/7-558p/35+144q/5, inverse p=93/41-70x/41+175y/738, q=81/82-155x/164+245y/1476; all three boundary vertices were exactly confirmed. The parameter triangle maps invertibly onto triangle A=(12/5,54/7), B=(17/10,261/70), C=(27/10,153/14) with entire side AC omitted; its other two edges represent rectangles and rhombi. Reconstruction of unordered A,B and |C| is unique up to congruence; varying p between 1/7 and 1/4 with q=7p/10-1/10 yields continuum with M2=1,M4=2. On compact nondegenerate shape families, inverse of affine data is Lipschitz before taking square roots; signed-angle and equal-side degeneracies yield exact 1/2 Hölder and the transverse rectangle perturbation has moment change O(t²) but shape change O(t), proving optimality. A Monte Carlo sample in the package is corroboration only.

## originality

PASS

The inverse covariogram theorem reconstructs planar convex bodies from the entire direction-labeled covariogram—much richer data than three scalar distance moments—and does NOT yield their minimal finite sufficiency. Gasparyan–Ohanyan and Martirosyan study direction-dependent random-line chord/covariogram distributions, not the independent area-uniform endpoint distance M2/M4/M6 inverse problem. Two Resultary parallelogram records were read in full: one uses projection WIDTH statistics (mean, second moment, diameter) and an angle inversion; another compares the boundary-to-interior FOURTH distance moment and angular phase transition. Neither treats the full triple of interior even moments, affine feasible triangle or 2-moment nonidentifiability. Best-of-knowledge originality therefore survives these stronger/nearby comparisons, with alias priority risk.

## value

PASS

The shape-from-statistics problem is a natural inverse geometric probability question. The theorem determines the entire feasible region for dimensionless observations, proves a sharp threshold of exactly three consecutive even distance moments for congruence reconstruction, supplies an explicit inverse without genericity restrictions, and gives quantitatively optimal 1/2-Hölder stability near the rectangle symmetry. These are intrinsic unknown exact invariants relevant to statistical shape retrieval, not mere formula substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
