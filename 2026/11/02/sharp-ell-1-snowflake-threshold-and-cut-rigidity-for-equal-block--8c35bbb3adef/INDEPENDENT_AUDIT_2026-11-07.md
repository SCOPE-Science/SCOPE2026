# Independent mathematical audit

## correctness

PASS

For every cut S with block counts a_i, directly count mean U on within-block pairs and W on cross-block pairs. Their exact difference W-(n-1)U/n =2 Σ_{i<j}(a_i-a_j)²/[r(r-1)n²] is a sum of squares. Cut-cone decomposition transfers it to all finite real ℓ1 metrics; noncontractive pair bounds imply D≥max(1,t(n-1)/n). Choose one vertex from each block uniformly to define B=n/2 Eδ_S, and P=1/2 Σδ_Ai; then B has pair distances 1 within and (n-1)/n across, while P has 0 within and 1 across. For t≤n/(n-1), tB+(1-t(n-1)/n)P realizes the original distances; above, tB attains D=t(n-1)/n. Equality in sums of squares and pairwise averages enforces balanced-support cuts and metric rigidity. All r,n≥2, t∈[1,2], and threshold equality explicitly covered. Independent exact Fraction all-cut enumeration for (2,3),(3,2),(3,3), respective 64,64,512 cuts corroborates identity; the analytic identity proves arbitrary r,n.

## originality

PASS

The negative-type literature for complete multipartite powered graph metrics supports necessity of the isometric cutoff, but an L1 distortion equality and every-optimum supporting-cut rigidity are different assertions. Facet-count and Lipschitz-free projection-invariant findings for the same graphs are not the pointwise L1 embedding distortion. Originality attaches to matching construction and rigidity, not the classical cut cone or numerical necessary obstruction.

## value

PASS

Real ℓ1 embeddability of natural balanced complete multipartite shortest-path snowflakes has a sharp exact threshold and quantitative supercritical distortion. The sum-of-squares supporting-cut criterion classifies all optimal embeddings at and above the threshold, beyond a routine toy example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
