# Independent mathematical audit

## correctness

PASS

The Fourier transform over the splitting field is invertible; descent by the 16-power Frobenius gives one independent base-field constraint for zero and two for each nonzero conjugate pair. Thus the new dimension is 282. The 1,a,a^(-1) Vandermonde excludes support of size at most three when first coordinates are distinct. With exactly two distinct first coordinates, the singleton is killed by 1,a and the remaining coefficients by 1,b; with one first coordinate use the second-coordinate Vandermonde. For the upper bound, rectangles with coefficients 1 handle zero exponents. On each four-point norm-one line, the three-row matrix has a one-dimensional kernel with all cofactors nonzero; Frobenius swaps its last two rows, so the unique null vector normalized to first entry 1 is fixed by Frobenius. This independently verifies the subfield-coefficient step behind the divided differences. An independent polynomial-arithmetic and cofactor replay, /workspace/review-evidence/5/replay.py, checked all 2,380 four-subsets, reproduced the published count vector (accounting for its index w=k+1), and split all 142 new Frobenius orbits into 14 rectangle, 120 line, and 8 residual cases. The last 8 are covered by the two supplied words under independent axis inversions and axis exchange. The replay checked nonzero fixed-field coefficients and all seven Fourier equations for both words. This exhausts exactly the one-added-orbit family, not multiple additions or arbitrary codes.

## originality

PASS

The base code, distance four, extension question and general test are prior art. The distinct content is the exact negative result over F16 for this fixed base and all 142 new orbits. The closest primary text poses this problem and gives explicit outcomes at q=2,4,8, not the exhaustive q=16 verdict. No inspected catalogue or other source supplies that verdict.

## value

PASS

This is the next power of two after the successful q=8 example in the published one-added-orbit problem. Ruling out every such extension at q=16 resolves a motivated design case and shows that the preceding success does not persist at the next field size. The certificate is a complete result for a fixed-base family, not a claim about the best possible length-289 code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
