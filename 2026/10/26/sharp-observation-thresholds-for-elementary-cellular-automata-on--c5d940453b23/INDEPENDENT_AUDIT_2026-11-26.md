# Independent mathematical audit

## correctness

PASS

Every legal finite k+2 block extends on both sides by zeros; the support of its k overlapping triples detects precisely when it emits 1^k. Direct finite enumeration reproduced the nine minimal k=4 supports and all 62 and 70 rule sets. The explicit periodic or single-run witnesses retain their support restrictions for every k≥4, so every forbidden mask remains forbidden. Conversely, after deletion of the 111 loop, the simple directed cycles of the pair de Bruijn graph use supports {0}, {1,2,4}, {2,5}, {1,3,4,6}, or {3,5,6}, all excluded. Each remaining path has at most three edges. If 111 is present, a loop-free three-edge path through 11 with fewer than three consecutive ones has word 10011, 00110, 11001, or 01100; the remaining four minimal masks forbidding these paths together with 111 exclude them. Shorter paths through 11 already have at least two ones in one run. Reinstating any 111 repetitions extends that run, so an admissible input never emits 1^k. Independently, `python3 /workspace/review-evidence/independent_finite_checks.py 2` compared direct exact n+2 block images through n=8 with the CSV for k=3,…,8. Every preserving nonshift has an admitted absent word; every remaining code demonstrably is a coordinate projection on legal triples and hence onto. Unused 111 accounts for the duplicate codes only at k=3. For k≥9 all input blocks of length ≤8 and all output words of length ≤6 are legal, so the full-shift enumeration through six applies identically, and its lengths match k=8. The maxima 7,8,5,5,6,6 and the unique two codes reaching eight were confirmed. At k=4 each listed peak word is a shortest witness, not the only witness for its rule: the other ones are 11010111 for rule 26 and 11101011 for rule 82. No higher radius or temporal conclusion is used.

## originality

PASS

The strongest matches cover analogous rigidity on different shifts, general beta-shift dynamics, and full-shift rule statistics, not the exact preserving-rule census and first-step shortest-word obstructions across the bounded-run family. The value and originality are in the combination of uniform preservation and the sharp nonmonotone restricted observation profile, not in the standard de Bruijn set construction.

## value

PASS

Rather than list a sample of rules, the result gives the exact decision horizon for distinguishing proper images from the full admitted language throughout an infinite family. The horizon can increase and then decrease even while the local rule family stays fixed, and the witnessed eight-letter peak shows why a shorter universal observation rule is impossible. The uniform proof and exact finite boundary complement one another.

The dated certificate retains the supplied scientific assessment, sources and limitations.
