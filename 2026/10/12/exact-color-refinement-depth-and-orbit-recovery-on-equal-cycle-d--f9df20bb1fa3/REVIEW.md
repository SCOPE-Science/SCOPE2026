# Self-review

## Correctness
PASS. The graph has only two degree-three vertices, and symmetry keeps them in one color class in every round. On each degree-two thread, round-\(r\) colors are exactly the unordered clipped endpoint-distance pairs. This gives the within-thread thresholds \(\lfloor m/2\rfloor\) and \(\lceil k/2\rceil\). For unequal thread lengths, endpoint-adjacent vertices realize the latest cross-thread collision and split exactly at the shorter thread length; equality of clipped pairs beyond that point would force equal total thread lengths. When the lengths coincide, cross-thread positions remain color-equivalent forever. The orbit statement then follows from cut-vertex status on the connector versus non-cut cycle vertices. The standalone checker verifies 2828 parameter pairs.

## Originality
PASS with residual priority risk. published-finding corpus searches for dumbbell/handcuff color-refinement depth, Weisfeiler--Leman iteration number, and the equal-length resonance returned no matching finding. The inspected dumbbell papers define and study this family spectrally; they do not discuss color refinement. Krebs--Verbitsky supplies only the general universal-cover/refinement framework. No inspected source states the piecewise stabilization formula or the exact resonance criterion for orbit recovery.

## Value
PASS. Dumbbell graphs are a standard bicyclic family, and the result identifies a structural phenomenon rather than a routine numeric table: equality of the cycle and connector thread lengths creates a precise \(1\)-WL resonance where refinement ceases to recover automorphism orbits. The same thread calculation gives a complete exact iteration law off resonance. This supplies a compact benchmark for how cycle structure can become invisible to color refinement despite being automorphism-theoretically decisive.

## Closest literature and limitations
The closest object-specific sources are Wang--Belardo--Huang--Li Marzi (2010) and Liu--Lu (2014), both on spectral determination of dumbbell graphs. The closest methodological source is Krebs--Verbitsky (2014) on universal covers and color-refinement depth. None of the inspected material gives the present formula. Unequal cycle lengths are not covered.

Self-review: passed. Independent audit: not yet performed.
