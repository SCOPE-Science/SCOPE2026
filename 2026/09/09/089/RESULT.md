# First-power regularity with extremal induced-C8 witness on C_14(1,3)

## Context
Castelnuovo-Mumford regularity of (powers of) edge ideals is a recognized program
(Herzog-Hibi-Trung asymptotic linearity reg(I^s)=2s+b; Banerjee even-connection
method; Banerjee-Beyarslan-Ha bounds; Katzman induced-matching lower bounds;
Banerjee-Nevo bipartite upper bound reg(I^s)<=2s+reg(I)-2 for s>=2).
The 4-regular bipartite circulants C_n(1,3) are a natural test cell where no
powers formula or certified power value was recorded: the nearest complete
result (Hang-Pham-Vu, arXiv:2409.20161) covers only cubic (3-regular)
circulants, while C_14(1,3) is 4-regular and outside it. The admitted target
(reg(I^s)=2s+2 for all s>=2) and preset fallback (reg(I^2)=6) remain open;
this record certifies the first-power foundation every powers argument on
this cell must cite.

## Definitions
- G = C_14(1,3): vertex set Z_14, edges {i,i+1} and {i,i+3} mod 14
  (28 edges, 4-regular, bipartite 7+7, connected).
- S = k[x_0,...,x_13], I(G) = (x_a x_b : {a,b} in E(G)).
- reg(S/I) = max{j-i : beta_{i,j}(S/I)!=0}; reg(I) = reg(S/I)+1.
- im(G) = induced matching number.
- Ind(H) = independence complex of H; Hochster's formula:
  beta_{i,j}(S/I(G)) = sum_{|W|=j} dim Htilde_{j-i-1}(Ind(G[W])).

## Result
Over k = QQ:
- reg(S/I(G)) = 3, i.e. reg(I(G)) = 4.
- The bound is extremal on W = {0,1,2,5,6,7,10,11}: G[W] is an induced
  8-cycle 0-1-2-5-6-7-10-11-0 with exactly the 8 edges
  {01,12,25,56,67,7-10,10-11,11-0}, and
  dim_QQ Htilde_2(Ind(G[W]);QQ) = 1
  (exact boundary ranks rk(d1)=7, rk(d2)=13, rk(d3)=2;
  equivalently beta_{5,8}(S/I(G)) >= 1 over QQ).
  The same witness gives Htilde_2 dim 1 at p=32003 and p=10007.
- im(G) = 2 exactly: 98 induced 2-matchings; 0 induced 3- or 4-matchings
  by exhaustive enumeration of C(28,2), C(28,3), C(28,4)
  (independent backtracking confirms max 2, e.g. {(7,8),(12,13)}).
  Hence reg(S/I) = 3 = im(G)+1: the Katzman lower bound is sharp, and the
  extremal witness is a full induced C8 rather than a scattered matching.

## Proof / evidence
1. Graph certificate (replayed): 28 edges listed in scripts; every vertex
   degree 4; BFS 2-colors 7+7, so bipartite 4-regular.
2. Lower bound reg(S/I)>=3 over QQ: for W above, G[W] verified induced C8
   (8 edges, all degrees 2, single-cycle traversal). Independence complex
   of G[W] has face counts (sizes 0..4: 1,8,20,16,2); exact-QQ Fraction
   boundary ranks 1,7,13,2 give dim Htilde_2 = 16-13-2 = 1 != 0.
   By Hochster, beta_{5,8} >= 1, so reg >= 3 over QQ.
3. Upper bound reg(S/I)<=3: exhaustive Hochster scan over all 2^14 subsets
   (339 independent sets) with modular homology at p=32003 and
   independently p=10007: no subset has Htilde_t != 0 with |W'|-i > 3.
   Transfer to QQ: any QQ free class persists mod p (UCT), so vanishing
   over one Fp forces vanishing over QQ for QQ-regularity. Hence
   reg(S/I;QQ) = 3 exactly; reg(I) = 4. Characteristic-free at the
   extremal degree (verified at two primes); full-resolution
   characteristic dependence beyond the extremal class not claimed.
4. Induced-matching census: exhaustive matching + no-cross-edge tests over
   C(28,k) for k=2,3,4 give 98/0/0; second independent backtracking script
   confirms max size 2. Hence im(G)=2 and reg(S/I)=im+1 sharp.

## Limitations
- Powers values undecided: target reg(I^s)=2s+2 (s>=2) and fallback
  reg(I^2)=6 are NOT claimed; reported strand data
  (beta_{1,7}(I^2)=0, beta_{2,8}(I^2)=0 at p=32003; beta_{3,9} enumeration
  incomplete) is evidence only.
- Upper line reg(I^s)<=2s+2 for powers invokes the published Banerjee-Nevo
  bipartite bound (externally cited, not re-proved); combined with im=2
  (Katzman line >=2s+1) it pins each power to {2s+1,2s+2} once cited.
- QQ headline + two-prime extremal verification; full minimal resolution
  characteristic dependence beyond the extremal class not settled.

## Reproducibility
- python3 output/artifacts/verify_emergent.py  # seconds; prints VERIFY_OK
  (graph certs, exhaustive im census, exact-QQ H~_2, C8 check)
- python3 output/artifacts/step2_hochster.py   # full upper-bound scan, two primes
- python3 output/artifacts/step3_qq_H.py       # exact-QQ witness
- python3 output/artifacts/step1b_imcheck.py   # independent im census + matching/girth stats
All scripts use stdlib (+ numpy for modular rank in step2); exact QQ ranks
use Fraction arithmetic, no floating point.

## References
- A. Banerjee, E. Nevo, Regularity of Edge Ideals Via Suspension,
  arXiv:1908.03115 (bipartite upper bound reg(I^s)<=2s+reg(I)-2).
- N. T. Hang, M. H. Pham, T. Vu, Regularity of Powers and symbolic powers
  of edge ideals of cubic circulant graphs, arXiv:2409.20161 (cubic-only;
  C_14(1,3) 4-regular outside scope).
- M. E. Uribe-Paczka, A. Van Tuyl, The regularity of some families of
  circulant graphs, arXiv:1906.06259 (first-power, cubic families).
- A. Banerjee, S. Kara, H. T. Ha, Regularity of Edge Ideals and Their Powers
  (survey), arXiv:1712.00887.
- K. Alilooee, A. Banerjee, Powers of edge ideals of regularity three
  bipartite graphs, arXiv:1408.2557.
