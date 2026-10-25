# Independent mathematical audit

## correctness

PASS

For a boundary side point x=(r,t), r=R cos α>0 and |t|≤s=R sin α, α=π/n, squared Euclidean distance restricted to each nondegenerate polygon edge is strictly convex, so its boundary maximum is at a polygon vertex. Every vertex lies at angle (2k+1)α. For odd n the antipodal target θ+π, |θ|≤α, has nearest vertex at π (with ties only at original-side endpoints), hence µ²=(R+r)²+t². For even n the nearest antipodal vertices are at π±α, yielding µ²=4r²+(s+|t|)². These exact expressions give unique minimizers t=0 per side, n boundary centers, squared defects t² and t²+2s|t|, plus the stated farthest vertices. Perimeter 2nR sin α divided by center values gives both exact ratios. Independent SymPy series reproduced odd π[1+π²/(12n²)+π⁴/(120n⁴)+O(n^-6)] and even π[1+5π²/(24n²)+61π⁴/(1920n⁴)+O(n^-6)]. An independent brute full-vertex maximum check for n=3..61 over 43 side points each made 81,184 vertex-distance comparisons, max abs squared error 1.33e-15. This finite test corroborates, not proves, the all-n claim; the proof is the angular order and convexity. All n≥5 and R>0 normalizations/boundaries accounted for.

## originality

PASS

Best-of-knowledge PASS for the complete all-n claim solely because its odd-family profile, exact quadratic stability and odd perimeter conjectural benchmark survive the primary-source and Resultary implication checks. IMPORTANT PRIOR COVERAGE: the published October 4 Resultary even-bisection result itself proves the entire even pointwise profile 4r²+(s+|t|)² and linear cusp (not just numerical radius). Thus those even ingredients carry NO independent originality. Walter 2016 gives an arbitrary fixed polygon finite algorithm, Balestro et al. 2021 treat triangles and a different maximization, and Nikitenko–Nikonorov 2023 conjecture odd n-gon global optimality without the odd profile. No compared prior source covers the odd family or combined parity statement. Historical risks remain explicit; prior-work attribution needs correction before publication.

## value

PASS

The odd regular n-gon profile gives an exact all-n candidate ratio 2n tan(π/(2n)) for the published odd n-gon minimum-perimeter-at-fixed-self-radius conjecture and classifies all boundary minimax centers and farthest chords, including best-possible exact t² displacement. This is a natural self-contained geometric classification and useful parameter-dependent benchmark, not an arbitrary slice. The parity contrast is real, but the even profile/cusp is ALREADY KNOWN and not itself counted as new value. The computation does not solve the global conjecture or assert n=3/4 novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
