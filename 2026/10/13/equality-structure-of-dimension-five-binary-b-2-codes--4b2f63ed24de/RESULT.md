# Equality structure of dimension-five binary \(B_2\)-codes
## Finding
For binary \(B_2\)-codes \(C\subseteq\{0,1\}^5\), where every coordinatewise ordinary sum \(x+y\in\{0,1,2\}^5\) arising from an unordered pair \(\{x,y\}\) with repetition allowed is distinct, the maximum cardinality is \(12\). Exactly \(192\) labeled maximum codes exist. Under the full Hamming-isometry group \((C_2)^5\rtimes S_5\) of order \(3840\), all \(192\) maxima form a single orbit, so every maximum has stabilizer order \(20\). Every maximum is balanced in each coordinate, contains exactly one antipodal pair, and its \(66\) unordered pairs have Hamming-distance distribution \((5,20,30,10,1)\) at distances \(1,2,3,4,5\), respectively.

The numerical optimum \(12\) is already recorded for dimension five in OEIS A309370. The contribution here is the complete equality-layer census and symmetry classification: there are exactly \(192\) labeled maximizers, and they are all Hamming-isometric.

## Assumptions and scope
A binary \(B_2\)-code is a subset \(C\subseteq\{0,1\}^5\) such that the coordinatewise ordinary sums \(x+y\in\{0,1,2\}^5\), taken over unordered pairs with repetition allowed, are all distinct. This is the Sidon-subset formulation for the five-dimensional Boolean cube under ordinary integer-vector addition. Only dimension five is classified here; there is no assertion about larger dimensions or about constant-weight restrictions.

## Proof
For a word \(a\in\{0,1\}^5\), bitwise translation \(x\mapsto x\oplus a\) preserves the \(B_2\) property. In every coordinate flipped by \(a\), a sum digit \(s\in\{0,1,2\}\) is replaced by \(2-s\), while unflipped coordinates are unchanged; hence equality of pair sums is preserved bijectively. Coordinate permutations preserve the property as well.

Therefore every nonempty code is Hamming-isometric to one containing \(00000\). The exhaustive search in `verify.py` fixes \(00000\), adds candidates in increasing binary order, and maintains the exact set of coordinatewise pair sums, including self-pairs. A candidate is admitted precisely when all newly created sums are distinct from the old sums and from one another. Because every increasing subset containing \(00000\) is reached once, this is an exhaustive search over normalized codes, not a heuristic.

The normalized search finds maximum size \(12\) and exactly \(72\) maximum codes containing \(00000\). Translating these \(72\) codes by all \(32\) xor masks and deduplicating gives exactly \(192\) labeled maxima. Completeness follows because translating any maximum by any one of its codewords produces a normalized maximum containing \(00000\).

Applying all \(32\cdot 5!=3840\) Hamming isometries to one maximum gives an orbit of size \(192\), equal to the full census. Thus there is one isometry orbit, and orbit-stabilizer gives stabilizer order \(3840/192=20\). Direct counting on a representative gives six ones in each coordinate, exactly one complementary pair, and Hamming pair counts \(5,20,30,10,1\) at distances \(1,2,3,4,5\). These quantities are invariant under Hamming isometries, so they hold for every maximum.

## Verification
`verify.py` reconstructs the \(32\) binary words, independently encodes all ordinary pair sums in base three, performs the normalized exhaustive search, regenerates all \(192\) labeled maxima, and checks the full Hamming-isometry orbit. It also verifies the balance, antipodal-pair count, and distance distribution. `census.json` contains the complete labeled census. A clean replay prints:

`VERIFY_OK maximum=12 normalized=72 labeled_maxima=192 isometry_orbits=1 orbit_size=192 stabilizer=20 balanced=6,6,6,6,6 antipodal_pairs=1 distances=5,20,30,10,1 census_sha256=97b0e977667667ded6818f50235f665d0477d4ebe38ce4d17fd6e41e44dd755b`

## Relationship to prior work
D'yachkov's survey gives the standard \(B_s\)-code definition, with repeated summands allowed, and identifies the \(s=2\) case with the two-user adder-channel formulation. OEIS A309370 records the exact maximum \(12\) in dimension five and supplies a size-\(12\) example, but does not state a labeled census or an isometry classification. Cohen, Litsyn, and Zemor study asymptotic upper bounds for binary \(B_2\)-sequences, while Sima et al. study the constant-weight version; neither inspected source states the dimension-five equality-layer census above. The previously checked local record for dimension four concerns a different ambient cube and does not imply the dimension-five classification.

## Limitations
The result is a finite exact classification for dimension five only. Its proof depends on exhaustive enumeration, but the search space, pruning invariant, symmetry reduction, and full output census are all explicit and replayable. The literature comparison did not reveal a prior statement of the \(192\)-code count or the single-orbit classification; an obscure finite census outside the inspected sources remains a residual bibliographic risk.

## References
- A. G. D'yachkov, *Lectures on Designing Screening Experiments*, arXiv:1401.7505v1, first publicly posted 2014-01-29. Section 5.1 gives the \(B_s\)-code definition and the \(s=2\) adder-channel connection.
- OEIS A309370, *Maximum size of a Sidon subset of \({0,1}^n\)*.
- G. Cohen, S. Litsyn, G. Zemor, *Binary \(B_2\)-sequences: a new upper bound*, Journal of Combinatorial Theory, Series A 94 (2001), DOI 10.1006/jcta.2000.3127.
- J. Sima, Y. Shomorony, A. A. Heidari, C. Fragouli, *On Constant-Weight Binary \(B_2\)-Sequences*, arXiv:2303.12990.
